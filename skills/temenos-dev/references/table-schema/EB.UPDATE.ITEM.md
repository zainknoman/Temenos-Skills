# EB.UPDATE.ITEM — Table Schema

> Source: `INSERTS/I_F.EB.UPDATE.ITEM` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UI.RELATED.UPDATE` | `EbUpdateItem_RelatedUpdate` | TField |  | Any dependent updates that must be released along with this one. |
| 2 | `EB.UI.REFERENCE` | `EbUpdateItem_Reference` | TField |  | A helpdesk or CSS reference. |
| 3 | `EB.UI.PROBLEM` | `EbUpdateItem_Problem` | TField |  | A description of the Problem. |
| 4 | `EB.UI.SYMPTOM` | `EbUpdateItem_Symptom` | TField |  | A description of the effect to the system that the Problem caused. |
| 5 | `EB.UI.NATURE.OF.FIX` | `EbUpdateItem_NatureOfFix` | TField |  | A brief description of what was done to resolve the problem or bug. |
| 6 | `EB.UI.INSTRUCTIONS` | `EbUpdateItem_Instructions` | TField |  | A guide to installing this update if necessary. |
| 7 | `EB.UI.PRIORITY` | `EbUpdateItem_Priority` | TField |  | Priority of the update. If it is Critical then it will be flagged. |
| 8 | `EB.UI.RESERVED.7` | `EbUpdateItem_Reserved7` | TField |  |  |
| 9 | `EB.UI.RESERVED.6` | `EbUpdateItem_Reserved6` | TField |  |  |
| 10 | `EB.UI.RESERVED.5` | `EbUpdateItem_Reserved5` | TField |  |  |
| 11 | `EB.UI.RESERVED.4` | `EbUpdateItem_Reserved4` | TField |  |  |
| 12 | `EB.UI.RESERVED.3` | `EbUpdateItem_Reserved3` | TField |  |  |
| 13 | `EB.UI.RESERVED.2` | `EbUpdateItem_Reserved2` | TField |  |  |
| 14 | `EB.UI.RESERVED.1` | `EbUpdateItem_Reserved1` | TField |  |  |
| 15 | `EB.UI.LOCAL.REF` | `EbUpdateItem_LocalRef` |  |  |  |
| 16 | `EB.UI.OVERRIDE` | `EbUpdateItem_Override` |  |  |  |
| 17 | `EB.UI.RECORD.STATUS` | `EbUpdateItem_RecordStatus` | String |  |  |
| 18 | `EB.UI.CURR.NO` | `EbUpdateItem_CurrNo` | String |  |  |
| 19 | `EB.UI.INPUTTER` | `EbUpdateItem_Inputter` |  |  |  |
| 20 | `EB.UI.DATE.TIME` | `EbUpdateItem_DateTime` |  |  |  |
| 21 | `EB.UI.AUTHORISER` | `EbUpdateItem_Authoriser` | String |  |  |
| 22 | `EB.UI.CO.CODE` | `EbUpdateItem_CoCode` | String |  |  |
| 23 | `EB.UI.DEPT.CODE` | `EbUpdateItem_DeptCode` | String |  |  |
| 24 | `EB.UI.AUDITOR.CODE` | `EbUpdateItem_AuditorCode` | String |  |  |
| 25 | `EB.UI.AUDIT.DATE.TIME` | `EbUpdateItem_AuditDateTime` | String |  |  |
