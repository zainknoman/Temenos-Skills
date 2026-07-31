# IS.PAYMENT — Table Schema

> Source: `INSERTS/I_F.IS.PAYMENT` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.PAY.PAYMENT.TYPE` | `IsPayment_PaymentType` | TField | Yes | The type of payment to be performed. Following are the list of payments supported 1. The option "Vendor" is chosen for Asset Payments 2. The option "Cost" is chosen for Cost Payments. 3. The option "Broker" is chosen for Broker Payments. 4. The option "Review" is chosen for Review Payments. 5. The option "DownPayment" is chosen for Down Payment. 6. The option "Retention" is chosen for Retention payments. 6. The option "Rebate" is chosen for Rebate payments. Validation Rules: 1. Valid values are Vendor, Cost, Broker, Review, DownPayment, Retention 2. Field Mandatory. Validation Rules: 1. Mandatory Input 2. Valid values are Vendor and Cost |
| 2 | `IS.PAY.OPERATION` | `IsPayment_Operation` | TField | Yes | The required Operation to be performed. A record in IS.PAYMENT can be created to execute a New Payment or to reverse an existing payment. The value "New" will create a new Payment and the option "Reverse" will reverse an existing payment. Validation Rules: 1. Valid values are "New" and "Reverse". 2. Field Mandatory |
| 3 | `IS.PAY.PAYMENT.CURRENCY` | `IsPayment_PaymentCurrency` | TField | Yes | The Currency in which the Payment has to be performed. The Accounts chosen for payment and the payment FT transaction will be created in this currency whereas the amount related fields are specified in terms of the currency defined in IS.CONTRACT. Validation Rules: 1. Valid Record from the table CURRENCY. 2. Field Mandatory. |
| 4 | `IS.PAY.VENDOR` | `IsPayment_Vendor` | TField | Yes | The Vendor of the Purchase contract. The Payment is made to the vendor through this application Validation Rules: 1. Must be a valid record from the table IS.VENDOR. 2. Mandatory Input |
| 5 | `IS.PAY.VENDOR.ACCT` | `IsPayment_VendorAcct` | TField |  | The Vendor account to which the vendor payment of the contract is credited. This is defaulted from the IS.VENDOR table w.r.t to the Company and Currency. If no account configured for the company and specified payment currency, no value is defaulted. Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Either Vendor Account or Beneficiary should be specified. |
| 6 | `IS.PAY.REVIEWER` | `IsPayment_Reviewer` | TField | Yes | The reviewer who reviewed the Asset or Commodity in the application IS.ASSET.REVIEW. This would represents the Appraiser or Surveyor who reviews the asset. Validation Rules: 1. Valid record in the table IS.REVIEWER. 2. Field Mandatory for the PAYMENT.TYPE "REVIEW". |
| 7 | `IS.PAY.REVIEWER.ACCT` | `IsPayment_ReviewerAcct` | TField | Yes | Account of the Reviewer in the logged-in Company and Contract Currency. This account number is defaulted from the parameterization of IS.REVIEWER record. User can specify any other account overriding the IS.REVIEWER parameter setting. Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Field Mandatory for the PAYMENT.TYPE "REVIEW". |
| 8 | `IS.PAY.BROKER` | `IsPayment_Broker` | TField | Yes | The broker to whom the broker payment has to be made. This is the broker defined as BUY.BROKER in the IS.CONTRACT specified. Validation Rules: 1. Must be a valid record in the table IS.BROKER. 2. Field mandatory if the PAYMENT.TYPE is 'BROKER' |
| 9 | `IS.PAY.BROKER.ACCT` | `IsPayment_BrokerAcct` | TField |  | The Broker account to which the broker payment of the contract is credited. This is defaulted from the IS.BROKER table w.r.t to the Company and Currency. If no account configured for the company and specified payment currency, no value is defaulted. Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Either Broker Account or Beneficiary should be specified. |
| 10 | `IS.PAY.CUSTOMER.ACCT` | `IsPayment_CustomerAcct` | TField |  | The account of the Customer who pays down payment. This is usually defaulted from the Down Payment screen. The down payment is debited from this account. This field is also allowed for Rebate Payment if RebatePayOpt is Customer. Validation Rules: 1. Must be a valid record from the table ACCOUNT. |
| 11 | `IS.PAY.BENEFICIARY` | `IsPayment_Beneficiary` | TField |  | The Beneficiary Reference defaulted from the IS.VENDOR table w.r.t to the Company and Currency. Validation Rules: 1. Must be a valid record in the table BENEFICIARY. 2. Either Vendor Account or Beneficiary should be specified. |
| 12 | `IS.PAY.BEN.CUST` | `IsPayment_BenCust` | TField |  | The Beneficiary Customer of the payment being made. The Customer who is the actual payee of the transaction. Validation Rules: 1. Value can be either free text value or valid customer id. 2. Maximum value of size 35 will be allowed. |
| 13 | `IS.PAY.ORDERING.CUST` | `IsPayment_OrderingCust` | TField | Yes | The Ordering Customer of the payment. This is defined in order to facilitate external FT payments. Validation Rules: 1. Field Mandatory for NOSTRO payments using BENEFICIARY. |
| 14 | `IS.PAY.VALUE.DATE` | `IsPayment_ValueDate` | TField |  | The Value date of the payment. If no date is given, system defaults the date to TODAY. Validation Rules: 1. Standard T24 Date field |
| 15 | `IS.PAY.PAYMENT.METHOD` | `IsPayment_PaymentMethod` | TField | Yes | The Payment Method to be executed for the payment. The following are the options: 1. ADHOC - FT Payment raised on authorization of the IS.PAYMENT record. 2. DD - Teller Payment done will be raised and the same transaction is recorded in IS.PAYMENT. 3. CASH - FT Payment done will be raised from the FT application and the same transaction is recorded in IS.PAYMENT. 4. SCHEDULE - FT Payment is recorded in the field IS.AUTO.PAY.SCHEDULES as defined in the schedule. 5. EXTERNAL - FT Payment will be raised from the FT application for broker payment and the same transaction is recorded in IS.PAYMENT. 6. DISBURSEMENT - For Payment of a contract which does not undergo purchase processing and the payment amount is controlled by the amount disbursed in the AA finance contract. Validation Rules: 1. Mandatory Input. 2. Valid Values are ADHOC, DD, CASH and SCHEDULE |
| 16 | `IS.PAY.PURCHASE.REF` | `IsPayment_PurchaseRef` |  |  |  |
| 17 | `IS.PAY.COMMODITY` | `IsPayment_Commodity` |  |  |  |
| 18 | `IS.PAY.ASSET.REF` | `IsPayment_AssetRef` |  |  |  |
| 19 | `IS.PAY.COST.REF` | `IsPayment_CostRef` |  |  |  |
| 20 | `IS.PAY.REVIEW.REF` | `IsPayment_ReviewRef` |  |  |  |
| 21 | `IS.PAY.PAYMENT.REF` | `IsPayment_PaymentRef` |  |  |  |
| 22 | `IS.PAY.PARENT.REF` | `IsPayment_ParentRef` |  |  |  |
| 23 | `IS.PAY.DECLARATION.REF` | `IsPayment_DeclarationRef` |  |  |  |
| 24 | `IS.PAY.BILL.DATE` | `IsPayment_BillDate` |  |  |  |
| 25 | `IS.PAY.BILL.AMT` | `IsPayment_BillAmt` |  |  |  |
| 26 | `IS.PAY.STATUS` | `IsPayment_Status` |  |  |  |
| 27 | `IS.PAY.RETENTION.PCT` | `IsPayment_RetentionPct` |  |  |  |
| 28 | `IS.PAY.PAYMENT.AMT` | `IsPayment_PaymentAmt` |  |  |  |
| 29 | `IS.PAY.RETENTION.AMT` | `IsPayment_RetentionAmt` |  |  |  |
| 30 | `IS.PAY.RESERVED.20` | `IsPayment_Reserved20` |  |  |  |
| 31 | `IS.PAY.RESERVED.19` | `IsPayment_Reserved19` |  |  |  |
| 32 | `IS.PAY.RESERVED.18` | `IsPayment_Reserved18` |  |  |  |
| 33 | `IS.PAY.RESERVED.17` | `IsPayment_Reserved17` |  |  |  |
| 34 | `IS.PAY.RESERVED.16` | `IsPayment_Reserved16` |  |  |  |
| 35 | `IS.PAY.TOTAL.BILL.AMT` | `IsPayment_TotalBillAmt` |  |  |  |
| 36 | `IS.PAY.RETENTION.ACCT` | `IsPayment_RetentionAcct` |  |  |  |
| 37 | `IS.PAY.REBATE.PAY.OPT` | `IsPayment_RebatePayOpt` |  |  |  |
| 38 | `IS.PAY.REBATE.PL.CATEG` | `IsPayment_RebatePlCateg` |  |  |  |
| 39 | `IS.PAY.RESERVED.13` | `IsPayment_Reserved13` |  |  |  |
| 40 | `IS.PAY.RESERVED.12` | `IsPayment_Reserved12` |  |  |  |
| 41 | `IS.PAY.RESERVED.11` | `IsPayment_Reserved11` |  |  |  |
| 42 | `IS.PAY.SOURCE.APPLICATION` | `IsPayment_SourceApplication` | TField |  | No Input field. This fields displays the application from which the payment transactions is initiated. Example: FUNDS.TRANSFER, IS.PAYMENT. |
| 43 | `IS.PAY.RESERVED.9` | `IsPayment_Reserved9` | TField |  |  |
| 44 | `IS.PAY.RESERVED.8` | `IsPayment_Reserved8` | TField |  |  |
| 45 | `IS.PAY.RESERVED.7` | `IsPayment_Reserved7` | TField |  |  |
| 46 | `IS.PAY.RESERVED.6` | `IsPayment_Reserved6` | TField |  |  |
| 47 | `IS.PAY.RESERVED.5` | `IsPayment_Reserved5` | TField |  |  |
| 48 | `IS.PAY.RESERVED.4` | `IsPayment_Reserved4` | TField |  |  |
| 49 | `IS.PAY.RESERVED.3` | `IsPayment_Reserved3` | TField |  |  |
| 50 | `IS.PAY.RESERVED.2` | `IsPayment_Reserved2` | TField |  |  |
| 51 | `IS.PAY.RESERVED.1` | `IsPayment_Reserved1` | TField |  |  |
| 52 | `IS.PAY.LOCAL.REF` | `IsPayment_LocalRef` |  |  |  |
| 53 | `IS.PAY.STMT.NOS` | `IsPayment_StmtNos` |  |  |  |
| 54 | `IS.PAY.OVERRIDE` | `IsPayment_Override` |  |  |  |
| 55 | `IS.PAY.RECORD.STATUS` | `IsPayment_RecordStatus` | String |  |  |
| 56 | `IS.PAY.CURR.NO` | `IsPayment_CurrNo` | String |  |  |
| 57 | `IS.PAY.INPUTTER` | `IsPayment_Inputter` |  |  |  |
| 58 | `IS.PAY.DATE.TIME` | `IsPayment_DateTime` |  |  |  |
| 59 | `IS.PAY.AUTHORISER` | `IsPayment_Authoriser` | String |  |  |
| 60 | `IS.PAY.CO.CODE` | `IsPayment_CoCode` | String |  |  |
| 61 | `IS.PAY.DEPT.CODE` | `IsPayment_DeptCode` | String |  |  |
| 62 | `IS.PAY.AUDITOR.CODE` | `IsPayment_AuditorCode` | String |  |  |
| 63 | `IS.PAY.AUDIT.DATE.TIME` | `IsPayment_AuditDateTime` | String |  |  |
