# FS.GA.CGT.HOLDING.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.CGT.HOLDING.PERIOD` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CGT.HOLDING.PERIOD.CAPITAL.GAIN.TAX.CODE` | `FsGaCgtHoldingPeriod_CapitalGainTaxCode` | TField |  | Capital Gain Tax Code Multifonds DB Column is CGT_CODE. |
| 2 | `FS.GA.CGT.HOLDING.PERIOD.TAX.DOMICILE` | `FsGaCgtHoldingPeriod_TaxDomicile` | TField |  | Shows the tax domicile of the securities Multifonds DB Column is CPAYS_TAX. |
| 3 | `FS.GA.CGT.HOLDING.PERIOD.CURRENCY.CODE` | `FsGaCgtHoldingPeriod_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 4 | `FS.GA.CGT.HOLDING.PERIOD.EFFECTIVE.DATE` | `FsGaCgtHoldingPeriod_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 5 | `FS.GA.CGT.HOLDING.PERIOD.TAX.SECURITY.TYPE` | `FsGaCgtHoldingPeriod_TaxSecurityType` | TField |  | Select the appropriate code which can be retrieved under 'TAX_SEC'. Allows to make an equivalence with the tax tables definition under Static data\Tax tables Multifonds DB Column is TAX_SEC_TYPE. |
| 6 | `FS.GA.CGT.HOLDING.PERIOD.NO.OF.DAYS.SHORT.TERM` | `FsGaCgtHoldingPeriod_NoOfDaysShortTerm` | TField |  | This field displays number of days short term for each tax security type Multifonds DB Column is HOLDING_PERIOD. |
| 7 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED10` | `FsGaCgtHoldingPeriod_Reserved10` | TField |  |  |
| 8 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED9` | `FsGaCgtHoldingPeriod_Reserved9` | TField |  |  |
| 9 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED8` | `FsGaCgtHoldingPeriod_Reserved8` | TField |  |  |
| 10 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED7` | `FsGaCgtHoldingPeriod_Reserved7` | TField |  |  |
| 11 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED6` | `FsGaCgtHoldingPeriod_Reserved6` | TField |  |  |
| 12 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED5` | `FsGaCgtHoldingPeriod_Reserved5` | TField |  |  |
| 13 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED4` | `FsGaCgtHoldingPeriod_Reserved4` | TField |  |  |
| 14 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED3` | `FsGaCgtHoldingPeriod_Reserved3` | TField |  |  |
| 15 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED2` | `FsGaCgtHoldingPeriod_Reserved2` | TField |  |  |
| 16 | `FS.GA.CGT.HOLDING.PERIOD.RESERVED1` | `FsGaCgtHoldingPeriod_Reserved1` | TField |  |  |
| 17 | `FS.GA.CGT.HOLDING.PERIOD.RECORD.STATUS` | `FsGaCgtHoldingPeriod_RecordStatus` | String |  |  |
| 18 | `FS.GA.CGT.HOLDING.PERIOD.CURR.NO` | `FsGaCgtHoldingPeriod_CurrNo` | String |  |  |
| 19 | `FS.GA.CGT.HOLDING.PERIOD.INPUTTER` | `FsGaCgtHoldingPeriod_Inputter` |  |  |  |
| 20 | `FS.GA.CGT.HOLDING.PERIOD.DATE.TIME` | `FsGaCgtHoldingPeriod_DateTime` |  |  |  |
| 21 | `FS.GA.CGT.HOLDING.PERIOD.AUTHORISER` | `FsGaCgtHoldingPeriod_Authoriser` | String |  |  |
| 22 | `FS.GA.CGT.HOLDING.PERIOD.CO.CODE` | `FsGaCgtHoldingPeriod_CoCode` | String |  |  |
| 23 | `FS.GA.CGT.HOLDING.PERIOD.DEPT.CODE` | `FsGaCgtHoldingPeriod_DeptCode` | String |  |  |
| 24 | `FS.GA.CGT.HOLDING.PERIOD.AUDITOR.CODE` | `FsGaCgtHoldingPeriod_AuditorCode` | String |  |  |
| 25 | `FS.GA.CGT.HOLDING.PERIOD.AUDIT.DATE.TIME` | `FsGaCgtHoldingPeriod_AuditDateTime` | String |  |  |
