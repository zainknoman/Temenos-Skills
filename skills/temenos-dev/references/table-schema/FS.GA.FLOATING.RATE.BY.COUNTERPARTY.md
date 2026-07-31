# FS.GA.FLOATING.RATE.BY.COUNTERPARTY — Table Schema

> Source: `INSERTS/I_F.FS.GA.FLOATING.RATE.BY.COUNTERPARTY` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.COUNTERPARTY.CORRESPONDENT` | `FsGaFloatingRateByCounterparty_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 2 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.LOCAL.CURRENCY` | `FsGaFloatingRateByCounterparty_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 3 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.DAYS.OF.ACCRUED.INTEREST` | `FsGaFloatingRateByCounterparty_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 4 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.EFFECTIVE.DATE` | `FsGaFloatingRateByCounterparty_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 5 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.INTEREST.RATE.PERCENTAGE` | `FsGaFloatingRateByCounterparty_InterestRatePercentage` | TField |  | Refers to interest rate % to be applied to deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is TX_DPO. |
| 6 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.HIGHEST` | `FsGaFloatingRateByCounterparty_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 7 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.SEQUENCE.NUMBER.1` | `FsGaFloatingRateByCounterparty_SequenceNumber1` | TField |  | Sequence Number 1 Multifonds DB Column is SEQ_NUM. |
| 8 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED10` | `FsGaFloatingRateByCounterparty_Reserved10` | TField |  |  |
| 9 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED9` | `FsGaFloatingRateByCounterparty_Reserved9` | TField |  |  |
| 10 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED8` | `FsGaFloatingRateByCounterparty_Reserved8` | TField |  |  |
| 11 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED7` | `FsGaFloatingRateByCounterparty_Reserved7` | TField |  |  |
| 12 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED6` | `FsGaFloatingRateByCounterparty_Reserved6` | TField |  |  |
| 13 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED5` | `FsGaFloatingRateByCounterparty_Reserved5` | TField |  |  |
| 14 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED4` | `FsGaFloatingRateByCounterparty_Reserved4` | TField |  |  |
| 15 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED3` | `FsGaFloatingRateByCounterparty_Reserved3` | TField |  |  |
| 16 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED2` | `FsGaFloatingRateByCounterparty_Reserved2` | TField |  |  |
| 17 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RESERVED1` | `FsGaFloatingRateByCounterparty_Reserved1` | TField |  |  |
| 18 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.RECORD.STATUS` | `FsGaFloatingRateByCounterparty_RecordStatus` | String |  |  |
| 19 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.CURR.NO` | `FsGaFloatingRateByCounterparty_CurrNo` | String |  |  |
| 20 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.INPUTTER` | `FsGaFloatingRateByCounterparty_Inputter` |  |  |  |
| 21 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.DATE.TIME` | `FsGaFloatingRateByCounterparty_DateTime` |  |  |  |
| 22 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.AUTHORISER` | `FsGaFloatingRateByCounterparty_Authoriser` | String |  |  |
| 23 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.CO.CODE` | `FsGaFloatingRateByCounterparty_CoCode` | String |  |  |
| 24 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.DEPT.CODE` | `FsGaFloatingRateByCounterparty_DeptCode` | String |  |  |
| 25 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.AUDITOR.CODE` | `FsGaFloatingRateByCounterparty_AuditorCode` | String |  |  |
| 26 | `FS.GA.FLOATING.RATE.BY.COUNTERPARTY.AUDIT.DATE.TIME` | `FsGaFloatingRateByCounterparty_AuditDateTime` | String |  |  |
