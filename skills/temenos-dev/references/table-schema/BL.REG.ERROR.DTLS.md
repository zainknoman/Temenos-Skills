# BL.REG.ERROR.DTLS — Table Schema

> Source: `INSERTS/I_F.BL.REG.ERROR.DTLS` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.ED.ERROR.STAGE` | `BlRegErrorDtls_ErrorStage` | TField |  | Identifies the stage on when error is encountered.Errors can be encountered during following process. UPDATE PRODUCT - Error encountered during updation of product. BATCH - Error encountered during creation of batch. |
| 2 | `BL.ED.UPLOAD.REF` | `BlRegErrorDtls_UploadRef` | TField |  | Identifies the upload reference from uploaded file thru' EB.FILE.UPLOAD application. |
| 3 | `BL.ED.ERROR.MSG` | `BlRegErrorDtls_ErrorMsg` | TField |  | Identifies the details of error encountered during updation of product or creation of batch. |
| 4 | `BL.ED.PROCESS.DATE` | `BlRegErrorDtls_ProcessDate` | TField |  | Identifies the date on when errors are encountered during processing. |
| 5 | `BL.ED.STATUS` | `BlRegErrorDtls_Status` | TField |  | Indicates the status of error encountered during attaching product or batching. Pending - When any errors are encountered when product type is attached to BL.REGISTER thru' BL.UPDATE.PRODUCT service. Manual_Resolved - When product type is attached manually thru' BL.REGISTER. Auto_Resolved - When product type is successfully updated thru' online service BL.UPDATE.PRODUCT. |
| 6 | `BL.ED.DATE.RESOLVED` | `BlRegErrorDtls_DateResolved` | TField |  | Specifies the date on when update product or batching errors are rectified either thru' manually or thru' online service. |
