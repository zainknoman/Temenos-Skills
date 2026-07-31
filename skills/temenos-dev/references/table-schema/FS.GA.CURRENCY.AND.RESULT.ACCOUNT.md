# FS.GA.CURRENCY.AND.RESULT.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCY.AND.RESULT.ACCOUNT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CHART.OF.ACCOUNTS.CODE` | `FsGaCurrencyAndResultAccount_ChartOfAccountsCode` |  |  |  |
| 2 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.SPOT.ACCOUNT` | `FsGaCurrencyAndResultAccount_CambioSpotAccount` |  |  |  |
| 3 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.SUFFIX.CAMBIO.SPOT.ACCOUNT` | `FsGaCurrencyAndResultAccount_SuffixCambioSpotAccount` |  |  |  |
| 4 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.REALIZED.CAMBIO.SPOT.ACC.DB` | `FsGaCurrencyAndResultAccount_RealizedCambioSpotAccDb` |  |  |  |
| 5 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.REALIZED.CAMBIO.SPOT.ACC.CR` | `FsGaCurrencyAndResultAccount_RealizedCambioSpotAccCr` |  |  |  |
| 6 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.SPOT.REALIZED.ACCOUNT.DB` | `FsGaCurrencyAndResultAccount_SpotRealizedAccountDb` |  |  |  |
| 7 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.SPOT.REALIZED.ACCOUNT.CR` | `FsGaCurrencyAndResultAccount_SpotRealizedAccountCr` |  |  |  |
| 8 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.ACCOUNT.FORWARD` | `FsGaCurrencyAndResultAccount_CambioAccountForward` |  |  |  |
| 9 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.SUFFIX.FOR.CAMBIO.ACC.FORWARD` | `FsGaCurrencyAndResultAccount_SuffixForCambioAccForward` |  |  |  |
| 10 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.FWD.REALIZED.ACCOUNT.DB` | `FsGaCurrencyAndResultAccount_FwdRealizedAccountDb` |  |  |  |
| 11 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.FWD.REALIZED.ACCOUNT.CR` | `FsGaCurrencyAndResultAccount_FwdRealizedAccountCr` |  |  |  |
| 12 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.REALIZED.CAMBIO.FWRD.ACC.DB` | `FsGaCurrencyAndResultAccount_RealizedCambioFwrdAccDb` |  |  |  |
| 13 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.REALIZED.CAMBIO.FWRD.ACC.CR` | `FsGaCurrencyAndResultAccount_RealizedCambioFwrdAccCr` |  |  |  |
| 14 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.GTI.CODE` | `FsGaCurrencyAndResultAccount_GtiCode` |  |  |  |
| 15 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.SPOT.ACCOUNT.NUMBER` | `FsGaCurrencyAndResultAccount_CambioSpotAccountNumber` |  |  |  |
| 16 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.SPOT.ACCOUNT.SUBNUMBER` | `FsGaCurrencyAndResultAccount_CambioSpotAccountSubnumber` |  |  |  |
| 17 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.FRWD.ACCOUNT.NUMBER` | `FsGaCurrencyAndResultAccount_CambioFrwdAccountNumber` |  |  |  |
| 18 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CAMBIO.FRWD.ACCOUNT.SUBNUMBER` | `FsGaCurrencyAndResultAccount_CambioFrwdAccountSubnumber` |  |  |  |
| 19 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED10` | `FsGaCurrencyAndResultAccount_Reserved10` |  |  |  |
| 20 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED9` | `FsGaCurrencyAndResultAccount_Reserved9` |  |  |  |
| 21 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED8` | `FsGaCurrencyAndResultAccount_Reserved8` |  |  |  |
| 22 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED7` | `FsGaCurrencyAndResultAccount_Reserved7` |  |  |  |
| 23 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED6` | `FsGaCurrencyAndResultAccount_Reserved6` |  |  |  |
| 24 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED5` | `FsGaCurrencyAndResultAccount_Reserved5` |  |  |  |
| 25 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED4` | `FsGaCurrencyAndResultAccount_Reserved4` |  |  |  |
| 26 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED3` | `FsGaCurrencyAndResultAccount_Reserved3` |  |  |  |
| 27 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED2` | `FsGaCurrencyAndResultAccount_Reserved2` |  |  |  |
| 28 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RESERVED1` | `FsGaCurrencyAndResultAccount_Reserved1` |  |  |  |
| 29 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.RECORD.STATUS` | `FsGaCurrencyAndResultAccount_RecordStatus` |  |  |  |
| 30 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CURR.NO` | `FsGaCurrencyAndResultAccount_CurrNo` |  |  |  |
| 31 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.INPUTTER` | `FsGaCurrencyAndResultAccount_Inputter` |  |  |  |
| 32 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.DATE.TIME` | `FsGaCurrencyAndResultAccount_DateTime` |  |  |  |
| 33 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.AUTHORISER` | `FsGaCurrencyAndResultAccount_Authoriser` |  |  |  |
| 34 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.CO.CODE` | `FsGaCurrencyAndResultAccount_CoCode` |  |  |  |
| 35 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.DEPT.CODE` | `FsGaCurrencyAndResultAccount_DeptCode` |  |  |  |
| 36 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.AUDITOR.CODE` | `FsGaCurrencyAndResultAccount_AuditorCode` |  |  |  |
| 37 | `FS.GA.CURRENCY.AND.RESULT.ACCOUNT.AUDIT.DATE.TIME` | `FsGaCurrencyAndResultAccount_AuditDateTime` |  |  |  |
