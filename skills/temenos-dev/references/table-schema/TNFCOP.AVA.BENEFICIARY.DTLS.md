# TNFCOP.AVA.BENEFICIARY.DTLS — Table Schema

> Source: `INSERTS/I_F.TNFCOP.AVA.BENEFICIARY.DTLS` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.AVA.BENEFICIARY.DTLS.BANK.CODE.REPORT` | `TnfcopAvaBeneficiaryDtls_BankCodeReport` | TField |  | Used to hold the BANK.CODE.REPORT value from TNFCOP.FOREX.PARAM |
| 2 | `TNFCOP.AVA.BENEFICIARY.DTLS.BRANCH.CODE` | `TnfcopAvaBeneficiaryDtls_BranchCode` | TField |  |  |
| 3 | `TNFCOP.AVA.BENEFICIARY.DTLS.OTHER.INFO` | `TnfcopAvaBeneficiaryDtls_OtherInfo` |  |  |  |
| 4 | `TNFCOP.AVA.BENEFICIARY.DTLS.LEGAL.ID` | `TnfcopAvaBeneficiaryDtls_LegalId` |  |  |  |
| 5 | `TNFCOP.AVA.BENEFICIARY.DTLS.AVA.ID` | `TnfcopAvaBeneficiaryDtlsAvaId` |  |  |  |
| 6 | `TNFCOP.AVA.BENEFICIARY.DTLS.BUSINESS.TYPE` | `TnfcopAvaBeneficiaryDtls_BusinessType` |  |  |  |
| 7 | `TNFCOP.AVA.BENEFICIARY.DTLS.OPENING.DATE` | `TnfcopAvaBeneficiaryDtls_OpeningDate` |  |  |  |
| 8 | `TNFCOP.AVA.BENEFICIARY.DTLS.BENEFICIARY.ID` | `TnfcopAvaBeneficiaryDtls_BeneficiaryId` |  |  |  |
| 9 | `TNFCOP.AVA.BENEFICIARY.DTLS.BENEFICIARY.CODE` | `TnfcopAvaBeneficiaryDtls_BeneficiaryCode` |  |  |  |
| 10 | `TNFCOP.AVA.BENEFICIARY.DTLS.BENEFICIARY.LEGAL.ID` | `TnfcopAvaBeneficiaryDtls_BeneficiaryLegalId` |  |  |  |
| 11 | `TNFCOP.AVA.BENEFICIARY.DTLS.NAME.1` | `TnfcopAvaBeneficiaryDtls_Name.1` |  |  |  |
| 12 | `TNFCOP.AVA.BENEFICIARY.DTLS.ROLE` | `TnfcopAvaBeneficiaryDtls_Role` |  |  |  |
| 13 | `TNFCOP.AVA.BENEFICIARY.DTLS.BENE.UPDATE.DATE` | `TnfcopAvaBeneficiaryDtls_BeneUpdateDate` |  |  |  |
| 14 | `TNFCOP.AVA.BENEFICIARY.DTLS.BENE.UPDATE.CODE` | `TnfcopAvaBeneficiaryDtls_BeneUpdateCode` |  |  |  |
| 15 | `TNFCOP.AVA.BENEFICIARY.DTLS.REGENERATE.FILE` | `TnfcopAvaBeneficiaryDtls_RegenerateFile` | TField |  | Populated as 'N' during report generation and 'Y' during re-generation. |
| 16 | `TNFCOP.AVA.BENEFICIARY.DTLS.CUSTOMER.ACCOUNT` | `TnfcopAvaBeneficiaryDtls_CustomerAccount` |  |  |  |
