# RELATION — Table Schema

> Source: `INSERTS/I_F.RELATION` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.REL.DESCRIPTION` | `Relation_Description` |  |  |  |
| 2 | `EB.REL.REVERSE.RELATION` | `Relation_ReverseRelation` |  |  |  |
| 3 | `EB.REL.REV.REL.DESC` | `Relation_RevRelDesc` |  |  |  |
| 4 | `EB.REL.RESERVED.15` | `Relation_Reserved15` | TField |  |  |
| 5 | `EB.REL.RESERVED.14` | `Relation_Reserved14` | TField |  |  |
| 6 | `EB.REL.RESERVED.13` | `Relation_Reserved13` | TField |  |  |
| 7 | `EB.REL.RESERVED.12` | `Relation_Reserved12` | TField |  |  |
| 8 | `EB.REL.RESERVED.11` | `Relation_Reserved11` | TField |  |  |
| 9 | `EB.REL.GROUP.RELATION` | `Relation_GroupRelation` | TField | No | Indicates if set to YES that the relation code defined is a Group Relation Type. Validation Rules: Values allowed are Yes,No,null (Optional - Default value is null. For later validations YES or NO must be entered to use CHILD/PARENT/OTHER.ALLOWED). When YES, cannot use OTHER.ALLOWED in conjunction with either of CHILD.ALLOWED or PARENT.ALLOWED. When NO, only one of CHILD/PARENT/OTHER.ALLOWED can be selected. |
| 10 | `EB.REL.GROUP.RELATIONSHIP` | `Relation_GroupRelationship` |  |  |  |
| 11 | `EB.REL.OWNERSHIP` | `Relation_Ownership` | TField | No | Indicates that the relationship is an ownership type and a percentage of ownership is allowed to be specified when used to define relationships, groups and hierarchies. Validation Rules: Values allowed are Yes,No,null (Optional - Default value is null that evaluates to No). |
| 12 | `EB.REL.CHILD.ALLOWED` | `Relation_ChildAllowed` | TField | No | Indicates when set to YES, this relation is the child of a parent / child relationship as a child of another relation between corporate customers. Validation Rules: Values allowed are Yes,No,null (Optional - Default value is null that evaluates to No). Only one of CHILD/PARENT/OTHER.ALLOWED can be selected when not a GROUP.RELATION record. |
| 13 | `EB.REL.PARENT.ALLOWED` | `Relation_ParentAllowed` | TField | No | Indicates when set to YES, this relation is the parent of a parent / child relationship as a parent of another relation between corporate customers. Validation Rules: Values allowed are Yes,No,null (Optional - Default value is null that evaluates to No). Only one of CHILD/PARENT/OTHER.ALLOWED can be selected when not a GROUP.RELATION record. |
| 14 | `EB.REL.OTHER.ALLOWED` | `Relation_OtherAllowed` | TField | No | Indicates when set to YES, this relation is not a parent / child relationship type. It will be used for relationships between individual customers. Validation Rules: Values allowed are Yes,No,null (Optional - Default value is null that evaluates to No). Only one of CHILD/PARENT/OTHER.ALLOWED can be selected when not a GROUP.RELATION record. |
| 15 | `EB.REL.SECTOR` | `Relation_Sector` |  |  |  |
| 16 | `EB.REL.AGGREGATE` | `Relation_Aggregate` | TField | No | Indicates when set to YES, that a customer that has this Relation code assigned should be aggregated under a primary customer record. Validation Rules: Values allowed are Yes,No,null. Cannot be YES if GROUP.RELATION is YES. (Optional - Default value is null that evaluates to No). |
| 17 | `EB.REL.GROUP.REL.CODE` | `Relation_GroupRelCode` |  |  |  |
| 18 | `EB.REL.LOCAL.REF` | `Relation_LocalRef` |  |  |  |
| 19 | `EB.REL.RESERVED.10` | `Relation_Reserved10` | TField |  |  |
| 20 | `EB.REL.RESERVED.09` | `Relation_Reserved09` | TField |  |  |
| 21 | `EB.REL.RESERVED.08` | `Relation_Reserved08` | TField |  |  |
| 22 | `EB.REL.RESERVED.07` | `Relation_Reserved07` | TField |  |  |
| 23 | `EB.REL.RESERVED.06` | `Relation_Reserved06` | TField |  |  |
| 24 | `EB.REL.RESERVED.05` | `Relation_Reserved05` | TField |  |  |
| 25 | `EB.REL.RESERVED.04` | `Relation_Reserved04` | TField |  |  |
| 26 | `EB.REL.RESERVED.03` | `Relation_Reserved03` | TField |  |  |
| 27 | `EB.REL.RESERVED.02` | `Relation_Reserved02` | TField |  |  |
| 28 | `EB.REL.RESERVED.01` | `Relation_Reserved01` | TField |  |  |
| 29 | `EB.REL.RECORD.STATUS` | `Relation_RecordStatus` | String |  |  |
| 30 | `EB.REL.CURR.NO` | `Relation_CurrNo` | String |  |  |
| 31 | `EB.REL.INPUTTER` | `Relation_Inputter` |  |  |  |
| 32 | `EB.REL.DATE.TIME` | `Relation_DateTime` |  |  |  |
| 33 | `EB.REL.AUTHORISER` | `Relation_Authoriser` | String |  |  |
| 34 | `EB.REL.CO.CODE` | `Relation_CoCode` | String |  |  |
| 35 | `EB.REL.DEPT.CODE` | `Relation_DeptCode` | String |  |  |
| 36 | `EB.REL.AUDITOR.CODE` | `Relation_AuditorCode` | String |  |  |
| 37 | `EB.REL.AUDIT.DATE.TIME` | `Relation_AuditDateTime` | String |  |  |
