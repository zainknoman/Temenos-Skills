# PP.RMA — Table Schema

> Source: `INSERTS/I_F.PP.RMA` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RMA.CompanyID` | `PpRma_Companyid` |  |  |  |
| 2 | `PP.RMA.SwiftService` | `PpRma_Swiftservice` | TField |  | Indicates type of SWIFT NET service for which the RMA applies. In addition to the SWIFT NET FIN service, with the adoption of the ISO20022 for cross border payments,theauthorisation for "swift.fin" and "swift.finplus" services will be received as separate records in the RMA filedistribution. Validation Rules: 35 alphanumeric characters. |
| 3 | `PP.RMA.MessageTypeInclude` | `PpRma_Messagetypeinclude` | TField |  | Indicates message types for which the RMA is not applicable for both MT and ISO messages. It can hold wildcards. To define an entry that excludes authorization for all the Cat - 1 messages with the exception of MT110&#44; the &apos;Include message Type&apos; would be storedwith 110 and the &apos;Exclude Message Type&apos; would be stored with 1*. To define an entry that excludes authorization for all the pacs messages&#44; with the exception of pacs.004 andpacs.008&#44; the &apos;Exclude message Type&apos; would be stored with pacs* and the &apos;include Message Type&apos; would be stored with pacs.004&#44; pacs.008. Together with Message Type Include&#44; it will give the messages for which the RMA is applicable. To define an entry that includes authorization of all the messages it should have a value of * If * has been specified cannot specify value in MessageTypeExclude Validation Rules: 250 alphabetic characters. We refer the message.name.id first 2 components for PP.RMA definition. So, Format for defining ISO messages should be like 4alpha.numeric or 4alpha* (eg.pacs.008/pacs*) If the MessageTypeInclude field is to be inputted with more than 250 alphabetic characters, an EB.OBJECT record needs to be created by giving the required length in the Max Length field. NOTE: If Creating EB.OBJECT the Record Id Should be "PP.RMA.MESSAGETYPE" |
| 4 | `PP.RMA.MessageTypeExclude` | `PpRma_Messagetypeexclude` | TField |  | Indicates message types for which the RMA is applicable for both MT and ISO messages. It can hold wildcards. Example: To define an entry that includes authorization for all the Cat - 2 messages with the exception of MT204 andMT207&#44; the &apos;Include message Type&apos; would be stored with 2* and the &apos;Exclude Message Type&apos; would be stored with 204&#44; 207. To define an entry that includes authorization for all the pacs messages&#44; with the exception of pacs.004 andpacs.008&#44; the &apos;Include message Type&apos; would be stored with pacs* and the &apos;Exclude Message Type&apos; would be stored with pacs.004&#44; pacs.008. Together with Message Type Exclude&#44; it will give the messages for which the RMA is applicable. To define an entry that excludes authorization of all the messages it should have a value of * If * has been specified cannot specify value in MessageTypeInclude Validation Rules: 250 alphabetic characters. We refer the message.name.id first 2 components for PP.RMA definition So, Format for defining ISO messages should be like 4alpha.numeric or 4alpha* (eg.pacs.008/pacs*) If the MessageTypeExclude field is to be inputted with more than 250 alphabetic characters, an EB.OBJECT record needs to be created by giving the required length in the Max Length field. NOTE: If Creating EB.OBJECT the Record Id Should be "PP.RMA.MESSAGETYPE" |
| 5 | `PP.RMA.OverrideThroughUpload` | `PpRma_Overridethroughupload` | TField |  | Indicates whether the record can be updated using an automated upload process in the payments hub. Possible values: Y &#x2010; The entry is manually updated and can be overridden by the upload process. N &#x2010; The entry is manual updated and the upload process should not override it. Any manually updated record in the RMA table is marked as manually updated. Subsequently&#44; the upload processshould not go on to rewrite these records with the contents of the upload file. A manually updated record hasgreater significance and therefore should not be replaced by the upload process. Validation Rules: A maximum of 1 characters may be entered based on possible values. |
| 6 | `PP.RMA.StartDate` | `PpRma_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Validation Rules: NoInput Field |
| 7 | `PP.RMA.EndDate` | `PpRma_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post thisdate&#44; the record will be set as Inactive by the payments hub. |
| 8 | `PP.RMA.ValidFrom` | `PpRma_ValidFrom` |  |  |  |
| 9 | `PP.RMA.AuthType` | `PpRma_AuthType` |  |  |  |
| 10 | `PP.RMA.RmaStatus` | `PpRma_RmsStatus` |  |  |  |
| 11 | `PP.RMA.IssueDateTime` | `PpRma_IssueDateTime` |  |  |  |
| 12 | `PP.RMA.Issuer` | `PpRma_Issuer` | TField |  | The correspondent which issued the authorisation to receive messages from the Temenos Bank Validation Rules: Not allowed for manual input. If not specified,Bic8 value of Id will be defaulted. |
| 13 | `PP.RMA.LOCAL.REF` | `PpRma_LocalRef` |  |  |  |
| 14 | `PP.RMA.OVERRIDE` | `PpRma_Override` |  |  |  |
| 15 | `PP.RMA.RECORD.STATUS` | `PpRma_RecordStatus` | String |  |  |
| 16 | `PP.RMA.CURR.NO` | `PpRma_CurrNo` | String |  |  |
| 17 | `PP.RMA.INPUTTER` | `PpRma_Inputter` |  |  |  |
| 18 | `PP.RMA.DATE.TIME` | `PpRma_DateTime` |  |  |  |
| 19 | `PP.RMA.AUTHORISER` | `PpRma_Authoriser` | String |  |  |
| 20 | `PP.RMA.CO.CODE` | `PpRma_CoCode` | String |  |  |
| 21 | `PP.RMA.DEPT.CODE` | `PpRma_DeptCode` | String |  |  |
| 22 | `PP.RMA.AUDITOR.CODE` | `PpRma_AuditorCode` | String |  |  |
| 23 | `PP.RMA.AUDIT.DATE.TIME` | `PpRma_AuditDateTime` | String |  |  |
| 24 | `PP.RMA.UploadType` | `PpRma_UploadType` |  |  |  |
| 25 | `PP.RMA.UpldFileCreateDateTime` | `PpRma_UpldFileCreateDateTime` |  |  |  |
| 26 | `PP.RMA.UpldFileName` | `PpRma_UpldFileName` |  |  |  |
| 27 | `PP.RMA.LastUpdateDate` | `PpRma_LastUpdateDate` |  |  |  |
| 28 | `PP.RMA.ExceptionReason` | `PpRma_ExceptionReason` |  |  |  |
