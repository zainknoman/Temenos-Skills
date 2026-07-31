# EB.SECURE.MESSAGE — Table Schema

> Source: `INSERTS/I_F.EB.SECURE.MESSAGE` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SM.TO.CUSTOMER` | `EbSecureMessage_ToCustomer` | TField |  | Must be a valid record id on customer table. Customer to which the message to be sent. Validation Rules: : Noinput field if the message is triggered from external user. |
| 2 | `EB.SM.TO.DAO` | `EbSecureMessage_ToDao` | TField |  | Must be a valid record id on department account officer table. Account Offcier to which the message to be sent. Validation Rules: : For external user, list of allowed DAO for messageing will be populated in this field.Otherwise, it is noinput field. |
| 3 | `EB.SM.FROM.DAO` | `EbSecureMessage_FromDao` | TField |  | Must be a valid record id on department account officer table. Account Offcier from which the message is triggered. Validation Rules: : DEPARTMENT.CODE on USER record will be populated if the message is triggered from internal users. |
| 4 | `EB.SM.FROM.CUSTOMER` | `EbSecureMessage_FromCustomer` | TField |  | Input must be a valid record id on customer table. Customer from which the message is triggered. Validation Rules: : Noinput field. External customer id will be populated for external users. |
| 5 | `EB.SM.SUBJECT` | `EbSecureMessage_Subject` | TField |  | This field contains the subject of the message to be sent or received. |
| 6 | `EB.SM.MESSAGE` | `EbSecureMessage_Message` |  |  |  |
| 7 | `EB.SM.DATE.SENT` | `EbSecureMessage_DateSent` | TField |  | Holds the date when the message is sent. Validation Rules: : Noinput field. This field will be updated when the message is authorised. |
| 8 | `EB.SM.TIME.SENT` | `EbSecureMessage_TimeSent` | TField |  | Specifies time when the message is sent. Validation Rules: : Noinput field. This field will be updated when the message is authorised. |
| 9 | `EB.SM.DATE.READ` | `EbSecureMessage_DateRead` | TField |  | It holds date when the message is read. Validation Rules: : Noinput field. This field will be updated when the message is read by the receiver. |
| 10 | `EB.SM.TO.STATUS` | `EbSecureMessage_ToStatus` | TField |  | Specifies status of the message. Default is UNREAD. Validation Rules: : It has two options. They are UNREAD and READ. |
| 11 | `EB.SM.FROM.STATUS` | `EbSecureMessage_FromStatus` | TField |  | This field specifies status of the received message. Default is SENT. Validation Rules: : It has two options. They are SENT and UNSENT. |
| 12 | `EB.SM.PARENT.MESSAGE.ID` | `EbSecureMessage_ParentMessageId` | TField |  | This field specifies the record ID of parent message. |
| 13 | `EB.SM.UPLOAD.ID` | `EbSecureMessage_UploadId` | TField |  | Holds the Image id when the upload attachment is required. Validation Rules: : NoInput field. The record id of the IM.DOCUMENT.IMAGE record which the file being uploaded will be linked to. |
| 14 | `EB.SM.FILE.UPLOAD` | `EbSecureMessage_FileUpload` | TField |  | The field uses a file browser to locate and display the file. Validation Rules: : The field uses a file browser to locate and display the file.When the link button is clicked the file is both renamed and then downloaded to the storage path specified in the IM.DOCUMENT.TYPE. |
| 15 | `EB.SM.RESERVED.8` | `EbSecureMessage_Reserved8` | TField |  |  |
| 16 | `EB.SM.RESERVED.7` | `EbSecureMessage_Reserved7` | TField |  |  |
| 17 | `EB.SM.RESERVED.6` | `EbSecureMessage_Reserved6` | TField |  |  |
| 18 | `EB.SM.RESERVED.5` | `EbSecureMessage_Reserved5` | TField |  |  |
| 19 | `EB.SM.RESERVED.4` | `EbSecureMessage_Reserved4` | TField |  |  |
| 20 | `EB.SM.RESERVED.3` | `EbSecureMessage_Reserved3` | TField |  |  |
| 21 | `EB.SM.RESERVED.2` | `EbSecureMessage_Reserved2` | TField |  |  |
| 22 | `EB.SM.RESERVED.1` | `EbSecureMessage_Reserved1` | TField |  |  |
| 23 | `EB.SM.LOCAL.REF` | `EbSecureMessage_LocalRef` |  |  |  |
| 24 | `EB.SM.OVERRIDE` | `EbSecureMessage_Override` |  |  |  |
| 25 | `EB.SM.RECORD.STATUS` | `EbSecureMessage_RecordStatus` | String |  |  |
| 26 | `EB.SM.CURR.NO` | `EbSecureMessage_CurrNo` | String |  |  |
| 27 | `EB.SM.INPUTTER` | `EbSecureMessage_Inputter` |  |  |  |
| 28 | `EB.SM.DATE.TIME` | `EbSecureMessage_DateTime` |  |  |  |
| 29 | `EB.SM.AUTHORISER` | `EbSecureMessage_Authoriser` | String |  |  |
| 30 | `EB.SM.CO.CODE` | `EbSecureMessage_CoCode` | String |  |  |
| 31 | `EB.SM.DEPT.CODE` | `EbSecureMessage_DeptCode` | String |  |  |
| 32 | `EB.SM.AUDITOR.CODE` | `EbSecureMessage_AuditorCode` | String |  |  |
| 33 | `EB.SM.AUDIT.DATE.TIME` | `EbSecureMessage_AuditDateTime` | String |  |  |
