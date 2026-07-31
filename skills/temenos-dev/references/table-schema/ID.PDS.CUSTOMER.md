# ID.PDS.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.ID.PDS.CUSTOMER` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CUS.DESCRIPTION` | `IdPdsCustomer_Description` |  |  |  |
| 2 | `ID.CUS.WEIGHT` | `IdPdsCustomer_Weight` | TField |  |  |
| 3 | `ID.CUS.RESERVED.10` | `IdPdsCustomer_Reserved10` | TField |  |  |
| 4 | `ID.CUS.RESERVED.9` | `IdPdsCustomer_Reserved9` | TField |  |  |
| 5 | `ID.CUS.RESERVED.8` | `IdPdsCustomer_Reserved8` | TField |  |  |
| 6 | `ID.CUS.RESERVED.7` | `IdPdsCustomer_Reserved7` | TField |  |  |
| 7 | `ID.CUS.RESERVED.6` | `IdPdsCustomer_Reserved6` | TField |  |  |
| 8 | `ID.CUS.RESERVED.5` | `IdPdsCustomer_Reserved5` | TField |  |  |
| 9 | `ID.CUS.RESERVED.4` | `IdPdsCustomer_Reserved4` | TField |  |  |
| 10 | `ID.CUS.RESERVED.3` | `IdPdsCustomer_Reserved3` | TField |  |  |
| 11 | `ID.CUS.RESERVED.2` | `IdPdsCustomer_Reserved2` | TField |  |  |
| 12 | `ID.CUS.RESERVED.1` | `IdPdsCustomer_Reserved1` | TField |  |  |
| 13 | `ID.CUS.LOCAL.REF` | `IdPdsCustomer_LocalRef` |  |  |  |
| 14 | `ID.CUS.OVERRIDE` | `IdPdsCustomer_Override` |  |  |  |
| 15 | `ID.CUS.RECORD.STATUS` | `IdPdsCustomer_RecordStatus` | String |  |  |
| 16 | `ID.CUS.CURR.NO` | `IdPdsCustomer_CurrNo` | String |  |  |
| 17 | `ID.CUS.INPUTTER` | `IdPdsCustomer_Inputter` |  |  |  |
| 18 | `ID.CUS.DATE.TIME` | `IdPdsCustomer_DateTime` |  |  |  |
| 19 | `ID.CUS.AUTHORISER` | `IdPdsCustomer_Authoriser` | String |  |  |
| 20 | `ID.CUS.CO.CODE` | `IdPdsCustomer_CoCode` | String |  |  |
| 21 | `ID.CUS.DEPT.CODE` | `IdPdsCustomer_DeptCode` | String |  |  |
| 22 | `ID.CUS.AUDITOR.CODE` | `IdPdsCustomer_AuditorCode` | String |  |  |
| 23 | `ID.CUS.AUDIT.DATE.TIME` | `IdPdsCustomer_AuditDateTime` | String |  |  |
