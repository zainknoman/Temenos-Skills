# DS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DS.PARAMETER` in `DS_Installer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DS.PARAM.DESCRIPTION` | `DsParameter_Description` |  |  |  |
| 2 | `DS.PARAM.VERSION.NAME` | `DsParameter_VersionName` | TField |  | Specifies the application and version, by which the records are created via OFS. If DS.PARAM.ID = VERSION , then VERSION.NAME can have any existing version id of the application called 'VERSION' . If DS.PARAM.ID = ENQUIRY , then VERSION.NAME can have any existing enquiry id of the application called 'ENQUIRY' . For e.g. To create a record in VERSION application, the value is specified as VERSION,DS which will be used in OFS message. The 'DS' is the pgm version for other files, which are specified in FILE.SORTING field. If the FILE.SORTING field is specified with the files EB.API , PGM.FILE and EB.DICTIONARY then the version installer will use the versions such as 'EB.API,DS' , 'PGM.FILE,DS' and 'EB.DICTIONARY,DS' respectively to form OFS messages. Validation Rules: If DS.PARAM.ID = VERSION (installer type), then the application name in VERSION.NAME field should be VERSION . If DS.PARAM.ID = ENQUIRY (installer type), then the application name in VERSION.NAME field should be ENQUIRY . This field cannot be blank if valid application name given as @ID Must be a valid entry in VERSION table. Allows maximum of 35 alphanumerics. |
| 3 | `DS.PARAM.FILE.SORTING` | `DsParameter_FileSorting` |  |  |  |
| 4 | `DS.PARAM.LOCAL.LIB.DIR` | `DsParameter_LocalLibDir` | TField |  | Defines the directory used to store libraries which comes with packager which is created via Design studio Directory given in this field will get created under run directory during DS.PARAMETER table authorization Accepts valid path of existing directory Validation Rules: Accepts input only if the PARAM.ID is SYSTEM Must be a type 1 or 19 (UD type) file Becomes noinput when VERSION.NAME and FILE.SORTING fields given Allows maximum of 50 characters. |
| 5 | `DS.PARAM.LOCAL.BIN.DIR` | `DsParameter_LocalBinDir` | TField |  | Defines the directory used to store binaries which comes with packager which is created via Design studio Directory given in this field will get created under run directory during DS.PARAMETER table authorization Accepts valid path of existing directory Validation Rules: Accepts input only if the PARAM.ID is SYSTEM Must be a type 1 or 19 (UD type) file Becomes noinput when VERSION.NAME and FILE.SORTING fields given Allows maximum of 50 characters. |
| 6 | `DS.PARAM.LOCAL.INSERT.DIR` | `DsParameter_LocalInsertDir` | TField |  | Defines the directory used to store inserts which comes with packager which is created via Design studio Directory given in this field will get created under run directory during DS.PARAMETER table authorization Accepts valid path of existing directory Validation Rules: Accepts input only if the PARAM.ID is SYSTEM Must be a type 1 or 19 (UD type) file Becomes noinput when VERSION.NAME and FILE.SORTING fields given Allows maximum of 50 characters. |
| 7 | `DS.PARAM.INPUT.USER.NAME` | `DsParameter_InputUserName` | TField |  |  |
| 8 | `DS.PARAM.FORCE.DEPLOYMENT.FAILURE` | `DsParameter_ForceDeploymentFailure` | TField |  | Field to enable/ disable global transaction Validation Rules: Rolls back all the transactions during failure. Commits all the successful transactions and rolls back the failure transactions during error. |
| 9 | `DS.PARAM.DISABLE.CASE.CONV` | `DsParameter_DisableCaseConv` | TField |  | Defines whether the case sensitivity check for package name should be disabled or not. If set to YES, it allows the package name without case sensitivity check. Default is NULL. Validation Rules: Allowed values are YES or NULL. |
| 10 | `DS.PARAM.RESERVED.1` | `DsParameter_Reserved1` |  |  |  |
| 11 | `DS.PARAM.RECORD.STATUS` | `DsParameter_RecordStatus` | String |  |  |
| 12 | `DS.PARAM.CURR.NO` | `DsParameter_CurrNo` | String |  |  |
| 13 | `DS.PARAM.INPUTTER` | `DsParameter_Inputter` |  |  |  |
| 14 | `DS.PARAM.DATE.TIME` | `DsParameter_DateTime` |  |  |  |
| 15 | `DS.PARAM.AUTHORISER` | `DsParameter_Authoriser` | String |  |  |
| 16 | `DS.PARAM.CO.CODE` | `DsParameter_CoCode` | String |  |  |
| 17 | `DS.PARAM.DEPT.CODE` | `DsParameter_DeptCode` | String |  |  |
| 18 | `DS.PARAM.AUDITOR.CODE` | `DsParameter_AuditorCode` | String |  |  |
| 19 | `DS.PARAM.AUDIT.DATE.TIME` | `DsParameter_AuditDateTime` | String |  |  |
