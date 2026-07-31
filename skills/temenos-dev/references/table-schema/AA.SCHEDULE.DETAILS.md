# AA.SCHEDULE.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.SCHEDULE.DETAILS` in `AA_PaymentSchedule.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SD.PAYMENT.DATE` | `AaScheduleDetails_PaymentDate` |  |  |  |
| 2 | `AA.SD.PAY.DATE.AMT` | `AaScheduleDetails_PayDateAmt` |  |  |  |
| 3 | `AA.SD.PAY.TYPE` | `AaScheduleDetails_PayType` |  |  |  |
| 4 | `AA.SD.PAY.METHOD` | `AaScheduleDetails_PayMethod` |  |  |  |
| 5 | `AA.SD.PAY.AMOUNT` | `AaScheduleDetails_PayAmount` |  |  |  |
| 6 | `AA.SD.OUTSTANDING.AMT` | `AaScheduleDetails_OutstandingAmt` |  |  |  |
