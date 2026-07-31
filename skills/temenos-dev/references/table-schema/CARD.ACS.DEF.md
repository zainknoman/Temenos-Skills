# CARD.ACS.DEF — Table Schema

> Source: `INSERTS/I_F.CARD.ACS.DEF` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAD.INTERFACE` | `CardAcsDef_Interface` |  |  |  |
| 2 | `CAD.BI.FLAG` | `CardAcsDef_BiFlag` |  |  |  |
| 3 | `CAD.MS.FLAG` | `CardAcsDef_MsFlag` |  |  |  |
| 4 | `CAD.WD.FLAG` | `CardAcsDef_WdFlag` |  |  |  |
| 5 | `CAD.DP.FLAG` | `CardAcsDef_DpFlag` |  |  |  |
| 6 | `CAD.TI.FLAG` | `CardAcsDef_TiFlag` |  |  |  |
| 7 | `CAD.TO.FLAG` | `CardAcsDef_ToFlag` |  |  |  |
| 8 | `CAD.BP.FLAG` | `CardAcsDef_BpFlag` |  |  |  |
| 9 | `CAD.PU.FLAG` | `CardAcsDef_PuFlag` |  |  |  |
| 10 | `CAD.EN.FLAG` | `CardAcsDef_EnFlag` |  |  |  |
| 11 | `CAD.MDB.ACCESS` | `CardAcsDef_MdbAccess` |  |  |  |
| 12 | `CAD.IMT.FLAG` | `CardAcsDef_ImtFlag` |  |  |  |
| 13 | `CAD.M2M.FLAG` | `CardAcsDef_M2mFlag` |  |  |  |
| 14 | `CAD.RESERVED.17` | `CardAcsDef_Reserved17` |  |  |  |
| 15 | `CAD.RESERVED.16` | `CardAcsDef_Reserved16` |  |  |  |
| 16 | `CAD.RESERVED.15` | `CardAcsDef_Reserved15` |  |  |  |
| 17 | `CAD.RESERVED.14` | `CardAcsDef_Reserved14` |  |  |  |
| 18 | `CAD.RESERVED.13` | `CardAcsDef_Reserved13` |  |  |  |
| 19 | `CAD.RESERVED.12` | `CardAcsDef_Reserved12` |  |  |  |
| 20 | `CAD.RESERVED.11` | `CardAcsDef_Reserved11` |  |  |  |
| 21 | `CAD.LOCAL.REF` | `CardAcsDef_LocalRef` |  |  |  |
| 22 | `CAD.OVERRIDE` | `CardAcsDef_Override` |  |  |  |
| 23 | `CAD.RESERVED.10` | `CardAcsDef_Reserved10` | TField |  |  |
| 24 | `CAD.RESERVED.9` | `CardAcsDef_Reserved9` | TField |  |  |
| 25 | `CAD.RESERVED.8` | `CardAcsDef_Reserved8` | TField |  |  |
| 26 | `CAD.RESERVED.7` | `CardAcsDef_Reserved7` | TField |  |  |
| 27 | `CAD.RESERVED.6` | `CardAcsDef_Reserved6` | TField |  |  |
| 28 | `CAD.RESERVED.5` | `CardAcsDef_Reserved5` | TField |  |  |
| 29 | `CAD.RESERVED.4` | `CardAcsDef_Reserved4` | TField |  |  |
| 30 | `CAD.RESERVED.3` | `CardAcsDef_Reserved3` | TField |  |  |
| 31 | `CAD.RESERVED.2` | `CardAcsDef_Reserved2` | TField |  |  |
| 32 | `CAD.RESERVED.1` | `CardAcsDef_Reserved1` | TField |  |  |
| 33 | `CAD.RECORD.STATUS` | `CardAcsDef_RecordStatus` | String |  |  |
| 34 | `CAD.CURR.NO` | `CardAcsDef_CurrNo` | String |  |  |
| 35 | `CAD.INPUTTER` | `CardAcsDef_Inputter` |  |  |  |
| 36 | `CAD.DATE.TIME` | `CardAcsDef_DateTime` |  |  |  |
| 37 | `CAD.AUTHORISER` | `CardAcsDef_Authoriser` | String |  |  |
| 38 | `CAD.CO.CODE` | `CardAcsDef_CoCode` | String |  |  |
| 39 | `CAD.DEPT.CODE` | `CardAcsDef_DeptCode` | String |  |  |
| 40 | `CAD.AUDITOR.CODE` | `CardAcsDef_AuditorCode` | String |  |  |
| 41 | `CAD.AUDIT.DATE.TIME` | `CardAcsDef_AuditDateTime` | String |  |  |
