# PARTY.RELATIONSHIP.XREF — Table Schema

> Source: `INSERTS/I_F.PARTY.RELATIONSHIP.XREF` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PRX.PARTY.ID` | `PartyRelationshipXref_PartyId` | TField |  |  |
| 2 | `ST.PRX.PARTY.TYPE` | `PartyRelationshipXref_PartyType` | TField |  |  |
| 3 | `ST.PRX.RESERVED22` | `PartyRelationshipXref_Reserved22` | TField |  |  |
| 4 | `ST.PRX.RESERVED21` | `PartyRelationshipXref_Reserved21` | TField |  |  |
| 5 | `ST.PRX.REL.PARTY.SEARCH.KEY` | `PartyRelationshipXref_RelPartySearchKey` |  |  |  |
| 6 | `ST.PRX.REL.PARTY.ID` | `PartyRelationshipXref_RelPartyId` |  |  |  |
| 7 | `ST.PRX.REL.PARTY.TYPE` | `PartyRelationshipXref_RelPartyType` |  |  |  |
| 8 | `ST.PRX.RELATION` | `PartyRelationshipXref_Relation` |  |  |  |
| 9 | `ST.PRX.PARTY.REL.ID` | `PartyRelationshipXref_PartyRelId` |  |  |  |
| 10 | `ST.PRX.OWNING.PERC` | `PartyRelationshipXref_OwningPerc` |  |  |  |
| 11 | `ST.PRX.REL.RESERVED03` | `PartyRelationshipXref_RelReserved03` | TField |  |  |
| 12 | `ST.PRX.REL.RESERVED02` | `PartyRelationshipXref_RelReserved02` | TField |  |  |
| 13 | `ST.PRX.REL.RESERVED01` | `PartyRelationshipXref_RelReserved01` | TField |  |  |
| 14 | `ST.PRX.PRIMARY` | `PartyRelationshipXref_Primary` | TField |  |  |
| 15 | `ST.PRX.ALTERNATIVE.CUST.ID` | `PartyRelationshipXref_AlternativeCustId` |  |  |  |
| 16 | `ST.PRX.ALT.PARTY.REL.ID` | `PartyRelationshipXref_AltPartyRelId` |  |  |  |
| 17 | `ST.PRX.AGGREGATE.RELATION` | `PartyRelationshipXref_AggregateRelation` |  |  |  |
| 18 | `ST.PRX.RESERVED19` | `PartyRelationshipXref_Reserved19` | TField |  |  |
| 19 | `ST.PRX.RESERVED18` | `PartyRelationshipXref_Reserved18` | TField |  |  |
| 20 | `ST.PRX.RESERVED17` | `PartyRelationshipXref_Reserved17` | TField |  |  |
| 21 | `ST.PRX.RESERVED16` | `PartyRelationshipXref_Reserved16` | TField |  |  |
| 22 | `ST.PRX.RESERVED15` | `PartyRelationshipXref_Reserved15` | TField |  |  |
| 23 | `ST.PRX.RESERVED14` | `PartyRelationshipXref_Reserved14` | TField |  |  |
| 24 | `ST.PRX.RESERVED13` | `PartyRelationshipXref_Reserved13` | TField |  |  |
| 25 | `ST.PRX.RESERVED12` | `PartyRelationshipXref_Reserved12` | TField |  |  |
| 26 | `ST.PRX.RESERVED11` | `PartyRelationshipXref_Reserved11` | TField |  |  |
| 27 | `ST.PRX.RESERVED10` | `PartyRelationshipXref_Reserved10` | TField |  |  |
| 28 | `ST.PRX.RESERVED09` | `PartyRelationshipXref_Reserved09` | TField |  |  |
| 29 | `ST.PRX.RESERVED08` | `PartyRelationshipXref_Reserved08` | TField |  |  |
| 30 | `ST.PRX.RESERVED07` | `PartyRelationshipXref_Reserved07` | TField |  |  |
| 31 | `ST.PRX.RESERVED06` | `PartyRelationshipXref_Reserved06` | TField |  |  |
| 32 | `ST.PRX.RESERVED05` | `PartyRelationshipXref_Reserved05` | TField |  |  |
| 33 | `ST.PRX.RESERVED04` | `PartyRelationshipXref_Reserved04` | TField |  |  |
| 34 | `ST.PRX.RESERVED03` | `PartyRelationshipXref_Reserved03` | TField |  |  |
| 35 | `ST.PRX.RESERVED02` | `PartyRelationshipXref_Reserved02` | TField |  |  |
| 36 | `ST.PRX.RESERVED01` | `PartyRelationshipXref_Reserved01` | TField |  |  |
