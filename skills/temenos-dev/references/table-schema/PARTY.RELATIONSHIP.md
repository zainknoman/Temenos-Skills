# PARTY.RELATIONSHIP — Table Schema

> Source: `INSERTS/I_F.PARTY.RELATIONSHIP` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PR.DESCRIPTION` | `PartyRelationship_Description` |  |  |  |
| 2 | `ST.PR.PARTY.TYPE` | `PartyRelationship_PartyType` |  |  |  |
| 3 | `ST.PR.PARTY.ID` | `PartyRelationship_PartyId` |  |  |  |
| 4 | `ST.PR.RELATION.CODE` | `PartyRelationship_RelationCode` |  |  |  |
| 5 | `ST.PR.RELATED.AS` | `PartyRelationship_RelatedAs` |  |  |  |
| 6 | `ST.PR.REL.PARTY.TYPE` | `PartyRelationship_RelPartyType` |  |  |  |
| 7 | `ST.PR.REL.PARTY.ID` | `PartyRelationship_RelPartyId` |  |  |  |
| 8 | `ST.PR.OWNING.PERC` | `PartyRelationship_OwningPerc` |  |  |  |
| 9 | `ST.PR.COMMENTS` | `PartyRelationship_Comments` |  |  |  |
| 10 | `ST.PR.RESERVED21` | `PartyRelationship_Reserved21` |  |  |  |
| 11 | `ST.PR.RESERVED20` | `PartyRelationship_Reserved20` |  |  |  |
| 12 | `ST.PR.RESERVED19` | `PartyRelationship_Reserved19` |  |  |  |
| 13 | `ST.PR.RESERVED18` | `PartyRelationship_Reserved18` |  |  |  |
| 14 | `ST.PR.RESERVED17` | `PartyRelationship_Reserved17` |  |  |  |
| 15 | `ST.PR.RESERVED16` | `PartyRelationship_Reserved16` |  |  |  |
| 16 | `ST.PR.RESERVED15` | `PartyRelationship_Reserved15` |  |  |  |
| 17 | `ST.PR.AGG.CUSTOMER` | `PartyRelationship_AggCustomer` |  |  |  |
| 18 | `ST.PR.AGG.PRIME.FLAG` | `PartyRelationship_AggPrimeFlag` |  |  |  |
| 19 | `ST.PR.RESERVED14` | `PartyRelationship_Reserved14` | TField |  |  |
| 20 | `ST.PR.RESERVED13` | `PartyRelationship_Reserved13` | TField |  |  |
| 21 | `ST.PR.RESERVED12` | `PartyRelationship_Reserved12` | TField |  |  |
| 22 | `ST.PR.GROUP.ID` | `PartyRelationship_GroupId` | TField |  | ID of customer group record that created the relationship. |
| 23 | `ST.PR.RESERVED11` | `PartyRelationship_Reserved11` | TField |  |  |
| 24 | `ST.PR.RESERVED10` | `PartyRelationship_Reserved10` | TField |  |  |
| 25 | `ST.PR.RESERVED9` | `PartyRelationship_Reserved9` | TField |  |  |
| 26 | `ST.PR.RESERVED8` | `PartyRelationship_Reserved8` | TField |  |  |
| 27 | `ST.PR.RESERVED7` | `PartyRelationship_Reserved7` | TField |  |  |
| 28 | `ST.PR.RESERVED6` | `PartyRelationship_Reserved6` | TField |  |  |
| 29 | `ST.PR.RESERVED5` | `PartyRelationship_Reserved5` | TField |  |  |
| 30 | `ST.PR.RESERVED4` | `PartyRelationship_Reserved4` | TField |  |  |
| 31 | `ST.PR.RESERVED3` | `PartyRelationship_Reserved3` | TField |  |  |
| 32 | `ST.PR.RESERVED2` | `PartyRelationship_Reserved2` | TField |  |  |
| 33 | `ST.PR.RESERVED1` | `PartyRelationship_Reserved1` | TField |  |  |
| 34 | `ST.PR.LOCAL.REF` | `PartyRelationship_LocalRef` |  |  |  |
| 35 | `ST.PR.OVERRIDE` | `PartyRelationship_Override` |  |  |  |
| 36 | `ST.PR.RECORD.STATUS` | `PartyRelationship_RecordStatus` | String |  |  |
| 37 | `ST.PR.CURR.NO` | `PartyRelationship_CurrNo` | String |  |  |
| 38 | `ST.PR.INPUTTER` | `PartyRelationship_Inputter` |  |  |  |
| 39 | `ST.PR.DATE.TIME` | `PartyRelationship_DateTime` |  |  |  |
| 40 | `ST.PR.AUTHORISER` | `PartyRelationship_Authoriser` | String |  |  |
| 41 | `ST.PR.CO.CODE` | `PartyRelationship_CoCode` | String |  |  |
| 42 | `ST.PR.DEPT.CODE` | `PartyRelationship_DeptCode` | String |  |  |
| 43 | `ST.PR.AUDITOR.CODE` | `PartyRelationship_AuditorCode` | String |  |  |
| 44 | `ST.PR.AUDIT.DATE.TIME` | `PartyRelationship_AuditDateTime` | String |  |  |
