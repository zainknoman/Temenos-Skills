# CL.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.CL.ACTIVITY` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.ACTIV.CUSTOMER` | `ClActivity_Customer` | TField |  | This field hold the customer No who is going to repay their overdue amount's. |
| 2 | `CL.ACTIV.ACTION.CODE` | `ClActivity_ActionCode` | TField |  | This field hold the collector action's or customer action's code. Following action made by collector 1. CALLO - collector call to customer 2. CALLI - customer call to collector 3. VISIT - Field visit |
| 3 | `CL.ACTIV.OUTCOME.CODE` | `ClActivity_OutcomeCode` | TField |  | This field hold the information about what commitment is gone between collector and customer. |
| 4 | `CL.ACTIV.SRC.QUEUE` | `ClActivity_SrcQueue` | TField |  | This field hold the information about Previous queue when collector has taken action. |
| 5 | `CL.ACTIV.DEST.QUEUE` | `ClActivity_DestQueue` | TField |  | This field hold the information about current queue when collector has taken action. |
| 6 | `CL.ACTIV.COLLECTOR` | `ClActivity_Collector` | TField |  |  |
| 7 | `CL.ACTIV.OUTCOME.DUE.DATE` | `ClActivity_OutcomeDueDate` | TField |  | Commitment/Customer Response date |
| 8 | `CL.ACTIV.OUTCOME.DUE.AMT` | `ClActivity_OutcomeDueAmt` | TField |  | Commitment/Repay Amount. |
| 9 | `CL.ACTIV.NOTES` | `ClActivity_Notes` |  |  |  |
| 10 | `CL.ACTIV.ACTION.DATE` | `ClActivity_ActionDate` | TField |  | specified date when the action is taken |
| 11 | `CL.ACTIV.START.TIME` | `ClActivity_StartTime` | TField |  | Action start time |
| 12 | `CL.ACTIV.END.TIME` | `ClActivity_EndTime` | TField |  | Action End time |
| 13 | `CL.ACTIV.PAYMENT.REFERENCE` | `ClActivity_PaymentReference` | TField |  |  |
| 14 | `CL.ACTIV.RESERVED.4` | `ClActivity_Reserved4` | TField |  |  |
| 15 | `CL.ACTIV.RESERVED.3` | `ClActivity_Reserved3` | TField |  |  |
| 16 | `CL.ACTIV.RESERVED.2` | `ClActivity_Reserved2` | TField |  |  |
| 17 | `CL.ACTIV.RESERVED.1` | `ClActivity_Reserved1` | TField |  |  |
| 18 | `CL.ACTIV.OUTCOME.DUE.CCY` | `ClActivity_OutcomeDueCcy` | TField |  | Commitment/Repay Amount currency |
| 19 | `CL.ACTIV.OUTCOME.DUE.AMT.LCY` | `ClActivity_OutcomeDueAmtLcy` | TField |  | Commitment/Repay Amount in local currency. |
