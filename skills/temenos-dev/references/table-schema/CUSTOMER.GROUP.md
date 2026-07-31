# CUSTOMER.GROUP — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.GROUP` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CG.DESCRIPTION` | `CustomerGroup_Description` |  |  |  |
| 2 | `ST.CG.GROUP.NAME` | `CustomerGroup_GroupName` |  |  |  |
| 3 | `ST.CG.GROUP.PURPOSE` | `CustomerGroup_GroupPurpose` | TField | Yes | The Group Purpose record that will contain rules about where the customer group can be used, and how customers and parties in the group can be stored. It must be a valid code on the CUST.GROUP.PURPOSE table Validation Rules: Mandatory Input. Maximum of 15 alphanumeric characters. |
| 4 | `ST.CG.GROUP.TYPE` | `CustomerGroup_GroupType` | TField |  | The Group Type field represents the type of the group for which additional subset of rules that may be defined in the table CUST.GROUP.PURPOSE. Input must have an existing record on EB.LOOKUP table.TYPE Validation Rules: Maximum of 9 alphanumeric characters. |
| 5 | `ST.CG.COMPANY.CD` | `CustomerGroup_CompanyCd` | TField |  | Name of the company. Allows the Branch/Company code to be defined for the main customer. Validation Rules: Maximum of 9 alphanumeric characters. |
| 6 | `ST.CG.ACCOUNT.OFFICER` | `CustomerGroup_AccountOfficer` | TField |  | Allocate the officer that is responsible for the Customer Group. This may be used where there is no Multi-Company structure or within a company to identify the owner or owning department Validation Rules: Maximum of 6 alphanumeric characters. Must exist in the DEPT.ACCT.OFFICER |
| 7 | `ST.CG.ALTERNATE.ID` | `CustomerGroup_AlternateId` | TField |  | Alternate Id of the Customer Group Hierarchy Validation Rules: Maximum of 15 alphanumeric characters. |
| 8 | `ST.CG.CLOSURE.DATE` | `CustomerGroup_ClosureDate` | TField |  | This will allow the customer group to be closed on a specified date Validation Rules: Date field. Must be the current system date or in the future. Overrides will be raised online if the customer group is not eligible for closure with respect to the current system date The actual closure process happens in the CUST.GRP.CLOSURE service |
| 9 | `ST.CG.PARTY.TYPE` | `CustomerGroup_PartyType` |  |  |  |
| 10 | `ST.CG.CUSTOMER.ID` | `CustomerGroup_CustomerId` |  |  |  |
| 11 | `ST.CG.IMPORT.RELATION` | `CustomerGroup_ImportRelation` |  |  |  |
| 12 | `ST.CG.RELATIONSHIP` | `CustomerGroup_Relationship` |  |  |  |
| 13 | `ST.CG.RELATED.AS` | `CustomerGroup_RelatedAs` |  |  |  |
| 14 | `ST.CG.GROUP.RELATION` | `CustomerGroup_GroupRelation` |  |  |  |
| 15 | `ST.CG.REL.PARTY.TYPE` | `CustomerGroup_RelPartyType` |  |  |  |
| 16 | `ST.CG.REL.PARTY.ID` | `CustomerGroup_RelPartyId` |  |  |  |
| 17 | `ST.CG.OWNING.PERC` | `CustomerGroup_OwningPerc` |  |  |  |
| 18 | `ST.CG.START.DATE` | `CustomerGroup_StartDate` |  |  |  |
| 19 | `ST.CG.EXCLUDE.PARTY` | `CustomerGroup_ExcludeParty` |  |  |  |
| 20 | `ST.CG.INVALID.EDIT.CHECK` | `CustomerGroup_InvalidEditCheck` |  |  |  |
| 21 | `ST.CG.RESERVED.34` | `CustomerGroup_Reserved34` |  |  |  |
| 22 | `ST.CG.EXPANDED` | `CustomerGroup_Expanded` |  |  |  |
| 23 | `ST.CG.RESERVED.32` | `CustomerGroup_Reserved32` | TField |  |  |
| 24 | `ST.CG.RESERVED.31` | `CustomerGroup_Reserved31` | TField |  |  |
| 25 | `ST.CG.SUB.GROUP.ID` | `CustomerGroup_SubGroupId` |  |  |  |
| 26 | `ST.CG.SG.NAME` | `CustomerGroup_SgName` |  |  |  |
| 27 | `ST.CG.SG.COMPANY.CD` | `CustomerGroup_SgCompanyCd` |  |  |  |
| 28 | `ST.CG.SG.ACCOUNT.OFFICER` | `CustomerGroup_SgAccountOfficer` |  |  |  |
| 29 | `ST.CG.SG.ALTERNATE.ID` | `CustomerGroup_SgAlternateId` |  |  |  |
| 30 | `ST.CG.SG.PARTY.TYPE` | `CustomerGroup_SgPartyType` |  |  |  |
| 31 | `ST.CG.RESERVED.24` | `CustomerGroup_Reserved24` |  |  |  |
| 32 | `ST.CG.RESERVED.23` | `CustomerGroup_Reserved23` |  |  |  |
| 33 | `ST.CG.SG.PARTY.ID` | `CustomerGroup_SgPartyId` |  |  |  |
| 34 | `ST.CG.RESERVED.21` | `CustomerGroup_Reserved21` | TField |  |  |
| 35 | `ST.CG.RESERVED.20` | `CustomerGroup_Reserved20` | TField |  |  |
| 36 | `ST.CG.CLOSURE.ERR` | `CustomerGroup_ClosureErr` |  |  |  |
| 37 | `ST.CG.PRIME.PARTY.TYPE` | `CustomerGroup_PrimePartyType` |  |  |  |
| 38 | `ST.CG.PRIME.CUST.ID` | `CustomerGroup_PrimeCustId` |  |  |  |
| 39 | `ST.CG.LIABILITY.CUSTOMER` | `CustomerGroup_LiabilityCustomer` | TField |  |  |
| 40 | `ST.CG.RESERVED.15` | `CustomerGroup_Reserved15` | TField |  |  |
| 41 | `ST.CG.RESERVED.14` | `CustomerGroup_Reserved14` | TField |  |  |
| 42 | `ST.CG.RESERVED.13` | `CustomerGroup_Reserved13` | TField |  |  |
| 43 | `ST.CG.RESERVED.12` | `CustomerGroup_Reserved12` | TField |  |  |
| 44 | `ST.CG.RESERVED.11` | `CustomerGroup_Reserved11` | TField |  |  |
| 45 | `ST.CG.RESERVED.10` | `CustomerGroup_Reserved10` | TField |  |  |
| 46 | `ST.CG.RESERVED.9` | `CustomerGroup_Reserved9` | TField |  |  |
| 47 | `ST.CG.RESERVED.8` | `CustomerGroup_Reserved8` | TField |  |  |
| 48 | `ST.CG.RESERVED.7` | `CustomerGroup_Reserved7` | TField |  |  |
| 49 | `ST.CG.RESERVED.6` | `CustomerGroup_Reserved6` | TField |  |  |
| 50 | `ST.CG.RESERVED.5` | `CustomerGroup_Reserved5` | TField |  |  |
| 51 | `ST.CG.RESERVED.4` | `CustomerGroup_Reserved4` | TField |  |  |
| 52 | `ST.CG.RESERVED.3` | `CustomerGroup_Reserved3` | TField |  |  |
| 53 | `ST.CG.RESERVED.2` | `CustomerGroup_Reserved2` | TField |  |  |
| 54 | `ST.CG.RESERVED.1` | `CustomerGroup_Reserved1` | TField |  |  |
| 55 | `ST.CG.LOCAL.REF` | `CustomerGroup_LocalRef` |  |  |  |
| 56 | `ST.CG.OVERRIDE` | `CustomerGroup_Override` |  |  |  |
| 57 | `ST.CG.RECORD.STATUS` | `CustomerGroup_RecordStatus` | String |  |  |
| 58 | `ST.CG.CURR.NO` | `CustomerGroup_CurrNo` | String |  |  |
| 59 | `ST.CG.INPUTTER` | `CustomerGroup_Inputter` |  |  |  |
| 60 | `ST.CG.DATE.TIME` | `CustomerGroup_DateTime` |  |  |  |
| 61 | `ST.CG.AUTHORISER` | `CustomerGroup_Authoriser` | String |  |  |
| 62 | `ST.CG.CO.CODE` | `CustomerGroup_CoCode` | String |  |  |
| 63 | `ST.CG.DEPT.CODE` | `CustomerGroup_DeptCode` | String |  |  |
| 64 | `ST.CG.AUDITOR.CODE` | `CustomerGroup_AuditorCode` | String |  |  |
| 65 | `ST.CG.AUDIT.DATE.TIME` | `CustomerGroup_AuditDateTime` | String |  |  |
