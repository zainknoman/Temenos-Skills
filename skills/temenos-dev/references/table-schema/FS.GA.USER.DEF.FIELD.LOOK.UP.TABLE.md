# FS.GA.USER.DEF.FIELD.LOOK.UP.TABLE — Table Schema

> Source: `INSERTS/I_F.FS.GA.USER.DEF.FIELD.LOOK.UP.TABLE` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.USER.DEF.FIELD.LOOK.UP.LOOK.UP.TABLE` | `FsGaUserDefFieldLookUpTable_LookUpTable` | TField |  | User can create any code that is identified as Table. This field accepts any alphanumeric value up to 20 characters. Multifonds DB Column is UDF_LOOK_TAB. |
| 2 | `GA.USER.DEF.FIELD.LOOK.UP.LOOK.UP.TABLE.DESCRIPTION` | `FsGaUserDefFieldLookUpTable_LookUpTableDescription` | TField |  | Long Description of Table name allows the user to enter up to 80 alphanumeric characters for this field Multifonds DB Column is UDF_LOOK_TAB_DESC. |
| 3 | `GA.USER.DEF.FIELD.LOOK.UP.SCREEN.OR.TABLE` | `FsGaUserDefFieldLookUpTable_ScreenOrTable` | TField | No | User has to define correct Multifonds non-processing screen ID's or list of tables available in Central Register. This field is optional. Multifonds DB Column is SYS_SCRN_TAB. |
| 4 | `GA.USER.DEF.FIELD.LOOK.UP.SYSTEM.ELEMENT` | `FsGaUserDefFieldLookUpTable_SystemElement` | TField | No | This field provides drop down box with list of valid columns available for selected Multifonds screen. Optional field. Multifonds DB Column is SYS_CELEM. |
| 5 | `GA.USER.DEF.FIELD.LOOK.UP.ELEMENT.REFERENCE` | `FsGaUserDefFieldLookUpTable_ElementReference` | TField |  | Filters info. based on the param. in the 'Element' column. E.g. If 'Element' is param. with 'TYPE' systems filters the records by type and displays relevant info. for 'TYPE' viz. 'AM', 'BK','BR' etc. Multifonds DB Column is REF_TYPE. |
| 6 | `GA.USER.DEF.FIELD.LOOK.UP.SHORT.CODE` | `FsGaUserDefFieldLookUpTable_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 7 | `GA.USER.DEF.FIELD.LOOK.UP.LONGDESCRIPTION` | `FsGaUserDefFieldLookUpTable_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 8 | `GA.USER.DEF.FIELD.LOOK.UP.IFRS.DEFAULT.CATEGORY` | `FsGaUserDefFieldLookUpTable_IfrsDefaultCategory` | TField |  | IFRS default category like AFS, HTM etc for the GTI and Security predefined Multifonds DB Column is FLG_DEFAULT. |
| 9 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED10` | `FsGaUserDefFieldLookUpTable_Reserved10` | TField |  |  |
| 10 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED9` | `FsGaUserDefFieldLookUpTable_Reserved9` | TField |  |  |
| 11 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED8` | `FsGaUserDefFieldLookUpTable_Reserved8` | TField |  |  |
| 12 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED7` | `FsGaUserDefFieldLookUpTable_Reserved7` | TField |  |  |
| 13 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED6` | `FsGaUserDefFieldLookUpTable_Reserved6` | TField |  |  |
| 14 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED5` | `FsGaUserDefFieldLookUpTable_Reserved5` | TField |  |  |
| 15 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED4` | `FsGaUserDefFieldLookUpTable_Reserved4` | TField |  |  |
| 16 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED3` | `FsGaUserDefFieldLookUpTable_Reserved3` | TField |  |  |
| 17 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED2` | `FsGaUserDefFieldLookUpTable_Reserved2` | TField |  |  |
| 18 | `GA.USER.DEF.FIELD.LOOK.UP.RESERVED1` | `FsGaUserDefFieldLookUpTable_Reserved1` | TField |  |  |
| 19 | `GA.USER.DEF.FIELD.LOOK.UP.LOCAL.REF` | `FsGaUserDefFieldLookUpTable_LocalRef` |  |  |  |
| 20 | `GA.USER.DEF.FIELD.LOOK.UP.OVERRIDE` | `FsGaUserDefFieldLookUpTable_Override` |  |  |  |
| 21 | `GA.USER.DEF.FIELD.LOOK.UP.RECORD.STATUS` | `FsGaUserDefFieldLookUpTable_RecordStatus` | String |  |  |
| 22 | `GA.USER.DEF.FIELD.LOOK.UP.CURR.NO` | `FsGaUserDefFieldLookUpTable_CurrNo` | String |  |  |
| 23 | `GA.USER.DEF.FIELD.LOOK.UP.INPUTTER` | `FsGaUserDefFieldLookUpTable_Inputter` |  |  |  |
| 24 | `GA.USER.DEF.FIELD.LOOK.UP.DATE.TIME` | `FsGaUserDefFieldLookUpTable_DateTime` |  |  |  |
| 25 | `GA.USER.DEF.FIELD.LOOK.UP.AUTHORISER` | `FsGaUserDefFieldLookUpTable_Authoriser` | String |  |  |
| 26 | `GA.USER.DEF.FIELD.LOOK.UP.CO.CODE` | `FsGaUserDefFieldLookUpTable_CoCode` | String |  |  |
| 27 | `GA.USER.DEF.FIELD.LOOK.UP.DEPT.CODE` | `FsGaUserDefFieldLookUpTable_DeptCode` | String |  |  |
| 28 | `GA.USER.DEF.FIELD.LOOK.UP.AUDITOR.CODE` | `FsGaUserDefFieldLookUpTable_AuditorCode` | String |  |  |
| 29 | `GA.USER.DEF.FIELD.LOOK.UP.AUDIT.DATE.TIME` | `FsGaUserDefFieldLookUpTable_AuditDateTime` | String |  |  |
