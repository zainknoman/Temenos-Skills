# CP.SUSPEND.REASON — Table Schema

> Source: `INSERTS/I_F.CP.SUSPEND.REASON` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.SPD.RSN.CP.SR.TABLE.NAME` | `CpSuspendReason_CpSrTableName` | TField |  | This field stores the name of the table (like CP.CAMPAIGN), whose records will be suspended, because of the Admin Item suspend. |
| 2 | `CP.SPD.RSN.CP.SR.RECORD.ID` | `CpSuspendReason_CpSrRecordId` | TField |  | This field stores record ID that will get suspended because of the Admin Item suspend. |
| 3 | `CP.SPD.RSN.CP.SR.CAMPAIGN.STATUS` | `CpSuspendReason_CpSrCampaignStatus` | TField |  | This field stores the suspended status of the Campaign, from the moment when it was suspended by a corresponding Admin Item suspend operation. |
| 4 | `CP.SPD.RSN.CP.SR.GENERATING.TBL` | `CpSuspendReason_CpSrGeneratingTbl` |  |  |  |
| 5 | `CP.SPD.RSN.CP.SR.GENERATING.REC.ID` | `CpSuspendReason_CpSrGeneratingRecId` |  |  |  |
| 6 | `CP.SPD.RSN.CP.SR.GEN.REC.STATUS` | `CpSuspendReason_CpSrGenRecStatus` |  |  |  |
| 7 | `CP.SPD.RSN.CP.SR.FOLLOW.UP.CAMPAIGN` | `CpSuspendReason_CpSrFollowUpCampaign` |  |  |  |
| 8 | `CP.SPD.RSN.CP.SR.LAST.GEN.TBL` | `CpSuspendReason_CpSrLastGenTbl` | TField |  | Table of the last Admin record which got re-approved, meaning the last reason that was keeping the campaign suspended. |
| 9 | `CP.SPD.RSN.CP.SR.LAST.GEN.REC.ID` | `CpSuspendReason_CpSrLastGenRecId` | TField |  | The ID of the last Admin record which got re-approved, meaning the last reason that was keeping the campaign suspended. |
| 10 | `CP.SPD.RSN.CP.SR.RECORD.PROCESSED` | `CpSuspendReason_CpSrRecordProcessed` | TField |  | This field tells you if the suspend reason record was fully processed: Y/N. |
| 11 | `CP.SPD.RSN.RESERVED.25` | `CpSuspendReason_Reserved25` | TField |  |  |
| 12 | `CP.SPD.RSN.RESERVED.24` | `CpSuspendReason_Reserved24` | TField |  |  |
| 13 | `CP.SPD.RSN.RESERVED.23` | `CpSuspendReason_Reserved23` | TField |  |  |
| 14 | `CP.SPD.RSN.RESERVED.22` | `CpSuspendReason_Reserved22` | TField |  |  |
| 15 | `CP.SPD.RSN.RESERVED.21` | `CpSuspendReason_Reserved21` | TField |  |  |
| 16 | `CP.SPD.RSN.RESERVED.20` | `CpSuspendReason_Reserved20` | TField |  |  |
| 17 | `CP.SPD.RSN.RESERVED.19` | `CpSuspendReason_Reserved19` | TField |  |  |
| 18 | `CP.SPD.RSN.RESERVED.18` | `CpSuspendReason_Reserved18` | TField |  |  |
| 19 | `CP.SPD.RSN.RESERVED.17` | `CpSuspendReason_Reserved17` | TField |  |  |
| 20 | `CP.SPD.RSN.RESERVED.16` | `CpSuspendReason_Reserved16` | TField |  |  |
| 21 | `CP.SPD.RSN.RESERVED.15` | `CpSuspendReason_Reserved15` | TField |  |  |
| 22 | `CP.SPD.RSN.RESERVED.14` | `CpSuspendReason_Reserved14` | TField |  |  |
| 23 | `CP.SPD.RSN.RESERVED.13` | `CpSuspendReason_Reserved13` | TField |  |  |
| 24 | `CP.SPD.RSN.RESERVED.12` | `CpSuspendReason_Reserved12` | TField |  |  |
| 25 | `CP.SPD.RSN.RESERVED.11` | `CpSuspendReason_Reserved11` | TField |  |  |
| 26 | `CP.SPD.RSN.RESERVED.10` | `CpSuspendReason_Reserved10` | TField |  |  |
| 27 | `CP.SPD.RSN.RESERVED.9` | `CpSuspendReason_Reserved9` | TField |  |  |
| 28 | `CP.SPD.RSN.RESERVED.8` | `CpSuspendReason_Reserved8` | TField |  |  |
| 29 | `CP.SPD.RSN.RESERVED.7` | `CpSuspendReason_Reserved7` | TField |  |  |
| 30 | `CP.SPD.RSN.RESERVED.6` | `CpSuspendReason_Reserved6` | TField |  |  |
| 31 | `CP.SPD.RSN.RESERVED.5` | `CpSuspendReason_Reserved5` | TField |  |  |
| 32 | `CP.SPD.RSN.RESERVED.4` | `CpSuspendReason_Reserved4` | TField |  |  |
| 33 | `CP.SPD.RSN.RESERVED.3` | `CpSuspendReason_Reserved3` | TField |  |  |
| 34 | `CP.SPD.RSN.RESERVED.2` | `CpSuspendReason_Reserved2` | TField |  |  |
| 35 | `CP.SPD.RSN.RESERVED.1` | `CpSuspendReason_Reserved1` | TField |  |  |
| 36 | `CP.SPD.RSN.LOCAL.REF` | `CpSuspendReason_LocalRef` |  |  |  |
| 37 | `CP.SPD.RSN.OVERRIDE` | `CpSuspendReason_Override` |  |  |  |
| 38 | `CP.SPD.RSN.RECORD.STATUS` | `CpSuspendReason_RecordStatus` | String |  |  |
| 39 | `CP.SPD.RSN.CURR.NO` | `CpSuspendReason_CurrNo` | String |  |  |
| 40 | `CP.SPD.RSN.INPUTTER` | `CpSuspendReason_Inputter` |  |  |  |
| 41 | `CP.SPD.RSN.DATE.TIME` | `CpSuspendReason_DateTime` |  |  |  |
| 42 | `CP.SPD.RSN.AUTHORISER` | `CpSuspendReason_Authoriser` | String |  |  |
| 43 | `CP.SPD.RSN.CO.CODE` | `CpSuspendReason_CoCode` | String |  |  |
| 44 | `CP.SPD.RSN.DEPT.CODE` | `CpSuspendReason_DeptCode` | String |  |  |
| 45 | `CP.SPD.RSN.AUDITOR.CODE` | `CpSuspendReason_AuditorCode` | String |  |  |
| 46 | `CP.SPD.RSN.AUDIT.DATE.TIME` | `CpSuspendReason_AuditDateTime` | String |  |  |
