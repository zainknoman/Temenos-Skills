# CAPL.FTRI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.FTRI.PARAMETER` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FTRI.PARAM.RET.POST.COMP` | `CaplFtriParameter_RetPostComp` | TField |  | Field is used to indicate the transaction entries should be posted under this company.Validation - record from COMPANY table. |
| 2 | `FTRI.PARAM.RET.FILE` | `CaplFtriParameter_RetFile` |  |  |  |
| 3 | `FTRI.PARAM.REJ.ENT.DATE` | `CaplFtriParameter_RejEntDate` |  |  |  |
| 4 | `FTRI.PARAM.TXN.CODE` | `CaplFtriParameter_TxnCode` |  |  |  |
| 5 | `FTRI.PARAM.FT.TXN.TYPE` | `CaplFtriParameter_FtTxnType` |  |  |  |
| 6 | `FTRI.PARAM.RET.SUSP.ACCT` | `CaplFtriParameter_RetSuspAcct` |  |  |  |
| 7 | `FTRI.PARAM.ACP.VERSION` | `CaplFtriParameter_AcpVersion` |  |  |  |
| 8 | `FTRI.PARAM.RCL.ACP.FT.ENT` | `CaplFtriParameter_RclAcpFtEnt` |  |  |  |
| 9 | `FTRI.PARAM.ACP.POST.CO` | `CaplFtriParameter_AcpPostCo` |  |  |  |
| 10 | `FTRI.PARAM.CHB.VERSION` | `CaplFtriParameter_ChbVersion` |  |  |  |
| 11 | `FTRI.PARAM.RCL.CHB.FT.ENT` | `CaplFtriParameter_RclChbFtEnt` |  |  |  |
| 12 | `FTRI.PARAM.CHB.POST.CO` | `CaplFtriParameter_ChbPostCo` |  |  |  |
| 13 | `FTRI.PARAM.REJ.VERSION.1` | `CaplFtriParameter_RejVersion1` |  |  |  |
| 14 | `FTRI.PARAM.RCL.REJ.FT.ENT.1` | `CaplFtriParameter_RclRejFtEnt1` |  |  |  |
| 15 | `FTRI.PARAM.REJ.POST.CO.1` | `CaplFtriParameter_RejPostCo1` |  |  |  |
| 16 | `FTRI.PARAM.REJ.VERSION.2` | `CaplFtriParameter_RejVersion2` |  |  |  |
| 17 | `FTRI.PARAM.RCL.REJ.FT.ENT.2` | `CaplFtriParameter_RclRejFtEnt2` |  |  |  |
| 18 | `FTRI.PARAM.REJ.POST.CO.2` | `CaplFtriParameter_RejPostCo2` |  |  |  |
| 19 | `FTRI.PARAM.RET.OFS.SOURCE` | `CaplFtriParameter_RetOfsSource` | TField |  | Field to store the OFS.SOURCE record to post the reversal transactions.Validation - record of OFS.SOURCE |
| 20 | `FTRI.PARAM.RET.OFS.USER` | `CaplFtriParameter_RetOfsUser` | TField |  |  |
| 21 | `FTRI.PARAM.CHQ.ORIG.ID` | `CaplFtriParameter_ChqOrigId` | TField |  | Field to store the cheque originator ID.Part of Cheque return specification, there field call 'fileOriginatorlong' in header session ( i.e 3rd position). 'fileOriginatorlong' value need to be parameterized here |
| 22 | `FTRI.PARAM.CHQ.TRANS.CODE` | `CaplFtriParameter_ChqTransCode` | TField |  | Field to store the Transit Number short reference.Part of Cheque return specification, there field call 'transitNumberShort' in header session ( i.e 4rd position). 'transitNumberShort' value need to be parameterized here. |
| 23 | `FTRI.PARAM.PAP.ORIG.ID` | `CaplFtriParameter_PapOrigId` | TField |  | Field to store the Originator ID to be mapped for the clearing extract.Originator of PAP return extract need to be configured here ( Required for both Central1 Compressed format and CPA Standard 005 Format specification). |
| 24 | `FTRI.PARAM.PAP.TRANS.CODE` | `CaplFtriParameter_PapTransCode` | TField |  | field is used to store the Transit Number of PAP return extract need to be configured (Required for Central1 Compressed format specification). |
| 25 | `FTRI.PARAM.FTRI.MAX.SEQ.NO` | `CaplFtriParameter_FtriMaxSeqNo` | TField |  | Field is used to parameterise the maximum file sequence number.Allowed up to 4 digits. |
| 26 | `FTRI.PARAM.RET.FILE.FORMAT` | `CaplFtriParameter_FileFormat` |  |  |  |
| 27 | `FTRI.PARAM.RESERVED.4` | `CaplFtriParameter_Reserved4` | TField |  |  |
| 28 | `FTRI.PARAM.RESERVED.3` | `CaplFtriParameter_Reserved3` | TField |  |  |
| 29 | `FTRI.PARAM.RESERVED.2` | `CaplFtriParameter_Reserved2` | TField |  |  |
| 30 | `FTRI.PARAM.RESERVED.1` | `CaplFtriParameter_Reserved1` | TField |  |  |
| 31 | `FTRI.PARAM.LOCAL.REF` | `CaplFtriParameter_LocalRef` |  |  |  |
| 32 | `FTRI.PARAM.OVERRIDE` | `CaplFtriParameter_Override` |  |  |  |
| 33 | `FTRI.PARAM.RECORD.STATUS` | `CaplFtriParameter_RecordStatus` | String |  |  |
| 34 | `FTRI.PARAM.CURR.NO` | `CaplFtriParameter_CurrNo` | String |  |  |
| 35 | `FTRI.PARAM.INPUTTER` | `CaplFtriParameter_Inputter` |  |  |  |
| 36 | `FTRI.PARAM.DATE.TIME` | `CaplFtriParameter_DateTime` |  |  |  |
| 37 | `FTRI.PARAM.AUTHORISER` | `CaplFtriParameter_Authoriser` | String |  |  |
| 38 | `FTRI.PARAM.CO.CODE` | `CaplFtriParameter_CoCode` | String |  |  |
| 39 | `FTRI.PARAM.DEPT.CODE` | `CaplFtriParameter_DeptCode` | String |  |  |
| 40 | `FTRI.PARAM.AUDITOR.CODE` | `CaplFtriParameter_AuditorCode` | String |  |  |
| 41 | `FTRI.PARAM.AUDIT.DATE.TIME` | `CaplFtriParameter_AuditDateTime` | String |  |  |
