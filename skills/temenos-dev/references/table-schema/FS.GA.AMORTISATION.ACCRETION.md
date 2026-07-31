# FS.GA.AMORTISATION.ACCRETION — Table Schema

> Source: `INSERTS/I_F.FS.GA.AMORTISATION.ACCRETION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AMORTISATION.ACCRETION.FUND.ID` | `FsGaAmortisationAccretion_Fund` |  |  |  |
| 2 | `AMORTISATION.ACCRETION.TRANSACTION.CODE` | `FsGaAmortisationAccretion_OperationCode` |  |  |  |
| 3 | `AMORTISATION.ACCRETION.ACCOUNT.NUMBER` | `FsGaAmortisationAccretion_AccountNumber` | TField |  | Account Number Multifonds DB Column is NRUBR. |
| 4 | `AMORTISATION.ACCRETION.ADJUSTMENT.TYPE` | `FsGaAmortisationAccretion_AdjustmentType` | TField |  | Adjustment Type Multifonds DB Column is TYPE_ADJUSTMENT. |
| 5 | `AMORTISATION.ACCRETION.PERCENTAGE.OR.AMOUNT` | `FsGaAmortisationAccretion_PercentageOrAmount` | TField |  | Percentage or Amount Multifonds DB Column is PCT_MNT. |
| 6 | `AMORTISATION.ACCRETION.LOCAL.CURRENCY` | `FsGaAmortisationAccretion_Currency` |  |  |  |
| 7 | `AMORTISATION.ACCRETION.EFFECTIVE.DATE` | `FsGaAmortisationAccretion_EffectiveDate` | TField |  | Effective Date Multifonds DB Column is EFFECTIVE_DATE. |
| 8 | `AMORTISATION.ACCRETION.POSTING.LOCAL.CURRENCY` | `FsGaAmortisationAccretion_PostingCurrency` | TField |  | Posting Currency Multifonds DB Column is CMON_POST. |
| 9 | `AMORTISATION.ACCRETION.RECORD.STATUS` | `FsGaAmortisationAccretion_RecordStatus` | String |  |  |
| 10 | `AMORTISATION.ACCRETION.CURR.NO` | `FsGaAmortisationAccretion_CurrNo` | String |  |  |
| 11 | `AMORTISATION.ACCRETION.INPUTTER` | `FsGaAmortisationAccretion_Inputter` |  |  |  |
| 12 | `AMORTISATION.ACCRETION.DATE.TIME` | `FsGaAmortisationAccretion_DateTime` |  |  |  |
| 13 | `AMORTISATION.ACCRETION.AUTHORISER` | `FsGaAmortisationAccretion_Authoriser` | String |  |  |
| 14 | `AMORTISATION.ACCRETION.CO.CODE` | `FsGaAmortisationAccretion_CoCode` | String |  |  |
| 15 | `AMORTISATION.ACCRETION.DEPT.CODE` | `FsGaAmortisationAccretion_DeptCode` | String |  |  |
| 16 | `AMORTISATION.ACCRETION.AUDITOR.CODE` | `FsGaAmortisationAccretion_AuditorCode` | String |  |  |
| 17 | `AMORTISATION.ACCRETION.AUDIT.DATE.TIME` | `FsGaAmortisationAccretion_AuditDateTime` | String |  |  |
