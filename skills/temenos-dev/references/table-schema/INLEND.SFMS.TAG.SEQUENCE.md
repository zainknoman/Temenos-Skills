# INLEND.SFMS.TAG.SEQUENCE — Table Schema

> Source: `INSERTS/I_F.INLEND.SFMS.TAG.SEQUENCE` in `INSFMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFMS.TAG.TAG.NUMBER` | `InlendSfmsTagSequence_TagNumber` |  |  |  |
| 2 | `SFMS.TAG.TAG.SEQUENCE` | `InlendSfmsTagSequence_TagSequence` |  |  |  |
| 3 | `SFMS.TAG.SFMS.TAG.LOCAL.REF` | `InlendSfmsTagSequence_LocalRef` |  |  |  |
| 4 | `SFMS.TAG.OVERRIDE` | `InlendSfmsTagSequence_Override` |  |  |  |
| 5 | `SFMS.TAG.RECORD.STATUS` | `InlendSfmsTagSequence_RecordStatus` | String |  |  |
| 6 | `SFMS.TAG.CURR.NO` | `InlendSfmsTagSequence_CurrNo` | String |  |  |
| 7 | `SFMS.TAG.INPUTTER` | `InlendSfmsTagSequence_Inputter` |  |  |  |
| 8 | `SFMS.TAG.DATE.TIME` | `InlendSfmsTagSequence_DateTime` |  |  |  |
| 9 | `SFMS.TAG.AUTHORISER` | `InlendSfmsTagSequence_Authoriser` | String |  |  |
| 10 | `SFMS.TAG.CO.CODE` | `InlendSfmsTagSequence_CoCode` | String |  |  |
| 11 | `SFMS.TAG.DEPT.CODE` | `InlendSfmsTagSequence_DeptCode` | String |  |  |
| 12 | `SFMS.TAG.AUDITOR.CODE` | `InlendSfmsTagSequence_AuditorCode` | String |  |  |
| 13 | `SFMS.TAG.AUDIT.DATE.TIME` | `InlendSfmsTagSequence_AuditDateTime` | String |  |  |
