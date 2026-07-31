# EB.API — Table Schema

> Source: `INSERTS/I_F.EB.API` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.API.DESCRIPTION` | `EbApi_Description` |  |  |  |
| 2 | `EB.API.PROTECTION.LEVEL` | `EbApi_ProtectionLevel` | TField |  | The protection level that is to be followed. The accepted values are FULL, PARTIAL and NONE |
| 3 | `EB.API.SOURCE.TYPE` | `EbApi_SourceType` | TField |  | The relevant source type of this user-defined subroutine. The accepted values are BASIC, JAVA, HOOK and METHOD A BASIC api suboroutine will share the ID of the current api record A JAVA api method will be detailed in the JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD fields A HOOK api will have at least one entry in the HOOK.DESCRIPTION, HOOK.COMPONENT, HOOK.METHOD, INVOKE.COMPONENT and INVOKE.METHOD fields A METHOD api will have either a COMPONENT and METHOD or a JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD |
| 4 | `EB.API.JAVA.METHOD` | `EbApi_JavaMethod` | TField | Yes | Name of the JAVA method that is to be invoked Mandatory when the source type is JAVA A JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD or COMPONENT and METHOD must be supplied when the SOURCE.TYPE is METHOD |
| 5 | `EB.API.JAVA.CLASS` | `EbApi_JavaClass` | TField | Yes | Name of the JAVA class that is to be invoked. The java program is to be compiled and the resultant .class file name is to be attached in this field Mandatory when the source type is JAVA A JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD or COMPONENT and METHOD must be supplied when the SOURCE.TYPE is METHOD |
| 6 | `EB.API.JAVA.PACKAGE` | `EbApi_JavaPackage` | TField | Yes | Name of the JAVA package that is to be invoked. Mandatory when the source type is JAVA A JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD or COMPONENT and METHOD must be supplied when the SOURCE.TYPE is METHOD |
| 7 | `EB.API.PARAMETER` | `EbApi_Parameter` |  |  |  |
| 8 | `EB.API.PARAM.DESCRIPTION` | `EbApi_ParamDescription` |  |  |  |
| 9 | `EB.API.PARAM.MANDATORY` | `EbApi_ParamMandatory` |  |  |  |
| 10 | `EB.API.RESERVED24` | `EbApi_Reserved24` |  |  |  |
| 11 | `EB.API.RESERVED23` | `EbApi_Reserved23` |  |  |  |
| 12 | `EB.API.RESERVED22` | `EbApi_Reserved22` |  |  |  |
| 13 | `EB.API.RESERVED21` | `EbApi_Reserved21` |  |  |  |
| 14 | `EB.API.RESERVED20` | `EbApi_Reserved20` | TField |  |  |
| 15 | `EB.API.HOOK.DESCRIPTION` | `EbApi_HookDescription` |  |  |  |
| 16 | `EB.API.HOOK.COMPONENT` | `EbApi_HookComponent` |  |  |  |
| 17 | `EB.API.HOOK.METHOD` | `EbApi_HookMethod` |  |  |  |
| 18 | `EB.API.RESERVED16` | `EbApi_Reserved16` |  |  |  |
| 19 | `EB.API.INVOKE.COMPONENT` | `EbApi_InvokeComponent` |  |  |  |
| 20 | `EB.API.INVOKE.METHOD` | `EbApi_InvokeMethod` |  |  |  |
| 21 | `EB.API.RESERVED13` | `EbApi_Reserved13` |  |  |  |
| 22 | `EB.API.RESERVED12` | `EbApi_Reserved12` |  |  |  |
| 23 | `EB.API.COMPONENT` | `EbApi_Component` | TField |  | The component name that contains the method A COMPONENT and METHOD or JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD must be supplied when the SOURCE.TYPE is METHOD |
| 24 | `EB.API.METHOD` | `EbApi_Method` | TField |  | The method name of the implementing method within the component A COMPONENT and METHOD or JAVA.PACKAGE, JAVA.CLASS and JAVA.METHOD must be supplied when the SOURCE.TYPE is METHOD |
| 25 | `EB.API.LINK.TO.TEC` | `EbApi_LinkToTec` | TField |  | Identifies the threshold profile to keep the threshold time for the JAVA API call. It must be supplied when the SOURCE.TYPE is METHOD Validation Rules: Inputted TEC.ITEM profile should have the ITEM.CLASIFICATION as either NULL or Technical and METRIC.TYPE should be TIME. |
| 26 | `EB.API.RESERVED8` | `EbApi_Reserved8` | TField |  |  |
| 27 | `EB.API.HOOK.APPLICATION` | `EbApi_HookApplication` |  |  |  |
| 28 | `EB.API.HOOK.FIELD.NAME` | `EbApi_HookFieldName` |  |  |  |
| 29 | `EB.API.HOOK.FIELD.TYPE` | `EbApi_HookFieldType` |  |  |  |
| 30 | `EB.API.HOOK.PREFIX` | `EbApi_HookPrefix` |  |  |  |
| 31 | `EB.API.RESERVED3` | `EbApi_Reserved3` | TField |  |  |
| 32 | `EB.API.RESERVED2` | `EbApi_Reserved2` | TField |  |  |
| 33 | `EB.API.RESERVED1` | `EbApi_Reserved1` | TField |  |  |
| 34 | `EB.API.RECORD.STATUS` | `EbApi_RecordStatus` | String |  |  |
| 35 | `EB.API.CURR.NO` | `EbApi_CurrNo` | String |  |  |
| 36 | `EB.API.INPUTTER` | `EbApi_Inputter` |  |  |  |
| 37 | `EB.API.DATE.TIME` | `EbApi_DateTime` |  |  |  |
| 38 | `EB.API.AUTHORISER` | `EbApi_Authoriser` | String |  |  |
| 39 | `EB.API.CO.CODE` | `EbApi_CoCode` | String |  |  |
| 40 | `EB.API.DEPT.CODE` | `EbApi_DeptCode` | String |  |  |
| 41 | `EB.API.AUDITOR.CODE` | `EbApi_AuditorCode` | String |  |  |
| 42 | `EB.API.AUDIT.DATE.TIME` | `EbApi_AuditDateTime` | String |  |  |
