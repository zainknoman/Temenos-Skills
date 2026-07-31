# PP.SO.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.PP.SO.TRANSACTION` in `PP_SwiftOutService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSOT.CompanyID` | `PpSoTransaction_Companyid` | TField |  | It will be defaulted with the value of CompanyID from POR.TRANSACTION. |
| 2 | `PPSOT.FTNumber` | `PpSoTransaction_Ftnumber` | TField |  | It holds the value of FTNumber from POR.TRANSACTION. |
| 3 | `PPSOT.TransactionAmount` | `PpSoTransaction_Transactionamount` | TField |  | It will be defaulted with the value of TransactionAmount from POR.TRANSACTION. |
| 4 | `PPSOT.CurrencyCode` | `PpSoTransaction_Currencycode` | TField |  | It will be defaulted with the value of TransactionCurrencyCode from POR.TRANSACTION. |
| 5 | `PPSOT.SendDate` | `PpSoTransaction_Senddate` | TField |  | It holds the value of PaymentSendDate from POR.TRANSACTION. |
| 6 | `PPSOT.ErrorCode` | `PpSoTransaction_Errorcode` | TField |  | It will be defaulted with the value of ErrorCode from POR.HISTORYLOG for the corresponding FT Number. |
| 7 | `PPSOT.ErrorDescription` | `PpSoTransaction_Errordescription` | TField |  | It will be defaulted with the value of AdditionalInformation from POR.HISTORYLOG for the corresponding FT Number. |
| 8 | `PPSOT.StatusCode` | `PpSoTransaction_Statuscode` | TField |  | It will be defaulted with the value 999 or 997. Possible values: Status Code: 999 indicates that the Payment is Complete. Status Code: 997 indicates that the Payment is cancelled. |
| 9 | `PPSOT.OutputChannel` | `PpSoTransaction_Outputchannel` | TField |  | It will be defaulted with the value of OuputChannel from POR.TRANSACTION. |
| 10 | `PPSOT.PaymentStatus` | `PpSoTransaction_Paymentstatus` | TField |  | It holds the status of the Payment. Possible values: Cancel: Payment will be reversed and moved to status 993. Complete: Payment will be moved to status 999. ProcessAsACKReceived: System will assume ACK has been received and payment will be moved to status 689 and 678 for the message types MT103 and MT202COV. ProcessAsDLNReceived:This action will move the payment to the next status assuming we have received positive DLN and continue processing. In case of serial, mark it to complete and generate confirmations. In case of cover, if it is underlying payment, generate cover and if it is cover, wait for DLN if DLN is required for underlying payment and when it is not received yet. Mark to complete if DLN is not required/already positive DLN received for underlying payment or if underlying payment is sent as MT103. |
| 11 | `PPSOT.MessageType` | `PpSoTransaction_Messagetype` | TField |  | It will be defaulted with the value of MessageType from POR.TRANSACTION. |
| 12 | `PPSOT.StatusDescription` | `PpSoTransaction_Statusdescription` | TField |  | Holds the description of a specific status code. |
| 13 | `PPSOT.ReasonForManualAction` | `PpSoTransaction_Reasonformanualaction` | TField |  | Specifies the reason to process a payment as ACK Received. |
| 14 | `PPSOT.RESERVED02` | `PpSoTransaction_Reserved02` |  |  |  |
| 15 | `PPSOT.RESERVED01` | `PpSoTransaction_Reserved01` |  |  |  |
| 16 | `PPSOT.OVERRIDE` | `PpSoTransaction_Override` |  |  |  |
| 17 | `PPSOT.RECORD.STATUS` | `PpSoTransaction_RecordStatus` | String |  |  |
| 18 | `PPSOT.CURR.NO` | `PpSoTransaction_CurrNo` | String |  |  |
| 19 | `PPSOT.INPUTTER` | `PpSoTransaction_Inputter` |  |  |  |
| 20 | `PPSOT.DATE.TIME` | `PpSoTransaction_DateTime` |  |  |  |
| 21 | `PPSOT.AUTHORISER` | `PpSoTransaction_Authoriser` | String |  |  |
| 22 | `PPSOT.CO.CODE` | `PpSoTransaction_CoCode` | String |  |  |
| 23 | `PPSOT.DEPT.CODE` | `PpSoTransaction_DeptCode` | String |  |  |
| 24 | `PPSOT.AUDITOR.CODE` | `PpSoTransaction_AuditorCode` | String |  |  |
| 25 | `PPSOT.AUDIT.DATE.TIME` | `PpSoTransaction_AuditDateTime` | String |  |  |
