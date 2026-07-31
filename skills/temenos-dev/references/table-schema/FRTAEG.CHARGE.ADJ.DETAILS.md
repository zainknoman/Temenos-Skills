# FRTAEG.CHARGE.ADJ.DETAILS — Table Schema

> Source: `INSERTS/I_F.FRTAEG.CHARGE.ADJ.DETAILS` in `FRTAEG_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHRG.DET.TOTAL.CHARGE.ADJ.AMOUNT` | `FrtaegChargeAdjDetails_TotalChargeAdjAmount` | TField |  | This field will store the reduction in charge required due to a decrease in MLR. It will be updated each time there is a change in APR due to a change in Cashflow. |
| 2 | `CHRG.DET.PENDING.AMOUNT` | `FrtaegChargeAdjDetails_PendingAmount` | TField |  | This field stores the charge amount which is yet to be adjusted. |
| 3 | `CHRG.DET.CHARGE.DUE.DATE` | `FrtaegChargeAdjDetails_ChargeDueDate` |  |  |  |
| 4 | `CHRG.DET.CHARGE.PROPERTY` | `FrtaegChargeAdjDetails_ChargeProperty` |  |  |  |
| 5 | `CHRG.DET.DUE.AMOUNT` | `FrtaegChargeAdjDetails_DueAmount` |  |  |  |
| 6 | `CHRG.DET.ADJUSTMENT.AMOUNT` | `FrtaegChargeAdjDetails_AdjustmentAmount` |  |  |  |
| 7 | `CHRG.DET.AMOUNT.ADJ.USED` | `FrtaegChargeAdjDetails_AmountAdjUsed` |  |  |  |
| 8 | `CHRG.DET.FINAL.AMOUNT.CHARGED` | `FrtaegChargeAdjDetails_FinalAmountCharged` |  |  |  |
| 9 | `CHRG.DET.ACTIVITY.ID` | `FrtaegChargeAdjDetails_ActivityId` |  |  |  |
| 10 | `CHRG.DET.ACTIVITY.DATE` | `FrtaegChargeAdjDetails_ActivityDate` |  |  |  |
