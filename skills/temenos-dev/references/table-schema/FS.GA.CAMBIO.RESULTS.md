# FS.GA.CAMBIO.RESULTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CAMBIO.RESULTS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMBIO.RESULTS.CHART` | `FsGaCambioResults_Chart` | TField |  | Chart Multifonds DB Column is CPDC. |
| 2 | `CAMBIO.RESULTS.CAMBIO.ACCOUNT.SPOT.ACCOUNT` | `FsGaCambioResults_CambioAccountSpotAccount` | TField |  | Cambio account Spot Account Multifonds DB Column is NRUBRCAM. |
| 3 | `CAMBIO.RESULTS.CAMBIO.ACCOUNT.SPOT.SUBNUM` | `FsGaCambioResults_CambioAccountSpotSubnum` | TField |  | Cambio account Spot Subnum Multifonds DB Column is NSUFFCAM. |
| 4 | `CAMBIO.RESULTS.REALIZED.ACCOUNT.SPOT.DEBIT` | `FsGaCambioResults_RealizedAccountSpotDebit` | TField |  | Realized account spot Debit Multifonds DB Column is NRUBRRES. |
| 5 | `CAMBIO.RESULTS.REALIZED.ACCOUNT.SPOT.CREDIT` | `FsGaCambioResults_RealizedAccountSpotCredit` | TField |  | Realized account spot Credit Multifonds DB Column is NRUBRRES_CR. |
| 6 | `CAMBIO.RESULTS.REALIZED.ACC.SPOT.DEBIT.SUFFIX` | `FsGaCambioResults_RealizedAccSpotDebitSuffix` | TField |  | Realized acc spot Debit suffix Multifonds DB Column is NSUFFRES. |
| 7 | `CAMBIO.RESULTS.REALIZED.ACC.SPOT.CR.SUFFIX` | `FsGaCambioResults_RealizedAccSpotCrSuffix` | TField |  | Realized acc spot Cr suffix Multifonds DB Column is NSUFFRES_CR. |
| 8 | `CAMBIO.RESULTS.CAMBIO.ACC.FORWARD.ACCOUNT` | `FsGaCambioResults_CambioAccForwardAccount` | TField |  | Cambio acc Forward Account Multifonds DB Column is NRUBRCTM. |
| 9 | `CAMBIO.RESULTS.CAMBIO.ACC.FORWARD.SUBNUM` | `FsGaCambioResults_CambioAccForwardSubnum` | TField |  | Cambio acc Forward Subnum Multifonds DB Column is NSUFFCTM. |
| 10 | `CAMBIO.RESULTS.REALIZED.ACCOUNT.FORWARD.DEBIT` | `FsGaCambioResults_RealizedAccountForwardDebit` | TField |  | Realized account forward Debit Multifonds DB Column is NRUBRRTM. |
| 11 | `CAMBIO.RESULTS.REALIZED.ACC.FORWARD.CREDIT` | `FsGaCambioResults_RealizedAccForwardCredit` | TField |  | Realized acc forward Credit Multifonds DB Column is NRUBRRTM_CR. |
| 12 | `CAMBIO.RESULTS.REALIZED.ACC.FORWARD.DR.SUFFIX` | `FsGaCambioResults_RealizedAccForwardDrSuffix` | TField |  | Realized acc forward Dr Suffix Multifonds DB Column is NSUFFRTM. |
| 13 | `CAMBIO.RESULTS.REALIZED.ACC.FORWARD.CR.SUFFIX` | `FsGaCambioResults_RealizedAccForwardCrSuffix` | TField |  | Realized acc forward Cr Suffix Multifonds DB Column is NSUFFRTM_CR. |
| 14 | `CAMBIO.RESULTS.SECURITY.TYPE` | `FsGaCambioResults_SecurityType` | TField |  | Security type Multifonds DB Column is CGTI. |
| 15 | `CAMBIO.RESULTS.CURRENCY.TR.ON.BALANCE.ACC` | `FsGaCambioResults_CurrencyTrOnBalanceAcc` | TField |  | Currency Tr on Balance Acc Multifonds DB Column is NRUBRCTN. |
| 16 | `CAMBIO.RESULTS.CCY.TR.ON.BALANCE.ACC.SUBNUM` | `FsGaCambioResults_CcyTrOnBalanceAccSubnum` | TField |  | Ccy Tr on Balance Acc subnum Multifonds DB Column is NSUFFCTN. |
| 17 | `CAMBIO.RESULTS.CURRENCY.TR.OFF.BALANCE.ACC` | `FsGaCambioResults_CurrencyTrOffBalanceAcc` | TField |  | Currency Tr off Balance Acc Multifonds DB Column is NRUBRCTF. |
| 18 | `CAMBIO.RESULTS.CCY.TR.OFF.BALANCE.ACC.SUBNUM` | `FsGaCambioResults_CcyTrOffBalanceAccSubnum` | TField |  | Ccy Tr off Balance Acc subnum Multifonds DB Column is NSUFFCTF. |
| 19 | `CAMBIO.RESULTS.RECORD.STATUS` | `FsGaCambioResults_RecordStatus` | String |  |  |
| 20 | `CAMBIO.RESULTS.CURR.NO` | `FsGaCambioResults_CurrNo` | String |  |  |
| 21 | `CAMBIO.RESULTS.INPUTTER` | `FsGaCambioResults_Inputter` |  |  |  |
| 22 | `CAMBIO.RESULTS.DATE.TIME` | `FsGaCambioResults_DateTime` |  |  |  |
| 23 | `CAMBIO.RESULTS.AUTHORISER` | `FsGaCambioResults_Authoriser` | String |  |  |
| 24 | `CAMBIO.RESULTS.CO.CODE` | `FsGaCambioResults_CoCode` | String |  |  |
| 25 | `CAMBIO.RESULTS.DEPT.CODE` | `FsGaCambioResults_DeptCode` | String |  |  |
| 26 | `CAMBIO.RESULTS.AUDITOR.CODE` | `FsGaCambioResults_AuditorCode` | String |  |  |
| 27 | `CAMBIO.RESULTS.AUDIT.DATE.TIME` | `FsGaCambioResults_AuditDateTime` | String |  |  |
