# CUSTOMER.RELATIONSHIP — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.RELATIONSHIP` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.REL.GROUP.ID` | `CustomerRelationship_GroupId` | TField |  | Identifies the key to CUSTOMER.REL.GROUP record to form a relation. Validation Rules: Valid record in CUSTOMER.REL.GROUP. |
| 2 | `CUS.REL.GROUP.NAME` | `CustomerRelationship_GroupName` | TField | No | This field will contain the is of a CUSTOMER.REL.GROUP if applicable to the relationship. Validation rules 1 to 15 any characters Must be a Valid record on the CUSTOMER.REL.GROUP Optional Input |
| 3 | `CUS.REL.REFERENCE.NO` | `CustomerRelationship_ReferenceNo` | TField | No | This field is used to a reference number if required. Validation rules 1 to 35 any characters Optional input |
| 4 | `CUS.REL.ORIG.RELATION` | `CustomerRelationship_OrigRelation` |  |  |  |
| 5 | `CUS.REL.ORIG.PARTY` | `CustomerRelationship_OrigParty` |  |  |  |
| 6 | `CUS.REL.ORIG.PARTY.ID` | `CustomerRelationship_OrigPartyId` |  |  |  |
| 7 | `CUS.REL.ORIG.OWNING.PER` | `CustomerRelationship_OrigOwningPer` |  |  |  |
| 8 | `CUS.REL.ORIG.REL` | `CustomerRelationship_OrigRel` |  |  |  |
| 9 | `CUS.REL.ORIG.ROLE` | `CustomerRelationship_OrigRole` |  |  |  |
| 10 | `CUS.REL.ORIG.EFF.DATE` | `CustomerRelationship_OrigEffDate` |  |  |  |
| 11 | `CUS.REL.ORIG.RES.BRANCH` | `CustomerRelationship_OrigResBranch` |  |  |  |
| 12 | `CUS.REL.ORIG.RES.DEPT` | `CustomerRelationship_OrigResDept` |  |  |  |
| 13 | `CUS.REL.REL.RELATION` | `CustomerRelationship_RelRelation` |  |  |  |
| 14 | `CUS.REL.REL.PARTY` | `CustomerRelationship_RelParty` |  |  |  |
| 15 | `CUS.REL.REL.PARTY.ID` | `CustomerRelationship_RelPartyId` |  |  |  |
| 16 | `CUS.REL.RELATION` | `CustomerRelationship_Relation` |  |  |  |
| 17 | `CUS.REL.ROLE` | `CustomerRelationship_Role` |  |  |  |
| 18 | `CUS.REL.REL.EFF.DATE` | `CustomerRelationship_RelEffDate` |  |  |  |
| 19 | `CUS.REL.RES.BRANCH` | `CustomerRelationship_ResBranch` |  |  |  |
| 20 | `CUS.REL.RES.DEPT` | `CustomerRelationship_ResDept` |  |  |  |
| 21 | `CUS.REL.OWNING.PER` | `CustomerRelationship_OwningPer` |  |  |  |
| 22 | `CUS.REL.LOCAL.REF` | `CustomerRelationship_LocalRef` |  |  |  |
| 23 | `CUS.REL.RELATION.MNE` | `CustomerRelationship_RelationMne` | TField | No | An alternative code for easy means of referencing the customer relationship Validation rules Alphanumeric character allowed Maximum of 15 alphanumeric chars is allowed Optional input |
| 24 | `CUS.REL.RELATION.TYPE` | `CustomerRelationship_RelationType` | TField |  | To state the purpose of the relationship between two or more customers defined in CUSTOMER.RELATIONSHIP record Validation rules Valid inputs are TAX, LIMIT or ADVICES or OTHERS or can be left blank Customer to Customer - This is mainly financial in nature. For eg. Tax splits, Limit exposures, etc. Customer to person/entity - This is mainly non-financial in nature. For eg. 'Advices' which is sent normally to the solicitor, accountant, etc. |
| 25 | `CUS.REL.AMENDMENT.REASON` | `CustomerRelationship_AmendmentReason` | TField | No | To specify a reason for changing the relationship record some of the examples could be New partnership End partnership Divorce Demise Validation rules This is a free text Upto 35 alphanumeric characters allowed Optional input |
| 26 | `CUS.REL.RESERVED.12` | `CustomerRelationship_Reserved12` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 27 | `CUS.REL.RESERVED.11` | `CustomerRelationship_Reserved11` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 28 | `CUS.REL.RESERVED.10` | `CustomerRelationship_Reserved10` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 29 | `CUS.REL.RESERVED.9` | `CustomerRelationship_Reserved9` | TField |  |  |
| 30 | `CUS.REL.RESERVED.8` | `CustomerRelationship_Reserved8` | TField |  |  |
| 31 | `CUS.REL.RESERVED.7` | `CustomerRelationship_Reserved7` | TField |  |  |
| 32 | `CUS.REL.RESERVED.6` | `CustomerRelationship_Reserved6` | TField |  |  |
| 33 | `CUS.REL.RESERVED.5` | `CustomerRelationship_Reserved5` | TField |  |  |
| 34 | `CUS.REL.RESERVED.4` | `CustomerRelationship_Reserved4` | TField |  |  |
| 35 | `CUS.REL.RESERVED.3` | `CustomerRelationship_Reserved3` | TField |  |  |
| 36 | `CUS.REL.RESERVED.2` | `CustomerRelationship_Reserved2` | TField |  |  |
| 37 | `CUS.REL.OVERRIDE` | `CustomerRelationship_Override` |  |  |  |
| 38 | `CUS.REL.RECORD.STATUS` | `CustomerRelationship_RecordStatus` | String |  |  |
| 39 | `CUS.REL.CURR.NO` | `CustomerRelationship_CurrNo` | String |  |  |
| 40 | `CUS.REL.INPUTTER` | `CustomerRelationship_Inputter` |  |  |  |
| 41 | `CUS.REL.DATE.TIME` | `CustomerRelationship_DateTime` |  |  |  |
| 42 | `CUS.REL.AUTHORISER` | `CustomerRelationship_Authoriser` | String |  |  |
| 43 | `CUS.REL.CO.CODE` | `CustomerRelationship_CoCode` | String |  |  |
| 44 | `CUS.REL.DEPT.CODE` | `CustomerRelationship_DeptCode` | String |  |  |
| 45 | `CUS.REL.AUDITOR.CODE` | `CustomerRelationship_AuditorCode` | String |  |  |
| 46 | `CUS.REL.AUDIT.DATE.TIME` | `CustomerRelationship_AuditDateTime` | String |  |  |
