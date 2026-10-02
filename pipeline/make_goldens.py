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


def main():
    ap = argparse.ArgumentParser()
    add_release_args(ap)
    ap.add_argument("--golden", default="tests/golden")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    conn = connect(args)
    templates = {t["id"]: t for t in load_templates()}
    for tid, (name, requirement, inputs) in CASES.items():
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
        main_file = next(f for f in files if f.endswith(".java" if language == "java" else ".b"))
        apps = [inputs[s["id"]] for s in template["inputs"] if s.get("kind") == "app"]
        field_ids = [s["id"] for s in template["inputs"] if s.get("kind") == "field"]
        expected = [values[f] for f in field_ids if language != "java" and values[f] in files[main_file]]
        case = {"name": name, "artefact": template["label"], "skill": SKILL[language], "requirement": requirement,
                "apps": apps, "file": main_file, "expected_fields": expected,
                "template": tid, "today": TODAY, "userInputs": inputs}
        (out / "case.json").write_text(json.dumps(case, indent=2) + "\n", encoding="utf-8")
        print(f"wrote  {name}: {', '.join(files)}")


if __name__ == "__main__":
    main()
