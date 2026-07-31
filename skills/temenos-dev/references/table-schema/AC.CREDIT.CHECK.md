# AC.CREDIT.CHECK — Table Schema

> Source: `INSERTS/I_F.AC.CREDIT.CHECK` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACC.DESCRIPTION` | `AcCreditCheck_Description` |  |  |  |
| 2 | `ACC.BASE.BALANCE.TYPE` | `AcCreditCheck_BaseBalanceType` | TField |  | This field holds only BASE balance type component specified in AC.BALANCE.COMPONENT. Validation : Should be a valid AC.BALANCE.COMPONENT record with BASE as BALANCE.TYPE |
| 3 | `ACC.OPTION.BALANCE.TYPE` | `AcCreditCheck_OptionBalanceType` |  |  |  |
| 4 | `ACC.RECORD.STATUS` | `AcCreditCheck_RecordStatus` | String |  |  |
| 5 | `ACC.CURR.NO` | `AcCreditCheck_CurrNo` | String |  |  |
| 6 | `ACC.INPUTTER` | `AcCreditCheck_Inputter` |  |  |  |
| 7 | `ACC.DATE.TIME` | `AcCreditCheck_DateTime` |  |  |  |
| 8 | `ACC.AUTHORISER` | `AcCreditCheck_Authoriser` | String |  |  |
| 9 | `ACC.CO.CODE` | `AcCreditCheck_CoCode` | String |  |  |
| 10 | `ACC.DEPT.CODE` | `AcCreditCheck_DeptCode` | String |  |  |
| 11 | `ACC.AUDITOR.CODE` | `AcCreditCheck_AuditorCode` | String |  |  |
| 12 | `ACC.AUDIT.DATE.TIME` | `AcCreditCheck_AuditDateTime` | String |  |  |
