# CP.VARIANT.SELECTION — Table Schema

> Source: `INSERTS/I_F.CP.VARIANT.SELECTION` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.VS.NAME` | `CpVariantSelection_Name` | TField | Yes | This field stores the name of the variant selection. Validation Rules :Mandatory field, any 50 characters. |
| 2 | `CP.VS.DESCRIPTION` | `CpVariantSelection_Description` |  |  |  |
| 3 | `CP.VS.PROJECT.NAME` | `CpVariantSelection_ProjectName` | TField |  | Each variant selection has a correspondent .ifp UXP project. This field stores the name of the corresponding UXP project for the given variant selection. Validation Rules :Any 100 characters. |
| 4 | `CP.VS.HAS.GLOBAL.OPTIONS` | `CpVariantSelection_HasGlobalOptions` | TField |  | This field stores only "yes" and "no" values. |
| 5 | `CP.VS.GLOBAL.DATA` | `CpVariantSelection_GlobalData` |  |  |  |
| 6 | `CP.VS.HAS.VARIANT.OPTIONS` | `CpVariantSelection_HasVariantOptions` |  |  |  |
| 7 | `CP.VS.RESERVED.10` | `CpVariantSelection_Reserved10` | TField |  |  |
| 8 | `CP.VS.RESERVED.9` | `CpVariantSelection_Reserved9` | TField |  |  |
| 9 | `CP.VS.RESERVED.8` | `CpVariantSelection_Reserved8` | TField |  |  |
| 10 | `CP.VS.RESERVED.7` | `CpVariantSelection_Reserved7` | TField |  |  |
| 11 | `CP.VS.RESERVED.6` | `CpVariantSelection_Reserved6` | TField |  |  |
| 12 | `CP.VS.RESERVED.5` | `CpVariantSelection_Reserved5` | TField |  |  |
| 13 | `CP.VS.RESERVED.4` | `CpVariantSelection_Reserved4` | TField |  |  |
| 14 | `CP.VS.RESERVED.3` | `CpVariantSelection_Reserved3` | TField |  |  |
| 15 | `CP.VS.RESERVED.2` | `CpVariantSelection_Reserved2` | TField |  |  |
| 16 | `CP.VS.RESERVED.1` | `CpVariantSelection_Reserved1` | TField |  |  |
| 17 | `CP.VS.LOCAL.REF` | `CpVariantSelection_LocalRef` |  |  |  |
| 18 | `CP.VS.OVERRIDE` | `CpVariantSelection_Override` |  |  |  |
| 19 | `CP.VS.RECORD.STATUS` | `CpVariantSelection_RecordStatus` | String |  |  |
| 20 | `CP.VS.CURR.NO` | `CpVariantSelection_CurrNo` | String |  |  |
| 21 | `CP.VS.INPUTTER` | `CpVariantSelection_Inputter` |  |  |  |
| 22 | `CP.VS.DATE.TIME` | `CpVariantSelection_DateTime` |  |  |  |
| 23 | `CP.VS.AUTHORISER` | `CpVariantSelection_Authoriser` | String |  |  |
| 24 | `CP.VS.CO.CODE` | `CpVariantSelection_CoCode` | String |  |  |
| 25 | `CP.VS.DEPT.CODE` | `CpVariantSelection_DeptCode` | String |  |  |
| 26 | `CP.VS.AUDITOR.CODE` | `CpVariantSelection_AuditorCode` | String |  |  |
| 27 | `CP.VS.AUDIT.DATE.TIME` | `CpVariantSelection_AuditDateTime` | String |  |  |
