# IM.DOCUMENT.UPLOAD — Table Schema

> Source: `INSERTS/I_F.IM.DOCUMENT.UPLOAD` in `IM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IM.UP.UPLOAD.ID` | `ImDocumentUpload_UploadId` | TField |  | The record id of the IM.DOCUMENT.IMAGE record which the file being uploaded will be linked to. |
| 2 | `IM.UP.FILE.UPLOAD` | `ImDocumentUpload_FileUpload` | TField |  | The is used in two ways; the first is to use a file browser to locate and display an image. When the link button is clicked the file is both renamed and then downloaded to the storage path specified in the M.DOCUMENT.TYPE. For non image files just the filename should be entered and the file placed in the storage location manually. |
| 3 | `IM.UP.LOCAL.REF` | `ImDocumentUpload_LocalRef` |  |  |  |
| 4 | `IM.UP.RECORD.STATUS` | `ImDocumentUpload_RecordStatus` | String |  |  |
| 5 | `IM.UP.CURR.NO` | `ImDocumentUpload_CurrNo` | String |  |  |
| 6 | `IM.UP.INPUTTER` | `ImDocumentUpload_Inputter` |  |  |  |
| 7 | `IM.UP.DATE.TIME` | `ImDocumentUpload_DateTime` |  |  |  |
| 8 | `IM.UP.AUTHORISER` | `ImDocumentUpload_Authoriser` | String |  |  |
| 9 | `IM.UP.CO.CODE` | `ImDocumentUpload_CoCode` | String |  |  |
| 10 | `IM.UP.DEPT.CODE` | `ImDocumentUpload_DeptCode` | String |  |  |
| 11 | `IM.UP.AUDITOR.CODE` | `ImDocumentUpload_AuditorCode` | String |  |  |
| 12 | `IM.UP.AUDIT.DATE.TIME` | `ImDocumentUpload_AuditDateTime` | String |  |  |
