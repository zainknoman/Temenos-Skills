# SE.NDBL.NER.UPDATE — Table Schema

> Source: `INSERTS/I_F.SE.NDBL.NER.UPDATE` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NDBL.NER.LOCK.RETRY.COUNT` | `SeNdblNerUpdate_LockRetryCount` | TField |  |  |
| 2 | `NDBL.NER.RECORD.STATUS` | `SeNdblNerUpdate_RecordStatus` | String |  |  |
| 3 | `NDBL.NER.CURR.NO` | `SeNdblNerUpdate_CurrNo` | String |  |  |
| 4 | `NDBL.NER.INPUTTER` | `SeNdblNerUpdate_Inputter` |  |  |  |
| 5 | `NDBL.NER.DATE.TIME` | `SeNdblNerUpdate_DateTime` |  |  |  |
| 6 | `NDBL.NER.AUTHORISER` | `SeNdblNerUpdate_Authoriser` | String |  |  |
| 7 | `NDBL.NER.CO.CODE` | `SeNdblNerUpdate_CoCode` | String |  |  |
| 8 | `NDBL.NER.DEPT.CODE` | `SeNdblNerUpdate_DeptCode` | String |  |  |
| 9 | `NDBL.NER.AUDITOR.CODE` | `SeNdblNerUpdate_AuditorCode` | String |  |  |
| 10 | `NDBL.NER.AUDIT.DATE.TIME` | `SeNdblNerUpdate_AuditDateTime` | String |  |  |
