# IS.PAYMENT.BALANCES — Table Schema

> Source: `INSERTS/I_F.IS.PAYMENT.BALANCES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.PBL.ORIG.PAYMENT.DUE` | `IsPaymentBalances_OrigPaymentDue` | TField |  | The purchase or cost amount exclusive of the down payment(in case of Asset/commodity) declared in the Islamic contract. For Islamic contracts that are financed without purchase processing, this field will get updated as and when a disbursement happens. At any point of time, only the disbursed amount can be paid to the vendor in this case. |
| 2 | `IS.PBL.PAYMENT.OUTSTANDING` | `IsPaymentBalances_PaymentOutstanding` | TField |  | The Asset or Cost amount due to be paid/scheduled for the Vendor or Cost Payment of the Purchase contract. |
| 3 | `IS.PBL.TOT.PAID.AMT` | `IsPaymentBalances_TotPaidAmt` | TField |  | The Total amount paid to the vendor on account of an asset, a commodity or an additional cost of a purchase contract. |
| 4 | `IS.PBL.RETENTION.AMT.PAID` | `IsPaymentBalances_RetentionAmtPaid` | TField |  | The total Retention Amount retained from the Vendor Payments. |
| 5 | `IS.PBL.RET.VENDOR.DUE` | `IsPaymentBalances_RetVendorDue` | TField |  | The Retention Amount due to be paid to the Vendor exclusive of the retention payments to the Vendor. |
| 6 | `IS.PBL.RET.VENDOR.PAID` | `IsPaymentBalances_RetVendorPaid` | TField |  | The amount paid to the Vendor from the Retention bucket. The portion retained from the vendor is stored in the field RET.VENDOR.DUE. As and when the retained portion is paid to the vendor, the amount in this field will go down by that amount. |
| 7 | `IS.PBL.IS.PAYMENT.REF` | `IsPaymentBalances_IsPaymentRef` |  |  |  |
| 8 | `IS.PBL.BILL.DATE` | `IsPaymentBalances_BillDate` |  |  |  |
| 9 | `IS.PBL.PAYMENT.AMT` | `IsPaymentBalances_PaymentAmt` |  |  |  |
| 10 | `IS.PBL.PAY.REF` | `IsPaymentBalances_PayRef` |  |  |  |
| 11 | `IS.PBL.RETENTION.AMT` | `IsPaymentBalances_RetentionAmt` |  |  |  |
| 12 | `IS.PBL.RET.PAY.REF` | `IsPaymentBalances_RetPayRef` |  |  |  |
| 13 | `IS.PBL.STATUS` | `IsPaymentBalances_Status` |  |  |  |
| 14 | `IS.PBL.COST.ID` | `IsPaymentBalances_CostId` |  |  |  |
| 15 | `IS.PBL.RESERVED.24` | `IsPaymentBalances_Reserved24` |  |  |  |
| 16 | `IS.PBL.RESERVED.23` | `IsPaymentBalances_Reserved23` |  |  |  |
| 17 | `IS.PBL.RESERVED.22` | `IsPaymentBalances_Reserved22` |  |  |  |
| 18 | `IS.PBL.RESERVED.21` | `IsPaymentBalances_Reserved21` |  |  |  |
| 19 | `IS.PBL.PAYMENT.OWNER` | `IsPaymentBalances_PaymentOwner` |  |  |  |
| 20 | `IS.PBL.PAYMENT.ACCOUNT` | `IsPaymentBalances_PaymentAccount` |  |  |  |
| 21 | `IS.PBL.PAYMENT.TYPE` | `IsPaymentBalances_PaymentType` |  |  |  |
| 22 | `IS.PBL.SOURCE` | `IsPaymentBalances_Source` |  |  |  |
| 23 | `IS.PBL.RESERVED.16` | `IsPaymentBalances_Reserved16` |  |  |  |
| 24 | `IS.PBL.PURCHASE.REF` | `IsPaymentBalances_PurchaseRef` | TField |  | The Purchase reference for which the Payment is made. |
| 25 | `IS.PBL.RET.VENDOR.REF` | `IsPaymentBalances_RetVendorRef` |  |  |  |
| 26 | `IS.PBL.RET.VENDOR.AMT` | `IsPaymentBalances_RetVendorAmt` |  |  |  |
| 27 | `IS.PBL.RET.VENDOR.STATUS` | `IsPaymentBalances_RetVendorStatus` |  |  |  |
| 28 | `IS.PBL.RESERVED.15` | `IsPaymentBalances_Reserved15` |  |  |  |
| 29 | `IS.PBL.RESERVED.14` | `IsPaymentBalances_Reserved14` |  |  |  |
| 30 | `IS.PBL.RESERVED.13` | `IsPaymentBalances_Reserved13` |  |  |  |
| 31 | `IS.PBL.RESERVED.12` | `IsPaymentBalances_Reserved12` |  |  |  |
| 32 | `IS.PBL.RESERVED.11` | `IsPaymentBalances_Reserved11` |  |  |  |
| 33 | `IS.PBL.DP.DECLARED` | `IsPaymentBalances_DpDeclared` | TField |  | The down payment amount declared by the customer in the contract in terms of Cash to the Bank. These are defined in the multi-value set of fields DP.COMMODITY-TOTAL.DP.CASH in the application IS.CONTRACT |
| 34 | `IS.PBL.DP.AMOUNT` | `IsPaymentBalances_DpAmount` |  |  |  |
| 35 | `IS.PBL.DECLARATION.REF` | `IsPaymentBalances_DeclarationRef` |  |  |  |
| 36 | `IS.PBL.DP.FT.REF` | `IsPaymentBalances_DpFtRef` |  |  |  |
| 37 | `IS.PBL.DP.STATUS` | `IsPaymentBalances_DpStatus` |  |  |  |
| 38 | `IS.PBL.DP.PAY.REF` | `IsPaymentBalances_DpPayRef` |  |  |  |
| 39 | `IS.PBL.DP.SOURCE` | `IsPaymentBalances_DpSource` |  |  |  |
| 40 | `IS.PBL.DP.DATE` | `IsPaymentBalances_DpDate` |  |  |  |
| 41 | `IS.PBL.RESERVED.8` | `IsPaymentBalances_Reserved8` |  |  |  |
| 42 | `IS.PBL.RESERVED.7` | `IsPaymentBalances_Reserved7` |  |  |  |
| 43 | `IS.PBL.RESERVED.6` | `IsPaymentBalances_Reserved6` |  |  |  |
| 44 | `IS.PBL.TOT.DOWN.PAYMENT` | `IsPaymentBalances_TotDownPayment` | TField |  | The Total Down Payment Paid for the Asset or Commodity |
| 45 | `IS.PBL.REVIEW.TYPE` | `IsPaymentBalances_ReviewType` |  |  |  |
| 46 | `IS.PBL.REVIEW.ID` | `IsPaymentBalances_ReviewId` |  |  |  |
| 47 | `IS.PBL.REVIEW.DATE` | `IsPaymentBalances_ReviewDate` |  |  |  |
| 48 | `IS.PBL.PROGRESS.PERCENT` | `IsPaymentBalances_ProgressPercent` |  |  |  |
| 49 | `IS.PBL.REVIEW.FEES` | `IsPaymentBalances_ReviewFees` |  |  |  |
| 50 | `IS.PBL.REVIEW.STATUS` | `IsPaymentBalances_ReviewStatus` |  |  |  |
| 51 | `IS.PBL.REVIEW.FT.REF` | `IsPaymentBalances_ReviewFtRef` |  |  |  |
| 52 | `IS.PBL.REVIEW.PAY.REF` | `IsPaymentBalances_ReviewPayRef` |  |  |  |
| 53 | `IS.PBL.REVIEW.CUST.FT` | `IsPaymentBalances_ReviewCustFt` |  |  |  |
| 54 | `IS.PBL.REVIEWER.ID` | `IsPaymentBalances_ReviewerId` |  |  |  |
| 55 | `IS.PBL.REVIEW.PAYMENT.TYPE` | `IsPaymentBalances_ReviewPaymentType` |  |  |  |
| 56 | `IS.PBL.REVIEW.PAY.SOURCE` | `IsPaymentBalances_ReviewPaySource` |  |  |  |
| 57 | `IS.PBL.TOT.REVIEW.FEES` | `IsPaymentBalances_TotReviewFees` |  |  |  |
| 58 | `IS.PBL.RESERVED.1` | `IsPaymentBalances_Reserved1` |  |  |  |
| 59 | `IS.PBL.VENDOR.ID` | `IsPaymentBalances_VendorId` | TField |  | Vendor customer of this payment type. Should be a valid customer and a involved party in a contract as a vendor. |
| 60 | `IS.PBL.REBATE.AMT` | `IsPaymentBalances_RebateAmt` |  |  |  |
| 61 | `IS.PBL.REBATE.DATE` | `IsPaymentBalances_RebateDate` |  |  |  |
| 62 | `IS.PBL.REBATE.PAY.REF` | `IsPaymentBalances_RebatePayRef` |  |  |  |
| 63 | `IS.PBL.REBATE.FT.REF` | `IsPaymentBalances_RebateFtRef` |  |  |  |
| 64 | `IS.PBL.REBATE.STATUS` | `IsPaymentBalances_RebateStatus` |  |  |  |
| 65 | `IS.PBL.REBATE.PAID.TO` | `IsPaymentBalances_RebatePaidTo` |  |  |  |
| 66 | `IS.PBL.REBATE.SOURCE` | `IsPaymentBalances_RebateSource` |  |  |  |
| 67 | `IS.PBL.TOT.REBATE.PAYMENT` | `IsPaymentBalances_TotRebatePayment` | TField |  | Rebate payment can be done in stages. This field will be updated with the total rebate amount paid. |
| 68 | `IS.PBL.TOT.REBATE.AMT` | `IsPaymentBalances_TotRebateAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 69 | `IS.PBL.PURCHASE.AMT` | `IsPaymentBalances_PurchaseAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
