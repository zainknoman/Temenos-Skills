# DFE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DFE.PARAMETER` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.PARAM.DESCRIPTION` | `DfeParameter_Description` |  |  |  |
| 2 | `DFE.PARAM.IN.OUT.TYPE` | `DfeParameter_InOutType` | TField |  |  |
| 3 | `DFE.PARAM.MODE.OF.TXN` | `DfeParameter_ModeOfTxn` | TField |  |  |
| 4 | `DFE.PARAM.MSG.POST.TYPE` | `DfeParameter_MsgPostType` | TField |  |  |
| 5 | `DFE.PARAM.UPLOAD.METHOD` | `DfeParameter_UploadMethod` | TField |  |  |
| 6 | `DFE.PARAM.RECORD.DELIMITER` | `DfeParameter_RecordDelimiter` | TField |  |  |
| 7 | `DFE.PARAM.DFE.MAPPING.ID` | `DfeParameter_DfeMappingId` | TField |  |  |
| 8 | `DFE.PARAM.NORMALIZE.DELIM` | `DfeParameter_NormalizeDelim` | TField |  |  |
| 9 | `DFE.PARAM.OFS.USER.NAME` | `DfeParameter_OfsUserName` | TField |  |  |
| 10 | `DFE.PARAM.OFS.SOURCE.ID` | `DfeParameter_OfsSourceId` | TField |  |  |
| 11 | `DFE.PARAM.OFS.VERSION` | `DfeParameter_OfsVersion` | TField |  |  |
| 12 | `DFE.PARAM.VALIDATE.IN.FILE` | `DfeParameter_ValidateInFile` | TField |  |  |
| 13 | `DFE.PARAM.GEN.EMPTY.FILE` | `DfeParameter_GenEmptyFile` | TField |  |  |
| 14 | `DFE.PARAM.MAINT.LOG.BY.COMP` | `DfeParameter_MaintLogByComp` | TField |  |  |
| 15 | `DFE.PARAM.MAINT.LOG.FILE` | `DfeParameter_MaintLogFile` | TField |  |  |
| 16 | `DFE.PARAM.MOVE.ERR.FILE` | `DfeParameter_MoveErrFile` | TField |  |  |
| 17 | `DFE.PARAM.REMOVE.ARC.FILE.EXT` | `DfeParameter_RemoveArcFileExt` | TField |  |  |
| 18 | `DFE.PARAM.INPUT.DIR` | `DfeParameter_InputDir` | TField |  |  |
| 19 | `DFE.PARAM.RESERVED.22` | `DfeParameter_Reserved22` | TField |  |  |
| 20 | `DFE.PARAM.OUTPUT.DIR` | `DfeParameter_OutputDir` | TField |  |  |
| 21 | `DFE.PARAM.ARCHIVE.DIR` | `DfeParameter_ArchiveDir` | TField |  |  |
| 22 | `DFE.PARAM.OFS.FUNCTION` | `DfeParameter_OfsFunction` | TField |  |  |
| 23 | `DFE.PARAM.IN.FILE.NAME` | `DfeParameter_InFileName` | TField |  |  |
| 24 | `DFE.PARAM.OUT.FILE.NAME` | `DfeParameter_OutFileName` | TField |  |  |
| 25 | `DFE.PARAM.HEADER.DETAILS` | `DfeParameter_HeaderDetails` |  |  |  |
| 26 | `DFE.PARAM.TRAILER.DETAILS` | `DfeParameter_TrailerDetails` |  |  |  |
| 27 | `DFE.PARAM.RESPONSE.MAP.ID` | `DfeParameter_ResponseMapId` | TField |  |  |
| 28 | `DFE.PARAM.RESPONSE.ROUTINE` | `DfeParameter_ResponseRoutine` | TField |  |  |
| 29 | `DFE.PARAM.DFE.CONNECTOR` | `DfeParameter_DfeConnector` | TField |  |  |
| 30 | `DFE.PARAM.WSDL.URL` | `DfeParameter_WsdlUrl` | TField |  |  |
| 31 | `DFE.PARAM.XML.TRANSFORM` | `DfeParameter_XmlTransform` | TField |  |  |
| 32 | `DFE.PARAM.COMPANY.CODE` | `DfeParameter_CompanyCode` | TField |  |  |
| 33 | `DFE.PARAM.JMS.CONN.FACTORY` | `DfeParameter_JmsConnFactory` | TField |  |  |
| 34 | `DFE.PARAM.REQUEST.QUEUE` | `DfeParameter_RequestQueue` | TField |  |  |
| 35 | `DFE.PARAM.REPLY.QUEUE` | `DfeParameter_ReplyQueue` | TField |  |  |
| 36 | `DFE.PARAM.MAX.EXTRACT.COUNT` | `DfeParameter_MaxExtractCount` | TField |  |  |
| 37 | `DFE.PARAM.SOAP.ACTION` | `DfeParameter_SoapAction` | TField |  |  |
| 38 | `DFE.PARAM.PART.FILE.NUMBER` | `DfeParameter_PartFileNumber` | TField |  |  |
| 39 | `DFE.PARAM.VALIDATE.REC` | `DfeParameter_ValidateRec` | TField |  |  |
| 40 | `DFE.PARAM.GROUP.ID` | `DfeParameter_GroupId` | TField |  |  |
| 41 | `DFE.PARAM.RESERVED.8` | `DfeParameter_Reserved8` | TField |  |  |
| 42 | `DFE.PARAM.RESERVED.7` | `DfeParameter_Reserved7` | TField |  |  |
| 43 | `DFE.PARAM.RESERVED.6` | `DfeParameter_Reserved6` | TField |  |  |
| 44 | `DFE.PARAM.RESERVED.5` | `DfeParameter_Reserved5` | TField |  |  |
| 45 | `DFE.PARAM.RESERVED.4` | `DfeParameter_Reserved4` | TField |  |  |
| 46 | `DFE.PARAM.RESERVED.3` | `DfeParameter_Reserved3` | TField |  |  |
| 47 | `DFE.PARAM.RESERVED.2` | `DfeParameter_Reserved2` | TField |  |  |
| 48 | `DFE.PARAM.LOCAL.REF` | `DfeParameter_LocalRef` |  |  |  |
| 49 | `DFE.PARAM.ALLOW.DUPLICATES` | `DfeParameter_AllowDuplicates` | TField |  |  |
| 50 | `DFE.PARAM.OVERRIDE` | `DfeParameter_Override` |  |  |  |
| 51 | `DFE.PARAM.RECORD.STATUS` | `DfeParameter_RecordStatus` | String |  |  |
| 52 | `DFE.PARAM.CURR.NO` | `DfeParameter_CurrNo` | String |  |  |
| 53 | `DFE.PARAM.INPUTTER` | `DfeParameter_Inputter` |  |  |  |
| 54 | `DFE.PARAM.DATE.TIME` | `DfeParameter_DateTime` |  |  |  |
| 55 | `DFE.PARAM.AUTHORISER` | `DfeParameter_Authoriser` | String |  |  |
| 56 | `DFE.PARAM.CO.CODE` | `DfeParameter_CoCode` | String |  |  |
| 57 | `DFE.PARAM.DEPT.CODE` | `DfeParameter_DeptCode` | String |  |  |
| 58 | `DFE.PARAM.AUDITOR.CODE` | `DfeParameter_AuditorCode` | String |  |  |
| 59 | `DFE.PARAM.AUDIT.DATE.TIME` | `DfeParameter_AuditDateTime` | String |  |  |
