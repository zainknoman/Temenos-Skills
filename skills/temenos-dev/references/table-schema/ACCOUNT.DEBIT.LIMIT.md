# ACCOUNT.DEBIT.LIMIT — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.DEBIT.LIMIT` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ADL.LIMIT` | `AccountDebitLimit_Limit` | TField | Yes | Standard T24 amount field. Validation Rules: Mandatory input. A maximum of 018 characters may be entered. |
| 2 | `IC.ADL.TEMPORARY.LIMIT` | `AccountDebitLimit_TemporaryLimit` | TField |  | Standard T24 amount field. Validation Rules: A maximum of 018 characters may be entered. |
| 3 | `IC.ADL.LOCAL.REF` | `AccountDebitLimit_LocalRef` |  |  |  |
| 4 | `IC.ADL.OVERRIDE` | `AccountDebitLimit_Override` |  |  |  |
| 5 | `IC.ADL.RECORD.STATUS` | `AccountDebitLimit_RecordStatus` | String |  |  |
| 6 | `IC.ADL.CURR.NO` | `AccountDebitLimit_CurrNo` | String |  |  |
| 7 | `IC.ADL.INPUTTER` | `AccountDebitLimit_Inputter` |  |  |  |
| 8 | `IC.ADL.DATE.TIME` | `AccountDebitLimit_DateTime` |  |  |  |
| 9 | `IC.ADL.AUTHORISER` | `AccountDebitLimit_Authoriser` | String |  |  |
| 10 | `IC.ADL.CO.CODE` | `AccountDebitLimit_CoCode` | String |  |  |
| 11 | `IC.ADL.DEPT.CODE` | `AccountDebitLimit_DeptCode` | String |  |  |
| 12 | `IC.ADL.AUDITOR.CODE` | `AccountDebitLimit_AuditorCode` | String |  |  |
| 13 | `IC.ADL.AUDIT.DATE.TIME` | `AccountDebitLimit_AuditDateTime` | String |  |  |
