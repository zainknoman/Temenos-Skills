# IFRS.ACCOUNTING.DETAILS — Table Schema

> Source: `INSERTS/I_F.IFRS.ACCOUNTING.DETAILS` in `IA_Accounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFRS.ACCT.DTLS.ACCT.HEAD.TYPE` | `IfrsAccountingDetails_AcctHeadType` |  |  |  |
| 2 | `IFRS.ACCT.DTLS.IFRS.BALANCE` | `IfrsAccountingDetails_IfrsBalance` |  |  |  |
| 3 | `IFRS.ACCT.DTLS.IFRS.LCY.BAL` | `IfrsAccountingDetails_IfrsLcyBal` |  |  |  |
| 4 | `IFRS.ACCT.DTLS.CONTRACT.BALANCE` | `IfrsAccountingDetails_ContractBalance` | TField |  | Also know as the T24 book balance,this field contains the total of on-balance sheet EB.CONTRACT.BALANCES till PERIOD.END excluding IF entries. User can also set any balance type for exclusion, provision for the same is given in BAL.TO.EXLD field of IFRS.ACCT.METHODS. |
| 5 | `IFRS.ACCT.DTLS.NPV.CON.CF.AMORT` | `IfrsAccountingDetails_NpvConCfAmort` | TField |  | To hold the NPV of the contractual cash flow under Amortised cost method, i.e at EIR |
| 6 | `IFRS.ACCT.DTLS.NPV.CON.CF.FV` | `IfrsAccountingDetails_NpvConCfFv` | TField |  | To hold the NPV of the contractual cash flow under FairValue method, i.e. at Market Rate |
| 7 | `IFRS.ACCT.DTLS.NPV.EXP.CF.AMORT` | `IfrsAccountingDetails_NpvExpCfAmort` | TField |  | To hold the NPV of the expected cash flow under Amortised cost, i.e. at EIR |
| 8 | `IFRS.ACCT.DTLS.VAL.EXP.COLL.AMORT` | `IfrsAccountingDetails_ValExpCollAmort` | TField |  | To hold the total value of the collateral under Amortised cost method. |
| 9 | `IFRS.ACCT.DTLS.NPV.EXP.CF.FV` | `IfrsAccountingDetails_NpvExpCfFv` | TField |  | To hold the NPV of expected cash flow under fairvalue method, i.e. Market Rate |
| 10 | `IFRS.ACCT.DTLS.VAL.EXP.COLL.FV` | `IfrsAccountingDetails_ValExpCollFv` | TField |  | To hold the total value of the collateral under fair value method |
| 11 | `IFRS.ACCT.DTLS.CASHFLOW.VERSION` | `IfrsAccountingDetails_CashflowVersion` | TField |  | This field denotes the version of the EB.CASHFLOW record used for the calculation of the entries or IFRS.BALANCE |
| 12 | `IFRS.ACCT.DTLS.CURR.NUM` | `IfrsAccountingDetails_CurrNum` | TField |  | This is the current number of this record. |
| 13 | `IFRS.ACCT.DTLS.HEDGED.CONTRACT.ID` | `IfrsAccountingDetails_HedgedContractId` |  |  |  |
| 14 | `IFRS.ACCT.DTLS.HEDGED.BOOK.COST` | `IfrsAccountingDetails_HedgedBookCost` |  |  |  |
| 15 | `IFRS.ACCT.DTLS.HEDGED.FAIR.VALUE` | `IfrsAccountingDetails_HedgedFairValue` |  |  |  |
| 16 | `IFRS.ACCT.DTLS.RESERVED.4` | `IfrsAccountingDetails_Reserved4` |  |  |  |
| 17 | `IFRS.ACCT.DTLS.RESERVED.3` | `IfrsAccountingDetails_Reserved3` |  |  |  |
| 18 | `IFRS.ACCT.DTLS.HEDGING.CONTRACT.ID` | `IfrsAccountingDetails_HedgingContractId` |  |  |  |
| 19 | `IFRS.ACCT.DTLS.HEDGING.BOOK.COST` | `IfrsAccountingDetails_HedgingBookCost` |  |  |  |
| 20 | `IFRS.ACCT.DTLS.HEDGING.FAIR.VALUE` | `IfrsAccountingDetails_HedgingFairValue` |  |  |  |
| 21 | `IFRS.ACCT.DTLS.RESERVED.2` | `IfrsAccountingDetails_Reserved2` |  |  |  |
| 22 | `IFRS.ACCT.DTLS.RESERVED.1` | `IfrsAccountingDetails_Reserved1` |  |  |  |
| 23 | `IFRS.ACCT.DTLS.HEDGE.STATUS` | `IfrsAccountingDetails_HedgeStatus` | TField |  | Field denotes the Hedge status for the Hedge relation defined in IAS.HEDGE.GROUP table. |
| 24 | `IFRS.ACCT.DTLS.PERIOD.DATE` | `IfrsAccountingDetails_PeriodDate` |  |  |  |
| 25 | `IFRS.ACCT.DTLS.I9ACT.HEAD.TYPE` | `IfrsAccountingDetails_I9actHeadType` |  |  |  |
| 26 | `IFRS.ACCT.DTLS.PROB.OF.DEFT` | `IfrsAccountingDetails_ProbOfDeft` |  |  |  |
| 27 | `IFRS.ACCT.DTLS.LOSS.GIVEN.DEFT` | `IfrsAccountingDetails_LossGivenDeft` |  |  |  |
| 28 | `IFRS.ACCT.DTLS.I9NPV.CON.CF.AMORT` | `IfrsAccountingDetails_I9npvConCfAmort` |  |  |  |
| 29 | `IFRS.ACCT.DTLS.I9NPV.CON.CF.FV` | `IfrsAccountingDetails_I9npvConCfFv` |  |  |  |
| 30 | `IFRS.ACCT.DTLS.I9NPV.EXP.CF.AMORT` | `IfrsAccountingDetails_I9npvExpCfAmort` |  |  |  |
| 31 | `IFRS.ACCT.DTLS.I9NPV.EXP.CF.FV` | `IfrsAccountingDetails_I9npvExpCfFv` |  |  |  |
| 32 | `IFRS.ACCT.DTLS.ECL` | `IfrsAccountingDetails_Ecl` |  |  |  |
| 33 | `IFRS.ACCT.DTLS.STAGE` | `IfrsAccountingDetails_Stage` |  |  |  |
| 34 | `IFRS.ACCT.DTLS.RESERVED5` | `IfrsAccountingDetails_Reserved5` |  |  |  |
| 35 | `IFRS.ACCT.DTLS.RESERVED4` | `IfrsAccountingDetails_Reserved4` |  |  |  |
| 36 | `IFRS.ACCT.DTLS.OVERDUE.BALANCES` | `IfrsAccountingDetails_OverdueBalances` | TField |  | This field holds the past due balance of the contract/account as on the date, on which this file is last updated if any. |
| 37 | `IFRS.ACCT.DTLS.EXPOSURE.AT.DEFAULT` | `IfrsAccountingDetails_ExposureAtDefault` | TField |  | Field which holds the exposure amount used for ECL(Expected Credit Loss) calculations. For contracts with steady cashflow, Exposure At Default(EAD) includes current outstanding principal as well as past due if any. For operating lease contracts, EAD includes ACC and DUE lease rentals from ECB. Updated when EAD.MODEL is OUTSTANDING.PRINCIPAL. Updated for Operating lease contract. |
| 38 | `IFRS.ACCT.DTLS.IFRS9.CONTRACT.BALANCE` | `IfrsAccountingDetails_Ifrs9ContractBalance` | TField |  | This field represents balance of a contract under IFRS9. This will be calculated as sum of contract balance (T24 balance) and balances under all IFRS accounting heads(excluding disclosure). |
| 39 | `IFRS.ACCT.DTLS.I9NPV.EXP.COLL.AMORT` | `IfrsAccountingDetails_I9npvExpCollAmort` |  |  |  |
| 40 | `IFRS.ACCT.DTLS.PIT.EAD` | `IfrsAccountingDetails_PitEad` |  |  |  |
