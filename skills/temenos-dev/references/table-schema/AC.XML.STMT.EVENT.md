# AC.XML.STMT.EVENT — Table Schema

> Source: `INSERTS/I_F.AC.XML.STMT.EVENT` in `AC_IFConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.XML.MESSAGE.ID` | `AcXmlStmtEvent_MessageId` | TField |  | Indicates the Message identification of the CAMT statement. This field corresponds to the Message Identification part of the Header tag in CAMT statement. |
| 2 | `AC.XML.MESSAGE.KEY` | `AcXmlStmtEvent_MessageKey` | TField | No | Unique identification for a CAMT statement per page Format: AccountId:StatementFrequencyNo:StatementDate:StatementTime:CAMTMessageType:PageNumber (eg. 101036:1:20200417:235959:CAMT053:1) Page Number is optional. If there is no Pagination, then it can be blank. |
| 3 | `AC.XML.MASTER.XML.MSG.ID` | `AcXmlStmtEvent_MasterXmlMsgId` | TField |  | Unique Id of a CAMT Statement when a statement have multiple pages, then this value will be common for all the pages of the statement. Format: AccountId:RecipientId:StatementCycleNo:StatementDate:StatementTime:CAMTMessageType:CompanyCode (eg. 101036:100100:1:20200417:235959:CAMT053:GB0010001) |
| 4 | `AC.XML.MESSAGE.TYPE` | `AcXmlStmtEvent_MessageType` | TField |  | Defines the message type of CAMT statement. |
| 5 | `AC.XML.CUSTOMER` | `AcXmlStmtEvent_Customer` | TField |  | Defines the owner of the Account for which CAMT statement is generated. |
| 6 | `AC.XML.ACCOUNT.ID` | `AcXmlStmtEvent_AccountId` | TField |  | Defines the account for which CAMT statement is generated. |
| 7 | `AC.XML.ACCOUNT.CCY` | `AcXmlStmtEvent_AccountCcy` | TField |  | Indicates the currency of the Account for which CAMT Statement is generated. |
| 8 | `AC.XML.DE.STMT.REQ.ID` | `AcXmlStmtEvent_DeStmtReqId` | TField |  | ID of the DE.STATEMENT.REQUEST record where the CAMT Statement request is defined. |
| 9 | `AC.XML.CARRIER` | `AcXmlStmtEvent_Carrier` | TField |  | Channel Type of Account owner, identifies the Delivery carrier. A valid record in DE.CARRIER |
| 10 | `AC.XML.DELIVERY.ADDRESS` | `AcXmlStmtEvent_DeliveryAddress` | TField |  | Specifies the Delivery Address of the Account owner. |
| 11 | `AC.XML.COMPANY.CODE` | `AcXmlStmtEvent_CompanyCode` | TField |  | Specifies the lead company where the Account is held. |
| 12 | `AC.XML.VARIANT` | `AcXmlStmtEvent_Variant` | TField |  | Defines the variant in which Payload has been generated for the Account owner. |
| 13 | `AC.XML.TRANSFORMATION.RULE` | `AcXmlStmtEvent_TransformationRule` | TField |  | Transformation Rule to be applied to convert the CAMT statement to the required variant configured for the Account owner. |
| 14 | `AC.XML.RECIPIENT.ID` | `AcXmlStmtEvent_RecipientId` | TField |  | Indicates the Recipient customer ID. |
| 15 | `AC.XML.RECIPIENT.NAME` | `AcXmlStmtEvent_RecipientName` | TField |  | Indicates the Name of the Recipient. This field corresponds to the Message Recipient Name part of the Header tag in CAMT statement. |
| 16 | `AC.XML.RECIPIENT.BIC` | `AcXmlStmtEvent_RecipientBic` | TField |  | Specifies the delivery Address of the recipient. |
| 17 | `AC.XML.RECIPIENT.CHANNEL` | `AcXmlStmtEvent_RecipientChannel` | TField |  | Indicates the channel type for the recipient. |
| 18 | `AC.XML.RECIPIENT.VARIANT` | `AcXmlStmtEvent_RecipientVariant` | TField |  | Defines the variant in which Payload has been generated for the Recipient. |
| 19 | `AC.XML.RECIPIENT.TRANS.RULE` | `AcXmlStmtEvent_RecipientTransRule` | TField |  | Transformation Rule to be applied to convert the CAMT statement to the required variant configured for the recipient. |
| 20 | `AC.XML.IN.XML.STMT` | `AcXmlStmtEvent_InXmlStmt` | TField |  | Stores the CAMT Statement received from Microservice in the encoded format. |
| 21 | `AC.XML.DCD.XML.STMT` | `AcXmlStmtEvent_DcdXmlStmt` | TField |  | Stores the decoded XML Statement. Currently it is not used since it may increase the file size. Validation Rule: 1. No input field. |
| 22 | `AC.XML.XML.FILE.NAME` | `AcXmlStmtEvent_XmlFileName` | TField |  | Indicates the File Name of the CAMT statement in case if CAMT statement generated is of size more than 1MB. Either IN.XML.STMT or XML.FILE.NAME could be available, both the field values are mutually exclusive and both should not be updated. |
| 23 | `AC.XML.DE.O.HEADER.ID` | `AcXmlStmtEvent_DeOHeaderId` | TField |  | Stores the DE.O.HEADER ID created for the CAMT statement event during the authorisation of the record. Validation Rule: 1. No input field. |
| 24 | `AC.XML.HANDOFF.DELIVERY` | `AcXmlStmtEvent_HandoffDelivery` | TField |  | Indicates wheather the CAMT statement is sent to delivery CAMEL queue or not. Validation Rule: Following are the valid options: YES/NULL - Send CAMT statement to CAMEL queue . NO - Unsend CAMT statement to CAMEL queue. |
| 25 | `AC.XML.COPY.DUPL.INDICATOR` | `AcXmlStmtEvent_CopyDuplIndicator` | TField |  | Specifies the indicator which provides ability to identify the additional CAMT message from the original sent to the Account owner and the authorised third party. Possible values for the BLANK,COPY,DUPL,CODU BLANK - For the original statement sent to the Account owner COPY - When a copy of the statement is sent to an Authorized Third Party, such as a company head office, parent entity, or an institution providing additional service. DUPL - When a duplicate of the statement is sent to the Account Owner through an alternate channel such as internet banking or customer service request. CODU - When a duplicate of a statement copy is sent to an Authorized Third Party, through an alternate channel such as internet banking or customer service request. |
| 26 | `AC.XML.ACCT.OWN.MSG.DATE.TIME` | `AcXmlStmtEvent_AcctOwnMsgDateTime` |  |  |  |
| 27 | `AC.XML.MSG.DATE.TIME` | `AcXmlStmtEvent_MsgDateTime` |  |  |  |
| 28 | `AC.XML.GENERATED.BY` | `AcXmlStmtEvent_GeneratedBy` | TField |  | To indicate how the statement has been generated (i.e.) the statement is generated either through Events and Microservice or through Services Valid options are: i) Statement through Services - To indicate that the CAMT statement is generated through IX module using XML.TRANSFORMATION service. ii) Statement through Events and Microservice � To indicate that the CAMT statement is generated through IZ module using streaming of data to the DATA.EVENTS table from where CAMT Microservice will consume the data and produce CAMT statement. |
| 29 | `AC.XML.RESERVED.10` | `AcXmlStmtEvent_Reserved10` | TField |  |  |
| 30 | `AC.XML.RESERVED.9` | `AcXmlStmtEvent_Reserved9` | TField |  |  |
| 31 | `AC.XML.RESERVED.8` | `AcXmlStmtEvent_Reserved8` | TField |  |  |
| 32 | `AC.XML.RESERVED.7` | `AcXmlStmtEvent_Reserved7` | TField |  |  |
| 33 | `AC.XML.RESERVED.6` | `AcXmlStmtEvent_Reserved6` | TField |  |  |
| 34 | `AC.XML.RESERVED.5` | `AcXmlStmtEvent_Reserved5` | TField |  |  |
| 35 | `AC.XML.RESERVED.4` | `AcXmlStmtEvent_Reserved4` | TField |  |  |
| 36 | `AC.XML.RESERVED.3` | `AcXmlStmtEvent_Reserved3` | TField |  |  |
| 37 | `AC.XML.RESERVED.2` | `AcXmlStmtEvent_Reserved2` | TField |  |  |
| 38 | `AC.XML.RESERVED.1` | `AcXmlStmtEvent_Reserved1` | TField |  |  |
| 39 | `AC.XML.OVERRIDE` | `AcXmlStmtEvent_Override` |  |  |  |
| 40 | `AC.XML.RECORD.STATUS` | `AcXmlStmtEvent_RecordStatus` | String |  |  |
| 41 | `AC.XML.CURR.NO` | `AcXmlStmtEvent_CurrNo` | String |  |  |
| 42 | `AC.XML.INPUTTER` | `AcXmlStmtEvent_Inputter` |  |  |  |
| 43 | `AC.XML.DATE.TIME` | `AcXmlStmtEvent_DateTime` |  |  |  |
| 44 | `AC.XML.AUTHORISER` | `AcXmlStmtEvent_Authoriser` | String |  |  |
| 45 | `AC.XML.CO.CODE` | `AcXmlStmtEvent_CoCode` | String |  |  |
| 46 | `AC.XML.DEPT.CODE` | `AcXmlStmtEvent_DeptCode` | String |  |  |
| 47 | `AC.XML.AUDITOR.CODE` | `AcXmlStmtEvent_AuditorCode` | String |  |  |
| 48 | `AC.XML.AUDIT.DATE.TIME` | `AcXmlStmtEvent_AuditDateTime` | String |  |  |
