# ADDRESS.MAPPING — Table Schema

> Source: `INSERTS/I_F.ADDRESS.MAPPING` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ADD.MAP.APPLICATION` | `AddressMapping_Application` |  |  |  |
| 2 | `CAMB.ADD.MAP.FIELD.NAME` | `AddressMapping_FieldName` |  |  |  |
| 3 | `CAMB.ADD.MAP.CONVERSION` | `AddressMapping_Conversion` |  |  |  |
| 4 | `CAMB.ADD.MAP.RESERVED.1` | `AddressMapping_Reserved1` | TField |  |  |
| 5 | `CAMB.ADD.MAP.RESERVED.2` | `AddressMapping_Reserved2` | TField |  |  |
| 6 | `CAMB.ADD.MAP.RESERVED.3` | `AddressMapping_Reserved3` | TField |  |  |
| 7 | `CAMB.ADD.MAP.RESERVED.4` | `AddressMapping_Reserved4` | TField |  |  |
| 8 | `CAMB.ADD.MAP.RESERVED.5` | `AddressMapping_Reserved5` | TField |  |  |
| 9 | `CAMB.ADD.MAP.RESERVED.6` | `AddressMapping_Reserved6` | TField |  |  |
| 10 | `CAMB.ADD.MAP.RESERVED.7` | `AddressMapping_Reserved7` | TField |  |  |
| 11 | `CAMB.ADD.MAP.RESERVED.8` | `AddressMapping_Reserved8` | TField |  |  |
| 12 | `CAMB.ADD.MAP.RESERVED.9` | `AddressMapping_Reserved9` | TField |  |  |
| 13 | `CAMB.ADD.MAP.RESERVED.10` | `AddressMapping_Reserved10` | TField |  |  |
| 14 | `CAMB.ADD.MAP.LOCAL.REF` | `AddressMapping_LocalRef` |  |  |  |
| 15 | `CAMB.ADD.MAP.RECORD.STATUS` | `AddressMapping_RecordStatus` | String |  |  |
| 16 | `CAMB.ADD.MAP.CURR.NO` | `AddressMapping_CurrNo` | String |  |  |
| 17 | `CAMB.ADD.MAP.INPUTTER` | `AddressMapping_Inputter` |  |  |  |
| 18 | `CAMB.ADD.MAP.DATE.TIME` | `AddressMapping_DateTime` |  |  |  |
| 19 | `CAMB.ADD.MAP.AUTHORISER` | `AddressMapping_Authoriser` | String |  |  |
| 20 | `CAMB.ADD.MAP.CO.CODE` | `AddressMapping_CoCode` | String |  |  |
| 21 | `CAMB.ADD.MAP.DEPT.CODE` | `AddressMapping_DeptCode` | String |  |  |
| 22 | `CAMB.ADD.MAP.AUDITOR.CODE` | `AddressMapping_AuditorCode` | String |  |  |
| 23 | `CAMB.ADD.MAP.AUDIT.DATE.TIME` | `AddressMapping_AuditDateTime` | String |  |  |
