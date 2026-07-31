# AM.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.AM.EXCEPTION` in `AM_Instrument.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.EX.TXN.CODE` | `AmException_TxnCode` |  |  |  |
| 2 | `AM.EX.PL.CATEG` | `AmException_PlCateg` |  |  |  |
| 3 | `AM.EX.RECORD.STATUS` | `AmException_RecordStatus` | String |  |  |
| 4 | `AM.EX.CURR.NO` | `AmException_CurrNo` | String |  |  |
| 5 | `AM.EX.INPUTTER` | `AmException_Inputter` |  |  |  |
| 6 | `AM.EX.DATE.TIME` | `AmException_DateTime` |  |  |  |
| 7 | `AM.EX.AUTHORISER` | `AmException_Authoriser` | String |  |  |
| 8 | `AM.EX.CO.CODE` | `AmException_CoCode` | String |  |  |
| 9 | `AM.EX.DEPT.CODE` | `AmException_DeptCode` | String |  |  |
| 10 | `AM.EX.AUDITOR.CODE` | `AmException_AuditorCode` | String |  |  |
| 11 | `AM.EX.AUDIT.DATE.TIME` | `AmException_AuditDateTime` | String |  |  |
