# MD.CR.DR.TXN.PARAM — Table Schema

> Source: `INSERTS/I_F.MD.CR.DR.TXN.PARAM` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.PARAM.MD.TXN.TYPE` | `MdCrDrTxnParam_MdTxnType` |  |  |  |
| 2 | `MD.PARAM.MD.TXN.CODE.LEN` | `MdCrDrTxnParam_MdTxnCodeLen` |  |  |  |
| 3 | `MD.PARAM.RESERVED.10` | `MdCrDrTxnParam_Reserved10` |  |  |  |
| 4 | `MD.PARAM.RESERVED.9` | `MdCrDrTxnParam_Reserved9` |  |  |  |
| 5 | `MD.PARAM.RESERVED.8` | `MdCrDrTxnParam_Reserved8` |  |  |  |
| 6 | `MD.PARAM.RESERVED.7` | `MdCrDrTxnParam_Reserved7` |  |  |  |
| 7 | `MD.PARAM.RESERVED.6` | `MdCrDrTxnParam_Reserved6` |  |  |  |
| 8 | `MD.PARAM.DR.CR` | `MdCrDrTxnParam_DrCr` |  |  |  |
| 9 | `MD.PARAM.MD.TXN.CODE` | `MdCrDrTxnParam_MdTxnCode` |  |  |  |
| 10 | `MD.PARAM.T24.TXN.TYPE` | `MdCrDrTxnParam_T24TxnType` |  |  |  |
| 11 | `MD.PARAM.REV.COMM.TYPE` | `MdCrDrTxnParam_RevCommType` |  |  |  |
| 12 | `MD.PARAM.T24.REV.TXN.TYPE` | `MdCrDrTxnParam_T24RevTxnType` |  |  |  |
| 13 | `MD.PARAM.RESERVED.4` | `MdCrDrTxnParam_Reserved4` |  |  |  |
| 14 | `MD.PARAM.RESERVED.3` | `MdCrDrTxnParam_Reserved3` |  |  |  |
| 15 | `MD.PARAM.RESERVED.2` | `MdCrDrTxnParam_Reserved2` |  |  |  |
| 16 | `MD.PARAM.RESERVED.1` | `MdCrDrTxnParam_Reserved1` |  |  |  |
| 17 | `MD.PARAM.SUSP.ACCT` | `MdCrDrTxnParam_SuspAcct` |  |  |  |
| 18 | `MD.PARAM.RECORD.STATUS` | `MdCrDrTxnParam_RecordStatus` |  |  |  |
| 19 | `MD.PARAM.CURR.NO` | `MdCrDrTxnParam_CurrNo` |  |  |  |
| 20 | `MD.PARAM.INPUTTER` | `MdCrDrTxnParam_Inputter` |  |  |  |
| 21 | `MD.PARAM.DATE.TIME` | `MdCrDrTxnParam_DateTime` |  |  |  |
| 22 | `MD.PARAM.AUTHORISER` | `MdCrDrTxnParam_Authoriser` |  |  |  |
| 23 | `MD.PARAM.CO.CODE` | `MdCrDrTxnParam_CoCode` |  |  |  |
| 24 | `MD.PARAM.DEPT.CODE` | `MdCrDrTxnParam_DeptCode` |  |  |  |
| 25 | `MD.PARAM.AUDITOR.CODE` | `MdCrDrTxnParam_AuditorCode` |  |  |  |
| 26 | `MD.PARAM.AUDIT.DATE.TIME` | `MdCrDrTxnParam_AuditDateTime` |  |  |  |
