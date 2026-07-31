# SC.NOTE.PAYOUT — Table Schema

> Source: `INSERTS/I_F.SC.NOTE.PAYOUT` in `SC_SccEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PY.DESCRIPTION` | `ScNotePayout_Description` | TField |  | This field is Description of the structured note instrument. This field defaults from SECURITY.MASTER- Description field.This field is only for information purposes. Validation Rules: NoInput Field. |
| 2 | `SC.PY.DIARY.TYPE` | `ScNotePayout_DiaryType` | TField |  | As a prerequisite to process the note payout, a DIARY.TYPE record needs to be set up to process COUPON/REDEMPTION/STOCK.CONVERSION events. The same needs to be referenced here Validation Rules: Should be a valid record in DIARY.TYPE application |
| 3 | `SC.PY.ISSUE.PRICE` | `ScNotePayout_IssuePrice` | TField |  | This is the issue price of the structured note.Value defaults from the security master ISSUE.PRICE field.Only for information purposes. Validation Rules: NoInput Field. |
| 4 | `SC.PY.STRIKE.PRICE` | `ScNotePayout_StrikePrice` |  |  |  |
| 5 | `SC.PY.UNDERLYING` | `ScNotePayout_Underlying` |  |  |  |
| 6 | `SC.PY.MATURITY.PRICE` | `ScNotePayout_MaturityPrice` |  |  |  |
| 7 | `SC.PY.CAP.PROTECTION` | `ScNotePayout_CapProtection` | TField |  | This field value will be from the security master CAP.PROTECTION field.This field is only for information purposes. Validation Rules: NoInput Field. |
| 8 | `SC.PY.CAP` | `ScNotePayout_Cap` | TField |  | This field value will be from the security master CAP field.This field is only for information purposes. Validation Rules: NoInput Field. |
| 9 | `SC.PY.PARTICIPATION.LEVEL` | `ScNotePayout_ParticipationLevel` | TField |  | This field value will be from the security master PARTICIPATION.LEVEL field.This field is only for information purposes. Validation Rules: NoInput Field. |
| 10 | `SC.PY.KNOCK.OUT.BARRIER` | `ScNotePayout_KnockOutBarrier` | TField |  |  |
| 11 | `SC.PY.REBATE` | `ScNotePayout_Rebate` | TField |  | This field value will be defaulted from the security master REBATE field.This field is only for information purposes. Validation Rules: NoInput Field. |
| 12 | `SC.PY.COUPON.RATE` | `ScNotePayout_CouponRate` | TField | Yes | Rate at which the coupon is payed out Validation Rules: Mandatory input for COUPON event. Mapped to RATE field in DIARY application |
| 13 | `SC.PY.PAYOUT.PRICE` | `ScNotePayout_PayoutPrice` | TField | Yes | The price at which the note is redeemed. if a pay out routine is defined for this instrument or SUB.ASSET.TYPE, Value can default based on routine logic or manually updated. Validation Rules: Mandatory input for REDEMPTION event.Mapped to RATE field in DIARY application |
| 14 | `SC.PY.PAYOUT.UNDERLYING` | `ScNotePayout_PayoutUnderlying` | TField | Yes | If the payout is in the form of a stock, the underlying is specified here. Validation Rules: Mandatory input for conversion event.Mapped to NEW.SEC.NO in DIARY application |
| 15 | `SC.PY.PAYOUT.UNDERLYING.PRICE` | `ScNotePayout_PayoutUnderlyingPrice` | TField | Yes | The price at which the underlying will be paid out. Validation Rules: Mandatory input for CONVERSION event. Mapped to NEW.PRICE in DIARY application |
| 16 | `SC.PY.UNDERLYING.OLD.RATIO` | `ScNotePayout_UnderlyingOldRatio` | TField | Yes | The ratio used to covert the note to the underlying stock is defined in this field along with the field UNDERLYING.NEW.RATIO. Validation Rules: Mandatory input for CONVERSION event. Mapped to OLD.RATIO in DIARY application |
| 17 | `SC.PY.UNDERLYING.NEW.RATIO` | `ScNotePayout_UnderlyingNewRatio` | TField | Yes | The ratio used to covert the note to the underlying stock is defined in this field along with the field UNDERLYING.OLD.RATIO. Validation Rules: Mandatory input for CONVERSION event. Mapped to NEW.RATIO in DIARY application |
| 18 | `SC.PY.DIARY.ID` | `ScNotePayout_DiaryId` | TField |  | Id of the DIARY created by the payout engine is updated here. Validation Rules: No Input fields. |
| 19 | `SC.PY.RESERVED.10` | `ScNotePayout_Reserved10` | TField |  |  |
| 20 | `SC.PY.RESERVED.9` | `ScNotePayout_Reserved9` | TField |  |  |
| 21 | `SC.PY.RESERVED.8` | `ScNotePayout_Reserved8` | TField |  |  |
| 22 | `SC.PY.RESERVED.7` | `ScNotePayout_Reserved7` | TField |  |  |
| 23 | `SC.PY.RESERVED.6` | `ScNotePayout_Reserved6` | TField |  |  |
| 24 | `SC.PY.RESERVED.5` | `ScNotePayout_Reserved5` | TField |  |  |
| 25 | `SC.PY.RESERVED.4` | `ScNotePayout_Reserved4` | TField |  |  |
| 26 | `SC.PY.RESERVED.3` | `ScNotePayout_Reserved3` | TField |  |  |
| 27 | `SC.PY.RESERVED.2` | `ScNotePayout_Reserved2` | TField |  |  |
| 28 | `SC.PY.RESERVED.1` | `ScNotePayout_Reserved1` | TField |  |  |
| 29 | `SC.PY.LOCAL.REF` | `ScNotePayout_LocalRef` |  |  |  |
| 30 | `SC.PY.OVERRIDE` | `ScNotePayout_Override` |  |  |  |
| 31 | `SC.PY.RECORD.STATUS` | `ScNotePayout_RecordStatus` | String |  |  |
| 32 | `SC.PY.CURR.NO` | `ScNotePayout_CurrNo` | String |  |  |
| 33 | `SC.PY.INPUTTER` | `ScNotePayout_Inputter` |  |  |  |
| 34 | `SC.PY.DATE.TIME` | `ScNotePayout_DateTime` |  |  |  |
| 35 | `SC.PY.AUTHORISER` | `ScNotePayout_Authoriser` | String |  |  |
| 36 | `SC.PY.CO.CODE` | `ScNotePayout_CoCode` | String |  |  |
| 37 | `SC.PY.DEPT.CODE` | `ScNotePayout_DeptCode` | String |  |  |
| 38 | `SC.PY.AUDITOR.CODE` | `ScNotePayout_AuditorCode` | String |  |  |
| 39 | `SC.PY.AUDIT.DATE.TIME` | `ScNotePayout_AuditDateTime` | String |  |  |
