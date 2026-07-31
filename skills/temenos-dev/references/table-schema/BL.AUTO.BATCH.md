# BL.AUTO.BATCH — Table Schema

> Source: `INSERTS/I_F.BL.AUTO.BATCH` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.AB.DESCRIPTION` | `BlAutoBatch_Description` |  |  |  |
| 2 | `BL.AB.UPLOAD.REF` | `BlAutoBatch_UploadRef` | TField |  | Specifies the upload reference for which auto batching of registers needs to be done based on rules defined in BL.BATCH.CONDITIONS. Validation Rules: Must be a valid Upload reference updated in BL.REGISTER. |
| 3 | `BL.AB.SELLER.ID` | `BlAutoBatch_SellerId` | TField | Yes | Specifies the customer for whom CHANGE PRODUCT (or) REBATCHING action needs to be triggered. Validation Rules: Mandatory when CHANGE.PRODUCT or REBATCH is selected Not allowed with upload reference Must be valid customer record. |
| 4 | `BL.AB.ACTION` | `BlAutoBatch_Action` | TField | Yes | Specifies the ACTION to be performed on the registers on whether to batch registers based on upload reference (or) rebatch the registers when product is changed. Validation Rules: Allowed values are "BATCH" and "REBATCH" Upload reference is mandatory for "BATCH" If upload reference is defined then default value must be BATCH Seller ID is mandatory when REBATCH option is selected. |
| 5 | `BL.AB.CHANGE.PRODUCT` | `BlAutoBatch_ChangeProduct` | TField | Yes | Specifies whether product change action needs to be triggered for seller based on CHANGE PRODUCT preset conditions defined in BL.BATCH.CONDITIONS Validation Rules: SELLER ID mandatory when CHANGE PRODUCT is defined Not allowed with upload reference |
| 6 | `BL.AB.PROCESSED.DATE` | `BlAutoBatch_ProcessedDate` | TField |  |  |
| 7 | `BL.AB.RESERVED5` | `BlAutoBatch_Reserved5` | TField |  |  |
| 8 | `BL.AB.RESERVED4` | `BlAutoBatch_Reserved4` | TField |  |  |
| 9 | `BL.AB.RESERVED3` | `BlAutoBatch_Reserved3` | TField |  |  |
| 10 | `BL.AB.RESERVED2` | `BlAutoBatch_Reserved2` | TField |  |  |
| 11 | `BL.AB.RESERVED1` | `BlAutoBatch_Reserved1` | TField |  |  |
| 12 | `BL.AB.LOCAL.REF` | `BlAutoBatch_LocalRef` |  |  |  |
| 13 | `BL.AB.OVERRIDE` | `BlAutoBatch_Override` |  |  |  |
| 14 | `BL.AB.RECORD.STATUS` | `BlAutoBatch_RecordStatus` | String |  |  |
| 15 | `BL.AB.CURR.NO` | `BlAutoBatch_CurrNo` | String |  |  |
| 16 | `BL.AB.INPUTTER` | `BlAutoBatch_Inputter` |  |  |  |
| 17 | `BL.AB.DATE.TIME` | `BlAutoBatch_DateTime` |  |  |  |
| 18 | `BL.AB.AUTHORISER` | `BlAutoBatch_Authoriser` | String |  |  |
| 19 | `BL.AB.CO.CODE` | `BlAutoBatch_CoCode` | String |  |  |
| 20 | `BL.AB.DEPT.CODE` | `BlAutoBatch_DeptCode` | String |  |  |
| 21 | `BL.AB.AUDITOR.CODE` | `BlAutoBatch_AuditorCode` | String |  |  |
| 22 | `BL.AB.AUDIT.DATE.TIME` | `BlAutoBatch_AuditDateTime` | String |  |  |
