# ILMATX.POSITION.BALANCE — Table Schema

> Source: `INSERTS/I_F.ILMATX.POSITION.BALANCE` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.POSITION.BALANCE.BALANCE` | `IlmatxPositionBalance_Balance` | TField |  | This field is Balance. |
| 2 | `ILMATX.POSITION.BALANCE.CREATE.DATE` | `IlmatxPositionBalance_CreateDate` | TField |  | This field is Record creation date. |
| 3 | `ILMATX.POSITION.BALANCE.LAST.VALUE.DATE` | `IlmatxPositionBalance_LastValueDate` | TField |  | This field is Last transaction Date. |
| 4 | `ILMATX.POSITION.BALANCE.POS.OPEN.DATE` | `IlmatxPositionBalance_PosOpenDate` | TField |  | This field is Position open date . |
| 5 | `ILMATX.POSITION.BALANCE.INV.CATEG` | `IlmatxPositionBalance_InvCateg` | TField |  | This field is Investment Category (Main/Sub). |
| 6 | `ILMATX.POSITION.BALANCE.DUAL.SEC` | `IlmatxPositionBalance_DualSec` | TField |  | This field is Dual security indicator. |
| 7 | `ILMATX.POSITION.BALANCE.ISRAELI` | `IlmatxPositionBalance_Israeli` | TField |  | This field is Israeli security indicator. |
| 8 | `ILMATX.POSITION.BALANCE.CURRENCY` | `IlmatxPositionBalance_Currency` | TField |  | This field is Rate Currency Code. |
| 9 | `ILMATX.POSITION.BALANCE.ADJ.CURRENCY` | `IlmatxPositionBalance_AdjCurrency` | TField |  | This field is Linkage/Adjusment Currency Code. |
| 10 | `ILMATX.POSITION.BALANCE.TRADE.CURRENCY` | `IlmatxPositionBalance_TradeCurrency` | TField |  | This field is Trade Currency Code. |
| 11 | `ILMATX.POSITION.BALANCE.RATE.MULT` | `IlmatxPositionBalance_RateMult` | TField |  | This field is Multiplier Rate. |
| 12 | `ILMATX.POSITION.BALANCE.RESERVED.5` | `IlmatxPositionBalance_Reserved5` | TField |  | Reserved for future use. |
| 13 | `ILMATX.POSITION.BALANCE.RESERVED.4` | `IlmatxPositionBalance_Reserved4` | TField |  | Reserved for future use. |
| 14 | `ILMATX.POSITION.BALANCE.RESERVED.3` | `IlmatxPositionBalance_Reserved3` | TField |  | Reserved for future use. |
| 15 | `ILMATX.POSITION.BALANCE.RESERVED.2` | `IlmatxPositionBalance_Reserved2` | TField |  | Reserved for future use. |
| 16 | `ILMATX.POSITION.BALANCE.RESERVED.1` | `IlmatxPositionBalance_Reserved1` | TField |  | Reserved for future use. |
| 17 | `ILMATX.POSITION.BALANCE.LOCAL.REF` | `IlmatxPositionBalance_LocalRef` |  |  |  |
| 18 | `ILMATX.POSITION.BALANCE.OVERRIDE` | `IlmatxPositionBalance_Override` |  |  |  |
| 19 | `ILMATX.POSITION.BALANCE.RECORD.STATUS` | `IlmatxPositionBalance_RecordStatus` | String |  |  |
| 20 | `ILMATX.POSITION.BALANCE.CURR.NO` | `IlmatxPositionBalance_CurrNo` | String |  |  |
| 21 | `ILMATX.POSITION.BALANCE.INPUTTER` | `IlmatxPositionBalance_Inputter` |  |  |  |
| 22 | `ILMATX.POSITION.BALANCE.DATE.TIME` | `IlmatxPositionBalance_DateTime` |  |  |  |
| 23 | `ILMATX.POSITION.BALANCE.AUTHORISER` | `IlmatxPositionBalance_Authoriser` | String |  |  |
| 24 | `ILMATX.POSITION.BALANCE.CO.CODE` | `IlmatxPositionBalance_CoCode` | String |  |  |
| 25 | `ILMATX.POSITION.BALANCE.DEPT.CODE` | `IlmatxPositionBalance_DeptCode` | String |  |  |
| 26 | `ILMATX.POSITION.BALANCE.AUDITOR.CODE` | `IlmatxPositionBalance_AuditorCode` | String |  |  |
| 27 | `ILMATX.POSITION.BALANCE.AUDIT.DATE.TIME` | `IlmatxPositionBalance_AuditDateTime` | String |  |  |
