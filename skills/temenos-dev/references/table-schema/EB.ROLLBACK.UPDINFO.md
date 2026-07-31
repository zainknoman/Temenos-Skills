# EB.ROLLBACK.UPDINFO — Table Schema

> Source: `INSERTS/I_F.EB.ROLLBACK.UPDINFO` in `EB_Updates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UPD.INFO.REMOVE.UPDATE` | `EbRollbackUpdinfo_RemoveUpdate` |  |  |  |
| 2 | `EB.UPD.INFO.REPLACE.UPDATE` | `EbRollbackUpdinfo_ReplaceUpdate` |  |  |  |
| 3 | `EB.UPD.INFO.RESERVED.5` | `EbRollbackUpdinfo_Reserved5` |  |  |  |
| 4 | `EB.UPD.INFO.RESERVED.4` | `EbRollbackUpdinfo_Reserved4` |  |  |  |
| 5 | `EB.UPD.INFO.RESERVED.3` | `EbRollbackUpdinfo_Reserved3` |  |  |  |
| 6 | `EB.UPD.INFO.RESERVED.2` | `EbRollbackUpdinfo_Reserved2` |  |  |  |
| 7 | `EB.UPD.INFO.RESERVED.1` | `EbRollbackUpdinfo_Reserved1` |  |  |  |
| 8 | `EB.UPD.INFO.RESERVED.10` | `EbRollbackUpdinfo_Reserved10` | TField |  |  |
| 9 | `EB.UPD.INFO.RESERVED.9` | `EbRollbackUpdinfo_Reserved9` | TField |  |  |
| 10 | `EB.UPD.INFO.RESERVED.8` | `EbRollbackUpdinfo_Reserved8` | TField |  |  |
| 11 | `EB.UPD.INFO.RESERVED.7` | `EbRollbackUpdinfo_Reserved7` | TField |  |  |
| 12 | `EB.UPD.INFO.RESERVED.6` | `EbRollbackUpdinfo_Reserved6` | TField |  |  |
| 13 | `EB.UPD.INFO.LOCAL.REF` | `EbRollbackUpdinfo_LocalRef` |  |  |  |
| 14 | `EB.UPD.INFO.OVERRIDE` | `EbRollbackUpdinfo_Override` |  |  |  |
| 15 | `EB.UPD.INFO.RECORD.STATUS` | `EbRollbackUpdinfo_RecordStatus` | String |  |  |
| 16 | `EB.UPD.INFO.CURR.NO` | `EbRollbackUpdinfo_CurrNo` | String |  |  |
| 17 | `EB.UPD.INFO.INPUTTER` | `EbRollbackUpdinfo_Inputter` |  |  |  |
| 18 | `EB.UPD.INFO.DATE.TIME` | `EbRollbackUpdinfo_DateTime` |  |  |  |
| 19 | `EB.UPD.INFO.AUTHORISER` | `EbRollbackUpdinfo_Authoriser` | String |  |  |
| 20 | `EB.UPD.INFO.CO.CODE` | `EbRollbackUpdinfo_CoCode` | String |  |  |
| 21 | `EB.UPD.INFO.DEPT.CODE` | `EbRollbackUpdinfo_DeptCode` | String |  |  |
| 23 | `EB.UPD.INFO.AUDIT.DATE.TIME` | `EbRollbackUpdinfo_AuditDateTime` | String |  |  |
