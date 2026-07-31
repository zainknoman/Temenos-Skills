# SC.HOLDINGS.INSTRUCT — Table Schema

> Source: `INSERTS/I_F.SC.HOLDINGS.INSTRUCT` in `SC_SctStockReconciliation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.HI.PORTFOLIO.ID` | `ScHoldingsInstruct_PortfolioId` | TField |  |  |
| 2 | `SC.HI.HOLD.STMT.FREQ` | `ScHoldingsInstruct_HoldStmtFreq` | TField |  |  |
| 3 | `SC.HI.BALANCE.TYPE` | `ScHoldingsInstruct_BalanceType` | TField |  |  |
| 4 | `SC.HI.DELIVERY.REF` | `ScHoldingsInstruct_DeliveryRef` |  |  |  |
| 5 | `SC.HI.MSG.DATE` | `ScHoldingsInstruct_MsgDate` | TField |  |  |
| 6 | `SC.HI.MSG.TIME` | `ScHoldingsInstruct_MsgTime` | TField |  |  |
| 7 | `SC.HI.GENERATED.BY` | `ScHoldingsInstruct_GeneratedBy` | TField |  |  |
| 8 | `SC.HI.RESERVED15` | `ScHoldingsInstruct_Reserved15` | TField |  |  |
| 9 | `SC.HI.RESERVED14` | `ScHoldingsInstruct_Reserved14` | TField |  |  |
| 10 | `SC.HI.RESERVED13` | `ScHoldingsInstruct_Reserved13` | TField |  |  |
| 11 | `SC.HI.RESERVED12` | `ScHoldingsInstruct_Reserved12` | TField |  |  |
| 12 | `SC.HI.RESERVED11` | `ScHoldingsInstruct_Reserved11` | TField |  |  |
| 13 | `SC.HI.RESERVED10` | `ScHoldingsInstruct_Reserved10` | TField |  |  |
| 14 | `SC.HI.RESERVED9` | `ScHoldingsInstruct_Reserved9` | TField |  |  |
| 15 | `SC.HI.RESERVED8` | `ScHoldingsInstruct_Reserved8` | TField |  |  |
| 16 | `SC.HI.RESERVED7` | `ScHoldingsInstruct_Reserved7` | TField |  |  |
| 17 | `SC.HI.RESERVED6` | `ScHoldingsInstruct_Reserved6` | TField |  |  |
| 18 | `SC.HI.RESERVED5` | `ScHoldingsInstruct_Reserved5` | TField |  |  |
| 19 | `SC.HI.RESERVED4` | `ScHoldingsInstruct_Reserved4` | TField |  |  |
| 20 | `SC.HI.RESERVED3` | `ScHoldingsInstruct_Reserved3` | TField |  |  |
| 21 | `SC.HI.RESERVED2` | `ScHoldingsInstruct_Reserved2` | TField |  |  |
| 22 | `SC.HI.RESERVED1` | `ScHoldingsInstruct_Reserved1` | TField |  |  |
| 23 | `SC.HI.LOCAL.REF` | `ScHoldingsInstruct_LocalRef` |  |  |  |
| 24 | `SC.HI.OVERRIDE` | `ScHoldingsInstruct_Override` |  |  |  |
| 25 | `SC.HI.RECORD.STATUS` | `ScHoldingsInstruct_RecordStatus` | String |  |  |
| 26 | `SC.HI.CURR.NO` | `ScHoldingsInstruct_CurrNo` | String |  |  |
| 27 | `SC.HI.INPUTTER` | `ScHoldingsInstruct_Inputter` |  |  |  |
| 28 | `SC.HI.DATE.TIME` | `ScHoldingsInstruct_DateTime` |  |  |  |
| 29 | `SC.HI.AUTHORISER` | `ScHoldingsInstruct_Authoriser` | String |  |  |
| 30 | `SC.HI.CO.CODE` | `ScHoldingsInstruct_CoCode` | String |  |  |
| 31 | `SC.HI.DEPT.CODE` | `ScHoldingsInstruct_DeptCode` | String |  |  |
| 32 | `SC.HI.AUDITOR.CODE` | `ScHoldingsInstruct_AuditorCode` | String |  |  |
| 33 | `SC.HI.AUDIT.DATE.TIME` | `ScHoldingsInstruct_AuditDateTime` | String |  |  |
