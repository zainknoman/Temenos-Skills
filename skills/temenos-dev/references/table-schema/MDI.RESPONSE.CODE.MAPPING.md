# MDI.RESPONSE.CODE.MAPPING — Table Schema

> Source: `INSERTS/I_F.MDI.RESPONSE.CODE.MAPPING` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.RES.MDI.ERR.TEXT` | `MdiResponseCodeMapping_MdiErrText` |  |  |  |
| 2 | `MDI.RES.LOCATE.ERR.CODE` | `MdiResponseCodeMapping_LocateErrCode` |  |  |  |
| 3 | `MDI.RES.MDI.RESPONSE.CODE` | `MdiResponseCodeMapping_MdiResponseCode` |  |  |  |
| 4 | `MDI.RES.RESERVED.10` | `MdiResponseCodeMapping_Reserved10` |  |  |  |
| 5 | `MDI.RES.RESERVED.9` | `MdiResponseCodeMapping_Reserved9` |  |  |  |
| 6 | `MDI.RES.RESERVED.8` | `MdiResponseCodeMapping_Reserved8` |  |  |  |
| 7 | `MDI.RES.RESERVED.7` | `MdiResponseCodeMapping_Reserved7` |  |  |  |
| 8 | `MDI.RES.RESERVED.6` | `MdiResponseCodeMapping_Reserved6` |  |  |  |
| 9 | `MDI.RES.RESERVED.5` | `MdiResponseCodeMapping_Reserved5` |  |  |  |
| 10 | `MDI.RES.RESERVED.4` | `MdiResponseCodeMapping_Reserved4` |  |  |  |
| 11 | `MDI.RES.RESERVED.3` | `MdiResponseCodeMapping_Reserved3` |  |  |  |
| 12 | `MDI.RES.RESERVED.2` | `MdiResponseCodeMapping_Reserved2` |  |  |  |
| 13 | `MDI.RES.RESERVED.1` | `MdiResponseCodeMapping_Reserved1` |  |  |  |
| 14 | `MDI.RES.LOCAL.REF` | `MdiResponseCodeMapping_LocalRef` |  |  |  |
| 15 | `MDI.RES.OVERRIDE` | `MdiResponseCodeMapping_Override` |  |  |  |
| 16 | `MDI.RES.RECORD.STATUS` | `MdiResponseCodeMapping_RecordStatus` |  |  |  |
| 17 | `MDI.RES.CURR.NO` | `MdiResponseCodeMapping_CurrNo` |  |  |  |
| 18 | `MDI.RES.INPUTTER` | `MdiResponseCodeMapping_Inputter` |  |  |  |
| 19 | `MDI.RES.DATE.TIME` | `MdiResponseCodeMapping_DateTime` |  |  |  |
| 20 | `MDI.RES.AUTHORISER` | `MdiResponseCodeMapping_Authoriser` |  |  |  |
| 21 | `MDI.RES.CO.CODE` | `MdiResponseCodeMapping_CoCode` |  |  |  |
| 22 | `MDI.RES.DEPT.CODE` | `MdiResponseCodeMapping_DeptCode` |  |  |  |
| 23 | `MDI.RES.AUDITOR.CODE` | `MdiResponseCodeMapping_AuditorCode` |  |  |  |
| 24 | `MDI.RES.AUDIT.DATE.TIME` | `MdiResponseCodeMapping_AuditDateTime` |  |  |  |
