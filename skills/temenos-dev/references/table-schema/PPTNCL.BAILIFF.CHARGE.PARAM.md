# PPTNCL.BAILIFF.CHARGE.PARAM — Table Schema

> Source: `INSERTS/I_F.PPTNCL.BAILIFF.CHARGE.PARAM` in `PPTNCL_ChequeClearing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTNCL.CQ.BAILIFF.CHARGE` | `PptnclBailiffChargeParam_BailiffCharge` | TField |  |  |
| 2 | `PPTNCL.CQ.INTEREST.RATE` | `PptnclBailiffChargeParam_InterestRate` | TField |  |  |
| 3 | `PPTNCL.CQ.LEGAL.TYPE` | `PptnclBailiffChargeParam_LegalType` |  |  |  |
| 4 | `PPTNCL.CQ.TREASURY.CHARGE` | `PptnclBailiffChargeParam_TreasuryCharge` |  |  |  |
| 5 | `PPTNCL.CQ.LEGAL.PERIOD.DAYS` | `PptnclBailiffChargeParam_LegalPeriodDays` |  |  |  |
| 6 | `PPTNCL.CQ.CURRENCY` | `PptnclBailiffChargeParam_Currency` | TField |  |  |
| 7 | `PPTNCL.CQ.BAILIFF.CHARGE.PL.ACCOUNT` | `PptnclBailiffChargeParam_BailiffChargePlAccount` | TField |  |  |
| 8 | `PPTNCL.CQ.TREASURY.CHARGE.PL.ACCOUNT` | `PptnclBailiffChargeParam_TreasuryChargePlAccount` | TField |  |  |
| 9 | `PPTNCL.CQ.RESERVED.9` | `PptnclBailiffChargeParam_Reserved9` | TField |  |  |
| 10 | `PPTNCL.CQ.RESERVED.8` | `PptnclBailiffChargeParam_Reserved8` | TField |  |  |
| 11 | `PPTNCL.CQ.RESERVED.7` | `PptnclBailiffChargeParam_Reserved7` | TField |  |  |
| 12 | `PPTNCL.CQ.RESERVED.6` | `PptnclBailiffChargeParam_Reserved6` | TField |  |  |
| 13 | `PPTNCL.CQ.RESERVED.5` | `PptnclBailiffChargeParam_Reserved5` | TField |  |  |
| 14 | `PPTNCL.CQ.RESERVED.4` | `PptnclBailiffChargeParam_Reserved4` | TField |  |  |
| 15 | `PPTNCL.CQ.RESERVED.3` | `PptnclBailiffChargeParam_Reserved3` | TField |  |  |
| 16 | `PPTNCL.CQ.RESERVED.2` | `PptnclBailiffChargeParam_Reserved2` | TField |  |  |
| 17 | `PPTNCL.CQ.RESERVED.1` | `PptnclBailiffChargeParam_Reserved1` | TField |  |  |
| 18 | `PPTNCL.CQ.LOCAL.REF` | `PptnclBailiffChargeParam_LocalRef` |  |  |  |
| 19 | `PPTNCL.CQ.OVERRIDE` | `PptnclBailiffChargeParam_Override` |  |  |  |
| 20 | `PPTNCL.CQ.RECORD.STATUS` | `PptnclBailiffChargeParam_RecordStatus` | String |  |  |
| 21 | `PPTNCL.CQ.CURR.NO` | `PptnclBailiffChargeParam_CurrNo` | String |  |  |
| 22 | `PPTNCL.CQ.INPUTTER` | `PptnclBailiffChargeParam_Inputter` |  |  |  |
| 23 | `PPTNCL.CQ.DATE.TIME` | `PptnclBailiffChargeParam_DateTime` |  |  |  |
| 24 | `PPTNCL.CQ.AUTHORISER` | `PptnclBailiffChargeParam_Authoriser` | String |  |  |
| 25 | `PPTNCL.CQ.CO.CODE` | `PptnclBailiffChargeParam_CoCode` | String |  |  |
| 26 | `PPTNCL.CQ.DEPT.CODE` | `PptnclBailiffChargeParam_DeptCode` | String |  |  |
| 27 | `PPTNCL.CQ.AUDITOR.CODE` | `PptnclBailiffChargeParam_AuditorCode` | String |  |  |
| 28 | `PPTNCL.CQ.AUDIT.DATE.TIME` | `PptnclBailiffChargeParam_AuditDateTime` | String |  |  |
