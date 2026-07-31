# USLEND.COUPON.SCHEDULE — Table Schema

> Source: `INSERTS/I_F.USLEND.COUPON.SCHEDULE` in `USLEND_CouponBooks.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COUPON.BOOKS.ARRANGEMENT.ID` | `UslendCouponSchedule_ArrangementId` | TField |  | Not Used |
| 2 | `COUPON.BOOKS.LOAN.ACCOUNT` | `UslendCouponSchedule_LoanAccount` | TField |  | Not Used |
| 3 | `COUPON.BOOKS.PAY.SCHEDULE.DATE` | `UslendCouponSchedule_PayScheduleDate` |  |  |  |
| 4 | `COUPON.BOOKS.PAY.SCHEDULE.AMT` | `UslendCouponSchedule_PayScheduleAmt` |  |  |  |
| 5 | `COUPON.BOOKS.LATE.PAY.CHARGE` | `UslendCouponSchedule_LatePayCharge` | TField |  | Not Used |
| 6 | `COUPON.BOOKS.TOTAL.COUPONS` | `UslendCouponSchedule_TotalCoupons` | TField |  | Not Used |
| 7 | `COUPON.BOOKS.COUPON.NUMBER` | `UslendCouponSchedule_CouponNumber` | TField |  | Not Used |
| 8 | `COUPON.BOOKS.PRINT.REQUEST.DATE` | `UslendCouponSchedule_PrintRequestDate` | TField |  | Not Used |
