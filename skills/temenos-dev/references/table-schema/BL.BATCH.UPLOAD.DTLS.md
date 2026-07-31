# BL.BATCH.UPLOAD.DTLS — Table Schema

> Source: `INSERTS/I_F.BL.BATCH.UPLOAD.DTLS` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.BU.UPLOAD.REF` | `BlBatchUploadDtls_UploadRef` | TField |  | Identifies the upload reference from uploaded file thru' EB.FILE.UPLOAD application. |
| 2 | `BL.BU.ITEMS.UPLOADED` | `BlBatchUploadDtls_ItemsUploaded` | TField |  | Identifies the total invoices uploaded thru' EB.FILE.UPLOAD application. Associated multi-value set with fields DOC.CCY and DOC.VALUE. |
| 3 | `BL.BU.DOC.CCY` | `BlBatchUploadDtls_DocCcy` |  |  |  |
| 4 | `BL.BU.DOC.VALUE` | `BlBatchUploadDtls_DocValue` |  |  |  |
| 5 | `BL.BU.ITEMS.PROCESSED` | `BlBatchUploadDtls_ItemsProcessed` | TField |  | Identifies the total invoices processed successfully by creating BL.REGISTER. Associated multi-value set with fields PROC.DOC.CCY and PROC.DOC.VALUE. |
| 6 | `BL.BU.PROC.DOC.CCY` | `BlBatchUploadDtls_ProcDocCcy` |  |  |  |
| 7 | `BL.BU.PROC.DOC.VALUE` | `BlBatchUploadDtls_ProcDocValue` |  |  |  |
| 8 | `BL.BU.ITEMS.ERR` | `BlBatchUploadDtls_ItemsErr` | TField |  | Identifies the total invoices in errors which has failed during creation of BL.REGISTER. Associated multi-value set with fields ERR.DOC.CCY and ERR.DOC.VALUE. |
| 9 | `BL.BU.ERR.DOC.CCY` | `BlBatchUploadDtls_ErrDocCcy` |  |  |  |
| 10 | `BL.BU.ERR.DOC.VALUE` | `BlBatchUploadDtls_ErrDocValue` |  |  |  |
