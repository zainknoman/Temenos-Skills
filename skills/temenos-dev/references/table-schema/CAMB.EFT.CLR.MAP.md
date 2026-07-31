# CAMB.EFT.CLR.MAP — Table Schema

> Source: `INSERTS/I_F.CAMB.EFT.CLR.MAP` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.EFT.MAP.CURRENCY` | `CambEftClrMap_Currency` | TField |  | Field which stores the currency of the record id.Allowed inputs - 'CAD' or 'USD'Validations - only if currency matches with the incoming file, clearing process will happen. |
| 2 | `CAMB.EFT.MAP.CLR.TRANS.CODE.ST` | `CambEftClrMap_ClrTransCodeSt` |  |  |  |
| 3 | `CAMB.EFT.MAP.CLR.TRANS.CODE.ED` | `CambEftClrMap_ClrTransCodeEd` |  |  |  |
| 4 | `CAMB.EFT.MAP.FT.TXN.TYPE` | `CambEftClrMap_FtTxnType` |  |  |  |
| 5 | `CAMB.EFT.MAP.DR.CR.IND` | `CambEftClrMap_DrCrInd` |  |  |  |
| 6 | `CAMB.EFT.MAP.GL.ACCOUNT` | `CambEftClrMap_GlAccount` |  |  |  |
| 7 | `CAMB.EFT.MAP.REJ.GL.ACCOUNT` | `CambEftClrMap_RejGlAccount` |  |  |  |
| 8 | `CAMB.EFT.MAP.REG.PLAN.GROUP` | `CambEftClrMap_RegPlanGroup` |  |  |  |
| 9 | `CAMB.EFT.MAP.FT.VERSION.REG` | `CambEftClrMap_FtVersionReg` |  |  |  |
| 10 | `CAMB.EFT.MAP.FT.VERSION.NON.REG` | `CambEftClrMap_FtVersionNonReg` |  |  |  |
| 11 | `CAMB.EFT.MAP.RET.DR.CR` | `CambEftClrMap_RetDrCr` |  |  |  |
| 12 | `CAMB.EFT.MAP.RET.GL.ACCOUNT` | `CambEftClrMap_RetGlAccount` |  |  |  |
| 13 | `CAMB.EFT.MAP.RET.TXN.TYPE` | `CambEftClrMap_RetTxnType` |  |  |  |
| 14 | `CAMB.EFT.MAP.PURGE.DAYS` | `CambEftClrMap_PurgeDays` | TField |  | Field is used to store the number of days to be specified for purging the transaction File.Eg. 30 (days) |
| 15 | `CAMB.EFT.MAP.EFT.CHQ.TYPE` | `CambEftClrMap_EftChqType` |  |  |  |
| 16 | `CAMB.EFT.MAP.ACTION.REQ` | `CambEftClrMap_ActionReq` | TField |  | Field to indicate whether transactions can be posted immediately or it needs to be stored in CAMB.EFT.PENDING.CONCAT file for later posting.Allowed values : PENDING / PROCESSThis field will set to pending to debit type of transactions, so that credit type transactions are posted first and later debits are posted to prevent overdrafting issues.PROCESS: If this is set to PROCESS then system will immediately post the payments through the actual clearing service.PENDING: If this is set to PENDING then system will record the transactions in CAMB.EFT.PENDING.CONCAT file for later processing. Upon running the service CAMB.EFT.CLR.PENDING.PROCESS, system picks the data from the CAMB.EFT.PENDING.CONCAT file and process the debit transactions. |
| 17 | `CAMB.EFT.MAP.RESERVED.8` | `CambEftClrMap_Reserved8` | TField |  |  |
| 18 | `CAMB.EFT.MAP.RESERVED.7` | `CambEftClrMap_Reserved7` | TField |  |  |
| 19 | `CAMB.EFT.MAP.RESERVED.6` | `CambEftClrMap_Reserved6` | TField |  |  |
| 20 | `CAMB.EFT.MAP.RESERVED.5` | `CambEftClrMap_Reserved5` | TField |  |  |
| 21 | `CAMB.EFT.MAP.RESERVED.4` | `CambEftClrMap_Reserved4` | TField |  |  |
| 22 | `CAMB.EFT.MAP.RESERVED.3` | `CambEftClrMap_Reserved3` | TField |  |  |
| 23 | `CAMB.EFT.MAP.RESERVED.2` | `CambEftClrMap_Reserved2` | TField |  |  |
| 24 | `CAMB.EFT.MAP.RESERVED.1` | `CambEftClrMap_Reserved1` | TField |  |  |
| 25 | `CAMB.EFT.MAP.LOCAL.REF` | `CambEftClrMap_LocalRef` |  |  |  |
| 26 | `CAMB.EFT.MAP.OVERRIDE` | `CambEftClrMap_Override` |  |  |  |
| 27 | `CAMB.EFT.MAP.RECORD.STATUS` | `CambEftClrMap_RecordStatus` | String |  |  |
| 28 | `CAMB.EFT.MAP.CURR.NO` | `CambEftClrMap_CurrNo` | String |  |  |
| 29 | `CAMB.EFT.MAP.INPUTTER` | `CambEftClrMap_Inputter` |  |  |  |
| 30 | `CAMB.EFT.MAP.DATE.TIME` | `CambEftClrMap_DateTime` |  |  |  |
| 31 | `CAMB.EFT.MAP.AUTHORISER` | `CambEftClrMap_Authoriser` | String |  |  |
| 32 | `CAMB.EFT.MAP.CO.CODE` | `CambEftClrMap_CoCode` | String |  |  |
| 33 | `CAMB.EFT.MAP.DEPT.CODE` | `CambEftClrMap_DeptCode` | String |  |  |
| 34 | `CAMB.EFT.MAP.AUDITOR.CODE` | `CambEftClrMap_AuditorCode` | String |  |  |
| 35 | `CAMB.EFT.MAP.AUDIT.DATE.TIME` | `CambEftClrMap_AuditDateTime` | String |  |  |
