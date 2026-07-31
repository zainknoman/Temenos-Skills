# FS.GA.USER.DEFINED.FIELD.FUTURE — Table Schema

> Source: `INSERTS/I_F.FS.GA.USER.DEFINED.FIELD.FUTURE` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.USER.DEFINED.FIELD.FUTURE.FUTURE.ID.CODE` | `FsGaUserDefinedFieldFuture_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 2 | `FS.GA.USER.DEFINED.FIELD.FUTURE.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUserDefinedFieldFuture_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 3 | `FS.GA.USER.DEFINED.FIELD.FUTURE.UDF.CODE` | `FsGaUserDefinedFieldFuture_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 4 | `FS.GA.USER.DEFINED.FIELD.FUTURE.MANDATORY.OR.OPTIONAL` | `FsGaUserDefinedFieldFuture_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 5 | `FS.GA.USER.DEFINED.FIELD.FUTURE.SHORT.CODE` | `FsGaUserDefinedFieldFuture_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 6 | `FS.GA.USER.DEFINED.FIELD.FUTURE.LONGDESCRIPTION` | `FsGaUserDefinedFieldFuture_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 7 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED10` | `FsGaUserDefinedFieldFuture_Reserved10` | TField |  |  |
| 8 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED9` | `FsGaUserDefinedFieldFuture_Reserved9` | TField |  |  |
| 9 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED8` | `FsGaUserDefinedFieldFuture_Reserved8` | TField |  |  |
| 10 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED7` | `FsGaUserDefinedFieldFuture_Reserved7` | TField |  |  |
| 11 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED6` | `FsGaUserDefinedFieldFuture_Reserved6` | TField |  |  |
| 12 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED5` | `FsGaUserDefinedFieldFuture_Reserved5` | TField |  |  |
| 13 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED4` | `FsGaUserDefinedFieldFuture_Reserved4` | TField |  |  |
| 14 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED3` | `FsGaUserDefinedFieldFuture_Reserved3` | TField |  |  |
| 15 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED2` | `FsGaUserDefinedFieldFuture_Reserved2` | TField |  |  |
| 16 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RESERVED1` | `FsGaUserDefinedFieldFuture_Reserved1` | TField |  |  |
| 17 | `FS.GA.USER.DEFINED.FIELD.FUTURE.RECORD.STATUS` | `FsGaUserDefinedFieldFuture_RecordStatus` | String |  |  |
| 18 | `FS.GA.USER.DEFINED.FIELD.FUTURE.CURR.NO` | `FsGaUserDefinedFieldFuture_CurrNo` | String |  |  |
| 19 | `FS.GA.USER.DEFINED.FIELD.FUTURE.INPUTTER` | `FsGaUserDefinedFieldFuture_Inputter` |  |  |  |
| 20 | `FS.GA.USER.DEFINED.FIELD.FUTURE.DATE.TIME` | `FsGaUserDefinedFieldFuture_DateTime` |  |  |  |
| 21 | `FS.GA.USER.DEFINED.FIELD.FUTURE.AUTHORISER` | `FsGaUserDefinedFieldFuture_Authoriser` | String |  |  |
| 22 | `FS.GA.USER.DEFINED.FIELD.FUTURE.CO.CODE` | `FsGaUserDefinedFieldFuture_CoCode` | String |  |  |
| 23 | `FS.GA.USER.DEFINED.FIELD.FUTURE.DEPT.CODE` | `FsGaUserDefinedFieldFuture_DeptCode` | String |  |  |
| 24 | `FS.GA.USER.DEFINED.FIELD.FUTURE.AUDITOR.CODE` | `FsGaUserDefinedFieldFuture_AuditorCode` | String |  |  |
| 25 | `FS.GA.USER.DEFINED.FIELD.FUTURE.AUDIT.DATE.TIME` | `FsGaUserDefinedFieldFuture_AuditDateTime` | String |  |  |
