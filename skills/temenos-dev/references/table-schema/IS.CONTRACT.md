# IS.CONTRACT — Table Schema

> Source: `INSERTS/I_F.IS.CONTRACT` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.CON.DESCRIPTION` | `IsContract_Description` |  |  |  |
| 2 | `IS.CON.CUSTOMER` | `IsContract_Customer` | TField | Yes | The Customer who requests the asset and the contract is booked for. Validation Rules: 1. Field Mandatory. 2. Must be a valid record in the table CUSTOMER. |
| 3 | `IS.CON.PRODUCT` | `IsContract_Product` | TField | Yes | This field is to specify the type of product the asset will be processed Validation Rules: 1. Field Mandatory 2. Must be a valid record from the table IS.PARAMETER. |
| 4 | `IS.CON.STATUS` | `IsContract_Status` | TField |  | The status of the Contract like REQUEST, APPROVAL, PURCHASE. The status transition happens according to the workflow defined in the IS.PARAMETER. Validation Rules: 1. The values to the field are defined in the EB.LOOKUP table with prefix "IS.WF.STATUS*". 2. Currently, APPROVAL and PURCHASE is designed to raise accounting entries. The Accounting entries for Cost is raised during the PURCHASE status |
| 5 | `IS.CON.STATUS.VALUE.DATE` | `IsContract_StatusValueDate` | TField |  | Date on which the Status is effective. Defaulted to the date given in the field VALUE.DATE. Validation Rules: 1. Standard T24 Date. 2. Defaulted to the value in the field VALUE.DATE if null |
| 6 | `IS.CON.ACCOUNTING.EVENT` | `IsContract_AccountingEvent` |  |  |  |
| 7 | `IS.CON.CURRENCY` | `IsContract_Currency` | TField | Yes | The currency in which the contract is booked. Validation Rules: 1. Field Mandatory 2. Must be a valid record in the table CURRENCY. |
| 8 | `IS.CON.DEAL.DATE` | `IsContract_DealDate` | TField |  | The Deal date of the contract specifies the actual date the Customer requests for the asset and the details being captured in the screen. The current date of the system(TODAY) is defaulted in this field. Validation Rules: 1. Field No-input. 2. Standard T24 Date Field. 3. Current date (TODAY) is defaulted. |
| 9 | `IS.CON.VALUE.DATE` | `IsContract_ValueDate` | TField |  | Value date of the Contract. Validation Rules: 1. Defaulted to TODAY. 2. Cannot be future dated. 3. Standard T24 Date field. |
| 10 | `IS.CON.COMMODITY` | `IsContract_Commodity` |  |  |  |
| 11 | `IS.CON.ASSET.REF` | `IsContract_AssetRef` |  |  |  |
| 12 | `IS.CON.VENDOR` | `IsContract_Vendor` |  |  |  |
| 13 | `IS.CON.VENDOR.NAME` | `IsContract_VendorName` |  |  |  |
| 14 | `IS.CON.BUY.BROKER` | `IsContract_BuyBroker` |  |  |  |
| 15 | `IS.CON.BUY.BROKER.ACCT` | `IsContract_BuyBrokerAcct` |  |  |  |
| 16 | `IS.CON.BUY.BR.WASH.ACCT` | `IsContract_BuyBrWashAcct` |  |  |  |
| 17 | `IS.CON.SELL.BROKER` | `IsContract_SellBroker` |  |  |  |
| 18 | `IS.CON.SELL.BROKER.ACCT` | `IsContract_SellBrokerAcct` |  |  |  |
| 19 | `IS.CON.SELL.BR.WASH.ACCT` | `IsContract_SellBrWashAcct` |  |  |  |
| 20 | `IS.CON.UNITS` | `IsContract_Units` |  |  |  |
| 21 | `IS.CON.UNIT.PRICE` | `IsContract_UnitPrice` |  |  |  |
| 22 | `IS.CON.QUANTITY` | `IsContract_Quantity` |  |  |  |
| 23 | `IS.CON.PURCHASE.PRICE` | `IsContract_PurchasePrice` |  |  |  |
| 24 | `IS.CON.RETURN.QUANTITY` | `IsContract_ReturnQuantity` |  |  |  |
| 25 | `IS.CON.RETURN.UNIT.PRICE` | `IsContract_ReturnUnitPrice` |  |  |  |
| 26 | `IS.CON.RETURN.TOTAL.SOLD.PRICE` | `IsContract_ReturnTotalSoldPrice` |  |  |  |
| 27 | `IS.CON.RETURN.SOLD.PROFIT` | `IsContract_ReturnSoldProfit` |  |  |  |
| 28 | `IS.CON.RETURN.SOLD.LOSS` | `IsContract_ReturnSoldLoss` |  |  |  |
| 29 | `IS.CON.TOT.PURCHASE.PRICE` | `IsContract_TotPurchasePrice` | TField |  | The Total Price of the contract (Sum of the purchase amounts of all Commodities/Assets) Validation Rules: 1. Field No-input. 2. System updates the field value as sum of all the purchase price. |
| 30 | `IS.CON.NO.OF.UNITS` | `IsContract_NoOfUnits` | TField |  | The number of units that the Finance Amount is comprised of. This is a user given value to represents the units of the Finance amount. Validation Rules: 1. Any numeric value. 2. When value is given in this field, only one asset or commodity can be transacted. |
| 31 | `IS.CON.UNIT.VALUE` | `IsContract_UnitValue` | TField |  | The unit value of the Asset or Commodity defined. System defaults the value by dividing the Finance Amount with NO.OF.UNITS. Finance Amount is calculated as Sum of Total Purchase Price and Cost(Type Finance) exclusive of Down Payment. Validation Rules: 1. Field No-input. |
| 32 | `IS.CON.CUSTOMER.ACCT` | `IsContract_CustomerAcct` | TField |  | The Customer account recorded in the Purchase contract. Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Account must belong to the Contract Customer. 3. NOSTRO or VOSTRO account not allowed. |
| 33 | `IS.CON.VENDOR.WASH.ACCT` | `IsContract_VendorWashAcct` | TField |  | The account that is used to act as Wash account for Vendor Payment. This Account is credited during Purchase and the Vendor Payments are disbursed from this account. The account formed is of the format &lt;ContractCurrency&gt;&lt;MultiSupplierCategory&gt;&lt;ProductCode&gt;&lt;SubDivisionCode&gt; Validation Rules: 1. Field No-input. 2. Defaulted with the account formed from the Multi Supplier Category of the Parameter record |
| 34 | `IS.CON.WAKALA.REF` | `IsContract_WakalaRef` | TField |  | The AA Arrangement Contract reference which acts as a Wakala contract. This is keyed in case of linked products like WAKALA-MUSAWAMA. Validation Rules: 1. Valid record in the table AA.ARRANGEMENT. |
| 35 | `IS.CON.DP.COMMODITY` | `IsContract_DpCommodity` |  |  |  |
| 36 | `IS.CON.DP.ASSET.REF` | `IsContract_DpAssetRef` |  |  |  |
| 37 | `IS.CON.DP.TYPE` | `IsContract_DpType` |  |  |  |
| 38 | `IS.CON.DP.VALUE` | `IsContract_DpValue` |  |  |  |
| 39 | `IS.CON.DP.PERCENT` | `IsContract_DpPercent` |  |  |  |
| 40 | `IS.CON.DP.CUST.CONTRIB` | `IsContract_DpCustContrib` |  |  |  |
| 41 | `IS.CON.DP.BANK.CONTRIB` | `IsContract_DpBankContrib` |  |  |  |
| 42 | `IS.CON.DP.CONTRIB.TYPE` | `IsContract_DpContribType` |  |  |  |
| 43 | `IS.CON.DP.CONTRIB.PAYTO` | `IsContract_DpContribPayto` |  |  |  |
| 44 | `IS.CON.DP.CONTRIB.AMT` | `IsContract_DpContribAmt` |  |  |  |
| 45 | `IS.CON.DP.CASH.CONTRIB` | `IsContract_DpCashContrib` |  |  |  |
| 46 | `IS.CON.DP.ACCOUNT` | `IsContract_DpAccount` |  |  |  |
| 47 | `IS.CON.DP.REC.AMOUNT` | `IsContract_DpRecAmount` |  |  |  |
| 48 | `IS.CON.RESERVED.33` | `IsContract_Reserved33` |  |  |  |
| 49 | `IS.CON.RESERVED.32` | `IsContract_Reserved32` |  |  |  |
| 50 | `IS.CON.RESERVED.31` | `IsContract_Reserved31` |  |  |  |
| 51 | `IS.CON.TOTAL.DP.AMT` | `IsContract_TotalDpAmt` | TField |  | The Total Down Payment amount of the Contract Validation Rules: 1. Field No-input. 2. System updates the field value as sum of all the down payment specified. |
| 52 | `IS.CON.TOTAL.DP.CASH` | `IsContract_TotalDpCash` | TField |  | The Total Down Payment amount contributed in terms of DP.CONTRIB.PAYTO as 'Bank' and DP.CONTRIB.TYPE as 'Cash'. Validation Rules: 1. Field No-input. |
| 53 | `IS.CON.GUARANTOR` | `IsContract_Guarantor` | TField |  | The Customer who will act as Guarantor for the contract. Validation Rules: 1. Must be a valid record from the table CUSTOMER. |
| 54 | `IS.CON.COST.TYPE` | `IsContract_CostType` |  |  |  |
| 55 | `IS.CON.COST.PAY.TYPE` | `IsContract_CostPayType` |  |  |  |
| 56 | `IS.CON.COST.AMT` | `IsContract_CostAmt` |  |  |  |
| 57 | `IS.CON.COST.DR.ACCT` | `IsContract_CostDrAcct` |  |  |  |
| 58 | `IS.CON.COST.CR.ACCT` | `IsContract_CostCrAcct` |  |  |  |
| 59 | `IS.CON.COST.DESC` | `IsContract_CostDesc` |  |  |  |
| 60 | `IS.CON.RESERVED.30` | `IsContract_Reserved30` |  |  |  |
| 61 | `IS.CON.RESERVED.29` | `IsContract_Reserved29` |  |  |  |
| 62 | `IS.CON.RESERVED.28` | `IsContract_Reserved28` |  |  |  |
| 63 | `IS.CON.RESERVED.27` | `IsContract_Reserved27` |  |  |  |
| 64 | `IS.CON.RESERVED.26` | `IsContract_Reserved26` |  |  |  |
| 65 | `IS.CON.MMIA.REF` | `IsContract_MmiaRef` | TField |  | The MMIA Agreement reference of the Purchase contract. |
| 66 | `IS.CON.ACTION.CODE` | `IsContract_ActionCode` |  |  |  |
| 67 | `IS.CON.ACTION.COMPLETED` | `IsContract_ActionCompleted` |  |  |  |
| 68 | `IS.CON.ACTION.SUCCESS` | `IsContract_ActionSuccess` |  |  |  |
| 69 | `IS.CON.NOTES` | `IsContract_Notes` | TField |  | Captures additional information about the contract Validation Rules: 1. Standard T24 Alphanumeric field. |
| 70 | `IS.CON.RESALE.CUSTOMER.ID` | `IsContract_ResaleCustomerId` | TField |  | This field is used to capture the Seller Customer details. Validation Rules: 1. It should display the List of records from CUSTOMER application. 2. It is used to capture the Seller customer number. |
| 71 | `IS.CON.RESALE.CUSTOMER.NAME` | `IsContract_ResaleCustomerName` | TField |  | This field displays the Seller Customer name of the Customer Id given in the field RESALE.CUSTOMER.ID. |
| 72 | `IS.CON.RESALE.SETTLE.ACCT` | `IsContract_ResaleSettleAcct` | TField |  | The price at which the repossessed asset is sold again. Validation Rules: 1. No-input field currently. Will be opened for user-input in future. |
| 73 | `IS.CON.RESERVED.41` | `IsContract_Reserved41` | TField |  |  |
| 74 | `IS.CON.RESERVED.40` | `IsContract_Reserved40` | TField |  |  |
| 75 | `IS.CON.RESERVED.39` | `IsContract_Reserved39` | TField |  |  |
| 76 | `IS.CON.RESERVED.38` | `IsContract_Reserved38` | TField |  |  |
| 77 | `IS.CON.RESERVED.37` | `IsContract_Reserved37` | TField |  |  |
| 78 | `IS.CON.RESERVED.36` | `IsContract_Reserved36` | TField |  |  |
| 79 | `IS.CON.RESERVED.35` | `IsContract_Reserved35` | TField |  |  |
| 80 | `IS.CON.RESERVED.34` | `IsContract_Reserved34` | TField |  |  |
| 81 | `IS.CON.REPOS.AMOUNT` | `IsContract_ReposAmount` | TField |  | Specifies the Amount received during Repossession of an asset. Validation Rules: 1. No-input field currently. Will be opened for user-input in future. |
| 82 | `IS.CON.REPOS.PUR.REF` | `IsContract_ReposPurRef` | TField |  | The reference captured during repurchase of the repossessed asset. Validation Rules: 1. No-input field currently. Will be opened for user-input in future. |
| 83 | `IS.CON.REPURCHASE` | `IsContract_Repurchase` | TField |  | Specifies if the contract is repurchased after repossession. Validation Rules: 1. No-input field currently. Will be opened for user-input in future. |
| 84 | `IS.CON.RESALE` | `IsContract_Resale` | TField |  | Specifies if the contract is resold after repossession Validation Rules: 1. No-input field currently. Will be opened for user-input in future. |
| 85 | `IS.CON.DELIVERY.DATE` | `IsContract_DeliveryDate` | TField |  | The Delivery Date of the asset. Validation Rules: 1. Standard T24 Date Field. 2. Functionality yet to be developed for delivery of Assets. |
| 86 | `IS.CON.SIMULATION.REF` | `IsContract_SimulationRef` | TField |  | The AA simulation reference which can be linked to the Purchase contract. User can simulate the finance and the repayment schedules using the AA simulation and the same can be linked here during purchase. Validation Rules: 1. Must be a valid record from the table "AA.SIMULATION.CAPTURE". 2. The Total Purchase amount should not exceed the Simulation Amount. |
| 87 | `IS.CON.SALE.REFERENCE` | `IsContract_SaleReference` | TField |  | The AA arrangement reference is captured in this field when the contract is financed. Validation Rules: 1. Field No-input. |
| 88 | `IS.CON.NEXT.STATUS` | `IsContract_NextStatus` | TField |  | Defines the expected Next Status of the Contract which is defined in the IS.PARAMETER workflow. Validation Rules: 1. The values to the field are defined in the EB.LOOKUP table with prefix "IS.WF.STATUS*". 2. Field No-input. 3. Defaulted by the system based on the value in the field STATUS. |
| 89 | `IS.CON.PREV.STATUS` | `IsContract_PrevStatus` |  |  |  |
| 90 | `IS.CON.PREV.STATUS.DATE` | `IsContract_PrevStatusDate` |  |  |  |
| 91 | `IS.CON.PREV.STATUS.NOTES` | `IsContract_PrevStatusNotes` |  |  |  |
| 92 | `IS.CON.PREV.ACCOUNTING` | `IsContract_PrevAccounting` |  |  |  |
| 93 | `IS.CON.RESERVED.25` | `IsContract_Reserved25` |  |  |  |
| 94 | `IS.CON.RESERVED.24` | `IsContract_Reserved24` |  |  |  |
| 95 | `IS.CON.RESERVED.23` | `IsContract_Reserved23` |  |  |  |
| 96 | `IS.CON.RESERVED.22` | `IsContract_Reserved22` |  |  |  |
| 97 | `IS.CON.RESERVED.21` | `IsContract_Reserved21` |  |  |  |
| 98 | `IS.CON.REQUEST.AMOUNT` | `IsContract_RequestAmount` | TField |  | The Finance amount requested by the customer. Validation Rules: 1. Must be a Numeric Field with Decimals. |
| 99 | `IS.CON.LIMIT.VALUE.DATE` | `IsContract_LimitValueDate` | TField |  | This field is defaulted with TODAY during PURCHASE stage. Validation Rules: 1. NOINPUT field. 1. Valid T24 date. |
| 100 | `IS.CON.BR.CHRG.CODE` | `IsContract_BrChrgCode` | TField |  | Contains the commission type to be used for calculation broker fee Validation Rules: 1. Must be a valid record in FT.COMMISSION.TYPE 2. Defaulted from the IS.BROKER record of the buy broker |
| 101 | `IS.CON.BR.FEE.CCY` | `IsContract_BrFeeCcy` | TField |  | The currency to be used for calculation of broker fee Validation Rules: Defaulted from the IS.BROKER record of the buy broker |
| 102 | `IS.CON.BR.CHRG.AMT` | `IsContract_BrChrgAmt` | TField |  | The Broker Fee Amount charged for the contract Broker fee amount should be calculated on TOT.PURCHASE.PRICE as base amount. Validation Rules: 1. Numeric field 2. Will be defaulted based on the Br charge code |
| 103 | `IS.CON.BR.FEE.DR.TYPE` | `IsContract_BrFeeDrType` | TField |  | Describes what type of account is to be used for the broker fee debit account Validation Rules: Allowed values are Customer Account,Expenses PL Category,Purchase Account |
| 104 | `IS.CON.BR.FEE.DR.ACCT` | `IsContract_BrFeeDrAcct` | TField | Yes | This field is used to input the account from which the broker fee amount to be debited. Mandatory if BR.FEE.DR.TYPE is chosen. Validation Rules: It should be a valid record in ACCOUNT application in active status. |
| 105 | `IS.CON.BR.FEE.CR.ACCT` | `IsContract_BrFeeCrAcct` | TField | Yes | This field is used to input the account to which the broker fee amount to be credited. Mandatory if BR.FEE.DR.TYPE is chosen. Validation Rules: It should be a valid record in ACCOUNT application in active status. |
| 106 | `IS.CON.BR.FEE.BROKER.SHARE` | `IsContract_BrFeeBrokerShare` | TField |  | Broker share of the Broker fee amount is calculated and defaulted in this field Validation Rules: Based on the broker share percentage defined in the IS.BROKER record of the buy broker the broker share is calculated |
| 107 | `IS.CON.BR.FEE.BANK.SHARE` | `IsContract_BrFeeBankShare` | TField |  | Bank share of the broker fee amount is calculated and defaulted Validation Rules: Based on the broker share percentage defined in the IS.BROKER record of the buy broker, the bank share percentage and bank share is calculated |
| 108 | `IS.CON.BR.FEE.BS.ACCTG` | `IsContract_BrFeeBsAcctg` | TField |  | If this field is set as YES then it should raise additional accounting entries for Bank share of Broker fees along with Broker fees entries |
| 109 | `IS.CON.BR.FEE.BS.CR.ACCT` | `IsContract_BrFeeBsCrAcct` | TField |  | The account that will be used to credit bank share amount Validation Rules: Defaults the PL Category/ Account number from FT.COMMISSION TYPE, CATEGORY.ACCOUNT field |
| 110 | `IS.CON.BR.FEE.TAX.BASE.AMT` | `IsContract_BrFeeTaxBaseAmt` | TField |  | The tax base amount for calcuating the tax amount Validation Rules: 1. Will be in the broker fee currency 2. Based upon IS.BROKER&gt;BR.FEE.TAX.BASE.AMT , it will update as either bank share amount , broker share amount or bank share+broker share amount |
| 111 | `IS.CON.BR.FEE.TAX.AMT` | `IsContract_BrFeeTaxAmt` | TField |  | The calculated tax amount for this contract Validation Rules: Tax amount will be calcualted by using tax base amount as the base value |
| 112 | `IS.CON.BR.FEE.BR.SHARE.PAID` | `IsContract_BrFeeBrSharePaid` | TField |  | Field will be marked as YES when the broker share is paid |
| 113 | `IS.CON.BR.CHRG.AMT.FCY` | `IsContract_BrChrgAmtFcy` | TField |  | The Broker Fee Amount charged for the contract calculated in foreign currency if broker fee currency is in a different currency to the contract currency Broker fee amount should be calculated on TOT.PURCHASE.PRICE as base amount. Validation Rules: |
| 114 | `IS.CON.BR.FEE.TAX.AMT.FCY` | `IsContract_BrFeeTaxAmtFcy` | TField |  | The tax amount for this contract calculated in foreign currency when broker fee currency is different to contract currency Validation Rules: |
| 115 | `IS.CON.RESERVED.3` | `IsContract_Reserved3` | TField |  |  |
| 116 | `IS.CON.RESERVED.2` | `IsContract_Reserved2` | TField |  |  |
| 117 | `IS.CON.RESERVED.1` | `IsContract_Reserved1` | TField |  |  |
| 118 | `IS.CON.LOCAL.REF` | `IsContract_LocalRef` |  |  |  |
| 119 | `IS.CON.STMT.NOS` | `IsContract_StmtNos` |  |  |  |
| 120 | `IS.CON.OVERRIDE` | `IsContract_Override` |  |  |  |
| 121 | `IS.CON.RECORD.STATUS` | `IsContract_RecordStatus` | String |  |  |
| 122 | `IS.CON.CURR.NO` | `IsContract_CurrNo` | String |  |  |
| 123 | `IS.CON.INPUTTER` | `IsContract_Inputter` |  |  |  |
| 124 | `IS.CON.DATE.TIME` | `IsContract_DateTime` |  |  |  |
| 125 | `IS.CON.AUTHORISER` | `IsContract_Authoriser` | String |  |  |
| 126 | `IS.CON.CO.CODE` | `IsContract_CoCode` | String |  |  |
| 127 | `IS.CON.DEPT.CODE` | `IsContract_DeptCode` | String |  |  |
| 128 | `IS.CON.AUDITOR.CODE` | `IsContract_AuditorCode` | String |  |  |
| 129 | `IS.CON.AUDIT.DATE.TIME` | `IsContract_AuditDateTime` | String |  |  |
| 130 | `IS.CON.CUSTOMER.POSSESSION` | `IsContract_CustomerPossession` |  |  |  |
| 131 | `IS.CON.REBATE.ALLWD` | `IsContract_RebateAllwd` | TField |  | If check box is set then Rebate functionality needs to be invoked. Rebate details from Vendor application will be populated and Rebate amount is calculated. Validation Rules: 1. Valid values are YES or NULL. |
| 132 | `IS.CON.REBATE.ACTION` | `IsContract_RebateAction` |  |  |  |
| 133 | `IS.CON.REBATE.TYPE` | `IsContract_RebateType` |  |  |  |
| 134 | `IS.CON.REBATE.VALUE` | `IsContract_RebateValue` |  |  |  |
| 135 | `IS.CON.REBATE.AMT` | `IsContract_RebateAmt` |  |  |  |
| 136 | `IS.CON.REBATE.CUST.SHARE` | `IsContract_RebateCustShare` |  |  |  |
| 137 | `IS.CON.REBATE.BANK.SHARE` | `IsContract_RebateBankShare` |  |  |  |
