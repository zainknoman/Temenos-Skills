# BETOBT.TAX.CONFIG — Table Schema

> Source: `INSERTS/I_F.BETOBT.TAX.CONFIG` in `BETOBT_WithholdingTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BETOBT.TC.DESCRIPTION` | `BetobtTaxConfig_Description` | TField |  | Valid Description |
| 2 | `BETOBT.TC.CONTRACT.GROUP` | `BetobtTaxConfig_ContractGroup` |  |  |  |
| 3 | `BETOBT.TC.MAIN.APPLICATION.FIELD` | `BetobtTaxConfig_MainApplicationField` |  |  |  |
| 4 | `BETOBT.TC.SUB.APPLICATION` | `BetobtTaxConfig_SubApplication` |  |  |  |
| 5 | `BETOBT.TC.SUB.APPLICATION.FIELD` | `BetobtTaxConfig_SubApplicationField` |  |  |  |
| 6 | `BETOBT.TC.SUB.FIELD.OPERAND` | `BetobtTaxConfig_SubFieldOperand` |  |  |  |
| 7 | `BETOBT.TC.SUB.FIELD.FROM` | `BetobtTaxConfig_SubFieldFrom` |  |  |  |
| 8 | `BETOBT.TC.SUB.FIELD.TO` | `BetobtTaxConfig_SubFieldTo` |  |  |  |
| 9 | `BETOBT.TC.RESERVED.10` | `BetobtTaxConfig_Reserved10` |  |  |  |
| 10 | `BETOBT.TC.RESERVED.9` | `BetobtTaxConfig_Reserved9` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 11 | `BETOBT.TC.RESERVED.8` | `BetobtTaxConfig_Reserved8` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 12 | `BETOBT.TC.RESERVED.7` | `BetobtTaxConfig_Reserved7` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 13 | `BETOBT.TC.RESERVED.6` | `BetobtTaxConfig_Reserved6` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 14 | `BETOBT.TC.RESERVED.5` | `BetobtTaxConfig_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 15 | `BETOBT.TC.RESERVED.4` | `BetobtTaxConfig_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 16 | `BETOBT.TC.RESERVED.3` | `BetobtTaxConfig_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 17 | `BETOBT.TC.RESERVED.2` | `BetobtTaxConfig_Reserved2` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 18 | `BETOBT.TC.RESERVED.1` | `BetobtTaxConfig_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 19 | `BETOBT.TC.LOCAL.REF` | `BetobtTaxConfig_LocalRef` |  |  |  |
| 20 | `BETOBT.TC.OVERRIDE` | `BetobtTaxConfig_Override` |  |  |  |
| 21 | `BETOBT.TC.RECORD.STATUS` | `BetobtTaxConfig_RecordStatus` | String |  |  |
| 22 | `BETOBT.TC.CURR.NO` | `BetobtTaxConfig_CurrNo` | String |  |  |
| 23 | `BETOBT.TC.INPUTTER` | `BetobtTaxConfig_Inputter` |  |  |  |
| 24 | `BETOBT.TC.DATE.TIME` | `BetobtTaxConfig_DateTime` |  |  |  |
| 25 | `BETOBT.TC.AUTHORISER` | `BetobtTaxConfig_Authoriser` | String |  |  |
| 26 | `BETOBT.TC.CO.CODE` | `BetobtTaxConfig_CoCode` | String |  |  |
| 27 | `BETOBT.TC.DEPT.CODE` | `BetobtTaxConfig_DeptCode` | String |  |  |
| 28 | `BETOBT.TC.AUDITOR.CODE` | `BetobtTaxConfig_AuditorCode` | String |  |  |
| 29 | `BETOBT.TC.AUDIT.DATE.TIME` | `BetobtTaxConfig_AuditDateTime` | String |  |  |
