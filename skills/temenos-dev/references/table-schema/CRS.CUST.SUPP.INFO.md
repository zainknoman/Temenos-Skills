# CRS.CUST.SUPP.INFO — Table Schema

> Source: `INSERTS/I_F.CRS.CUST.SUPP.INFO` in `CD_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CD.SI.CRS.CUSTOMER.TYPE` | `CrsCustSuppInfo_CrsCustomerType` | TField | Yes | Field to state whether the customer is an Individual or an Entity. If the client is an Entity, then further granular level classification is required in to the Entity as a Reportable Person Entity as a Passive NFE. Validation rules: Mandatory field. This value provided must have a record in CRS.CLIENT.TYPE |
| 2 | `CD.SI.KYC.CHECK` | `CrsCustSuppInfo_KycCheck` | TField |  | Field to record whether the KYC checks have been done or not. Validation rules: Allowed values are YES, NO. |
| 3 | `CD.SI.SELF.CERTIFICATION` | `CrsCustSuppInfo_SelfCertification` | TField | Yes | Field to determine whether the Reporting Financial Institution has obtained a self-certification as part of the account opening documentation to determine Account Holders Residence for tax purposes. This is mandatory for the customers opening by a Reporting Financial Institution after the Effective date of the regulation. Validation rules: Applicable in case of the followings: Pre-existing Entity High, New Individual Accounts, New Entity Accounts Allowed values are Yes - Signifies that Self-certificate form is submitted and valid for the customer No - Signifies that Self-certificate form is yet to be submitted by the customer Expired - Signifies an expired Self Certificate In.Grace.Period - Signifies an expiring self-certificate Null - Can be mapped to Null for the migrated customers until their Self certificate document status is ascertained. This value can be updated for the migrated customers until the Self certification situation is assessed. |
| 4 | `CD.SI.BIRTH.INCORP.DATE` | `CrsCustSuppInfo_BirthIncorpDate` | TField | Yes | Field to record the birth/incorporation date of the beneficial owner. In case of Individuals Date of Birth, in case of Entities Date of Incorporation. If this has been specified in the CUSTOMER table then that will be defaulted from there. Validation rules: Mandatory field. If BIRTH.INCORP.DATE is present in the CUSTOMER application, then the date specified in this field should be same with the Customer application. |
| 5 | `CD.SI.BIRTH.INCORP.PLACE` | `CrsCustSuppInfo_BirthIncorpPlace` | TField | Yes | Field to record the place of birth/incorporation place for the beneficial owner. In case of individuals - Place of Birth, in case of entities - Place of incorporation. Validation rules: Mandatory field. Must be a valid country code. |
| 6 | `CD.SI.TAX.RESIDENCE` | `CrsCustSuppInfo_TaxResidence` |  |  |  |
| 7 | `CD.SI.TAX.IDENTITY.NO` | `CrsCustSuppInfo_TaxIdentityNo` |  |  |  |
| 8 | `CD.SI.ADDRESS.TYPE` | `CrsCustSuppInfo_AddressType` |  |  |  |
| 9 | `CD.SI.ADDRESS.COUNTRY` | `CrsCustSuppInfo_AddressCountry` |  |  |  |
| 10 | `CD.SI.TELEPHONE.NO` | `CrsCustSuppInfo_TelephoneNo` |  |  |  |
| 11 | `CD.SI.TELEPHONE.COUNTRY` | `CrsCustSuppInfo_TelephoneCountry` |  |  |  |
| 12 | `CD.SI.STANDING.INSTRUCT` | `CrsCustSuppInfo_StandingInstruct` |  |  |  |
| 13 | `CD.SI.POA.HOLDER.COUNTRY` | `CrsCustSuppInfo_PoaHolderCountry` |  |  |  |
| 14 | `CD.SI.ROLE.TYPE` | `CrsCustSuppInfo_RoleType` |  |  |  |
| 15 | `CD.SI.CUSTOMER.ID` | `CrsCustSuppInfo_CustomerId` |  |  |  |
| 16 | `CD.SI.CUSTOMER.NAME` | `CrsCustSuppInfo_CustomerName` |  |  |  |
| 17 | `CD.SI.CUSTOMER.REFERENCE` | `CrsCustSuppInfo_CustomerReference` |  |  |  |
| 18 | `CD.SI.DATE.OF.BIRTH` | `CrsCustSuppInfo_DateOfBirth` |  |  |  |
| 19 | `CD.SI.PLACE.OF.BIRTH` | `CrsCustSuppInfo_PlaceOfBirth` |  |  |  |
| 20 | `CD.SI.RT.TAX.RESIDENCE` | `CrsCustSuppInfo_RtTaxResidence` |  |  |  |
| 21 | `CD.SI.TIN` | `CrsCustSuppInfo_Tin` |  |  |  |
| 22 | `CD.SI.CTRLG.PERSON.TYPE` | `CrsCustSuppInfo_CtrlgPersonType` |  |  |  |
| 23 | `CD.SI.ADDRESS` | `CrsCustSuppInfo_Address` |  |  |  |
| 24 | `CD.SI.RT.ADDRESS.COUNTRY` | `CrsCustSuppInfo_RtAddressCountry` |  |  |  |
| 25 | `CD.SI.REMARKS` | `CrsCustSuppInfo_Remarks` |  |  |  |
| 26 | `CD.SI.RESERVED.11` | `CrsCustSuppInfo_Reserved11` |  |  |  |
| 27 | `CD.SI.INDICIA` | `CrsCustSuppInfo_Indicia` | TField |  | System will populate YES if any of the indicia's are met or else NO. Validation rules: No input field. |
| 28 | `CD.SI.REPORTABLE.JUR.RES` | `CrsCustSuppInfo_ReportableJurRes` |  |  |  |
| 29 | `CD.SI.REPORT.WAIVER.REC` | `CrsCustSuppInfo_ReportWaiverRec` |  |  |  |
| 30 | `CD.SI.CRS.STATUS` | `CrsCustSuppInfo_CrsStatus` |  |  |  |
| 31 | `CD.SI.STATUS.CHNG.DATE` | `CrsCustSuppInfo_StatusChngDate` |  |  |  |
| 32 | `CD.SI.CHANGE.REASON` | `CrsCustSuppInfo_ChangeReason` |  |  |  |
| 33 | `CD.SI.DORMANT.STATUS` | `CrsCustSuppInfo_DormantStatus` | TField |  | This field will be set to YES to indicate that the customer has become DORMANT.This is performed by job ST.UPDATE.INDICIA during COB based on the set up in CRS.PARAMETER application in dormant related fields.Based on this field DormantAccount attribute for AccountNumber tag is set to YES. |
| 34 | `CD.SI.LAST.AGGR.DATE` | `CrsCustSuppInfo_LastAggrDate` | TField |  | This field represents the date on which the last aggregation for this customer has happened. This is populated by job ST.BUILD.AGGR.BALANCES. |
| 35 | `CD.SI.SC.CUST.REF` | `CrsCustSuppInfo_ScCustRef` |  |  |  |
| 36 | `CD.SI.SC.REQ.DATE` | `CrsCustSuppInfo_ScReqDate` |  |  |  |
| 37 | `CD.SI.SC.RECV.DATE` | `CrsCustSuppInfo_ScRecvDate` |  |  |  |
| 38 | `CD.SI.SC.CUT.OFF.DATE` | `CrsCustSuppInfo_ScCutOffDate` |  |  |  |
| 39 | `CD.SI.SC.DOC.STATUS` | `CrsCustSuppInfo_ScDocStatus` |  |  |  |
| 40 | `CD.SI.RT.SC.DOC.STATUS` | `CrsCustSuppInfo_RtScDocStatus` |  |  |  |
| 41 | `CD.SI.INDICIA.SUMMARY` | `CrsCustSuppInfo_IndiciaSummary` |  |  |  |
| 42 | `CD.SI.INDICIA.COUNTRY` | `CrsCustSuppInfo_IndiciaCountry` |  |  |  |
| 43 | `CD.SI.LOCAL.REF` | `CrsCustSuppInfo_LocalRef` |  |  |  |
| 44 | `CD.SI.OVERRIDE` | `CrsCustSuppInfo_Override` |  |  |  |
| 45 | `CD.SI.RECORD.STATUS` | `CrsCustSuppInfo_RecordStatus` | String |  |  |
| 46 | `CD.SI.CURR.NO` | `CrsCustSuppInfo_CurrNo` | String |  |  |
| 47 | `CD.SI.INPUTTER` | `CrsCustSuppInfo_Inputter` |  |  |  |
| 48 | `CD.SI.DATE.TIME` | `CrsCustSuppInfo_DateTime` |  |  |  |
| 49 | `CD.SI.AUTHORISER` | `CrsCustSuppInfo_Authoriser` | String |  |  |
| 50 | `CD.SI.CO.CODE` | `CrsCustSuppInfo_CoCode` | String |  |  |
| 51 | `CD.SI.DEPT.CODE` | `CrsCustSuppInfo_DeptCode` | String |  |  |
| 52 | `CD.SI.AUDITOR.CODE` | `CrsCustSuppInfo_AuditorCode` | String |  |  |
| 53 | `CD.SI.AUDIT.DATE.TIME` | `CrsCustSuppInfo_AuditDateTime` | String |  |  |
| 54 | `CD.SI.TIN.NOT.PROVIDED.CODE` | `CrsCustSuppInfo_TinNotProvidedCode` |  |  |  |
| 55 | `CD.SI.TIN.NOT.PROVIDED.REASON` | `CrsCustSuppInfo_TinNotProvidedReason` |  |  |  |
| 56 | `CD.SI.INDICIA.START.DATE` | `CrsCustSuppInfo_IndiciaStartDate` |  |  |  |
| 57 | `CD.SI.INDICIA.DATA.RULE` | `CrsCustSuppInfo_IndiciaDataRule` |  |  |  |
| 58 | `CD.SI.INDICIA.DATA.VALUE` | `CrsCustSuppInfo_IndiciaDataValue` |  |  |  |
| 59 | `CD.SI.TIN.STATUS` | `CrsCustSuppInfo_TinStatus` |  |  |  |
| 60 | `CD.SI.SC.EXP.DATE` | `CrsCustSuppInfo_ScExpDate` |  |  |  |
