# USCORE.IMAGE.DOC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USCORE.IMAGE.DOC.PARAMETER` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAR.DOCUMENT.TYPE` | `UscoreImageDocParameter_DocumentType` | A (alphanumeric) | Yes | This field will be linked to DOCUMENT.TYPE table. This will be a dropdown. The user will be able to select the required Type of Document (example:PASSPORT) Validation Rules 10 type A (alphanumeric) characters. (Mandatory input) |
| 2 | `PAR.REFERENCE.NO` | `UscoreImageDocParameter_ReferenceNo` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 3 | `PAR.STATE` | `UscoreImageDocParameter_State` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 4 | `PAR.COUNTRY` | `UscoreImageDocParameter_Country` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 5 | `PAR.ISSUER` | `UscoreImageDocParameter_Issuer` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 6 | `PAR.ISSUE.DATE` | `UscoreImageDocParameter_IssueDate` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 7 | `PAR.END.DATE` | `UscoreImageDocParameter_EndDate` | TField | Yes | To select if this field is Mandatory or not. Validation Rules Options YES/NO (Mandatory input) |
| 8 | `PAR.RESERVED.5` | `UscoreImageDocParameter_Reserved5` | TField |  |  |
| 9 | `PAR.RESERVED.4` | `UscoreImageDocParameter_Reserved4` | TField |  |  |
| 10 | `PAR.RESERVED.3` | `UscoreImageDocParameter_Reserved3` | TField |  |  |
| 11 | `PAR.RESERVED.2` | `UscoreImageDocParameter_Reserved2` | TField |  |  |
| 12 | `PAR.RESERVED.1` | `UscoreImageDocParameter_Reserved1` | TField |  |  |
| 13 | `PAR.LOCAL.REF` | `UscoreImageDocParameter_LocalRef` |  |  |  |
| 14 | `PAR.RECORD.STATUS` | `UscoreImageDocParameter_RecordStatus` | String |  |  |
| 15 | `PAR.CURR.NO` | `UscoreImageDocParameter_CurrNo` | String |  |  |
| 16 | `PAR.INPUTTER` | `UscoreImageDocParameter_Inputter` |  |  |  |
| 17 | `PAR.DATE.TIME` | `UscoreImageDocParameter_DateTime` |  |  |  |
| 18 | `PAR.AUTHORISER` | `UscoreImageDocParameter_Authoriser` | String |  |  |
| 19 | `PAR.CO.CODE` | `UscoreImageDocParameter_CoCode` | String |  |  |
| 20 | `PAR.DEPT.CODE` | `UscoreImageDocParameter_DeptCode` | String |  |  |
| 21 | `PAR.AUDITOR.CODE` | `UscoreImageDocParameter_AuditorCode` | String |  |  |
| 22 | `PAR.AUDIT.DATE.TIME` | `UscoreImageDocParameter_AuditDateTime` | String |  |  |
