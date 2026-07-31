# DEBAIS.DATA.MAPPING — Table Schema

> Source: `INSERTS/I_F.DEBAIS.DATA.MAPPING` in `DEBAIS_RegulatoryReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BAIS.MAPPING.BAIS.FIELD.NAME` | `DebaisDataMapping_BaisFieldName` |  |  |  |
| 2 | `BAIS.MAPPING.T24.FIELD.VALUE` | `DebaisDataMapping_T24FieldValue` |  |  |  |
| 3 | `BAIS.MAPPING.BAIS.FIELD.VALUE` | `DebaisDataMapping_BaisFieldValue` |  |  |  |
| 4 | `BAIS.MAPPING.PRODUCT` | `DebaisDataMapping_Product` |  |  |  |
| 5 | `BAIS.MAPPING.BALANCE.TYPE` | `DebaisDataMapping_BalanceType` |  |  |  |
| 6 | `BAIS.MAPPING.LOCAL.REF` | `DebaisDataMapping_LocalRef` |  |  |  |
| 7 | `BAIS.MAPPING.RESERVED.5` | `DebaisDataMapping_Reserved5` |  |  |  |
| 8 | `BAIS.MAPPING.RESERVED.4` | `DebaisDataMapping_Reserved4` | TField |  | Reserved field for future use |
| 9 | `BAIS.MAPPING.RESERVED.3` | `DebaisDataMapping_Reserved3` | TField |  | Reserved field for future use |
| 10 | `BAIS.MAPPING.RESERVED.2` | `DebaisDataMapping_Reserved2` | TField |  | Reserved field for future use |
| 11 | `BAIS.MAPPING.RESERVED.1` | `DebaisDataMapping_Reserved1` | TField |  | Reserved field for future use |
| 12 | `BAIS.MAPPING.OVERRIDE` | `DebaisDataMapping_Override` |  |  |  |
| 13 | `BAIS.MAPPING.RECORD.STATUS` | `DebaisDataMapping_RecordStatus` | String |  |  |
| 14 | `BAIS.MAPPING.CURR.NO` | `DebaisDataMapping_CurrNo` | String |  |  |
| 15 | `BAIS.MAPPING.INPUTTER` | `DebaisDataMapping_Inputter` |  |  |  |
| 16 | `BAIS.MAPPING.DATE.TIME` | `DebaisDataMapping_DateTime` |  |  |  |
| 17 | `BAIS.MAPPING.AUTHORISER` | `DebaisDataMapping_Authoriser` | String |  |  |
| 18 | `BAIS.MAPPING.CO.CODE` | `DebaisDataMapping_CoCode` | String |  |  |
| 19 | `BAIS.MAPPING.DEPT.CODE` | `DebaisDataMapping_DeptCode` | String |  |  |
| 20 | `BAIS.MAPPING.AUDITOR.CODE` | `DebaisDataMapping_AuditorCode` | String |  |  |
| 21 | `BAIS.MAPPING.AUDIT.DATE.TIME` | `DebaisDataMapping_AuditDateTime` | String |  |  |
