# FS.GA.WARRANT.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.WARRANT.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WARRANT.DETAIL.INTERNAL.SECURITY.ID` | `FsGaWarrantDetail_SecurityId` |  |  |  |
| 2 | `FS.GA.WARRANT.DETAIL.DESCRIPTION` | `FsGaWarrantDetail_Description` |  |  |  |
| 3 | `FS.GA.WARRANT.DETAIL.START.DATE.WARRANT.EXERCISE` | `FsGaWarrantDetail_StartDateWarrantExercise` |  |  |  |
| 4 | `FS.GA.WARRANT.DETAIL.END.DATE.WARRANT.EXERCISE` | `FsGaWarrantDetail_EndDateWarrantExercise` |  |  |  |
| 5 | `FS.GA.WARRANT.DETAIL.CALL.OR.PUT.WARRANT.TYPE` | `FsGaWarrantDetail_CallOrPutWarrantType` |  |  |  |
| 6 | `FS.GA.WARRANT.DETAIL.WARRANT.STRIKE.TRANSACTION.PRICE` | `FsGaWarrantDetail_WarrantStrikePrice` |  |  |  |
| 7 | `FS.GA.WARRANT.DETAIL.WARRANT.STRIKE.PRICE.LOCAL.CURRENCY` | `FsGaWarrantDetail_WarrantStrikePriceCurrency` |  |  |  |
| 8 | `FS.GA.WARRANT.DETAIL.EXCH.RATE.WARRANT.STRIKE.PR` | `FsGaWarrantDetail_ExchRateWarrantStrikePr` |  |  |  |
| 9 | `FS.GA.WARRANT.DETAIL.WARRANT.EXECUTION.TRANSACTION.PRICE` | `FsGaWarrantDetail_WarrantExecutionPrice` |  |  |  |
| 10 | `FS.GA.WARRANT.DETAIL.WARRANT.EXECUTION.PRICE.CCY` | `FsGaWarrantDetail_WarrantExecutionPriceCcy` |  |  |  |
| 11 | `FS.GA.WARRANT.DETAIL.EXCH.RATE.WARRANT.EXEC.PR` | `FsGaWarrantDetail_ExchRateWarrantExecPr` |  |  |  |
| 12 | `FS.GA.WARRANT.DETAIL.GIVE.FOR` | `FsGaWarrantDetail_GiveFor` |  |  |  |
| 13 | `FS.GA.WARRANT.DETAIL.UNDERLYING.RATIO.WARRANTS` | `FsGaWarrantDetail_UnderlyingRatioWarrants` |  |  |  |
| 14 | `FS.GA.WARRANT.DETAIL.RESERVED10` | `FsGaWarrantDetail_Reserved10` |  |  |  |
| 15 | `FS.GA.WARRANT.DETAIL.RESERVED9` | `FsGaWarrantDetail_Reserved9` |  |  |  |
| 16 | `FS.GA.WARRANT.DETAIL.RESERVED8` | `FsGaWarrantDetail_Reserved8` |  |  |  |
| 17 | `FS.GA.WARRANT.DETAIL.RESERVED7` | `FsGaWarrantDetail_Reserved7` |  |  |  |
| 18 | `FS.GA.WARRANT.DETAIL.RESERVED6` | `FsGaWarrantDetail_Reserved6` |  |  |  |
| 19 | `FS.GA.WARRANT.DETAIL.RESERVED5` | `FsGaWarrantDetail_Reserved5` |  |  |  |
| 20 | `FS.GA.WARRANT.DETAIL.RESERVED4` | `FsGaWarrantDetail_Reserved4` |  |  |  |
| 21 | `FS.GA.WARRANT.DETAIL.RESERVED3` | `FsGaWarrantDetail_Reserved3` |  |  |  |
| 22 | `FS.GA.WARRANT.DETAIL.RESERVED2` | `FsGaWarrantDetail_Reserved2` |  |  |  |
| 23 | `FS.GA.WARRANT.DETAIL.RESERVED1` | `FsGaWarrantDetail_Reserved1` |  |  |  |
| 24 | `FS.GA.WARRANT.DETAIL.RECORD.STATUS` | `FsGaWarrantDetail_RecordStatus` |  |  |  |
| 25 | `FS.GA.WARRANT.DETAIL.CURR.NO` | `FsGaWarrantDetail_CurrNo` |  |  |  |
| 26 | `FS.GA.WARRANT.DETAIL.INPUTTER` | `FsGaWarrantDetail_Inputter` |  |  |  |
| 27 | `FS.GA.WARRANT.DETAIL.DATE.TIME` | `FsGaWarrantDetail_DateTime` |  |  |  |
| 28 | `FS.GA.WARRANT.DETAIL.AUTHORISER` | `FsGaWarrantDetail_Authoriser` |  |  |  |
| 29 | `FS.GA.WARRANT.DETAIL.CO.CODE` | `FsGaWarrantDetail_CoCode` |  |  |  |
| 30 | `FS.GA.WARRANT.DETAIL.DEPT.CODE` | `FsGaWarrantDetail_DeptCode` |  |  |  |
| 31 | `FS.GA.WARRANT.DETAIL.AUDITOR.CODE` | `FsGaWarrantDetail_AuditorCode` |  |  |  |
| 32 | `FS.GA.WARRANT.DETAIL.AUDIT.DATE.TIME` | `FsGaWarrantDetail_AuditDateTime` |  |  |  |
