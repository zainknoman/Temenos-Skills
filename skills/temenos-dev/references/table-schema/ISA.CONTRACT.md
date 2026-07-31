# ISA.CONTRACT — Table Schema

> Source: `INSERTS/I_F.ISA.CONTRACT` in `UKISA1_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ISA.CON.TAX.END.DATE` | `IsaContract_TaxEndDate` | TField |  | The Tax end date of the customer |
| 2 | `ISA.CON.ISA.ARRANGEMENT` | `IsaContract_IsaArrangement` |  |  |  |
| 3 | `ISA.CON.FIRST.SUB.DATE` | `IsaContract_FirstSubDate` |  |  |  |
| 4 | `ISA.CON.ISA.SUBSCRIPTION` | `IsaContract_IsaSubscription` |  |  |  |
| 5 | `ISA.CON.LAST.SUB.DATE` | `IsaContract_LastSubDate` |  |  |  |
| 6 | `ISA.CON.ISA.WITHDRAWAL` | `IsaContract_IsaWithdrawal` |  |  |  |
| 7 | `ISA.CON.RESERVED.13` | `IsaContract_Reserved13` |  |  |  |
| 8 | `ISA.CON.TOTAL.SUBSCRIPTION` | `IsaContract_TotalSubscription` | TField |  | The total amount subscribed for the customer per year |
| 9 | `ISA.CON.TOTAL.WITHDRAWAL` | `IsaContract_TotalWithdrawal` | TField |  | The total amount withdrawn for the customer per year |
| 10 | `ISA.CON.ISA.UTIL.ALLOWANCE` | `IsaContract_IsaUtilAllowance` | TField |  | The total amount subscribed for the customer per year |
| 11 | `ISA.CON.FLEXIBLE.ALLOWANCE` | `IsaContract_FlexibleAllowance` | TField |  | This Field have the value if the customer withdraw more than the subscription amount |
| 12 | `ISA.CON.ISA.DOFS` | `IsaContract_IsaDofs` | TField |  | This Field have the first subscription date at a customer level. This field will be updated based on the earliest subscription date across arrangements held by a customer in a tax year.Any amendments made by the user in ISA.CONTRACT.ADJ will overwrite the existing values in this field. |
| 13 | `ISA.CON.SUB.ADJUSTMENT` | `IsaContract_SubAdjustment` | TField |  | This Field have the value adjusted for the allowances like subscription allowance utilized, flexible allowance, etc. |
| 14 | `ISA.CON.RESERVED.5` | `IsaContract_Reserved5` |  |  |  |
| 15 | `ISA.CON.RESERVED.4` | `IsaContract_Reserved4` | TField |  |  |
| 16 | `ISA.CON.RESERVED.3` | `IsaContract_Reserved3` | TField |  |  |
| 17 | `ISA.CON.RESERVED.2` | `IsaContract_Reserved2` | TField |  |  |
| 18 | `ISA.CON.RESERVED.1` | `IsaContract_Reserved1` | TField |  |  |
