# PP.MANUAL.AUTH.REQUIRED — Table Schema

> Source: `INSERTS/I_F.PP.MANUAL.AUTH.REQUIRED` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MAR.CompanyID` | `PpManualAuthRequired_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.MAR.Ranking` | `PpManualAuthRequired_Ranking` | TField | Yes | Specifies the order (sequence) of the record in the application. Based on the value, a record is prioritised in such a way that, it is given higher preference for selection under peeling logic applied in the payments hub. Validation Rules: Mandatory field. 9 numeric characters. |
| 3 | `PP.MAR.BusinessLine` | `PpManualAuthRequired_Businessline` | TField | Yes | Indicates the business line. Validation Rules: Mandatory input. 1-3 Alphanumeric character Equivalent to Target of the Customer. Default value can be defined as * |
| 4 | `PP.MAR.OriginatingWorkflow` | `PpManualAuthRequired_Originatingworkflow` | TField | Yes | Mandatory Field. 1-3 Alphanumeric character. Represents the Workflow Origin of the payment Possible values 1) STP - Straight Through Processing 2) OE - Order Entry 3) RPR - Repair 4) CD - Cheque Deposit 5) DD - Demand Draft Default value can be *" |
| 5 | `PP.MAR.OriginatingSource` | `PpManualAuthRequired_Originatingsource` | TField | Yes | Indicate the origin of the payment order. Validation Rules: Mandatory input. Value links to field 'Source' in PPT.SOURCE. |
| 6 | `PP.MAR.MessagePriority` | `PpManualAuthRequired_Messagepriority` | TField | Yes | Indicates the priority of the payment. Validation Rules: Mandatory input.1-2 Numeric Character.Possible values are 1-9. Default Value can be *" |
| 7 | `PP.MAR.BankingPriority` | `PpManualAuthRequired_Bankingpriority` | TField | Yes | Specifies the banking priority. Validation Rules: Mandatory input. 1-4 Alphanumeric character. Default value can be defined as *. |
| 8 | `PP.MAR.TransactionAmountUpperLimit` | `PpManualAuthRequired_Transactionamountupperlimit` | TField | Yes | Indicates the limit of the transaction amount upto which the setup can be considered for selection under the peeling logic. The Transaction Amount of the payment order should be Lower than or equal to the amount mentioned here. Amount is maintained in the home currency of the company. Validation Rules: Mandatory Input. 1-20 Alphanumeric character. Default Value is * |
| 9 | `PP.MAR.IncomingMessageType` | `PpManualAuthRequired_Incomingmessagetype` | TField | Yes | Specifies the Incoming Message Type of the Payment. Mandatory input. Value links to field 'MessagePaymentType' in PP.MSGPAYMENTTYPE Default Value can be * |
| 10 | `PP.MAR.ClearingNatureCode` | `PpManualAuthRequired_Clearingnaturecode` | TField | Yes | Indicates a unique nature code for the clearing. Validation Rules: Mandatory Input. Value links to field 'ClearingNatureCode' in PP.CLEARING.NATURE.CODE |
| 11 | `PP.MAR.ManualAuthRequiredFlag` | `PpManualAuthRequired_Manualauthrequiredflag` | TField | Yes | Specifies if manual authorization is required for the payment based on the defined characteristics in this table if PH is installed. Value is always set to 'N' and the field is non-inputtable if PH is not installed. Possible values: "Y" - Yes. Implies that the Manual Authorization can be requested for the payment order if required. "N" - No. Implies that the Manual Authorization cannot be requested for the payment order. Validation Rules: Mandatory Input. 1 alphanumeric character. |
| 12 | `PP.MAR.TxnStopAuthRequired` | `PpManualAuthRequired_Txnstopauthrequired` | TField | No | Optional field to indicate if the TPH has to send the payment to AFCA queue for manual authorisation or Repair Queue when the Transaction Stop response is Return Allowed Values : Y_N When not defined, it will be considered as N When set as Y, the Payment will be sent to ACFA Queue, when the Transaction Stop Response is Return When set as N, the Payment will be sent to Repair Queue, when the Transaction Stop Response is Return |
| 13 | `PP.MAR.RESERVED.4` | `PpManualAuthRequired_Reserved4` |  |  |  |
| 14 | `PP.MAR.RESERVED.3` | `PpManualAuthRequired_Reserved3` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 15 | `PP.MAR.RESERVED.2` | `PpManualAuthRequired_Reserved2` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 16 | `PP.MAR.RESERVED.1` | `PpManualAuthRequired_Reserved1` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 17 | `PP.MAR.LOCAL.REF` | `PpManualAuthRequired_LocalRef` |  |  |  |
| 18 | `PP.MAR.OVERRIDE` | `PpManualAuthRequired_Override` |  |  |  |
| 19 | `PP.MAR.RECORD.STATUS` | `PpManualAuthRequired_RecordStatus` | String |  |  |
| 20 | `PP.MAR.CURR.NO` | `PpManualAuthRequired_CurrNo` | String |  |  |
| 21 | `PP.MAR.INPUTTER` | `PpManualAuthRequired_Inputter` |  |  |  |
| 22 | `PP.MAR.DATE.TIME` | `PpManualAuthRequired_DateTime` |  |  |  |
| 23 | `PP.MAR.AUTHORISER` | `PpManualAuthRequired_Authoriser` | String |  |  |
| 24 | `PP.MAR.CO.CODE` | `PpManualAuthRequired_CoCode` | String |  |  |
| 25 | `PP.MAR.DEPT.CODE` | `PpManualAuthRequired_DeptCode` | String |  |  |
| 26 | `PP.MAR.AUDITOR.CODE` | `PpManualAuthRequired_AuditorCode` | String |  |  |
| 27 | `PP.MAR.AUDIT.DATE.TIME` | `PpManualAuthRequired_AuditDateTime` | String |  |  |
