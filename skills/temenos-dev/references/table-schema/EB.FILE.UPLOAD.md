# EB.FILE.UPLOAD — Table Schema

> Source: `INSERTS/I_F.EB.FILE.UPLOAD` in `EB_FileUpload.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UF.UPLOAD.TYPE` | `EbFileUpload_UploadType` | TField | Conditional | Mandatory, NOCHANGE field. Can be specified in AUT.NEW.CONTENT in a VERSION. The upload type specifies the upload directory, and optionally a maximum upload size limit and file extension. Field is NOCHANGE because the system does not have the ability to move the file if the new UPLOAD.TYPE specifies a different location. |
| 2 | `EB.UF.SYSTEM.FILE.NAME` | `EbFileUpload_SystemFileName` | TField |  | The system will generate a new filename for the uploaded file. The filename will be made up of the SIGN.ON.NAME, a date time stamp (number of milli-seconds since January 1st 1970), and a file extension specified in the EB.FILE.UPLOAD.TYPE record. |
| 3 | `EB.UF.FILE.NAME` | `EbFileUpload_FileName` | TField |  | NOCHANGE field. Allows a file to be uploaded. Select the required file and click the upload button. |
| 4 | `EB.UF.STATUS` | `EbFileUpload_Status` | TField |  | NOINPUT field. Allows the system to track the processed status of the file once it has been uploaded. After initial upload, this field will be set to 'Uploaded'. |
| 5 | `EB.UF.DESCRIPTION` | `EbFileUpload_Description` | TField |  | Free form field for describing the upload. |
| 6 | `EB.UF.TARGET.COMPANY` | `EbFileUpload_TargetCompany` | TField |  | Allows the upload to be assigned to a company. |
| 7 | `EB.UF.UPLOAD.SIZE` | `EbFileUpload_UploadSize` | TField |  | NOINPUT field. Will be set to the size of the upload (in bytes) after validate / commit. |
| 8 | `EB.UF.UPLOAD.USER` | `EbFileUpload_UploadUser` | TField |  | NOINPUT field. The SIGN.ON.NAME of the user uploading the file. |
| 9 | `EB.UF.EXTERNAL.USER` | `EbFileUpload_ExternalUser` | TField |  | NOINPUT field. If the file is uploaded by an EB.EXTERNAL.USER, then this field will be set to the EB.EXTERNAL.USER ID on validate / commit. Otherwise will be blank. |
| 10 | `EB.UF.HEADER.ID` | `EbFileUpload_HeaderId` | TField |  | Id used in the upload process whose file is specified in the corresponding EB.FILE.UPLOAD.TYPE application in the field HDR.UPD.APPL No inputable field |
| 11 | `EB.UF.SERVICE.STATUS` | `EbFileUpload_ServiceStatus` | TField |  | This field contains the status of the service T24.UPLOAD.PROCESS. Possible values �PROCESSED�, �RECEIVED� , �PROCESSING� , �ERROR.IN.PROCESSING� RECEIVED: On committing the EB.FILE.UPLOAD record, system will update the service status field as 'RECEIVED' and those record are selected by the service T24.UPLOAD.PROCESS PROCESSING: once the uploaded record picked by the service then the record status changed from RECEIVED to PROCESSING PROCESSED: once the uploaded record are processed then the field status changed from �PROCESSING� to �PROCESSED� ERROR.IN.PROCESSING: if any error in the service then the field updated with the value as �ERROR.IN.PROCESSING� Noinputable field |
| 12 | `EB.UF.T24.FILE` | `EbFileUpload_T24File` | TField |  | This field determines whether the uploaded file via EB.FILE.UPLOAD is a Standard T24 File OR a file like PDF. This field value updated from the field T24.FILE in EB.FILE.UPLOAD.TYPE Possible values: �YES�, �NO� or �NULL� Noinputable field |
| 13 | `EB.UF.UPLOAD.DATE` | `EbFileUpload_UpdateDate` |  |  |  |
| 14 | `EB.UF.RESERVED.7` | `EbFileUpload_Reserved7` |  |  |  |
| 15 | `EB.UF.RESERVED.6` | `EbFileUpload_Reserved6` | TField |  |  |
| 16 | `EB.UF.RESERVED.5` | `EbFileUpload_Reserved5` | TField |  |  |
| 17 | `EB.UF.RESERVED.4` | `EbFileUpload_Reserved4` | TField |  |  |
| 18 | `EB.UF.RESERVED.3` | `EbFileUpload_Reserved3` | TField |  |  |
| 19 | `EB.UF.RESERVED.2` | `EbFileUpload_Reserved2` | TField |  |  |
| 20 | `EB.UF.RESERVED.1` | `EbFileUpload_Reserved1` | TField |  |  |
| 21 | `EB.UF.LOCAL.REF` | `EbFileUpload_LocalRef` |  |  |  |
| 22 | `EB.UF.OVERRIDE` | `EbFileUpload_Override` |  |  |  |
| 23 | `EB.UF.RECORD.STATUS` | `EbFileUpload_RecordStatus` | String |  |  |
| 24 | `EB.UF.CURR.NO` | `EbFileUpload_CurrNo` | String |  |  |
| 25 | `EB.UF.INPUTTER` | `EbFileUpload_Inputter` |  |  |  |
| 26 | `EB.UF.DATE.TIME` | `EbFileUpload_DateTime` |  |  |  |
| 27 | `EB.UF.AUTHORISER` | `EbFileUpload_Authoriser` | String |  |  |
| 28 | `EB.UF.CO.CODE` | `EbFileUpload_CoCode` | String |  |  |
| 29 | `EB.UF.DEPT.CODE` | `EbFileUpload_DeptCode` | String |  |  |
| 30 | `EB.UF.AUDITOR.CODE` | `EbFileUpload_AuditorCode` | String |  |  |
| 31 | `EB.UF.AUDIT.DATE.TIME` | `EbFileUpload_AuditDateTime` | String |  |  |
