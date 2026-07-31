# IS.DISBURSEMENT — Table Schema

> Source: `INSERTS/I_F.IS.DISBURSEMENT` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.DIS.CUSTOMER` | `IsDisbursement_Customer` | TField |  | The Customer of the Contract. The finance contract of this customer will undergo disbursement. Validation Rules: 1. Field No-Change. |
| 2 | `IS.DIS.PURCHASE.REF` | `IsDisbursement_PurchaseRef` | TField |  | The Islamic contract for which the finance is disbursed. The contract specified in this field is the Islamic contract in the application IS.CONTRACT through which the customer requests the asset. |
| 3 | `IS.DIS.COMMODITY` | `IsDisbursement_Commodity` | TField |  | Commodity of the Asset Requested in the Islamic Contract. Validation Rules: 1. Must be a valid record from the table IS.COMMODITY. 2. Allowed only for a Quantified asset. |
| 4 | `IS.DIS.ASSET.REF` | `IsDisbursement_AssetRef` | TField |  | The Asset requested by the Customer for which a Disbursement has to be performed. Validation Rules: 1. The Asset being requested in the Islamic Contract. 2. Must be a valid record in the Asset table defined in the Commodity record. |
| 5 | `IS.DIS.PURCHASE.PRICE` | `IsDisbursement_PurchasePrice` | TField |  | The Purchase Price of the Asset / Commodity as defined in the Islamic Contract. Validation Rules: 1. Field No-input. 2. The field is defaulted with the value defined in the PURCHASE.PRICE field of the respective Asset/Commodity defined in the application IS.CONTRACT. |
| 6 | `IS.DIS.CURRENCY` | `IsDisbursement_Currency` | TField |  | The Currency of the Contract. This is defaulted from the IS.CONTRACT record. Validation Rules: 1. Field No-input. |
| 7 | `IS.DIS.BILL.DATE` | `IsDisbursement_BillDate` | TField |  | The Bill date of the disbursement. The Disbursement on the Arrangement will be effective on this date. Validation Rules: 1. Standard T24 Date Field. |
| 8 | `IS.DIS.BILL.AMOUNT` | `IsDisbursement_BillAmount` | TField |  | The Bill Amount of the Disbursement. The Amount to be disbursed for the finance contract should be specified here. Validation Rules: 1. The amount should not exceed the purchase price of the asset/commodity. |
| 9 | `IS.DIS.CONTRIB.TYPE` | `IsDisbursement_ContribType` |  |  |  |
| 10 | `IS.DIS.CONTRIB.PAYTO` | `IsDisbursement_ContribPayto` |  |  |  |
| 11 | `IS.DIS.AMOUNT.TYPE` | `IsDisbursement_AmountType` |  |  |  |
| 12 | `IS.DIS.CONTRIB.VALUE` | `IsDisbursement_ContribValue` |  |  |  |
| 13 | `IS.DIS.CONTRIB.PERC` | `IsDisbursement_ContribPerc` |  |  |  |
| 14 | `IS.DIS.CONTRIB.AMT` | `IsDisbursement_ContribAmt` |  |  |  |
| 15 | `IS.DIS.RESERVED.15` | `IsDisbursement_Reserved15` |  |  |  |
| 16 | `IS.DIS.RESERVED.14` | `IsDisbursement_Reserved14` |  |  |  |
| 17 | `IS.DIS.RESERVED.13` | `IsDisbursement_Reserved13` |  |  |  |
| 18 | `IS.DIS.RESERVED.12` | `IsDisbursement_Reserved12` |  |  |  |
| 19 | `IS.DIS.RESERVED.11` | `IsDisbursement_Reserved11` |  |  |  |
| 20 | `IS.DIS.CUST.CONTRIB` | `IsDisbursement_CustContrib` | TField |  | Sum of all the customer contribution amounts. Validation Rules: 1. Field No-input. |
| 21 | `IS.DIS.BANK.CONTRIB` | `IsDisbursement_BankContrib` | TField |  | The Bank contribution for the Disbursement bill defined. This value could even be Zero. Validation Rules: 1. Field No-input. |
| 22 | `IS.DIS.CASH.CONTRIB` | `IsDisbursement_CashContrib` | TField |  | The Customer contribution in terms of Cash paid to the Bank. The sum of amounts defined with CONTRIB.TYPE as &quot;CASH&quot; and CONTRIB.PAYTO as &quot;BANK&quot;. Validation Rules: 1. Field No-input. |
| 23 | `IS.DIS.DISBURSE.AMT` | `IsDisbursement_DisburseAmt` | TField |  | The Disburse Amount to be disbursed from the finance contract. Validation Rules: 1. Field No-input. |
| 24 | `IS.DIS.COMMIT.DECR.AMT` | `IsDisbursement_CommitDecrAmt` | TField |  | The Commitment Decrease Amount that is to be decreased from the Finance contract. This value is the difference of the values in the fields CUST.CONTRIB and CASH.CONTRIB. Validation Rules: 1. Field No-input. |
| 25 | `IS.DIS.REPAYMENT.AMT` | `IsDisbursement_RepaymentAmt` | TField |  | The Repayment Amount is the Advance Payment amount of the finance contract. The value in this field is the Customer Contribution in terms of CONTRIB.TYPE as &quot;CASH&quot; and CONTRIB.PAYTO as &quot;BANK&quot;. Validation Rules: 1. Field No-input. |
| 26 | `IS.DIS.RESERVED.10` | `IsDisbursement_Reserved10` | TField |  |  |
| 27 | `IS.DIS.RESERVED.9` | `IsDisbursement_Reserved9` | TField |  |  |
| 28 | `IS.DIS.RESERVED.8` | `IsDisbursement_Reserved8` | TField |  |  |
| 29 | `IS.DIS.RESERVED.7` | `IsDisbursement_Reserved7` | TField |  |  |
| 30 | `IS.DIS.RESERVED.6` | `IsDisbursement_Reserved6` | TField |  |  |
| 31 | `IS.DIS.RESERVED.5` | `IsDisbursement_Reserved5` | TField |  |  |
| 32 | `IS.DIS.RESERVED.4` | `IsDisbursement_Reserved4` | TField |  |  |
| 33 | `IS.DIS.RESERVED.3` | `IsDisbursement_Reserved3` | TField |  |  |
| 34 | `IS.DIS.RESERVED.2` | `IsDisbursement_Reserved2` | TField |  |  |
| 35 | `IS.DIS.RESERVED.1` | `IsDisbursement_Reserved1` | TField |  |  |
| 36 | `IS.DIS.LOCAL.REF` | `IsDisbursement_LocalRef` |  |  |  |
| 37 | `IS.DIS.STMT.NOS` | `IsDisbursement_StmtNos` |  |  |  |
| 38 | `IS.DIS.OVERRIDE` | `IsDisbursement_Override` |  |  |  |
| 39 | `IS.DIS.RECORD.STATUS` | `IsDisbursement_RecordStatus` | String |  |  |
| 40 | `IS.DIS.CURR.NO` | `IsDisbursement_CurrNo` | String |  |  |
| 41 | `IS.DIS.INPUTTER` | `IsDisbursement_Inputter` |  |  |  |
| 42 | `IS.DIS.DATE.TIME` | `IsDisbursement_DateTime` |  |  |  |
| 43 | `IS.DIS.AUTHORISER` | `IsDisbursement_Authoriser` | String |  |  |
| 44 | `IS.DIS.CO.CODE` | `IsDisbursement_CoCode` | String |  |  |
| 45 | `IS.DIS.DEPT.CODE` | `IsDisbursement_DeptCode` | String |  |  |
| 46 | `IS.DIS.AUDITOR.CODE` | `IsDisbursement_AuditorCode` | String |  |  |
| 47 | `IS.DIS.AUDIT.DATE.TIME` | `IsDisbursement_AuditDateTime` | String |  |  |
