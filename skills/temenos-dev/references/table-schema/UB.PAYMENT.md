# UB.PAYMENT — Table Schema

> Source: `INSERTS/I_F.UB.PAYMENT` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PMT.PAYER` | `UbPayment_Payer` | TField |  | Field to store the customer ID who is making the bill payment.Validation - record of CUSTOMER application. |
| 2 | `UB.PMT.PAYER.FROM.AC` | `UbPayment_PayerFromAc` | TField |  | Field to store the Customer's T24 account number used for making the bill payment to the vendor.Validation - record from ACCOUNT application. |
| 3 | `UB.PMT.PAYEE.ID` | `UbPayment_PayeeId` | TField |  | Field to store the Vendor ID for bill payment.Validation - record of UB.PAYEE.ACCT application. |
| 4 | `UB.PMT.PAYEE.NAME` | `UbPayment_PayeeName` | TField |  | Field to store the name of the vendor defined in the field PAYEE.ID.Auto defaulted based on PAYEE.ID field. |
| 5 | `UB.PMT.PAYER.BP.AC.NO` | `UbPayment_PayerBpAcNo` | TField | Yes | Field is used to store the Customer's Vendor Account number to which bill payment to be made.Mandatory field. |
| 6 | `UB.PMT.PAYEE.INT.AC.NO` | `UbPayment_PayeeIntAcNo` | TField | Yes | Field is used to store the t24 Vendor'S Account number to which bill payment to be made.Mandatory field.Validation - record from ACCOUNT application |
| 7 | `UB.PMT.EFFECTIVE.DATE` | `UbPayment_EffectiveDate` | TField | Yes | Field to store the date on which the bill payment to be effective.Considered as Value date.Date format field.Mandatory field. |
| 8 | `UB.PMT.AMOUNT` | `UbPayment_Amount` | TField | Yes | Field to store the amount for which the bill payment to be made.Mandatory field. |
| 9 | `UB.PMT.ADDITIONAL.FLD` | `UbPayment_AdditionalFld` |  |  |  |
| 10 | `UB.PMT.ADDITIONAL.VAL` | `UbPayment_AdditionalVal` |  |  |  |
| 11 | `UB.PMT.INT.OFS.MSG.ID` | `UbPayment_IntOfsMsgId` | TField |  | Fiedl to store the OFS message reference for the Bill payment. |
| 12 | `UB.PMT.INT.TXN.STATUS` | `UbPayment_IntTxnStatus` | TField |  | Field to store the Transaction Status of the Bill payment.Eg. PROCESSED, REVERSED |
| 13 | `UB.PMT.INT.TXN.ID` | `UbPayment_IntTxnId` | TField |  | Field to store the transaction reference of the bill payment.Mapped from ID of FUNDS.TRANSFER |
| 14 | `UB.PMT.INT.OVR.DETAILS` | `UbPayment_IntOvrDetails` |  |  |  |
| 15 | `UB.PMT.INT.ERR.DETAILS` | `UbPayment_IntErrDetails` |  |  |  |
| 16 | `UB.PMT.INT.DATE.TIME` | `UbPayment_IntDateTime` |  |  |  |
| 17 | `UB.PMT.EXT.TXN.STATUS` | `UbPayment_ExtTxnStatus` | TField |  | Field to store the Transaction Status at Ebill Switch.Inputs shall be :00 = Transaction Approved25 = Transaction not found |
| 18 | `UB.PMT.EXT.TXN.ID` | `UbPayment_ExtTxnId` | TField |  | Field to store the account number from which the bill is paid |
| 19 | `UB.PMT.EXT.ERR.DETAILS` | `UbPayment_ExtErrDetails` | TField |  | Field to store the error detals at Ebill Switch Level. |
| 20 | `UB.PMT.EXT.DATE.TIME` | `UbPayment_ExtDateTime` |  |  |  |
| 21 | `UB.PMT.LOCAL.REF` | `UbPayment_LocalRef` |  |  |  |
| 22 | `UB.PMT.UB.ACCT` | `UbPayment_UbAcct` | TField |  | Field to store the Account number from which the bill is paid |
| 23 | `UB.PMT.UB.PAYER.ID` | `UbPayment_UbPayerId` | TField |  | Field to store the Customer Vendor account number of the Bill payment. |
| 24 | `UB.PMT.UBR.REF.ID` | `UbPayment_UbrRefId` | TField |  | Field to store the reference ID when a recurring payment is added to the Ub Acct. |
| 25 | `UB.PMT.UB.MDI.REF` | `UbPayment_UbMdiRef` | TField |  | Field to update the MDI reference number for Bill payment. |
| 26 | `UB.PMT.RESERVED.6` | `UbPayment_Reserved6` | TField |  |  |
| 27 | `UB.PMT.RESERVED.5` | `UbPayment_Reserved5` | TField |  |  |
| 28 | `UB.PMT.RESERVED.4` | `UbPayment_Reserved4` | TField |  |  |
| 29 | `UB.PMT.RESERVED.3` | `UbPayment_Reserved3` | TField |  |  |
| 30 | `UB.PMT.RESERVED.2` | `UbPayment_Reserved2` | TField |  |  |
| 31 | `UB.PMT.RESERVED.1` | `UbPayment_Reserved1` | TField |  |  |
| 32 | `UB.PMT.OVERRIDE` | `UbPayment_Override` |  |  |  |
| 33 | `UB.PMT.RECORD.STATUS` | `UbPayment_RecordStatus` | String |  |  |
| 34 | `UB.PMT.CURR.NO` | `UbPayment_CurrNo` | String |  |  |
| 35 | `UB.PMT.INPUTTER` | `UbPayment_Inputter` |  |  |  |
| 36 | `UB.PMT.DATE.TIME` | `UbPayment_DateTime` |  |  |  |
| 37 | `UB.PMT.AUTHORISER` | `UbPayment_Authoriser` | String |  |  |
| 38 | `UB.PMT.CO.CODE` | `UbPayment_CoCode` | String |  |  |
| 39 | `UB.PMT.DEPT.CODE` | `UbPayment_DeptCode` | String |  |  |
| 40 | `UB.PMT.AUDITOR.CODE` | `UbPayment_AuditorCode` | String |  |  |
| 41 | `UB.PMT.AUDIT.DATE.TIME` | `UbPayment_AuditDateTime` | String |  |  |
