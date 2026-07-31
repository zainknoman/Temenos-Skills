# FS.GA.NAV.CHART — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CHART` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CHART.PARENT.REF.ID` | `FsGaNavChart_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CHART.ORA.ROWID` | `FsGaNavChart_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CHART.CHART.OF.ACCOUNTS.CODE` | `FsGaNavChart_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.NAV.CHART.GL.ACCOUNT` | `FsGaNavChart_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.NAV.CHART.BS.GROUPING` | `FsGaNavChart_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 6 | `FS.GA.NAV.CHART.DESCRIPTION` | `FsGaNavChart_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.NAV.CHART.BS.SUB.GROUPING` | `FsGaNavChart_BsSubGrouping` | TField |  | Balance sheet sub grouping Multifonds DB Column is CTIF2. |
| 8 | `FS.GA.NAV.CHART.DETAIL.OR.TOTAL` | `FsGaNavChart_DetailOrTotal` | TField |  | Detailed or Total information Multifonds DB Column is CDTOT. |
| 9 | `FS.GA.NAV.CHART.PRINT.NAV.IML` | `FsGaNavChart_PrintNavIml` | TField |  | Flag Y or N for printing the group in NAV IML reports Multifonds DB Column is FLAG_IMP_NAV. |
| 10 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.1` | `FsGaNavChart_ForSubtotal1` | TField |  | Not in use in the system - SubTotal 1 on NAV Chart Multifonds DB Column is SOUS_TOT1. |
| 11 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.2` | `FsGaNavChart_ForSubtotal2` | TField |  | Not in use in the system - SubTotal 2 on NAV Chart Multifonds DB Column is SOUS_TOT2. |
| 12 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.3` | `FsGaNavChart_ForSubtotal3` | TField |  | Not in use in the system - SubTotal 3 on NAV Chart Multifonds DB Column is SOUS_TOT3. |
| 13 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.4` | `FsGaNavChart_ForSubtotal4` | TField |  | Not in use in the system - SubTotal 4 on NAV Chart Multifonds DB Column is SOUS_TOT4. |
| 14 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.5` | `FsGaNavChart_ForSubtotal5` | TField |  | Not in use in the system - SubTotal 5 on NAV Chart Multifonds DB Column is SOUS_TOT5. |
| 15 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.6` | `FsGaNavChart_ForSubtotal6` | TField |  | Not in use in the system - SubTotal 6 on NAV Chart Multifonds DB Column is SOUS_TOT6. |
| 16 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.7` | `FsGaNavChart_ForSubtotal7` | TField |  | Not in use in the system - SubTotal 7 on NAV Chart Multifonds DB Column is SOUS_TOT7. |
| 17 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.8` | `FsGaNavChart_ForSubtotal8` | TField |  | Not in use in the system - SubTotal 8 on NAV Chart Multifonds DB Column is SOUS_TOT8. |
| 18 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.9` | `FsGaNavChart_ForSubtotal9` | TField |  | Not in use in the system - SubTotal 9 on NAV Chart Multifonds DB Column is SOUS_TOT9. |
| 19 | `FS.GA.NAV.CHART.FOR.SUBTOTAL.10` | `FsGaNavChart_ForSubtotal10` | TField |  | Not in use in the system - SubTotal 10 on NAV Chart Multifonds DB Column is SOUS_TOT10. |
| 20 | `FS.GA.NAV.CHART.DETAIL` | `FsGaNavChart_Detail` | TField |  | Flag Y or N for printing the details in NAV reports Multifonds DB Column is FLG_DETAIL. |
| 21 | `FS.GA.NAV.CHART.RESERVED10` | `FsGaNavChart_Reserved10` | TField |  |  |
| 22 | `FS.GA.NAV.CHART.RESERVED9` | `FsGaNavChart_Reserved9` | TField |  |  |
| 23 | `FS.GA.NAV.CHART.RESERVED8` | `FsGaNavChart_Reserved8` | TField |  |  |
| 24 | `FS.GA.NAV.CHART.RESERVED7` | `FsGaNavChart_Reserved7` | TField |  |  |
| 25 | `FS.GA.NAV.CHART.RESERVED6` | `FsGaNavChart_Reserved6` | TField |  |  |
| 26 | `FS.GA.NAV.CHART.RESERVED5` | `FsGaNavChart_Reserved5` | TField |  |  |
| 27 | `FS.GA.NAV.CHART.RESERVED4` | `FsGaNavChart_Reserved4` | TField |  |  |
| 28 | `FS.GA.NAV.CHART.RESERVED3` | `FsGaNavChart_Reserved3` | TField |  |  |
| 29 | `FS.GA.NAV.CHART.RESERVED2` | `FsGaNavChart_Reserved2` | TField |  |  |
| 30 | `FS.GA.NAV.CHART.RESERVED1` | `FsGaNavChart_Reserved1` | TField |  |  |
| 31 | `FS.GA.NAV.CHART.LOCAL.REF` | `FsGaNavChart_LocalRef` |  |  |  |
| 32 | `FS.GA.NAV.CHART.OVERRIDE` | `FsGaNavChart_Override` |  |  |  |
| 33 | `FS.GA.NAV.CHART.RECORD.STATUS` | `FsGaNavChart_RecordStatus` | String |  |  |
| 34 | `FS.GA.NAV.CHART.CURR.NO` | `FsGaNavChart_CurrNo` | String |  |  |
| 35 | `FS.GA.NAV.CHART.INPUTTER` | `FsGaNavChart_Inputter` |  |  |  |
| 36 | `FS.GA.NAV.CHART.DATE.TIME` | `FsGaNavChart_DateTime` |  |  |  |
| 37 | `FS.GA.NAV.CHART.AUTHORISER` | `FsGaNavChart_Authoriser` | String |  |  |
| 38 | `FS.GA.NAV.CHART.CO.CODE` | `FsGaNavChart_CoCode` | String |  |  |
| 39 | `FS.GA.NAV.CHART.DEPT.CODE` | `FsGaNavChart_DeptCode` | String |  |  |
| 40 | `FS.GA.NAV.CHART.AUDITOR.CODE` | `FsGaNavChart_AuditorCode` | String |  |  |
| 41 | `FS.GA.NAV.CHART.AUDIT.DATE.TIME` | `FsGaNavChart_AuditDateTime` | String |  |  |
