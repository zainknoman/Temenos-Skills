# POR.OTHERACCOUNTRESTRICTIONS — Table Schema

> Source: `INSERTS/I_F.POR.OTHERACCOUNTRESTRICTIONS` in `PP_DebitPartyDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPRE.AccountInfoID` | `PorOtheraccountrestrictions_Accountinfoid` |  |  |  |
| 2 | `PPPRE.OtherRestrictionType` | `PorOtheraccountrestrictions_Otherrestrictiontype` |  |  |  |
| 3 | `PPPRE.OtherRestrictionDesc` | `PorOtheraccountrestrictions_Otherrestrictiondesc` |  |  |  |
