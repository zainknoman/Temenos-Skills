# SC.SETT.INSTRUCT — Table Schema

> Source: `INSERTS/I_F.SC.SETT.INSTRUCT` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SSI.SSI` | `ScSettInstruct_Ssi` |  |  |  |
| 2 | `SC.SSI.STOCK.EXCHANGE` | `ScSettInstruct_StockExchange` |  |  |  |
| 3 | `SC.SSI.PL.SETT` | `ScSettInstruct_PlSett` |  |  |  |
| 4 | `SC.SSI.ASSET.SUB` | `ScSettInstruct_AssetSub` |  |  |  |
| 5 | `SC.SSI.ISIN.COUNTRY` | `ScSettInstruct_IsinCountry` |  |  |  |
| 6 | `SC.SSI.DEAG` | `ScSettInstruct_Deag` |  |  |  |
| 7 | `SC.SSI.DEAG.AC` | `ScSettInstruct_DeagAc` |  |  |  |
| 8 | `SC.SSI.REAG` | `ScSettInstruct_Reag` |  |  |  |
| 9 | `SC.SSI.REAG.AC` | `ScSettInstruct_ReagAc` |  |  |  |
| 10 | `SC.SSI.DECU` | `ScSettInstruct_Decu` |  |  |  |
| 11 | `SC.SSI.DECU.AC` | `ScSettInstruct_DecuAc` |  |  |  |
| 12 | `SC.SSI.RECU` | `ScSettInstruct_Recu` |  |  |  |
| 13 | `SC.SSI.RECU.AC` | `ScSettInstruct_RecuAc` |  |  |  |
| 14 | `SC.SSI.BUYR` | `ScSettInstruct_Buyr` |  |  |  |
| 15 | `SC.SSI.BUYR.AC` | `ScSettInstruct_BuyrAc` |  |  |  |
| 16 | `SC.SSI.SELL` | `ScSettInstruct_Sell` |  |  |  |
| 17 | `SC.SSI.SELL.AC` | `ScSettInstruct_SellAc` |  |  |  |
| 18 | `SC.SSI.PSET` | `ScSettInstruct_Pset` |  |  |  |
| 19 | `SC.SSI.PL.CODE` | `ScSettInstruct_PlCode` |  |  |  |
| 20 | `SC.SSI.PL.SAFEKEEP` | `ScSettInstruct_PlSafekeep` |  |  |  |
| 21 | `SC.SSI.STAMP.TXN` | `ScSettInstruct_StampTxn` |  |  |  |
| 22 | `SC.SSI.STAMP.INDICATOR` | `ScSettInstruct_StampIndicator` |  |  |  |
| 23 | `SC.SSI.DIRECT.CHARGES` | `ScSettInstruct_DirectCharges` |  |  |  |
| 24 | `SC.SSI.RESERVED.12` | `ScSettInstruct_Reserved12` |  |  |  |
| 25 | `SC.SSI.RESERVED.13` | `ScSettInstruct_Reserved13` |  |  |  |
| 26 | `SC.SSI.RESERVED.14` | `ScSettInstruct_Reserved14` |  |  |  |
| 27 | `SC.SSI.RESERVED.15` | `ScSettInstruct_Reserved15` |  |  |  |
| 28 | `SC.SSI.DELIVERY.INSTR` | `ScSettInstruct_DeliveryInstr` | TField |  | This field will accept valid SC.DEL.INSTR ID. The field will be defaulted from CUSTOMER.SECURITY record of thebroker. |
| 29 | `SC.SSI.DEPOT.ADVICE.REQD` | `ScSettInstruct_DepotAdviceReqd` | TField |  | This field specifies whether a depository advice is to be produced. |
| 30 | `SC.SSI.SEC.HOLD.SETTLE` | `ScSettInstruct_SecHoldSettle` | TField |  | This field will be used to control whether stock will update the SC.SETTLEMENT application. |
| 31 | `SC.SSI.SSI.BRK.CHG` | `ScSettInstruct_SsiBrkChg` |  |  |  |
| 32 | `SC.SSI.BRK.CHG.ACCT` | `ScSettInstruct_BrkChgAcct` |  |  |  |
| 33 | `SC.SSI.BRK.CHG.ACC.CCY` | `ScSettInstruct_BrkChgAccCcy` |  |  |  |
| 34 | `SC.SSI.INST.TYPE` | `ScSettInstruct_InstType` |  |  |  |
| 35 | `SC.SSI.INST.CURRENCY` | `ScSettInstruct_InstCurrency` |  |  |  |
| 36 | `SC.SSI.BEN.BANK` | `ScSettInstruct_BenBank` |  |  |  |
| 37 | `SC.SSI.BEN.ACCOUNT` | `ScSettInstruct_BenAccount` |  |  |  |
| 38 | `SC.SSI.LOCAL.REF` | `ScSettInstruct_LocalRef` |  |  |  |
| 39 | `SC.SSI.RECORD.STATUS` | `ScSettInstruct_RecordStatus` | String |  |  |
| 40 | `SC.SSI.CURR.NO` | `ScSettInstruct_CurrNo` | String |  |  |
| 41 | `SC.SSI.INPUTTER` | `ScSettInstruct_Inputter` |  |  |  |
| 42 | `SC.SSI.DATE.TIME` | `ScSettInstruct_DateTime` |  |  |  |
| 43 | `SC.SSI.AUTHORISER` | `ScSettInstruct_Authoriser` | String |  |  |
| 44 | `SC.SSI.CO.CODE` | `ScSettInstruct_CoCode` | String |  |  |
| 45 | `SC.SSI.DEPT.CODE` | `ScSettInstruct_DeptCode` | String |  |  |
| 46 | `SC.SSI.AUDITOR.CODE` | `ScSettInstruct_AuditorCode` | String |  |  |
| 47 | `SC.SSI.AUDIT.DATE.TIME` | `ScSettInstruct_AuditDateTime` | String |  |  |
| 48 | `SC.SSI.ISSUER` | `ScSettInstruct_Issuer` |  |  |  |
| 49 | `SC.SSI.VALID.FROM` | `ScSettInstruct_ValidFrom` |  |  |  |
| 50 | `SC.SSI.VALID.TO` | `ScSettInstruct_ValidTo` |  |  |  |
| 51 | `SC.SSI.LAST.REVIEW.DATE` | `ScSettInstruct_LastReviewDate` |  |  |  |
| 52 | `SC.SSI.STATUS` | `ScSettInstruct_Status` |  |  |  |
| 53 | `SC.SSI.SSI.STP` | `ScSettInstruct_SsiStp` |  |  |  |
| 54 | `SC.SSI.ROLE` | `ScSettInstruct_Role` | TField |  | This field will show the role played by the counterparty The Role will be defaulted CUSTOMER.TYPE of CUSTOMER.SECURITY |
| 55 | `SC.SSI.OVERRIDE` | `ScSettInstruct_Override` |  |  |  |
