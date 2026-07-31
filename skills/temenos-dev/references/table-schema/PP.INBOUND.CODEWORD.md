# PP.INBOUND.CODEWORD — Table Schema

> Source: `INSERTS/I_F.PP.INBOUND.CODEWORD` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.IC.CompanyID` | `PpInboundCodeword_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.IC.CodeWord` | `PpInboundCodeword_Codeword` | TField | Yes | The codeword received in the incoming payment message. Validation Rules: Mandatory field. 8 alphanumeric characters. |
| 3 | `PP.IC.InformationCode` | `PpInboundCodeword_Informationcode` | TField | Yes | Denotes the SWIFT information code containing the codeword. Possible Values: TIMIND INSBNK INSSDR REGREP INSBNK INSCVR Validation Rules: Mandatory field. 6 alphanumeric characters. |
| 4 | `PP.IC.MessagePaymentType` | `PpInboundCodeword_Messagepaymenttype` | TField | Yes | Indicates the type of the payment message. The value will be used as one of the criteria for selection of a record of this application based on peeling logic. Validation Rules: Mandatory field. 10 alphanumeric characters which includes '*'. Value links to field 'MessagePaymentType' in PP.MSGPAYMENTTYPE |
| 5 | `PP.IC.OriginatingSource` | `PpInboundCodeword_Originatingsource` | TField |  | Identifies the source of the payment message. Validation Rules: Value links to the field, 'Source' in PP.SOURCE A default value of "*" is set. |
| 6 | `PP.IC.CodeWordRanking` | `PpInboundCodeword_Codewordranking` |  |  |  |
| 7 | `PP.IC.CodeWordText` | `PpInboundCodeword_Codewordtext` |  |  |  |
| 8 | `PP.IC.CodeWordPriorityforPD` | `PpInboundCodeword_Codewordpriorityforpd` |  |  |  |
| 9 | `PP.IC.AdjustedMessagePriority` | `PpInboundCodeword_Adjustedmessagepriority` |  |  |  |
| 10 | `PP.IC.ProcessingSequenceNumber` | `PpInboundCodeword_Processingsequencenumber` |  |  |  |
| 11 | `PP.IC.NonSTPIndicator` | `PpInboundCodeword_Nonstpindicator` |  |  |  |
| 12 | `PP.IC.FeeCodewordFlag` | `PpInboundCodeword_Feecodewordflag` |  |  |  |
| 13 | `PP.IC.OutboundCwApplicableFlag` | `PpInboundCodeword_Outboundcwapplicableflag` |  |  |  |
| 14 | `PP.IC.StartDate` | `PpInboundCodeword_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. This is made NOINPUT field. On click of validate button, StartDate gets autopopulated from ID field. This date can be CurrentBusinessDate or Future Dated. |
| 15 | `PP.IC.EndDate` | `PpInboundCodeword_Enddate` | TField | Yes | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. This field is made non mandatory. It can be left blank and can be assumed that record will not expire. |
| 16 | `PP.IC.RESERVED.5` | `PpInboundCodeword_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 17 | `PP.IC.RESERVED.4` | `PpInboundCodeword_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 18 | `PP.IC.RESERVED.3` | `PpInboundCodeword_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 19 | `PP.IC.RESERVED.2` | `PpInboundCodeword_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 20 | `PP.IC.RESERVED.1` | `PpInboundCodeword_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 21 | `PP.IC.LOCAL.REF` | `PpInboundCodeword_LocalRef` |  |  |  |
| 22 | `PP.IC.LinkID` | `PpInboundCodeword_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. For EX: OTHRINSBNK103SWIFT-20160406 |
| 23 | `PP.IC.OVERRIDE` | `PpInboundCodeword_Override` |  |  |  |
| 24 | `PP.IC.RECORD.STATUS` | `PpInboundCodeword_RecordStatus` | String |  |  |
| 25 | `PP.IC.CURR.NO` | `PpInboundCodeword_CurrNo` | String |  |  |
| 26 | `PP.IC.INPUTTER` | `PpInboundCodeword_Inputter` |  |  |  |
| 27 | `PP.IC.DATE.TIME` | `PpInboundCodeword_DateTime` |  |  |  |
| 28 | `PP.IC.AUTHORISER` | `PpInboundCodeword_Authoriser` | String |  |  |
| 29 | `PP.IC.CO.CODE` | `PpInboundCodeword_CoCode` | String |  |  |
| 30 | `PP.IC.DEPT.CODE` | `PpInboundCodeword_DeptCode` | String |  |  |
| 31 | `PP.IC.AUDITOR.CODE` | `PpInboundCodeword_AuditorCode` | String |  |  |
| 32 | `PP.IC.AUDIT.DATE.TIME` | `PpInboundCodeword_AuditDateTime` | String |  |  |
