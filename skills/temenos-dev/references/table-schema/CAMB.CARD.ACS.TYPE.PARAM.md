# CAMB.CARD.ACS.TYPE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.CARD.ACS.TYPE.PARAM` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CARD.PARAM.DESCRIPTION` | `CambCardAcsTypeParam_Description` | TField |  |  |
| 2 | `CAMB.CARD.PARAM.INTERFACE` | `CambCardAcsTypeParam_Interface` |  |  |  |
| 3 | `CAMB.CARD.PARAM.ACCESS.LEVEL` | `CambCardAcsTypeParam_AccessLevel` |  |  |  |
| 4 | `CAMB.CARD.PARAM.DEFAULT.ACS` | `CambCardAcsTypeParam_DefaultAcs` |  |  |  |
| 5 | `CAMB.CARD.PARAM.RESERVED.1` | `CambCardAcsTypeParam_Reserved1` | TField |  |  |
| 6 | `CAMB.CARD.PARAM.RESERVED.2` | `CambCardAcsTypeParam_Reserved2` | TField |  |  |
| 7 | `CAMB.CARD.PARAM.LOCAL.REF` | `CambCardAcsTypeParam_LocalRef` |  |  |  |
| 8 | `CAMB.CARD.PARAM.OVERRIDE` | `CambCardAcsTypeParam_Override` |  |  |  |
| 9 | `CAMB.CARD.PARAM.RECORD.STATUS` | `CambCardAcsTypeParam_RecordStatus` | String |  |  |
| 10 | `CAMB.CARD.PARAM.CURR.NO` | `CambCardAcsTypeParam_CurrNo` | String |  |  |
| 11 | `CAMB.CARD.PARAM.INPUTTER` | `CambCardAcsTypeParam_Inputter` |  |  |  |
| 12 | `CAMB.CARD.PARAM.DATE.TIME` | `CambCardAcsTypeParam_DateTime` |  |  |  |
| 13 | `CAMB.CARD.PARAM.AUTHORISER` | `CambCardAcsTypeParam_Authoriser` | String |  |  |
| 14 | `CAMB.CARD.PARAM.CO.CODE` | `CambCardAcsTypeParam_CoCode` | String |  |  |
| 15 | `CAMB.CARD.PARAM.DEPT.CODE` | `CambCardAcsTypeParam_DeptCode` | String |  |  |
| 16 | `CAMB.CARD.PARAM.AUDITOR.CODE` | `CambCardAcsTypeParam_AuditorCode` | String |  |  |
| 17 | `CAMB.CARD.PARAM.AUDIT.DATE.TIME` | `CambCardAcsTypeParam_AuditDateTime` | String |  |  |
