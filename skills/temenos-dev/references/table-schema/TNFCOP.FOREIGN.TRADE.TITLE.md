# TNFCOP.FOREIGN.TRADE.TITLE — Table Schema

> Source: `INSERTS/I_F.TNFCOP.FOREIGN.TRADE.TITLE` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRADE.TITLE.TITLE.CODE` | `TnfcopForeignTradeTitle_TitleCode` | TField |  | This is the code which represents what type of foreign trade title.The possible values are 31,21,33,22,39. |
| 2 | `TRADE.TITLE.DOMICILIATION.DATE` | `TnfcopForeignTradeTitle_DomiciliationDate` | TField |  | This field is to store the date on which the foreign trade title is domiciled in T24. |
| 3 | `TRADE.TITLE.TITLE.DOMICILIATION.NO` | `TnfcopForeignTradeTitle_TitleDomiciliationNo` | TField |  |  |
| 4 | `TRADE.TITLE.EXP.CLEARANCE.DATE` | `TnfcopForeignTradeTitle_ExpClearanceDate` | TField |  | This field denotes the Expiry date for the clearance of the foreign trade title.This date is used for reporting the trade title to the Central Bank |
| 5 | `TRADE.TITLE.BANK.CODE` | `TnfcopForeignTradeTitle_BankCode` | TField |  | This field is to store the Bank code of the bank in which the foreign trade title is domiciled |
| 6 | `TRADE.TITLE.BANK.NAME` | `TnfcopForeignTradeTitle_BankName` | TField |  | This field is to store the bank name in which the foreign trade title is domiciled |
| 7 | `TRADE.TITLE.DEPOSIT.REFERENCE` | `TnfcopForeignTradeTitle_DepositReference` | TField |  | This field is to store the document reference number.When prohibited goods are traded, the document has to be submitted to minitry of trade and Central Bankand that reference should be updated for domiciliation |
| 8 | `TRADE.TITLE.DEPOSIT.DATE` | `TnfcopForeignTradeTitle_DepositDate` | TField |  | This field is to store the date on which the document is deposited for the prohibited goods trade |
| 9 | `TRADE.TITLE.VISA.NUMBER` | `TnfcopForeignTradeTitle_VisaNumber` | TField |  | This field is to store the Agreement reference provided by the ministry of trade for the prohibited goods |
| 10 | `TRADE.TITLE.VISA.DATE` | `TnfcopForeignTradeTitle_VisaDate` | TField |  | This field is to store the date on which the agreement number is provided by Ministry |
| 11 | `TRADE.TITLE.EXPIRY.DATE` | `TnfcopForeignTradeTitle_ExpiryDate` | TField |  | This field is to store the date on which the title is getting expired.Each type of title has different validity. |
| 12 | `TRADE.TITLE.APPROVAL.NUMBER` | `TnfcopForeignTradeTitle_ApprovalNumber` | TField |  | This field denotes the approval number received from government organisations for execution of the trade |
| 13 | `TRADE.TITLE.APPROVAL.DATE` | `TnfcopForeignTradeTitle_ApprovalDate` | TField |  | This field is to store the date on which the approval is received from the government |
| 14 | `TRADE.TITLE.CUST.ACCT.NUMBER` | `TnfcopForeignTradeTitle_CustAcctNumber` | TField |  | This field is to store the account number of the customer for whom the trade title is raised.This should be a valid T24 account. |
| 15 | `TRADE.TITLE.LEGAL.ID` | `TnfcopForeignTradeTitle_LegalId` | TField |  | This field is to store the Legal ID of the customer, to identify the customer by central banks |
| 16 | `TRADE.TITLE.CUSTOMER.NAME` | `TnfcopForeignTradeTitle_CustomerName` | TField |  | This field is to store the name of the customer for whom the trade title is raised |
| 17 | `TRADE.TITLE.FIRST.DESTN.COUNTRY` | `TnfcopForeignTradeTitle_FirstDestnCountry` | TField |  | This field denotes the country code to which the good will reach first from the origination country |
| 18 | `TRADE.TITLE.FINAL.DESTN.COUNTRY` | `TnfcopForeignTradeTitle_FinalDestnCountry` | TField |  | This field denotes the country code which is the final destination for the goods (Importer country) |
| 19 | `TRADE.TITLE.ORIGIN.COUNTRY` | `TnfcopForeignTradeTitle_OriginCountry` | TField |  | This field denotes the country code from where the goods are originated |
| 20 | `TRADE.TITLE.SETTLEMENT.MODE` | `TnfcopForeignTradeTitle_SettlementMode` | TField |  | This field denotes the code of the settlement mode for the trade title.Each settlement mode has different code. |
| 21 | `TRADE.TITLE.SETTLEMENT.PERIOD` | `TnfcopForeignTradeTitle_SettlementPeriod` | TField |  | This field denotes the code of the settlement period for the trade title, each settlement period has different code. |
| 22 | `TRADE.TITLE.DELIVERY.TERMS` | `TnfcopForeignTradeTitle_DeliveryTerms` | TField |  | This field denotes the code of the delivery terms for the trade title. There are different delivery terms and having different code |
| 23 | `TRADE.TITLE.CONTRACT.REFERENCE` | `TnfcopForeignTradeTitle_ContractReference` | TField |  | This field denotes the reference number of the document which is used for creating the trade title |
| 24 | `TRADE.TITLE.CONTRACT.DATE` | `TnfcopForeignTradeTitle_ContractDate` | TField |  | This field is to store the date on which the contract or proforma invoice is created |
| 25 | `TRADE.TITLE.SETTLEMENT.CCY` | `TnfcopForeignTradeTitle_SettlementCcy` | TField |  | The currency code on which the settlement of the trade happens |
| 26 | `TRADE.TITLE.INVOICE.CURRENCY` | `TnfcopForeignTradeTitle_InvoiceCurrency` | TField |  | The currency code on which the invoice is created |
| 27 | `TRADE.TITLE.CUSTOMS.REGIME.CODE` | `TnfcopForeignTradeTitle_CustomsRegimeCode` | TField |  | This field denoted the regime code of the customs where the goods are imputed |
| 28 | `TRADE.TITLE.JOINT.REFERENCE` | `TnfcopForeignTradeTitle_JointReference` | TField |  | The joined reference code will be updated in this field if there is multiple documents involved for this title |
| 29 | `TRADE.TITLE.BENEFICIARY.NAME` | `TnfcopForeignTradeTitle_BeneficiaryName` | TField |  | This field denotes the name of the beneficiary for this title |
| 30 | `TRADE.TITLE.FCY.FOB.AMOUNT` | `TnfcopForeignTradeTitle_FcyFobAmount` | TField |  | this field used to update Free on board amount for the trade title in foreign currency |
| 31 | `TRADE.TITLE.LCY.FOB.AMOUNT` | `TnfcopForeignTradeTitle_LcyFobAmount` | TField |  | This field used to update the free on board amount for the trade title in local currency |
| 32 | `TRADE.TITLE.ALLOC.AMT.FCY` | `TnfcopForeignTradeTitle_AllocAmtFcy` | TField |  | The amount for which the title is created in foreign currency |
| 33 | `TRADE.TITLE.ALLOC.AMT.LCY` | `TnfcopForeignTradeTitle_AllocAmtLcy` | TField |  | The title amount in local currency |
| 34 | `TRADE.TITLE.IMPUTED.AMT.LCY` | `TnfcopForeignTradeTitle_ImputedAmtLcy` | TField |  | The amount in local currency for which the goods imputed by the customs in destination country |
| 35 | `TRADE.TITLE.IMPUTED.AMT.FCY` | `TnfcopForeignTradeTitle_ImputedAmtFcy` | TField |  | The amount in foreign currency for which the goods imputed by the customs in destination country |
| 36 | `TRADE.TITLE.TITLE.STATUS` | `TnfcopForeignTradeTitle_TitleStatus` | TField |  | The field is updated with the status of the title. The allowed status are "CANCELLED", "NOT-CLEARED" AND "CLEARED" |
| 37 | `TRADE.TITLE.DOMICILIATION.YEAR` | `TnfcopForeignTradeTitle_DomiciliationYear` | TField |  | The year on which the title is domiciled in the bank |
| 38 | `TRADE.TITLE.DEPOSIT.YEAR` | `TnfcopForeignTradeTitle_DepositYear` | TField |  | The year on which the goods are imputed by the customs |
| 39 | `TRADE.TITLE.SEQUENCE.NUMBER` | `TnfcopForeignTradeTitle_SequenceNumber` |  |  |  |
| 40 | `TRADE.TITLE.NGP.CODE` | `TnfcopForeignTradeTitle_NgpCode` |  |  |  |
| 41 | `TRADE.TITLE.NGP.DESCRIPTION` | `TnfcopForeignTradeTitle_NgpDescription` |  |  |  |
| 42 | `TRADE.TITLE.NGP.ALLOCATED.AMT` | `TnfcopForeignTradeTitle_NgpAllocatedAmt` |  |  |  |
| 43 | `TRADE.TITLE.NGP.CCY` | `TnfcopForeignTradeTitle_NgpCcy` |  |  |  |
| 44 | `TRADE.TITLE.NGP.ALLOC.QUANTITY` | `TnfcopForeignTradeTitle_NgpAllocQuantity` |  |  |  |
| 45 | `TRADE.TITLE.NGP.ALLOC.QUANTITY.CODE` | `TnfcopForeignTradeTitle_NgpAllocQuantityCode` |  |  |  |
| 46 | `TRADE.TITLE.NGP.COUNTRY.CODE` | `TnfcopForeignTradeTitle_NgpCountryCode` |  |  |  |
| 47 | `TRADE.TITLE.NGP.IMP.QUANTITY` | `TnfcopForeignTradeTitle_NgpImpQuantity` |  |  |  |
| 48 | `TRADE.TITLE.DECLARATION.NUMBER` | `TnfcopForeignTradeTitle_DeclarationNumber` |  |  |  |
| 49 | `TRADE.TITLE.DECLARATION.DATE` | `TnfcopForeignTradeTitle_DeclarationDate` |  |  |  |
| 50 | `TRADE.TITLE.NGP.IMPUTED.AMOUNT` | `TnfcopForeignTradeTitle_NgpImputedAmount` |  |  |  |
| 51 | `TRADE.TITLE.IMPUTATION.CCY` | `TnfcopForeignTradeTitle_ImputationCcy` |  |  |  |
| 52 | `TRADE.TITLE.FOB.IMPUTED.AMT.FCY` | `TnfcopForeignTradeTitle_FobImputedAmtFcy` |  |  |  |
| 53 | `TRADE.TITLE.FOB.IMPUTED.AMT.LCY` | `TnfcopForeignTradeTitle_FobImputedAmtLcy` |  |  |  |
| 54 | `TRADE.TITLE.AUTO.IMP.IND` | `TnfcopForeignTradeTitle_AutoImpInd` |  |  |  |
| 55 | `TRADE.TITLE.EXCHANGE.RATE` | `TnfcopForeignTradeTitle_ExchangeRate` |  |  |  |
| 56 | `TRADE.TITLE.NGP.TOTAL.AMOUNT.IMPUTED` | `TnfcopForeignTradeTitle_NgpTotalAmountImputed` |  |  |  |
| 57 | `TRADE.TITLE.SUM.OF.NGP.AMT` | `TnfcopForeignTradeTitle_SumOfNgpAmt` | TField |  | The total sum amount of imputation |
| 58 | `TRADE.TITLE.CANCELLATION.DATE` | `TnfcopForeignTradeTitle_CancellationDate` | TField |  | Date on which the trade title is cancelled |
| 59 | `TRADE.TITLE.REASON.CANCELLATION` | `TnfcopForeignTradeTitle_ReasonCancellation` | TField |  | Reason for which the trade is cancelled. It is free text field for the user to input |
| 60 | `TRADE.TITLE.TRADE.TITLE.OPR` | `TnfcopForeignTradeTitle_TradeTitleOpr` | TField |  | This field is used to store trade title operations like Domicilation, Custom imputation to define the charges |
| 61 | `TRADE.TITLE.CHARGE.TYPE` | `TnfcopForeignTradeTitle_ChargeType` |  |  |  |
| 62 | `TRADE.TITLE.CHARGE.AMT` | `TnfcopForeignTradeTitle_ChargeAmt` |  |  |  |
| 63 | `TRADE.TITLE.TAX.AMT` | `TnfcopForeignTradeTitle_TaxAmt` |  |  |  |
| 64 | `TRADE.TITLE.CHARGE.ACCOUNT` | `TnfcopForeignTradeTitle_ChargeAccount` | TField |  | This field is to store the account from where the charge amount should be debited. |
| 65 | `TRADE.TITLE.REPORTING.STATUS` | `TnfcopForeignTradeTitle_ReportingStatus` | TField |  | This field denotes the rejected status of the trade title. |
| 66 | `TRADE.TITLE.IMPUTATION.DATE` | `TnfcopForeignTradeTitle_ImputationDate` | TField |  | This is the date on which the goods are imputed |
| 67 | `TRADE.TITLE.TRANSACTION.REF` | `TnfcopForeignTradeTitle_TransactionRef` |  |  |  |
| 68 | `TRADE.TITLE.AUTO.RESERVE.IND` | `TnfcopForeignTradeTitle_AutoReserveInd` |  |  |  |
| 69 | `TRADE.TITLE.RESERVED.AMT` | `TnfcopForeignTradeTitle_ReservedAmt` |  |  |  |
| 70 | `TRADE.TITLE.RESERVATION.DATE` | `TnfcopForeignTradeTitle_ReservationDate` |  |  |  |
| 71 | `TRADE.TITLE.RELEASE.AMT` | `TnfcopForeignTradeTitle_ReleaseAmt` |  |  |  |
| 72 | `TRADE.TITLE.RELEASE.RES.DATE` | `TnfcopForeignTradeTitle_ReleaseResDate` |  |  |  |
| 73 | `TRADE.TITLE.SETT.TRANS.REF` | `TnfcopForeignTradeTitle_SettTransRef` |  |  |  |
| 74 | `TRADE.TITLE.AUTO.SETT.IND` | `TnfcopForeignTradeTitle_AutoSettInd` |  |  |  |
| 75 | `TRADE.TITLE.SETTLEMENT.AMT` | `TnfcopForeignTradeTitle_SettlementAmt` |  |  |  |
| 76 | `TRADE.TITLE.SETT.TRANS.CCY` | `TnfcopForeignTradeTitle_SettTransCcy` |  |  |  |
| 77 | `TRADE.TITLE.SETTLEMENT.DATE` | `TnfcopForeignTradeTitle_SettlementDate` |  |  |  |
| 78 | `TRADE.TITLE.EXTRACTION.DATE` | `TnfcopForeignTradeTitle_ExtractionDate` | TField |  | Date when file is extracted from T24 |
| 79 | `TRADE.TITLE.LOCAL.REF` | `TnfcopForeignTradeTitle_LocalRef` |  |  |  |
| 80 | `TRADE.TITLE.OVERRIDE` | `TnfcopForeignTradeTitle_Override` |  |  |  |
| 81 | `TRADE.TITLE.RECORD.STATUS` | `TnfcopForeignTradeTitle_RecordStatus` | String |  |  |
| 82 | `TRADE.TITLE.CURR.NO` | `TnfcopForeignTradeTitle_CurrNo` | String |  |  |
| 83 | `TRADE.TITLE.INPUTTER` | `TnfcopForeignTradeTitle_Inputter` |  |  |  |
| 84 | `TRADE.TITLE.DATE.TIME` | `TnfcopForeignTradeTitle_DateTime` |  |  |  |
| 85 | `TRADE.TITLE.AUTHORISER` | `TnfcopForeignTradeTitle_Authoriser` | String |  |  |
| 86 | `TRADE.TITLE.CO.CODE` | `TnfcopForeignTradeTitle_CoCode` | String |  |  |
| 87 | `TRADE.TITLE.DEPT.CODE` | `TnfcopForeignTradeTitle_DeptCode` | String |  |  |
| 88 | `TRADE.TITLE.AUDITOR.CODE` | `TnfcopForeignTradeTitle_AuditorCode` | String |  |  |
| 89 | `TRADE.TITLE.AUDIT.DATE.TIME` | `TnfcopForeignTradeTitle_AuditDateTime` | String |  |  |
| 90 | `TRADE.TITLE.TRF.ELIGIBLE` | `TnfcopForeignTradeTitle_TrfEligible` | TField |  | This field stores Yes or NO value. A value of YES indicates that the indicated title code is eligible for transfer.Its a neighbour field. |
| 91 | `TRADE.TITLE.RESERVE.REF` | `TnfcopForeignTradeTitle_ReserveRef` |  |  |  |
| 92 | `TRADE.TITLE.TITLE.AVA.NUMBER` | `TnfcopForeignTradeTitle_TitleAvaNumber` |  |  |  |
| 93 | `TRADE.TITLE.COUNTRY.OF.BOP` | `TnfcopForeignTradeTitle_CountryOfBop` |  |  |  |
| 94 | `TRADE.TITLE.ORIGIN.OF.FUNDS` | `TnfcopForeignTradeTitle_OriginOfFunds` |  |  |  |
| 95 | `TRADE.TITLE.LINKED.AVA` | `TnfcopForeignTradeTitle_LinkedAva` |  |  |  |
