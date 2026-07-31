# CAPL.PROD.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAPL.PROD.MAPPING` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PM.DESCRIPTION` | `CaplProdMapping_Description` | TField |  | Description of the tableallowed up to 35 char |
| 2 | `CAPL.PM.CONVERT.FROM.TYPE` | `CaplProdMapping_ConvertFromType` |  |  |  |
| 3 | `CAPL.PM.CONVERT.FROM` | `CaplProdMapping_ConvertFrom` |  |  |  |
| 4 | `CAPL.PM.CONVERSION` | `CaplProdMapping_Conversion` |  |  |  |
| 5 | `CAPL.PM.RESERVED.12` | `CaplProdMapping_Reserved12` |  |  |  |
| 6 | `CAPL.PM.RESERVED.11` | `CaplProdMapping_Reserved11` |  |  |  |
| 7 | `CAPL.PM.CONVERT.TO.TYPE` | `CaplProdMapping_ConvertToType` |  |  |  |
| 8 | `CAPL.PM.CONVERT.TO` | `CaplProdMapping_ConvertTo` |  |  |  |
| 9 | `CAPL.PM.RESERVED.10` | `CaplProdMapping_Reserved10` | TField |  |  |
| 10 | `CAPL.PM.RESERVED.9` | `CaplProdMapping_Reserved9` | TField |  |  |
| 11 | `CAPL.PM.RESERVED.8` | `CaplProdMapping_Reserved8` | TField |  |  |
| 12 | `CAPL.PM.RESERVED.7` | `CaplProdMapping_Reserved7` | TField |  |  |
| 13 | `CAPL.PM.RESERVED.6` | `CaplProdMapping_Reserved6` | TField |  |  |
| 14 | `CAPL.PM.RESERVED.5` | `CaplProdMapping_Reserved5` | TField |  |  |
| 15 | `CAPL.PM.RESERVED.4` | `CaplProdMapping_Reserved4` | TField |  |  |
| 16 | `CAPL.PM.RESERVED.3` | `CaplProdMapping_Reserved3` | TField |  |  |
| 17 | `CAPL.PM.RESERVED.2` | `CaplProdMapping_Reserved2` | TField |  |  |
| 18 | `CAPL.PM.RESERVED.1` | `CaplProdMapping_Reserved1` | TField |  |  |
| 19 | `CAPL.PM.LOCAL.REF` | `CaplProdMapping_LocalRef` |  |  |  |
| 20 | `CAPL.PM.OVERRIDE` | `CaplProdMapping_Override` |  |  |  |
| 21 | `CAPL.PM.RECORD.STATUS` | `CaplProdMapping_RecordStatus` | String |  |  |
| 22 | `CAPL.PM.CURR.NO` | `CaplProdMapping_CurrNo` | String |  |  |
| 23 | `CAPL.PM.INPUTTER` | `CaplProdMapping_Inputter` |  |  |  |
| 24 | `CAPL.PM.DATE.TIME` | `CaplProdMapping_DateTime` |  |  |  |
| 25 | `CAPL.PM.AUTHORISER` | `CaplProdMapping_Authoriser` | String |  |  |
| 26 | `CAPL.PM.CO.CODE` | `CaplProdMapping_CoCode` | String |  |  |
| 27 | `CAPL.PM.DEPT.CODE` | `CaplProdMapping_DeptCode` | String |  |  |
| 28 | `CAPL.PM.AUDITOR.CODE` | `CaplProdMapping_AuditorCode` | String |  |  |
| 29 | `CAPL.PM.AUDIT.DATE.TIME` | `CaplProdMapping_AuditDateTime` | String |  |  |
