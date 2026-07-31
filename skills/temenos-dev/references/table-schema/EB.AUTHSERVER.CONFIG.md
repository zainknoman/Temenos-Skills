# EB.AUTHSERVER.CONFIG — Table Schema

> Source: `INSERTS/I_F.EB.AUTHSERVER.CONFIG` in `EB_ArcSecurity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.AC.DESCRIPTION` | `EbAuthserverConfig_Description` | TField |  | A free text field to give a meaningful description to the record. Has no business/functional usage and is only an informative field. |
| 2 | `EB.AC.FIELD.NAMES` | `EbAuthserverConfig_FieldNames` |  |  |  |
| 3 | `EB.AC.RESERVED.5` | `EbAuthserverConfig_Reserved5` | TField |  |  |
| 4 | `EB.AC.RESERVED.4` | `EbAuthserverConfig_Reserved4` | TField |  |  |
| 5 | `EB.AC.RESERVED.3` | `EbAuthserverConfig_Reserved3` | TField |  |  |
| 6 | `EB.AC.RESERVED.2` | `EbAuthserverConfig_Reserved2` | TField |  |  |
| 7 | `EB.AC.RESERVED.1` | `EbAuthserverConfig_Reserved1` | TField |  |  |
| 8 | `EB.AC.LOCAL.REF` | `EbAuthserverConfig_LocalRef` |  |  |  |
| 9 | `EB.AC.OVERRIDE.TEXT` | `EbAuthserverConfig_OverrideText` |  |  |  |
| 10 | `EB.AC.RECORD.STATUS` | `EbAuthserverConfig_RecordStatus` | String |  |  |
| 11 | `EB.AC.CURR.NO` | `EbAuthserverConfig_CurrNo` | String |  |  |
| 12 | `EB.AC.INPUTTER` | `EbAuthserverConfig_Inputter` |  |  |  |
| 13 | `EB.AC.DATE.TIME` | `EbAuthserverConfig_DateTime` |  |  |  |
| 14 | `EB.AC.AUTHORISER` | `EbAuthserverConfig_Authoriser` | String |  |  |
| 15 | `EB.AC.CO.CODE` | `EbAuthserverConfig_CoCode` | String |  |  |
| 16 | `EB.AC.DEPT.CODE` | `EbAuthserverConfig_DeptCode` | String |  |  |
| 17 | `EB.AC.AUDITOR.CODE` | `EbAuthserverConfig_AuditorCode` | String |  |  |
| 18 | `EB.AC.AUDIT.DATE.TIME` | `EbAuthserverConfig_AuditDateTime` | String |  |  |
