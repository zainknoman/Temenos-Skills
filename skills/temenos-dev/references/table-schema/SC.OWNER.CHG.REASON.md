# SC.OWNER.CHG.REASON — Table Schema

> Source: `INSERTS/I_F.SC.OWNER.CHG.REASON` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.OCR.SHORT.DESCRIPTION` | `ScOwnerChgReason_ShortDescription` | TField |  |  |
| 2 | `SC.OCR.DESCRIPTION` | `ScOwnerChgReason_Description` |  |  |  |
| 3 | `SC.OCR.RESERVED.03` | `ScOwnerChgReason_Reserved03` | TField |  |  |
| 4 | `SC.OCR.RESERVED.02` | `ScOwnerChgReason_Reserved02` | TField |  |  |
| 5 | `SC.OCR.RESERVED.01` | `ScOwnerChgReason_Reserved01` | TField |  |  |
| 6 | `SC.OCR.LOCAL.REF` | `ScOwnerChgReason_LocalRef` |  |  |  |
| 7 | `SC.OCR.OVERRIDE` | `ScOwnerChgReason_Override` |  |  |  |
| 8 | `SC.OCR.RECORD.STATUS` | `ScOwnerChgReason_RecordStatus` | String |  |  |
| 9 | `SC.OCR.CURR.NO` | `ScOwnerChgReason_CurrNo` | String |  |  |
| 10 | `SC.OCR.INPUTTER` | `ScOwnerChgReason_Inputter` |  |  |  |
| 11 | `SC.OCR.DATE.TIME` | `ScOwnerChgReason_DateTime` |  |  |  |
| 12 | `SC.OCR.AUTHORISER` | `ScOwnerChgReason_Authoriser` | String |  |  |
| 13 | `SC.OCR.CO.CODE` | `ScOwnerChgReason_CoCode` | String |  |  |
| 14 | `SC.OCR.DEPT.CODE` | `ScOwnerChgReason_DeptCode` | String |  |  |
| 15 | `SC.OCR.AUDITOR.CODE` | `ScOwnerChgReason_AuditorCode` | String |  |  |
| 16 | `SC.OCR.AUDIT.DATE.TIME` | `ScOwnerChgReason_AuditDateTime` | String |  |  |
