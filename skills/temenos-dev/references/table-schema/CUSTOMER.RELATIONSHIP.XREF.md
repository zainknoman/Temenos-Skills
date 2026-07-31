# CUSTOMER.RELATIONSHIP.XREF — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.RELATIONSHIP.XREF` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CRX.RELATION.TYPE` | `CustomerRelationshipXref_RelationType` |  |  |  |
| 2 | `ST.CRX.PARTY.ID` | `CustomerRelationshipXref_PartyId` |  |  |  |
| 3 | `ST.CRX.PARTY.TYPE` | `CustomerRelationshipXref_PartyType` |  |  |  |
| 4 | `ST.CRX.RESERVED10` | `CustomerRelationshipXref_Reserved10` |  |  |  |
| 5 | `ST.CRX.RESERVED09` | `CustomerRelationshipXref_Reserved09` |  |  |  |
| 6 | `ST.CRX.RESERVED08` | `CustomerRelationshipXref_Reserved08` |  |  |  |
| 7 | `ST.CRX.REL.PARTY.SEARCH.KEY` | `CustomerRelationshipXref_RelPartySearchKey` |  |  |  |
| 8 | `ST.CRX.PARTY.REL` | `CustomerRelationshipXref_PartyRel` |  |  |  |
| 9 | `ST.CRX.REL.PARTY.ID` | `CustomerRelationshipXref_RelPartyId` |  |  |  |
| 10 | `ST.CRX.REL.PARTY.TYPE` | `CustomerRelationshipXref_RelPartyType` |  |  |  |
| 11 | `ST.CRX.RELATIONSHIP` | `CustomerRelationshipXref_Relationship` |  |  |  |
| 12 | `ST.CRX.CUSTOMER.RELATIONSHIP.ID` | `CustomerRelationshipXref_CustomerRelationshipId` |  |  |  |
| 13 | `ST.CRX.RESERVED07` | `CustomerRelationshipXref_Reserved07` | TField |  |  |
| 14 | `ST.CRX.RESERVED06` | `CustomerRelationshipXref_Reserved06` | TField |  |  |
| 15 | `ST.CRX.RESERVED05` | `CustomerRelationshipXref_Reserved05` | TField |  |  |
| 16 | `ST.CRX.RESERVED04` | `CustomerRelationshipXref_Reserved04` | TField |  |  |
| 17 | `ST.CRX.RESERVED03` | `CustomerRelationshipXref_Reserved03` | TField |  |  |
| 18 | `ST.CRX.RESERVED02` | `CustomerRelationshipXref_Reserved02` | TField |  |  |
| 19 | `ST.CRX.RESERVED01` | `CustomerRelationshipXref_Reserved01` | TField |  |  |
