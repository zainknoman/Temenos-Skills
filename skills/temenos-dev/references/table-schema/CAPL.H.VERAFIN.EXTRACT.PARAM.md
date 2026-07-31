# CAPL.H.VERAFIN.EXTRACT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.VERAFIN.EXTRACT.PARAM` in `CAVNFR_Verafin.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.VEP.GIT.INTERFACE.OUT` | `CaplHVerafinExtractParam_GitInterfaceOut` |  |  |  |
| 2 | `CAPL.VEP.COB.ONLINE` | `CaplHVerafinExtractParam_CobOnline` |  |  |  |
| 3 | `CAPL.VEP.INCREMENTAL.EXTRACT` | `CaplHVerafinExtractParam_IncrementalExtract` |  |  |  |
| 4 | `CAPL.VEP.INCREMENT.BY` | `CaplHVerafinExtractParam_IncrementBy` |  |  |  |
| 5 | `CAPL.VEP.LAST.PROCESS.DATE.TIME` | `CaplHVerafinExtractParam_LastProcessDateTime` |  |  |  |
| 6 | `CAPL.VEP.FILE.NAME` | `CaplHVerafinExtractParam_FileName` |  |  |  |
| 7 | `CAPL.VEP.ERROR.MSG` | `CaplHVerafinExtractParam_ErrorMsg` |  |  |  |
| 8 | `CAPL.VEP.CATEG.TXN.FLAG` | `CaplHVerafinExtractParam_CategTxnFlag` | TField |  | Not used |
| 9 | `CAPL.VEP.CATEG.CODE` | `CaplHVerafinExtractParam_CategCode` |  |  |  |
| 10 | `CAPL.VEP.TXN.CODE` | `CaplHVerafinExtractParam_TxnCode` |  |  |  |
| 11 | `CAPL.VEP.SOURCE.DIR` | `CaplHVerafinExtractParam_SourceDir` | TField |  | Field is used to store the valid directory for placing the Verafin files for producing the extracts.Eg. ./bnk.interface/VERAFIN.OUT |
| 12 | `CAPL.VEP.TEMP.DIR` | `CaplHVerafinExtractParam_TempDir` | TField |  | Field is used to store the valid directory path incase to place the back up the extracted files.Eg. ./bnk.interface/VERAFIN.BACKUP |
| 13 | `CAPL.VEP.ARC.PERIOD` | `CaplHVerafinExtractParam_ArcPeriod` | TField |  | Not used |
| 14 | `CAPL.VEP.LOCAL.REF` | `CaplHVerafinExtractParam_LocalRef` |  |  |  |
| 15 | `CAPL.VEP.TFS.TXN.CODE` | `CaplHVerafinExtractParam_TfsTxnCode` |  |  |  |
| 16 | `CAPL.VEP.CASH.IN.TXNS` | `CaplHVerafinExtractParam_CashInTxns` |  |  |  |
| 17 | `CAPL.VEP.CASH.OUT.TXNS` | `CaplHVerafinExtractParam_CashOutTxns` |  |  |  |
| 18 | `CAPL.VEP.TFS.CHQ.TXNS` | `CaplHVerafinExtractParam_TfsChqTxns` |  |  |  |
| 19 | `CAPL.VEP.OWN.ROLES` | `CaplHVerafinExtractParam_OwnRoles` |  |  |  |
| 20 | `CAPL.VEP.CARD.STATUS` | `CaplHVerafinExtractParam_CardStatus` |  |  |  |
| 21 | `CAPL.VEP.EXC.ARR.STATUS` | `CaplHVerafinExtractParam_ExcArrStatus` |  |  |  |
| 22 | `CAPL.VEP.CUST.IND.FLAG` | `CaplHVerafinExtractParam_CustIndFlag` | TField |  | Based on this flag, the Industry/Naics code and its respective description will is displayed in the customer extract This field has two values - Industry and Naics code. If Industry is chosen then Industry and Industry description will be displayed in the customer extract. If Naics code or 'None' is chosen then based Naics code and Naics description will be displayed |
| 23 | `CAPL.VEP.ALT.CUST.MAP.EXT` | `CaplHVerafinExtractParam_AltCustMapExt` | TField |  |  |
| 24 | `CAPL.VEP.TFS.INDIV` | `CaplHVerafinExtractParam_TfsIndiv` | TField |  |  |
| 25 | `CAPL.VEP.RESERVED.5` | `CaplHVerafinExtractParam_Reserved5` | TField |  |  |
| 26 | `CAPL.VEP.RESERVED.4` | `CaplHVerafinExtractParam_Reserved4` | TField |  |  |
| 27 | `CAPL.VEP.RESERVED.3` | `CaplHVerafinExtractParam_Reserved3` | TField |  |  |
| 28 | `CAPL.VEP.RESERVED.2` | `CaplHVerafinExtractParam_Reserved2` | TField |  |  |
| 29 | `CAPL.VEP.RESERVED.1` | `CaplHVerafinExtractParam_Reserved1` | TField |  |  |
| 30 | `CAPL.VEP.OVERRIDE` | `CaplHVerafinExtractParam_Override` |  |  |  |
| 31 | `CAPL.VEP.RECORD.STATUS` | `CaplHVerafinExtractParam_RecordStatus` | String |  |  |
| 32 | `CAPL.VEP.CURR.NO` | `CaplHVerafinExtractParam_CurrNo` | String |  |  |
| 33 | `CAPL.VEP.INPUTTER` | `CaplHVerafinExtractParam_Inputter` |  |  |  |
| 34 | `CAPL.VEP.DATE.TIME` | `CaplHVerafinExtractParam_DateTime` |  |  |  |
| 35 | `CAPL.VEP.AUTHORISER` | `CaplHVerafinExtractParam_Authoriser` | String |  |  |
| 36 | `CAPL.VEP.CO.CODE` | `CaplHVerafinExtractParam_CoCode` | String |  |  |
| 37 | `CAPL.VEP.DEPT.CODE` | `CaplHVerafinExtractParam_DeptCode` | String |  |  |
| 38 | `CAPL.VEP.AUDITOR.CODE` | `CaplHVerafinExtractParam_AuditorCode` | String |  |  |
| 39 | `CAPL.VEP.AUDIT.DATE.TIME` | `CaplHVerafinExtractParam_AuditDateTime` | String |  |  |
| 40 | `CAPL.VEP.SEL.CRITERIA` | `CaplHVerafinExtractParam_SelCriteria` |  |  |  |
