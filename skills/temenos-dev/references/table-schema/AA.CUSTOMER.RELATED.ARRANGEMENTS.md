# AA.CUSTOMER.RELATED.ARRANGEMENTS — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER.RELATED.ARRANGEMENTS` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUS.REL.ARR.ARRANGEMENT` | `AaCustomerRelatedArrangements_Arrangement` |  |  |  |
| 2 | `AA.CUS.REL.ARR.OWNER` | `AaCustomerRelatedArrangements_Owner` |  |  |  |
| 3 | `AA.CUS.REL.ARR.RELATION.CODE` | `AaCustomerRelatedArrangements_RelationCode` |  |  |  |
| 4 | `AA.CUS.REL.ARR.START.DATE` | `AaCustomerRelatedArrangements_StartDate` |  |  |  |
| 5 | `AA.CUS.REL.ARR.END.DATE` | `AaCustomerRelatedArrangements_EndDate` |  |  |  |
| 6 | `AA.CUS.REL.ARR.RESERVED.5` | `AaCustomerRelatedArrangements_Reserved5` | TField |  | Reserved for future use. |
| 7 | `AA.CUS.REL.ARR.RESERVED.4` | `AaCustomerRelatedArrangements_Reserved4` | TField |  | Reserved for future use. |
| 8 | `AA.CUS.REL.ARR.RESERVED.3` | `AaCustomerRelatedArrangements_Reserved3` | TField |  | Reserved for future use. |
| 9 | `AA.CUS.REL.ARR.RESERVED.2` | `AaCustomerRelatedArrangements_Reserved2` | TField |  | Reserved for future use. |
| 10 | `AA.CUS.REL.ARR.RESERVED.1` | `AaCustomerRelatedArrangements_Reserved1` | TField |  | Reserved for future use. |
| 11 | `AA.CUS.REL.ARR.UNRELATED` | `AaCustomerRelatedArrangements_Unrelated` |  |  |  |
