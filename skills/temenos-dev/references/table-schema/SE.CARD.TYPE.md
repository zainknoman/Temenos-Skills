# SE.CARD.TYPE — Table Schema

> Source: `INSERTS/I_F.SE.CARD.TYPE` in `SE_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCT.DESCRIPTION` | `SeCardType_Description` |  |  |  |
| 2 | `TCT.CUSTOMER.NAME` | `SeCardType_CustomerName` | TField |  |  |
| 3 | `TCT.CATEGORY` | `SeCardType_Category` | TField |  |  |
| 4 | `TCT.CARD.TYPE` | `SeCardType_CardType` |  |  |  |
| 5 | `TCT.CARD.CHARGES` | `SeCardType_CardCharges` | TField |  |  |
| 6 | `TCT.CARD.REVIEW.FREQUENCY` | `SeCardType_CardReviewFrequency` | TField |  |  |
| 7 | `TCT.NO.OF.CARDS` | `SeCardType_NoOfCards` | TField |  |  |
| 8 | `TCT.START.DATE` | `SeCardType_StartDate` | TField |  |  |
| 9 | `TCT.END.DATE` | `SeCardType_EndDate` | TField |  |  |
| 10 | `TCT.ALLOWED.PRIVILEGES` | `SeCardType_AllowedPrivileges` | TField |  |  |
| 11 | `TCT.NOTES` | `SeCardType_Notes` | TField |  |  |
| 12 | `TCT.CARD.ISSUE.DATE` | `SeCardType_CardIssueDate` |  |  |  |
| 13 | `TCT.CARD.JOINT.HOLDER.NAME` | `SeCardType_CardJointHolderName` |  |  |  |
| 14 | `TCT.CARD.JOINT.HOLDER.RELATION` | `SeCardType_CardJointHolderRelation` |  |  |  |
| 15 | `TCT.CARD.JOINT.HOLDER.ADDRESS` | `SeCardType_CardJointHolderAddress` |  |  |  |
| 16 | `TCT.JOINT.HOLDER.AADHAAR.NO` | `SeCardType_JointHolderAadhaarNo` |  |  |  |
| 17 | `TCT.OTHER.OFFICER` | `SeCardType_OtherOfficer` |  |  |  |
| 18 | `TCT.LOCAL.REF` | `SeCardType_LocalRef` |  |  |  |
| 19 | `TCT.OVERRIDE` | `SeCardType_Override` |  |  |  |
| 20 | `TCT.RECORD.STATUS` | `SeCardType_RecordStatus` | String |  |  |
| 21 | `TCT.CURR.NO` | `SeCardType_CurrNo` | String |  |  |
| 22 | `TCT.INPUTTER` | `SeCardType_Inputter` |  |  |  |
| 23 | `TCT.DATE.TIME` | `SeCardType_DateTime` |  |  |  |
| 24 | `TCT.AUTHORISER` | `SeCardType_Authoriser` | String |  |  |
| 25 | `TCT.CO.CODE` | `SeCardType_CoCode` | String |  |  |
| 26 | `TCT.DEPT.CODE` | `SeCardType_DeptCode` | String |  |  |
| 27 | `TCT.AUDITOR.CODE` | `SeCardType_AuditorCode` | String |  |  |
| 28 | `TCT.AUDIT.DATE.TIME` | `SeCardType_AuditDateTime` | String |  |  |
