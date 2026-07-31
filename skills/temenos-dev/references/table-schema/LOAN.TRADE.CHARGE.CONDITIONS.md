# LOAN.TRADE.CHARGE.CONDITIONS — Table Schema

> Source: `INSERTS/I_F.LOAN.TRADE.CHARGE.CONDITIONS` in `LNTRAD_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LN.TRAD.SHORT.DESCRIPTION` | `TradeChargeConditions_ShortDescription` |  |  |  |
| 2 | `LN.TRAD.FULL.DESCRIPTION` | `TradeChargeConditions_FullDescription` |  |  |  |
| 3 | `LN.TRAD.CURRENCY` | `TradeChargeConditions_Currency` |  |  |  |
| 4 | `LN.TRAD.PL.CATEGORY` | `TradeChargeConditions_PlCategory` |  |  |  |
| 5 | `LN.TRAD.DEBIT.TXN.CODE` | `TradeChargeConditions_DebitTxnCode` |  |  |  |
| 6 | `LN.TRAD.CREDIT.TXN.CODE` | `TradeChargeConditions_CreditTxnCode` |  |  |  |
| 7 | `LN.TRAD.PAY.OR.RECEIVE` | `TradeChargeConditions_PayOrReceive` |  |  |  |
| 8 | `LN.TRAD.FLAT.AMOUNT` | `TradeChargeConditions_FlatAmount` |  |  |  |
| 9 | `LN.TRAD.PERCENTAGE` | `TradeChargeConditions_Percentage` |  |  |  |
| 10 | `LN.TRAD.CALC.SOURCE` | `TradeChargeConditions_CalcSource` |  |  |  |
| 11 | `LN.TRAD.AMORT` | `TradeChargeConditions_Amort` |  |  |  |
| 12 | `LN.TRAD.AMORT.PROPERTY` | `TradeChargeConditions_AmortProperty` |  |  |  |
| 13 | `LN.TRAD.INC.EXP.TREATMENT` | `TradeChargeConditions_IncExpTreatment` |  |  |  |
| 14 | `LN.TRAD.RESERVED14` | `TradeChargeConditions_Reserved14` |  |  |  |
| 15 | `LN.TRAD.RESERVED15` | `TradeChargeConditions_Reserved15` |  |  |  |
| 16 | `LN.TRAD.RESERVED16` | `TradeChargeConditions_Reserved16` |  |  |  |
| 17 | `LN.TRAD.RESERVED17` | `TradeChargeConditions_Reserved17` |  |  |  |
| 18 | `LN.TRAD.RESERVED18` | `TradeChargeConditions_Reserved18` |  |  |  |
| 19 | `LN.TRAD.RESERVED19` | `TradeChargeConditions_Reserved19` |  |  |  |
| 20 | `LN.TRAD.RESERVED20` | `TradeChargeConditions_Reserved20` |  |  |  |
| 21 | `LN.TRAD.RESERVED21` | `TradeChargeConditions_Reserved21` |  |  |  |
| 22 | `LN.TRAD.RESERVED22` | `TradeChargeConditions_Reserved22` |  |  |  |
| 23 | `LN.TRAD.LOCAL.REF` | `TradeChargeConditions_LocalRef` |  |  |  |
| 24 | `LN.TRAD.OVERRIDE` | `TradeChargeConditions_Override` |  |  |  |
| 25 | `LN.TRAD.RECORD.STATUS` | `TradeChargeConditions_RecordStatus` |  |  |  |
| 26 | `LN.TRAD.CURR.NO` | `TradeChargeConditions_CurrNo` |  |  |  |
| 27 | `LN.TRAD.INPUTTER` | `TradeChargeConditions_Inputter` |  |  |  |
| 28 | `LN.TRAD.DATE.TIME` | `TradeChargeConditions_DateTime` |  |  |  |
| 29 | `LN.TRAD.AUTHORISER` | `TradeChargeConditions_Authoriser` |  |  |  |
| 30 | `LN.TRAD.CO.CODE` | `TradeChargeConditions_CoCode` |  |  |  |
| 31 | `LN.TRAD.DEPT.CODE` | `TradeChargeConditions_DeptCode` |  |  |  |
| 32 | `LN.TRAD.AUDITOR.CODE` | `TradeChargeConditions_AuditorCode` |  |  |  |
| 33 | `LN.TRAD.AUDIT.DATE.TIME` | `TradeChargeConditions_AuditDateTime` |  |  |  |
