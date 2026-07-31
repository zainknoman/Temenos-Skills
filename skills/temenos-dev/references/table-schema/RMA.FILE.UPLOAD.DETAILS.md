# RMA.FILE.UPLOAD.DETAILS — Table Schema

> Source: `INSERTS/I_F.RMA.FILE.UPLOAD.DETAILS` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.RFUD.PART.FILE.CREATE.DT` | `RmaFileUploadDetails_PartFileCreateDT` |  |  |  |
| 2 | `DE.RFUD.PART.FILE.NAME` | `RmaFileUploadDetails_PartFileName` | TField | Yes | Indicates the name of the latest partial file uploaded in PP.RMA Validations: String type field. If the PART.FILE.UPLD.DATETIME or PART.FILE.CREATE.DT is given the PART.FILE.NAME is mandatory |
| 3 | `DE.RFUD.PART.FILE.UPLD.DATETIME` | `RmaFileUploadDetails_PartFileUpldDateTime` |  |  |  |
| 4 | `DE.RFUD.COMP.FILE.CREATE.DT` | `RmaFileUploadDetails_CompFileCreateDT` |  |  |  |
| 5 | `DE.RFUD.COMP.FILE.NAME` | `RmaFileUploadDetails_CompFileName` | TField | Yes | Indicates the name of the last complete file uploaded in PP.RMA Validations: String field. If the COMP.FILE.UPLD.DATETIME or COMP.FILE.CREATE.DT is given the COMP.FILE.NAME is mandatory |
| 6 | `DE.RFUD.COMP.FILE.UPLD.DATETIME` | `RmaFileUploadDetails_CompFileUpldDateTime` |  |  |  |
| 7 | `DE.RFUD.INIT.ARC.RUN` | `RmaFileUploadDetails_InitArcRun` | TField |  | No Input field. Initially blank. Will be updated by the system as YES when the first archival run happens after the first complete file has been uploaded. |
| 8 | `DE.RFUD.RESERVED.10` | `RmaFileUploadDetails_Reserved10` | TField |  |  |
| 9 | `DE.RFUD.RESERVED.9` | `RmaFileUploadDetails_Reserved9` | TField |  |  |
| 10 | `DE.RFUD.RESERVED.8` | `RmaFileUploadDetails_Reserved8` | TField |  |  |
| 11 | `DE.RFUD.RESERVED.7` | `RmaFileUploadDetails_Reserved7` | TField |  |  |
| 12 | `DE.RFUD.RESERVED.6` | `RmaFileUploadDetails_Reserved6` | TField |  |  |
| 13 | `DE.RFUD.RESERVED.5` | `RmaFileUploadDetails_Reserved5` | TField |  |  |
| 14 | `DE.RFUD.RESERVED.4` | `RmaFileUploadDetails_Reserved4` | TField |  |  |
| 15 | `DE.RFUD.RESERVED.3` | `RmaFileUploadDetails_Reserved3` | TField |  |  |
| 16 | `DE.RFUD.RESERVED.2` | `RmaFileUploadDetails_Reserved2` | TField |  |  |
| 17 | `DE.RFUD.RESERVED.1` | `RmaFileUploadDetails_Reserved1` | TField |  |  |
| 18 | `DE.RFUD.LOCAL.REF` | `RmaFileUploadDetails_LocalRef` |  |  |  |
| 19 | `DE.RFUD.OVERRIDE` | `RmaFileUploadDetails_Override` |  |  |  |
| 20 | `DE.RFUD.RECORD.STATUS` | `RmaFileUploadDetails_RecordStatus` | String |  |  |
| 21 | `DE.RFUD.CURR.NO` | `RmaFileUploadDetails_CurrNo` | String |  |  |
| 22 | `DE.RFUD.INPUTTER` | `RmaFileUploadDetails_Inputter` |  |  |  |
| 23 | `DE.RFUD.DATE.TIME` | `RmaFileUploadDetails_DateTime` |  |  |  |
| 24 | `DE.RFUD.AUTHORISER` | `RmaFileUploadDetails_Authoriser` | String |  |  |
| 25 | `DE.RFUD.CO.CODE` | `RmaFileUploadDetails_CoCode` | String |  |  |
| 26 | `DE.RFUD.DEPT.CODE` | `RmaFileUploadDetails_DeptCode` | String |  |  |
| 27 | `DE.RFUD.AUDITOR.CODE` | `RmaFileUploadDetails_AuditorCode` | String |  |  |
| 28 | `DE.RFUD.AUDIT.DATE.TIME` | `RmaFileUploadDetails_AuditDateTime` | String |  |  |
