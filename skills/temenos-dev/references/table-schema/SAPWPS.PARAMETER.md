# SAPWPS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SAPWPS.PARAMETER` in `SAPWPS_WagesProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAPWPS.DESCRIPTION` | `SapwpsParameter_Description` | TField |  | Description of the id Record. Allowed length 35 characters. |
| 2 | `SAPWPS.FILE.NAME.SUFFIX` | `SapwpsParameter_FileNameSuffix` |  |  |  |
| 3 | `SAPWPS.FILE.TYPE` | `SapwpsParameter_FileType` |  |  |  |
| 4 | `SAPWPS.DEBIT.ACCOUNT.NUMBER` | `SapwpsParameter_DebitAccountNumber` |  |  |  |
| 5 | `SAPWPS.CREDIT.ACCOUNT.NUMBER` | `SapwpsParameter_CreditAccountNumber` |  |  |  |
| 6 | `SAPWPS.CHARGES` | `SapwpsParameter_Charges` |  |  |  |
| 7 | `SAPWPS.WAIVE.CHARGES` | `SapwpsParameter_WaiveCharges` |  |  |  |
| 8 | `SAPWPS.LENGTH.EMPLOYER.ID` | `SapwpsParameter_LengthEmployerId` | TField |  | This field is to hold the length of the employer id as instructed by the regulatory in the region. Must be numeric. |
| 9 | `SAPWPS.RESERVED.1` | `SapwpsParameter_Reserved1` | TField |  | This field is reserved for future use |
| 10 | `SAPWPS.RESERVED.2` | `SapwpsParameter_Reserved2` | TField |  | This field is reserved for future use |
| 11 | `SAPWPS.RESERVED.3` | `SapwpsParameter_Reserved3` | TField |  | This field is reserved for future use |
| 12 | `SAPWPS.RESERVED.4` | `SapwpsParameter_Reserved4` | TField |  | This field is reserved for future use |
| 13 | `SAPWPS.RESERVED.5` | `SapwpsParameter_Reserved5` | TField |  | This field is reserved for future use |
| 14 | `SAPWPS.LOCAL.REF` | `SapwpsParameter_LocalRef` |  |  |  |
| 15 | `SAPWPS.OVERRIDE` | `SapwpsParameter_Override` |  |  |  |
| 16 | `SAPWPS.RECORD.STATUS` | `SapwpsParameter_RecordStatus` | String |  |  |
| 17 | `SAPWPS.CURR.NO` | `SapwpsParameter_CurrNo` | String |  |  |
| 18 | `SAPWPS.INPUTTER` | `SapwpsParameter_Inputter` |  |  |  |
| 19 | `SAPWPS.DATE.TIME` | `SapwpsParameter_DateTime` |  |  |  |
| 20 | `SAPWPS.AUTHORISER` | `SapwpsParameter_Authoriser` | String |  |  |
| 21 | `SAPWPS.CO.CODE` | `SapwpsParameter_CoCode` | String |  |  |
| 22 | `SAPWPS.DEPT.CODE` | `SapwpsParameter_DeptCode` | String |  |  |
| 23 | `SAPWPS.AUDITOR.CODE` | `SapwpsParameter_AuditorCode` | String |  |  |
| 24 | `SAPWPS.AUDIT.DATE.TIME` | `SapwpsParameter_AuditDateTime` | String |  |  |
