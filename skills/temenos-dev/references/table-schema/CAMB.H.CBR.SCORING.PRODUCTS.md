# CAMB.H.CBR.SCORING.PRODUCTS — Table Schema

> Source: `INSERTS/I_F.CAMB.H.CBR.SCORING.PRODUCTS` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SCR.DESCRIPTION` | `CambHCbrScoringProducts_Description` |  |  |  |
| 2 | `SCR.SCORING.NUMBER` | `CambHCbrScoringProducts_ScoringNumber` | TField |  |  |
| 3 | `SCR.REPORT.ATTRIBUTE` | `CambHCbrScoringProducts_ReportAttribute` | TField |  |  |
| 4 | `SCR.PARAMETER.ID` | `CambHCbrScoringProducts_ParameterId` |  |  |  |
| 5 | `SCR.PARAMETER.TYPE` | `CambHCbrScoringProducts_ParameterType` |  |  |  |
| 6 | `SCR.PARAMETER.VALUE` | `CambHCbrScoringProducts_ParameterValue` |  |  |  |
| 7 | `SCR.REQ.IN.EXTRACT` | `CambHCbrScoringProducts_ReqInExtract` | TField |  |  |
| 8 | `SCR.RECORD.STATUS` | `CambHCbrScoringProducts_RecordStatus` | String |  |  |
| 9 | `SCR.CURR.NO` | `CambHCbrScoringProducts_CurrNo` | String |  |  |
| 10 | `SCR.INPUTTER` | `CambHCbrScoringProducts_Inputter` |  |  |  |
| 11 | `SCR.DATE.TIME` | `CambHCbrScoringProducts_DateTime` |  |  |  |
| 12 | `SCR.AUTHORISER` | `CambHCbrScoringProducts_Authoriser` | String |  |  |
| 13 | `SCR.CO.CODE` | `CambHCbrScoringProducts_CoCode` | String |  |  |
| 14 | `SCR.DEPT.CODE` | `CambHCbrScoringProducts_DeptCode` | String |  |  |
| 15 | `SCR.AUDITOR.CODE` | `CambHCbrScoringProducts_AuditorCode` | String |  |  |
| 16 | `SCR.AUDIT.DATE.TIME` | `CambHCbrScoringProducts_AuditDateTime` | String |  |  |
