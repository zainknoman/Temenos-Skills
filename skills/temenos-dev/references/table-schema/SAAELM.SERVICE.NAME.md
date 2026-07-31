# SAAELM.SERVICE.NAME — Table Schema

> Source: `INSERTS/I_F.SAAELM.SERVICE.NAME` in `SAAELM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAAELM.SERVICES.DESCRIPTION` | `SaaelmServiceName_Description` | TField |  | A brief description about the preferred lookup. The value of this field will be part of the drop down list when the combo box is invoked. |
| 2 | `SAAELM.SERVICES.WSDL.LINK` | `SaaelmServiceName_WsdlLink` | TField |  | This field captures the WSDL Link URL. |
| 3 | `SAAELM.SERVICES.RESERVED.1` | `SaaelmServiceName_Reserved1` | TField |  | Reserved for future use |
| 4 | `SAAELM.SERVICES.RESERVED.2` | `SaaelmServiceName_Reserved2` | TField |  | Reserved for future use |
| 5 | `SAAELM.SERVICES.RESERVED.3` | `SaaelmServiceName_Reserved3` | TField |  | Reserved for future use |
| 6 | `SAAELM.SERVICES.RESERVED.4` | `SaaelmServiceName_Reserved4` | TField |  | Reserved for future use |
| 7 | `SAAELM.SERVICES.RESERVED.5` | `SaaelmServiceName_Reserved5` | TField |  | Reserved for future use |
| 8 | `SAAELM.SERVICES.RESERVED.6` | `SaaelmServiceName_Reserved6` | TField |  | Reserved for future use |
| 9 | `SAAELM.SERVICES.RESERVED.7` | `SaaelmServiceName_Reserved7` | TField |  | Reserved for future use |
| 10 | `SAAELM.SERVICES.RESERVED.8` | `SaaelmServiceName_Reserved8` | TField |  | Reserved for future use |
| 11 | `SAAELM.SERVICES.RESERVED.9` | `SaaelmServiceName_Reserved9` | TField |  | Reserved for future use |
| 12 | `SAAELM.SERVICES.RESERVED.10` | `SaaelmServiceName_Reserved10` | TField |  | Reserved for future use |
| 13 | `SAAELM.SERVICES.LOCAL.REF` | `SaaelmServiceName_LocalRef` |  |  |  |
| 14 | `SAAELM.SERVICES.OVERRIDE` | `SaaelmServiceName_Override` |  |  |  |
| 15 | `SAAELM.SERVICES.RECORD.STATUS` | `SaaelmServiceName_RecordStatus` | String |  |  |
| 16 | `SAAELM.SERVICES.CURR.NO` | `SaaelmServiceName_CurrNo` | String |  |  |
| 17 | `SAAELM.SERVICES.INPUTTER` | `SaaelmServiceName_Inputter` |  |  |  |
| 18 | `SAAELM.SERVICES.DATE.TIME` | `SaaelmServiceName_DateTime` |  |  |  |
| 19 | `SAAELM.SERVICES.AUTHORISER` | `SaaelmServiceName_Authoriser` | String |  |  |
| 20 | `SAAELM.SERVICES.CO.CODE` | `SaaelmServiceName_CoCode` | String |  |  |
| 21 | `SAAELM.SERVICES.DEPT.CODE` | `SaaelmServiceName_DeptCode` | String |  |  |
| 22 | `SAAELM.SERVICES.AUDITOR.CODE` | `SaaelmServiceName_AuditorCode` | String |  |  |
| 23 | `SAAELM.SERVICES.AUDIT.DATE.TIME` | `SaaelmServiceName_AuditDateTime` | String |  |  |
