# PP.BATCH.SUSPENSE.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.PP.BATCH.SUSPENSE.ACCOUNT` in `PP_BatchServerService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BSA.CompanyID` | `PpBatchSuspenseAccount_Companyid` | TField |  | Indicates the FIN company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FIN Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.BSA.SuspenseAccountCompanyID` | `PpBatchSuspenseAccount_Suspenseaccountcompanyid` | TField |  | Specifies the ID of the company to which the internal suspense account belongs to. It is NOINPUT field. On click of validate button, it gets autopopulated from FIN Company. Validation Rules: 3 alphanumeric characters. |
| 3 | `PP.BSA.SuspenseAccount` | `PpBatchSuspenseAccount_Suspenseaccount` | TField | Yes | Specifies the account number of the internal suspense account. The value will be validated by DDA system, used by the payments hub. Validation Rules: Mandatory field. This field can hold upto 35 characters of type 'ACCA'. |
| 4 | `PP.BSA.SuspenseAccountCurrency` | `PpBatchSuspenseAccount_Suspenseaccountcurrency` | TField |  | Specifies the currency of the internal suspense account. It is NOINPUT field. On click of validate button, it gets autopopulated with the CurrencyCode value. Validation Rules: 3 alphanumeric characters. |
| 5 | `PP.BSA.SuspenseAccountNumberContra` | `PpBatchSuspenseAccount_Suspenseaccountnumbercontra` | TField |  | This field will hold the internal suspense account number which will get credited for Post-settle clearing. |
| 6 | `PP.BSA.SuspenseAccNumberContraCcy` | `PpBatchSuspenseAccount_Suspenseaccnumbercontraccy` | TField |  | This field will be populated with the internal suspense account number currency. Should be no change field and populated based on Clearing Currency. |
| 7 | `PP.BSA.SuspenseAccNumberContraCmpy` | `PpBatchSuspenseAccount_Suspenseaccnumbercontracmpy` | TField |  | This field will be populated with the Company of internal suspense account number. Should be no change field and populated based on Clearing Company. |
| 8 | `PP.BSA.RESERVED.2` | `PpBatchSuspenseAccount_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.BSA.RESERVED.1` | `PpBatchSuspenseAccount_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.BSA.LOCAL.REF` | `PpBatchSuspenseAccount_LocalRef` |  |  |  |
| 11 | `PP.BSA.OVERRIDE` | `PpBatchSuspenseAccount_Override` |  |  |  |
| 12 | `PP.BSA.RECORD.STATUS` | `PpBatchSuspenseAccount_RecordStatus` | String |  |  |
| 13 | `PP.BSA.CURR.NO` | `PpBatchSuspenseAccount_CurrNo` | String |  |  |
| 14 | `PP.BSA.INPUTTER` | `PpBatchSuspenseAccount_Inputter` |  |  |  |
| 15 | `PP.BSA.DATE.TIME` | `PpBatchSuspenseAccount_DateTime` |  |  |  |
| 16 | `PP.BSA.AUTHORISER` | `PpBatchSuspenseAccount_Authoriser` | String |  |  |
| 17 | `PP.BSA.CO.CODE` | `PpBatchSuspenseAccount_CoCode` | String |  |  |
| 18 | `PP.BSA.DEPT.CODE` | `PpBatchSuspenseAccount_DeptCode` | String |  |  |
| 19 | `PP.BSA.AUDITOR.CODE` | `PpBatchSuspenseAccount_AuditorCode` | String |  |  |
| 20 | `PP.BSA.AUDIT.DATE.TIME` | `PpBatchSuspenseAccount_AuditDateTime` | String |  |  |
