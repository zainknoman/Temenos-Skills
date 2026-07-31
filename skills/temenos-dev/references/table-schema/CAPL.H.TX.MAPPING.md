# CAPL.H.TX.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.MAPPING` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TX.MAP.GIT.ID` | `CaplHTxMapping_GitId` | TField |  |  |
| 2 | `CAPL.TX.MAP.FIELD.NAME` | `CaplHTxMapping_FieldName` |  |  |  |
| 3 | `CAPL.TX.MAP.INC.TXN.CODE` | `CaplHTxMapping_IncTxnCode` |  |  |  |
| 4 | `CAPL.TX.MAP.DEF.FLD.NAME` | `CaplHTxMapping_DefFldName` |  |  |  |
| 5 | `CAPL.TX.MAP.DEF.FLD.VALUE` | `CaplHTxMapping_DefFldValue` |  |  |  |
| 6 | `CAPL.TX.MAP.RESERVED.10` | `CaplHTxMapping_Reserved10` |  |  |  |
| 7 | `CAPL.TX.MAP.RESERVED.9` | `CaplHTxMapping_Reserved9` |  |  |  |
| 8 | `CAPL.TX.MAP.RESERVED.8` | `CaplHTxMapping_Reserved8` |  |  |  |
| 9 | `CAPL.TX.MAP.RESERVED.7` | `CaplHTxMapping_Reserved7` |  |  |  |
| 10 | `CAPL.TX.MAP.RESERVED.6` | `CaplHTxMapping_Reserved6` | TField |  |  |
| 11 | `CAPL.TX.MAP.RESERVED.5` | `CaplHTxMapping_Reserved5` | TField |  |  |
| 12 | `CAPL.TX.MAP.RESERVED.4` | `CaplHTxMapping_Reserved4` | TField |  |  |
| 13 | `CAPL.TX.MAP.RESERVED.3` | `CaplHTxMapping_Reserved3` | TField |  |  |
| 14 | `CAPL.TX.MAP.RESERVED.2` | `CaplHTxMapping_Reserved2` | TField |  |  |
| 15 | `CAPL.TX.MAP.RESERVED.1` | `CaplHTxMapping_Reserved1` | TField |  |  |
| 16 | `CAPL.TX.MAP.LOCAL.REF` | `CaplHTxMapping_LocalRef` |  |  |  |
| 17 | `CAPL.TX.MAP.OVERRIDE` | `CaplHTxMapping_Override` |  |  |  |
| 18 | `CAPL.TX.MAP.RECORD.STATUS` | `CaplHTxMapping_RecordStatus` | String |  |  |
| 19 | `CAPL.TX.MAP.CURR.NO` | `CaplHTxMapping_CurrNo` | String |  |  |
| 20 | `CAPL.TX.MAP.INPUTTER` | `CaplHTxMapping_Inputter` |  |  |  |
| 21 | `CAPL.TX.MAP.DATE.TIME` | `CaplHTxMapping_DateTime` |  |  |  |
| 22 | `CAPL.TX.MAP.AUTHORISER` | `CaplHTxMapping_Authoriser` | String |  |  |
| 23 | `CAPL.TX.MAP.CO.CODE` | `CaplHTxMapping_CoCode` | String |  |  |
| 24 | `CAPL.TX.MAP.DEPT.CODE` | `CaplHTxMapping_DeptCode` | String |  |  |
| 25 | `CAPL.TX.MAP.AUDITOR.CODE` | `CaplHTxMapping_AuditorCode` | String |  |  |
| 26 | `CAPL.TX.MAP.AUDIT.DATE.TIME` | `CaplHTxMapping_AuditDateTime` | String |  |  |
