# MIFID.CHARGES — Table Schema

> Source: `INSERTS/I_F.MIFID.CHARGES` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.CHG.STMT.ENTRY` | `MifidCharges_StmtEntry` |  |  |  |
| 2 | `MIFID.CHG.CURRENCY.CODE` | `MifidCharges_CurrencyCode` |  |  |  |
| 3 | `MIFID.CHG.CHARGE.VALUE` | `MifidCharges_ChargeValue` |  |  |  |
| 4 | `MIFID.CHG.CHARGE.DATE` | `MifidCharges_ChargeDate` |  |  |  |
| 5 | `MIFID.CHG.NARRATIVE.EXT.CHG` | `MifidCharges_NarrativeExtChg` |  |  |  |
| 6 | `MIFID.CHG.EXT.CURRENCY.CODE` | `MifidCharges_ExtCurrencyCode` |  |  |  |
| 7 | `MIFID.CHG.EXT.CHARGE.VALUE` | `MifidCharges_ExtChargeValue` |  |  |  |
| 8 | `MIFID.CHG.EXT.CHARGE.DATE` | `MifidCharges_ExtChargeDate` |  |  |  |
| 9 | `MIFID.CHG.LOCAL.REF` | `MifidCharges_LocalRef` |  |  |  |
| 10 | `MIFID.CHG.RESERVED.10` | `MifidCharges_Reserved10` | TField |  |  |
| 11 | `MIFID.CHG.RESERVED.9` | `MifidCharges_Reserved9` | TField |  |  |
| 12 | `MIFID.CHG.RESERVED.8` | `MifidCharges_Reserved8` | TField |  |  |
| 13 | `MIFID.CHG.RESERVED.7` | `MifidCharges_Reserved7` | TField |  |  |
| 14 | `MIFID.CHG.RESERVED.6` | `MifidCharges_Reserved6` | TField |  |  |
| 15 | `MIFID.CHG.RESERVED.5` | `MifidCharges_Reserved5` | TField |  |  |
| 16 | `MIFID.CHG.RESERVED.4` | `MifidCharges_Reserved4` | TField |  |  |
| 17 | `MIFID.CHG.RESERVED.3` | `MifidCharges_Reserved3` | TField |  |  |
| 18 | `MIFID.CHG.RESERVED.2` | `MifidCharges_Reserved2` | TField |  |  |
| 19 | `MIFID.CHG.RESERVED.1` | `MifidCharges_Reserved1` | TField |  |  |
| 20 | `MIFID.CHG.OVERRIDE` | `MifidCharges_Override` |  |  |  |
| 21 | `MIFID.CHG.RECORD.STATUS` | `MifidCharges_RecordStatus` | String |  |  |
| 22 | `MIFID.CHG.CURR.NO` | `MifidCharges_CurrNo` | String |  |  |
| 23 | `MIFID.CHG.INPUTTER` | `MifidCharges_Inputter` |  |  |  |
| 24 | `MIFID.CHG.DATE.TIME` | `MifidCharges_DateTime` |  |  |  |
| 25 | `MIFID.CHG.AUTHORISER` | `MifidCharges_Authoriser` | String |  |  |
| 26 | `MIFID.CHG.CO.CODE` | `MifidCharges_CoCode` | String |  |  |
| 27 | `MIFID.CHG.DEPT.CODE` | `MifidCharges_DeptCode` | String |  |  |
| 28 | `MIFID.CHG.AUDITOR.CODE` | `MifidCharges_AuditorCode` | String |  |  |
| 29 | `MIFID.CHG.AUDIT.DATE.TIME` | `MifidCharges_AuditDateTime` | String |  |  |
