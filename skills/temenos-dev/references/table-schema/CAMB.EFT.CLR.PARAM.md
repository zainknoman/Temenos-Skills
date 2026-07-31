# CAMB.EFT.CLR.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.EFT.CLR.PARAM` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.EFT.DATA.FILE.DIR` | `CambEftClrParam_DataFileDir` |  |  |  |
| 2 | `CAMB.EFT.DATA.FILENAME` | `CambEftClrParam_DataFilename` |  |  |  |
| 3 | `CAMB.EFT.LOG.DIR` | `CambEftClrParam_LogDir` |  |  |  |
| 4 | `CAMB.EFT.LOG.FILENAME` | `CambEftClrParam_LogFilename` |  |  |  |
| 5 | `CAMB.EFT.SEQUENCE.NO` | `CambEftClrParam_SequenceNo` |  |  |  |
| 6 | `CAMB.EFT.PRE.PROCESS` | `CambEftClrParam_PreProcess` |  |  |  |
| 7 | `CAMB.EFT.POST.PROCESS` | `CambEftClrParam_PostProcess` |  |  |  |
| 8 | `CAMB.EFT.PROCESS.DEPENDENCY` | `CambEftClrParam_ProcessDependency` |  |  |  |
| 9 | `CAMB.EFT.DEPENDENCY.FLAG` | `CambEftClrParam_DependencyFlag` |  |  |  |
| 10 | `CAMB.EFT.REVERSAL.SEQ.NO` | `CambEftClrParam_ReversalSeqNo` |  |  |  |
| 11 | `CAMB.EFT.REV.PROCESS.DATE` | `CambEftClrParam_RevProcessDate` |  |  |  |
| 12 | `CAMB.EFT.ORIGINATOR.ID` | `CambEftClrParam_OriginatorId` |  |  |  |
| 13 | `CAMB.EFT.RED.STAGE` | `CambEftClrParam_RedStage` |  |  |  |
| 14 | `CAMB.EFT.PURGE.DAYS` | `CambEftClrParam_PurgeDays` |  |  |  |
| 15 | `CAMB.EFT.NOTICE.FILENAME` | `CambEftClrParam_NoticeFilename` |  |  |  |
| 16 | `CAMB.EFT.RET.FILE.DIR` | `CambEftClrParam_RetFileDir` |  |  |  |
| 17 | `CAMB.EFT.RET.FILENAME` | `CambEftClrParam_RetFilename` |  |  |  |
| 18 | `CAMB.EFT.STATIC.HEADER` | `CambEftClrParam_StaticHeader` |  |  |  |
| 19 | `CAMB.EFT.DEF.DELIMITER.ASC` | `CambEftClrParam_DefDelimiterAsc` |  |  |  |
| 20 | `CAMB.EFT.DELIM.SRC.ASC` | `CambEftClrParam_DelimSrcAsc` |  |  |  |
| 21 | `CAMB.EFT.DELIM.REPL.ASC` | `CambEftClrParam_DelimReplAsc` |  |  |  |
| 22 | `CAMB.EFT.RETURN.SEQ.NO` | `CambEftClrParam_ReturnSeqNo` |  |  |  |
| 23 | `CAMB.EFT.DFE.REC.TYPE.C` | `CambEftClrParam_DfeRecTypeC` |  |  |  |
| 24 | `CAMB.EFT.DFE.REC.TYPE.D` | `CambEftClrParam_DfeRecTypeD` |  |  |  |
| 25 | `CAMB.EFT.DFE.REC.TYPE.E` | `CambEftClrParam_DfeRecTypeE` |  |  |  |
| 26 | `CAMB.EFT.DFE.REC.TYPE.F` | `CambEftClrParam_DfeRecTypeF` |  |  |  |
| 27 | `CAMB.EFT.DFE.REC.TYPE.I` | `CambEftClrParam_DfeRecTypeI` |  |  |  |
| 28 | `CAMB.EFT.DFE.REC.TYPE.J` | `CambEftClrParam_DfeRecTypeJ` |  |  |  |
| 29 | `CAMB.EFT.VALUE.DATE` | `CambEftClrParam_ValueDate` |  |  |  |
| 30 | `CAMB.EFT.TXN.POSTING.DATE` | `CambEftClrParam_TxnPostingDate` |  |  |  |
| 31 | `CAMB.EFT.RESERVED.3` | `CambEftClrParam_Reserved3` |  |  |  |
| 32 | `CAMB.EFT.RESERVED.2` | `CambEftClrParam_Reserved2` |  |  |  |
| 33 | `CAMB.EFT.RESERVED.1` | `CambEftClrParam_Reserved1` |  |  |  |
| 34 | `CAMB.EFT.LOCAL.REF` | `CambEftClrParam_LocalRef` |  |  |  |
| 35 | `CAMB.EFT.OVERRIDE` | `CambEftClrParam_Override` |  |  |  |
| 36 | `CAMB.EFT.RECORD.STATUS` | `CambEftClrParam_RecordStatus` |  |  |  |
| 37 | `CAMB.EFT.CURR.NO` | `CambEftClrParam_CurrNo` |  |  |  |
| 38 | `CAMB.EFT.INPUTTER` | `CambEftClrParam_Inputter` |  |  |  |
| 39 | `CAMB.EFT.DATE.TIME` | `CambEftClrParam_DateTime` |  |  |  |
| 40 | `CAMB.EFT.AUTHORISER` | `CambEftClrParam_Authoriser` |  |  |  |
| 41 | `CAMB.EFT.CO.CODE` | `CambEftClrParam_CoCode` |  |  |  |
| 42 | `CAMB.EFT.DEPT.CODE` | `CambEftClrParam_DeptCode` |  |  |  |
| 43 | `CAMB.EFT.AUDITOR.CODE` | `CambEftClrParam_AuditorCode` |  |  |  |
| 44 | `CAMB.EFT.AUDIT.DATE.TIME` | `CambEftClrParam_AuditDateTime` |  |  |  |
