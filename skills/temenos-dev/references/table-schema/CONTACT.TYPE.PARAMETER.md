# CONTACT.TYPE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CONTACT.TYPE.PARAMETER` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CTP.DESCRIPTION` | `ContactTypeParameter_Description` | TField |  | Identifies the purpose of the setup. |
| 2 | `ST.CTP.TYPE` | `ContactTypeParameter_Type` |  |  |  |
| 3 | `ST.CTP.UPD.PRIMARY.ADDR` | `ContactTypeParameter_UpdPrimaryAddr` | TField | No | Optional Field If set to Yes the primary delivery address(es) will be automatically updated. This option is allowed only when UPDATE CONTACT DATA DIRECTLY is set to Yes in COUNTRY.PARAMETER. If No or blank then the contact data will not be updated in the primary delivery addresses Validation rules This option is allowed only when UPD.CONTACT.DATA.DIRECT is set to Yes in COUNTRY.PARAMETER. The bank cannot define 2 contact types which have the same type and the Update Primary Address set to Yes. |
| 4 | `ST.CTP.RESERVED.10` | `ContactTypeParameter_Reserved10` | TField |  |  |
| 5 | `ST.CTP.RESERVED.9` | `ContactTypeParameter_Reserved9` | TField |  |  |
| 6 | `ST.CTP.RESERVED.8` | `ContactTypeParameter_Reserved8` | TField |  |  |
| 7 | `ST.CTP.RESERVED.7` | `ContactTypeParameter_Reserved7` | TField |  |  |
| 8 | `ST.CTP.RESERVED.6` | `ContactTypeParameter_Reserved6` | TField |  |  |
| 9 | `ST.CTP.RESERVED.5` | `ContactTypeParameter_Reserved5` | TField |  |  |
| 10 | `ST.CTP.RESERVED.4` | `ContactTypeParameter_Reserved4` | TField |  |  |
| 11 | `ST.CTP.RESERVED.3` | `ContactTypeParameter_Reserved3` | TField |  |  |
| 12 | `ST.CTP.RESERVED.2` | `ContactTypeParameter_Reserved2` | TField |  |  |
| 13 | `ST.CTP.RESERVED.1` | `ContactTypeParameter_Reserved1` | TField |  |  |
| 14 | `ST.CTP.LOCAL.REF` | `ContactTypeParameter_LocalRef` |  |  |  |
| 15 | `ST.CTP.OVERRIDE` | `ContactTypeParameter_Override` |  |  |  |
| 16 | `ST.CTP.RECORD.STATUS` | `ContactTypeParameter_RecordStatus` | String |  |  |
| 17 | `ST.CTP.CURR.NO` | `ContactTypeParameter_CurrNo` | String |  |  |
| 18 | `ST.CTP.INPUTTER` | `ContactTypeParameter_Inputter` |  |  |  |
| 19 | `ST.CTP.DATE.TIME` | `ContactTypeParameter_DateTime` |  |  |  |
| 20 | `ST.CTP.AUTHORISER` | `ContactTypeParameter_Authoriser` | String |  |  |
| 21 | `ST.CTP.CO.CODE` | `ContactTypeParameter_CoCode` | String |  |  |
| 22 | `ST.CTP.DEPT.CODE` | `ContactTypeParameter_DeptCode` | String |  |  |
| 23 | `ST.CTP.AUDITOR.CODE` | `ContactTypeParameter_AuditorCode` | String |  |  |
| 24 | `ST.CTP.AUDIT.DATE.TIME` | `ContactTypeParameter_AuditDateTime` | String |  |  |
