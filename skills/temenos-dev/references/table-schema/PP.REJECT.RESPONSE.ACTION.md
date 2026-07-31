# PP.REJECT.RESPONSE.ACTION — Table Schema

> Source: `INSERTS/I_F.PP.REJECT.RESPONSE.ACTION` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RRA.CompanyID` | `PpRejectResponseAction_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.RRA.Ranking` | `PpRejectResponseAction_Ranking` | TField | Yes | Specifies the order (sequence) of the record in the application. Based on the value, a record is prioritised in such a way that, it is given higher preference for selection under peeling logic applied in the payments hub. Validation Rules: Mandatory field. 8 numeric characters. |
| 3 | `PP.RRA.BusinessLine` | `PpRejectResponseAction_Businessline` | TField |  | Differentiates between a Retail and Corporate payment. It is derived from the accounts data retrieved from the DDA. If it is set to *, then the Business Line is not used in the match criteria. |
| 4 | `PP.RRA.OriginatingWorkflow` | `PpRejectResponseAction_Originatingworkflow` | TField |  | Indicates the flow from which the payment has originated. Possible values: STP - Straight Through Processing OE - Order Entry RPR - Repair CD - Cheque Deposit DD - Demand Deposit WFM - Workflow Manager * - Others Validation Rules: 3 alphanumeric characters. |
| 5 | `PP.RRA.OriginatingSource` | `PpRejectResponseAction_Originatingsource` | TField |  | Specifies the source through which the payment hub receives a message. Validation Rules: 10 alphabetic characters. The value links to the field 'OriginatingSource' in PP.SOURCE. |
| 6 | `PP.RRA.MessagePriority` | `PpRejectResponseAction_Messagepriority` | TField | Yes | Indicates the priority of the message. Possible values: Values ranging from 1 to 9. * is allowed too. Validation Rules: Mandatory fields. 2 alphanumeric characters. |
| 7 | `PP.RRA.BankingPriority` | `PpRejectResponseAction_Bankingpriority` | TField | Yes | Indicates the priority of the message. This information is retrieved from the header ((field 113) from "User Header Block� (Block 3))of the swift message. The value in the message is validated against the value of this field. If it is set to * then the Banking Priority is not used in the match criteria. Validation Rules: Mandatory field. 3 alphanumeric characters. |
| 8 | `PP.RRA.TransactionAmountUpperLimit` | `PpRejectResponseAction_Transactionamountupperlimit` | TField | Yes | Indicates the upper limit(maximum) of the amount for a payment. Validation Rules: Mandatory fields. 17 alphanumeric characters. |
| 9 | `PP.RRA.IncomingMessageType` | `PpRejectResponseAction_Incomingmessagetype` | TField | Yes | Specifies the type of the incoming message from a channel. Example: For channel, SWIFT MT101 MT103 For channel, PMTROUTER ATABE ATADE Example : BNK,GB1 Validation Rules: Mandatory field. 10 alphanumeric characters. |
| 10 | `PP.RRA.ClearingNatureCode` | `PpRejectResponseAction_Clearingnaturecode` | TField | Yes | Differentiates between the different types of local clearing payments with a unique code. Validation Rules: Mandatory field. 20 alphanumeric characters. Value links to field, 'ClearingNatureCode' in PP.CLEARING.NATURE.CODE. If it is set to * then the clearing nature code is not used in the match criteria. |
| 11 | `PP.RRA.ManualRejectResponseAction` | `PpRejectResponseAction_Manualrejectresponseaction` | TField |  | Specifies the reject response action to be taken by the payments hub for a payment of the specified characteristics. Possible values: R � Reject the payment C � Cancel the payment Applicable Only for PH module.If PH is not installed, values will be made blank/ default functionality will be applicable during payment processing |
| 12 | `PP.RRA.RESERVED.5` | `PpRejectResponseAction_Reserved5` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 13 | `PP.RRA.RESERVED.4` | `PpRejectResponseAction_Reserved4` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 14 | `PP.RRA.RESERVED.3` | `PpRejectResponseAction_Reserved3` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 15 | `PP.RRA.RESERVED.2` | `PpRejectResponseAction_Reserved2` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 16 | `PP.RRA.RESERVED.1` | `PpRejectResponseAction_Reserved1` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 17 | `PP.RRA.LOCAL.REF` | `PpRejectResponseAction_LocalRef` |  |  |  |
| 18 | `PP.RRA.OVERRIDE` | `PpRejectResponseAction_Override` |  |  |  |
| 19 | `PP.RRA.RECORD.STATUS` | `PpRejectResponseAction_RecordStatus` | String |  |  |
| 20 | `PP.RRA.CURR.NO` | `PpRejectResponseAction_CurrNo` | String |  |  |
| 21 | `PP.RRA.INPUTTER` | `PpRejectResponseAction_Inputter` |  |  |  |
| 22 | `PP.RRA.DATE.TIME` | `PpRejectResponseAction_DateTime` |  |  |  |
| 23 | `PP.RRA.AUTHORISER` | `PpRejectResponseAction_Authoriser` | String |  |  |
| 24 | `PP.RRA.CO.CODE` | `PpRejectResponseAction_CoCode` | String |  |  |
| 25 | `PP.RRA.DEPT.CODE` | `PpRejectResponseAction_DeptCode` | String |  |  |
| 26 | `PP.RRA.AUDITOR.CODE` | `PpRejectResponseAction_AuditorCode` | String |  |  |
| 27 | `PP.RRA.AUDIT.DATE.TIME` | `PpRejectResponseAction_AuditDateTime` | String |  |  |
