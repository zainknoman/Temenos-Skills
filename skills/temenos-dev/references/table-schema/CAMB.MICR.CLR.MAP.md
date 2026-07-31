# CAMB.MICR.CLR.MAP — Table Schema

> Source: `INSERTS/I_F.CAMB.MICR.CLR.MAP` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.MAP.TRANS.CODE` | `CambMicrClrMap_TransCode` |  |  |  |
| 2 | `CAMB.MAP.CURRENCY` | `CambMicrClrMap_Currency` |  |  |  |
| 3 | `CAMB.MAP.DR.CR.IND` | `CambMicrClrMap_DrCrInd` |  |  |  |
| 4 | `CAMB.MAP.FT.TXN.TYPE` | `CambMicrClrMap_FtTxnType` |  |  |  |
| 5 | `CAMB.MAP.RESERVED.10` | `CambMicrClrMap_Reserved10` |  |  |  |
| 6 | `CAMB.MAP.RESERVED.9` | `CambMicrClrMap_Reserved9` |  |  |  |
| 7 | `CAMB.MAP.RESERVED.8` | `CambMicrClrMap_Reserved8` |  |  |  |
| 8 | `CAMB.MAP.DEF.BRANCH` | `CambMicrClrMap_DefBranch` |  |  |  |
| 9 | `CAMB.MAP.GL.CURRENCY` | `CambMicrClrMap_GlCurrency` |  |  |  |
| 10 | `CAMB.MAP.GL.ACCOUNT` | `CambMicrClrMap_GlAccount` |  |  |  |
| 11 | `CAMB.MAP.REJ.GL.ACCOUNT` | `CambMicrClrMap_RejGlAccount` |  |  |  |
| 12 | `CAMB.MAP.RESERVED.7` | `CambMicrClrMap_Reserved7` |  |  |  |
| 13 | `CAMB.MAP.RESERVED.6` | `CambMicrClrMap_Reserved6` |  |  |  |
| 14 | `CAMB.MAP.DEF.CHQ.TYPE` | `CambMicrClrMap_DefChqType` |  |  |  |
| 15 | `CAMB.MAP.REDIR.GL.ACCOUNT` | `CambMicrClrMap_RedirGlAccount` |  |  |  |
| 16 | `CAMB.MAP.CHQ.TYPE` | `CambMicrClrMap_ChqType` |  |  |  |
| 17 | `CAMB.MAP.UPDATE.ISSUE.TYPE` | `CambMicrClrMap_UpdateIssueType` |  |  |  |
| 18 | `CAMB.MAP.CHQ.FT.TXN.TYPE` | `CambMicrClrMap_ChqFtTxnType` |  |  |  |
| 19 | `CAMB.MAP.RESERVED.4` | `CambMicrClrMap_Reserved4` |  |  |  |
| 20 | `CAMB.MAP.RESERVED.3` | `CambMicrClrMap_Reserved3` |  |  |  |
| 21 | `CAMB.MAP.RESERVED.2` | `CambMicrClrMap_Reserved2` |  |  |  |
| 22 | `CAMB.MAP.RESERVED.1` | `CambMicrClrMap_Reserved1` |  |  |  |
| 23 | `CAMB.MAP.LOCAL.REF` | `CambMicrClrMap_LocalRef` |  |  |  |
| 24 | `CAMB.MAP.OVERRIDE` | `CambMicrClrMap_Override` |  |  |  |
| 25 | `CAMB.MAP.RECORD.STATUS` | `CambMicrClrMap_RecordStatus` |  |  |  |
| 26 | `CAMB.MAP.CURR.NO` | `CambMicrClrMap_CurrNo` |  |  |  |
| 27 | `CAMB.MAP.INPUTTER` | `CambMicrClrMap_Inputter` |  |  |  |
| 28 | `CAMB.MAP.DATE.TIME` | `CambMicrClrMap_DateTime` |  |  |  |
| 29 | `CAMB.MAP.AUTHORISER` | `CambMicrClrMap_Authoriser` |  |  |  |
| 30 | `CAMB.MAP.CO.CODE` | `CambMicrClrMap_CoCode` |  |  |  |
| 31 | `CAMB.MAP.DEPT.CODE` | `CambMicrClrMap_DeptCode` |  |  |  |
| 32 | `CAMB.MAP.AUDITOR.CODE` | `CambMicrClrMap_AuditorCode` |  |  |  |
| 33 | `CAMB.MAP.AUDIT.DATE.TIME` | `CambMicrClrMap_AuditDateTime` |  |  |  |
