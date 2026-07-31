# FS.GI.LP.GL.CONSOLIDATION.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.CONSOLIDATION.PROCESS` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.PARENT.REF.ID` | `FsGiLpGlConsolidationProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.ORA.ROWID` | `FsGiLpGlConsolidationProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.TA.FUND.ID` | `FsGiLpGlConsolidationProcess_TaFundId` | TField |  | TA Fund internal identification. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.SHARE.CLASS.CODE` | `FsGiLpGlConsolidationProcess_ShareClassCode` | TField |  | Share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.FUND.ID` | `FsGiLpGlConsolidationProcess_FundId` | TField |  | MF Fund internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 6 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.NAV.DATE` | `FsGiLpGlConsolidationProcess_NavDate` | TField |  | Nav Date. Multifonds DB Column is NAVDATE. |
| 7 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.BREAK.PERIOD.END.DATE` | `FsGiLpGlConsolidationProcess_BreakPeriodEndDate` | TField |  | Break period end date. Multifonds DB Column is BP_END_DATE. |
| 8 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.LAST.DATE` | `FsGiLpGlConsolidationProcess_LastDate` | TField |  | Last processing date. Multifonds DB Column is LAST_DATE. |
| 9 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED10` | `FsGiLpGlConsolidationProcess_Reserved10` | TField |  |  |
| 10 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED9` | `FsGiLpGlConsolidationProcess_Reserved9` | TField |  |  |
| 11 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED8` | `FsGiLpGlConsolidationProcess_Reserved8` | TField |  |  |
| 12 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED7` | `FsGiLpGlConsolidationProcess_Reserved7` | TField |  |  |
| 13 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED6` | `FsGiLpGlConsolidationProcess_Reserved6` | TField |  |  |
| 14 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED5` | `FsGiLpGlConsolidationProcess_Reserved5` | TField |  |  |
| 15 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED4` | `FsGiLpGlConsolidationProcess_Reserved4` | TField |  |  |
| 16 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED3` | `FsGiLpGlConsolidationProcess_Reserved3` | TField |  |  |
| 17 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED2` | `FsGiLpGlConsolidationProcess_Reserved2` | TField |  |  |
| 18 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RESERVED1` | `FsGiLpGlConsolidationProcess_Reserved1` | TField |  |  |
| 19 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.LOCAL.REF` | `FsGiLpGlConsolidationProcess_LocalRef` |  |  |  |
| 20 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.OVERRIDE` | `FsGiLpGlConsolidationProcess_Override` |  |  |  |
| 21 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.RECORD.STATUS` | `FsGiLpGlConsolidationProcess_RecordStatus` | String |  |  |
| 22 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.CURR.NO` | `FsGiLpGlConsolidationProcess_CurrNo` | String |  |  |
| 23 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.INPUTTER` | `FsGiLpGlConsolidationProcess_Inputter` |  |  |  |
| 24 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.DATE.TIME` | `FsGiLpGlConsolidationProcess_DateTime` |  |  |  |
| 25 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.AUTHORISER` | `FsGiLpGlConsolidationProcess_Authoriser` | String |  |  |
| 26 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.CO.CODE` | `FsGiLpGlConsolidationProcess_CoCode` | String |  |  |
| 27 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.DEPT.CODE` | `FsGiLpGlConsolidationProcess_DeptCode` | String |  |  |
| 28 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.AUDITOR.CODE` | `FsGiLpGlConsolidationProcess_AuditorCode` | String |  |  |
| 29 | `FS.GI.LP.GL.CONSOLIDATION.PROCESS.AUDIT.DATE.TIME` | `FsGiLpGlConsolidationProcess_AuditDateTime` | String |  |  |
