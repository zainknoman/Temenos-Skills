# NORSIC.UTILISED.SUBSIDY — Table Schema

> Source: `INSERTS/I_F.NORSIC.UTILISED.SUBSIDY` in `NORSIC_SubsidyInterestCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORUTS.LOAN.SUBSIDY.UTILISED.AMOUNT` | `NorsicUtilisedSubsidy_LoanSubsidyUtilisedAmount` | TField |  | This field will hold the subsidy utilised amount updated during the close of business. |
| 2 | `NORUTS.LOAN.SUBSIDY.AVAILABLE.AMOUNT` | `NorsicUtilisedSubsidy_LoanSubsidyAvailableAmount` | TField |  | This field will hold the subsidy available amount updated during the close of business. |
| 3 | `NORUTS.SUBSIDY.LOAN` | `NorsicUtilisedSubsidy_SubsidyLoan` | TField |  | This field will be updated by the system when the loan is a subsidy loan. When the subsidy loan gets converted to a normal loan this flag will be set to Null. |
| 4 | `NORUTS.SUBSIDY.STAIRS.DATE` | `NorsicUtilisedSubsidy_SubsidyStairsDate` | TField |  | This field will be updated by the system with the applicable stairs date based on set up done in LOAN.SUBSIDY.YEAR.UPTO field in external property class. |
| 5 | `NORUTS.LOCAL.REF` | `NorsicUtilisedSubsidy_LocalRef` |  |  |  |
| 6 | `NORUTS.EXISTING.STAIRS` | `NorsicUtilisedSubsidy_ExistingStairs` | TField |  | This field will be updated by the system during SOD stage of COB for the forward dated Interest changes. |
| 7 | `NORUTS.RESERVED.4` | `NorsicUtilisedSubsidy_Reserved4` | TField |  |  |
| 8 | `NORUTS.RESERVED.3` | `NorsicUtilisedSubsidy_Reserved3` | TField |  |  |
| 9 | `NORUTS.RESERVED.2` | `NorsicUtilisedSubsidy_Reserved2` | TField |  |  |
| 10 | `NORUTS.RESERVED.1` | `NorsicUtilisedSubsidy_Reserved1` | TField |  |  |
