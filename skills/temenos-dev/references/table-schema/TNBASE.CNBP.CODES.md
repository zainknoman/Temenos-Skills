# TNBASE.CNBP.CODES — Table Schema

> Source: `INSERTS/I_F.TNBASE.CNBP.CODES` in `TNBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNBP.CODES.DECLARATION.REQUIRED` | `TnbaseCnbpCodes_DeclarationRequired` | TField |  | Yes/No field to indicate if declarations is required for this code |
| 2 | `CNBP.CODES.DESCRIPTION` | `TnbaseCnbpCodes_Description` |  |  |  |
| 3 | `CNBP.CODES.EXPENSE.TYPE` | `TnbaseCnbpCodes_ExpenseType` | TField |  | This field to indicate the allowed Type of Expenses for this code |
| 4 | `CNBP.CODES.RESERVED.8` | `TnbaseCnbpCodes_Reserved8` | TField |  | Field for future use |
| 5 | `CNBP.CODES.RESERVED.7` | `TnbaseCnbpCodes_Reserved7` | TField |  | Field for future use |
| 6 | `CNBP.CODES.RESERVED.6` | `TnbaseCnbpCodes_Reserved6` | TField |  | Field for future use |
| 7 | `CNBP.CODES.RESERVED.5` | `TnbaseCnbpCodes_Reserved5` | TField |  | Field for future use |
| 8 | `CNBP.CODES.RESERVED.4` | `TnbaseCnbpCodes_Reserved4` | TField |  | Field for future use |
| 9 | `CNBP.CODES.RESERVED.3` | `TnbaseCnbpCodes_Reserved3` | TField |  | Field for future use |
| 10 | `CNBP.CODES.RESERVED.2` | `TnbaseCnbpCodes_Reserved2` | TField |  | Field for future use |
| 11 | `CNBP.CODES.RESERVED.1` | `TnbaseCnbpCodes_Reserved1` | TField |  | Field for future use |
| 12 | `CNBP.CODES.LOCAL.REF` | `TnbaseCnbpCodes_LocalRef` |  |  |  |
| 13 | `CNBP.CODES.OVERRIDE` | `TnbaseCnbpCodes_Override` |  |  |  |
| 14 | `CNBP.CODES.RECORD.STATUS` | `TnbaseCnbpCodes_RecordStatus` | String |  |  |
| 15 | `CNBP.CODES.CURR.NO` | `TnbaseCnbpCodes_CurrNo` | String |  |  |
| 16 | `CNBP.CODES.INPUTTER` | `TnbaseCnbpCodes_Inputter` |  |  |  |
| 17 | `CNBP.CODES.DATE.TIME` | `TnbaseCnbpCodes_DateTime` |  |  |  |
| 18 | `CNBP.CODES.AUTHORISER` | `TnbaseCnbpCodes_Authoriser` | String |  |  |
| 19 | `CNBP.CODES.CO.CODE` | `TnbaseCnbpCodes_CoCode` | String |  |  |
| 20 | `CNBP.CODES.DEPT.CODE` | `TnbaseCnbpCodes_DeptCode` | String |  |  |
| 21 | `CNBP.CODES.AUDITOR.CODE` | `TnbaseCnbpCodes_AuditorCode` | String |  |  |
| 22 | `CNBP.CODES.AUDIT.DATE.TIME` | `TnbaseCnbpCodes_AuditDateTime` | String |  |  |
