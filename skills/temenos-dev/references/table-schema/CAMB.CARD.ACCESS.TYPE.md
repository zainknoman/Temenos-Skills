# CAMB.CARD.ACCESS.TYPE — Table Schema

> Source: `INSERTS/I_F.CAMB.CARD.ACCESS.TYPE` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CARD.DESCRIPTION` | `CambCardAccessType_Description` | TField |  |  |
| 2 | `CAMB.CARD.INTERFACE` | `CambCardAccessType_Interface` | TField |  |  |
| 3 | `CAMB.CARD.BI.FLAG` | `CambCardAccessType_BiFlag` | TField |  |  |
| 4 | `CAMB.CARD.MS.FLAG` | `CambCardAccessType_MsFlag` | TField |  |  |
| 5 | `CAMB.CARD.WD.FLAG` | `CambCardAccessType_WdFlag` | TField |  |  |
| 6 | `CAMB.CARD.DP.FLAG` | `CambCardAccessType_DpFlag` | TField |  |  |
| 7 | `CAMB.CARD.TI.FLAG` | `CambCardAccessType_TiFlag` | TField |  |  |
| 8 | `CAMB.CARD.TO.FLAG` | `CambCardAccessType_ToFlag` | TField |  |  |
| 9 | `CAMB.CARD.BP.FLAG` | `CambCardAccessType_BpFlag` | TField |  |  |
| 10 | `CAMB.CARD.PU.FLAG` | `CambCardAccessType_PuFlag` | TField |  |  |
| 11 | `CAMB.CARD.IMT.FLAG` | `CambCardAccessType_ImtFlag` | TField |  |  |
| 12 | `CAMB.CARD.BPS.FLAG` | `CambCardAccessType_BpsFlag` | TField |  |  |
| 13 | `CAMB.CARD.RESERVED.1` | `CambCardAccessType_Reserved1` | TField |  |  |
| 14 | `CAMB.CARD.RESERVED.2` | `CambCardAccessType_Reserved2` | TField |  |  |
| 15 | `CAMB.CARD.LOCAL.REF` | `CambCardAccessType_LocalRef` |  |  |  |
| 16 | `CAMB.CARD.OVERRIDE` | `CambCardAccessType_Override` |  |  |  |
| 17 | `CAMB.CARD.RECORD.STATUS` | `CambCardAccessType_RecordStatus` | String |  |  |
| 18 | `CAMB.CARD.CURR.NO` | `CambCardAccessType_CurrNo` | String |  |  |
| 19 | `CAMB.CARD.INPUTTER` | `CambCardAccessType_Inputter` |  |  |  |
| 20 | `CAMB.CARD.DATE.TIME` | `CambCardAccessType_DateTime` |  |  |  |
| 21 | `CAMB.CARD.AUTHORISER` | `CambCardAccessType_Authoriser` | String |  |  |
| 22 | `CAMB.CARD.CO.CODE` | `CambCardAccessType_CoCode` | String |  |  |
| 23 | `CAMB.CARD.DEPT.CODE` | `CambCardAccessType_DeptCode` | String |  |  |
| 24 | `CAMB.CARD.AUDITOR.CODE` | `CambCardAccessType_AuditorCode` | String |  |  |
| 25 | `CAMB.CARD.AUDIT.DATE.TIME` | `CambCardAccessType_AuditDateTime` | String |  |  |
