# AUWHTX.TAX.CLASS — Table Schema

> Source: `INSERTS/I_F.AUWHTX.TAX.CLASS` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.CLASS.DESCRIPTION` | `AuwhtxTaxClass_Description` | TField |  | Description associated with the tax class. Ex : Fully Paid Ordinary, Fixed Interest, Preferred Shares etc. |
| 2 | `TAX.CLASS.45.DAY.RULE.FLAG` | `AuwhtxTaxClass_45DayRuleFlag` |  |  |  |
| 3 | `TAX.CLASS.TAX.INCOME.BASIS` | `AuwhtxTaxClass_TaxIncomeBasis` | TField |  | This indicates the Income basis associated with the Tax class. |
| 4 | `TAX.CLASS.CGT.BASIS` | `AuwhtxTaxClass_CgtBasis` | TField |  | This indicates the CGT basis associated with the Tax class. |
| 5 | `TAX.CLASS.INSTRUMENT.LISTING.TYPE` | `AuwhtxTaxClass_InstrumentListingType` | TField |  | The listing type of the instrument as to whether it is a domestic, International or Dual Listed security. |
| 6 | `TAX.CLASS.LOCAL.REF` | `AuwhtxTaxClass_LocalRef` |  |  |  |
| 7 | `TAX.CLASS.RESERVED.1` | `AuwhtxTaxClass_Reserved1` | TField |  |  |
| 8 | `TAX.CLASS.RESERVED.2` | `AuwhtxTaxClass_Reserved2` | TField |  |  |
| 9 | `TAX.CLASS.RESERVED.3` | `AuwhtxTaxClass_Reserved3` | TField |  |  |
| 10 | `TAX.CLASS.RESERVED.4` | `AuwhtxTaxClass_Reserved4` | TField |  |  |
| 11 | `TAX.CLASS.RESERVED.5` | `AuwhtxTaxClass_Reserved5` | TField |  |  |
| 12 | `TAX.CLASS.RESERVED.6` | `AuwhtxTaxClass_Reserved6` | TField |  |  |
| 13 | `TAX.CLASS.RESERVED.7` | `AuwhtxTaxClass_Reserved7` | TField |  |  |
| 14 | `TAX.CLASS.RESERVED.8` | `AuwhtxTaxClass_Reserved8` | TField |  |  |
| 15 | `TAX.CLASS.RESERVED.9` | `AuwhtxTaxClass_Reserved9` | TField |  |  |
| 16 | `TAX.CLASS.RESERVED.10` | `AuwhtxTaxClass_Reserved10` | TField |  |  |
| 17 | `TAX.CLASS.OVERRIDE` | `AuwhtxTaxClass_Override` |  |  |  |
| 18 | `TAX.CLASS.RECORD.STATUS` | `AuwhtxTaxClass_RecordStatus` | String |  |  |
| 19 | `TAX.CLASS.CURR.NO` | `AuwhtxTaxClass_CurrNo` | String |  |  |
| 20 | `TAX.CLASS.INPUTTER` | `AuwhtxTaxClass_Inputter` |  |  |  |
| 21 | `TAX.CLASS.DATE.TIME` | `AuwhtxTaxClass_DateTime` |  |  |  |
| 22 | `TAX.CLASS.AUTHORISER` | `AuwhtxTaxClass_Authoriser` | String |  |  |
| 23 | `TAX.CLASS.CO.CODE` | `AuwhtxTaxClass_CoCode` | String |  |  |
| 24 | `TAX.CLASS.DEPT.CODE` | `AuwhtxTaxClass_DeptCode` | String |  |  |
| 25 | `TAX.CLASS.AUDITOR.CODE` | `AuwhtxTaxClass_AuditorCode` | String |  |  |
| 26 | `TAX.CLASS.AUDIT.DATE.TIME` | `AuwhtxTaxClass_AuditDateTime` | String |  |  |
