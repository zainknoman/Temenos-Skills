# PP.INBOUND.OUTBOUND.CDWMP — Table Schema

> Source: `INSERTS/I_F.PP.INBOUND.OUTBOUND.CDWMP` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ICM.CompanyID` | `PpInboundOutboundCdwmp_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.ICM.IncomingCodeword` | `PpInboundOutboundCdwmp_Incomingcodeword` | TField | Yes | Specifies the codeword which is received in the payment message. Validation Rules: Mandatory fields. 8 alphanumeric characters. |
| 3 | `PP.ICM.IncomingInformationCode` | `PpInboundOutboundCdwmp_Incominginformationcode` | TField |  | Specifies the information code of the incoming message. The SWIFT tags containing the codeword. Possible values: TIMIND INSBNK INSSDR REGREP |
| 4 | `PP.ICM.OriginatingSource` | `PpInboundOutboundCdwmp_Originatingsource` | TField |  | Specifies the source of the payment. Validation Rules: Value links to field 'Source' in PP.SOURCE. Default value of �*� is set. |
| 5 | `PP.ICM.ReceiverBankBIC` | `PpInboundOutboundCdwmp_Receiverbankbic` | TField |  | Specifies the BIC of the receiver bank. Validation Rules: Field is a free text field, but it is checked against field 'BICCode' in PPT.BICTABLE. Wildcard character "*" is also allowed. |
| 6 | `PP.ICM.CodewordRanking` | `PpInboundOutboundCdwmp_Codewordranking` |  |  |  |
| 7 | `PP.ICM.IncomingCodewordText` | `PpInboundOutboundCdwmp_Incomingcodewordtext` |  |  |  |
| 8 | `PP.ICM.IncomingMessagePaymentType` | `PpInboundOutboundCdwmp_Incomingmessagepaymenttype` |  |  |  |
| 9 | `PP.ICM.OutboundMessagePaymentType` | `PpInboundOutboundCdwmp_Outboundmessagepaymenttype` |  |  |  |
| 10 | `PP.ICM.TransactionCurrency` | `PpInboundOutboundCdwmp_Transactioncurrency` |  |  |  |
| 11 | `PP.ICM.MessagePriority` | `PpInboundOutboundCdwmp_Messagepriority` |  |  |  |
| 12 | `PP.ICM.OutboundInformationCode` | `PpInboundOutboundCdwmp_Outboundinformationcode` |  |  |  |
| 13 | `PP.ICM.OutboundCodeword` | `PpInboundOutboundCdwmp_Outboundcodeword` |  |  |  |
| 14 | `PP.ICM.OutboundCodewordText` | `PpInboundOutboundCdwmp_Outboundcodewordtext` |  |  |  |
| 15 | `PP.ICM.ProcessingSequenceNumber` | `PpInboundOutboundCdwmp_Processingsequencenumber` |  |  |  |
| 16 | `PP.ICM.OutboundCodewordPriority` | `PpInboundOutboundCdwmp_Outboundcodewordpriority` |  |  |  |
| 17 | `PP.ICM.StartDate` | `PpInboundOutboundCdwmp_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. This is made NOINPUT field. On click of validate button, StartDate gets autopopulated from ID field. This date can be CurrentBusinessDate or Future Dated. |
| 18 | `PP.ICM.EndDate` | `PpInboundOutboundCdwmp_Enddate` | TField | Yes | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. This field is made non mandatory. It can be left blank and can be assumed that record will not expire. |
| 19 | `PP.ICM.RESERVED.5` | `PpInboundOutboundCdwmp_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 20 | `PP.ICM.RESERVED.4` | `PpInboundOutboundCdwmp_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 21 | `PP.ICM.RESERVED.3` | `PpInboundOutboundCdwmp_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 22 | `PP.ICM.RESERVED.2` | `PpInboundOutboundCdwmp_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 23 | `PP.ICM.RESERVED.1` | `PpInboundOutboundCdwmp_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 24 | `PP.ICM.LOCAL.REF` | `PpInboundOutboundCdwmp_LocalRef` |  |  |  |
| 25 | `PP.ICM.LinkID` | `PpInboundOutboundCdwmp_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. For EX: OTHRINSBNK103SWIFT-20160406 |
| 26 | `PP.ICM.OVERRIDE` | `PpInboundOutboundCdwmp_Override` |  |  |  |
| 27 | `PP.ICM.RECORD.STATUS` | `PpInboundOutboundCdwmp_RecordStatus` | String |  |  |
| 28 | `PP.ICM.CURR.NO` | `PpInboundOutboundCdwmp_CurrNo` | String |  |  |
| 29 | `PP.ICM.INPUTTER` | `PpInboundOutboundCdwmp_Inputter` |  |  |  |
| 30 | `PP.ICM.DATE.TIME` | `PpInboundOutboundCdwmp_DateTime` |  |  |  |
| 31 | `PP.ICM.AUTHORISER` | `PpInboundOutboundCdwmp_Authoriser` | String |  |  |
| 32 | `PP.ICM.CO.CODE` | `PpInboundOutboundCdwmp_CoCode` | String |  |  |
| 33 | `PP.ICM.DEPT.CODE` | `PpInboundOutboundCdwmp_DeptCode` | String |  |  |
| 34 | `PP.ICM.AUDITOR.CODE` | `PpInboundOutboundCdwmp_AuditorCode` | String |  |  |
| 35 | `PP.ICM.AUDIT.DATE.TIME` | `PpInboundOutboundCdwmp_AuditDateTime` | String |  |  |
