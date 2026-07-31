# SC.ENT.INSTR — Table Schema

> Source: `INSERTS/I_F.SC.ENT.INSTR` in `SC_SccConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.INSTR.RIGHTS.TYPE` | `ScEntInstr_RightsType` |  |  |  |
| 2 | `SC.INSTR.RIGHTS.DOMICILE` | `ScEntInstr_RightsDomicile` |  |  |  |
| 3 | `SC.INSTR.RIGHTS.CCY` | `ScEntInstr_RightsCcy` |  |  |  |
| 4 | `SC.INSTR.RIGHTS` | `ScEntInstr_Rights` |  |  |  |
| 5 | `SC.INSTR.STOCK.CASH.TYPE` | `ScEntInstr_StockCashType` |  |  |  |
| 6 | `SC.INSTR.STOCK.CASH.DOM` | `ScEntInstr_StockCashDom` |  |  |  |
| 7 | `SC.INSTR.STOCK.CASH.CCY` | `ScEntInstr_StockCashCcy` |  |  |  |
| 8 | `SC.INSTR.STOCK.CASH` | `ScEntInstr_StockCash` |  |  |  |
| 9 | `SC.INSTR.REINVEST.TYPE` | `ScEntInstr_ReinvestType` |  |  |  |
| 10 | `SC.INSTR.REINVEST.DOM` | `ScEntInstr_ReinvestDom` |  |  |  |
| 11 | `SC.INSTR.REINVEST.CCY` | `ScEntInstr_ReinvestCcy` |  |  |  |
| 12 | `SC.INSTR.REINVEST.INCOME` | `ScEntInstr_ReinvestIncome` |  |  |  |
| 13 | `SC.INSTR.SELL.LOTS.TYPE` | `ScEntInstr_SellLotsType` |  |  |  |
| 14 | `SC.INSTR.SELL.LOTS.DOM` | `ScEntInstr_SellLotsDom` |  |  |  |
| 15 | `SC.INSTR.SELL.LOTS.CCY` | `ScEntInstr_SellLotsCcy` |  |  |  |
| 16 | `SC.INSTR.SELL.ODD.LOTS` | `ScEntInstr_SellOddLots` |  |  |  |
| 17 | `SC.INSTR.CASH.DIV.CCY` | `ScEntInstr_CashDivCcy` |  |  |  |
| 18 | `SC.INSTR.CASH.DIV.DFLT.CCY` | `ScEntInstr_CashDivDfltCcy` |  |  |  |
| 19 | `SC.INSTR.EVENT.TYPE` | `ScEntInstr_EventType` |  |  |  |
| 20 | `SC.INSTR.SEC.TYPE` | `ScEntInstr_SecType` |  |  |  |
| 21 | `SC.INSTR.EVENT.OPTION` | `ScEntInstr_EventOption` |  |  |  |
| 22 | `SC.INSTR.LOCAL.REF` | `ScEntInstr_LocalRef` |  |  |  |
| 23 | `SC.INSTR.RECORD.STATUS` | `ScEntInstr_RecordStatus` | String |  |  |
| 24 | `SC.INSTR.CURR.NO` | `ScEntInstr_CurrNo` | String |  |  |
| 25 | `SC.INSTR.INPUTTER` | `ScEntInstr_Inputter` |  |  |  |
| 26 | `SC.INSTR.DATE.TIME` | `ScEntInstr_DateTime` |  |  |  |
| 27 | `SC.INSTR.AUTHORISER` | `ScEntInstr_Authoriser` | String |  |  |
| 28 | `SC.INSTR.CO.CODE` | `ScEntInstr_CoCode` | String |  |  |
| 29 | `SC.INSTR.DEPT.CODE` | `ScEntInstr_DeptCode` | String |  |  |
| 30 | `SC.INSTR.AUDITOR.CODE` | `ScEntInstr_AuditorCode` | String |  |  |
| 31 | `SC.INSTR.AUDIT.DATE.TIME` | `ScEntInstr_AuditDateTime` | String |  |  |
