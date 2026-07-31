# SC.CLEARING.CODE — Table Schema

> Source: `INSERTS/I_F.SC.CLEARING.CODE` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CLS.DEPOSITORY` | `ScClearingCode_Depository` |  |  |  |
| 2 | `SC.CLS.DEPOSITORY.TYPE` | `ScClearingCode_DepositoryType` |  |  |  |
| 3 | `SC.CLS.ASSET.TYPE` | `ScClearingCode_AssetType` |  |  |  |
| 4 | `SC.CLS.SUB.ASSET.TYPE` | `ScClearingCode_SubAssetType` |  |  |  |
| 5 | `SC.CLS.STOCK.EXCHANGE` | `ScClearingCode_StockExchange` |  |  |  |
| 6 | `SC.CLS.CLEARING.CODE` | `ScClearingCode_ClearingCode` |  |  |  |
| 7 | `SC.CLS.STATUS` | `ScClearingCode_Status` |  |  |  |
| 8 | `SC.CLS.RESERVED.10` | `ScClearingCode_Reserved10` |  |  |  |
| 9 | `SC.CLS.RESERVED.9` | `ScClearingCode_Reserved9` |  |  |  |
| 10 | `SC.CLS.RESERVED.8` | `ScClearingCode_Reserved8` |  |  |  |
| 11 | `SC.CLS.RESERVED.7` | `ScClearingCode_Reserved7` |  |  |  |
| 12 | `SC.CLS.RESERVED.6` | `ScClearingCode_Reserved6` |  |  |  |
| 13 | `SC.CLS.RESERVED.5` | `ScClearingCode_Reserved5` |  |  |  |
| 14 | `SC.CLS.RESERVED.4` | `ScClearingCode_Reserved4` |  |  |  |
| 15 | `SC.CLS.RESERVED.3` | `ScClearingCode_Reserved3` |  |  |  |
| 16 | `SC.CLS.RESERVED.2` | `ScClearingCode_Reserved2` |  |  |  |
| 17 | `SC.CLS.RESERVED.1` | `ScClearingCode_Reserved1` |  |  |  |
| 18 | `SC.CLS.LOCAL.REF` | `ScClearingCode_LocalRef` |  |  |  |
| 19 | `SC.CLS.OVERRIDE` | `ScClearingCode_Override` |  |  |  |
| 20 | `SC.CLS.RECORD.STATUS` | `ScClearingCode_RecordStatus` | String |  |  |
| 21 | `SC.CLS.CURR.NO` | `ScClearingCode_CurrNo` | String |  |  |
| 22 | `SC.CLS.INPUTTER` | `ScClearingCode_Inputter` |  |  |  |
| 23 | `SC.CLS.DATE.TIME` | `ScClearingCode_DateTime` |  |  |  |
| 24 | `SC.CLS.AUTHORISER` | `ScClearingCode_Authoriser` | String |  |  |
| 25 | `SC.CLS.CO.CODE` | `ScClearingCode_CoCode` | String |  |  |
| 26 | `SC.CLS.DEPT.CODE` | `ScClearingCode_DeptCode` | String |  |  |
| 27 | `SC.CLS.AUDITOR.CODE` | `ScClearingCode_AuditorCode` | String |  |  |
| 28 | `SC.CLS.AUDIT.DATE.TIME` | `ScClearingCode_AuditDateTime` | String |  |  |
