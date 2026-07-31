# FS.GA.ADJUST.AMORTIZATION.ACCRETION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ADJUST.AMORTIZATION.ACCRETION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.FUND.ID` | `FsGaAdjustAmortizationAccretion_Fund` |  |  |  |
| 2 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.OPERATION.CODE` | `FsGaAdjustAmortizationAccretion_TransactionType` |  |  |  |
| 3 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.GL.ACCOUNT` | `FsGaAdjustAmortizationAccretion_CashAccountNumber` |  |  |  |
| 4 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.AMORTISATION.OR.ACCRETION.TYPE` | `FsGaAdjustAmortizationAccretion_AmortisationOrAccretionType` |  |  |  |
| 5 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.PCT.OR.AMOUNT.AMORT.OR.ACCR` | `FsGaAdjustAmortizationAccretion_PctOrAmountAmortOrAccr` |  |  |  |
| 6 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.LOCAL.CURRENCY` | `FsGaAdjustAmortizationAccretion_Currency` |  |  |  |
| 7 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.EFFECT.DATE` | `FsGaAdjustAmortizationAccretion_EffectDate` |  |  |  |
| 8 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.POSTING.LOCAL.CURRENCY` | `FsGaAdjustAmortizationAccretion_PostingCurrency` |  |  |  |
| 9 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED10` | `FsGaAdjustAmortizationAccretion_Reserved10` |  |  |  |
| 10 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED9` | `FsGaAdjustAmortizationAccretion_Reserved9` |  |  |  |
| 11 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED8` | `FsGaAdjustAmortizationAccretion_Reserved8` |  |  |  |
| 12 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED7` | `FsGaAdjustAmortizationAccretion_Reserved7` |  |  |  |
| 13 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED6` | `FsGaAdjustAmortizationAccretion_Reserved6` |  |  |  |
| 14 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED5` | `FsGaAdjustAmortizationAccretion_Reserved5` |  |  |  |
| 15 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED4` | `FsGaAdjustAmortizationAccretion_Reserved4` |  |  |  |
| 16 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED3` | `FsGaAdjustAmortizationAccretion_Reserved3` |  |  |  |
| 17 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED2` | `FsGaAdjustAmortizationAccretion_Reserved2` |  |  |  |
| 18 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RESERVED1` | `FsGaAdjustAmortizationAccretion_Reserved1` |  |  |  |
| 19 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.RECORD.STATUS` | `FsGaAdjustAmortizationAccretion_RecordStatus` |  |  |  |
| 20 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.CURR.NO` | `FsGaAdjustAmortizationAccretion_CurrNo` |  |  |  |
| 21 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.INPUTTER` | `FsGaAdjustAmortizationAccretion_Inputter` |  |  |  |
| 22 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.DATE.TIME` | `FsGaAdjustAmortizationAccretion_DateTime` |  |  |  |
| 23 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.AUTHORISER` | `FsGaAdjustAmortizationAccretion_Authoriser` |  |  |  |
| 24 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.CO.CODE` | `FsGaAdjustAmortizationAccretion_CoCode` |  |  |  |
| 25 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.DEPT.CODE` | `FsGaAdjustAmortizationAccretion_DeptCode` |  |  |  |
| 26 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.AUDITOR.CODE` | `FsGaAdjustAmortizationAccretion_AuditorCode` |  |  |  |
| 27 | `FS.GA.ADJUST.AMORTIZATION.ACCRETION.AUDIT.DATE.TIME` | `FsGaAdjustAmortizationAccretion_AuditDateTime` |  |  |  |
