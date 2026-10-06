#!/usr/bin/env python3
"""Generate golden cases (tests/golden/<case>/) by rendering each template with
fixed sample inputs against a release DB. Rendering only fills placeholders --
the golden files are then field-checked and compiled by run_golden.py, which is
what makes a template trustworthy. Existing golden cases are left untouched
unless --force.

  python pipeline/make_goldens.py --release R25 [--force]
"""
import argparse
import json
from pathlib import Path

from artefact_templates import load_templates, render, resolve
from releases import add_release_args, connect

TODAY = "2026-10-02"
SKILL = {"infobasic": "temenos-infobasic", "jbc": "temenos-jbc", "java": "temenos-l3"}

COMMON_B = {"DESCRIPTION": "Golden case", "AUTHOR": "golden-case"}
COMMON_LEGACY = {**COMMON_B, "PACKAGE": "GOLDEN.Legacy"}
COMMON_JBC = {**COMMON_B, "PACKAGE": "GOLDEN.Api"}
COMMON_JAVA = {"JAVA_PACKAGE": "com.temenos.t24.custom.golden"}

# template id -> (golden case name, requirement, userInputs)
CASES = {
    "infobasic/vvr": ("infobasic-vvr", "Reject an empty CUSTOMER mnemonic at field level.",
                      {**COMMON_LEGACY, "METHOD_NAME": "vGoldenVvr", "ROUTINE_NAME": "V.GOLDEN.VVR", "APP": "CUSTOMER", "FIELD": "EB.CUS.MNEMONIC",
                       "ERROR_TEXT": "MNEMONIC IS MANDATORY"}),
    "infobasic/vir": ("infobasic-vir", "Reject a CUSTOMER with no sector on input.",
                      {**COMMON_LEGACY, "METHOD_NAME": "vGoldenVir", "ROUTINE_NAME": "V.GOLDEN.VIR", "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR",
                       "ERROR_TEXT": "SECTOR IS MANDATORY"}),
    "infobasic/var": ("infobasic-var", "On FT authorisation, stop if the debit account has no category.",
                      {**COMMON_LEGACY, "METHOD_NAME": "vGoldenVar", "ROUTINE_NAME": "V.GOLDEN.VAR", "APP": "FUNDS.TRANSFER", "FIELD": "FT.DEBIT.ACCT.NO",
                       "LINK_APP": "ACCOUNT", "LINK_FIELD": "AC.CATEGORY", "ERROR_TEXT": "DEBIT ACCOUNT HAS NO CATEGORY"}),
    "infobasic/nofile": ("infobasic-nofile", "List CUSTOMER ids for a sector.",
                         {**COMMON_LEGACY, "METHOD_NAME": "eGoldenNofile", "ROUTINE_NAME": "E.GOLDEN.NOFILE", "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}),
    "infobasic/ofs-routine": ("infobasic-ofs-routine", "Set a CUSTOMER's sector through OFS.",
                              {**COMMON_LEGACY, "METHOD_NAME": "goldenOfsUpdate", "ROUTINE_NAME": "GOLDEN.OFS.UPDATE", "APP": "CUSTOMER",
                               "VERSION_NAME": "GOLDEN.OFS", "FIELD": "EB.CUS.SECTOR", "OFS_SOURCE": "TEST.OFS"}),
    "jbc/get-api": ("jbc-get-api", "Return a CUSTOMER's sector.",
                    {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.GET.SECTOR", "METHOD_NAME": "getSector",
                     "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}),
    "jbc/write-api": ("jbc-write-api", "Set a CUSTOMER's sector through OFS.",
                      {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.SET.SECTOR", "METHOD_NAME": "setSector",
                       "APP": "CUSTOMER", "VERSION_NAME": "GOLDEN.OFS", "FIELD": "EB.CUS.SECTOR", "OFS_SOURCE": "TEST.OFS"}),
    "jbc/nofile": ("jbc-nofile", "List CUSTOMER ids for a sector.",
                   {**COMMON_JBC, "ROUTINE_NAME": "E.GOLDEN.JBC.NOFILE", "METHOD_NAME": "listBySector",
                    "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}),
    "java/record-lifecycle-check-id": ("java-record-lifecycle-check-id", "Prefix CUSTOMER ids with SMP.",
                                       {**COMMON_JAVA, "CLASS_NAME": "GoldenCheckId", "APP": "CUSTOMER", "ID_PREFIX": "SMP"}),
    "java/record-lifecycle-default": ("java-record-lifecycle-default", "Default an empty CUSTOMER sector to 1001.",
                                      {**COMMON_JAVA, "CLASS_NAME": "GoldenDefault", "APP": "CUSTOMER",
                                       "FIELD": "EB.CUS.SECTOR", "DEFAULT_VALUE": "1001"}),
    "java/record-lifecycle-hot-field": ("java-record-lifecycle-hot-field", "When SECTOR changes, set MNEMONIC.",
                                        {**COMMON_JAVA, "CLASS_NAME": "GoldenHotField", "APP": "CUSTOMER",
                                         "FIELD": "EB.CUS.SECTOR", "TARGET_FIELD": "EB.CUS.MNEMONIC", "DEFAULT_VALUE": "SAMPLE"}),
    "java/record-lifecycle-validate-field": ("java-record-lifecycle-validate-field", "Reject an empty sector (deprecated hook).",
                                             {**COMMON_JAVA, "CLASS_NAME": "GoldenValidateField", "APP": "CUSTOMER",
                                              "FIELD": "EB.CUS.SECTOR", "ERROR_TEXT": "SECTOR IS MANDATORY"}),
    "java/record-lifecycle-update": ("java-record-lifecycle-update", "Update the debit ACCOUNT in the same commit.",
                                     {**COMMON_JAVA, "CLASS_NAME": "GoldenUpdateRecord", "APP": "FUNDS.TRANSFER",
                                      "FIELD": "FT.DEBIT.ACCT.NO", "TARGET_APP": "ACCOUNT", "TARGET_VERSION": "GOLDEN.UPDATE",
                                      "TARGET_FIELD": "AC.CATEGORY", "TARGET_VALUE": "1001"}),
    "java/record-lifecycle-post-update": ("java-record-lifecycle-post-update", "After authorisation, update the debit ACCOUNT via OFS.",
                                          {**COMMON_JAVA, "CLASS_NAME": "GoldenPostUpdate", "APP": "FUNDS.TRANSFER",
                                           "FIELD": "FT.DEBIT.ACCT.NO", "TARGET_APP": "ACCOUNT", "TARGET_VERSION": "GOLDEN.UPDATE",
                                           "TARGET_FIELD": "AC.CATEGORY", "TARGET_VALUE": "1001", "OFS_SOURCE": "TEST.OFS"}),
    "java/record-lifecycle-override-auto-approve": ("java-record-lifecycle-override-auto-approve", "Auto-approve one override.",
                                                    {**COMMON_JAVA, "CLASS_NAME": "GoldenOverride", "APP": "FUNDS.TRANSFER",
                                                     "OVERRIDE_ID": "SAMPLE.OVERRIDE"}),
    "java/service-lifecycle": ("java-service-lifecycle", "Process CUSTOMERs of sector 1001 in a service.",
                               {**COMMON_JAVA, "CLASS_NAME": "GoldenService", "APP": "CUSTOMER",
                                "FIELD": "EB.CUS.SECTOR", "SELECT_VALUE": "1001"}),
    "java/enquiry-nofile": ("java-enquiry-nofile", "List CUSTOMER ids for a sector.",
                            {**COMMON_JAVA, "CLASS_NAME": "GoldenNofile", "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}),
    "java/enquiry-build": ("java-enquiry-build", "Restrict an enquiry to sector 1001.",
                           {**COMMON_JAVA, "CLASS_NAME": "GoldenBuild", "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR",
                            "FILTER_VALUE": "1001"}),
    "java/enquiry-conversion": ("java-enquiry-conversion", "Show NOT SET for empty values.",
                                {**COMMON_JAVA, "CLASS_NAME": "GoldenConversion", "APP": "CUSTOMER", "EMPTY_TEXT": "NOT SET"}),
    "java/activity-lifecycle-validate": ("java-activity-lifecycle-validate", "Reject an AA activity with no effective date.",
                                         {**COMMON_JAVA, "CLASS_NAME": "GoldenActivityCheck", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                          "FIELD": "AA.ARR.ACT.EFFECTIVE.DATE", "ERROR_TEXT": "EFFECTIVE DATE IS MANDATORY"}),
    "java/aa-calculation-charge": ("java-aa-calculation-charge", "Charge 1.5% of the base amount, minimum 10.",
                                   {**COMMON_JAVA, "CLASS_NAME": "GoldenChargeCalc", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                    "RATE_PERCENT": "1.5", "MIN_CHARGE": "10"}),
    "java/payment-lifecycle-validate-clearing": ("java-payment-lifecycle-validate-clearing", "Reject a payment with no credit party.",
                                                 {**COMMON_JAVA, "CLASS_NAME": "GoldenClearingCheck", "APP": "POR.TRANSACTION",
                                                  "ERROR_CODE": "AC01", "ERROR_TEXT": "CREDIT PARTY MISSING"}),
    "java/payment-order-validate": ("java-payment-order-validate", "Reject a PAYMENT.ORDER with no debit account.",
                                    {**COMMON_JAVA, "CLASS_NAME": "GoldenPaymentOrderCheck", "APP": "PAYMENT.ORDER",
                                     "FIELD": "PO.DEBIT.ACCOUNT", "ERROR_TEXT": "DEBIT ACCOUNT IS MANDATORY"}),
}

# Added 2026-10-06; all compile on R25 (run_golden.py --release R25, 2026-10-06).
CASES.update({
    "infobasic/id-routine": ("infobasic-id-routine", "Reject a CUSTOMER id without the SMP prefix.",
                             {**COMMON_LEGACY, "METHOD_NAME": "vGoldenIdRtn", "ROUTINE_NAME": "V.GOLDEN.ID.RTN", "APP": "CUSTOMER",
                              "ID_PREFIX": "SMP", "ERROR_TEXT": "ID MUST START WITH SMP"}),
    "infobasic/check-record": ("infobasic-check-record", "Default an empty CUSTOMER sector to 1001.",
                               {**COMMON_LEGACY, "METHOD_NAME": "vGoldenCheckRec", "ROUTINE_NAME": "V.GOLDEN.CHECK.REC", "APP": "CUSTOMER",
                                "FIELD": "EB.CUS.SECTOR", "DEFAULT_VALUE": "1001"}),
    "infobasic/auto-field": ("infobasic-auto-field", "Fill the FT debit currency from the debit account.",
                             {**COMMON_LEGACY, "METHOD_NAME": "vGoldenAutoField", "ROUTINE_NAME": "V.GOLDEN.AUTO.FIELD", "APP": "FUNDS.TRANSFER",
                              "FIELD": "FT.DEBIT.ACCT.NO", "LINK_APP": "ACCOUNT", "LINK_FIELD": "AC.CURRENCY", "TARGET_FIELD": "FT.DEBIT.CURRENCY"}),
    "infobasic/before-auth": ("infobasic-before-auth", "Set the CUSTOMER mnemonic before authorisation.",
                              {**COMMON_LEGACY, "METHOD_NAME": "vGoldenBeforeAuth", "ROUTINE_NAME": "V.GOLDEN.BEFORE.AUTH", "APP": "CUSTOMER",
                               "FIELD": "EB.CUS.MNEMONIC", "FIELD_VALUE": "SAMPLE"}),
    "infobasic/after-unau": ("infobasic-after-unau", "Log the CUSTOMER sector after input.",
                             {**COMMON_LEGACY, "METHOD_NAME": "vGoldenAfterUnau", "ROUTINE_NAME": "V.GOLDEN.AFTER.UNAU", "APP": "CUSTOMER",
                              "FIELD": "EB.CUS.SECTOR", "LOG_FILE": "SAMPLE.AUDIT.LOG"}),
    "infobasic/auth-routine": ("infobasic-auth-routine", "Log the CUSTOMER sector after authorisation.",
                               {**COMMON_LEGACY, "METHOD_NAME": "vGoldenAuthRtn", "ROUTINE_NAME": "V.GOLDEN.AUTH.RTN", "APP": "CUSTOMER",
                                "FIELD": "EB.CUS.SECTOR", "LOG_FILE": "SAMPLE.AUDIT.LOG"}),
    "infobasic/enquiry-conversion": ("infobasic-enquiry-conversion", "Show the sector of a CUSTOMER id.",
                                     {**COMMON_LEGACY, "METHOD_NAME": "eGoldenConv", "ROUTINE_NAME": "E.GOLDEN.CONV", "APP": "CUSTOMER",
                                      "FIELD": "EB.CUS.SECTOR"}),
    "infobasic/enquiry-build": ("infobasic-enquiry-build", "Restrict an enquiry to sector 1001.",
                                {**COMMON_LEGACY, "METHOD_NAME": "eGoldenBuild", "ROUTINE_NAME": "E.GOLDEN.BUILD", "APP": "CUSTOMER",
                                 "FIELD": "EB.CUS.SECTOR", "FILTER_VALUE": "1001"}),
    "infobasic/cob-service": ("infobasic-cob-service", "Process CUSTOMERs of sector 1001 in a COB job.",
                              {**COMMON_LEGACY, "METHOD_NAME": "bGoldenService", "ROUTINE_NAME": "B.GOLDEN.SERVICE", "APP": "CUSTOMER",
                               "FIELD": "EB.CUS.SECTOR", "SELECT_VALUE": "1001"}),
    "infobasic/de-conversion": ("infobasic-de-conversion", "Print an account currency on an advice.",
                                {**COMMON_LEGACY, "METHOD_NAME": "deGoldenConv", "ROUTINE_NAME": "GOLDEN.DE.CONV", "APP": "ACCOUNT",
                                 "FIELD": "AC.CURRENCY"}),
    "infobasic/aa-calculation": ("infobasic-aa-calculation", "1.5% of the base amount, minimum 10.",
                                 {**COMMON_LEGACY, "METHOD_NAME": "aaGoldenCalc", "ROUTINE_NAME": "GOLDEN.AA.CALC", "APP": "AA.ARRANGEMENT",
                                  "RATE_PERCENT": "1.5", "MIN_AMOUNT": "10"}),
    "infobasic/aa-getter": ("infobasic-aa-getter", "Return the status of an arrangement.",
                            {**COMMON_LEGACY, "METHOD_NAME": "aaGoldenGetStatus", "ROUTINE_NAME": "GOLDEN.AA.GET.STATUS", "APP": "AA.ARRANGEMENT",
                             "FIELD": "AA.ARR.ARR.STATUS"}),
    "infobasic/batch-program": ("infobasic-batch-program", "Count CUSTOMERs of sector 1001.",
                                {**COMMON_B, "ROUTINE_NAME": "GOLDEN.COUNT.SECTOR", "APP": "CUSTOMER",
                                 "FIELD": "EB.CUS.SECTOR", "SELECT_VALUE": "1001"}),
    "infobasic/local-table": ("infobasic-local-table", "Define a sample parameter table.",
                              {**COMMON_LEGACY, "METHOD_NAME": "goldenParameter", "TABLE_NAME": "GOLDEN.PARAMETER", "TITLE": "Golden parameter", "PRODUCT": "EB",
                               "EQUATE_PREFIX": "GOLDEN.PRM", "ID_LENGTH": "20", "FIELD_NAME": "DESCRIPTION", "FIELD_LENGTH": "35"}),
    "jbc/id-routine": ("jbc-id-routine", "Reject a CUSTOMER id without the SMP prefix.",
                       {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.ID.RTN", "METHOD_NAME": "checkId", "APP": "CUSTOMER",
                        "ID_PREFIX": "SMP", "ERROR_TEXT": "ID MUST START WITH SMP"}),
    "jbc/input-routine": ("jbc-input-routine", "Reject a CUSTOMER with no sector on commit.",
                          {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.INPUT.RTN", "METHOD_NAME": "checkInput", "APP": "CUSTOMER",
                           "FIELD": "EB.CUS.SECTOR", "ERROR_TEXT": "SECTOR IS MANDATORY"}),
    "jbc/check-record": ("jbc-check-record", "Default an empty CUSTOMER sector to 1001.",
                         {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.CHECK.REC", "METHOD_NAME": "checkRecord", "APP": "CUSTOMER",
                          "FIELD": "EB.CUS.SECTOR", "DEFAULT_VALUE": "1001"}),
    "jbc/before-auth": ("jbc-before-auth", "Set the CUSTOMER mnemonic before authorisation.",
                        {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.BEFORE.AUTH", "METHOD_NAME": "beforeAuth", "APP": "CUSTOMER",
                         "FIELD": "EB.CUS.MNEMONIC", "FIELD_VALUE": "SAMPLE"}),
    "jbc/enquiry-conversion": ("jbc-enquiry-conversion", "Show the sector of a CUSTOMER id.",
                               {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.E.CONV", "METHOD_NAME": "convSector", "APP": "CUSTOMER",
                                "FIELD": "EB.CUS.SECTOR"}),
    "jbc/enquiry-build": ("jbc-enquiry-build", "Restrict an enquiry to sector 1001.",
                          {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.E.BUILD", "METHOD_NAME": "buildSector", "APP": "CUSTOMER",
                           "FIELD": "EB.CUS.SECTOR", "FILTER_VALUE": "1001"}),
    "jbc/query-api": ("jbc-query-api", "List CUSTOMER id and mnemonic for a sector.",
                      {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.QUERY.SECTOR", "METHOD_NAME": "querySector", "APP": "CUSTOMER",
                       "FIELD": "EB.CUS.SECTOR", "RETURN_FIELD": "EB.CUS.MNEMONIC"}),
    "jbc/de-conversion": ("jbc-de-conversion", "Print an account currency on an advice.",
                          {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.DE.CONV.JBC", "METHOD_NAME": "deCurrency", "APP": "ACCOUNT",
                           "FIELD": "AC.CURRENCY"}),
    "jbc/cob-service": ("jbc-cob-service", "Process CUSTOMERs of sector 1001 in a COB job.",
                        {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.JBC.SERVICE", "METHOD_NAME": "goldenService", "APP": "CUSTOMER",
                         "FIELD": "EB.CUS.SECTOR", "SELECT_VALUE": "1001"}),
    "jbc/package-initialise": ("jbc-package-initialise", "Initialise a standalone T24 session.",
                               {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.INITIALISE", "METHOD_NAME": "initialise",
                                "OFS_SOURCE": "TEST.OFS", "COMPANY_ID": "GB0010001"}),
    "jbc/complex-get": ("jbc-complex-get", "Return the sector of a CUSTOMER as a typed object.",
                        {**COMMON_JBC, "ROUTINE_NAME": "GOLDEN.GET.TYPED", "METHOD_NAME": "getTyped", "COMPLEX_NAME": "GoldenApi",
                         "TYPE_NAME": "GoldenRecord", "APP": "CUSTOMER", "FIELD": "EB.CUS.SECTOR"}),
    "jbc/local-table": ("jbc-local-table", "Define a sample parameter table.",
                        {**COMMON_JBC, "METHOD_NAME": "goldenParameter", "TABLE_NAME": "GOLDEN.JBC.PARAMETER", "TITLE": "Golden parameter",
                         "PRODUCT": "EB", "EQUATE_PREFIX": "GOLDEN.JPRM", "ID_LENGTH": "20", "FIELD_NAME": "DESCRIPTION", "FIELD_LENGTH": "35"}),
    "java/record-lifecycle-update-core": ("java-record-lifecycle-update-core", "Set the mnemonic before authorisation.",
                                          {**COMMON_JAVA, "CLASS_NAME": "GoldenUpdateCore", "APP": "CUSTOMER",
                                           "FIELD": "EB.CUS.MNEMONIC", "FIELD_VALUE": "SAMPLE"}),
    "java/activity-lifecycle-default": ("java-activity-lifecycle-default", "Default the AA activity name.",
                                        {**COMMON_JAVA, "CLASS_NAME": "GoldenActivityDefault", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                         "FIELD": "AA.ARR.ACT.ACTIVITY", "DEFAULT_VALUE": "SAMPLE"}),
    "java/activity-lifecycle-post-update": ("java-activity-lifecycle-post-update", "After an authorised activity, update an ACCOUNT.",
                                            {**COMMON_JAVA, "CLASS_NAME": "GoldenActivityPost", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                             "TARGET_APP": "ACCOUNT", "TARGET_VERSION": "GOLDEN.UPDATE", "TARGET_ID": "SAMPLE.ID",
                                             "TARGET_FIELD": "AC.CATEGORY", "TARGET_VALUE": "1001", "OFS_SOURCE": "TEST.OFS"}),
    "java/activity-lifecycle-lookup": ("java-activity-lifecycle-lookup", "Index arrangements under a key.",
                                       {**COMMON_JAVA, "CLASS_NAME": "GoldenActivityLookup", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                        "LOOKUP_TABLE": "SAMPLE.ARRANGEMENT.LIST", "LOOKUP_KEY": "SAMPLE.KEY"}),
    "java/activity-lifecycle-secondary": ("java-activity-lifecycle-secondary", "Trigger a secondary activity.",
                                          {**COMMON_JAVA, "CLASS_NAME": "GoldenSecondary", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                           "SECONDARY_ACTIVITY": "ACCOUNTS-UPDATE-ARRANGEMENT"}),
    "java/aa-calculation-payment": ("java-aa-calculation-payment", "Fixed instalment of 100.",
                                    {**COMMON_JAVA, "CLASS_NAME": "GoldenPaymentCalc", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                     "PAYMENT_AMOUNT": "100"}),
    "java/aa-calculation-adjusted-charge": ("java-aa-calculation-adjusted-charge", "Waive half the charge.",
                                            {**COMMON_JAVA, "CLASS_NAME": "GoldenChargeWaiver", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                             "WAIVE_PERCENT": "50", "REASON": "SAMPLE WAIVER"}),
    "java/aa-calculation-interest-rate": ("java-aa-calculation-interest-rate", "Custom rate of 5.25.",
                                          {**COMMON_JAVA, "CLASS_NAME": "GoldenInterestRate", "APP": "AA.ARRANGEMENT.ACTIVITY",
                                           "RATE": "5.25"}),
})

# Cases rendered and field-checked but not yet compiled on a T24 install: they export with
# "compiled": false until run_golden.py passes on R25 and they move into CASES.
CASES_NOT_COMPILED = {}


def main():
    ap = argparse.ArgumentParser()
    add_release_args(ap)
    ap.add_argument("--golden", default="tests/golden")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    conn = connect(args)
    templates = {t["id"]: t for t in load_templates()}
    for tid, (name, requirement, inputs) in {**CASES, **CASES_NOT_COMPILED}.items():
        out = Path(args.golden) / name
        if out.exists() and not args.force:
            print(f"skip   {name} (exists)")
            continue
        template = templates[tid]
        values = resolve(template, inputs, conn, TODAY)
        files = render(template, values)
        out.mkdir(parents=True, exist_ok=True)
        for fname, content in files.items():
            (out / fname).write_text(content, encoding="utf-8")
        language = template["language"]
        apps = [inputs[s["id"]] for s in template["inputs"] if s.get("kind") == "app"]
        field_ids = [s["id"] for s in template["inputs"] if s.get("kind") == "field"]
        # A template with several routines (a COB service) is checked on the one that uses the most fields.
        sources = [f for f in files if f.endswith(".java" if language == "java" else ".b")]
        main_file = max(sources, key=lambda f: sum(values[i] in files[f] for i in field_ids))
        expected = [values[f] for f in field_ids if language != "java" and values[f] in files[main_file]]
        case = {"name": name, "artefact": template["label"], "skill": SKILL[language], "requirement": requirement,
                "apps": apps, "file": main_file, "expected_fields": expected,
                "template": tid, "today": TODAY, "userInputs": inputs}
        if tid in CASES_NOT_COMPILED:
            case["compiled"] = False
        (out / "case.json").write_text(json.dumps(case, indent=2) + "\n", encoding="utf-8")
        print(f"wrote  {name}: {', '.join(files)}")


if __name__ == "__main__":
    main()
