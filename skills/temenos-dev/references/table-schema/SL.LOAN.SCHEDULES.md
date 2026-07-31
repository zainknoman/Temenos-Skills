# SL.LOAN.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.SCHEDULES` in `SL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SLLS.SCH.TYPE` | `SlLoanSchedules_SchType` |  |  |  |
| 2 | `SLLS.CHG.CODE` | `SlLoanSchedules_ChgCode` |  |  |  |
| 3 | `SLLS.CHG.CURRENCY` | `SlLoanSchedules_ChgCurrency` |  |  |  |
| 4 | `SLLS.CHG.AMOUNT` | `SlLoanSchedules_ChgAmount` |  |  |  |
| 5 | `SLLS.SCH.AMOUNT` | `SlLoanSchedules_SchAmount` |  |  |  |
| 6 | `SLLS.PART.ID` | `SlLoanSchedules_PartId` |  |  |  |
| 7 | `SLLS.PART.AMT` | `SlLoanSchedules_PartAmt` |  |  |  |
| 8 | `SLLS.PART.FAC.AMT` | `SlLoanSchedules_PartFacAmt` |  |  |  |
| 9 | `SLLS.FACI.REPAY.SCH` | `SlLoanSchedules_FaciRepaySch` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
