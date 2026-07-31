# FS.GA.INTEREST.RATE.TYPE.DELAY.DAY — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.RATE.TYPE.DELAY.DAY` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.INTEREST.RATE.TYPE` | `FsGaInterestRateTypeDelayDay_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 2 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.DELAY.DAYS` | `FsGaInterestRateTypeDelayDay_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 3 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.LOCAL.CURRENCY` | `FsGaInterestRateTypeDelayDay_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 4 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.FUND.ID` | `FsGaInterestRateTypeDelayDay_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED10` | `FsGaInterestRateTypeDelayDay_Reserved10` | TField |  |  |
| 6 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED9` | `FsGaInterestRateTypeDelayDay_Reserved9` | TField |  |  |
| 7 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED8` | `FsGaInterestRateTypeDelayDay_Reserved8` | TField |  |  |
| 8 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED7` | `FsGaInterestRateTypeDelayDay_Reserved7` | TField |  |  |
| 9 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED6` | `FsGaInterestRateTypeDelayDay_Reserved6` | TField |  |  |
| 10 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED5` | `FsGaInterestRateTypeDelayDay_Reserved5` | TField |  |  |
| 11 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED4` | `FsGaInterestRateTypeDelayDay_Reserved4` | TField |  |  |
| 12 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED3` | `FsGaInterestRateTypeDelayDay_Reserved3` | TField |  |  |
| 13 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED2` | `FsGaInterestRateTypeDelayDay_Reserved2` | TField |  |  |
| 14 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RESERVED1` | `FsGaInterestRateTypeDelayDay_Reserved1` | TField |  |  |
| 15 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.RECORD.STATUS` | `FsGaInterestRateTypeDelayDay_RecordStatus` | String |  |  |
| 16 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.CURR.NO` | `FsGaInterestRateTypeDelayDay_CurrNo` | String |  |  |
| 17 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.INPUTTER` | `FsGaInterestRateTypeDelayDay_Inputter` |  |  |  |
| 18 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.DATE.TIME` | `FsGaInterestRateTypeDelayDay_DateTime` |  |  |  |
| 19 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.AUTHORISER` | `FsGaInterestRateTypeDelayDay_Authoriser` | String |  |  |
| 20 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.CO.CODE` | `FsGaInterestRateTypeDelayDay_CoCode` | String |  |  |
| 21 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.DEPT.CODE` | `FsGaInterestRateTypeDelayDay_DeptCode` | String |  |  |
| 22 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.AUDITOR.CODE` | `FsGaInterestRateTypeDelayDay_AuditorCode` | String |  |  |
| 23 | `FS.GA.INTEREST.RATE.TYPE.DELAY.DAY.AUDIT.DATE.TIME` | `FsGaInterestRateTypeDelayDay_AuditDateTime` | String |  |  |
