# CAMB.H.INTENDED.USE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.H.INTENDED.USE.PARAM` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.INT.USE.DESCRIPTION` | `CambHIntendedUseParam_Description` | A (alphanumeric) |  | Field to hold the description of the intended use code.Up to 35 type A (alphanumeric) characters |
| 2 | `CAMB.INT.USE.ALLOW.CATEG` | `CambHIntendedUseParam_AllowCateg` |  |  |  |
| 3 | `CAMB.INT.USE.RESERVED.1` | `CambHIntendedUseParam_Reserved1` | TField |  |  |
| 4 | `CAMB.INT.USE.RESERVED.2` | `CambHIntendedUseParam_Reserved2` | TField |  |  |
| 5 | `CAMB.INT.USE.RESERVED.3` | `CambHIntendedUseParam_Reserved3` | TField |  |  |
| 6 | `CAMB.INT.USE.RESERVED.4` | `CambHIntendedUseParam_Reserved4` | TField |  |  |
| 7 | `CAMB.INT.USE.RESERVED.5` | `CambHIntendedUseParam_Reserved5` | TField |  |  |
| 8 | `CAMB.INT.USE.RECORD.STATUS` | `CambHIntendedUseParam_RecordStatus` | String |  |  |
| 9 | `CAMB.INT.USE.CURR.NO` | `CambHIntendedUseParam_CurrNo` | String |  |  |
| 10 | `CAMB.INT.USE.INPUTTER` | `CambHIntendedUseParam_Inputter` |  |  |  |
| 11 | `CAMB.INT.USE.DATE.TIME` | `CambHIntendedUseParam_DateTime` |  |  |  |
| 12 | `CAMB.INT.USE.AUTHORISER` | `CambHIntendedUseParam_Authoriser` | String |  |  |
| 13 | `CAMB.INT.USE.CO.CODE` | `CambHIntendedUseParam_CoCode` | String |  |  |
| 14 | `CAMB.INT.USE.DEPT.CODE` | `CambHIntendedUseParam_DeptCode` | String |  |  |
| 15 | `CAMB.INT.USE.AUDITOR.CODE` | `CambHIntendedUseParam_AuditorCode` | String |  |  |
| 16 | `CAMB.INT.USE.AUDIT.DATE.TIME` | `CambHIntendedUseParam_AuditDateTime` | String |  |  |
