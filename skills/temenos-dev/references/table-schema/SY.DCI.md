# SY.DCI — Table Schema

> Source: `INSERTS/I_F.SY.DCI` in `DI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.DCI.DESCRIPTION` | `SyDci_Description` |  |  |  |
| 2 | `SY.DCI.CONTRACT.STATUS` | `SyDci_ContractStatus` | TField |  | On contract input, gets updated as ACTIVE. On maturity gets updated as 'MATURED'. Validation Rules: NOINPUT field |
| 3 | `SY.DCI.VARIANT` | `SyDci_Variant` | TField |  | Variant for the contract to use the said categories based on the SY.PRODUCT.VARIANT selected. Validation Rules: Valid SY.PRODUCT.VARIANT record. |
| 4 | `SY.DCI.TRADE.DATE` | `SyDci_TradeDate` | TField |  | Trade date of the contract which is what is mapped to the TRADE.DATE of DX.TRADE and DEAL.DATE of MM.MONEY.MARKET |
| 5 | `SY.DCI.VALUE.DATE` | `SyDci_ValueDate` | TField |  | Value date of the contract from which it is active. This is the date that gets mapped to VALUE.DATE of DX.TRADEand MM.MONEY.MARKET. The premium, fee entries of the contract gets posted on value date |
| 6 | `SY.DCI.MATURITY.DATE` | `SyDci_MaturityDate` | TField |  | The date on which the underlying DX.TRADE and MM.MONEY.MARKET gets matured. This date gets mapped to the DEC.DATEof DX.TRADE and MATURITY.DATE of MM.MONEY.MARKET. |
| 7 | `SY.DCI.FIXING.DATE` | `SyDci_FixingDate` | TField |  | The date on which the fixing event happens i.e the decision is made whether to exercise or expire the contract. Validation Rules: To be after VALUE.DATE and on or before MATURITY.DATE Defaults to MATURITY.DATE when not given. Must correspond to the id of record in the CURRENCY table |
| 8 | `SY.DCI.FIXING.TIME` | `SyDci_FixingTime` | TField |  | This field is used for reporting purpose, where the time during which the fixing event happens is recordedmanually. |
| 9 | `SY.DCI.TRADE.CCY` | `SyDci_TradeCcy` | TField |  | This is the deposit currency in which the customer deposit / takes loan in MM.MONEY.MARKET. Is the TRADE.CCY ofDX.TRADE. Validation Rules: Type CCY Must correspond to the id of record in the CURRENCY table |
| 10 | `SY.DCI.ALTERNATE.CCY.1` | `SyDci_AlternateCcy1` | TField |  | The alternate currency in which the deposit amount is paid back i.e the delivery currency in DX.TRADE and theother currency in FOREX. Validation Rules: Type CCY Must correspond to the id of record in the CURRENCY table |
| 11 | `SY.DCI.CUSTOMER` | `SyDci_Customer` | TField |  | Can be a Customer / Dealer book which gets mapped to PRI.CUST.NO in DX.TRADE and CUSTOMER.ID in MM.MONEY.MARKET. Validation Rules: Valid record in DX.CUSTOMER |
| 12 | `SY.DCI.PORTFOLIO` | `SyDci_Portfolio` | TField |  | Holds the portfolio corresponding to CUSTOMER. Validation Rules: Valid record in SEC.ACC.MASTER |
| 13 | `SY.DCI.CUST.DEPOSIT.ACC` | `SyDci_CustDepositAcc` | TField |  | CUSTOMER account from which the amount gets debited for deposit and credited on loan Validation Rules: Account must correspond to TRADE.CCY and belong to the PORTFOLIO \ CUSTOMER used. When dealer book gets defaulted to CRF account. |
| 14 | `SY.DCI.CUST.ALT.CCY.ACC.1` | `SyDci_CustAltCcyAcc1` | TField |  | This is the settlement account in ALTERNATE.CCY.1 in which the deposit amount is settled back to customer. Validation Rules: Account must correspond to ALTERNATE.CCY.1 and belong to the PORTFOLIO \ CUSTOMER used. When dealer book gets defaulted to CRF account. |
| 15 | `SY.DCI.COUNTERPARTY` | `SyDci_Counterparty` | TField |  | This will be dealer book for client deals and counterparty for counterparty deals. Validation Rules: Either CUSTOMER or COUNTERPARTY should be OWN-BOOK |
| 16 | `SY.DCI.CPARTY.PORTFOLIO` | `SyDci_CpartyPortfolio` | TField |  | Portfolio corresponding to COUNTERPARTY when the counterparty is customer. Validation Rules: Valid record in SEC.ACC.MASTER |
| 17 | `SY.DCI.CPARTY.DEPOSIT.ACC` | `SyDci_CpartyDepositAcc` | TField |  | COUNTERPARTY's deposit account in TRADE.CCY. Validation Rules: Account must correspond to TRADE.CCY and belong to the PORTFOLIO / COUNTERPARTY used. |
| 18 | `SY.DCI.CPARTY.ALTCCYACC.1` | `SyDci_CpartyAltccyacc1` | TField |  |  |
| 19 | `SY.DCI.BASE.CCY.1` | `SyDci_BaseCcy1` | TField |  | The base or quote currency between TRADE.CCY and ALTERNATE.CCY.1 Validation Rules: Type CCY Defaults with stronger currency among TRADE.CCY and ALTERNATE.CCY.1 when not given To be either TRADE.CCY or ALTERNATE.CCY.1 |
| 20 | `SY.DCI.SPOT.PRICE.1` | `SyDci_SpotPrice1` | TField |  | The spot exchange rate on TRADE.DATE i.e during the contract input between TRADE and ALTERNATE.CCY.1 in terms ofBASE.CCY.1 Validation Rules: When not inputted defaults with mid rate between TRADE.CCY and ALTERNATE.CCY.1 in terms of BASE.CCY.1 |
| 21 | `SY.DCI.STRIKE.PERCENT.1` | `SyDci_StrikePercent1` | TField |  | This is a percentage field. When set, STRIKE.PRICE.1 is calculated as (SPOT.PRICE.1 * STRIKE.PERCENT.1)/100 |
| 22 | `SY.DCI.STRIKE.PRICE.1` | `SyDci_StrikePrice1` | TField |  | This is rate between TRADE.CCY and ALTERNATE.CCY.1 in terms of BASE.CCY.1. When STRIKE.PERCENT.1 is given thenthe field value is calculated as (SPOT.PRICE * STRIKE.PERCENT.1)/100. Validation Rules: Defaults with mid rate between TRADE.CCY and ALTERNATE.CCY.1 with base currency as BASE.CCY.1 |
| 23 | `SY.DCI.CATEGORY` | `SyDci_Category` | TField |  | The deposit or loan category in which the MM.MONEY.MARKET gets created.This field value is mapped to CATEGORYfield of MM.MONEY.MARKET. The category code from 21000 to 21049 is for deposits and 21050 to 21099 is for loans. Validation Rules: Valid record in CATEGORY table Allowed category code is between the range 21000 to 21099. |
| 24 | `SY.DCI.BASE.INTEREST.RATE` | `SyDci_BaseInterestRate` | TField |  | This field is for information purpose which holds the base interest rate. |
| 25 | `SY.DCI.INTEREST.SPREAD` | `SyDci_InterestSpread` | TField |  | This field is for information purpose which holds the interest spread. |
| 26 | `SY.DCI.INTEREST.RATE` | `SyDci_InterestRate` | TField |  | This the interest paid on money market contract, which is mapped to INTEREST.RATE field of MM.MONEY.MARKET. |
| 27 | `SY.DCI.DAY.BASIS` | `SyDci_DayBasis` | TField |  | Day basis based on which the total interest amount is calcualted in money market contract. This field value ismapped to INTEREST.BASIS field of MM.MONEY.MARKET. Validation Rules: Default the INTEREST.DAY.BASIS of TRADE.CCY The accepted values are A, B, C, D, E, F, S, W, E1, W1, G |
| 28 | `SY.DCI.DEPOSIT.AMOUNT` | `SyDci_DepositAmount` | TField |  | The amount deposited or taken as loan in TRADE.CCY by CUSTOMER. This gets mapped to PRINCIPAL in MM.MONEY.MARKET. |
| 29 | `SY.DCI.INTEREST.AMOUNT` | `SyDci_InterestAmount` | TField |  | The interest on DEPOSIT.AMOUNT based on the interest rate and day basis for the period between value date andmaturity date is updated here. When value inputted this gets mapped to TOT.INTEREST.AMT field of money marketcontractamount deposited or taken as loan in TRADE.CCY by CUSTOMER. This gets mapped to PRINCIPAL inMM.MONEY.MARKET. |
| 30 | `SY.DCI.DEP.AMT.ALT.CCY.1` | `SyDci_DepAmtAltCcy1` | TField |  |  |
| 31 | `SY.DCI.INT.AMT.ALT.CCY.1` | `SyDci_IntAmtAltCcy1` | TField |  |  |
| 32 | `SY.DCI.ALTERNATE.CCY.2` | `SyDci_AlternateCcy2` | TField |  | The second alternate currency in which the deposit amount is paid back i.e this field enables the TRIPLE CURRENCYINVESTMENT. On exercise of option FOREX gets created between TRADE.CCY and ALTERNATE.CCY.2. The option tradebetween TRADE.CCY and ALTERNATE.CCY.1 is expired. Validation Rules: Type CCY Must correspond to the id of record in the CURRENCY table |
| 33 | `SY.DCI.BASE.CCY.2` | `SyDci_BaseCcy2` | TField |  | The base or quote currency between TRADE.CCY and ALTERNATE.CCY.2 Validation Rules: Type CCY Defaults with stronger currency among TRADE.CCY and ALTERNATE.CCY.2 when not given To be either TRADE.CCY or ALTERNATE.CCY.2 |
| 34 | `SY.DCI.SPOT.PRICE.2` | `SyDci_SpotPrice2` | TField |  | The spot exchange rate on TRADE.DATE i.e during the contract input between TRADE and ALTERNATE.CCY.2 in terms ofBASE.CCY.2 Validation Rules: When not inputted defaults with mid rate between TRADE.CCY and ALTERNATE.CCY.2 in terms of BASE.CCY.2 |
| 35 | `SY.DCI.STRIKE.PERCENT.2` | `SyDci_StrikePercent2` | TField |  | This is a percentage field. When set, STRIKE.PRICE.2 is calculated as (SPOT.PRICE.2 * STRIKE.PERCENT.2)/100 |
| 36 | `SY.DCI.STRIKE.PRICE.2` | `SyDci_StrikePrice2` | TField |  | This is rate between TRADE.CCY and ALTERNATE.CCY.2 in terms of BASE.CCY.2. When STRIKE.PERCENT.2 is given thenthe field value is calculated as (SPOT.PRICE * STRIKE.PERCENT.2)/100. Validation Rules: Defaults with mid rate between TRADE.CCY and ALTERNATE.CCY.2 with base currency as BASE.CCY.2 |
| 37 | `SY.DCI.CUST.ALT.CCY.ACC.2` | `SyDci_CustAltCcyAcc2` | TField |  | This is the settlement account in ALTERNATE.CCY.2 in which the deposit amount is settled back to customer. Validation Rules: Account must correspond to ALTERNATE.CCY.2 and belong to the PORTFOLIO \ CUSTOMER used. When dealer book gets defaulted to CRF account. |
| 38 | `SY.DCI.CPARTY.ALTCCYACC.2` | `SyDci_CpartyAltccyacc2` | TField |  |  |
| 39 | `SY.DCI.DEP.AMT.ALT.CCY.2` | `SyDci_DepAmtAltCcy2` | TField |  |  |
| 40 | `SY.DCI.INT.AMT.ALT.CCY.2` | `SyDci_IntAmtAltCcy2` | TField |  |  |
| 41 | `SY.DCI.DX.CONTRACT.CODE` | `SyDci_DxContractCode` | TField |  | The CONTRACT.CODE of option trade is mentioned here. The contract code should belong to generic FX-OTC option i.ethe currency pair being defined at trade level. Validation Rules: Valid in DX.CONTRACT.MASTER Only Daily maturity contract is allowed. |
| 42 | `SY.DCI.PREMIUM.CCY` | `SyDci_PremiumCcy` | TField |  | The currency in which the premium is denoted in the contract in the field PREMIUM.PRICE. |
| 43 | `SY.DCI.PREMIUM.PRICE` | `SyDci_PremiumPrice` | TField |  | The premium price per unit of lot in premium currency. |
| 44 | `SY.DCI.PREMIUM.PERCENT` | `SyDci_PremiumPercent` | TField |  | Either PREMIUM.PRICE or PREMIUM.PERCENT is allowed to input. This field holds the percenatge of premium to becharged from CUSTOMER. |
| 45 | `SY.DCI.PREMIUM.AMT` | `SyDci_PremiumAmt` | TField |  | Premium amount in terms of premium currency. When PREMIUM.PRICE is provide the premium amount is calculated asPREMIUM.PRICE in TRADE.CCY* DEPOSIT.AMOUNT . When PREMIUM.PERCENT is provided the amount is calcualted as(DEPOSIT.AMOUNT * PREMIUM.PERCENT)/100.In both the cases the PREMIUM.AMT is to be convereted in PREMIUM.CCY terms. |
| 46 | `SY.DCI.CPTY.PREM.AMT` | `SyDci_CptyPremAmt` | TField |  | This field will store the premium amount debited from/credited to the counterparty. Debit or Credit from counterparty will be decided based on the field PREMIUM.PAY.RECEIVE set This field is applicable only for agency booking model contracts. |
| 47 | `SY.DCI.PREMIUM.PAY.RECEIVE` | `SyDci_PremiumPayReceive` | TField |  | This field will say whether the customer have to pay/receive the premium amount |
| 48 | `SY.DCI.PREM.RESERVED.5` | `SyDci_PremReserved5` | TField |  |  |
| 49 | `SY.DCI.PREM.RESERVED.4` | `SyDci_PremReserved4` | TField |  |  |
| 50 | `SY.DCI.PREM.RESERVED.3` | `SyDci_PremReserved3` | TField |  |  |
| 51 | `SY.DCI.PREM.RESERVED.2` | `SyDci_PremReserved2` | TField |  |  |
| 52 | `SY.DCI.PREM.RESERVED.1` | `SyDci_PremReserved1` | TField |  |  |
| 53 | `SY.DCI.NOTIONAL.DEP.CCY` | `SyDci_NotionalDepCcy` | TField |  |  |
| 54 | `SY.DCI.NOTIONAL.ALT.CCY.1` | `SyDci_NotionalAltCcy1` | TField |  | Notional amount in terms of ALTERNATE.CCY.1 for which the notional entry is raised. This is the contingent entrythat gets reversed on maturity. |
| 55 | `SY.DCI.SY.TRANSACTION.REF` | `SyDci_SyTransactionRef` | TField |  | Stores the SY.TRANSACTION id that gets generated for the contract. Validation Rules: NOINPUT field |
| 56 | `SY.DCI.EXTERNAL.REF` | `SyDci_ExternalRef` | TField |  | This field is for information purpose used by client during interface. this is of free format text. |
| 57 | `SY.DCI.SY.DX.REFERENCE` | `SyDci_SyDxReference` | TField |  | This is a free text field which holds a reference. The same reference will be available in its underlying also.Updates SY.DX.LINK.FILE. |
| 58 | `SY.DCI.COUNTERPARTY.DEAL` | `SyDci_CounterpartyDeal` | TField |  | When the field is set as YES the deal is considered as the counterparty deal for Back to Back. |
| 59 | `SY.DCI.B2B.REFERENCE` | `SyDci_B2bReference` | TField |  | This is a free text field holding Back to Back reference. |
| 60 | `SY.DCI.MIS.INTEREST.RATE` | `SyDci_MisInterestRate` | TField |  | This field is for information purpose. |
| 61 | `SY.DCI.FEE.CCY` | `SyDci_FeeCcy` | TField |  | The currency in which FEE.AMT is paid |
| 62 | `SY.DCI.FEE.AMT` | `SyDci_FeeAmt` | TField |  | Amount of charges to be booked. This will be booked in the fee PL category with value date. |
| 63 | `SY.DCI.FEE.ACC` | `SyDci_FeeAcc` | TField |  | Customer account in fee currency from which the fee is paid. |
| 64 | `SY.DCI.CPTY.FEE.AMT` | `SyDci_CptyFeeAmt` | TField |  | This field will store the fee amount credited to counterparty. Fee amount entered in existing field FEE.AMT will be debited from customer and credited to PL/suspense categoryaccount.Fee entered in CPTY.FEE.AMT will be debited from PL/suspense category account and credited to thecounterparty. This field is applicable only for agency booking model contracts. |
| 65 | `SY.DCI.FEE.RESERVED.5` | `SyDci_FeeReserved5` | TField |  |  |
| 66 | `SY.DCI.FEE.RESERVED.4` | `SyDci_FeeReserved4` | TField |  |  |
| 67 | `SY.DCI.FEE.RESERVED.3` | `SyDci_FeeReserved3` | TField |  |  |
| 68 | `SY.DCI.FEE.RESERVED.2` | `SyDci_FeeReserved2` | TField |  |  |
| 69 | `SY.DCI.FEE.RESERVED.1` | `SyDci_FeeReserved1` | TField |  |  |
| 70 | `SY.DCI.RM.SPREAD.CCY` | `SyDci_RmSpreadCcy` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 71 | `SY.DCI.RM.SPREAD.RATE` | `SyDci_RmSpreadRate` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 72 | `SY.DCI.RM.SPREAD.AMT` | `SyDci_RmSpreadAmt` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 73 | `SY.DCI.CONVERT.INTEREST` | `SyDci_ConvertInterest` | TField |  | Allowed values are NO and null. When set to null, along with deposit amount interest is also paid inALTERNATE.CCY.1. When set to NO interest amount is paid back to customer in TRADE.CCY. |
| 74 | `SY.DCI.CREATE.DEPOSIT` | `SyDci_CreateDeposit` | TField |  | This field holds good only when SUPRESS.UNDERLYING in SY.PRODUCT.VARIANT/ SY.PRODUCT.DEFINITION (Product variantis of high priority) is set to YES. Which means that though supress underlying is set creation of MM deposit isstill performed by SY processing through T24 system. When SUPPRESS.UNDERLYING is set ot NO by default this fieldhold value as YES. |
| 75 | `SY.DCI.CREATE.OPTION` | `SyDci_CreateOption` | TField |  | This field holds good only when SUPRESS.UNDERLYING in SY.PRODUCT.VARIANT/ SY.PRODUCT.DEFINITION (Product variantis of high priority) is set to YES. Which means that though supress underlying is set creation of DX.TRADE is stillperformed by SY processing through T24 system. When SUPPRESS.UNDERLYING is set ot NO by default this field holdvalue as YES. |
| 76 | `SY.DCI.EXOTIC.TYPE` | `SyDci_ExoticType` |  |  |  |
| 77 | `SY.DCI.TRIGGER.EXOTIC` | `SyDci_TriggerExotic` |  |  |  |
| 78 | `SY.DCI.USR.FLD.TEXT` | `SyDci_UsrFldText` |  |  |  |
| 79 | `SY.DCI.USR.FLD.VAL` | `SyDci_UsrFldVal` |  |  |  |
| 80 | `SY.DCI.USR.RESERVED.05` | `SyDci_UsrReserved05` |  |  |  |
| 81 | `SY.DCI.USR.RESERVED.04` | `SyDci_UsrReserved04` |  |  |  |
| 82 | `SY.DCI.USR.RESERVED.03` | `SyDci_UsrReserved03` |  |  |  |
| 83 | `SY.DCI.USR.RESERVED.02` | `SyDci_UsrReserved02` |  |  |  |
| 84 | `SY.DCI.USR.RESERVED.01` | `SyDci_UsrReserved01` |  |  |  |
| 85 | `SY.DCI.EXERCISE.EXPIRE` | `SyDci_ExerciseExpire` | TField |  | When the field is set to EXERCISE the option contract is exercised and when set to EXPIRE the option contract isexpired. The value to the field can be manually determined. When not the fixing event determines the value to thisfield. The fixing routine to have 2 parameter which are outcoming. The 1st to hold the EXERCISE or EXPIRE as valuesaying the decision and the second to hold the EXERCISE.CCY if suppose the decision is to exercise the optioncontract. Validation Rules: The exotic rules gets applied to this which go along with DX. |
| 86 | `SY.DCI.EXERCISE.CCY` | `SyDci_ExerciseCcy` | TField |  | The currency in which the forex is created when it is ALTERNATE.CCY.1 then the DX.TRADE is exercised. When it isALTERNATE.CCY.2 then it means the DX.TRADE between trade and first alternate currency is expired and a new FX getscreated between TRADE.CCY and ALTERNATE.CCY.2. Validation Rules: Either ALTERNATE.CCY.1 or ALTERNATE.CCY.2 alone is allowed. |
| 87 | `SY.DCI.NEW.MATURITY.DATE` | `SyDci_NewMaturityDate` | TField |  | The early maturity or preclosure date. This date gets mapped to the MATURITY.DATE of money market contract. Validation Rules: Date beyond MATURITY.DATE is not allowed. |
| 88 | `SY.DCI.NEW.INTEREST.RATE` | `SyDci_NewInterestRate` | TField |  | The new rate on deposit. Validation Rules: Input allowed only when NEW.MATURITY.DATE is set. |
| 89 | `SY.DCI.NEW.INTEREST.AMT` | `SyDci_NewInterestAmt` | TField |  | The interest amount calcualted based on the new maturity date and new interest rate. Validation Rules: Input allowed only when NEW.MATURITY.DATE is set. Input allowed only when NEW.INTEREST.RATE is not set. |
| 90 | `SY.DCI.UNWIND.CHG.CCY` | `SyDci_UnwindChgCcy` | TField |  | Currency in which early termination charge are booked. |
| 91 | `SY.DCI.UNWIND.CHG.AMT` | `SyDci_UnwindChgAmt` | TField |  | Amount of charges to be booked. This will be booked in the unwinding charge PL category during unwinding process. |
| 92 | `SY.DCI.UNWIND.CHG.ACC` | `SyDci_UnwindChgAcc` | TField |  | Account in which unwinding charge are paid should be of UNWIND.CHG.CCY. |
| 93 | `SY.DCI.CPTY.UNWIND.CHG.AMT` | `SyDci_CptyUnwindChgAmt` | TField |  | This field will store the unwinding charge amount credited to counterparty. Unwinding charges entered in existing field UNWIND.CHG.AMT will be debited from customer and credited toPL/suspense category account. Charges entered in CPTY.UNWIND.CHG.AMT will be debited from PL/suspense categoryaccount and credited to the counterparty This field is applicable only for agency booking model contracts. |
| 94 | `SY.DCI.UNWIND.RESERVED.5` | `SyDci_UnwindReserved5` | TField |  |  |
| 95 | `SY.DCI.UNWIND.RESERVED.4` | `SyDci_UnwindReserved4` | TField |  |  |
| 96 | `SY.DCI.UNWIND.RESERVED.3` | `SyDci_UnwindReserved3` | TField |  |  |
| 97 | `SY.DCI.UNWIND.RESERVED.2` | `SyDci_UnwindReserved2` | TField |  |  |
| 98 | `SY.DCI.UNWIND.RESERVED.1` | `SyDci_UnwindReserved1` | TField |  |  |
| 99 | `SY.DCI.FX.AUTH` | `SyDci_FxAuth` | TField |  | The field is used to determine, if on exercise the FOREX contract is to be created on hold or authorised state.Allowed values are HOLD and AUTHORISED. Validation Rules: Default is HOLD. |
| 100 | `SY.DCI.DEALER.DESK` | `SyDci_DealerDesk` | TField |  | Specifies the system how its dealing room activity is organised Validation Rules: Must be a valid record in DEALER.DESK |
| 101 | `SY.DCI.UNWIND.POST.TIME` | `SyDci_UnwindPostTime` | TField |  | To post accounting entries based on selection Contains value IMMEDIATE and MATURITY |
| 102 | `SY.DCI.SY.MASTER` | `SyDci_SyMaster` | TField |  | This field will hold the SY.MASTER linked to the contract Validation Rules: Must be the ID of a valid SY.MASTER file record. |
| 103 | `SY.DCI.RISK.LEVEL` | `SyDci_RiskLevel` | TField |  | This field holds the product risk rating for the contract This field will be defaulted from SY.MASTER if master linked to the contract Validation Rules: Input to this field is derived from EB.LOOKUP table - RISK.LEVEL*(1-10) |
| 104 | `SY.DCI.ACCRUED.INT` | `SyDci_AccruedInt` | TField |  | Accrued interest will be calculated based on the transaction attributes (Principal, Interest rate, tenor, Daybasis) and will be updated during each COB |
| 105 | `SY.DCI.TAX.INTEREST.KEY` | `SyDci_TaxInterestKey` | TField |  | Tax will be calculated using the tax rate defined in the tax record Validation Rules: Must be a valid TAX record |
| 106 | `SY.DCI.TAX.INTEREST.TYPE` | `SyDci_TaxInterestType` | TField |  | Based on the customer grouping the corresponding TAX record will be used for calculating the tax Validation Rules: Must be a valid TAX.TYPE.CONDITION record |
| 107 | `SY.DCI.LOCAL.OR.SOURCE` | `SyDci_LocalOrSource` | TField |  | If set to 'LOCAL', in the customer vs counterparty booking model, the tax needs to be withheld by the bank. i.e.Tax needs to be calculated and posted to the tax account If set to 'SOURCE', it indicates that the counterparty has withheld the tax and therefore thetax entry will not be posted Validation Rules: Accepts LOCAL or SOURCE |
| 108 | `SY.DCI.TOT.INT.TAX` | `SyDci_TotIntTax` | TField |  | The tax rate is applied on the interest component and tax amount is stored in this field. |
| 109 | `SY.DCI.TOT.TAX.INT.LCY` | `SyDci_TotTaxIntLcy` | TField |  | Holds the tax amount in local currency. |
| 110 | `SY.DCI.PYMT.MSG.REQD` | `SyDci_PymtMsgReqd` | TField |  | When this field holds the value as YES, then payment message will be generated |
| 111 | `SY.DCI.DEP.CCY.BEN.BANK` | `SyDci_DepCcyBenBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 112 | `SY.DCI.DEP.CCY.BEN.ADD` | `SyDci_DepCcyBenAdd` |  |  |  |
| 113 | `SY.DCI.DEP.CCY.BEN.ACCT` | `SyDci_DepCcyBenAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 114 | `SY.DCI.DEP.CCY.INTR.BANK` | `SyDci_DepCcyIntrBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 115 | `SY.DCI.DEP.CCY.INTR.ADD` | `SyDci_DepCcyIntrAdd` |  |  |  |
| 116 | `SY.DCI.DEP.CCY.CPTY.NO` | `SyDci_DepCcyCptyNo` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 117 | `SY.DCI.DEP.CCY.CPTY.ADD` | `SyDci_DepCcyCptyAdd` |  |  |  |
| 118 | `SY.DCI.DEP.CCY.CPTY.ACCT` | `SyDci_DepCcyCptyAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 119 | `SY.DCI.TRADER.ID` | `SyDci_TraderId` | TField |  | This field holds the trader ID. |
| 120 | `SY.DCI.FIXING.REF.RATE` | `SyDci_FixingRefRate` | TField |  | This field will hold fixing rate, cut off time and location. |
| 121 | `SY.DCI.RM.MARKUP` | `SyDci_RmMarkup` | TField |  | This field will hold the RM Mark up |
| 122 | `SY.DCI.EXEC.CHANNEL` | `SyDci_ExecChannel` | TField |  | This field will hold the Execution channel |
| 123 | `SY.DCI.INT.CCY` | `SyDci_IntCcy` | TField |  | Holds the currency in which the interest can be paid, for deposits in precious metals |
| 124 | `SY.DCI.INT.CCY.ACCOUNT` | `SyDci_IntCcyAccount` | TField |  | Holds the account to which the interest need to be paid, for deposits in precious metals |
| 125 | `SY.DCI.INT.SPOT.RATE` | `SyDci_IntSpotRate` | TField |  | Defaults the exchange rate between Deposit currency and Interest Currency |
| 126 | `SY.DCI.ALT.CCY.BEN.BANK` | `SyDci_AltCcyBenBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 127 | `SY.DCI.ALT.CCY.BEN.ADD` | `SyDci_AltCcyBenAdd` |  |  |  |
| 128 | `SY.DCI.ALT.CCY.BEN.ACCT` | `SyDci_AltCcyBenAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 129 | `SY.DCI.ALT.CCY.INTR.BANK` | `SyDci_AltCcyIntrBank` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 130 | `SY.DCI.ALT.CCY.INTR.ADD` | `SyDci_AltCcyIntrAdd` |  |  |  |
| 131 | `SY.DCI.ALT.CCY.CPTY.NO` | `SyDci_AltCcyCptyNo` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 132 | `SY.DCI.ALT.CCY.CPTY.ADD` | `SyDci_AltCcyCptyAdd` |  |  |  |
| 133 | `SY.DCI.ALT.CCY.CPTY.ACCT` | `SyDci_AltCcyCptyAcct` | TField |  | This field will be mapped to SWIFT payment message (MT202) |
| 134 | `SY.DCI.ORDER.INITIATOR` | `SyDci_OrderInitiator` | TField |  | This field holds the Order Initiator. This might be the bank or the client (account holder). It can either hold values bank or Client�s customer ID. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 135 | `SY.DCI.TRADER` | `SyDci_Trader` | TField |  | This field holds the trader third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 136 | `SY.DCI.MANAGER` | `SyDci_Manager` | TField |  | This field holds the manager third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 137 | `SY.DCI.DECISION.MKR.ID` | `SyDci_DecisionMkrId` | TField |  | This field will provide user with the ability to identify the decision maker on the trade. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 138 | `SY.DCI.INSTRUCTION.MKR` | `SyDci_InstructionMkr` | TField |  | This field holds the ID of Instruction maker third party who is entitled to place orders on behalf of the main account holder. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 139 | `SY.DCI.CUSTOMER.LEI.NCI` | `SyDci_CustomerLeiNci` | TField |  | This field holds the LEI/NCI code of the customer. Validation If blank, system defaults the LEI/NCI of the customer based on priority defined in SC.NCI.PRIORITY and rules defined in SC.NCI.PARAMETER System raises error if it is not in the below format L/N-CustomerNo-LEI/NCI code |
| 140 | `SY.DCI.LEI.NCI.CHK.REQ` | `SyDci_LeiNciChkReq` | TField |  |  |
| 141 | `SY.DCI.RESERVED.07` | `SyDci_Reserved07` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 142 | `SY.DCI.RESERVED.06` | `SyDci_Reserved06` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 143 | `SY.DCI.RESERVED.05` | `SyDci_Reserved05` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 144 | `SY.DCI.RESERVED.04` | `SyDci_Reserved04` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 145 | `SY.DCI.RESERVED.03` | `SyDci_Reserved03` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 146 | `SY.DCI.RESERVED.02` | `SyDci_Reserved02` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 147 | `SY.DCI.RESERVED.01` | `SyDci_Reserved01` | TField |  | Reserved for future use. Validation Rules: NOINPUT field |
| 148 | `SY.DCI.LOCAL.REF` | `SyDci_LocalRef` |  |  |  |
| 149 | `SY.DCI.STMT.NOS` | `SyDci_StmtNos` |  |  |  |
| 150 | `SY.DCI.OVERRIDE` | `SyDci_Override` |  |  |  |
| 151 | `SY.DCI.RECORD.STATUS` | `SyDci_RecordStatus` | String |  |  |
| 152 | `SY.DCI.CURR.NO` | `SyDci_CurrNo` | String |  |  |
| 153 | `SY.DCI.INPUTTER` | `SyDci_Inputter` |  |  |  |
| 154 | `SY.DCI.DATE.TIME` | `SyDci_DateTime` |  |  |  |
| 155 | `SY.DCI.AUTHORISER` | `SyDci_Authoriser` | String |  |  |
| 156 | `SY.DCI.CO.CODE` | `SyDci_CoCode` | String |  |  |
| 157 | `SY.DCI.DEPT.CODE` | `SyDci_DeptCode` | String |  |  |
| 158 | `SY.DCI.AUDITOR.CODE` | `SyDci_AuditorCode` | String |  |  |
| 159 | `SY.DCI.AUDIT.DATE.TIME` | `SyDci_AuditDateTime` | String |  |  |
