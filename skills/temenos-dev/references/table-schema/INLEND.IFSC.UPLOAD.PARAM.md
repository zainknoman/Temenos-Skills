# INLEND.IFSC.UPLOAD.PARAM — Table Schema

> Source: `INSERTS/I_F.INLEND.IFSC.UPLOAD.PARAM` in `INSFMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.UPLOAD.PARAM.CUSTOMER.VERSION` | `InlendIfscUploadParam_CustomerVersion` | TField |  | This will be the version that is used for the creation of CUSTOMER record by using some values from RD.CENTRAL.BANK.DIR and other default values Validation : Valid version of CUSTOMER application |
| 2 | `INLEND.UPLOAD.PARAM.DE.ADDRESS.VERISON` | `InlendIfscUploadParam_DeAddressVerison` | TField |  | This will be the version of DE.ADDRESS application that will be used to create a record by picking the IFSC and one value from CUSTOMER record.Validation : Valid version of DE.ADDRESS application |
| 3 | `INLEND.UPLOAD.PARAM.IFSC.INACTIVE.MARKING.VERSION` | `InlendIfscUploadParam_IfscInactiveMarkingVersion` | TField |  | This will be the version of RD.CENTRAL.BANK.DIR application that will be used to mark the IFSC code as Inactive using the OFS service.Validation : Valid version of RD.CENTRAL.BANK.DIR application |
| 4 | `INLEND.UPLOAD.PARAM.OFS.SOURCE` | `InlendIfscUploadParam_OfsSource` | TField |  | This OFS source will be responsible for the creation of CUSTOMER and DE.ADDRESS once IFSC upload is completed. |
| 5 | `INLEND.UPLOAD.PARAM.IFSC.REASON.FOR.INACTIVE` | `InlendIfscUploadParam_IfscReasonForInactive` | TField |  | When the IFSC codes are being marked as Inactive through service, the reason for marking the field as Inactive will be picked from this field. The configuration should be done here, for marking the default reason.Validation : Should be a valid Inactive reason from the EB.LOOKUP of RD.CENTRAL.BANK.DIR>IFSC.INACTIVE.REASON. |
| 6 | `INLEND.UPLOAD.PARAM.RESERVED.10` | `InlendIfscUploadParam_Reserved10` | TField |  |  |
| 7 | `INLEND.UPLOAD.PARAM.RESERVED.9` | `InlendIfscUploadParam_Reserved9` | TField |  |  |
| 8 | `INLEND.UPLOAD.PARAM.RESERVED.8` | `InlendIfscUploadParam_Reserved8` | TField |  |  |
| 9 | `INLEND.UPLOAD.PARAM.RESERVED.7` | `InlendIfscUploadParam_Reserved7` | TField |  |  |
| 10 | `INLEND.UPLOAD.PARAM.RESERVED.6` | `InlendIfscUploadParam_Reserved6` | TField |  |  |
| 11 | `INLEND.UPLOAD.PARAM.RESERVED.5` | `InlendIfscUploadParam_Reserved5` | TField |  |  |
| 12 | `INLEND.UPLOAD.PARAM.RESERVED.4` | `InlendIfscUploadParam_Reserved4` | TField |  |  |
| 13 | `INLEND.UPLOAD.PARAM.RESERVED.3` | `InlendIfscUploadParam_Reserved3` | TField |  |  |
| 14 | `INLEND.UPLOAD.PARAM.RESERVED.2` | `InlendIfscUploadParam_Reserved2` | TField |  |  |
| 15 | `INLEND.UPLOAD.PARAM.RESERVED.1` | `InlendIfscUploadParam_Reserved1` | TField |  |  |
| 16 | `INLEND.UPLOAD.PARAM.LOCAL.REF` | `InlendIfscUploadParam_LocalRef` |  |  |  |
| 17 | `INLEND.UPLOAD.PARAM.OVERRIDE` | `InlendIfscUploadParam_Override` |  |  |  |
| 18 | `INLEND.UPLOAD.PARAM.RECORD.STATUS` | `InlendIfscUploadParam_RecordStatus` | String |  |  |
| 19 | `INLEND.UPLOAD.PARAM.CURR.NO` | `InlendIfscUploadParam_CurrNo` | String |  |  |
| 20 | `INLEND.UPLOAD.PARAM.INPUTTER` | `InlendIfscUploadParam_Inputter` |  |  |  |
| 21 | `INLEND.UPLOAD.PARAM.DATE.TIME` | `InlendIfscUploadParam_DateTime` |  |  |  |
| 22 | `INLEND.UPLOAD.PARAM.AUTHORISER` | `InlendIfscUploadParam_Authoriser` | String |  |  |
| 23 | `INLEND.UPLOAD.PARAM.CO.CODE` | `InlendIfscUploadParam_CoCode` | String |  |  |
| 24 | `INLEND.UPLOAD.PARAM.DEPT.CODE` | `InlendIfscUploadParam_DeptCode` | String |  |  |
| 25 | `INLEND.UPLOAD.PARAM.AUDITOR.CODE` | `InlendIfscUploadParam_AuditorCode` | String |  |  |
| 26 | `INLEND.UPLOAD.PARAM.AUDIT.DATE.TIME` | `InlendIfscUploadParam_AuditDateTime` | String |  |  |
