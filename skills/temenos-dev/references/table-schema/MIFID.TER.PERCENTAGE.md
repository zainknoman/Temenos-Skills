# MIFID.TER.PERCENTAGE — Table Schema

> Source: `INSERTS/I_F.MIFID.TER.PERCENTAGE` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.TER.TER.PCT` | `MifidTerPercentage_TerPct` | TField |  | Field to capture TER percentage. |
| 2 | `MIFID.TER.LOCAL.REF` | `MifidTerPercentage_LocalRef` |  |  |  |
| 3 | `MIFID.TER.RESERVED.10` | `MifidTerPercentage_Reserved10` | TField |  |  |
| 4 | `MIFID.TER.RESERVED.9` | `MifidTerPercentage_Reserved9` | TField |  |  |
| 5 | `MIFID.TER.RESERVED.8` | `MifidTerPercentage_Reserved8` | TField |  |  |
| 6 | `MIFID.TER.RESERVED.7` | `MifidTerPercentage_Reserved7` | TField |  |  |
| 7 | `MIFID.TER.RESERVED.6` | `MifidTerPercentage_Reserved6` | TField |  |  |
| 8 | `MIFID.TER.RESERVED.5` | `MifidTerPercentage_Reserved5` | TField |  |  |
| 9 | `MIFID.TER.RESERVED.4` | `MifidTerPercentage_Reserved4` | TField |  |  |
| 10 | `MIFID.TER.RESERVED.3` | `MifidTerPercentage_Reserved3` | TField |  |  |
| 11 | `MIFID.TER.RESERVED.2` | `MifidTerPercentage_Reserved2` | TField |  |  |
| 12 | `MIFID.TER.RESERVED.1` | `MifidTerPercentage_Reserved1` | TField |  |  |
| 13 | `MIFID.TER.OVERRIDE` | `MifidTerPercentage_Override` |  |  |  |
| 14 | `MIFID.TER.RECORD.STATUS` | `MifidTerPercentage_RecordStatus` | String |  |  |
| 15 | `MIFID.TER.CURR.NO` | `MifidTerPercentage_CurrNo` | String |  |  |
| 16 | `MIFID.TER.INPUTTER` | `MifidTerPercentage_Inputter` |  |  |  |
| 17 | `MIFID.TER.DATE.TIME` | `MifidTerPercentage_DateTime` |  |  |  |
| 18 | `MIFID.TER.AUTHORISER` | `MifidTerPercentage_Authoriser` | String |  |  |
| 19 | `MIFID.TER.CO.CODE` | `MifidTerPercentage_CoCode` | String |  |  |
| 20 | `MIFID.TER.DEPT.CODE` | `MifidTerPercentage_DeptCode` | String |  |  |
| 21 | `MIFID.TER.AUDITOR.CODE` | `MifidTerPercentage_AuditorCode` | String |  |  |
| 22 | `MIFID.TER.AUDIT.DATE.TIME` | `MifidTerPercentage_AuditDateTime` | String |  |  |
