# SAWATQ.MAPPING — Table Schema

> Source: `INSERTS/I_F.SAWATQ.MAPPING` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.MAP.NOFILE.TEMPLATE` | `SawatqMapping_NofileTemplate` | TField |  | Holds the STANDARD.SELECTION name has been configured in EB.LOOKUP>SAWATQ.STANDARD.SELECTION |
| 2 | `SA.MAP.ATTRIBUTE` | `SawatqMapping_Attribute` |  |  |  |
| 3 | `SA.MAP.INQUIRED.PARTY` | `SawatqMapping_InquiredParty` |  |  |  |
| 4 | `SA.MAP.APPLICATION` | `SawatqMapping_Application` |  |  |  |
| 5 | `SA.MAP.FIELD.NAME` | `SawatqMapping_FieldName` |  |  |  |
| 6 | `SA.MAP.CONVERSION.ROUTINE` | `SawatqMapping_ConversionRoutine` |  |  |  |
| 7 | `SA.MAP.LOCAL.REF` | `SawatqMapping_LocalRef` |  |  |  |
| 8 | `SA.MAP.OVERRIDE` | `SawatqMapping_Override` |  |  |  |
| 9 | `SA.MAP.RESERVED.1` | `SawatqMapping_Reserved1` | TField |  |  |
| 10 | `SA.MAP.RESERVED.2` | `SawatqMapping_Reserved2` | TField |  |  |
| 11 | `SA.MAP.RESERVED.3` | `SawatqMapping_Reserved3` | TField |  |  |
| 12 | `SA.MAP.RESERVED.4` | `SawatqMapping_Reserved4` | TField |  |  |
| 13 | `SA.MAP.RESERVED.5` | `SawatqMapping_Reserved5` | TField |  |  |
| 14 | `SA.MAP.RESERVED.6` | `SawatqMapping_Reserved6` | TField |  |  |
| 15 | `SA.MAP.RESERVED.7` | `SawatqMapping_Reserved7` | TField |  |  |
| 16 | `SA.MAP.RESERVED.8` | `SawatqMapping_Reserved8` | TField |  |  |
| 17 | `SA.MAP.RESERVED.9` | `SawatqMapping_Reserved9` | TField |  |  |
| 18 | `SA.MAP.RESERVED.10` | `SawatqMapping_Reserved10` | TField |  |  |
| 19 | `SA.MAP.RECORD.STATUS` | `SawatqMapping_RecordStatus` | String |  |  |
| 20 | `SA.MAP.CURR.NO` | `SawatqMapping_CurrNo` | String |  |  |
| 21 | `SA.MAP.INPUTTER` | `SawatqMapping_Inputter` |  |  |  |
| 22 | `SA.MAP.DATE.TIME` | `SawatqMapping_DateTime` |  |  |  |
| 23 | `SA.MAP.AUTHORISER` | `SawatqMapping_Authoriser` | String |  |  |
| 24 | `SA.MAP.CO.CODE` | `SawatqMapping_CoCode` | String |  |  |
| 25 | `SA.MAP.DEPT.CODE` | `SawatqMapping_DeptCode` | String |  |  |
| 26 | `SA.MAP.AUDITOR.CODE` | `SawatqMapping_AuditorCode` | String |  |  |
| 27 | `SA.MAP.AUDIT.DATE.TIME` | `SawatqMapping_AuditDateTime` | String |  |  |
