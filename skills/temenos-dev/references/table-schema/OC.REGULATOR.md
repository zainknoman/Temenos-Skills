# OC.REGULATOR — Table Schema

> Source: `INSERTS/I_F.OC.REGULATOR` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.REG.REGULATOR.NAME` | `OcRegulator_RegulatorName` |  |  |  |
| 2 | `OC.REG.REGULATOR.LEI` | `OcRegulator_RegulatorLei` | TField | No | Denotes the Legal Entity Identifier of the regulator. Validation Rules: Optional field. Upto 50 alphanumeric characters |
| 3 | `OC.REG.COUNTRY` | `OcRegulator_Country` | TField | No | Denotes the country of the regulator. Validation Rules: Should be a valid country code. Optional field |
| 4 | `OC.REG.GEOGRAPHICAL.BLOCK` | `OcRegulator_GeographicalBlock` | TField | No | Denotes the geographical block of the regulator . Validation Rules: Should be a valid record in geographical block . Defaulted with the geographical block value defined in COUNTRY Optional field |
| 5 | `OC.REG.REPORTING.JURISDICTION` | `OcRegulator_ReportingJurisdiction` | TField | Yes | Denotes whether both the counterparties or one of the counterparties is required to make the reporting under whose regulator�s jurisdiction the T24 bank is operating. Validation Rules: Mandatory field. Valid values are Single or Multiple. |
| 6 | `OC.REG.RESERVED10` | `OcRegulator_Reserved10` | TField |  |  |
| 7 | `OC.REG.RESERVED9` | `OcRegulator_Reserved9` | TField |  |  |
| 8 | `OC.REG.RESERVED8` | `OcRegulator_Reserved8` | TField |  |  |
| 9 | `OC.REG.RESERVED7` | `OcRegulator_Reserved7` | TField |  |  |
| 10 | `OC.REG.RESERVED6` | `OcRegulator_Reserved6` | TField |  |  |
| 11 | `OC.REG.RESERVED5` | `OcRegulator_Reserved5` | TField |  |  |
| 12 | `OC.REG.RESERVED4` | `OcRegulator_Reserved4` | TField |  |  |
| 13 | `OC.REG.RESERVED3` | `OcRegulator_Reserved3` | TField |  |  |
| 14 | `OC.REG.RESERVED2` | `OcRegulator_Reserved2` | TField |  |  |
| 15 | `OC.REG.RESERVED1` | `OcRegulator_Reserved1` | TField |  |  |
| 16 | `OC.REG.LOCAL.REF` | `OcRegulator_LocalRef` |  |  |  |
| 17 | `OC.REG.RECORD.STATUS` | `OcRegulator_RecordStatus` | String |  |  |
| 18 | `OC.REG.CURR.NO` | `OcRegulator_CurrNo` | String |  |  |
| 19 | `OC.REG.INPUTTER` | `OcRegulator_Inputter` |  |  |  |
| 20 | `OC.REG.DATE.TIME` | `OcRegulator_DateTime` |  |  |  |
| 21 | `OC.REG.AUTHORISER` | `OcRegulator_Authoriser` | String |  |  |
| 22 | `OC.REG.CO.CODE` | `OcRegulator_CoCode` | String |  |  |
| 23 | `OC.REG.DEPT.CODE` | `OcRegulator_DeptCode` | String |  |  |
| 24 | `OC.REG.AUDITOR.CODE` | `OcRegulator_AuditorCode` | String |  |  |
| 25 | `OC.REG.AUDIT.DATE.TIME` | `OcRegulator_AuditDateTime` | String |  |  |
