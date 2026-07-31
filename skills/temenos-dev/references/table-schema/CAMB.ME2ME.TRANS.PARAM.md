# CAMB.ME2ME.TRANS.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.ME2ME.TRANS.PARAM` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ME2ME.PAR.HOLD.DAYS` | `CambMe2meTransParam_HoldDays` |  |  |  |
| 2 | `ME2ME.PAR.DR.CR.IND` | `CambMe2meTransParam_DrCrInd` |  |  |  |
| 3 | `ME2ME.PAR.TXN.TYPE` | `CambMe2meTransParam_TxnType` |  |  |  |
| 4 | `ME2ME.PAR.CPA.TXN.CODE` | `CambMe2meTransParam_CpaTxnCode` |  |  |  |
| 5 | `ME2ME.PAR.INT.ACCT` | `CambMe2meTransParam_IntAcct` |  |  |  |
| 6 | `ME2ME.PAR.LOG.DIR` | `CambMe2meTransParam_LogDir` |  |  |  |
| 7 | `ME2ME.PAR.LOG.FILENAME` | `CambMe2meTransParam_LogFilename` |  |  |  |
| 8 | `ME2ME.PAR.FT.TXN.TYPE` | `CambMe2meTransParam_FtTxnType` |  |  |  |
| 9 | `ME2ME.PAR.RESERVED.9` | `CambMe2meTransParam_Reserved9` |  |  |  |
| 10 | `ME2ME.PAR.RESERVED.8` | `CambMe2meTransParam_Reserved8` |  |  |  |
| 11 | `ME2ME.PAR.RESERVED.7` | `CambMe2meTransParam_Reserved7` |  |  |  |
| 12 | `ME2ME.PAR.RESERVED.6` | `CambMe2meTransParam_Reserved6` |  |  |  |
| 13 | `ME2ME.PAR.RESERVED.5` | `CambMe2meTransParam_Reserved5` |  |  |  |
| 14 | `ME2ME.PAR.RESERVED.4` | `CambMe2meTransParam_Reserved4` |  |  |  |
| 15 | `ME2ME.PAR.RESERVED.3` | `CambMe2meTransParam_Reserved3` |  |  |  |
| 16 | `ME2ME.PAR.RESERVED.2` | `CambMe2meTransParam_Reserved2` |  |  |  |
| 17 | `ME2ME.PAR.RESERVED.1` | `CambMe2meTransParam_Reserved1` |  |  |  |
| 18 | `ME2ME.PAR.LOCAL.REF` | `CambMe2meTransParam_LocalRef` |  |  |  |
| 19 | `ME2ME.PAR.OVERRIDE` | `CambMe2meTransParam_Override` |  |  |  |
| 20 | `ME2ME.PAR.RECORD.STATUS` | `CambMe2meTransParam_RecordStatus` |  |  |  |
| 21 | `ME2ME.PAR.CURR.NO` | `CambMe2meTransParam_CurrNo` |  |  |  |
| 22 | `ME2ME.PAR.INPUTTER` | `CambMe2meTransParam_Inputter` |  |  |  |
| 23 | `ME2ME.PAR.DATE.TIME` | `CambMe2meTransParam_DateTime` |  |  |  |
| 24 | `ME2ME.PAR.AUTHORISER` | `CambMe2meTransParam_Authoriser` |  |  |  |
| 25 | `ME2ME.PAR.CO.CODE` | `CambMe2meTransParam_CoCode` |  |  |  |
| 26 | `ME2ME.PAR.DEPT.CODE` | `CambMe2meTransParam_DeptCode` |  |  |  |
| 27 | `ME2ME.PAR.AUDITOR.CODE` | `CambMe2meTransParam_AuditorCode` |  |  |  |
| 28 | `ME2ME.PAR.AUDIT.DATE.TIME` | `CambMe2meTransParam_AuditDateTime` |  |  |  |
