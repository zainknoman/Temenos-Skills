# PP.IN.CHANNELS — Table Schema

> Source: `INSERTS/I_F.PP.IN.CHANNELS` in `PP_InwardFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ICH.InfolderName` | `PpInChannels_Infoldername` |  |  |  |
| 2 | `PP.ICH.QueueName` | `PpInChannels_Queuename` |  |  |  |
| 3 | `PP.ICH.BackupFolder` | `PpInChannels_Backupfolder` |  |  |  |
| 4 | `PP.ICH.GenericFolder` | `PpInChannels_Genericfolder` |  |  |  |
| 5 | `PP.ICH.SchemaFolder` | `PpInChannels_Schemafolder` |  |  |  |
| 6 | `PP.ICH.StyleSheetFolder` | `PpInChannels_Stylesheetfolder` |  |  |  |
| 7 | `PP.ICH.ErrorFolder` | `PpInChannels_Errorfolder` |  |  |  |
| 8 | `PP.ICH.PropertyFolder` | `PpInChannels_Propertyfolder` |  |  |  |
| 9 | `PP.ICH.HeaderCode` | `PpInChannels_Headercode` |  |  |  |
| 10 | `PP.ICH.HeaderLineCount` | `PpInChannels_Headerlinecount` |  |  |  |
| 11 | `PP.ICH.TrailerCode` | `PpInChannels_Trailercode` |  |  |  |
| 12 | `PP.ICH.TrailerLineCount` | `PpInChannels_Trailerlinecount` |  |  |  |
| 13 | `PP.ICH.TransactionCode` | `PpInChannels_Transactioncode` |  |  |  |
| 14 | `PP.ICH.FileTransferIndicator` | `PpInChannels_Filetransferindicator` |  |  |  |
| 15 | `PP.ICH.StandIn` | `PpInChannels_Standin` |  |  |  |
| 16 | `PP.ICH.IntegrityRequired` | `PpInChannels_Integrityrequired` |  |  |  |
| 17 | `PP.ICH.IntegrityAPI` | `PpInChannels_Integrityapi` |  |  |  |
| 18 | `PP.ICH.LOCAL.REF` | `PpInChannels_LocalRef` |  |  |  |
| 19 | `PP.ICH.OVERRIDE` | `PpInChannels_Override` |  |  |  |
| 20 | `PP.ICH.RECORD.STATUS` | `PpInChannels_RecordStatus` | String |  |  |
| 21 | `PP.ICH.CURR.NO` | `PpInChannels_CurrNo` | String |  |  |
| 22 | `PP.ICH.INPUTTER` | `PpInChannels_Inputter` |  |  |  |
| 23 | `PP.ICH.DATE.TIME` | `PpInChannels_DateTime` |  |  |  |
| 24 | `PP.ICH.AUTHORISER` | `PpInChannels_Authoriser` | String |  |  |
| 25 | `PP.ICH.CO.CODE` | `PpInChannels_CoCode` | String |  |  |
| 26 | `PP.ICH.DEPT.CODE` | `PpInChannels_DeptCode` | String |  |  |
| 27 | `PP.ICH.AUDITOR.CODE` | `PpInChannels_AuditorCode` | String |  |  |
| 28 | `PP.ICH.AUDIT.DATE.TIME` | `PpInChannels_AuditDateTime` | String |  |  |
