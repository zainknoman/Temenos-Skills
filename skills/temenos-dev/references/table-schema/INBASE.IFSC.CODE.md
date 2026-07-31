# INBASE.IFSC.CODE — Table Schema

> Source: `INSERTS/I_F.INBASE.IFSC.CODE` in `INBASE_CustomerValidations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INBASE.IFSC.STATE` | `InbaseIfscCode_State` | TField |  | State of the bank. |
| 2 | `INBASE.IFSC.STATUS` | `InbaseIfscCode_Status` | TField |  | Stores the status "O" - Operational or "C" - Closed. Radio button field.. |
| 3 | `INBASE.IFSC.DEAL.FEX` | `InbaseIfscCode_DealFex` | TField |  | Stores whether the branch deals with Foreign exchange or not. Radio Button field with options "YES" or "NO |
| 4 | `INBASE.IFSC.DATA.STATUS` | `InbaseIfscCode_DataStatus` | TField |  | Denotes whether this data updation is "F" - Fresh or "A" - Amendment. Radio button field. |
| 5 | `INBASE.IFSC.UPLOAD.IFSC.DATA` | `InbaseIfscCode_UploadIfscData` | TField |  | BranchA radio button field to denote whether the changes has to be uploaded to DGFT. Radio button field with options �YES� or �NO�. |
| 6 | `INBASE.IFSC.DATE` | `InbaseIfscCode_Date` | TField |  | Stores the date on which the IFSC data is updated. Defaults to system date |
| 7 | `INBASE.IFSC.RESERVED.10` | `InbaseIfscCode_Reserved10` | TField |  | This field is reserved for future purpose |
| 8 | `INBASE.IFSC.RESERVED.9` | `InbaseIfscCode_Reserved9` | TField |  | This field is reserved for future purpose |
| 9 | `INBASE.IFSC.RESERVED.8` | `InbaseIfscCode_Reserved8` | TField |  | This field is reserved for future purpose |
| 10 | `INBASE.IFSC.RESERVED.7` | `InbaseIfscCode_Reserved7` | TField |  | This field is reserved for future purpose |
| 11 | `INBASE.IFSC.RESERVED.6` | `InbaseIfscCode_Reserved6` | TField |  | This field is reserved for future purpose |
| 12 | `INBASE.IFSC.RESERVED.5` | `InbaseIfscCode_Reserved5` | TField |  | This field is reserved for future purpose |
| 13 | `INBASE.IFSC.RESERVED.4` | `InbaseIfscCode_Reserved4` | TField |  | This field is reserved for future purpose |
| 14 | `INBASE.IFSC.RESERVED.3` | `InbaseIfscCode_Reserved3` | TField |  | This field is reserved for future purpose |
| 15 | `INBASE.IFSC.RESERVED.2` | `InbaseIfscCode_Reserved2` | TField |  | This field is reserved for future purpose |
| 16 | `INBASE.IFSC.RESERVED.1` | `InbaseIfscCode_Reserved1` | TField |  | This field is reserved for future purpose |
| 17 | `INBASE.IFSC.LOCAL.REF` | `InbaseIfscCode_LocalRef` |  |  |  |
| 18 | `INBASE.IFSC.OVERRIDE` | `InbaseIfscCode_Override` |  |  |  |
| 19 | `INBASE.IFSC.RECORD.STATUS` | `InbaseIfscCode_RecordStatus` | String |  |  |
| 20 | `INBASE.IFSC.CURR.NO` | `InbaseIfscCode_CurrNo` | String |  |  |
| 21 | `INBASE.IFSC.INPUTTER` | `InbaseIfscCode_Inputter` |  |  |  |
| 22 | `INBASE.IFSC.DATE.TIME` | `InbaseIfscCode_DateTime` |  |  |  |
| 23 | `INBASE.IFSC.AUTHORISER` | `InbaseIfscCode_Authoriser` | String |  |  |
| 24 | `INBASE.IFSC.CO.CODE` | `InbaseIfscCode_CoCode` | String |  |  |
| 25 | `INBASE.IFSC.DEPT.CODE` | `InbaseIfscCode_DeptCode` | String |  |  |
| 26 | `INBASE.IFSC.AUDITOR.CODE` | `InbaseIfscCode_AuditorCode` | String |  |  |
| 27 | `INBASE.IFSC.AUDIT.DATE.TIME` | `InbaseIfscCode_AuditDateTime` | String |  |  |
