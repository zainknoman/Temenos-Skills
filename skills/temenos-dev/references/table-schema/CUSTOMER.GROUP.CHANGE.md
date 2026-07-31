# CUSTOMER.GROUP.CHANGE — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.GROUP.CHANGE` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CGC.GROUP.ID` | `CustomerGroupChange_GroupId` | TField |  | This field indicates the CUSTOMER.GROUP record that has pending changes. Validation Rules: Must exist on CUSTOMER.GROUP. Value of this field cannot be changed. |
| 2 | `ST.CGC.CREATED.BY` | `CustomerGroupChange_CreatedBy` | TField |  | The ID of the PARTY.RELATIONSHIP that has been modified. Validation Rules: Value of this field cannot be changed. |
| 3 | `ST.CGC.CLOSE.GROUP` | `CustomerGroupChange_CloseGroup` | TField | No | The field determines whether the Group should be closed or not. When set to YES or SYSTEM any REMOVE or ADD amendments are ignored. Validation Rules: YES, NO ,SYSTEM or null Optional field When a deletion of a particular relation from PARTY.RELATIONSHIP results in the removal of all relations in a customer group, this field will be defaulted to SYSTEM. The user can then decide to accept the removal of relations and can amend this field suitably. |
| 4 | `ST.CGC.REMOVE.PARTY.TYPE` | `CustomerGroupChange_RemovePartyType` |  |  |  |
| 5 | `ST.CGC.REMOVE.PARTY.ID` | `CustomerGroupChange_RemovePartyId` |  |  |  |
| 6 | `ST.CGC.REMOVE.RELATION` | `CustomerGroupChange_RemoveRelation` |  |  |  |
| 7 | `ST.CGC.REMOVE.GRP.RELATION` | `CustomerGroupChange_RemoveGrpRelation` |  |  |  |
| 8 | `ST.CGC.REMOVE.REL.PARTY.TYPE` | `CustomerGroupChange_RemoveRelPartyType` |  |  |  |
| 9 | `ST.CGC.REMOVE.REL.PARTY.ID` | `CustomerGroupChange_RemoveRelPartyId` |  |  |  |
| 10 | `ST.CGC.ACCEPT.REMOVAL` | `CustomerGroupChange_AcceptRemoval` |  |  |  |
| 11 | `ST.CGC.REMOVE.NOTES` | `CustomerGroupChange_RemoveNotes` |  |  |  |
| 12 | `ST.CGC.REMOVE.OWNING.PERC` | `CustomerGroupChange_RemoveOwningPerc` |  |  |  |
| 13 | `ST.CGC.REMOVE.IMPORT.INFO` | `CustomerGroupChange_RemoveImportInfo` |  |  |  |
| 14 | `ST.CGC.REMOVE.RELATED.AS` | `CustomerGroupChange_RemoveRelatedAs` |  |  |  |
| 15 | `ST.CGC.REMOVE.COMPARE.STR` | `CustomerGroupChange_RemoveCompareStr` |  |  |  |
| 16 | `ST.CGC.RESERVED36` | `CustomerGroupChange_Reserved36` |  |  |  |
| 17 | `ST.CGC.RESERVED35` | `CustomerGroupChange_Reserved35` |  |  |  |
| 18 | `ST.CGC.RESERVED34` | `CustomerGroupChange_Reserved34` |  |  |  |
| 19 | `ST.CGC.RESERVED33` | `CustomerGroupChange_Reserved33` |  |  |  |
| 20 | `ST.CGC.RESERVED32` | `CustomerGroupChange_Reserved32` |  |  |  |
| 21 | `ST.CGC.RESERVED31` | `CustomerGroupChange_Reserved31` |  |  |  |
| 22 | `ST.CGC.ADD.PARTY.TYPE` | `CustomerGroupChange_AddPartyType` |  |  |  |
| 23 | `ST.CGC.ADD.PARTY.ID` | `CustomerGroupChange_AddPartyId` |  |  |  |
| 24 | `ST.CGC.ADD.RELATION` | `CustomerGroupChange_AddRelation` |  |  |  |
| 25 | `ST.CGC.ADD.GRP.RELATION` | `CustomerGroupChange_AddGrpRelation` |  |  |  |
| 26 | `ST.CGC.ADD.REL.PARTY.TYPE` | `CustomerGroupChange_AddRelPartyType` |  |  |  |
| 27 | `ST.CGC.ADD.REL.PARTY.ID` | `CustomerGroupChange_AddRelPartyId` |  |  |  |
| 28 | `ST.CGC.ACCEPT.ADD` | `CustomerGroupChange_AcceptAdd` |  |  |  |
| 29 | `ST.CGC.ADD.NOTES` | `CustomerGroupChange_AddNotes` |  |  |  |
| 30 | `ST.CGC.ADD.OWNING.PERC` | `CustomerGroupChange_AddOwningPerc` |  |  |  |
| 31 | `ST.CGC.ADD.IMPORT.INFO` | `CustomerGroupChange_AddImportInfo` |  |  |  |
| 32 | `ST.CGC.ADD.RELATED.AS` | `CustomerGroupChange_AddRelatedAs` |  |  |  |
| 33 | `ST.CGC.ADD.COMPARE.STR` | `CustomerGroupChange_AddCompareStr` |  |  |  |
| 34 | `ST.CGC.RESERVED26` | `CustomerGroupChange_Reserved26` |  |  |  |
| 35 | `ST.CGC.RESERVED25` | `CustomerGroupChange_Reserved25` |  |  |  |
| 36 | `ST.CGC.RESERVED24` | `CustomerGroupChange_Reserved24` |  |  |  |
| 37 | `ST.CGC.RESERVED23` | `CustomerGroupChange_Reserved23` |  |  |  |
| 38 | `ST.CGC.RESERVED22` | `CustomerGroupChange_Reserved22` |  |  |  |
| 39 | `ST.CGC.RESERVED21` | `CustomerGroupChange_Reserved21` |  |  |  |
| 40 | `ST.CGC.COMPLETE` | `CustomerGroupChange_Complete` | TField | Yes | System generated field to show that changes have been processed by service Validation Rules: YES, NO or null Mandatory field |
| 41 | `ST.CGC.ERROR.LIST` | `CustomerGroupChange_ErrorList` |  |  |  |
| 42 | `ST.CGC.RESERVED20` | `CustomerGroupChange_Reserved20` | TField |  |  |
| 43 | `ST.CGC.RESERVED19` | `CustomerGroupChange_Reserved19` | TField |  |  |
| 44 | `ST.CGC.RESERVED18` | `CustomerGroupChange_Reserved18` | TField |  |  |
| 45 | `ST.CGC.RESERVED17` | `CustomerGroupChange_Reserved17` | TField |  |  |
| 46 | `ST.CGC.RESERVED16` | `CustomerGroupChange_Reserved16` | TField |  |  |
| 47 | `ST.CGC.RESERVED15` | `CustomerGroupChange_Reserved15` | TField |  |  |
| 48 | `ST.CGC.RESERVED14` | `CustomerGroupChange_Reserved14` | TField |  |  |
| 49 | `ST.CGC.RESERVED13` | `CustomerGroupChange_Reserved13` | TField |  |  |
| 50 | `ST.CGC.RESERVED12` | `CustomerGroupChange_Reserved12` | TField |  |  |
| 51 | `ST.CGC.RESERVED11` | `CustomerGroupChange_Reserved11` | TField |  |  |
| 52 | `ST.CGC.RESERVED10` | `CustomerGroupChange_Reserved10` | TField |  |  |
| 53 | `ST.CGC.RESERVED9` | `CustomerGroupChange_Reserved9` | TField |  |  |
| 54 | `ST.CGC.RESERVED8` | `CustomerGroupChange_Reserved8` | TField |  |  |
| 55 | `ST.CGC.RESERVED7` | `CustomerGroupChange_Reserved7` | TField |  |  |
| 56 | `ST.CGC.RESERVED6` | `CustomerGroupChange_Reserved6` | TField |  |  |
| 57 | `ST.CGC.RESERVED5` | `CustomerGroupChange_Reserved5` | TField |  |  |
| 58 | `ST.CGC.RESERVED4` | `CustomerGroupChange_Reserved4` | TField |  |  |
| 59 | `ST.CGC.RESERVED3` | `CustomerGroupChange_Reserved3` | TField |  |  |
| 60 | `ST.CGC.RESERVED2` | `CustomerGroupChange_Reserved2` | TField |  |  |
| 61 | `ST.CGC.RESERVED1` | `CustomerGroupChange_Reserved1` | TField |  |  |
| 62 | `ST.CGC.LOCAL.REF` | `CustomerGroupChange_LocalRef` |  |  |  |
| 63 | `ST.CGC.OVERRIDE` | `CustomerGroupChange_Override` |  |  |  |
| 64 | `ST.CGC.RECORD.STATUS` | `CustomerGroupChange_RecordStatus` | String |  |  |
| 65 | `ST.CGC.CURR.NO` | `CustomerGroupChange_CurrNo` | String |  |  |
| 66 | `ST.CGC.INPUTTER` | `CustomerGroupChange_Inputter` |  |  |  |
| 67 | `ST.CGC.DATE.TIME` | `CustomerGroupChange_DateTime` |  |  |  |
| 68 | `ST.CGC.AUTHORISER` | `CustomerGroupChange_Authoriser` | String |  |  |
| 69 | `ST.CGC.CO.CODE` | `CustomerGroupChange_CoCode` | String |  |  |
| 70 | `ST.CGC.DEPT.CODE` | `CustomerGroupChange_DeptCode` | String |  |  |
| 71 | `ST.CGC.AUDITOR.CODE` | `CustomerGroupChange_AuditorCode` | String |  |  |
| 72 | `ST.CGC.AUDIT.DATE.TIME` | `CustomerGroupChange_AuditDateTime` | String |  |  |
