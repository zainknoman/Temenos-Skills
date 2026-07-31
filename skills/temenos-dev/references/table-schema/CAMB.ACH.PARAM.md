# CAMB.ACH.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.ACH.PARAM` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.PARM.DATA.FILE.DIR` | `CambAchParam_DataFileDir` |  |  |  |
| 2 | `ACH.PARM.DATA.FILENAME` | `CambAchParam_DataFilename` |  |  |  |
| 3 | `ACH.PARM.CR.DR.FILE` | `CambAchParam_CrDrFile` |  |  |  |
| 4 | `ACH.PARM.ORIGINATOR.ID` | `CambAchParam_OriginatorId` |  |  |  |
| 5 | `ACH.PARM.LOG.DIR` | `CambAchParam_LogDir` |  |  |  |
| 6 | `ACH.PARM.LOG.FILENAME` | `CambAchParam_LogFilename` |  |  |  |
| 7 | `ACH.PARM.PRE.PROCESS` | `CambAchParam_PreProcess` |  |  |  |
| 8 | `ACH.PARM.POST.PROCESS` | `CambAchParam_PostProcess` |  |  |  |
| 9 | `ACH.PARM.PROCESS.DEPENDENCY` | `CambAchParam_ProcessDependency` |  |  |  |
| 10 | `ACH.PARM.DEPENDENCY.FLAG` | `CambAchParam_DependencyFlag` |  |  |  |
| 11 | `ACH.PARM.PROD.HEADER` | `CambAchParam_ProdHeader` |  |  |  |
| 12 | `ACH.PARM.TEST.HEADER` | `CambAchParam_TestHeader` |  |  |  |
| 13 | `ACH.PARM.RUN.TYPE` | `CambAchParam_RunType` |  |  |  |
| 14 | `ACH.PARM.LEAD.DAYS` | `CambAchParam_LeadDays` |  |  |  |
| 15 | `ACH.PARM.ACH.HLD.DAYS` | `CambAchParam_AchHldDays` |  |  |  |
| 16 | `ACH.PARM.ACH.HLD.CAL` | `CambAchParam_AchHldCal` |  |  |  |
| 17 | `ACH.PARM.ACH.SEQ.NO` | `CambAchParam_AchSeqNo` |  |  |  |
| 18 | `ACH.PARM.ACH.DEP.INT.ERR` | `CambAchParam_AchDepIntErr` |  |  |  |
| 19 | `ACH.PARM.ACH.EXC.INT.ERR` | `CambAchParam_AchExcIntErr` |  |  |  |
| 20 | `ACH.PARM.ACH.OFS.SRC` | `CambAchParam_AchOfsSrc` |  |  |  |
| 21 | `ACH.PARM.ACH.HEADER.DR.RCL` | `CambAchParam_AchHeaderDrRcl` |  |  |  |
| 22 | `ACH.PARM.ACH.DR.DET.RCL` | `CambAchParam_AchDrDetRcl` |  |  |  |
| 23 | `ACH.PARM.ACH.TRAILER.DR.RCL` | `CambAchParam_AchTrailerDrRcl` |  |  |  |
| 24 | `ACH.PARM.ACH.HEADER.CR.RCL` | `CambAchParam_AchHeaderCrRcl` |  |  |  |
| 25 | `ACH.PARM.ACH.CR.DET.RCL` | `CambAchParam_AchCrDetRcl` |  |  |  |
| 26 | `ACH.PARM.ACH.TRAILER.CR.RCL` | `CambAchParam_AchTrailerCrRcl` |  |  |  |
| 27 | `ACH.PARM.ACH.HOLD.VERSION` | `CambAchParam_AchHoldVersion` |  |  |  |
| 28 | `ACH.PARM.PO.DR.DET.RCL` | `CambAchParam_PoDrDetRcl` |  |  |  |
| 29 | `ACH.PARM.PO.CR.DET.RCL` | `CambAchParam_PoCrDetRcl` |  |  |  |
| 30 | `ACH.PARM.INS.ID.RETURN` | `CambAchParam_InsIdReturn` |  |  |  |
| 31 | `ACH.PARM.ACC.NO.RETURN` | `CambAchParam_AccNoReturn` |  |  |  |
| 32 | `ACH.PARM.ORIG.SHORT.NAME` | `CambAchParam_OrigShortName` |  |  |  |
| 33 | `ACH.PARM.ORIG.LONG.NAME` | `CambAchParam_OrigLongName` |  |  |  |
| 34 | `ACH.PARM.DEST.DATA.CENTER` | `CambAchParam_DestDataCenter` |  |  |  |
| 35 | `ACH.PARM.NO.OF.RETRIES` | `CambAchParam_NoOfRetries` |  |  |  |
| 36 | `ACH.PARM.EFT.AUTOMATION` | `CambAchParam_EftAutomation` |  |  |  |
| 37 | `ACH.PARM.RESERVED.5` | `CambAchParam_Reserved5` |  |  |  |
| 38 | `ACH.PARM.RESERVED.4` | `CambAchParam_Reserved4` |  |  |  |
| 39 | `ACH.PARM.RESERVED.3` | `CambAchParam_Reserved3` |  |  |  |
| 40 | `ACH.PARM.RESERVED.2` | `CambAchParam_Reserved2` |  |  |  |
| 41 | `ACH.PARM.RESERVED.1` | `CambAchParam_Reserved1` |  |  |  |
| 42 | `ACH.PARM.RECORD.STATUS` | `CambAchParam_RecordStatus` |  |  |  |
| 43 | `ACH.PARM.CURR.NO` | `CambAchParam_CurrNo` |  |  |  |
| 44 | `ACH.PARM.INPUTTER` | `CambAchParam_Inputter` |  |  |  |
| 45 | `ACH.PARM.DATE.TIME` | `CambAchParam_DateTime` |  |  |  |
| 46 | `ACH.PARM.AUTHORISER` | `CambAchParam_Authoriser` |  |  |  |
| 47 | `ACH.PARM.CO.CODE` | `CambAchParam_CoCode` |  |  |  |
| 48 | `ACH.PARM.DEPT.CODE` | `CambAchParam_DeptCode` |  |  |  |
| 49 | `ACH.PARM.AUDITOR.CODE` | `CambAchParam_AuditorCode` |  |  |  |
| 50 | `ACH.PARM.AUDIT.DATE.TIME` | `CambAchParam_AuditDateTime` |  |  |  |
