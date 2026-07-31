# IDD.CODE.DEF — Table Schema

> Source: `INSERTS/I_F.IDD.CODE.DEF` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDD.COD.DESCRIPTION` | `IddCodeDef_Description` |  |  |  |
| 2 | `IDD.COD.REGION.CODE.LENGTH` | `IddCodeDef_RegionCodeLength` | TField |  | This field will be used to hold the length of the area code that is to be used by the system to calculate which country the phone number belongs to |
| 3 | `IDD.COD.ZERO.REGION.PREFIX` | `IddCodeDef_ZeroRegionPrefix` | TField |  | This field will be used to determine if a zero will prefix the region code. Allowed values are YES,NO or Null |
| 4 | `IDD.COD.PHONE.NO.LENGTH` | `IddCodeDef_PhoneNoLength` | TField |  | This field will be used to hold the maximum length of the phone number excluding the IDD code. |
| 5 | `IDD.COD.RESERVED.20` | `IddCodeDef_Reserved20` | TField |  | Reserved for future use |
| 6 | `IDD.COD.RESERVED.19` | `IddCodeDef_Reserved19` | TField |  | Reserved for future use |
| 7 | `IDD.COD.RESERVED.18` | `IddCodeDef_Reserved18` | TField |  | Reserved for future use |
| 8 | `IDD.COD.RESERVED.17` | `IddCodeDef_Reserved17` | TField |  | Reserved for future use |
| 9 | `IDD.COD.RESERVED.16` | `IddCodeDef_Reserved16` | TField |  | Reserved for future use |
| 10 | `IDD.COD.RESERVED.15` | `IddCodeDef_Reserved15` | TField |  | Reserved for future use |
| 11 | `IDD.COD.RESERVED.14` | `IddCodeDef_Reserved14` | TField |  | Reserved for future use |
| 12 | `IDD.COD.RESERVED.13` | `IddCodeDef_Reserved13` | TField |  | Reserved for future use |
| 13 | `IDD.COD.RESERVED.12` | `IddCodeDef_Reserved12` | TField |  | Reserved for future use |
| 14 | `IDD.COD.RESERVED.11` | `IddCodeDef_Reserved11` | TField |  | Reserved for future use |
| 15 | `IDD.COD.RESERVED.10` | `IddCodeDef_Reserved10` | TField |  | Reserved for future use |
| 16 | `IDD.COD.RESERVED.9` | `IddCodeDef_Reserved9` | TField |  | Reserved for future use |
| 17 | `IDD.COD.RESERVED.8` | `IddCodeDef_Reserved8` | TField |  | Reserved for future use |
| 18 | `IDD.COD.RESERVED.7` | `IddCodeDef_Reserved7` | TField |  | Reserved for future use |
| 19 | `IDD.COD.RESERVED.6` | `IddCodeDef_Reserved6` | TField |  | Reserved for future use |
| 20 | `IDD.COD.RESERVED.5` | `IddCodeDef_Reserved5` | TField |  | Reserved for future use |
| 21 | `IDD.COD.RESERVED.4` | `IddCodeDef_Reserved4` | TField |  | Reserved for future use |
| 22 | `IDD.COD.RESERVED.3` | `IddCodeDef_Reserved3` | TField |  | Reserved for future use |
| 23 | `IDD.COD.RESERVED.2` | `IddCodeDef_Reserved2` | TField |  | Reserved for future use |
| 24 | `IDD.COD.RESERVED.1` | `IddCodeDef_Reserved1` | TField |  | Reserved for future use |
| 25 | `IDD.COD.LOCAL.REF` | `IddCodeDef_LocalRef` |  |  |  |
| 26 | `IDD.COD.OVERRIDE` | `IddCodeDef_Override` |  |  |  |
| 27 | `IDD.COD.RECORD.STATUS` | `IddCodeDef_RecordStatus` | String |  | Status of the record |
| 28 | `IDD.COD.CURR.NO` | `IddCodeDef_CurrNo` | String |  | Curr No |
| 29 | `IDD.COD.INPUTTER` | `IddCodeDef_Inputter` |  |  |  |
| 30 | `IDD.COD.DATE.TIME` | `IddCodeDef_DateTime` |  |  |  |
| 31 | `IDD.COD.AUTHORISER` | `IddCodeDef_Authoriser` | String |  | Authoriser |
| 32 | `IDD.COD.CO.CODE` | `IddCodeDef_CoCode` | String |  | Company code |
| 33 | `IDD.COD.DEPT.CODE` | `IddCodeDef_DeptCode` | String |  | Department code |
| 34 | `IDD.COD.AUDITOR.CODE` | `IddCodeDef_AuditorCode` | String |  | Auditor Code |
| 35 | `IDD.COD.AUDIT.DATE.TIME` | `IddCodeDef_AuditDateTime` | String |  | Audit Date and time |
