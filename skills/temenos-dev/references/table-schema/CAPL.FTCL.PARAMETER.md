# CAPL.FTCL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.FTCL.PARAMETER` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FTCL.PARAM.CLR.FILE` | `CaplFtclParameter_ClrFile` |  |  |  |
| 2 | `FTCL.PARAM.CLR.BASE.DATE` | `CaplFtclParameter_ClrBaseDate` |  |  |  |
| 3 | `FTCL.PARAM.CLR.POST.DATE` | `CaplFtclParameter_ClrPostDate` |  |  |  |
| 4 | `FTCL.PARAM.CLR.BASE.DATE.EOM` | `CaplFtclParameter_ClrBaseDateEom` |  |  |  |
| 5 | `FTCL.PARAM.CLR.POST.DATE.EOM` | `CaplFtclParameter_ClrPostDateEom` |  |  |  |
| 6 | `FTCL.PARAM.CLR.OFS.SOURCE` | `CaplFtclParameter_ClrOfsSource` |  |  |  |
| 7 | `FTCL.PARAM.CLR.OFS.USER` | `CaplFtclParameter_ClrOfsUser` |  |  |  |
| 8 | `FTCL.PARAM.CLR.POST.COMP` | `CaplFtclParameter_ClrPostComp` |  |  |  |
| 9 | `FTCL.PARAM.RETAIN.DAYS` | `CaplFtclParameter_RetainDays` |  |  |  |
| 10 | `FTCL.PARAM.CLR.TXN.CODE` | `CaplFtclParameter_ClrTxnCode` |  |  |  |
| 11 | `FTCL.PARAM.VALID.PROD` | `CaplFtclParameter_ValidProd` |  |  |  |
| 12 | `FTCL.PARAM.FT.TXN.TYPE` | `CaplFtclParameter_FtTxnType` |  |  |  |
| 13 | `FTCL.PARAM.CLR.ASSC.VER` | `CaplFtclParameter_ClrAsscVer` |  |  |  |
| 14 | `FTCL.PARAM.OVE.GROUP` | `CaplFtclParameter_OveGroup` |  |  |  |
| 15 | `FTCL.PARAM.RCL.FT.MAPPING` | `CaplFtclParameter_RclFtMapping` |  |  |  |
| 16 | `FTCL.PARAM.DR.CR.CUS.ACCT` | `CaplFtclParameter_DrCrCusAcct` |  |  |  |
| 17 | `FTCL.PARAM.CLR.CONTRA.ACCT` | `CaplFtclParameter_ClrContraAcct` |  |  |  |
| 18 | `FTCL.PARAM.CLOSE.ACCT.FLAG` | `CaplFtclParameter_CloseAcctFlag` |  |  |  |
| 19 | `FTCL.PARAM.RED.STAGE` | `CaplFtclParameter_RedStage` |  |  |  |
| 20 | `FTCL.PARAM.CLR.CHQ.TYPE` | `CaplFtclParameter_ClrChqType` |  |  |  |
| 21 | `FTCL.PARAM.CLR.CHQ.NUM` | `CaplFtclParameter_ClrChqNum` |  |  |  |
| 22 | `FTCL.PARAM.RESERVED.13` | `CaplFtclParameter_Reserved13` |  |  |  |
| 23 | `FTCL.PARAM.RESERVED.14` | `CaplFtclParameter_Reserved14` |  |  |  |
| 24 | `FTCL.PARAM.RESERVED.15` | `CaplFtclParameter_Reserved15` |  |  |  |
| 25 | `FTCL.PARAM.CHQ.IMAGE.URL` | `CaplFtclParameter_ChqImageUrl` |  |  |  |
| 26 | `FTCL.PARAM.HIST.RETAIN.DAYS` | `CaplFtclParameter_HistRetainDays` | TField |  | This field used to indicate the number of days the CAPL.FTCL.EXCEPTIONHIS records needs to be retained. If the number of days is crossed then the records will be moved to CAPL.FTCL.EXCEPTION$ARC. |
| 27 | `FTCL.PARAM.CLR.ID.CO.CODE` | `CaplFtclParameter_ClrIdCoCode` |  |  |  |
| 28 | `FTCL.PARAM.FTCL.MAX.SEQ.NO` | `CaplFtclParameter_FtclMaxSeqNo` | TField |  |  |
| 29 | `FTCL.PARAM.SWITCH.STATUS` | `CaplFtclParameter_SwitchStatus` | TField |  |  |
| 30 | `FTCL.PARAM.FILE.SEQUENCE` | `CaplFtclParameter_FileSequence` | TField |  | This field is used to specify No of files received per clearing file like 2 file - XCC1, XCC2. |
| 31 | `FTCL.PARAM.STOCK.ACCT.NO` | `CaplFtclParameter_StockAcctNo` |  |  |  |
| 32 | `FTCL.PARAM.STOCK.FT.TXN.TYPE` | `CaplFtclParameter_StockFtTxnType` |  |  |  |
| 33 | `FTCL.PARAM.RESERVED.4` | `CaplFtclParameter_Reserved4` |  |  |  |
| 34 | `FTCL.PARAM.RESERVED.3` | `CaplFtclParameter_Reserved3` |  |  |  |
| 35 | `FTCL.PARAM.STOCK.CHQ.TYPE` | `CaplFtclParameter_StockChqType` |  |  |  |
| 36 | `FTCL.PARAM.REJ.FT.VER` | `CaplFtclParameter_RejFtVer` | TField |  | Field used to store the version to be used for the posting return items during the clearing process. Validation - record from VERSION table. Eg. FUNDS.TRANSFER,CAMB.CLEARING |
| 37 | `FTCL.PARAM.RESERVED.2` | `CaplFtclParameter_Reserved2` | TField |  |  |
| 38 | `FTCL.PARAM.RESERVED.1` | `CaplFtclParameter_Reserved1` | TField |  |  |
| 39 | `FTCL.PARAM.LOCAL.REF` | `CaplFtclParameter_LocalRef` |  |  |  |
| 40 | `FTCL.PARAM.OVERRIDE` | `CaplFtclParameter_Override` |  |  |  |
| 41 | `FTCL.PARAM.RECORD.STATUS` | `CaplFtclParameter_RecordStatus` | String |  |  |
| 42 | `FTCL.PARAM.CURR.NO` | `CaplFtclParameter_CurrNo` | String |  |  |
| 43 | `FTCL.PARAM.INPUTTER` | `CaplFtclParameter_Inputter` |  |  |  |
| 44 | `FTCL.PARAM.DATE.TIME` | `CaplFtclParameter_DateTime` |  |  |  |
| 45 | `FTCL.PARAM.AUTHORISER` | `CaplFtclParameter_Authoriser` | String |  |  |
| 46 | `FTCL.PARAM.CO.CODE` | `CaplFtclParameter_CoCode` | String |  |  |
| 47 | `FTCL.PARAM.DEPT.CODE` | `CaplFtclParameter_DeptCode` | String |  |  |
| 48 | `FTCL.PARAM.AUDITOR.CODE` | `CaplFtclParameter_AuditorCode` | String |  |  |
| 49 | `FTCL.PARAM.AUDIT.DATE.TIME` | `CaplFtclParameter_AuditDateTime` | String |  |  |
