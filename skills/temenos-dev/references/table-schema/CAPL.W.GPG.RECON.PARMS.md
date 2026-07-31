# CAPL.W.GPG.RECON.PARMS — Table Schema

> Source: `INSERTS/I_F.CAPL.W.GPG.RECON.PARMS` in `CAGPGR_Reconciliation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.GRP.SHORT.DESCRP` | `CaplWGpgReconParms_ShortDescrp` |  |  |  |
| 2 | `CAPL.GRP.DESCRIPTION` | `CaplWGpgReconParms_Description` |  |  |  |
| 3 | `CAPL.GRP.RECON.STR.DATE` | `CaplWGpgReconParms_ReconStrDate` | TField |  | Purpose of the field to define the starting DATE range for the transactions to be extracted from T24.Validations: Date format field.Eg. 01DEC2015extract will selected with the trasactions with a date range from the date defined in RECON.STR.DATE till RECON.END.DATENote: This should be Date of the transaction booked in T24 and not VALUE date. |
| 4 | `CAPL.GRP.RECON.STR.TIME` | `CaplWGpgReconParms_ReconStrTime` | TField |  | Purpose of the field to define the starting Time range for the transaction to be extracted from T24.Purpose of the field to define the TIME range for the transactions to be extracted from T24.Validations: format to be 12:01(Hours:Minutes)Eg. 12:01Note: This should be Time of the transaction booked in T24 and not based on the VALUE date. |
| 5 | `CAPL.GRP.RECON.END.DATE` | `CaplWGpgReconParms_ReconEndDate` | TField |  | Purpose of the field to define the End DATE range for the transactions to be extracted from T24.Validations: Frequency type field and gets recycled after reconciliation process runs.Note: This should be Date of the transaction booked in T24 and not VALUE dateThis date should not be lower than today's date.Eg. 31DEC2015extract will selected with the trasactions with a date range from the date defined in RECON.STR.DATE till RECON.END.DATE |
| 6 | `CAPL.GRP.RECON.END.TIME` | `CaplWGpgReconParms_ReconEndTime` | TField |  | Purpose of the field to define the end Time range for the transaction to be extracted from T24.Purpose of the field to define the TIME range for the transactions to be extracted from T24.Validations: format to be 12:59(Hours:Minutes)Eg. 12:59Note: This should be Time of the transaction booked in T24 and not based on the VALUE date. |
| 7 | `CAPL.GRP.RECON.ACCT.ID` | `CaplWGpgReconParms_ReconAcctId` |  |  |  |
| 8 | `CAPL.GRP.RECON.CATEGORY` | `CaplWGpgReconParms_ReconCategory` |  |  |  |
| 9 | `CAPL.GRP.RECON.TXN.CODE` | `CaplWGpgReconParms_ReconTxnCode` |  |  |  |
| 10 | `CAPL.GRP.RECON.FT.TXN` | `CaplWGpgReconParms_ReconFtTxn` |  |  |  |
| 11 | `CAPL.GRP.RESERVED.9` | `CaplWGpgReconParms_Reserved9` |  |  |  |
| 12 | `CAPL.GRP.RESERVED.10` | `CaplWGpgReconParms_Reserved10` |  |  |  |
| 13 | `CAPL.GRP.RESERVED.11` | `CaplWGpgReconParms_Reserved11` |  |  |  |
| 14 | `CAPL.GRP.RESERVED.12` | `CaplWGpgReconParms_Reserved12` |  |  |  |
| 15 | `CAPL.GRP.RESERVED.13` | `CaplWGpgReconParms_Reserved13` |  |  |  |
| 16 | `CAPL.GRP.FTP.ID` | `CaplWGpgReconParms_FtpId` | TField |  | Not in use now. |
| 17 | `CAPL.GRP.T24.OUT.DIR` | `CaplWGpgReconParms_T24OutDir` | TField |  | Purpose of the field to define a valid path in which the reconciliation extract to be placed.Eg. .\bnk.interface\GPG.RECON.OUT - once the reconciliation extract is completed, the file will be placed in this path. |
| 18 | `CAPL.GRP.LOCAL.REF` | `CaplWGpgReconParms_LocalRef` |  |  |  |
| 19 | `CAPL.GRP.GPG.RECON.SERVICE` | `CaplWGpgReconParms_GpgReconService` | TField |  | Field used to defined the service to be triggered automatically for reconciliation extract, after COB process is completed.Valid records of TSA.SERVICE.System automatically start the service to generate the extract for online file generation.This field should not be configured, if reconciliation extract to be triggered as part of COB process.Eg.FI using Threshold switch provider:XXX/ CAMB.B.GPG.RECON.ATM - service for generation of file for ATM transactions.XXX/ CAMB.B.GPG.RECON.POS - service for generation of file for POS transactions.XXX/ CAMB.B.GPG.RECON.EBILL - service for generation of file for EBILL transactions.XXX/ CAMB.B.GPG.RECON.INTERAC - service for generation of file for INTERAC transactions.FI using Everlink switch provider:XXX/ CAMB.B.GPG.RECON.EVR.ATM - service for generation of file for ATM transactions.XXX/ CAMB.B.GPG.RECON.EVR.POS - service for generation of file for POS transactions.XXX/ CAMB.B.GPG.RECON.EBILL - service for generation of file for EBILL transactions.XXX/ CAMB.B.GPG.RECON.INTERAC - service for generation of file for INTERAC transactions..if this field is not defined, reconciliation extract will be process as part of COB using the below BATCH record attached to COB process.XXX/ CAMB.B.GPG.RECON is used for Threshold switch provider.XXX/ CAMB.B.GPG.RECON.EVR is used for Everlink switch provider. |
| 20 | `CAPL.GRP.AMOUNT.PRIORITY` | `CaplWGpgReconParms_AmountPriority` |  |  |  |
| 21 | `CAPL.GRP.RESERVED.8` | `CaplWGpgReconParms_Reserved8` | TField |  |  |
| 22 | `CAPL.GRP.RESERVED.7` | `CaplWGpgReconParms_Reserved7` | TField |  |  |
| 23 | `CAPL.GRP.RESERVED.6` | `CaplWGpgReconParms_Reserved6` | TField |  |  |
| 24 | `CAPL.GRP.RESERVED.5` | `CaplWGpgReconParms_Reserved5` | TField |  |  |
| 25 | `CAPL.GRP.RESERVED.4` | `CaplWGpgReconParms_Reserved4` | TField |  |  |
| 26 | `CAPL.GRP.RESERVED.3` | `CaplWGpgReconParms_Reserved3` | TField |  |  |
| 27 | `CAPL.GRP.RESERVED.2` | `CaplWGpgReconParms_Reserved2` | TField |  |  |
| 28 | `CAPL.GRP.RESERVED.1` | `CaplWGpgReconParms_Reserved1` | TField |  |  |
| 29 | `CAPL.GRP.OVERRIDE` | `CaplWGpgReconParms_Override` |  |  |  |
| 30 | `CAPL.GRP.RECORD.STATUS` | `CaplWGpgReconParms_RecordStatus` | String |  |  |
| 31 | `CAPL.GRP.CURR.NO` | `CaplWGpgReconParms_CurrNo` | String |  |  |
| 32 | `CAPL.GRP.INPUTTER` | `CaplWGpgReconParms_Inputter` |  |  |  |
| 33 | `CAPL.GRP.DATE.TIME` | `CaplWGpgReconParms_DateTime` |  |  |  |
| 34 | `CAPL.GRP.AUTHORISER` | `CaplWGpgReconParms_Authoriser` | String |  |  |
| 35 | `CAPL.GRP.CO.CODE` | `CaplWGpgReconParms_CoCode` | String |  |  |
| 36 | `CAPL.GRP.DEPT.CODE` | `CaplWGpgReconParms_DeptCode` | String |  |  |
| 37 | `CAPL.GRP.AUDITOR.CODE` | `CaplWGpgReconParms_AuditorCode` | String |  |  |
| 38 | `CAPL.GRP.AUDIT.DATE.TIME` | `CaplWGpgReconParms_AuditDateTime` | String |  |  |
