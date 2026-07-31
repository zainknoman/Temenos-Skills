# MD.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.MD.SCHEDULES` in `MD_Schedules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.SCH.CHARGE.SCH` | `MdSchedules_ChargeSch` | TField |  | In the event of a Charge to be collected at a future date (as listed in the ID), the same is scheduled with the date being appended to the Deal ID. Validation Rules: System Maintained. |
| 2 | `MD.SCH.CHARGE.ADVICE` | `MdSchedules_ChargeAdvice` | TField |  | field is not used. |
| 3 | `MD.SCH.PRINCIPAL.SCH` | `MdSchedules_PrincipalSch` | TField |  | Represents the Principal movement for the Deal on the date (as displayed in the ID). Validation Rules: System Maintained. |
| 4 | `MD.SCH.MATURITY.SCH` | `MdSchedules_MaturitySch` | TField |  | As detailed in the ID, this represents the date on which the Deal is set to Mature. The value is populated only when AUTO.EXPIRY is set to YES in the Deal. Validation Rules: System Maintained. |
| 5 | `MD.SCH.COMMISSION.SCH` | `MdSchedules_CommissionSch` | TField |  | As detailed in the ID, this is the commission schedule representing the date on which the next commission accounting is to be carried out, be it Manual or Frequency, Begin or End, for the referred Deal. Validation Rules: System Maintained. |
| 6 | `MD.SCH.PROV.REL.SCH` | `MdSchedules_ProvRelSch` | TField |  | As indicated by the ID, this schedule is set for the Deal on the date, representing release of Provision (Cash Margin). Validation Rules: System Maintained. |
| 7 | `MD.SCH.RATE.CHG.SCH` | `MdSchedules_RateChgSch` | TField |  | As indicated by the ID, this schedule is set for the Deal on the date, representing Rate change. Validation Rules: System Maintained. |
| 8 | `MD.SCH.ADV.EXP.SCH` | `MdSchedules_AdvExpSch` | TField |  | Flag to change the status of the contract from 'CUR' to 'EXP' on the expiry date. |
