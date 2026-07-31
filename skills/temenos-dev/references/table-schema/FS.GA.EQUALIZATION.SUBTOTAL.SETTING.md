# FS.GA.EQUALIZATION.SUBTOTAL.SETTING — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUALIZATION.SUBTOTAL.SETTING` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.PARENT.REF.ID` | `FsGaEqualizationSubtotalSetting_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.ORA.ROWID` | `FsGaEqualizationSubtotalSetting_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.CHART.OF.ACCOUNTS.CODE` | `FsGaEqualizationSubtotalSetting_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.PRINT.SUB.SEQUENCE.1` | `FsGaEqualizationSubtotalSetting_PrintSubSequence1` | TField |  | Level of printing desired report Multifonds DB Column is SEQ. |
| 5 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.PRINT.SUB.SEQUENCE.LEVEL` | `FsGaEqualizationSubtotalSetting_PrintSubSequenceLevel` | TField |  | Level of printing desired report Multifonds DB Column is SEQ_1. |
| 6 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.PRINT.SEQUENCE.LEVEL` | `FsGaEqualizationSubtotalSetting_PrintSequenceLevel` | TField |  | Level of printing desired report Multifonds DB Column is SEQ_2. |
| 7 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.LANGUAGE` | `FsGaEqualizationSubtotalSetting_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 8 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.DESCRIPTION` | `FsGaEqualizationSubtotalSetting_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 9 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED10` | `FsGaEqualizationSubtotalSetting_Reserved10` | TField |  |  |
| 10 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED9` | `FsGaEqualizationSubtotalSetting_Reserved9` | TField |  |  |
| 11 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED8` | `FsGaEqualizationSubtotalSetting_Reserved8` | TField |  |  |
| 12 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED7` | `FsGaEqualizationSubtotalSetting_Reserved7` | TField |  |  |
| 13 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED6` | `FsGaEqualizationSubtotalSetting_Reserved6` | TField |  |  |
| 14 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED5` | `FsGaEqualizationSubtotalSetting_Reserved5` | TField |  |  |
| 15 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED4` | `FsGaEqualizationSubtotalSetting_Reserved4` | TField |  |  |
| 16 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED3` | `FsGaEqualizationSubtotalSetting_Reserved3` | TField |  |  |
| 17 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED2` | `FsGaEqualizationSubtotalSetting_Reserved2` | TField |  |  |
| 18 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RESERVED1` | `FsGaEqualizationSubtotalSetting_Reserved1` | TField |  |  |
| 19 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.LOCAL.REF` | `FsGaEqualizationSubtotalSetting_LocalRef` |  |  |  |
| 20 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.OVERRIDE` | `FsGaEqualizationSubtotalSetting_Override` |  |  |  |
| 21 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.RECORD.STATUS` | `FsGaEqualizationSubtotalSetting_RecordStatus` | String |  |  |
| 22 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.CURR.NO` | `FsGaEqualizationSubtotalSetting_CurrNo` | String |  |  |
| 23 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.INPUTTER` | `FsGaEqualizationSubtotalSetting_Inputter` |  |  |  |
| 24 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.DATE.TIME` | `FsGaEqualizationSubtotalSetting_DateTime` |  |  |  |
| 25 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.AUTHORISER` | `FsGaEqualizationSubtotalSetting_Authoriser` | String |  |  |
| 26 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.CO.CODE` | `FsGaEqualizationSubtotalSetting_CoCode` | String |  |  |
| 27 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.DEPT.CODE` | `FsGaEqualizationSubtotalSetting_DeptCode` | String |  |  |
| 28 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.AUDITOR.CODE` | `FsGaEqualizationSubtotalSetting_AuditorCode` | String |  |  |
| 29 | `FS.GA.EQUALIZATION.SUBTOTAL.SETTING.AUDIT.DATE.TIME` | `FsGaEqualizationSubtotalSetting_AuditDateTime` | String |  |  |
