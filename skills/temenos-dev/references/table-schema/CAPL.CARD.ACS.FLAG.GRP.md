# CAPL.CARD.ACS.FLAG.GRP — Table Schema

> Source: `INSERTS/I_F.CAPL.CARD.ACS.FLAG.GRP` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CRD.AC.GRP.GROUP.NAME` | `CaplCardAcsFlagGrp_GroupName` |  |  |  |
| 2 | `CP.CRD.AC.GRP.BI.FLAG` | `CaplCardAcsFlagGrp_BiFlag` |  |  |  |
| 3 | `CP.CRD.AC.GRP.MS.FLAG` | `CaplCardAcsFlagGrp_MsFlag` |  |  |  |
| 4 | `CP.CRD.AC.GRP.WD.FLAG` | `CaplCardAcsFlagGrp_WdFlag` |  |  |  |
| 5 | `CP.CRD.AC.GRP.DP.FLAG` | `CaplCardAcsFlagGrp_DpFlag` |  |  |  |
| 6 | `CP.CRD.AC.GRP.TI.FLAG` | `CaplCardAcsFlagGrp_TiFlag` |  |  |  |
| 7 | `CP.CRD.AC.GRP.TO.FLAG` | `CaplCardAcsFlagGrp_ToFlag` |  |  |  |
| 8 | `CP.CRD.AC.GRP.BP.FLAG` | `CaplCardAcsFlagGrp_BpFlag` |  |  |  |
| 9 | `CP.CRD.AC.GRP.PU.FLAG` | `CaplCardAcsFlagGrp_PuFlag` |  |  |  |
| 10 | `CP.CRD.AC.GRP.IMT.FLAG` | `CaplCardAcsFlagGrp_ImtFlag` |  |  |  |
| 11 | `CP.CRD.AC.GRP.RESERVED.9` | `CaplCardAcsFlagGrp_Reserved9` | TField |  |  |
| 12 | `CP.CRD.AC.GRP.RESERVED.8` | `CaplCardAcsFlagGrp_Reserved8` | TField |  |  |
| 13 | `CP.CRD.AC.GRP.RESERVED.7` | `CaplCardAcsFlagGrp_Reserved7` | TField |  |  |
| 14 | `CP.CRD.AC.GRP.RESERVED.6` | `CaplCardAcsFlagGrp_Reserved6` | TField |  |  |
| 15 | `CP.CRD.AC.GRP.RESERVED.5` | `CaplCardAcsFlagGrp_Reserved5` | TField |  |  |
| 16 | `CP.CRD.AC.GRP.RESERVED.4` | `CaplCardAcsFlagGrp_Reserved4` | TField |  |  |
| 17 | `CP.CRD.AC.GRP.RESERVED.3` | `CaplCardAcsFlagGrp_Reserved3` | TField |  |  |
| 18 | `CP.CRD.AC.GRP.RESERVED.2` | `CaplCardAcsFlagGrp_Reserved2` | TField |  |  |
| 19 | `CP.CRD.AC.GRP.RESERVED.1` | `CaplCardAcsFlagGrp_Reserved1` | TField |  |  |
| 20 | `CP.CRD.AC.GRP.LOCAL.REF` | `CaplCardAcsFlagGrp_LocalRef` |  |  |  |
| 21 | `CP.CRD.AC.GRP.OVERRIDE` | `CaplCardAcsFlagGrp_Override` |  |  |  |
| 22 | `CP.CRD.AC.GRP.RECORD.STATUS` | `CaplCardAcsFlagGrp_RecordStatus` | String |  |  |
| 23 | `CP.CRD.AC.GRP.CURR.NO` | `CaplCardAcsFlagGrp_CurrNo` | String |  |  |
| 24 | `CP.CRD.AC.GRP.INPUTTER` | `CaplCardAcsFlagGrp_Inputter` |  |  |  |
| 25 | `CP.CRD.AC.GRP.DATE.TIME` | `CaplCardAcsFlagGrp_DateTime` |  |  |  |
| 26 | `CP.CRD.AC.GRP.AUTHORISER` | `CaplCardAcsFlagGrp_Authoriser` | String |  |  |
| 27 | `CP.CRD.AC.GRP.CO.CODE` | `CaplCardAcsFlagGrp_CoCode` | String |  |  |
| 28 | `CP.CRD.AC.GRP.DEPT.CODE` | `CaplCardAcsFlagGrp_DeptCode` | String |  |  |
| 29 | `CP.CRD.AC.GRP.AUDITOR.CODE` | `CaplCardAcsFlagGrp_AuditorCode` | String |  |  |
| 30 | `CP.CRD.AC.GRP.AUDIT.DATE.TIME` | `CaplCardAcsFlagGrp_AuditDateTime` | String |  |  |
