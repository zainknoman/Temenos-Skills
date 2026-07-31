# FS.GA.NAV.PROCESS.FX.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.PROCESS.FX.GROUP` in `FS_ProcessingValuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.PROCESS.FX.GROUP.PROCESS.ID` | `FsGaNavProcessFxGroup_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 2 | `FS.GA.NAV.PROCESS.FX.GROUP.VALUATION.TYPE` | `FsGaNavProcessFxGroup_ValuationType` | TField |  | Type of NAV like O for Official, U for Unofficial, I for Intraday etc Multifonds DB Column is TYP_TRT. |
| 3 | `FS.GA.NAV.PROCESS.FX.GROUP.EXCHANGE.RATE.GROUP` | `FsGaNavProcessFxGroup_ExchangeRateGroup` | TField |  | Group of exchange rate. Use to define/select specific exchange rates and not generic. Multifonds DB Column is FX_GROUP. |
| 4 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED10` | `FsGaNavProcessFxGroup_Reserved10` | TField |  |  |
| 5 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED9` | `FsGaNavProcessFxGroup_Reserved9` | TField |  |  |
| 6 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED8` | `FsGaNavProcessFxGroup_Reserved8` | TField |  |  |
| 7 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED7` | `FsGaNavProcessFxGroup_Reserved7` | TField |  |  |
| 8 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED6` | `FsGaNavProcessFxGroup_Reserved6` | TField |  |  |
| 9 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED5` | `FsGaNavProcessFxGroup_Reserved5` | TField |  |  |
| 10 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED4` | `FsGaNavProcessFxGroup_Reserved4` | TField |  |  |
| 11 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED3` | `FsGaNavProcessFxGroup_Reserved3` | TField |  |  |
| 12 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED2` | `FsGaNavProcessFxGroup_Reserved2` | TField |  |  |
| 13 | `FS.GA.NAV.PROCESS.FX.GROUP.RESERVED1` | `FsGaNavProcessFxGroup_Reserved1` | TField |  |  |
| 14 | `FS.GA.NAV.PROCESS.FX.GROUP.RECORD.STATUS` | `FsGaNavProcessFxGroup_RecordStatus` | String |  |  |
| 15 | `FS.GA.NAV.PROCESS.FX.GROUP.CURR.NO` | `FsGaNavProcessFxGroup_CurrNo` | String |  |  |
| 16 | `FS.GA.NAV.PROCESS.FX.GROUP.INPUTTER` | `FsGaNavProcessFxGroup_Inputter` |  |  |  |
| 17 | `FS.GA.NAV.PROCESS.FX.GROUP.DATE.TIME` | `FsGaNavProcessFxGroup_DateTime` |  |  |  |
| 18 | `FS.GA.NAV.PROCESS.FX.GROUP.AUTHORISER` | `FsGaNavProcessFxGroup_Authoriser` | String |  |  |
| 19 | `FS.GA.NAV.PROCESS.FX.GROUP.CO.CODE` | `FsGaNavProcessFxGroup_CoCode` | String |  |  |
| 20 | `FS.GA.NAV.PROCESS.FX.GROUP.DEPT.CODE` | `FsGaNavProcessFxGroup_DeptCode` | String |  |  |
| 21 | `FS.GA.NAV.PROCESS.FX.GROUP.AUDITOR.CODE` | `FsGaNavProcessFxGroup_AuditorCode` | String |  |  |
| 22 | `FS.GA.NAV.PROCESS.FX.GROUP.AUDIT.DATE.TIME` | `FsGaNavProcessFxGroup_AuditDateTime` | String |  |  |
