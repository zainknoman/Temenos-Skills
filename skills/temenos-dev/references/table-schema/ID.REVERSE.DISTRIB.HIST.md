# ID.REVERSE.DISTRIB.HIST — Table Schema

> Source: `INSERTS/I_F.ID.REVERSE.DISTRIB.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.RDH.REVERSAL.REF` | `IdReverseDistribHist_ReversalRef` | TField |  | This field will hold valid PDS Action Reference for which reversal is triggered Validation Rules: 1. Valid Record in ID.PDS.ACTION Record |
| 2 | `ID.RDH.START.DATE` | `IdReverseDistribHist_StartDate` | TField |  | This field will hold the value of PDS Start Date from the reversal record Validation Rules: 1. Valid Date type of field |
| 3 | `ID.RDH.END.DATE` | `IdReverseDistribHist_EndDate` | TField |  | This field will hold the value of PDS End Date from the reversal record Validation Rules: 1. Valid account no or PL category |
| 4 | `ID.RDH.NEW.ACTION.REF` | `IdReverseDistribHist_NewActionRef` | TField |  | This field will hold valid PDS Action Reference for which the new simulation/distribution is triggered as a reinitiation for the reversed action Validation Rules: 1. Valid account no or PL category |
| 5 | `ID.RDH.NEW.ACTION.DATE` | `IdReverseDistribHist_NewActionDate` | TField |  | This field will hold the value of new simulation run date Validation Rules: 1. Valid Transaction Code |
| 6 | `ID.RDH.RESERVED.5` | `IdReverseDistribHist_Reserved5` | TField |  | Reserved for future use |
| 7 | `ID.RDH.RESERVED.4` | `IdReverseDistribHist_Reserved4` | TField |  | Reserved for future use |
| 8 | `ID.RDH.RESERVED.3` | `IdReverseDistribHist_Reserved3` | TField |  | Reserved for future use |
| 9 | `ID.RDH.RESERVED.2` | `IdReverseDistribHist_Reserved2` | TField |  | Reserved for future use |
| 10 | `ID.RDH.RESERVED.1` | `IdReverseDistribHist_Reserved1` | TField |  | Reserved for future use |
