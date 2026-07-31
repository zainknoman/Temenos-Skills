# FS.GA.INTEREST.CALCULATION.BY.CP — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.CALCULATION.BY.CP` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.CALCULATION.BY.CP.COUNTERPARTY.CORRESPONDENT` | `FsGaInterestCalculationByCp_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 2 | `FS.GA.INTEREST.CALCULATION.BY.CP.LOCAL.CURRENCY` | `FsGaInterestCalculationByCp_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 3 | `FS.GA.INTEREST.CALCULATION.BY.CP.EFFECTIVE.DATE` | `FsGaInterestCalculationByCp_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 4 | `FS.GA.INTEREST.CALCULATION.BY.CP.PRICING.FACTOR.CODE` | `FsGaInterestCalculationByCp_PricingFactorCode` | TField |  | Calculation code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 5 | `FS.GA.INTEREST.CALCULATION.BY.CP.FIXING.RATE.INTEREST.CALC` | `FsGaInterestCalculationByCp_FixingRateInterestCalc` | TField |  | Fixing Rate Interest Calculation Multifonds DB Column is CUSANCE_FIX. |
| 6 | `FS.GA.INTEREST.CALCULATION.BY.CP.FLOATING.RATE.INTEREST.CALC` | `FsGaInterestCalculationByCp_FloatingRateInterestCalc` | TField |  | Floating Rate Interest Calculation Multifonds DB Column is CUSANCE_FLOAT. |
| 7 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED10` | `FsGaInterestCalculationByCp_Reserved10` | TField |  |  |
| 8 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED9` | `FsGaInterestCalculationByCp_Reserved9` | TField |  |  |
| 9 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED8` | `FsGaInterestCalculationByCp_Reserved8` | TField |  |  |
| 10 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED7` | `FsGaInterestCalculationByCp_Reserved7` | TField |  |  |
| 11 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED6` | `FsGaInterestCalculationByCp_Reserved6` | TField |  |  |
| 12 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED5` | `FsGaInterestCalculationByCp_Reserved5` | TField |  |  |
| 13 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED4` | `FsGaInterestCalculationByCp_Reserved4` | TField |  |  |
| 14 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED3` | `FsGaInterestCalculationByCp_Reserved3` | TField |  |  |
| 15 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED2` | `FsGaInterestCalculationByCp_Reserved2` | TField |  |  |
| 16 | `FS.GA.INTEREST.CALCULATION.BY.CP.RESERVED1` | `FsGaInterestCalculationByCp_Reserved1` | TField |  |  |
| 17 | `FS.GA.INTEREST.CALCULATION.BY.CP.RECORD.STATUS` | `FsGaInterestCalculationByCp_RecordStatus` | String |  |  |
| 18 | `FS.GA.INTEREST.CALCULATION.BY.CP.CURR.NO` | `FsGaInterestCalculationByCp_CurrNo` | String |  |  |
| 19 | `FS.GA.INTEREST.CALCULATION.BY.CP.INPUTTER` | `FsGaInterestCalculationByCp_Inputter` |  |  |  |
| 20 | `FS.GA.INTEREST.CALCULATION.BY.CP.DATE.TIME` | `FsGaInterestCalculationByCp_DateTime` |  |  |  |
| 21 | `FS.GA.INTEREST.CALCULATION.BY.CP.AUTHORISER` | `FsGaInterestCalculationByCp_Authoriser` | String |  |  |
| 22 | `FS.GA.INTEREST.CALCULATION.BY.CP.CO.CODE` | `FsGaInterestCalculationByCp_CoCode` | String |  |  |
| 23 | `FS.GA.INTEREST.CALCULATION.BY.CP.DEPT.CODE` | `FsGaInterestCalculationByCp_DeptCode` | String |  |  |
| 24 | `FS.GA.INTEREST.CALCULATION.BY.CP.AUDITOR.CODE` | `FsGaInterestCalculationByCp_AuditorCode` | String |  |  |
| 25 | `FS.GA.INTEREST.CALCULATION.BY.CP.AUDIT.DATE.TIME` | `FsGaInterestCalculationByCp_AuditDateTime` | String |  |  |
