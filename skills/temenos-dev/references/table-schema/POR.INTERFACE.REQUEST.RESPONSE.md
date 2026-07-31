# POR.INTERFACE.REQUEST.RESPONSE — Table Schema

> Source: `INSERTS/I_F.POR.INTERFACE.REQUEST.RESPONSE` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORIR.RESERVATION.KEY` | `PorInterfaceRequestResponse_ReservationKey` |  |  |  |
| 2 | `PORIR.RETURN.CODE` | `PorInterfaceRequestResponse_ReturnCode` |  |  |  |
| 3 | `PORIR.RETURN.REASON.DESC` | `PorInterfaceRequestResponse_ReturnReasonDesc` |  |  |  |
| 4 | `PORIR.ERROR.CODE` | `PorInterfaceRequestResponse_ErrorCode` |  |  |  |
| 5 | `PORIR.ERROR.DETAILS` | `PorInterfaceRequestResponse_ErrorDetails` |  |  |  |
| 6 | `PORIR.INDICATOR` | `PorInterfaceRequestResponse_Indicator` |  |  |  |
| 7 | `PORIR.ACCOUNT.NUMBER` | `PorInterfaceRequestResponse_AccountNumber` |  |  |  |
| 8 | `PORIR.RESERVED.1` | `PorInterfaceRequestResponse_Reserved1` |  |  |  |
| 9 | `PORIR.RESERVED.2` | `PorInterfaceRequestResponse_Reserved2` |  |  |  |
| 10 | `PORIR.RESERVED.3` | `PorInterfaceRequestResponse_Reserved3` |  |  |  |
| 11 | `PORIR.RESERVED.4` | `PorInterfaceRequestResponse_Reserved4` |  |  |  |
| 12 | `PORIR.RESERVED.5` | `PorInterfaceRequestResponse_Reserved5` |  |  |  |
| 13 | `PORIR.PROCESSING.DATE` | `PorInterfaceRequestResponse_ProcessingDate` | TField |  | Indicates the date on which the payment is processed |
| 14 | `PORIR.STATUS` | `PorInterfaceRequestResponse_Status` | TField |  | Indicates the status of the requested payment Possible Values are: S - Indicates the request has been sent R - Indicates the response for the request has been received |
| 15 | `PORIR.STATUS.DATE.TIME` | `PorInterfaceRequestResponse_StatusDateTime` |  |  |  |
| 16 | `PORIR.DEBIT.CREDIT.INDICATOR` | `PorInterfaceRequestResponse_DebitCreditIndicator` | TField |  | Indicator to denote whether the request is on debit or credit side Possible Values are: D - Indicate the request is on debit side C - Indicate the request is on credit side |
| 17 | `PORIR.LIM.ORDER.REFERENCE` | `PorInterfaceRequestResponse_LimOrderReference` | TField |  | Holds the reference id of FX.LIM.ORDER record. |
| 18 | `PORIR.RESERVED.6` | `PorInterfaceRequestResponse_Reserved6` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 19 | `PORIR.RESERVED.7` | `PorInterfaceRequestResponse_Reserved7` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 20 | `PORIR.RESERVED.8` | `PorInterfaceRequestResponse_Reserved8` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 21 | `PORIR.RESERVED.9` | `PorInterfaceRequestResponse_Reserved9` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 22 | `PORIR.RESERVED.10` | `PorInterfaceRequestResponse_Reserved10` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 23 | `PORIR.PAYMENT.STATUS` | `PorInterfaceRequestResponse_PaymentStatus` | TField | Yes | Indicates the status of a payment that was sent to screening interface. The only valid value that user can choose for this field is APPROVED. Validation Rules: Mandatory field. 10 alphanumeric characters. When the payment status is set to APPROVED then the field UserAcceptanceReason must also be filled. Possible values: 1) NEW - The payment was sent to the screening interface; 2) POSSIBLE - The payment is a possible hit, TPS needs to wait for a second reply of the screening interface; 3) APPROVED - The payment is a accepted, no hit was found; 4) REJECTED - The payment is a true hit. |
| 24 | `PORIR.SEND.DATE` | `PorInterfaceRequestResponse_SendDate` | TField |  | Indicates the business date when the payment was send to Screening interface. Validation Rules: 11 characters Date format should be filled in. |
| 25 | `PORIR.SEND.TIMESTAMP` | `PorInterfaceRequestResponse_SendTimestamp` | TField |  | Indicates the system date and time when the payment was sent to Screening interface. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 |
| 26 | `PORIR.POSS.STAT.RECEIVED.TIME` | `PorInterfaceRequestResponse_PossStatReceivedTime` | TField |  | Indicates the system date and time when the Screening interface replied that a possible hit was found. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 |
| 27 | `PORIR.RESPONSE.RECEIVED.TIME` | `PorInterfaceRequestResponse_ResponseReceivedTime` | TField |  | Indicates the system date and time when the Screening interface replied with a final answer. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 |
| 28 | `PORIR.USER.ACCEPTANCE.FLAG` | `PorInterfaceRequestResponse_UserAcceptanceFlag` | TField |  | Specifies if the payment was approved or not by a user without waiting the screening interface response. Validation Rules: 1 alphanumeric character. It needs to be set on Y (Yes) when the payment status is set as approved. Possible values: Y(Yes) or N(No) |
| 29 | `PORIR.USER.ACCEPTANCE.DATE` | `PorInterfaceRequestResponse_UserAcceptanceDate` | TField |  | Specifies the business date when the user accepted a payment. Validation Rules: 11 characters Date format should be filled in. Default value defined as Current Business Date. |
| 30 | `PORIR.USER.ACCEPTANCE.REASON` | `PorInterfaceRequestResponse_UserAcceptanceReason` | TField |  | Specifies the reasons why the user has accepted a payment. Validation Rules: 1-256 alphanumeric characters. This field must be set when the payment status was set to APPROVED. |
| 31 | `PORIR.USER.REJECTION.FLAG` | `PorInterfaceRequestResponse_UserRejectionFlag` | TField |  | Specifies if the payment was rejected or not (meaning that was send to repair) by a user without waiting the screening interface response. Validation Rules: 1 alphanumeric character. It needs to be set on Y (Yes) when the payment status is set as rejected. Possible values: Y(Yes) or N(No) |
| 32 | `PORIR.USER.REJECTION.DATE` | `PorInterfaceRequestResponse_UserRejectionDate` | TField |  | Specifies the business date when the user rejected (sent to repair) a payment. Validation Rules: 11 characters Date format should be filled in. Default value defined as Current Business Date. |
| 33 | `PORIR.SCREENED.DATE` | `PorInterfaceRequestResponse_ScreenedDate` | TField |  | Specifies the business date when the payment was processed in TPS based on the answer received from Screening. Validation Rules: 11 characters Date format should be filled in. The value is not editable by the user. |
| 34 | `PORIR.LATE.RESPONSE.FLAG` | `PorInterfaceRequestResponse_LateResponseFlag` | TField |  | Specifies if the answer from Screening interface came after a manually intervention on the payment. It will allow the SOD process to delete this record. Validation Rules: 1 alphanumeric character. The value is not editable by the user. EOD will set it on Y (Yes) when the LateResponse field is filled. Possible values: Y(Yes) or N(No) |
| 35 | `PORIR.ENTRY.USER.ID` | `PorInterfaceRequestResponse_EntryUserId` | TField |  | Indicates the user that initiated the acceptance of the payment. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 36 | `PORIR.ENTRY.DATE.TIME` | `PorInterfaceRequestResponse_EntryDateTime` |  |  |  |
| 37 | `PORIR.APPROVER.USER.ID` | `PorInterfaceRequestResponse_ApproverUserId` |  |  |  |
| 38 | `PORIR.APPROVED.DATE.TIME` | `PorInterfaceRequestResponse_ApprovedDateTime` |  |  |  |
| 39 | `PORIR.RESERVED.11` | `PorInterfaceRequestResponse_Reserved11` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 40 | `PORIR.RESERVED.12` | `PorInterfaceRequestResponse_Reserved12` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 41 | `PORIR.RESERVED.13` | `PorInterfaceRequestResponse_Reserved13` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 42 | `PORIR.RESERVED.14` | `PorInterfaceRequestResponse_Reserved14` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 43 | `PORIR.RESERVED.15` | `PorInterfaceRequestResponse_Reserved15` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
