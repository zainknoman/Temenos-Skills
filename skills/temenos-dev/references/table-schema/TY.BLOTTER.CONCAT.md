# TY.BLOTTER.CONCAT — Table Schema

> Source: `INSERTS/I_F.TY.BLOTTER.CONCAT` in `TY_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.BLT.CON.COUNTERPARTY` | `TyBlotterConcat_Counterparty` | TField |  |  |
| 2 | `TY.BLT.CON.COUNTERPARTY.NAME` | `TyBlotterConcat_CounterpartyName` | TField |  |  |
| 3 | `TY.BLT.CON.DEAL.TYPE` | `TyBlotterConcat_DealType` | TField |  |  |
| 4 | `TY.BLT.CON.SUB.DEAL.TYPE` | `TyBlotterConcat_SubDealType` | TField |  |  |
| 5 | `TY.BLT.CON.AMOUNT.1` | `TyBlotterConcat_Amount1` | TField |  |  |
| 6 | `TY.BLT.CON.CCY.1` | `TyBlotterConcat_Ccy1` | TField |  |  |
| 7 | `TY.BLT.CON.RATE.1` | `TyBlotterConcat_Rate1` | TField |  |  |
| 8 | `TY.BLT.CON.AMOUNT.2` | `TyBlotterConcat_Amount2` | TField |  |  |
| 9 | `TY.BLT.CON.CCY.2` | `TyBlotterConcat_Ccy2` | TField |  |  |
| 10 | `TY.BLT.CON.RATE.2` | `TyBlotterConcat_Rate2` | TField |  |  |
| 11 | `TY.BLT.CON.VALUE.DATE` | `TyBlotterConcat_ValueDate` | TField |  |  |
| 12 | `TY.BLT.CON.REUTERS.DEAL.ID` | `TyBlotterConcat_ReutersDealId` | TField |  |  |
| 13 | `TY.BLT.CON.MATURITY.DATE` | `TyBlotterConcat_MaturityDate` | TField |  |  |
| 14 | `TY.BLT.CON.DEAL.DATE` | `TyBlotterConcat_DealDate` | TField |  |  |
| 15 | `TY.BLT.CON.INSTRUMENT` | `TyBlotterConcat_Instrument` | TField |  |  |
| 16 | `TY.BLT.CON.ISSUED.BY` | `TyBlotterConcat_IssuedBy` | TField |  |  |
| 17 | `TY.BLT.CON.PORTFOLIO` | `TyBlotterConcat_Portfolio` | TField |  |  |
| 18 | `TY.BLT.CON.DEPOSITORY` | `TyBlotterConcat_Depository` | TField |  |  |
| 19 | `TY.BLT.CON.INPUTTER` | `TyBlotterConcat_Inputter` |  |  |  |
| 20 | `TY.BLT.CON.BROKER` | `TyBlotterConcat_Broker` | TField |  |  |
| 21 | `TY.BLT.CON.METHOD` | `TyBlotterConcat_Method` | TField |  |  |
| 22 | `TY.BLT.CON.DEALER.DESK` | `TyBlotterConcat_DealerDesk` | TField |  |  |
| 23 | `TY.BLT.CON.INTER.DEALER.DESK` | `TyBlotterConcat_InterDealerDesk` | TField |  |  |
| 24 | `TY.BLT.CON.DESCRIPTION` | `TyBlotterConcat_Description` | TField |  |  |
| 25 | `TY.BLT.CON.ORDER.STATUS` | `TyBlotterConcat_OrderStatus` | TField |  |  |
| 26 | `TY.BLT.CON.BUY.OR.SELL` | `TyBlotterConcat_BuyOrSell` | TField |  |  |
| 27 | `TY.BLT.CON.RECORD.STATUS` | `TyBlotterConcat_RecordStatus` | String |  |  |
| 28 | `TY.BLT.CON.CONTRACT.STATUS` | `TyBlotterConcat_ContractStatus` | TField |  |  |
| 29 | `TY.BLT.CON.DATE.TIME` | `TyBlotterConcat_DateTime` |  |  |  |
| 30 | `TY.BLT.CON.FIXING.OR.EXERCISE.DATE` | `TyBlotterConcat_FixingOrExerciseDate` | TField |  |  |
| 31 | `TY.BLT.CON.RATE.KEY.1` | `TyBlotterConcat_RateKey1` | TField |  |  |
| 32 | `TY.BLT.CON.RATE.KEY.2` | `TyBlotterConcat_RateKey2` | TField |  |  |
| 33 | `TY.BLT.CON.WHAT.IF` | `TyBlotterConcat_WhatIf` | TField |  |  |
| 34 | `TY.BLT.CON.RESERVED.7` | `TyBlotterConcat_Reserved7` | TField |  |  |
| 35 | `TY.BLT.CON.RESERVED.6` | `TyBlotterConcat_Reserved6` | TField |  |  |
| 36 | `TY.BLT.CON.RESERVED.5` | `TyBlotterConcat_Reserved5` | TField |  |  |
| 37 | `TY.BLT.CON.RESERVED.4` | `TyBlotterConcat_Reserved4` | TField |  |  |
| 38 | `TY.BLT.CON.RESERVED.3` | `TyBlotterConcat_Reserved3` | TField |  |  |
| 39 | `TY.BLT.CON.RESERVED.2` | `TyBlotterConcat_Reserved2` | TField |  |  |
| 40 | `TY.BLT.CON.RESERVED.1` | `TyBlotterConcat_Reserved1` | TField |  |  |
| 41 | `TY.BLT.CON.LOCAL.REF` | `TyBlotterConcat_LocalRef` |  |  |  |
