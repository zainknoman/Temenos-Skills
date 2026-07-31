# EB.FILE.UPLOAD.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.FILE.UPLOAD.TYPE` in `EB_FileUpload.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.UT.DESCRIPTION` | `EbFileUploadType_Description` |  |  |  |
| 2 | `EB.UT.UPLOAD.DIR` | `EbFileUploadType_UploadDir` | TField | Yes | Warning! Changing the value of this field will require any existing uploaded files to be moved manually to the new directory. Mandatory field. This specifies which directory files will be uploaded to. This directory will be relative to the directory specified in the EB.FILE.UPLOAD.PARAM / SYSTEM / TC.UPLOAD.DIR field. The TC server process must have permissions to write to the directory specified in this field. |
| 3 | `EB.UT.EXTENSION` | `EbFileUploadType_Extension` | TField | No | Optional field. If set, then only files with that extension will be uploaded. The system generated filename will also be given the extension provided. If this field is not set, then any file type can be uploaded, and the system generated name will be the SIGN.ON.NAME plus a time stamp. A leading period character to delimit the extension will be added automatically if none is specified. This field is not case sensitive. An extension of 'csv' will allow 'CSV' files to be uploaded. |
| 4 | `EB.UT.MAX.SIZE` | `EbFileUploadType_MaxSize` | TField | No | Optional field. If set, then specifies a maximum size (in bytes) to be uploaded. If not set, then the system will not place any artificial limits on the upload file size. |
| 5 | `EB.UT.HDR.UPD.APPL` | `EbFileUploadType_HdrUpdAppl` | TField | Yes | This field must contain a valid application name. PGM.FILE type must be H,U,L. This field indicates the application to be used in the uploaded file for HEADER. It is a Mandatory field. |
| 6 | `EB.UT.HDR.UPD.VERSION` | `EbFileUploadType_HdrUpdVersion` | TField | Yes | This field contains a valid version belonging to the application mentioned in HDR.UPD.APPL. This field indicates the version to be used to create records in HEADER APPLICATION Mandatory field. |
| 7 | `EB.UT.SEPARATOR` | `EbFileUploadType_Separator` | TField | Yes | Contains the value of the field delimiter that used in the uploaded file. The delimiter may be any single character. Mandatory field |
| 8 | `EB.UT.ITEMS.UPD.APPL` | `EbFileUploadType_ItemsUpdAppl` | TField | Yes | This field must contain a valid application name. PGM.FILE type must H, U and L. This field indicates the application to be used in the uploaded file for ITEMS. It is a Mandatory field. |
| 9 | `EB.UT.ITEMS.UPD.VERSION` | `EbFileUploadType_ItemsUpdVersion` | TField | Yes | This field contains a valid version belonging to the application mentioned in ITEMS.UPD.APPL This field indicates the version to be used to create records in ITEMS APPLICATION It is a Mandatory field. |
| 10 | `EB.UT.REFORMAT.PLUGIN` | `EbFileUploadType_ReformatPlugin` | TField | No | A valid plug-in to reformat the file. Input must be an ID in EB.API Optional field. This routine should process and Modify the line STRING specified for the HEADER &amp; LINES application in run time. The format plug-in routine should have 4 arguments ARG 1: to specify the processing string is a HEADER string or ITEMS strings ARG 2: to specify a line number ARG 3: to specify an EB.FILE.UPLOAD id ARG 4: to specify the line string to process |
| 11 | `EB.UT.HEADER.POSITION` | `EbFileUploadType_HeaderPosition` | TField | Yes | This field indicates the position of the header in the uploaded file. Value should be numeric. Mandatory field |
| 12 | `EB.UT.HDR.ID.INCLUDED` | `EbFileUploadType_HdrIdIncluded` | TField | No | This field indicates whether the id is specified in the uploaded file for HEADER or not. If the field specified to YES then first column of the uploaded file contains the id of the transaction. Optional field. Validation Rules: : YES or NO field |
| 13 | `EB.UT.ITEMS.ID.INCLUDED` | `EbFileUploadType_ItemsIdIncluded` | TField | No | This field indicates whether the id is specified in the uploaded for ITEMS file or not. If the field specified to YES then first column of the uploaded file contains the id of the transaction. Optional field. Validation Rules: : YES or NO field |
| 14 | `EB.UT.T24.FILE` | `EbFileUploadType_T24File` | TField |  | This field determines whether the Uploaded file via EB.FILE.UPLOAD is of Standard T24 File to be processed via Service or the corresponding EB.FILE.UPLOAD is for uploading file like PDF. Possible values: YES , NO or NULL NULL value or Y denotes that it is a T24.FILE to be picked up the service and also force values for fields HDR.UPD.APPL, HDR.UPD.VERSION, ITEMS.UPD.APPL, ITEMS.UPD.VERSION, SEPARATER and HEADER.POSITION etc and if the value is N then these fields cannot be input and this type of EB.FILE.UPLOAD records will not be picked up by the service. |
| 15 | `EB.UT.FIXED.LENGTH` | `EbFileUploadType_FixedLength` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `EB.UT.INTERFACE.ROUTINE` | `EbFileUploadType_InterfaceRoutine` | TField |  |  |
| 17 | `EB.UT.LOCAL.REF` | `EbFileUploadType_LocalRef` |  |  |  |
| 18 | `EB.UT.OVERRIDE` | `EbFileUploadType_Override` |  |  |  |
| 19 | `EB.UT.RECORD.STATUS` | `EbFileUploadType_RecordStatus` | String |  |  |
| 20 | `EB.UT.CURR.NO` | `EbFileUploadType_CurrNo` | String |  |  |
| 21 | `EB.UT.INPUTTER` | `EbFileUploadType_Inputter` |  |  |  |
| 22 | `EB.UT.DATE.TIME` | `EbFileUploadType_DateTime` |  |  |  |
| 23 | `EB.UT.AUTHORISER` | `EbFileUploadType_Authoriser` | String |  |  |
| 24 | `EB.UT.CO.CODE` | `EbFileUploadType_CoCode` | String |  |  |
| 25 | `EB.UT.DEPT.CODE` | `EbFileUploadType_DeptCode` | String |  |  |
| 26 | `EB.UT.AUDITOR.CODE` | `EbFileUploadType_AuditorCode` | String |  |  |
| 27 | `EB.UT.AUDIT.DATE.TIME` | `EbFileUploadType_AuditDateTime` | String |  |  |
| 28 | `EB.UT.TRANSFORM.ID` | `EbFileUploadType_TransformId` | TField | No | Optional field which holds the valid id from EB.TRANSFORM application This field is applicable only for XML files to validate the uploaded XML file against the XSL defined in EB.TRANSFORM record |
| 29 | `EB.UT.XSD.DIR` | `EbFileUploadType_XsdDir` | TField | No | Field applicable for XML file extensions. To specify the folder path where XSD files are available. Optional field |
| 30 | `EB.UT.XSD.FILE` | `EbFileUploadType_XsdFile` | TField | No | Field applicable for XML file extensions. To hold the XSD file name against which the uploaded XML needs to be validated. Optional field |
| 31 | `EB.UT.XML.VALIDATION.ROUTINE` | `EbFileUploadType_XmlValidationRoutine` | TField | No | Field applicable for XML file extensions. Should hold a valid entry to EB.API application This routine validates the uploaded XML against the given XSD or XSL if specified. Optional field |
| 32 | `EB.UT.PRE.PROCESS.API` | `EbFileUploadType_PreProcessApi` | TField | Yes | This is a Non-Mandatory field, should hold a valid entry to EB.API application can be configured for the respective upload type and will be triggered only once for a file during the 'Header' processing it provides an opportunity for any vertical or bank to attach their own routine. |
| 33 | `EB.UT.SEPARATE.XML.PROCESS` | `EbFileUploadType_SeparateXmlProcess` | TField |  |  |
