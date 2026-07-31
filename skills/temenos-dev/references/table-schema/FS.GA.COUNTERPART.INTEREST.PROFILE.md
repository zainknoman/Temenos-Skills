# FS.GA.COUNTERPART.INTEREST.PROFILE — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUNTERPART.INTEREST.PROFILE` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUNTERPART.INTEREST.PROFILE.COUNTERPARTY.CORRESPONDENT` | `FsGaCounterpartInterestProfile_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 2 | `FS.GA.COUNTERPART.INTEREST.PROFILE.INCOME.TYPE` | `FsGaCounterpartInterestProfile_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 3 | `FS.GA.COUNTERPART.INTEREST.PROFILE.INTEREST.RATE.TYPE` | `FsGaCounterpartInterestProfile_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 4 | `FS.GA.COUNTERPART.INTEREST.PROFILE.FUND.ID` | `FsGaCounterpartInterestProfile_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.COUNTERPART.INTEREST.PROFILE.SERVICE.CODE` | `FsGaCounterpartInterestProfile_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED10` | `FsGaCounterpartInterestProfile_Reserved10` | TField |  |  |
| 7 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED9` | `FsGaCounterpartInterestProfile_Reserved9` | TField |  |  |
| 8 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED8` | `FsGaCounterpartInterestProfile_Reserved8` | TField |  |  |
| 9 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED7` | `FsGaCounterpartInterestProfile_Reserved7` | TField |  |  |
| 10 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED6` | `FsGaCounterpartInterestProfile_Reserved6` | TField |  |  |
| 11 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED5` | `FsGaCounterpartInterestProfile_Reserved5` | TField |  |  |
| 12 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED4` | `FsGaCounterpartInterestProfile_Reserved4` | TField |  |  |
| 13 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED3` | `FsGaCounterpartInterestProfile_Reserved3` | TField |  |  |
| 14 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED2` | `FsGaCounterpartInterestProfile_Reserved2` | TField |  |  |
| 15 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RESERVED1` | `FsGaCounterpartInterestProfile_Reserved1` | TField |  |  |
| 16 | `FS.GA.COUNTERPART.INTEREST.PROFILE.RECORD.STATUS` | `FsGaCounterpartInterestProfile_RecordStatus` | String |  |  |
| 17 | `FS.GA.COUNTERPART.INTEREST.PROFILE.CURR.NO` | `FsGaCounterpartInterestProfile_CurrNo` | String |  |  |
| 18 | `FS.GA.COUNTERPART.INTEREST.PROFILE.INPUTTER` | `FsGaCounterpartInterestProfile_Inputter` |  |  |  |
| 19 | `FS.GA.COUNTERPART.INTEREST.PROFILE.DATE.TIME` | `FsGaCounterpartInterestProfile_DateTime` |  |  |  |
| 20 | `FS.GA.COUNTERPART.INTEREST.PROFILE.AUTHORISER` | `FsGaCounterpartInterestProfile_Authoriser` | String |  |  |
| 21 | `FS.GA.COUNTERPART.INTEREST.PROFILE.CO.CODE` | `FsGaCounterpartInterestProfile_CoCode` | String |  |  |
| 22 | `FS.GA.COUNTERPART.INTEREST.PROFILE.DEPT.CODE` | `FsGaCounterpartInterestProfile_DeptCode` | String |  |  |
| 23 | `FS.GA.COUNTERPART.INTEREST.PROFILE.AUDITOR.CODE` | `FsGaCounterpartInterestProfile_AuditorCode` | String |  |  |
| 24 | `FS.GA.COUNTERPART.INTEREST.PROFILE.AUDIT.DATE.TIME` | `FsGaCounterpartInterestProfile_AuditDateTime` | String |  |  |
