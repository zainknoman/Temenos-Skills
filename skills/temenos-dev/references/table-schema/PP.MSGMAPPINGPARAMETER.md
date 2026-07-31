# PP.MSGMAPPINGPARAMETER — Table Schema

> Source: `INSERTS/I_F.PP.MSGMAPPINGPARAMETER` in `PP_MessageMappingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MMP.DebulkAPI` | `PpMsgmappingparameter_Debulkapi` | TField |  | API to be used to debulk a clearing/batch message. Validation Rules: 255 alphanumeric characters. |
| 2 | `PP.MMP.MappingAPI` | `PpMsgmappingparameter_Mappingapi` | TField | Yes | API to be used to map a payment file to payment order. Validation Rules: Mandatory field. 255 alphanumeric characters. |
| 3 | `PP.MMP.SourceTypeAPI` | `PpMsgmappingparameter_Sourcetypeapi` | TField |  | API to copy the "Received Source" to "Originating Source" and make bank specific changes to the "Originating Source". Validation Rules Specify either A jBC implementation using a valid EB.API record with a source type of BASIC For java implementations: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record PP.MSGMAPPINGPARAM.SrcTypeApi.HOOK. This field supports the PaymentLifecycle.getSource() and PaymentLifecycle.getSwiftSource() methods. The PaymentLifecycle class is in the com.temenos.t24.api.hook.payments package which is in PP_PaymentLifecycleHook.jar shipped with T24. 255 alphanumeric characters. |
| 4 | `PP.MMP.ClearingTransactionType` | `PpMsgmappingparameter_Clearingtransactiontype` | TField |  | This field is used to maintain a distinction between returns / refunds and normal incoming credit transfers / direct debits Validation Rules: 2 alphanumeric characters The value links to the field 'ClearingTransactionType' in PPT.TRANSACTIONTYPES table. |
| 5 | `PP.MMP.ClearingNatureCode` | `PpMsgmappingparameter_Clearingnaturecode` |  |  |  |
| 6 | `PP.MMP.EnrichAPI` | `PpMsgmappingparameter_Enrichapi` | TField |  | API used to enrich values in transaction tables and log Audit Trail accordingly for informational purposes. Validation Rules Specify either A jBC implementation using a valid EB.API record with a source type of BASIC For java implementations: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record MAPPING.PARAMETER.ENRICH.API.HOOK. This field supports the Message.updateInformationLine() and Message.updatePaymentObject() methods. The PaymentLifecycle class is in the com.temenos.t24.api.hook.message package which is in PP_MessageHook.jar shipped with T24. An EB.API record of type METHOD which implements an interface defined in the EB.API record MAPPING.PARAMETER.ENRICH.API.HOOK. |
| 7 | `PP.MMP.BulkDuplicateCheckID` | `PpMsgmappingparameter_Bulkduplicatecheckid` | TField |  | This field indicates if bulk duplicate check must be performed or not for all files received by TPH. If duplicate check must be performed then it must be populated with ID from EB.DUPLICATE.TYPE Validation Rules: The value in this field should be a valid definition in the table EB.DUPLICATE.TYPE If duplicate check must not be performed then this field must be left blank. |
| 8 | `PP.MMP.AgreementValidationCriteriaAPI` | `PpMsgmappingparameter_Agreementvalidationcriteriaapi` | TField |  | This API is responsible for retrieving the sending BIC and the service type from the file level details or bulk level details of a file received from indirect participant. These details will be used to determine if the IP has an agreement with the processing bank to send the file for the service type If IP Validation check must be skipped for certain message types then this field must be left blank. |
| 9 | `PP.MMP.LOCAL.REF` | `PpMsgmappingparameter_LocalRef` |  |  |  |
| 10 | `PP.MMP.OVERRIDE` | `PpMsgmappingparameter_Override` |  |  |  |
| 11 | `PP.MMP.RECORD.STATUS` | `PpMsgmappingparameter_RecordStatus` | String |  |  |
| 12 | `PP.MMP.CURR.NO` | `PpMsgmappingparameter_CurrNo` | String |  |  |
| 13 | `PP.MMP.INPUTTER` | `PpMsgmappingparameter_Inputter` |  |  |  |
| 14 | `PP.MMP.DATE.TIME` | `PpMsgmappingparameter_DateTime` |  |  |  |
| 15 | `PP.MMP.AUTHORISER` | `PpMsgmappingparameter_Authoriser` | String |  |  |
| 16 | `PP.MMP.CO.CODE` | `PpMsgmappingparameter_CoCode` | String |  |  |
| 17 | `PP.MMP.DEPT.CODE` | `PpMsgmappingparameter_DeptCode` | String |  |  |
| 18 | `PP.MMP.AUDITOR.CODE` | `PpMsgmappingparameter_AuditorCode` | String |  |  |
| 19 | `PP.MMP.AUDIT.DATE.TIME` | `PpMsgmappingparameter_AuditDateTime` | String |  |  |
| 20 | `PP.MMP.InstantLocalInstrumentCode` | `PpMsgmappingparameter_Instantlocalinstrumentcode` |  |  |  |
| 21 | `PP.MMP.InstantPaymentMethod` | `PpMsgmappingparameter_Instantpaymentmethod` |  |  |  |
| 22 | `PP.MMP.OriginalPmtIDAPI` | `PpMsgmappingparameter_Originalpmtidapi` | TField |  | Hook API to determine the original payment transaction number for which a return or reversal received in TPH. If left blank, the original transaction need not to be retrieved during mapping stage. |
| 23 | `PP.MMP.SkipFileBulkUpdate` | `PpMsgmappingparameter_Skipfilebulkupdate` | TField |  | Field to indicate if the Inward Mapping Framework has to skip updates to the tables PPT.RECEIVEDFILEDETAILS, PPT.RECEIVEDBULKDETAILS and map only the Payment tables(POR). Possible values are Blank, INST and NRINST |
