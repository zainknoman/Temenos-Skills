# CAPL.UB.RECURR.PAYMENT — Table Schema

> Source: `INSERTS/I_F.CAPL.UB.RECURR.PAYMENT` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UBR.PMT.PAYER` | `CaplUbRecurrPayment_Payer` | TField | Yes | The Customer ID to which the Ebill recurring payment needs to be attached.Mandatory field.Validation - record from CUSTOMER table.Allowed upto 10 char |
| 2 | `UBR.PMT.PAYER.NAME` | `CaplUbRecurrPayment_PayerName` | TField |  | Field is used to store the name of the Customer id(Payer) defined in the field PAYER.Max 60 char allowed |
| 3 | `UBR.PMT.PAYER.FROM.AC` | `CaplUbRecurrPayment_PayerFromAc` | TField | Yes | Field to store the Account of the Customer from which the payments need to be made. Ideally PAYER account.Validation - record from ACCOUNT application.Mandatory field. |
| 4 | `UBR.PMT.PAYEE.ID` | `CaplUbRecurrPayment_PayeeId` | TField | Yes | Field is used to store the Vendor ID will be selected from the drop down.Ideally payee id in Bill payment.Vendor who is a Payee id called as Utility id.Validation - record from UB.PAYEE.ACCTMandatory field. |
| 5 | `UBR.PMT.PAYER.BP.AC.NO` | `CaplUbRecurrPayment_PayerBpAcNo` | TField | Yes | Field is used to store the Customer's Vendor Account number to which bill payment to be made.Mandatory field. |
| 6 | `UBR.PMT.SETUP.DATE` | `CaplUbRecurrPayment_SetupDate` | TField |  | Field is used to store the Date on which the Ebill Recurring payment is booked.Field is refer a Booking date.Valid date format field. |
| 7 | `UBR.PMT.FIXED.AMOUNT` | `CaplUbRecurrPayment_FixedAmount` | TField | Yes | Purpose of the field to store the recurring amount of bill that needs to be paid.The amount in this Field is called recurring amount.Validation - Amuont should be greater than zero.Mandatory field.Eg. 100 |
| 8 | `UBR.PMT.CURRENT.FREQUENCY` | `CaplUbRecurrPayment_CurrentFrequency` | TField |  | Field is used to store the frequency at which the recurring ebills need to be paid.Allowed inputs:1.It can have Today's date2.It can be Future date3.If Date specified as Frequency type, Date should be greater than Todayeg. 24 JUL 2015DAILY |
| 9 | `UBR.PMT.CURRENT.END.DATE` | `CaplUbRecurrPayment_CurrentEndDate` | TField | No | Field is used to store the date until which the recurring ebills need to be paid.Date entered in this field is considered as the last date for the recurring bill payment.Considered as Maturity Date of payment.Optional Input.Validation:Either CURRENT.END.DATE or NO.OF.PAYMENTS can inputtable and not both.Valid date format field. |
| 10 | `UBR.PMT.NO.OF.PAYMENTS` | `CaplUbRecurrPayment_NoOfPayments` | TField | No | The number of payments that can be made can be entered here. Optional field.Optional Input.Either CURRENT.END.DATE or NO.OF.PAYMENTS can inputable and not both.Allowed up to 3 digits, 1-99eg. 25 |
| 11 | `UBR.PMT.PAYMENT.DETAILS` | `CaplUbRecurrPayment_PaymentDetails` |  |  |  |
| 12 | `UBR.PMT.RETRY.REQ` | `CaplUbRecurrPayment_RetryReq` | TField |  | Purpose of the field to indicate if an retry is required or not, when the recurring bill payment is failed, due to any reason.Allowed inputs:YES /NOIf set as yes - (Multivalued field with No.of retries) to define no of entries and days for retryFor example:Entry: YNo of retris:1Entry: YNo of retris:2This means, there will be 2 retries one after 1 day and 2nd after 2 days.STart of Multi value field |
| 13 | `UBR.PMT.NO.OF.RETRY` | `CaplUbRecurrPayment_NoOfRetry` | TField |  | Field to store the number of retries that can be made for the payment which are failed.Based on the numbers defined in this field, system validates the to be made effective can be entered hereValidation:This field can have value only when field RETRY.REQ is set to YESFor example:Entry: YNo of retris:1Entry: YNo of retris:2This means, there will be 2 retries one after 1 day and 2nd after 2 days.End of multi value. |
| 14 | `UBR.PMT.FAIL.FEE.CODE` | `CaplUbRecurrPayment_FailFeeCode` | TField |  | Field to store the charge type to be considered, when bill payment is failed.Validation - record from FT.COMMISSION.TYPE. |
| 15 | `UBR.PMT.UB.PAYMENT.VERSION` | `CaplUbRecurrPayment_UbPaymentVersion` | TField | Yes | The version that is used for making the payment. This will be defaulted by the system.Version for Payment (Mandatory).Validation :Record from VERSION and this version should have a Valid entry in UB.MESSAGES table. |
| 16 | `UBR.PMT.NEXT.PAY.DATE` | `CaplUbRecurrPayment_NextPayDate` | TField |  | Field to store the date for next bill payment.No input field.System udpate field during COB process.Date format field. |
| 17 | `UBR.PMT.PAYMENT.REF` | `CaplUbRecurrPayment_PaymentRef` |  |  |  |
| 18 | `UBR.PMT.STATUS` | `CaplUbRecurrPayment_Status` | TField |  | Field to store the status of the Bill Payment.Noinput field.Updated by system.Allowed inputs: NEW /DELETE/MATURED.NEW - When Record created initially STATUS field will be NEWDELETE- If CANCEL.DATE is Equal to TODAY then STATUS field will be DELETEMATURED -If CURRENT.END.DATE equal to TODAY then STATUS field will be MATURED |
| 19 | `UBR.PMT.PAYMENT.CNT` | `CaplUbRecurrPayment_PaymentCnt` | TField |  | Field to store the number of payments made will be updated here.Considered as Payment count so for.Noinput field.Eg. 10 |
| 20 | `UBR.PMT.CANCEL.DATE` | `CaplUbRecurrPayment_CancelDate` | TField |  | Field to store the Date on which the recurring ebills need to be revoked/cancelled.Validation:1. Should be greater than today when record created.2. If CANCEL.DATE EQ TODAY then STATUS field gets updated with DELETE.3. If CANCEL.DATE GT TODAY and CANCEL.DATE LT NEXT.PAY.DATE then STATUS to be updated with DELETE |
| 21 | `UBR.PMT.PAY.SEQUENCE` | `CaplUbRecurrPayment_PaySequence` | TField |  | Field to store the sequence number for the Vendor for bill payments.Noinput field.Validation :If payer record is exist in CAPL.UBR.PAY.SEQUENCE table, The LAST.SEQUENCE number will be in PAY.SEQUENCE and also update.If no record existing for this Member then PAY.SEQUENCE will be 00001 |
| 22 | `UBR.PMT.PYMT.START.DATE` | `CaplUbRecurrPayment_PymtStartDate` | TField |  | Field to store the start date of the recurring bill payment. |
| 23 | `UBR.PMT.MDI.PAY.REF` | `CaplUbRecurrPayment_MdiPayRef` | TField |  | Field to update the MDI reference number for Recurring bill payment. |
| 24 | `UBR.PMT.RESERVED.3` | `CaplUbRecurrPayment_Reserved3` | TField |  |  |
| 25 | `UBR.PMT.RESERVED.4` | `CaplUbRecurrPayment_Reserved4` | TField |  |  |
| 26 | `UBR.PMT.RESERVED.5` | `CaplUbRecurrPayment_Reserved5` | TField |  |  |
| 27 | `UBR.PMT.RESERVED.6` | `CaplUbRecurrPayment_Reserved6` | TField |  |  |
| 28 | `UBR.PMT.RESERVED.7` | `CaplUbRecurrPayment_Reserved7` | TField |  |  |
| 29 | `UBR.PMT.RESERVED.8` | `CaplUbRecurrPayment_Reserved8` | TField |  |  |
| 30 | `UBR.PMT.RESERVED.9` | `CaplUbRecurrPayment_Reserved9` | TField |  |  |
| 31 | `UBR.PMT.RESERVED.10` | `CaplUbRecurrPayment_Reserved10` | TField |  |  |
| 32 | `UBR.PMT.LOCAL.REF` | `CaplUbRecurrPayment_LocalRef` |  |  |  |
| 33 | `UBR.PMT.OVERRIDE` | `CaplUbRecurrPayment_Override` |  |  |  |
| 34 | `UBR.PMT.RECORD.STATUS` | `CaplUbRecurrPayment_RecordStatus` | String |  |  |
| 35 | `UBR.PMT.CURR.NO` | `CaplUbRecurrPayment_CurrNo` | String |  |  |
| 36 | `UBR.PMT.INPUTTER` | `CaplUbRecurrPayment_Inputter` |  |  |  |
| 37 | `UBR.PMT.DATE.TIME` | `CaplUbRecurrPayment_DateTime` |  |  |  |
| 38 | `UBR.PMT.AUTHORISER` | `CaplUbRecurrPayment_Authoriser` | String |  |  |
| 39 | `UBR.PMT.CO.CODE` | `CaplUbRecurrPayment_CoCode` | String |  |  |
| 40 | `UBR.PMT.DEPT.CODE` | `CaplUbRecurrPayment_DeptCode` | String |  |  |
| 41 | `UBR.PMT.AUDITOR.CODE` | `CaplUbRecurrPayment_AuditorCode` | String |  |  |
| 42 | `UBR.PMT.AUDIT.DATE.TIME` | `CaplUbRecurrPayment_AuditDateTime` | String |  |  |
