# CAREGS.CDIC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.PARAMETER` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.PRM.DESCRIPTION` | `CaregsCdicParameter_Description` | TField |  | Field to store the description/purpose of the table. |
| 2 | `CDIC.PRM.EXCLUDE.ACCOUNT.STATUS` | `CaregsCdicParameter_ExcludeAccountStatus` |  |  |  |
| 3 | `CDIC.PRM.FEDERAL.START.DATE` | `CaregsCdicParameter_FederalStartDate` | TField |  | Purpose of the field to indicate the date from which FI moved from BC to Federal Credit Union.Date type field. |
| 4 | `CDIC.PRM.FEDERAL.END.DATE` | `CaregsCdicParameter_FederalEndDate` | TField |  | Purpose of the field to indicate the Federal transaction end date for the FI who has moved from BC to Federal Credit Union.Date type field. |
| 5 | `CDIC.PRM.JOINT.CHECK` | `CaregsCdicParameter_JointCheck` | TField |  | Purpose of the field to define the consideration for joint owner validation.Applicable inputs.* Customer Role - Joint check validation will be based on AA.CUSTOMER.ROLE or AA.OTHER.PARTY* Relation - Joint check validation will be based on the relation codes defined in RELATION.CODE field. |
| 6 | `CDIC.PRM.RELATION.CODE` | `CaregsCdicParameter_RelationCode` |  |  |  |
| 7 | `CDIC.PRM.JOINT.AA.ROLE` | `CaregsCdicParameter_JointAaRole` |  |  |  |
| 8 | `CDIC.PRM.ACCT.BAL.TYPE` | `CaregsCdicParameter_AcctBalType` | TField |  | Purpose of the field to report the ACCOUNT balance.Example - CURACCOUNT |
| 9 | `CDIC.PRM.DEPOSIT.BAL.TYPE` | `CaregsCdicParameter_DepositBalType` | TField |  | Purpose of the field to report the DEPOSIT balance.Example - CURACCOUNT |
| 10 | `CDIC.PRM.FOREIGN.BRANCH` | `CaregsCdicParameter_ForeignBranch` |  |  |  |
| 11 | `CDIC.PRM.DETERMINATION.MODE` | `CaregsCdicParameter_DeterminationMode` | TField |  | Field to indicate the bank corrupts and need to reverse all the user records.Allowed inputs: YES / NOValidation - One time input. |
| 12 | `CDIC.PRM.EXC.USER.GROUP` | `CaregsCdicParameter_ExcUserGroup` |  |  |  |
| 13 | `CDIC.PRM.USER.PROCESS` | `CaregsCdicParameter_UserProcess` | TField |  | REVERSE or INACTIVEIf set to reverse, User record not matching USER.SMS.GROUP defined in EXC.USER.GROUP will be reversed.If set to Inactive, User record not matching USER.SMS.GROUP defined in EXC.USER.GROUP will be set to Inactive. |
| 14 | `CDIC.PRM.INSURANCE.PRIORITY` | `CaregsCdicParameter_InsurancePriority` |  |  |  |
| 15 | `CDIC.PRM.MI.SECTOR` | `CaregsCdicParameter_MiSector` |  |  |  |
| 16 | `CDIC.PRM.NOMINEE.SECTOR` | `CaregsCdicParameter_NomineeSector` |  |  |  |
| 17 | `CDIC.PRM.NOMINEE.INDUSTRY` | `CaregsCdicParameter_NomineeIndustry` |  |  |  |
| 18 | `CDIC.PRM.INTERNAL.CATEGORY` | `CaregsCdicParameter_InternalCategory` |  |  |  |
| 19 | `CDIC.PRM.INTERNAL.ACCOUNT` | `CaregsCdicParameter_InternalAccount` |  |  |  |
| 20 | `CDIC.PRM.INCLUDE.AGC` | `CaregsCdicParameter_IncludeAgc` |  |  |  |
| 21 | `CDIC.PRM.HOLD.TYPE` | `CaregsCdicParameter_HoldType` | TField |  | The hold type is a numeric value used to update AC.LOCKED.EVENTS&gt;HOLD.TYPE field at the time of placing the hold. |
| 22 | `CDIC.PRM.SUBSYSTEM.ID` | `CaregsCdicParameter_SubsystemId` | TField |  | CDIC Subystem id will be used for reporting purpose |
| 23 | `CDIC.PRM.ACCT.INT.PROPERTY` | `CaregsCdicParameter_AcctIntProperty` | TField |  | The field is to define the Account Interest Property |
| 24 | `CDIC.PRM.DEP.INT.PROPERTY` | `CaregsCdicParameter_DepIntProperty` | TField |  | The field is to define the Desposit Interest Property |
| 25 | `CDIC.PRM.CHEQUE.TYPE` | `CaregsCdicParameter_ChequeType` |  |  |  |
| 26 | `CDIC.PRM.TRANSACTION` | `CaregsCdicParameter_Transaction` |  |  |  |
| 27 | `CDIC.PRM.NON.TST.ACT.CD` | `CaregsCdicParameter_NonTstActCd` |  |  |  |
| 28 | `CDIC.PRM.OFS.VERSION` | `CaregsCdicParameter_OfsVersion` | TField |  | the field is to define the OFS version used for Processing Ac Locked Events |
| 29 | `CDIC.PRM.OFS.SOURCE` | `CaregsCdicParameter_OfsSource` | TField |  | the field is to define the OFS Source used for Processing Ac Locked Events |
| 30 | `CDIC.PRM.LOCAL.REF` | `CaregsCdicParameter_LocalRef` |  |  |  |
| 31 | `CDIC.PRM.BROK.OR.NOM` | `CaregsCdicParameter_BrokOrNom` | TField |  | Field to indicate whether Broker Id or Nominee CIF id to be treated as owners for Nominee deposits.Allowed inputs: Broker / Nominee / None. |
| 32 | `CDIC.PRM.NB.PT.RELATION` | `CaregsCdicParameter_NbPtRelation` |  |  |  |
| 33 | `CDIC.PRM.NB.PT.REL.CODE` | `CaregsCdicParameter_NbPtRelCode` |  |  |  |
| 34 | `CDIC.PRM.EXCLUDE.PRODUCT` | `CaregsCdicParameter_ExcludeProduct` |  |  |  |
| 35 | `CDIC.PRM.HOOK.API` | `CaregsCdicParameter_HookApi` | TField |  | Purpose of the field to define the Hook API for L3. It should be a valid EB.API record. |
| 36 | `CDIC.PRM.NB.PT.CHECK` | `CaregsCdicParameter_NbPtCheck` |  |  |  |
| 37 | `CDIC.PRM.PRIMARY.OWNER.ROLE` | `CaregsCdicParameter_PrimaryOwnerRole` | TField |  | Purpose of the field to define the role to be assigned for the Primary Customer.Role defined in this field will be considered as Primary Customer role and getsupdated in CAREGS.CDIC.ACCT.DETAILS > OWNER.ROLE |
| 38 | `CDIC.PRM.RESERVED.3` | `CaregsCdicParameter_Reserved3` |  |  |  |
| 39 | `CDIC.PRM.RESERVED.2` | `CaregsCdicParameter_Reserved2` |  |  |  |
| 40 | `CDIC.PRM.RESERVED.1` | `CaregsCdicParameter_Reserved1` |  |  |  |
| 41 | `CDIC.PRM.OVERRIDE` | `CaregsCdicParameter_Override` |  |  |  |
| 42 | `CDIC.PRM.RECORD.STATUS` | `CaregsCdicParameter_RecordStatus` | String |  |  |
| 43 | `CDIC.PRM.CURR.NO` | `CaregsCdicParameter_CurrNo` | String |  |  |
| 44 | `CDIC.PRM.INPUTTER` | `CaregsCdicParameter_Inputter` |  |  |  |
| 45 | `CDIC.PRM.DATE.TIME` | `CaregsCdicParameter_DateTime` |  |  |  |
| 46 | `CDIC.PRM.AUTHORISER` | `CaregsCdicParameter_Authoriser` | String |  |  |
| 47 | `CDIC.PRM.CO.CODE` | `CaregsCdicParameter_CoCode` | String |  |  |
| 48 | `CDIC.PRM.DEPT.CODE` | `CaregsCdicParameter_DeptCode` | String |  |  |
| 49 | `CDIC.PRM.AUDITOR.CODE` | `CaregsCdicParameter_AuditorCode` | String |  |  |
| 50 | `CDIC.PRM.AUDIT.DATE.TIME` | `CaregsCdicParameter_AuditDateTime` | String |  |  |
