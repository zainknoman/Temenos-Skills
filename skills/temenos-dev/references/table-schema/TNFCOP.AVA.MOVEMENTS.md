# TNFCOP.AVA.MOVEMENTS — Table Schema

> Source: `INSERTS/I_F.TNFCOP.AVA.MOVEMENTS` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.AVA.MOVEMENTS.BANK.CODE.REPORT` | `TnfcopAvaMovements_BankCodeReport` | TField |  | Used to hold the BANK.CODE.REPORT value from TNFCOP.FOREX.PARAM. |
| 2 | `TNFCOP.AVA.MOVEMENTS.BRANCH.CODE` | `TnfcopAvaMovementsBranchCode` |  |  |  |
| 3 | `TNFCOP.AVA.MOVEMENTS.REPORTING.PERIOD` | `TnfcopAvaMovements_ReportingPeriod` | TField |  | Field to have the Month and year on which the report has been generated. |
| 4 | `TNFCOP.AVA.MOVEMENTS.AVA.HOLDER.TYPE` | `TnfcopAvaMovementsAvaHolderType` |  |  |  |
| 5 | `TNFCOP.AVA.MOVEMENTS.LEGAL.ID` | `TnfcopAvaMovements_LegalId` | TField |  | Field to have the Legal Ids of the Beneficiary customers. |
| 6 | `TNFCOP.AVA.MOVEMENTS.NAME.1` | `TnfcopAvaMovements_Name.1` |  |  |  |
| 7 | `TNFCOP.AVA.MOVEMENTS.ADDRESS` | `TnfcopAvaMovements_Address` | TField |  | To hold the address like Street, Address, Town Country, and post code of the AVA customer. |
| 8 | `TNFCOP.AVA.MOVEMENTS.TELEPHONE.NUMBER` | `TnfcopAvaMovements_TelephoneNumber` | TField |  | This field holds the first 8 digits of the Customer's phone number (OFF.PHONE field). |
| 9 | `TNFCOP.AVA.MOVEMENTS.FAX.NUMBER` | `TnfcopAvaMovements_FaxNumber` | TField |  | Holds the value from the field FAX.1 from CUSTOMER application. |
| 10 | `TNFCOP.AVA.MOVEMENTS.RECORD.TYPE.ENTITY` | `TnfcopAvaMovements_RecordTypeEntity` |  |  |  |
| 11 | `TNFCOP.AVA.MOVEMENTS.AVA.RECORD.ID` | `TnfcopAvaMovements_RecordId` |  |  |  |
| 12 | `TNFCOP.AVA.MOVEMENTS.AVA.TYPE` | `TnfcopAvaMovements_AvaType` |  |  |  |
| 13 | `TNFCOP.AVA.MOVEMENTS.OPENING.DATE` | `TnfcopAvaMovements_OpeningDate` |  |  |  |
| 14 | `TNFCOP.AVA.MOVEMENTS.ACTIVITY` | `TnfcopAvaMovements_Activity` |  |  |  |
| 15 | `TNFCOP.AVA.MOVEMENTS.AUTH.NUM.CBT` | `TnfcopAvaMovements_AuthNumCbt` |  |  |  |
| 16 | `TNFCOP.AVA.MOVEMENTS.AUTH.DATE.CBT` | `TnfcopAvaMovements_AuthDateCbt` |  |  |  |
| 17 | `TNFCOP.AVA.MOVEMENTS.CLOSURE.DATE` | `TnfcopAvaMovements_ClosureDate` |  |  |  |
| 18 | `TNFCOP.AVA.MOVEMENTS.RECORD.TYPE.MOVEMENTS` | `TnfcopAvaMovements_TypeMovement` |  |  |  |
| 19 | `TNFCOP.AVA.MOVEMENTS.OTHER.INFO` | `TnfcopAvaMovements_OtherInfo` |  |  |  |
| 20 | `TNFCOP.AVA.MOVEMENTS.AUTH.AMT.CBT` | `TnfcopAvaMovements_AuthAmtCbt` |  |  |  |
| 21 | `TNFCOP.AVA.MOVEMENTS.INC.DEC.DATE` | `TnfcopAvaMovements_IncDecDate` |  |  |  |
| 22 | `TNFCOP.AVA.MOVEMENTS.INC.DEC.AMT` | `TnfcopAvaMovements_IncDecAmt` |  |  |  |
| 23 | `TNFCOP.AVA.MOVEMENTS.OPERATION.CODE` | `TnfcopAvaMovements_OperationCode` |  |  |  |
| 24 | `TNFCOP.AVA.MOVEMENTS.ORIGIN.OF.FUNDS` | `TnfcopAvaMovements_OriginOfFunds` |  |  |  |
| 25 | `TNFCOP.AVA.MOVEMENTS.COUNTRY` | `TnfcopAvaMovements_Country` |  |  |  |
| 26 | `TNFCOP.AVA.MOVEMENTS.BENEFICIARY.CODE` | `TnfcopAvaMovements_BeneficiaryCode` |  |  |  |
| 27 | `TNFCOP.AVA.MOVEMENTS.BENEFICIARY.LEGAL.ID` | `TnfcopAvaMovements_BeneficiaryLegalId` |  |  |  |
| 28 | `TNFCOP.AVA.MOVEMENTS.BENEFICIARY.NAME` | `TnfcopAvaMovements_BeneficiaryName` |  |  |  |
| 29 | `TNFCOP.AVA.MOVEMENTS.EXPORT.REVENUE` | `TnfcopAvaMovements_ExportRevenue` |  |  |  |
| 30 | `TNFCOP.AVA.MOVEMENTS.ELIGIBLE.AMT` | `TnfcopAvaMovements_EligibleAmt` |  |  |  |
| 31 | `TNFCOP.AVA.MOVEMENTS.CUMULATIVE.USED.AMT` | `TnfcopAvaMovements_CumulativeUsedAmt` |  |  |  |
| 32 | `TNFCOP.AVA.MOVEMENTS.REGENERATE.FILE` | `TnfcopAvaMovements_RegenerateFile` | TField |  | Populated as 'N' during report generation and 'Y' during re-generation. |
| 33 | `TNFCOP.AVA.MOVEMENTS.CUSTOMER.ACCOUNT` | `TnfcopAvaMovements_CustomerAccount` |  |  |  |
