# CR.RELATIONSHIP — Table Schema

> Source: `INSERTS/I_F.CR.RELATIONSHIP` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.RS.RELATIONSHIP.NAME` | `CrRelationship_RelationshipName` | A (alphanumeric) | Yes | Text description of relationship name. Validation Rules 1-50 type A (alphanumeric) characters. Mandatory Input. |
| 2 | `CR.RS.RISK` | `CrRelationship_Risk` |  |  |  |
| 3 | `CR.RS.WHY.RISK.ACCEPTED` | `CrRelationship_WhyRiskAccepted` |  |  |  |
| 4 | `CR.RS.BOOKING.CENTER` | `CrRelationship_BookingCenter` | TField |  | Holds the Booking Center for CR Relationship. Validation Rules 1 � 4 Numeric CharactersThis links to Dept Acct Officer table. Therefore it must be a valid account officer on the DEPT.ACCT.OFFICER table. |
| 5 | `CR.RS.BRANCH.CODE` | `CrRelationship_BranchCode` | TField |  | Holds the details about the company in which the relationship is available. Validation Rules This is linked to the COMPANY table. |
| 6 | `CR.RS.REL.MANAGER` | `CrRelationship_RelManager` | TField |  | Specific Relationship Manager for the Customer Relationship. Validation Rules 1 � 4 Numeric Characters.This links to Dept Acct Officer table. Therefore it must be a valid account officer on the DEPT.ACCT.OFFICER table. |
| 7 | `CR.RS.FURTHER.MANAGERS` | `CrRelationship_FurtherManagers` |  |  |  |
| 8 | `CR.RS.MIS.CODE` | `CrRelationship_MisCode` | TField |  | MIS Code � A number allocated by the bank�s MIS System. Validation Rules Must be 1 � 10 Alphanumeric characters |
| 9 | `CR.RS.RELATIONSHIP.UPDATE` | `CrRelationship_RelationshipUpdate` |  |  |  |
| 10 | `CR.RS.UPDATE.REASON` | `CrRelationship_UpdateReason` |  |  |  |
| 11 | `CR.RS.UPDATE.DATE` | `CrRelationship_UpdateDate` |  |  |  |
| 12 | `CR.RS.REL.START.DATE` | `CrRelationship_RelStartDate` | TField |  | Specifies the date for the start of the relationship. Validation Rules Up to 9 date characters (standard Date format in range 1950 - 2049) - Type D.The date entered must not exceed the maximum system forward Value Date defined in the Dates file. |
| 13 | `CR.RS.HOW.INTRODUCED` | `CrRelationship_HowIntroduced` | TField |  | Specifies how the client was introduced. Validation Rules Must be a key to a record in CR.INTRODUCTION.SOURCE table |
| 14 | `CR.RS.INTRO.DETAILS` | `CrRelationship_IntroDetails` |  |  |  |
| 15 | `CR.RS.MARKET.INDICATOR` | `CrRelationship_MarketIndicator` | TField |  | Target Market Indicator Validation Rules This is linked to the virtual EB.LOOKUP. All values must have an entry in EB.LOOKUP table. |
| 16 | `CR.RS.RETROCESSION.PAYMENT` | `CrRelationship_RetrocessionPayment` | TField |  | Identifies if payment needs to be made of a retrocession as a result of the Customer Relationship. Validation Rules Input must be either YES or NO |
| 17 | `CR.RS.RETROCESSION.DETAILS` | `CrRelationship_RetrocessionDetails` |  |  |  |
| 18 | `CR.RS.REFERENCES` | `CrRelationship_References` |  |  |  |
| 19 | `CR.RS.PRIMARY.CONTACT` | `CrRelationship_PrimaryContact` |  |  |  |
| 20 | `CR.RS.CALC.AML.EVALUATION` | `CrRelationship_CalcAmlEvaluation` | TField |  | Holds the automated calculation of AML rating. The data for this is loaded in to the system from an outside source. Validation Rules This is linked to the virtual EB.LOOKUP. All values must have an entry in EB.LOOKUP table. |
| 21 | `CR.RS.MANUAL.AML.EVALUATION` | `CrRelationship_ManualAmlEvaluation` | TField |  | Holds the Manual AML Evaluation. This will be manually entered by the user. Validation Rules This is linked to the virtual EB.LOOKUP. All values must have an entry in EB.LOOKUP table. |
| 22 | `CR.RS.REASON.DIFFT.AML.EVAL` | `CrRelationship_ReasonDifftAmlEval` |  |  |  |
| 23 | `CR.RS.PROFILE.REVIEW.EVAL` | `CrRelationship_ProfileReviewEval` | TField |  | Evaluation after Client Profile Review. Validation Rules This is linked to the virtual EB.LOOKUP. All values must have an entry in EB.LOOKUP table. |
| 24 | `CR.RS.REASON.DIFFT.RISK.EVAL` | `CrRelationship_ReasonDifftRiskEval` |  |  |  |
| 25 | `CR.RS.FOLLOW.UP.REQUIRED` | `CrRelationship_FollowUpRequired` |  |  |  |
| 26 | `CR.RS.TAGGING.REQUIRED` | `CrRelationship_TaggingRequired` | TField |  | Specifies if the customer relationship is to be tagged for further attention. Validation Rules This is linked to the virtual EB.LOOKUP. All values must have an entry in EB.LOOKUP table. |
| 27 | `CR.RS.RESTRICTIONS.REQUIRED` | `CrRelationship_RestrictionsRequired` |  |  |  |
| 28 | `CR.RS.RESERVED.8` | `CrRelationship_Reserved8` | TField |  |  |
| 29 | `CR.RS.RESERVED.7` | `CrRelationship_Reserved7` | TField |  |  |
| 30 | `CR.RS.RESERVED.6` | `CrRelationship_Reserved6` | TField |  |  |
| 31 | `CR.RS.RESERVED.5` | `CrRelationship_Reserved5` | TField |  |  |
| 32 | `CR.RS.RESERVED.4` | `CrRelationship_Reserved4` | TField |  |  |
| 33 | `CR.RS.RESERVED.3` | `CrRelationship_Reserved3` | TField |  |  |
| 34 | `CR.RS.RESERVED.2` | `CrRelationship_Reserved2` | TField |  |  |
| 35 | `CR.RS.RESERVED.1` | `CrRelationship_Reserved1` | TField |  |  |
| 36 | `CR.RS.LOCAL.REF` | `CrRelationship_LocalRef` |  |  |  |
| 37 | `CR.RS.OVERRIDE` | `CrRelationship_Override` |  |  |  |
| 38 | `CR.RS.RECORD.STATUS` | `CrRelationship_RecordStatus` | String |  |  |
| 39 | `CR.RS.CURR.NO` | `CrRelationship_CurrNo` | String |  |  |
| 40 | `CR.RS.INPUTTER` | `CrRelationship_Inputter` |  |  |  |
| 41 | `CR.RS.DATE.TIME` | `CrRelationship_DateTime` |  |  |  |
| 42 | `CR.RS.AUTHORISER` | `CrRelationship_Authoriser` | String |  |  |
| 43 | `CR.RS.CO.CODE` | `CrRelationship_CoCode` | String |  |  |
| 44 | `CR.RS.DEPT.CODE` | `CrRelationship_DeptCode` | String |  |  |
| 45 | `CR.RS.AUDITOR.CODE` | `CrRelationship_AuditorCode` | String |  |  |
| 46 | `CR.RS.AUDIT.DATE.TIME` | `CrRelationship_AuditDateTime` | String |  |  |
