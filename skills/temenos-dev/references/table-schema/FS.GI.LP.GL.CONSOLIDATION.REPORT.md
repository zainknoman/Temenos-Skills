# FS.GI.LP.GL.CONSOLIDATION.REPORT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.CONSOLIDATION.REPORT` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.FUND.ID` | `FsGiLpGlConsolidationReport_FundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.SHARE.CLASS.CODE` | `FsGiLpGlConsolidationReport_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 3 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.PROCESS.DATE` | `FsGiLpGlConsolidationReport_ProcessDate` | TField |  | Current break period end date. Multifonds DB Column is DPROCESS. |
| 4 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.DESCRIPTION` | `FsGiLpGlConsolidationReport_Description` | TField |  | Status of GL accounts balance consolidation process. Multifonds DB Column is LIBELLE. |
| 5 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED10` | `FsGiLpGlConsolidationReport_Reserved10` | TField |  |  |
| 6 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED9` | `FsGiLpGlConsolidationReport_Reserved9` | TField |  |  |
| 7 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED8` | `FsGiLpGlConsolidationReport_Reserved8` | TField |  |  |
| 8 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED7` | `FsGiLpGlConsolidationReport_Reserved7` | TField |  |  |
| 9 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED6` | `FsGiLpGlConsolidationReport_Reserved6` | TField |  |  |
| 10 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED5` | `FsGiLpGlConsolidationReport_Reserved5` | TField |  |  |
| 11 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED4` | `FsGiLpGlConsolidationReport_Reserved4` | TField |  |  |
| 12 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED3` | `FsGiLpGlConsolidationReport_Reserved3` | TField |  |  |
| 13 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED2` | `FsGiLpGlConsolidationReport_Reserved2` | TField |  |  |
| 14 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RESERVED1` | `FsGiLpGlConsolidationReport_Reserved1` | TField |  |  |
| 15 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.OVERRIDE` | `FsGiLpGlConsolidationReport_Override` |  |  |  |
| 16 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.LOCAL.REF` | `FsGiLpGlConsolidationReport_LocalRef` |  |  |  |
| 17 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.RECORD.STATUS` | `FsGiLpGlConsolidationReport_RecordStatus` | String |  |  |
| 18 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.CURR.NO` | `FsGiLpGlConsolidationReport_CurrNo` | String |  |  |
| 19 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.INPUTTER` | `FsGiLpGlConsolidationReport_Inputter` |  |  |  |
| 20 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.DATE.TIME` | `FsGiLpGlConsolidationReport_DateTime` |  |  |  |
| 21 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.AUTHORISER` | `FsGiLpGlConsolidationReport_Authoriser` | String |  |  |
| 22 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.CO.CODE` | `FsGiLpGlConsolidationReport_CoCode` | String |  |  |
| 23 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.DEPT.CODE` | `FsGiLpGlConsolidationReport_DeptCode` | String |  |  |
| 24 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.AUDITOR.CODE` | `FsGiLpGlConsolidationReport_AuditorCode` | String |  |  |
| 25 | `FS.GI.LP.GL.CONSOLIDATION.REPORT.AUDIT.DATE.TIME` | `FsGiLpGlConsolidationReport_AuditDateTime` | String |  |  |
