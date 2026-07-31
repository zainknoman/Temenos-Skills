# EB.FILE.UPLOAD.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.FILE.UPLOAD.PARAM` in `EB_FileUpload.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UP.TC.UPLOAD.PATH` | `EbFileUploadParam_TcUploadPath` | TField | Yes | Warning: Changing this field after files have been uploaded means the system will no longer be able to find uploaded files! This field must be the same as the &lt;UPLOAD_PATH&gt; in the tcserver.xml &lt;LISTENER&gt; used for file uploads. If they are different, files will be uploaded but EB.FILE.UPLOAD records will not validate. The TC server process must have permissions to write to the upload directory (specified in this field and the EB.FILE.UPLOAD.TYPE / UPLOAD.DIR field). Mandatory field. 1-150 characters allowed. |
| 2 | `EB.UP.FILE.UPLOAD` | `EbFileUploadParam_FileUpload` | TField |  |  |
| 3 | `EB.UP.RESERVED.9` | `EbFileUploadParam_Reserved9` |  |  |  |
| 4 | `EB.UP.RESERVED.8` | `EbFileUploadParam_Reserved8` |  |  |  |
| 5 | `EB.UP.RESERVED.7` | `EbFileUploadParam_Reserved7` |  |  |  |
| 6 | `EB.UP.RESERVED.6` | `EbFileUploadParam_Reserved6` | TField |  |  |
| 7 | `EB.UP.RESERVED.5` | `EbFileUploadParam_Reserved5` | TField |  |  |
| 8 | `EB.UP.RESERVED.4` | `EbFileUploadParam_Reserved4` | TField |  |  |
| 9 | `EB.UP.RESERVED.3` | `EbFileUploadParam_Reserved3` | TField |  |  |
| 10 | `EB.UP.RESERVED.2` | `EbFileUploadParam_Reserved2` | TField |  |  |
| 11 | `EB.UP.RESERVED.1` | `EbFileUploadParam_Reserved1` | TField |  |  |
| 12 | `EB.UP.LOCAL.REF` | `EbFileUploadParam_LocalRef` |  |  |  |
| 13 | `EB.UP.OVERRIDE` | `EbFileUploadParam_Override` |  |  |  |
| 14 | `EB.UP.RECORD.STATUS` | `EbFileUploadParam_RecordStatus` | String |  |  |
| 15 | `EB.UP.CURR.NO` | `EbFileUploadParam_CurrNo` | String |  |  |
| 16 | `EB.UP.INPUTTER` | `EbFileUploadParam_Inputter` |  |  |  |
| 17 | `EB.UP.DATE.TIME` | `EbFileUploadParam_DateTime` |  |  |  |
| 18 | `EB.UP.AUTHORISER` | `EbFileUploadParam_Authoriser` | String |  |  |
| 19 | `EB.UP.CO.CODE` | `EbFileUploadParam_CoCode` | String |  |  |
| 20 | `EB.UP.DEPT.CODE` | `EbFileUploadParam_DeptCode` | String |  |  |
| 21 | `EB.UP.AUDITOR.CODE` | `EbFileUploadParam_AuditorCode` | String |  |  |
| 22 | `EB.UP.AUDIT.DATE.TIME` | `EbFileUploadParam_AuditDateTime` | String |  |  |
