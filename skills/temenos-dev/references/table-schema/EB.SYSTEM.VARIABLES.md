# EB.SYSTEM.VARIABLES — Table Schema

> Source: `INSERTS/I_F.EB.SYSTEM.VARIABLES` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SYS.DESCRIPTION` | `EbSystemVariables_Description` | TField |  | Free Text field used to describe about the record |
| 2 | `EB.SYS.T24.VARIABLE` | `EbSystemVariables_T24Variable` | TField |  | Text field ,accepts T24 common variable from which system should get value for the variable This is text field and there is no validation to check if the common variable is available in T24 Standard common variable LCCY,ID.COMPANY,TODAY are only supported For using other common variable INVOKE.API can be maintained to call routine and get value for the variable Validation : Any one among T24.VARIABLE , INVOKE.API or LOOKUP is allowed for a record |
| 3 | `EB.SYS.LOOKUP` | `EbSystemVariables_Lookup` | TField |  | Field is used to specify table field to get value Validation : APPLICATION>RECID>FIELD RECID can again be a variable name which can be specified as APPLICATION>!SYSTEM.XXX>FIELD Validation : Any one among T24.VARIABLE , INVOKE.API or LOOKUP is allowed for a record |
| 4 | `EB.SYS.INVOKE.API` | `EbSystemVariables_InvokeApi` | TField |  | This is a CHECK FIELD for EB.API Validation : should be a valid record in EB.API Validation : Any one among T24.VARIABLE , INVOKE.API or LOOKUP is allowed for a record |
| 5 | `EB.SYS.CONDITION` | `EbSystemVariables_Condition` | TField |  | Reserved for Future use. |
| 6 | `EB.SYS.RESERVED.6` | `EbSystemVariables_Reserved6` | TField |  | Reserved Field |
| 7 | `EB.SYS.RESERVED.7` | `EbSystemVariables_Reserved7` | TField |  | Reserved Field |
| 8 | `EB.SYS.RESERVED.8` | `EbSystemVariables_Reserved8` | TField |  | Reserved Field |
| 9 | `EB.SYS.RESERVED.9` | `EbSystemVariables_Reserved9` | TField |  | Reserved Field |
| 10 | `EB.SYS.RESERVED.10` | `EbSystemVariables_Reserved10` | TField |  | Reserved Field |
| 11 | `EB.SYS.OVERRIDE` | `EbSystemVariables_Override` |  |  |  |
| 12 | `EB.SYS.RECORD.STATUS` | `EbSystemVariables_RecordStatus` | String |  |  |
| 13 | `EB.SYS.CURR.NO` | `EbSystemVariables_CurrNo` | String |  |  |
| 14 | `EB.SYS.INPUTTER` | `EbSystemVariables_Inputter` |  |  |  |
| 15 | `EB.SYS.DATE.TIME` | `EbSystemVariables_DateTime` |  |  |  |
| 16 | `EB.SYS.AUTHORISER` | `EbSystemVariables_Authoriser` | String |  |  |
| 17 | `EB.SYS.CO.CODE` | `EbSystemVariables_CoCode` | String |  |  |
| 18 | `EB.SYS.DEPT.CODE` | `EbSystemVariables_DeptCode` | String |  |  |
| 19 | `EB.SYS.AUDITOR.CODE` | `EbSystemVariables_AuditorCode` | String |  |  |
| 20 | `EB.SYS.AUDIT.DATE.TIME` | `EbSystemVariables_AuditDateTime` | String |  |  |
