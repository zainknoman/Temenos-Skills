# USRETL.AVAILABLE.BAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.USRETL.AVAILABLE.BAL.DETAILS` in `USRETL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USRETL.AVL.BAL.DESCRIPTION` | `UsretlAvailableBalDetails_Description` |  |  |  |
| 2 | `USRETL.AVL.BAL.CALC.ROUTINE` | `UsretlAvailableBalDetails_CalcRoutine` | TField |  | This field should hold the valid Routine to return the amount for the account supplied in it. This field should only have a Valid EB.API Record. Rule: Field length - 35. |
| 3 | `USRETL.AVL.BAL.RESERVED.9` | `UsretlAvailableBalDetails_Reserved9` | TField |  |  |
| 4 | `USRETL.AVL.BAL.RESERVED.8` | `UsretlAvailableBalDetails_Reserved8` | TField |  |  |
| 5 | `USRETL.AVL.BAL.RESERVED.7` | `UsretlAvailableBalDetails_Reserved7` | TField |  |  |
| 6 | `USRETL.AVL.BAL.RESERVED.6` | `UsretlAvailableBalDetails_Reserved6` | TField |  |  |
| 7 | `USRETL.AVL.BAL.RESERVED.5` | `UsretlAvailableBalDetails_Reserved5` | TField |  |  |
| 8 | `USRETL.AVL.BAL.RESERVED.4` | `UsretlAvailableBalDetails_Reserved4` | TField |  |  |
| 9 | `USRETL.AVL.BAL.RESERVED.3` | `UsretlAvailableBalDetails_Reserved3` | TField |  |  |
| 10 | `USRETL.AVL.BAL.RESERVED.2` | `UsretlAvailableBalDetails_Reserved2` | TField |  |  |
| 11 | `USRETL.AVL.BAL.RESERVED.1` | `UsretlAvailableBalDetails_Reserved1` | TField |  |  |
| 12 | `USRETL.AVL.BAL.RECORD.STATUS` | `UsretlAvailableBalDetails_RecordStatus` | String |  |  |
| 13 | `USRETL.AVL.BAL.CURR.NO` | `UsretlAvailableBalDetails_CurrNo` | String |  |  |
| 14 | `USRETL.AVL.BAL.INPUTTER` | `UsretlAvailableBalDetails_Inputter` |  |  |  |
| 15 | `USRETL.AVL.BAL.DATE.TIME` | `UsretlAvailableBalDetails_DateTime` |  |  |  |
| 16 | `USRETL.AVL.BAL.AUTHORISER` | `UsretlAvailableBalDetails_Authoriser` | String |  |  |
| 17 | `USRETL.AVL.BAL.CO.CODE` | `UsretlAvailableBalDetails_CoCode` | String |  |  |
| 18 | `USRETL.AVL.BAL.DEPT.CODE` | `UsretlAvailableBalDetails_DeptCode` | String |  |  |
| 19 | `USRETL.AVL.BAL.AUDITOR.CODE` | `UsretlAvailableBalDetails_AuditorCode` | String |  |  |
| 20 | `USRETL.AVL.BAL.AUDIT.DATE.TIME` | `UsretlAvailableBalDetails_AuditDateTime` | String |  |  |
