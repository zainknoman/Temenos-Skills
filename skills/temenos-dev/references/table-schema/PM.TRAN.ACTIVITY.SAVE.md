# PM.TRAN.ACTIVITY.SAVE — Table Schema

> Source: `INSERTS/I_F.PM.TRAN.ACTIVITY.SAVE` in `PM_Engine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PMS.CURRENCY.MARKET` | `PmTranActivitySave_CurrencyMarket` |  |  |  |
| 2 | `PMS.DEALER.DESK` | `PmTranActivitySave_DealerDesk` |  |  |  |
| 3 | `PMS.POSN.TYPE` | `PmTranActivitySave_PosnType` |  |  |  |
| 4 | `PMS.ASST.LIAB.CD` | `PmTranActivitySave_AsstLiabCd` |  |  |  |
| 5 | `PMS.VALUE.DATE` | `PmTranActivitySave_ValueDate` |  |  |  |
| 6 | `PMS.VALUE.DATE.SFX` | `PmTranActivitySave_ValueDateSfx` |  |  |  |
| 7 | `PMS.POSN.CLASS` | `PmTranActivitySave_PosnClass` |  |  |  |
| 8 | `PMS.CURRENCY` | `PmTranActivitySave_Currency` |  |  |  |
| 9 | `PMS.CCY.AMT` | `PmTranActivitySave_CcyAmt` |  |  |  |
| 10 | `PMS.RATE` | `PmTranActivitySave_Rate` |  |  |  |
| 11 | `PMS.INT.KEY` | `PmTranActivitySave_IntKey` |  |  |  |
| 12 | `PMS.MARGIN` | `PmTranActivitySave_Margin` |  |  |  |
| 13 | `PMS.EQUIV.CODE` | `PmTranActivitySave_EquivCode` |  |  |  |
| 14 | `PMS.EQUIV.AMT` | `PmTranActivitySave_EquivAmt` |  |  |  |
| 15 | `PMS.ACTY.PROC.CD` | `PmTranActivitySave_ActyProcCd` |  |  |  |
| 16 | `PMS.FIXED.CCY` | `PmTranActivitySave_FixedCcy` |  |  |  |
| 17 | `PMS.FIXED.AMT` | `PmTranActivitySave_FixedAmt` |  |  |  |
| 18 | `PMS.TRAN.PROC.CD` | `PmTranActivitySave_TranProcCd` |  |  |  |
| 19 | `PMS.TRAN.PROC.DETL` | `PmTranActivitySave_TranProcDetl` |  |  |  |
| 20 | `PMS.APPLICATION` | `PmTranActivitySave_Application` | TField |  |  |
| 21 | `PMS.BOOKING.DATE` | `PmTranActivitySave_BookingDate` | TField |  |  |
| 22 | `PMS.DATE.TIME` | `PmTranActivitySave_DateTime` |  |  |  |
