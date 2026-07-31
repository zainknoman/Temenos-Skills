# COUNTRY.RULES — Table Schema

> Source: `INSERTS/I_F.COUNTRY.RULES` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORL.DESCRIPTION` | `CountryRules_Description` | TField |  | This will represent the description of the address country. |
| 2 | `CORL.DEFAULT.RULE` | `CountryRules_DefaultRule` | TField | Yes | It will represent the default address rule to be applied. This is mandatory. The default address rule will be used by the system when there is no address type inputted by the user when captures address information in either Customer or Delivery Address applications. It will be also used when the address type captured by the user for an address doesnt have any correspondent address rule defined into this table. (e.g. the user captures BUSINESS as an address type into the Customer application but there is only an address rule defined for RESIDENCE address type) Validation Rules: Check file ADDRESS.RULE, mandatory field |
| 3 | `CORL.ADDRESS.TYPE` | `CountryRules_AddressType` |  |  |  |
| 4 | `CORL.ADDRESS.RULE` | `CountryRules_AddressRule` |  |  |  |
| 5 | `CORL.RESERVED.10` | `CountryRules_Reserved10` | TField |  |  |
| 6 | `CORL.RESERVED.9` | `CountryRules_Reserved9` | TField |  |  |
| 7 | `CORL.RESERVED.8` | `CountryRules_Reserved8` | TField |  |  |
| 8 | `CORL.RESERVED.7` | `CountryRules_Reserved7` | TField |  |  |
| 9 | `CORL.RESERVED.6` | `CountryRules_Reserved6` | TField |  |  |
| 10 | `CORL.RESERVED.5` | `CountryRules_Reserved5` | TField |  |  |
| 11 | `CORL.RESERVED.4` | `CountryRules_Reserved4` | TField |  |  |
| 12 | `CORL.RESERVED.3` | `CountryRules_Reserved3` | TField |  |  |
| 13 | `CORL.RESERVED.2` | `CountryRules_Reserved2` | TField |  |  |
| 14 | `CORL.RESERVED.1` | `CountryRules_Reserved1` | TField |  |  |
| 15 | `CORL.LOCAL.REF` | `CountryRules_LocalRef` |  |  |  |
| 16 | `CORL.OVERRIDE` | `CountryRules_Override` |  |  |  |
| 17 | `CORL.RECORD.STATUS` | `CountryRules_RecordStatus` | String |  |  |
| 18 | `CORL.CURR.NO` | `CountryRules_CurrNo` | String |  |  |
| 19 | `CORL.INPUTTER` | `CountryRules_Inputter` |  |  |  |
| 20 | `CORL.DATE.TIME` | `CountryRules_DateTime` |  |  |  |
| 21 | `CORL.AUTHORISER` | `CountryRules_Authoriser` | String |  |  |
| 22 | `CORL.CO.CODE` | `CountryRules_CoCode` | String |  |  |
| 23 | `CORL.DEPT.CODE` | `CountryRules_DeptCode` | String |  |  |
| 24 | `CORL.AUDITOR.CODE` | `CountryRules_AuditorCode` | String |  |  |
| 25 | `CORL.AUDIT.DATE.TIME` | `CountryRules_AuditDateTime` | String |  |  |
