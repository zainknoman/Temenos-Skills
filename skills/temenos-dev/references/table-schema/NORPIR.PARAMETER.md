# NORPIR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NORPIR.PARAMETER` in `NORPIR_PeriodicRateReset.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORPIR.SPOT.RATE.DAYS.NO` | `NorpirParameter_SpotRateDaysNo` | TField |  | The number of business days for applying the spot rate for the region. |
| 2 | `NORPIR.APPLY.SPOT.RATE` | `NorpirParameter_ApplySpotRate` | TField |  | Yes/No field indicating whether to apply spot rate or not. If Yes, then apply the spot rate with in the spot days. If No, then apply the spot rate whenever the interest update happens. |
| 3 | `NORPIR.MAINTAIN.FIRST.DISBURSE.RATE` | `NorpirParameter_MaintainFirstDisburseRate` | TField |  | Yes/No field indicating whether to maintain rate from first disbursement for subsequent disbursements. If Yes, then the loan contracts for the region will be maintained by the 1st disbursement interest rate until the periodic reset/change interest happens. If periodic reset/change interest happens then that is the interest rate will be maintained during the subsequent disbursements. If No, then system does not maintain the 1st disbursement interest rate |
| 4 | `NORPIR.PRODUCT` | `NorpirParameter_Product` |  |  |  |
| 5 | `NORPIR.INTEREST.PROPERTY` | `NorpirParameter_InterestProperty` |  |  |  |
| 6 | `NORPIR.RESERVED.10` | `NorpirParameter_Reserved10` | TField |  | Reserved for future use |
| 7 | `NORPIR.RESERVED.9` | `NorpirParameter_Reserved9` | TField |  | Reserved for future use |
| 8 | `NORPIR.RESERVED.8` | `NorpirParameter_Reserved8` | TField |  | Reserved for future use |
| 9 | `NORPIR.RESERVED.7` | `NorpirParameter_Reserved7` | TField |  | Reserved for future use |
| 10 | `NORPIR.RESERVED.6` | `NorpirParameter_Reserved6` | TField |  | Reserved for future use |
| 11 | `NORPIR.RESERVED.5` | `NorpirParameter_Reserved5` | TField |  | Reserved for future use |
| 12 | `NORPIR.RESERVED.4` | `NorpirParameter_Reserved4` | TField |  | Reserved for future use |
| 13 | `NORPIR.RESERVED.3` | `NorpirParameter_Reserved3` | TField |  | Reserved for future use |
| 14 | `NORPIR.RESERVED.2` | `NorpirParameter_Reserved2` | TField |  | Reserved for future use |
| 15 | `NORPIR.RESERVED.1` | `NorpirParameter_Reserved1` | TField |  | Reserved for future use |
| 16 | `NORPIR.LOCAL.REF` | `NorpirParameter_LocalRef` |  |  |  |
| 17 | `NORPIR.OVERRIDE` | `NorpirParameter_Override` |  |  |  |
| 18 | `NORPIR.RECORD.STATUS` | `NorpirParameter_RecordStatus` | String |  |  |
| 19 | `NORPIR.CURR.NO` | `NorpirParameter_CurrNo` | String |  |  |
| 20 | `NORPIR.INPUTTER` | `NorpirParameter_Inputter` |  |  |  |
| 21 | `NORPIR.DATE.TIME` | `NorpirParameter_DateTime` |  |  |  |
| 22 | `NORPIR.AUTHORISER` | `NorpirParameter_Authoriser` | String |  |  |
| 23 | `NORPIR.CO.CODE` | `NorpirParameter_CoCode` | String |  |  |
| 24 | `NORPIR.DEPT.CODE` | `NorpirParameter_DeptCode` | String |  |  |
| 25 | `NORPIR.AUDITOR.CODE` | `NorpirParameter_AuditorCode` | String |  |  |
| 26 | `NORPIR.AUDIT.DATE.TIME` | `NorpirParameter_AuditDateTime` | String |  |  |
