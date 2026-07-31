# IS.REVIEWER — Table Schema

> Source: `INSERTS/I_F.IS.REVIEWER` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.REV.NAME` | `IsReviewer_Name` | TField |  | Defines the Name of the Reviewer. Defaulted as Name of the Customer (@ID being Customer Reference). It can be over-written to specify User-Defined names. Validation Rules: 1. Defaulted as NAME.1 from the Customer table. 2. Standard T24 Alphanumeric field. |
| 2 | `IS.REV.STATUS` | `IsReviewer_Status` | TField | Yes | Defines the status of the Reviewer. The values to the field are defined in the EB.LOOKUP table with prefix "IS.REVIEWER.STATUS*". Validation Rules: 1. Valid values are Active, Inactive should be defined in EB.LOOKUP table as "IS.REVIEWER.STATUS*" 2. Mandatory field. |
| 3 | `IS.REV.TYPE` | `IsReviewer_Type` | TField | Yes | Defines the type of review the reviewer will perform. The values to the field are defined in the EB.LOOKUP table with prefix "REVIEW". Validation Rules: 1. Valid values like Appraiser, Surveyor, Adviser should be defined in EB.LOOKUP table as "REVIEW*" 2. Mandatory field. |
| 4 | `IS.REV.COMPANY` | `IsReviewer_Company` |  |  |  |
| 5 | `IS.REV.CURRENCY` | `IsReviewer_Currency` |  |  |  |
| 6 | `IS.REV.ACCOUNT` | `IsReviewer_Account` |  |  |  |
| 7 | `IS.REV.BENEFICIARY` | `IsReviewer_Beneficiary` |  |  |  |
| 8 | `IS.REV.RESERVED.8` | `IsReviewer_Reserved8` |  |  |  |
| 9 | `IS.REV.RESERVED.7` | `IsReviewer_Reserved7` |  |  |  |
| 10 | `IS.REV.RESERVED.6` | `IsReviewer_Reserved6` |  |  |  |
| 11 | `IS.REV.COMMENTS` | `IsReviewer_Comments` |  |  |  |
| 12 | `IS.REV.RESERVED.5` | `IsReviewer_Reserved5` | TField |  |  |
| 13 | `IS.REV.RESERVED.4` | `IsReviewer_Reserved4` | TField |  |  |
| 14 | `IS.REV.RESERVED.3` | `IsReviewer_Reserved3` | TField |  |  |
| 15 | `IS.REV.RESERVED.2` | `IsReviewer_Reserved2` | TField |  |  |
| 16 | `IS.REV.RESERVED.1` | `IsReviewer_Reserved1` | TField |  |  |
| 17 | `IS.REV.LOCAL.REF` | `IsReviewer_LocalRef` |  |  |  |
| 18 | `IS.REV.OVERRIDE` | `IsReviewer_Override` |  |  |  |
| 19 | `IS.REV.RECORD.STATUS` | `IsReviewer_RecordStatus` | String |  |  |
| 20 | `IS.REV.CURR.NO` | `IsReviewer_CurrNo` | String |  |  |
| 21 | `IS.REV.INPUTTER` | `IsReviewer_Inputter` |  |  |  |
| 22 | `IS.REV.DATE.TIME` | `IsReviewer_DateTime` |  |  |  |
| 23 | `IS.REV.AUTHORISER` | `IsReviewer_Authoriser` | String |  |  |
| 24 | `IS.REV.CO.CODE` | `IsReviewer_CoCode` | String |  |  |
| 25 | `IS.REV.DEPT.CODE` | `IsReviewer_DeptCode` | String |  |  |
| 26 | `IS.REV.AUDITOR.CODE` | `IsReviewer_AuditorCode` | String |  |  |
| 27 | `IS.REV.AUDIT.DATE.TIME` | `IsReviewer_AuditDateTime` | String |  |  |
