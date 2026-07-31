# INLEND.SFMS.OUT.TAG.ORDER — Table Schema

> Source: `INSERTS/I_F.INLEND.SFMS.OUT.TAG.ORDER` in `INSFMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFMS.OUT.TAG.TAG.ORDER` | `InlendSfmsOutTagOrder_TagOrder` |  |  |  |
| 2 | `SFMS.OUT.TAG.LOCAL.REF` | `InlendSfmsOutTagOrder_LocalRef` |  |  |  |
| 3 | `SFMS.OUT.TAG.OVERRIDE` | `InlendSfmsOutTagOrder_Override` |  |  |  |
| 4 | `SFMS.OUT.TAG.RECORD.STATUS` | `InlendSfmsOutTagOrder_RecordStatus` | String |  |  |
| 5 | `SFMS.OUT.TAG.CURR.NO` | `InlendSfmsOutTagOrder_CurrNo` | String |  |  |
| 6 | `SFMS.OUT.TAG.INPUTTER` | `InlendSfmsOutTagOrder_Inputter` |  |  |  |
| 7 | `SFMS.OUT.TAG.DATE.TIME` | `InlendSfmsOutTagOrder_DateTime` |  |  |  |
| 8 | `SFMS.OUT.TAG.AUTHORISER` | `InlendSfmsOutTagOrder_Authoriser` | String |  |  |
| 9 | `SFMS.OUT.TAG.CO.CODE` | `InlendSfmsOutTagOrder_CoCode` | String |  |  |
| 10 | `SFMS.OUT.TAG.DEPT.CODE` | `InlendSfmsOutTagOrder_DeptCode` | String |  |  |
| 11 | `SFMS.OUT.TAG.AUDITOR.CODE` | `InlendSfmsOutTagOrder_AuditorCode` | String |  |  |
| 12 | `SFMS.OUT.TAG.AUDIT.DATE.TIME` | `InlendSfmsOutTagOrder_AuditDateTime` | String |  |  |
