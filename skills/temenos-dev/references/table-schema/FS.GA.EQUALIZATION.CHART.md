# FS.GA.EQUALIZATION.CHART — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUALIZATION.CHART` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUALIZATION.CHART.PARENT.REF.ID` | `FsGaEqualizationChart_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUALIZATION.CHART.ORA.ROWID` | `FsGaEqualizationChart_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUALIZATION.CHART.CHART.OF.ACCOUNTS.CODE` | `FsGaEqualizationChart_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.EQUALIZATION.CHART.GL.ACCOUNT` | `FsGaEqualizationChart_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.EQUALIZATION.CHART.BS.GROUPING` | `FsGaEqualizationChart_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 6 | `FS.GA.EQUALIZATION.CHART.DESCRIPTION` | `FsGaEqualizationChart_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.EQUALIZATION.CHART.PRINT.SUB.SEQUENCE.1` | `FsGaEqualizationChart_PrintSubSequence1` | TField |  | Level of printing desired report Multifonds DB Column is SEQ. |
| 8 | `FS.GA.EQUALIZATION.CHART.QUOTATION.TYPE` | `FsGaEqualizationChart_QuotationType` | TField |  | Quatation Type Multifonds DB Column is CTYPE. |
| 9 | `FS.GA.EQUALIZATION.CHART.AKTIENGEWINN.GROUP` | `FsGaEqualizationChart_AktiengewinnGroup` | TField |  | Master group (Equity/Non equity) used to determine AG expenses allocation ratio Multifonds DB Column is AKTIENGEWINN_GRP. |
| 10 | `FS.GA.EQUALIZATION.CHART.INCOME.OR.REALISED` | `FsGaEqualizationChart_IncomeOrRealised` | TField |  | Income or realised results Multifonds DB Column is FLG_IR. |
| 11 | `FS.GA.EQUALIZATION.CHART.TG.ACCOUNT.NUMBER` | `FsGaEqualizationChart_TgAccountNumber` | TField |  | Level of printing desired report Multifonds DB Column is NRUBR_TG. |
| 12 | `FS.GA.EQUALIZATION.CHART.ADJUST.POSITION.CATEGORY` | `FsGaEqualizationChart_AdjustPositionCategory` | TField |  | Level of printing desired report Multifonds DB Column is ADJ_POS_CATG. |
| 13 | `FS.GA.EQUALIZATION.CHART.RESERVED10` | `FsGaEqualizationChart_Reserved10` | TField |  |  |
| 14 | `FS.GA.EQUALIZATION.CHART.RESERVED9` | `FsGaEqualizationChart_Reserved9` | TField |  |  |
| 15 | `FS.GA.EQUALIZATION.CHART.RESERVED8` | `FsGaEqualizationChart_Reserved8` | TField |  |  |
| 16 | `FS.GA.EQUALIZATION.CHART.RESERVED7` | `FsGaEqualizationChart_Reserved7` | TField |  |  |
| 17 | `FS.GA.EQUALIZATION.CHART.RESERVED6` | `FsGaEqualizationChart_Reserved6` | TField |  |  |
| 18 | `FS.GA.EQUALIZATION.CHART.RESERVED5` | `FsGaEqualizationChart_Reserved5` | TField |  |  |
| 19 | `FS.GA.EQUALIZATION.CHART.RESERVED4` | `FsGaEqualizationChart_Reserved4` | TField |  |  |
| 20 | `FS.GA.EQUALIZATION.CHART.RESERVED3` | `FsGaEqualizationChart_Reserved3` | TField |  |  |
| 21 | `FS.GA.EQUALIZATION.CHART.RESERVED2` | `FsGaEqualizationChart_Reserved2` | TField |  |  |
| 22 | `FS.GA.EQUALIZATION.CHART.RESERVED1` | `FsGaEqualizationChart_Reserved1` | TField |  |  |
| 23 | `FS.GA.EQUALIZATION.CHART.LOCAL.REF` | `FsGaEqualizationChart_LocalRef` |  |  |  |
| 24 | `FS.GA.EQUALIZATION.CHART.OVERRIDE` | `FsGaEqualizationChart_Override` |  |  |  |
| 25 | `FS.GA.EQUALIZATION.CHART.RECORD.STATUS` | `FsGaEqualizationChart_RecordStatus` | String |  |  |
| 26 | `FS.GA.EQUALIZATION.CHART.CURR.NO` | `FsGaEqualizationChart_CurrNo` | String |  |  |
| 27 | `FS.GA.EQUALIZATION.CHART.INPUTTER` | `FsGaEqualizationChart_Inputter` |  |  |  |
| 28 | `FS.GA.EQUALIZATION.CHART.DATE.TIME` | `FsGaEqualizationChart_DateTime` |  |  |  |
| 29 | `FS.GA.EQUALIZATION.CHART.AUTHORISER` | `FsGaEqualizationChart_Authoriser` | String |  |  |
| 30 | `FS.GA.EQUALIZATION.CHART.CO.CODE` | `FsGaEqualizationChart_CoCode` | String |  |  |
| 31 | `FS.GA.EQUALIZATION.CHART.DEPT.CODE` | `FsGaEqualizationChart_DeptCode` | String |  |  |
| 32 | `FS.GA.EQUALIZATION.CHART.AUDITOR.CODE` | `FsGaEqualizationChart_AuditorCode` | String |  |  |
| 33 | `FS.GA.EQUALIZATION.CHART.AUDIT.DATE.TIME` | `FsGaEqualizationChart_AuditDateTime` | String |  |  |
