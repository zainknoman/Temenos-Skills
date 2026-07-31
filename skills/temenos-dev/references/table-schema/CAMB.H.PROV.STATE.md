# CAMB.H.PROV.STATE — Table Schema

> Source: `INSERTS/I_F.CAMB.H.PROV.STATE` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.PROV.STAT.PROV` | `CambHProvState_StatProv` |  |  |  |
| 2 | `CAMB.PROV.DESCRIPTION` | `CambHProvState_Description` |  |  |  |
| 3 | `CAMB.PROV.RECORD.STATUS` | `CambHProvState_RecordStatus` | String |  |  |
| 4 | `CAMB.PROV.CURR.NO` | `CambHProvState_CurrNo` | String |  |  |
| 5 | `CAMB.PROV.INPUTTER` | `CambHProvState_Inputter` |  |  |  |
| 6 | `CAMB.PROV.DATE.TIME` | `CambHProvState_DateTime` |  |  |  |
| 7 | `CAMB.PROV.AUTHORISER` | `CambHProvState_Authoriser` | String |  |  |
| 8 | `CAMB.PROV.CO.CODE` | `CambHProvState_CoCode` | String |  |  |
| 9 | `CAMB.PROV.DEPT.CODE` | `CambHProvState_DeptCode` | String |  |  |
| 10 | `CAMB.PROV.AUDITOR.CODE` | `CambHProvState_AuditorCode` | String |  |  |
| 11 | `CAMB.PROV.AUDIT.DATE.TIME` | `CambHProvState_AuditDateTime` | String |  |  |
