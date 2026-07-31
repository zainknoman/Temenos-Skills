# AML.TXN.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AML.TXN.PARAMETER` in `VP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AML.PAR.DESCRIPTION` | `AmlTxnParameter_Description` |  |  |  |
| 2 | `AML.PAR.APPLICATION` | `AmlTxnParameter_Application` |  |  |  |
| 3 | `AML.PAR.RECORD.STATUS` | `AmlTxnParameter_RecordStatus` | String |  |  |
| 4 | `AML.PAR.CURR.NO` | `AmlTxnParameter_CurrNo` | String |  |  |
| 5 | `AML.PAR.INPUTTER` | `AmlTxnParameter_Inputter` |  |  |  |
| 6 | `AML.PAR.DATE.TIME` | `AmlTxnParameter_DateTime` |  |  |  |
| 7 | `AML.PAR.AUTHORISER` | `AmlTxnParameter_Authoriser` | String |  |  |
| 8 | `AML.PAR.CO.CODE` | `AmlTxnParameter_CoCode` | String |  |  |
| 9 | `AML.PAR.DEPT.CODE` | `AmlTxnParameter_DeptCode` | String |  |  |
| 10 | `AML.PAR.AUDITOR.CODE` | `AmlTxnParameter_AuditorCode` | String |  |  |
| 11 | `AML.PAR.AUDIT.DATE.TIME` | `AmlTxnParameter_AuditDateTime` | String |  |  |
