# SC.CA.MKT.PROVIDER — Table Schema

> Source: `INSERTS/I_F.SC.CA.MKT.PROVIDER` in `SC_SccConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CA.MKT.PROVIDER.BIC` | `ScCaMktProvider_ProviderBic` | TField |  | This field holds swift address/bic of the provider. Validation Rules: Must be a valid ID of the DE.BIC file |
| 2 | `SC.CA.MKT.PROVIDER.NAME` | `ScCaMktProvider_ProviderName` | TField |  | This field holds the name of the market provider Validation Rules: 35 alphanumeric characters. |
| 3 | `SC.CA.MKT.CUSTOMER.NO` | `ScCaMktProvider_CustomerNo` | TField |  | This field holds the Customer Number in Transact for the corresponding provider Validation Rules: Valid customer |
| 4 | `SC.CA.MKT.RESERVED.10` | `ScCaMktProvider_Reserved10` | TField |  |  |
| 5 | `SC.CA.MKT.RESERVED.9` | `ScCaMktProvider_Reserved9` | TField |  |  |
| 6 | `SC.CA.MKT.RESERVED.8` | `ScCaMktProvider_Reserved8` | TField |  |  |
| 7 | `SC.CA.MKT.RESERVED.7` | `ScCaMktProvider_Reserved7` | TField |  |  |
| 8 | `SC.CA.MKT.RESERVED.6` | `ScCaMktProvider_Reserved6` | TField |  |  |
| 9 | `SC.CA.MKT.RESERVED.5` | `ScCaMktProvider_Reserved5` | TField |  |  |
| 10 | `SC.CA.MKT.RESERVED.4` | `ScCaMktProvider_Reserved4` | TField |  |  |
| 11 | `SC.CA.MKT.RESERVED.3` | `ScCaMktProvider_Reserved3` | TField |  |  |
| 12 | `SC.CA.MKT.RESERVED.2` | `ScCaMktProvider_Reserved2` | TField |  |  |
| 13 | `SC.CA.MKT.RESERVED.1` | `ScCaMktProvider_Reserved1` | TField |  |  |
| 14 | `SC.CA.MKT.LOCAL.REF` | `ScCaMktProvider_LocalRef` |  |  |  |
| 15 | `SC.CA.MKT.OVERRIDE` | `ScCaMktProvider_Override` |  |  |  |
| 16 | `SC.CA.MKT.RECORD.STATUS` | `ScCaMktProvider_RecordStatus` | String |  |  |
| 17 | `SC.CA.MKT.CURR.NO` | `ScCaMktProvider_CurrNo` | String |  |  |
| 18 | `SC.CA.MKT.INPUTTER` | `ScCaMktProvider_Inputter` |  |  |  |
| 19 | `SC.CA.MKT.DATE.TIME` | `ScCaMktProvider_DateTime` |  |  |  |
| 20 | `SC.CA.MKT.AUTHORISER` | `ScCaMktProvider_Authoriser` | String |  |  |
| 21 | `SC.CA.MKT.CO.CODE` | `ScCaMktProvider_CoCode` | String |  |  |
| 22 | `SC.CA.MKT.DEPT.CODE` | `ScCaMktProvider_DeptCode` | String |  |  |
| 23 | `SC.CA.MKT.AUDITOR.CODE` | `ScCaMktProvider_AuditorCode` | String |  |  |
| 24 | `SC.CA.MKT.AUDIT.DATE.TIME` | `ScCaMktProvider_AuditDateTime` | String |  |  |
