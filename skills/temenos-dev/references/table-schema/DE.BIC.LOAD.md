# DE.BIC.LOAD — Table Schema

> Source: `INSERTS/I_F.DE.BIC.LOAD` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.BIC.LOAD.DESCRIPTION` | `DeBicLoad_Description` |  |  |  |
| 2 | `DE.BIC.LOAD.ACTION` | `DeBicLoad_Action` | TField | Yes | The type of action to be performed on the existing records in the DE.BIC table. Validation Rules: Mandatory Field with two options: Update or Overwrite Update - Clear down only those records that have been automatically uploaded. Manually input records will remain. Overwrite - Clear down all existing records and upload the current BIC directory as replacement. Modify - All records (manual as well as automatically uploaded) records will remain and specific records will be modified. N.B. In all of the above modes, records will always be written in live. Care must be taken before uploading file. |
| 3 | `DE.BIC.LOAD.FILE.NAME` | `DeBicLoad_FileName` | TField |  | The name of the file to load. Validation Rules: No Input Field Defaults to bicplus.txt Note that Unix is case sensitive. |
| 4 | `DE.BIC.LOAD.FILE.LOCATION` | `DeBicLoad_FileLocation` | TField | No | Location of the BIC+ directory file Validation Rules: Optional field Default value will be the current working directory |
| 5 | `DE.BIC.LOAD.DELIMITER` | `DeBicLoad_Delimiter` | TField |  | BIC+ directory file field delimitter character. Validation Rules: Can have the value of TAB or COMMA Standard BIC export is TAB COMMA is for possible future use |
| 6 | `DE.BIC.LOAD.MAINT.MANUAL` | `DeBicLoad_MaintManual` | TField |  | Controls if DE.BIC record should go to INAU or live when Action is MODIFY. Validation Rules: Y, N or null. Default is null. If Y then DE.BIC records will be written in INAU status and user has to manually authorise. If N or null then DE.BIC records will be written in live directly. |
| 7 | `DE.BIC.LOAD.RESERVED9` | `DeBicLoad_Reserved9` | TField |  |  |
| 8 | `DE.BIC.LOAD.RESERVED8` | `DeBicLoad_Reserved8` | TField |  |  |
| 9 | `DE.BIC.LOAD.RESERVED7` | `DeBicLoad_Reserved7` | TField |  |  |
| 10 | `DE.BIC.LOAD.RESERVED6` | `DeBicLoad_Reserved6` | TField |  |  |
| 11 | `DE.BIC.LOAD.RESERVED5` | `DeBicLoad_Reserved5` | TField |  |  |
| 12 | `DE.BIC.LOAD.RESERVED4` | `DeBicLoad_Reserved4` | TField |  |  |
| 13 | `DE.BIC.LOAD.RESERVED3` | `DeBicLoad_Reserved3` | TField |  |  |
| 14 | `DE.BIC.LOAD.RESERVED2` | `DeBicLoad_Reserved2` | TField |  |  |
| 15 | `DE.BIC.LOAD.RESERVED1` | `DeBicLoad_Reserved1` | TField |  |  |
| 16 | `DE.BIC.LOAD.LOCAL.REF` | `DeBicLoad_LocalRef` |  |  |  |
| 17 | `DE.BIC.LOAD.OVERRIDE` | `DeBicLoad_Override` |  |  |  |
| 18 | `DE.BIC.LOAD.RECORD.STATUS` | `DeBicLoad_RecordStatus` | String |  |  |
| 19 | `DE.BIC.LOAD.CURR.NO` | `DeBicLoad_CurrNo` | String |  |  |
| 20 | `DE.BIC.LOAD.INPUTTER` | `DeBicLoad_Inputter` |  |  |  |
| 21 | `DE.BIC.LOAD.DATE.TIME` | `DeBicLoad_DateTime` |  |  |  |
| 22 | `DE.BIC.LOAD.AUTHORISER` | `DeBicLoad_Authoriser` | String |  |  |
| 23 | `DE.BIC.LOAD.CO.CODE` | `DeBicLoad_CoCode` | String |  |  |
| 24 | `DE.BIC.LOAD.DEPT.CODE` | `DeBicLoad_DeptCode` | String |  |  |
| 25 | `DE.BIC.LOAD.AUDITOR.CODE` | `DeBicLoad_AuditorCode` | String |  |  |
| 26 | `DE.BIC.LOAD.AUDIT.DATE.TIME` | `DeBicLoad_AuditDateTime` | String |  |  |
