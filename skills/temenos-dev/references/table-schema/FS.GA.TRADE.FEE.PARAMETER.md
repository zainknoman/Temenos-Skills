# FS.GA.TRADE.FEE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.TRADE.FEE.PARAMETER` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TRADE.FEE.PARAMETER.FEE.CODES` | `FsGaTradeFeeParameter_FeeCodes` | TField |  | Fee Code Multifonds DB Column is FEE_CODE. |
| 2 | `FS.GA.TRADE.FEE.PARAMETER.FEE.DESCRIPTION` | `FsGaTradeFeeParameter_FeeDescription` | TField |  | Fee Description Multifonds DB Column is FEE_DESC. |
| 3 | `FS.GA.TRADE.FEE.PARAMETER.PORTFOLIO.CODE` | `FsGaTradeFeeParameter_PortfolioCode` | TField |  | Portfolio Code Multifonds DB Column is PORTFOLIOCODE. |
| 4 | `FS.GA.TRADE.FEE.PARAMETER.LOVS.FOR.MFDI.MAPPING` | `FsGaTradeFeeParameter_LovsForMfdiMapping` | TField |  | List Of Values corresponding to columns of transaction / position to be maped (used for Db/Cr) Multifonds DB Column is MAP_LOV. |
| 5 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED10` | `FsGaTradeFeeParameter_Reserved10` | TField |  |  |
| 6 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED9` | `FsGaTradeFeeParameter_Reserved9` | TField |  |  |
| 7 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED8` | `FsGaTradeFeeParameter_Reserved8` | TField |  |  |
| 8 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED7` | `FsGaTradeFeeParameter_Reserved7` | TField |  |  |
| 9 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED6` | `FsGaTradeFeeParameter_Reserved6` | TField |  |  |
| 10 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED5` | `FsGaTradeFeeParameter_Reserved5` | TField |  |  |
| 11 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED4` | `FsGaTradeFeeParameter_Reserved4` | TField |  |  |
| 12 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED3` | `FsGaTradeFeeParameter_Reserved3` | TField |  |  |
| 13 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED2` | `FsGaTradeFeeParameter_Reserved2` | TField |  |  |
| 14 | `FS.GA.TRADE.FEE.PARAMETER.RESERVED1` | `FsGaTradeFeeParameter_Reserved1` | TField |  |  |
| 15 | `FS.GA.TRADE.FEE.PARAMETER.RECORD.STATUS` | `FsGaTradeFeeParameter_RecordStatus` | String |  |  |
| 16 | `FS.GA.TRADE.FEE.PARAMETER.CURR.NO` | `FsGaTradeFeeParameter_CurrNo` | String |  |  |
| 17 | `FS.GA.TRADE.FEE.PARAMETER.INPUTTER` | `FsGaTradeFeeParameter_Inputter` |  |  |  |
| 18 | `FS.GA.TRADE.FEE.PARAMETER.DATE.TIME` | `FsGaTradeFeeParameter_DateTime` |  |  |  |
| 19 | `FS.GA.TRADE.FEE.PARAMETER.AUTHORISER` | `FsGaTradeFeeParameter_Authoriser` | String |  |  |
| 20 | `FS.GA.TRADE.FEE.PARAMETER.CO.CODE` | `FsGaTradeFeeParameter_CoCode` | String |  |  |
| 21 | `FS.GA.TRADE.FEE.PARAMETER.DEPT.CODE` | `FsGaTradeFeeParameter_DeptCode` | String |  |  |
| 22 | `FS.GA.TRADE.FEE.PARAMETER.AUDITOR.CODE` | `FsGaTradeFeeParameter_AuditorCode` | String |  |  |
| 23 | `FS.GA.TRADE.FEE.PARAMETER.AUDIT.DATE.TIME` | `FsGaTradeFeeParameter_AuditDateTime` | String |  |  |
