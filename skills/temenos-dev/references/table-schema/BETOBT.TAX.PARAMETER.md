# BETOBT.TAX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BETOBT.TAX.PARAMETER` in `BETOBT_WithholdingTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BETOBT.TP.BEN.OWN.CHG.TRANS.CR` | `BetobtTaxParameter_BenOwnChgTransCr` | TField |  | Drop down from SC.TRANS.NAME; appropriate Security Cr Code will be defined. |
| 2 | `BETOBT.TP.BEN.OWN.CHG.TRANS.DR` | `BetobtTaxParameter_BenOwnChgTransDr` | TField |  | Drop down from SC.TRANS.NAME; appropriate Security Dr Code will be defined. |
| 3 | `BETOBT.TP.BROKER.ID` | `BetobtTaxParameter_BrokerId` |  |  |  |
| 4 | `BETOBT.TP.PRIMARY.MKT.TRANS.CODE.EVENT` | `BetobtTaxParameter_PrimaryMktTransCodeEvent` |  |  |  |
| 5 | `BETOBT.TP.PRIMARY.MKT.TRANS.CODE.TRADE` | `BetobtTaxParameter_PrimaryMktTransCodeTrade` |  |  |  |
| 6 | `BETOBT.TP.TOB.TAX.TYPE` | `BetobtTaxParameter_TobTaxType` | TField |  |  |
| 7 | `BETOBT.TP.RESERVED.9` | `BetobtTaxParameter_Reserved9` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 8 | `BETOBT.TP.RESERVED.8` | `BetobtTaxParameter_Reserved8` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 9 | `BETOBT.TP.RESERVED.7` | `BetobtTaxParameter_Reserved7` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 10 | `BETOBT.TP.RESERVED.6` | `BetobtTaxParameter_Reserved6` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 11 | `BETOBT.TP.RESERVED.5` | `BetobtTaxParameter_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 12 | `BETOBT.TP.RESERVED.4` | `BetobtTaxParameter_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 13 | `BETOBT.TP.RESERVED.3` | `BetobtTaxParameter_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 14 | `BETOBT.TP.RESERVED.2` | `BetobtTaxParameter_Reserved2` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 15 | `BETOBT.TP.RESERVED.1` | `BetobtTaxParameter_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 16 | `BETOBT.TP.LOCAL.REF` | `BetobtTaxParameter_LocalRef` |  |  |  |
| 17 | `BETOBT.TP.OVERRIDE` | `BetobtTaxParameter_Override` |  |  |  |
| 18 | `BETOBT.TP.RECORD.STATUS` | `BetobtTaxParameter_RecordStatus` | String |  |  |
| 19 | `BETOBT.TP.CURR.NO` | `BetobtTaxParameter_CurrNo` | String |  |  |
| 20 | `BETOBT.TP.INPUTTER` | `BetobtTaxParameter_Inputter` |  |  |  |
| 21 | `BETOBT.TP.DATE.TIME` | `BetobtTaxParameter_DateTime` |  |  |  |
| 22 | `BETOBT.TP.AUTHORISER` | `BetobtTaxParameter_Authoriser` | String |  |  |
| 23 | `BETOBT.TP.CO.CODE` | `BetobtTaxParameter_CoCode` | String |  |  |
| 24 | `BETOBT.TP.DEPT.CODE` | `BetobtTaxParameter_DeptCode` | String |  |  |
| 25 | `BETOBT.TP.AUDITOR.CODE` | `BetobtTaxParameter_AuditorCode` | String |  |  |
| 26 | `BETOBT.TP.AUDIT.DATE.TIME` | `BetobtTaxParameter_AuditDateTime` | String |  |  |
