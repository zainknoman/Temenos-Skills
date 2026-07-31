# CAPL.FTCL.STATUS — Table Schema

> Source: `INSERTS/I_F.CAPL.FTCL.STATUS` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FTCL.STATS.FILE.PROCESS` | `CaplFtclStatus_FileProcess` |  |  |  |
| 2 | `FTCL.STATS.STATUS` | `CaplFtclStatus_Status` |  |  |  |
| 3 | `FTCL.STATS.STATUS.DATE` | `CaplFtclStatus_StatusDate` |  |  |  |
| 4 | `FTCL.STATS.STATUS.TIME` | `CaplFtclStatus_StatusTime` |  |  |  |
| 5 | `FTCL.STATS.STATUS.UPDATED.BY` | `CaplFtclStatus_StatusUpdatedBy` |  |  |  |
| 6 | `FTCL.STATS.ERROR.DETAILS` | `CaplFtclStatus_ErrorDetails` |  |  |  |
| 7 | `FTCL.STATS.BRANCH.NO` | `CaplFtclStatus_BranchNo` |  |  |  |
| 8 | `FTCL.STATS.TXN.CNT` | `CaplFtclStatus_TxnCnt` |  |  |  |
| 9 | `FTCL.STATS.MAX.CNT` | `CaplFtclStatus_MaxCnt` |  |  |  |
| 10 | `FTCL.STATS.BRANCH.STATUS` | `CaplFtclStatus_BranchStatus` |  |  |  |
| 11 | `FTCL.STATS.MAX.BRANCH` | `CaplFtclStatus_MaxBranch` |  |  |  |
| 12 | `FTCL.STATS.RESERVED.5` | `CaplFtclStatus_Reserved5` |  |  |  |
| 13 | `FTCL.STATS.RESERVED.4` | `CaplFtclStatus_Reserved4` |  |  |  |
| 14 | `FTCL.STATS.RESERVED.3` | `CaplFtclStatus_Reserved3` |  |  |  |
| 15 | `FTCL.STATS.RESERVED.2` | `CaplFtclStatus_Reserved2` |  |  |  |
| 16 | `FTCL.STATS.RESERVED.1` | `CaplFtclStatus_Reserved1` |  |  |  |
| 17 | `FTCL.STATS.LOCAL.REF` | `CaplFtclStatus_LocalRef` |  |  |  |
| 18 | `FTCL.STATS.OVERRIDE` | `CaplFtclStatus_Override` |  |  |  |
| 19 | `FTCL.STATS.RECORD.STATUS` | `CaplFtclStatus_RecordStatus` |  |  |  |
| 20 | `FTCL.STATS.CURR.NO` | `CaplFtclStatus_CurrNo` |  |  |  |
| 21 | `FTCL.STATS.INPUTTER` | `CaplFtclStatus_Inputter` |  |  |  |
| 22 | `FTCL.STATS.DATE.TIME` | `CaplFtclStatus_DateTime` |  |  |  |
| 23 | `FTCL.STATS.AUTHORISER` | `CaplFtclStatus_Authoriser` |  |  |  |
| 24 | `FTCL.STATS.CO.CODE` | `CaplFtclStatus_CoCode` |  |  |  |
| 25 | `FTCL.STATS.DEPT.CODE` | `CaplFtclStatus_DeptCode` |  |  |  |
| 26 | `FTCL.STATS.AUDITOR.CODE` | `CaplFtclStatus_AuditorCode` |  |  |  |
| 27 | `FTCL.STATS.AUDIT.DATE.TIME` | `CaplFtclStatus_AuditDateTime` |  |  |  |
