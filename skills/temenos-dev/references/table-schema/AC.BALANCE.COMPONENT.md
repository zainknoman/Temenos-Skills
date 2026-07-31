# AC.BALANCE.COMPONENT — Table Schema

> Source: `INSERTS/I_F.AC.BALANCE.COMPONENT` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ABC.DESCRIPTION` | `AcBalanceComponent_Description` |  |  |  |
| 2 | `ABC.BALANCE.TYPE` | `AcBalanceComponent_BalanceType` | TField |  | This field specifies the Balance type of the Credit checking component. AVAILABLE - BASE AVAIL.FWD - BASE AVAIL.WORK - BASE WORKING - BASE FORWARD - BASE FLOAT - OPTION FORWARD.OPTION - OPTION TDGL - OPTION LOCK.FUNDS - OPTION SWEEP - OPTION |
| 3 | `ABC.RECORD.STATUS` | `AcBalanceComponent_RecordStatus` | String |  |  |
| 4 | `ABC.CURR.NO` | `AcBalanceComponent_CurrNo` | String |  |  |
| 5 | `ABC.INPUTTER` | `AcBalanceComponent_Inputter` |  |  |  |
| 6 | `ABC.DATE.TIME` | `AcBalanceComponent_DateTime` |  |  |  |
| 7 | `ABC.AUTHORISER` | `AcBalanceComponent_Authoriser` | String |  |  |
| 8 | `ABC.CO.CODE` | `AcBalanceComponent_CoCode` | String |  |  |
| 9 | `ABC.DEPT.CODE` | `AcBalanceComponent_DeptCode` | String |  |  |
| 10 | `ABC.AUDITOR.CODE` | `AcBalanceComponent_AuditorCode` | String |  |  |
| 11 | `ABC.AUDIT.DATE.TIME` | `AcBalanceComponent_AuditDateTime` | String |  |  |
