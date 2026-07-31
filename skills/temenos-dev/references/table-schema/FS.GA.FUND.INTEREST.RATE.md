# FS.GA.FUND.INTEREST.RATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.INTEREST.RATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.INTEREST.RATE.FUND.ID` | `FsGaFundInterestRate_Fund` |  |  |  |
| 2 | `FS.GA.FUND.INTEREST.RATE.LOCAL.CURRENCY` | `FsGaFundInterestRate_Currency` |  |  |  |
| 3 | `FS.GA.FUND.INTEREST.RATE.INTEREST.RATE.TYPE` | `FsGaFundInterestRate_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 4 | `FS.GA.FUND.INTEREST.RATE.MINIMUM.DAYS` | `FsGaFundInterestRate_MinimumDays` | TField |  | Enter minimum days Multifonds DB Column is MIN_DAYS. |
| 5 | `FS.GA.FUND.INTEREST.RATE.MAXIMUM.DAYS` | `FsGaFundInterestRate_MaximumDays` | TField |  | Enter maximum days Multifonds DB Column is MAX_DAYS. |
| 6 | `FS.GA.FUND.INTEREST.RATE.RESERVED10` | `FsGaFundInterestRate_Reserved10` | TField |  |  |
| 7 | `FS.GA.FUND.INTEREST.RATE.RESERVED9` | `FsGaFundInterestRate_Reserved9` | TField |  |  |
| 8 | `FS.GA.FUND.INTEREST.RATE.RESERVED8` | `FsGaFundInterestRate_Reserved8` | TField |  |  |
| 9 | `FS.GA.FUND.INTEREST.RATE.RESERVED7` | `FsGaFundInterestRate_Reserved7` | TField |  |  |
| 10 | `FS.GA.FUND.INTEREST.RATE.RESERVED6` | `FsGaFundInterestRate_Reserved6` | TField |  |  |
| 11 | `FS.GA.FUND.INTEREST.RATE.RESERVED5` | `FsGaFundInterestRate_Reserved5` | TField |  |  |
| 12 | `FS.GA.FUND.INTEREST.RATE.RESERVED4` | `FsGaFundInterestRate_Reserved4` | TField |  |  |
| 13 | `FS.GA.FUND.INTEREST.RATE.RESERVED3` | `FsGaFundInterestRate_Reserved3` | TField |  |  |
| 14 | `FS.GA.FUND.INTEREST.RATE.RESERVED2` | `FsGaFundInterestRate_Reserved2` | TField |  |  |
| 15 | `FS.GA.FUND.INTEREST.RATE.RESERVED1` | `FsGaFundInterestRate_Reserved1` | TField |  |  |
| 16 | `FS.GA.FUND.INTEREST.RATE.RECORD.STATUS` | `FsGaFundInterestRate_RecordStatus` | String |  |  |
| 17 | `FS.GA.FUND.INTEREST.RATE.CURR.NO` | `FsGaFundInterestRate_CurrNo` | String |  |  |
| 18 | `FS.GA.FUND.INTEREST.RATE.INPUTTER` | `FsGaFundInterestRate_Inputter` |  |  |  |
| 19 | `FS.GA.FUND.INTEREST.RATE.DATE.TIME` | `FsGaFundInterestRate_DateTime` |  |  |  |
| 20 | `FS.GA.FUND.INTEREST.RATE.AUTHORISER` | `FsGaFundInterestRate_Authoriser` | String |  |  |
| 21 | `FS.GA.FUND.INTEREST.RATE.CO.CODE` | `FsGaFundInterestRate_CoCode` | String |  |  |
| 22 | `FS.GA.FUND.INTEREST.RATE.DEPT.CODE` | `FsGaFundInterestRate_DeptCode` | String |  |  |
| 23 | `FS.GA.FUND.INTEREST.RATE.AUDITOR.CODE` | `FsGaFundInterestRate_AuditorCode` | String |  |  |
| 24 | `FS.GA.FUND.INTEREST.RATE.AUDIT.DATE.TIME` | `FsGaFundInterestRate_AuditDateTime` | String |  |  |
