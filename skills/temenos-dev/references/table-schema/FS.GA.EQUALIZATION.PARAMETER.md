# FS.GA.EQUALIZATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUALIZATION.PARAMETER` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUALIZATION.PARAMETER.PARENT.REF.ID` | `FsGaEqualizationParameter_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUALIZATION.PARAMETER.ORA.ROWID` | `FsGaEqualizationParameter_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUALIZATION.PARAMETER.CHART.OF.ACCOUNTS.CODE` | `FsGaEqualizationParameter_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.EQUALIZATION.PARAMETER.EQUALISATION.CHART` | `FsGaEqualizationParameter_EqualisationChart` | TField |  | Enter equalization chart number. Multifonds DB Column is NRUBR_REGUL. |
| 5 | `FS.GA.EQUALIZATION.PARAMETER.PRINT.SUB.SEQUENCE.1` | `FsGaEqualizationParameter_PrintSubSequence1` | TField |  | Level of printing desired report Multifonds DB Column is SEQ. |
| 6 | `FS.GA.EQUALIZATION.PARAMETER.PRINT.SUB.SEQUENCE.LEVEL` | `FsGaEqualizationParameter_PrintSubSequenceLevel` | TField |  | Level of printing desired report Multifonds DB Column is SEQ_1. |
| 7 | `FS.GA.EQUALIZATION.PARAMETER.PRINT.SEQUENCE.LEVEL` | `FsGaEqualizationParameter_PrintSequenceLevel` | TField |  | Level of printing desired report Multifonds DB Column is SEQ_2. |
| 8 | `FS.GA.EQUALIZATION.PARAMETER.PRINT.DETAIL.LEVEL` | `FsGaEqualizationParameter_PrintDetailLevel` | TField |  | Level of printing desired report Multifonds DB Column is PRT_DETAIL. |
| 9 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED10` | `FsGaEqualizationParameter_Reserved10` | TField |  |  |
| 10 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED9` | `FsGaEqualizationParameter_Reserved9` | TField |  |  |
| 11 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED8` | `FsGaEqualizationParameter_Reserved8` | TField |  |  |
| 12 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED7` | `FsGaEqualizationParameter_Reserved7` | TField |  |  |
| 13 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED6` | `FsGaEqualizationParameter_Reserved6` | TField |  |  |
| 14 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED5` | `FsGaEqualizationParameter_Reserved5` | TField |  |  |
| 15 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED4` | `FsGaEqualizationParameter_Reserved4` | TField |  |  |
| 16 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED3` | `FsGaEqualizationParameter_Reserved3` | TField |  |  |
| 17 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED2` | `FsGaEqualizationParameter_Reserved2` | TField |  |  |
| 18 | `FS.GA.EQUALIZATION.PARAMETER.RESERVED1` | `FsGaEqualizationParameter_Reserved1` | TField |  |  |
| 19 | `FS.GA.EQUALIZATION.PARAMETER.LOCAL.REF` | `FsGaEqualizationParameter_LocalRef` |  |  |  |
| 20 | `FS.GA.EQUALIZATION.PARAMETER.OVERRIDE` | `FsGaEqualizationParameter_Override` |  |  |  |
| 21 | `FS.GA.EQUALIZATION.PARAMETER.RECORD.STATUS` | `FsGaEqualizationParameter_RecordStatus` | String |  |  |
| 22 | `FS.GA.EQUALIZATION.PARAMETER.CURR.NO` | `FsGaEqualizationParameter_CurrNo` | String |  |  |
| 23 | `FS.GA.EQUALIZATION.PARAMETER.INPUTTER` | `FsGaEqualizationParameter_Inputter` |  |  |  |
| 24 | `FS.GA.EQUALIZATION.PARAMETER.DATE.TIME` | `FsGaEqualizationParameter_DateTime` |  |  |  |
| 25 | `FS.GA.EQUALIZATION.PARAMETER.AUTHORISER` | `FsGaEqualizationParameter_Authoriser` | String |  |  |
| 26 | `FS.GA.EQUALIZATION.PARAMETER.CO.CODE` | `FsGaEqualizationParameter_CoCode` | String |  |  |
| 27 | `FS.GA.EQUALIZATION.PARAMETER.DEPT.CODE` | `FsGaEqualizationParameter_DeptCode` | String |  |  |
| 28 | `FS.GA.EQUALIZATION.PARAMETER.AUDITOR.CODE` | `FsGaEqualizationParameter_AuditorCode` | String |  |  |
| 29 | `FS.GA.EQUALIZATION.PARAMETER.AUDIT.DATE.TIME` | `FsGaEqualizationParameter_AuditDateTime` | String |  |  |
