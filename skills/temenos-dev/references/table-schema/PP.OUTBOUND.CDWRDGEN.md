# PP.OUTBOUND.CDWRDGEN — Table Schema

> Source: `INSERTS/I_F.PP.OUTBOUND.CDWRDGEN` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.OCG.CompanyID` | `PpOutboundCdwrdgen_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.OCG.ReceiverBankBIC` | `PpOutboundCdwrdgen_Receiverbankbic` | TField |  | This field represents the BIC of the Receiver Bank |
| 3 | `PP.OCG.OutboundMessagePaymentType` | `PpOutboundCdwrdgen_Outboundmessagepaymenttype` |  |  |  |
| 4 | `PP.OCG.TransactionCurrency` | `PpOutboundCdwrdgen_Transactioncurrency` |  |  |  |
| 5 | `PP.OCG.MessagePriority` | `PpOutboundCdwrdgen_Messagepriority` |  |  |  |
| 6 | `PP.OCG.OutboundInformationCode` | `PpOutboundCdwrdgen_Outboundinformationcode` |  |  |  |
| 7 | `PP.OCG.OutboundCodeword` | `PpOutboundCdwrdgen_Outboundcodeword` |  |  |  |
| 8 | `PP.OCG.OutboundCodewordText` | `PpOutboundCdwrdgen_Outboundcodewordtext` |  |  |  |
| 9 | `PP.OCG.ProcessingSequenceNumber` | `PpOutboundCdwrdgen_Processingsequencenumber` |  |  |  |
| 10 | `PP.OCG.OutboundCodewordPriority` | `PpOutboundCdwrdgen_Outboundcodewordpriority` |  |  |  |
| 11 | `PP.OCG.StartDate` | `PpOutboundCdwrdgen_Startdate` | TField |  | Specifies the date from which the record is considered active for payments processing. This is made NOINPUT field. On click of validate button, StartDate gets autopopulated from ID field. This date can be CurrentBusinessDate or Future Dated. |
| 12 | `PP.OCG.EndDate` | `PpOutboundCdwrdgen_Enddate` | TField | Yes | Specifies the date until which the record is considered active for payments processing.Post this date, the record will be set as Inactive by the payments hub. This field is made non mandatory. It can be left blank and can be assumed that record will not expire. |
| 13 | `PP.OCG.RESERVED.5` | `PpOutboundCdwrdgen_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 14 | `PP.OCG.RESERVED.4` | `PpOutboundCdwrdgen_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 15 | `PP.OCG.RESERVED.3` | `PpOutboundCdwrdgen_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 16 | `PP.OCG.RESERVED.2` | `PpOutboundCdwrdgen_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 17 | `PP.OCG.RESERVED.1` | `PpOutboundCdwrdgen_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 18 | `PP.OCG.LOCAL.REF` | `PpOutboundCdwrdgen_LocalRef` |  |  |  |
| 19 | `PP.OCG.LinkID` | `PpOutboundCdwrdgen_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. For EX: OTHRINSBNK103SWIFT-20160406 |
| 20 | `PP.OCG.OVERRIDE` | `PpOutboundCdwrdgen_Override` |  |  |  |
| 21 | `PP.OCG.RECORD.STATUS` | `PpOutboundCdwrdgen_RecordStatus` | String |  |  |
| 22 | `PP.OCG.CURR.NO` | `PpOutboundCdwrdgen_CurrNo` | String |  |  |
| 23 | `PP.OCG.INPUTTER` | `PpOutboundCdwrdgen_Inputter` |  |  |  |
| 24 | `PP.OCG.DATE.TIME` | `PpOutboundCdwrdgen_DateTime` |  |  |  |
| 25 | `PP.OCG.AUTHORISER` | `PpOutboundCdwrdgen_Authoriser` | String |  |  |
| 26 | `PP.OCG.CO.CODE` | `PpOutboundCdwrdgen_CoCode` | String |  |  |
| 27 | `PP.OCG.DEPT.CODE` | `PpOutboundCdwrdgen_DeptCode` | String |  |  |
| 28 | `PP.OCG.AUDITOR.CODE` | `PpOutboundCdwrdgen_AuditorCode` | String |  |  |
| 29 | `PP.OCG.AUDIT.DATE.TIME` | `PpOutboundCdwrdgen_AuditDateTime` | String |  |  |
