# PAYMENT.STOP — Table Schema

> Source: `INSERTS/I_F.PAYMENT.STOP` in `CQ_ChqPaymentStop.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.PAY.CURRENCY` | `PaymentStop_Currency` | TField |  | Identifies the Currency of the Account to which this Payment Stop record refers. The amounts input to the AMOUNT FROM (Field 6) and AMOUNT TO (Field 7) must be in the Currency indicated by this field. Validation Rules: Automatically generated field. No input possible. |
| 2 | `AC.PAY.PAYM.STOP.TYPE` | `PaymentStop_PaymStopType` |  |  |  |
| 3 | `AC.PAY.FIRST.CHEQUE.NO` | `PaymentStop_FirstChequeNo` |  |  |  |
| 4 | `AC.PAY.LAST.CHEQUE.NO` | `PaymentStop_LastChequeNo` |  |  |  |
| 5 | `AC.PAY.NO.OF.LEAVES` | `PaymentStop_NoOfLeaves` |  |  |  |
| 6 | `AC.PAY.CHEQUE.TYPE` | `PaymentStop_ChequeType` |  |  |  |
| 7 | `AC.PAY.STOP.DATE` | `PaymentStop_StopDate` |  |  |  |
| 8 | `AC.PAY.AMOUNT.FROM` | `PaymentStop_AmountFrom` |  |  |  |
| 9 | `AC.PAY.AMOUNT.TO` | `PaymentStop_AmountTo` |  |  |  |
| 10 | `AC.PAY.STOP.ACTIVE` | `PaymentStop_StopActive` |  |  |  |
| 11 | `AC.PAY.WAIVE.CHARGE` | `PaymentStop_WaiveCharge` |  |  |  |
| 12 | `AC.PAY.BENEFICIARY` | `PaymentStop_Beneficiary` |  |  |  |
| 13 | `AC.PAY.STOP.END.FLAG` | `PaymentStop_StopEndFlag` |  |  |  |
| 14 | `AC.PAY.APPLY.DATE` | `PaymentStop_ApplyDate` |  |  |  |
| 15 | `AC.PAY.REMARKS` | `PaymentStop_Remarks` |  |  |  |
| 16 | `AC.PAY.RAISE.ACTIVITY` | `PaymentStop_RaiseActivity` |  |  |  |
| 17 | `AC.PAY.CHARGE.CODE` | `PaymentStop_ChargeCode` |  |  |  |
| 18 | `AC.PAY.CHG.ACCOUNT` | `PaymentStop_ChgAccount` |  |  |  |
| 19 | `AC.PAY.CHG.CURRENCY` | `PaymentStop_ChgCurrency` |  |  |  |
| 20 | `AC.PAY.CHG.AMOUNT` | `PaymentStop_ChgAmount` |  |  |  |
| 21 | `AC.PAY.TAX.TYPE` | `PaymentStop_TaxType` |  |  |  |
| 22 | `AC.PAY.TAX.AMT` | `PaymentStop_TaxAmt` |  |  |  |
| 23 | `AC.PAY.TAX.CCY` | `PaymentStop_TaxCcy` |  |  |  |
| 24 | `AC.PAY.TAX.DATE` | `PaymentStop_TaxDate` |  |  |  |
| 25 | `AC.PAY.RESERVED.1` | `PaymentStop_Reserved1` |  |  |  |
| 26 | `AC.PAY.RESERVED.2` | `PaymentStop_Reserved2` |  |  |  |
| 27 | `AC.PAY.TRANS.REFERENCE` | `PaymentStop_TransReference` |  |  |  |
| 28 | `AC.PAY.CUSTOMER.NO` | `PaymentStop_CustomerNo` | TField | Yes | Identifies the Customer to whom the Cheque/Account belongs. When the field MESSAGE.REC is Blank the SWIFT Message is sent to the SWIFT address of this customer on the DE.ADDRESS File. This field is Inputtable only if RAISE.ACTIVITY is set to Yes or if created from EB.MESSAGE.111. Mandatory Field (when RAISE.ACTIVITY is set to Yes). Validation Rules: 1-10 numeric character Customer Code or 3-10 type MNE (uppercase alpha or numeric or '.') character Customer Mnemonic. |
| 29 | `AC.PAY.DATE.OF.ISSUE` | `PaymentStop_DateOfIssue` | TField | Yes | This field contains the date on which the cheque (FIRST.CHEQUE.NO) was issued. This field is Inputtable only if RAISE.ACTIVITY is set to Yes or if created from EB.MESSAGE.111 Mandatory Field (when RAISE.ACTIVITY is set to Yes). Note: This field must less than STOP.DATE and ACTION.DATE. This field does not accept forward dates. Validation Rules: Up to 9 type D date characters (Date format in range 1950 to 2049). |
| 30 | `AC.PAY.ACTION.DATE` | `PaymentStop_ActionDate` | TField |  | Identifies the Value Date when the Drawer Bank has previously credited the Drawee Bank with the cheque amount. Note: This field should not be less than STOP.DATE and DATE.OF.ISSUE. This field is Inputtable only if RAISE.ACTIVITY is set to Yes. This field does not accept forward dates. Validation Rules: Up to 9 type D date characters (Date format in range 1950 to 2049) Type D. |
| 31 | `AC.PAY.OUR.REFERENCE` | `PaymentStop_OurReference` | A (Alphanumeric) | Yes | This field identifies the reference assigned by the sender to unambiguously identify the message. This field is Imputable only if RAISE.ACTIVITY is set to Yes or if created from EB.MESSAGE.111. Mandatory Field (when RAISE.ACTIVITY is set to Yes). Validation Rules: Up to 16 type A (Alphanumeric) characters. This field must not start or end with a / and must not contain two consecutive slashes // (SWIFT Error Code T26) |
| 32 | `AC.PAY.MESSAGE.REC` | `PaymentStop_MessageRec` | S (SWIFT) |  | MESSAGE.REC: This field identifies an alternative delivery address other than the Drawer Bank (Customer) If an entry of a SWIFT address is made to MESSAGE.REC, then AC.PAYMENT.STOP.DELIVERY will route the message direct to the address entered, using the OVERRIDE CARRIER and OVERRIDE DELIVERY ADDRESS for delivery. Identifies the Company or Customer, carrier and address version number whose address is held in the DE.ADDRESS File. Validation Rules: 12 type S (SWIFT) characters. OR 1-10 numeric character Customer Code or 3-10 type MNE (uppercase alpha or numeric or '.') character Customer Mnemonic. Acceptable Inputs are either a Customer Number (whose address is held in the DE.ADDRESS File) or a valid SWIFT Address preceded by SW- e.g. SW-PDOUUS23 No Multi Values Allowed. |
| 33 | `AC.PAY.PAYEE` | `PaymentStop_Payee` |  |  |  |
| 34 | `AC.PAY.ANSWERS` | `PaymentStop_Answers` |  |  |  |
| 35 | `AC.PAY.SEND.NOTICE` | `PaymentStop_SendNotice` |  |  |  |
| 36 | `AC.PAY.ACTIVITY.CODE` | `PaymentStop_ActivityCode` |  |  |  |
| 37 | `AC.PAY.ACTIVITY.DATE` | `PaymentStop_ActivityDate` |  |  |  |
| 38 | `AC.PAY.MAPPING.KEY` | `PaymentStop_MappingKey` |  |  |  |
| 39 | `AC.PAY.DELIVERY.REF` | `PaymentStop_DeliveryRef` |  |  |  |
| 40 | `AC.PAY.MT112.CHEQUE.NO` | `PaymentStop_Mt112ChequeNo` | TField |  | Identifies the Cheque Number, which is being stopped. This relates to SWIFT Tag 21 in Swift Message MT112. This field is defaulted from the FIRST.CHEQUE.NO field for the set of Multi-Values for which RAISE.ACTIVITY has been set to "Yes". Validation Rules: Automatically generated field. No input possible. |
| 41 | `AC.PAY.MT112.AMOUNT` | `PaymentStop_Mt112Amount` | TField |  | Specifies the Amount for the Cheque, which is being stopped. This relates to SWIFT Tag 32A in Swift Message MT112. This field is defaulted from the AMOUNT.FROM field for the set of Multi-Values for which RAISE.ACTIVITY has been set to "Yes". Validation Rules: Automatically generated field. No input possible. |
| 42 | `AC.PAY.LOCAL.REF` | `PaymentStop_LocalRef` |  |  |  |
| 43 | `AC.PAY.MOD.PS.CHQ.NO` | `PaymentStop_ModPsChqNo` |  |  |  |
| 44 | `AC.PAY.MOD.CHQ.TYPE` | `PaymentStop_ModChqType` |  |  |  |
| 45 | `AC.PAY.MOD.PS.DATE` | `PaymentStop_ModPsDate` |  |  |  |
| 46 | `AC.PAY.REV.AUTH.DATE` | `PaymentStop_RevAuthDate` |  |  |  |
| 47 | `AC.PAY.IN.DRAWER.BK.ACCT` | `PaymentStop_InDrawerBkAcct` | TField |  | Contains the inward Drawer bank Account No in the same format as received from delivery or the clearing system. Validation Rules: This is a NOINPUT field. |
| 48 | `AC.PAY.IN.DRAWER.BANK` | `PaymentStop_InDrawerBank` |  |  |  |
| 49 | `AC.PAY.IN.DELIVERY.REF` | `PaymentStop_InDeliveryRef` | TField |  | Identifies the reference number allocated by Delivery for incoming SWIFT message received direct from Delivery. This will enable enquiries to be made on the original SWIFT message received. Validation Rules: No Input - Internal field. |
| 50 | `AC.PAY.INWARD.MSG.TYPE` | `PaymentStop_InwardMsgType` | TField |  | Identifies the incoming SWIFT message Validation Rules: No Input - Internal field. |
| 51 | `AC.PAY.IN.SWIFT.MSG` | `PaymentStop_InSwiftMsg` |  |  |  |
| 52 | `AC.PAY.IN.PROCESS.ERR` | `PaymentStop_InProcessErr` |  |  |  |
| 53 | `AC.PAY.DD.BC.SORT.CODE` | `PaymentStop_DdBcSortCode` |  |  |  |
| 54 | `AC.PAY.DD.MANDATE.REF` | `PaymentStop_DdMandateRef` |  |  |  |
| 55 | `AC.PAY.DD.STOP.TYPE` | `PaymentStop_DdStopType` |  |  |  |
| 56 | `AC.PAY.RESERVED1` | `PaymentStop_Reserved1` |  |  |  |
| 57 | `AC.PAY.STMT.NOS` | `PaymentStop_StmtNos` |  |  |  |
| 58 | `AC.PAY.OVERRIDE` | `PaymentStop_Override` |  |  |  |
| 59 | `AC.PAY.RECORD.STATUS` | `PaymentStop_RecordStatus` | String |  |  |
| 60 | `AC.PAY.CURR.NO` | `PaymentStop_CurrNo` | String |  |  |
| 61 | `AC.PAY.INPUTTER` | `PaymentStop_Inputter` |  |  |  |
| 62 | `AC.PAY.DATE.TIME` | `PaymentStop_DateTime` |  |  |  |
| 63 | `AC.PAY.AUTHORISER` | `PaymentStop_Authoriser` | String |  |  |
| 64 | `AC.PAY.CO.CODE` | `PaymentStop_CoCode` | String |  |  |
| 65 | `AC.PAY.DEPT.CODE` | `PaymentStop_DeptCode` | String |  |  |
| 66 | `AC.PAY.AUDITOR.CODE` | `PaymentStop_AuditorCode` | String |  |  |
| 67 | `AC.PAY.AUDIT.DATE.TIME` | `PaymentStop_AuditDateTime` | String |  |  |
