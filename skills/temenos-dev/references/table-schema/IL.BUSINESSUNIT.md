# IL.BUSINESSUNIT — Table Schema

> Source: `INSERTS/I_F.IL.BUSINESSUNIT` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.BUSUNIT.BUSINESS.UNIT.NAME` | `IlBusinessunit_BusinessUnitName` | TField | Yes | This field holds the name of the business unit. Validation Rules: Standard T24 Alphanumeric field and accepts upto 35 alphanumeric characters. Mandatory field. |
| 2 | `IL.BUSUNIT.BUSINESS.UNIT.DESCRIPTION` | `IlBusinessunit_BusinessUnitDescription` |  |  |  |
| 3 | `IL.BUSUNIT.BUSINESS.UNIT.ENTITY` | `IlBusinessunit_BusinessUnitEntity` | TField |  | This field classifies and controls access within a multi entity environment. Validation Rules: Drop down field. Must be valid IL.ENTITY record |
| 4 | `IL.BUSUNIT.RESERVED.10` | `IlBusinessunit_Reserved10` | TField |  |  |
| 5 | `IL.BUSUNIT.RESERVED.9` | `IlBusinessunit_Reserved9` | TField |  |  |
| 6 | `IL.BUSUNIT.RESERVED.8` | `IlBusinessunit_Reserved8` | TField |  |  |
| 7 | `IL.BUSUNIT.RESERVED.7` | `IlBusinessunit_Reserved7` | TField |  |  |
| 8 | `IL.BUSUNIT.RESERVED.6` | `IlBusinessunit_Reserved6` | TField |  |  |
| 9 | `IL.BUSUNIT.RESERVED.5` | `IlBusinessunit_Reserved5` | TField |  |  |
| 10 | `IL.BUSUNIT.RESERVED.4` | `IlBusinessunit_Reserved4` | TField |  |  |
| 11 | `IL.BUSUNIT.RESERVED.3` | `IlBusinessunit_Reserved3` | TField |  |  |
| 12 | `IL.BUSUNIT.RESERVED.2` | `IlBusinessunit_Reserved2` | TField |  |  |
| 13 | `IL.BUSUNIT.RESERVED.1` | `IlBusinessunit_Reserved1` | TField |  |  |
| 14 | `IL.BUSUNIT.LOCAL.REF` | `IlBusinessunit_LocalRef` |  |  |  |
| 15 | `IL.BUSUNIT.OVERRIDE` | `IlBusinessunit_Override` |  |  |  |
| 16 | `IL.BUSUNIT.RECORD.STATUS` | `IlBusinessunit_RecordStatus` | String |  |  |
| 17 | `IL.BUSUNIT.CURR.NO` | `IlBusinessunit_CurrNo` | String |  |  |
| 18 | `IL.BUSUNIT.INPUTTER` | `IlBusinessunit_Inputter` |  |  |  |
| 19 | `IL.BUSUNIT.DATE.TIME` | `IlBusinessunit_DateTime` |  |  |  |
| 20 | `IL.BUSUNIT.AUTHORISER` | `IlBusinessunit_Authoriser` | String |  |  |
| 21 | `IL.BUSUNIT.CO.CODE` | `IlBusinessunit_CoCode` | String |  |  |
| 22 | `IL.BUSUNIT.DEPT.CODE` | `IlBusinessunit_DeptCode` | String |  |  |
| 23 | `IL.BUSUNIT.AUDITOR.CODE` | `IlBusinessunit_AuditorCode` | String |  |  |
| 24 | `IL.BUSUNIT.AUDIT.DATE.TIME` | `IlBusinessunit_AuditDateTime` | String |  |  |
