# AUADRI.ADDRESS.TYPES — Table Schema

> Source: `INSERTS/I_F.AUADRI.ADDRESS.TYPES` in `AUADRI_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUADRI.DESCRIPTION` | `AuadriAddressTypes_Description` | TField |  | Providing meaningful description for the Address Type |
| 2 | `AUADRI.LOCAL.REF` | `AuadriAddressTypes_LocalRef` |  |  |  |
| 3 | `AUADRI.OVERRIDE` | `AuadriAddressTypes_Override` |  |  |  |
| 4 | `AUADRI.RECORD.STATUS` | `AuadriAddressTypes_RecordStatus` | String |  |  |
| 5 | `AUADRI.CURR.NO` | `AuadriAddressTypes_CurrNo` | String |  |  |
| 6 | `AUADRI.INPUTTER` | `AuadriAddressTypes_Inputter` |  |  |  |
| 7 | `AUADRI.DATE.TIME` | `AuadriAddressTypes_DateTime` |  |  |  |
| 8 | `AUADRI.AUTHORISER` | `AuadriAddressTypes_Authoriser` | String |  |  |
| 9 | `AUADRI.CO.CODE` | `AuadriAddressTypes_CoCode` | String |  |  |
| 10 | `AUADRI.DEPT.CODE` | `AuadriAddressTypes_DeptCode` | String |  |  |
| 11 | `AUADRI.AUDITOR.CODE` | `AuadriAddressTypes_AuditorCode` | String |  |  |
| 12 | `AUADRI.AUDIT.DATE.TIME` | `AuadriAddressTypes_AuditDateTime` | String |  |  |
