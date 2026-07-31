# CAMB.H.XML.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAMB.H.XML.MAPPING` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `XML.MAP.DESCRIPTION` | `CambHXmlMapping_Description` |  |  |  |
| 2 | `XML.MAP.PARENT.TAG.NAME` | `CambHXmlMapping_ParentTagName` |  |  |  |
| 3 | `XML.MAP.PARENT.TAG.VAL` | `CambHXmlMapping_ParentTagVal` |  |  |  |
| 4 | `XML.MAP.CHILD.TAG.NAME` | `CambHXmlMapping_ChildTagName` |  |  |  |
| 5 | `XML.MAP.CHILD.TAG.VAL` | `CambHXmlMapping_ChildTagVal` |  |  |  |
| 6 | `XML.MAP.CR.REP.FLD.NAME` | `CambHXmlMapping_CrRepFldName` |  |  |  |
| 7 | `XML.MAP.CR.SINGLE.MULTI` | `CambHXmlMapping_CrSingleMulti` |  |  |  |
| 8 | `XML.MAP.RECORD.STATUS` | `CambHXmlMapping_RecordStatus` | String |  |  |
| 9 | `XML.MAP.CURR.NO` | `CambHXmlMapping_CurrNo` | String |  |  |
| 10 | `XML.MAP.INPUTTER` | `CambHXmlMapping_Inputter` |  |  |  |
| 11 | `XML.MAP.DATE.TIME` | `CambHXmlMapping_DateTime` |  |  |  |
| 12 | `XML.MAP.AUTHORISER` | `CambHXmlMapping_Authoriser` | String |  |  |
| 13 | `XML.MAP.CO.CODE` | `CambHXmlMapping_CoCode` | String |  |  |
| 14 | `XML.MAP.DEPT.CODE` | `CambHXmlMapping_DeptCode` | String |  |  |
| 15 | `XML.MAP.AUDITOR.CODE` | `CambHXmlMapping_AuditorCode` | String |  |  |
| 16 | `XML.MAP.AUDIT.DATE.TIME` | `CambHXmlMapping_AuditDateTime` | String |  |  |
