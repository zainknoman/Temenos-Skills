# CNTELL.DAILY.MATCHING.PARAM — Table Schema

> Source: `INSERTS/I_F.CNTELL.DAILY.MATCHING.PARAM` in `CNTELL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLY.PARAM.ITEM` | `CntellDailyMatchingParam_Item` |  |  |  |
| 2 | `DLY.PARAM.DESCRIPTION` | `CntellDailyMatchingParam_Description` |  |  |  |
| 3 | `DLY.PARAM.APPLICATION` | `CntellDailyMatchingParam_Application` |  |  |  |
| 4 | `DLY.PARAM.TXN.CODE.START.RANGE` | `CntellDailyMatchingParam_TxnCodeStartRange` |  |  |  |
| 5 | `DLY.PARAM.TXN.CODE.END.RANGE` | `CntellDailyMatchingParam_TxnCodeEndRange` |  |  |  |
| 6 | `DLY.PARAM.CRF.TYPE` | `CntellDailyMatchingParam_CrfType` |  |  |  |
| 7 | `DLY.PARAM.EXCLUDED.APPLICATION` | `CntellDailyMatchingParam_ExcludedApplication` |  |  |  |
| 8 | `DLY.PARAM.EXCLUDED.TXN.CODE` | `CntellDailyMatchingParam_ExcludedTxnCode` |  |  |  |
| 9 | `DLY.PARAM.EXCLUDED.PL.CATEGORY` | `CntellDailyMatchingParam_ExcludedPlCategory` |  |  |  |
| 10 | `DLY.PARAM.EXCLUDED.CRF.TYPE` | `CntellDailyMatchingParam_ExcludedCrfType` |  |  |  |
| 11 | `DLY.PARAM.RESERVED.8` | `CntellDailyMatchingParam_Reserved8` |  |  |  |
| 12 | `DLY.PARAM.RESERVED.7` | `CntellDailyMatchingParam_Reserved7` | TField |  | Reserved for future use. |
| 13 | `DLY.PARAM.RESERVED.6` | `CntellDailyMatchingParam_Reserved6` | TField |  | Reserved for future use. |
| 14 | `DLY.PARAM.RESERVED.5` | `CntellDailyMatchingParam_Reserved5` | TField |  | Reserved for future use. |
| 15 | `DLY.PARAM.RESERVED.4` | `CntellDailyMatchingParam_Reserved4` | TField |  | Reserved for future use. |
| 16 | `DLY.PARAM.RESERVED.3` | `CntellDailyMatchingParam_Reserved3` | TField |  | Reserved for future use. |
| 17 | `DLY.PARAM.RESERVED.2` | `CntellDailyMatchingParam_Reserved2` | TField |  | Reserved for future use. |
| 18 | `DLY.PARAM.RESERVED.1` | `CntellDailyMatchingParam_Reserved1` | TField |  | Reserved for future use. |
| 19 | `DLY.PARAM.LOCAL.REF` | `CntellDailyMatchingParam_LocalRef` |  |  |  |
| 20 | `DLY.PARAM.OVERRIDE` | `CntellDailyMatchingParam_Override` |  |  |  |
| 21 | `DLY.PARAM.RECORD.STATUS` | `CntellDailyMatchingParam_RecordStatus` | String |  |  |
| 22 | `DLY.PARAM.CURR.NO` | `CntellDailyMatchingParam_CurrNo` | String |  |  |
| 23 | `DLY.PARAM.INPUTTER` | `CntellDailyMatchingParam_Inputter` |  |  |  |
| 24 | `DLY.PARAM.DATE.TIME` | `CntellDailyMatchingParam_DateTime` |  |  |  |
| 25 | `DLY.PARAM.AUTHORISER` | `CntellDailyMatchingParam_Authoriser` | String |  |  |
| 26 | `DLY.PARAM.CO.CODE` | `CntellDailyMatchingParam_CoCode` | String |  |  |
| 27 | `DLY.PARAM.DEPT.CODE` | `CntellDailyMatchingParam_DeptCode` | String |  |  |
| 28 | `DLY.PARAM.AUDITOR.CODE` | `CntellDailyMatchingParam_AuditorCode` | String |  |  |
| 29 | `DLY.PARAM.AUDIT.DATE.TIME` | `CntellDailyMatchingParam_AuditDateTime` | String |  |  |
