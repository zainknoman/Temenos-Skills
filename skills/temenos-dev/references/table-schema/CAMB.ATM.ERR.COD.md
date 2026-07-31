# CAMB.ATM.ERR.COD — Table Schema

> Source: `INSERTS/I_F.CAMB.ATM.ERR.COD` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ERR.COD.ERR.CODE` | `CambAtmErrCod_ErrCode` |  |  |  |
| 2 | `ERR.COD.RECORD.STATUS` | `CambAtmErrCod_RecordStatus` | String |  |  |
| 3 | `ERR.COD.CURR.NO` | `CambAtmErrCod_CurrNo` | String |  |  |
| 4 | `ERR.COD.INPUTTER` | `CambAtmErrCod_Inputter` |  |  |  |
| 5 | `ERR.COD.DATE.TIME` | `CambAtmErrCod_DateTime` |  |  |  |
| 6 | `ERR.COD.AUTHORISER` | `CambAtmErrCod_Authoriser` | String |  |  |
| 7 | `ERR.COD.CO.CODE` | `CambAtmErrCod_CoCode` | String |  |  |
| 8 | `ERR.COD.DEPT.CODE` | `CambAtmErrCod_DeptCode` | String |  |  |
| 9 | `ERR.COD.AUDITOR.CODE` | `CambAtmErrCod_AuditorCode` | String |  |  |
| 10 | `ERR.COD.AUDIT.DATE.TIME` | `CambAtmErrCod_AuditDateTime` | String |  |  |
