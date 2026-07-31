# CUST.GROUP.PURPOSE — Table Schema

> Source: `INSERTS/I_F.CUST.GROUP.PURPOSE` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CGP.DESCRIPTION` | `CustGroupPurpose_Description` |  |  |  |
| 2 | `ST.CGP.SYSTEM.USE` | `CustGroupPurpose_SystemUse` | TField | No | This field is used to indicate whether the Bank is going to use the Customer Group specifically for risk or not. Validation Rules: Optional Input. Valid values are RISK or null. There can only be ONE purpose type of RISK defined at any given time. Value of this field cannot be changed after authorisation. |
| 3 | `ST.CGP.UNIQUE.CUSTOMER` | `CustGroupPurpose_UniqueCustomer` | TField | Yes | This field is used to indicate whether the Customer Group with this purpose will allow its customers to be part of the other Customer Groups or not. Customers in a Customer Group with Purpose having UNIQUE.CUSTOMER set to YES, can be present in other groups where Purpose have UNIQUE.CUSTOMER has NO. Validation Rules: Mandatory Input. Valid values are YES_NO When the SYSTEM.USE is set to RISK, the value in this field has to be YES since Limit cannot accept customers in multiple groups. |
| 4 | `ST.CGP.UPD.GRP.RELATION` | `CustGroupPurpose_UpdGrpRelation` | TField | Yes | This field is used to indicate whether Group Relations have to be defaulted in Customer Group from PARTY.RELATIONSHIP.XREF. When set to YES, system will automatically convert the real life relation and create a new technical relationship between two customers into Customer Group record based on the mapping of Group Relationship. When set to NO, system will not do any automatic upload and will not allow any manual input for the Group Relation field under CUSTOMER.GROUP record. Validation Rules: Mandatory Input. Valid values are YES_NO |
| 5 | `ST.CGP.UPD.RELATION` | `CustGroupPurpose_UpdRelation` | TField | Yes | This field is used to indicate whether Real Relations have to be defaulted in Customer Group from PARTY.RELATIONSHIP.XREF. When set to YES, system will automatically upload the Relation field under CUSTOMER.GROUP record based on predefined Party Relationships. When set to NO, system will not do any automatic upload and will not allow any manual input for the Relation field under CUSTOMER.GROUP record. Validation Rules: Mandatory Input. Valid values are YES_NO |
| 6 | `ST.CGP.CUST.SUB.GROUP` | `CustGroupPurpose_CustSubGroup` | TField | No | This field is used to setup whether a Customer is allowed to part of multiple sub-groups or not. When set to &quot;UNIQUE&quot; a customer can be part of only one sub-group. When set to &quot;MULTIPLE&quot; system will allow a customer to be part of multiple sub-groups. When set to &quot;NONE&quot; system will not allow any sub group to be defined. Validation Rules: Optional input. Valid values are UNIQUE_MULTIPLE_NONE If the field is left blank, then the value NONE will get defaulted. |
| 7 | `ST.CGP.GROUP.TYPE` | `CustGroupPurpose_GroupType` |  |  |  |
| 8 | `ST.CGP.ALLOW.RELATION` | `CustGroupPurpose_AllowRelation` |  |  |  |
| 9 | `ST.CGP.ALLOW.GRP.RELATION` | `CustGroupPurpose_AllowGrpRelation` |  |  |  |
| 10 | `ST.CGP.ALLOW.CUST.TYPE` | `CustGroupPurpose_AllowCustType` |  |  |  |
| 11 | `ST.CGP.ALL.PERS.ENT.STATUS` | `CustGroupPurpose_AllPersEntStatus` |  |  |  |
| 12 | `ST.CGP.SECTOR` | `CustGroupPurpose_Sector` |  |  |  |
| 13 | `ST.CGP.VALIDATION.RTN` | `CustGroupPurpose_ValidationRtn` |  |  |  |
| 14 | `ST.CGP.AGGREGATED.RELATION` | `CustGroupPurpose_AggregatedRelation` |  |  |  |
| 15 | `ST.CGP.RESERVED14` | `CustGroupPurpose_Reserved14` |  |  |  |
| 16 | `ST.CGP.RESERVED13` | `CustGroupPurpose_Reserved13` |  |  |  |
| 17 | `ST.CGP.RESERVED12` | `CustGroupPurpose_Reserved12` |  |  |  |
| 18 | `ST.CGP.RESERVED11` | `CustGroupPurpose_Reserved11` |  |  |  |
| 19 | `ST.CGP.AUTO.RELATION.LINK` | `CustGroupPurpose_AutoRelationLink` | TField |  | Field for future use. |
| 20 | `ST.CGP.RESERVED10` | `CustGroupPurpose_Reserved10` | TField |  |  |
| 21 | `ST.CGP.RESERVED9` | `CustGroupPurpose_Reserved9` | TField |  |  |
| 22 | `ST.CGP.RESERVED8` | `CustGroupPurpose_Reserved8` | TField |  |  |
| 23 | `ST.CGP.RESERVED7` | `CustGroupPurpose_Reserved7` | TField |  |  |
| 24 | `ST.CGP.RESERVED6` | `CustGroupPurpose_Reserved6` | TField |  |  |
| 25 | `ST.CGP.RESERVED5` | `CustGroupPurpose_Reserved5` | TField |  |  |
| 26 | `ST.CGP.RESERVED4` | `CustGroupPurpose_Reserved4` | TField |  |  |
| 27 | `ST.CGP.RESERVED3` | `CustGroupPurpose_Reserved3` | TField |  |  |
| 28 | `ST.CGP.RESERVED2` | `CustGroupPurpose_Reserved2` | TField |  |  |
| 29 | `ST.CGP.RESERVED1` | `CustGroupPurpose_Reserved1` | TField |  |  |
| 30 | `ST.CGP.LOCAL.REF` | `CustGroupPurpose_LocalRef` |  |  |  |
| 31 | `ST.CGP.OVERRIDE` | `CustGroupPurpose_Override` |  |  |  |
| 32 | `ST.CGP.RECORD.STATUS` | `CustGroupPurpose_RecordStatus` | String |  |  |
| 33 | `ST.CGP.CURR.NO` | `CustGroupPurpose_CurrNo` | String |  |  |
| 34 | `ST.CGP.INPUTTER` | `CustGroupPurpose_Inputter` |  |  |  |
| 35 | `ST.CGP.DATE.TIME` | `CustGroupPurpose_DateTime` |  |  |  |
| 36 | `ST.CGP.AUTHORISER` | `CustGroupPurpose_Authoriser` | String |  |  |
| 37 | `ST.CGP.CO.CODE` | `CustGroupPurpose_CoCode` | String |  |  |
| 38 | `ST.CGP.DEPT.CODE` | `CustGroupPurpose_DeptCode` | String |  |  |
| 39 | `ST.CGP.AUDITOR.CODE` | `CustGroupPurpose_AuditorCode` | String |  |  |
| 40 | `ST.CGP.AUDIT.DATE.TIME` | `CustGroupPurpose_AuditDateTime` | String |  |  |
