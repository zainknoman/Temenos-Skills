# REGION.TAXES — Table Schema

> Source: `INSERTS/I_F.REGION.TAXES` in `CALEND_Taxes.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REG.TAX.TAX.CODE` | `RegionTaxes_TaxCode` | TField |  | Represents a reference on the TAX table which will indicate the rate to be used for computation of taxation for the associated Prvince and Charge Property. |
| 2 | `REG.TAX.RESERVED.15` | `RegionTaxes_Reserved15` | TField |  |  |
| 3 | `REG.TAX.RESERVED.14` | `RegionTaxes_Reserved14` | TField |  |  |
| 4 | `REG.TAX.RESERVED.13` | `RegionTaxes_Reserved13` | TField |  |  |
| 5 | `REG.TAX.RESERVED.12` | `RegionTaxes_Reserved12` | TField |  |  |
| 6 | `REG.TAX.RESERVED.11` | `RegionTaxes_Reserved11` | TField |  |  |
| 7 | `REG.TAX.RESERVED.10` | `RegionTaxes_Reserved10` | TField |  |  |
| 8 | `REG.TAX.RESERVED.9` | `RegionTaxes_Reserved9` | TField |  |  |
| 9 | `REG.TAX.RESERVED.8` | `RegionTaxes_Reserved8` | TField |  |  |
| 10 | `REG.TAX.RESERVED.7` | `RegionTaxes_Reserved7` | TField |  |  |
| 11 | `REG.TAX.RESERVED.6` | `RegionTaxes_Reserved6` | TField |  |  |
| 12 | `REG.TAX.RESERVED.5` | `RegionTaxes_Reserved5` | TField |  |  |
| 13 | `REG.TAX.RESERVED.4` | `RegionTaxes_Reserved4` | TField |  |  |
| 14 | `REG.TAX.RESERVED.3` | `RegionTaxes_Reserved3` | TField |  |  |
| 15 | `REG.TAX.RESERVED.2` | `RegionTaxes_Reserved2` | TField |  |  |
| 16 | `REG.TAX.RESERVED.1` | `RegionTaxes_Reserved1` | TField |  |  |
| 17 | `REG.TAX.RECORD.STATUS` | `RegionTaxes_RecordStatus` | String |  |  |
| 18 | `REG.TAX.CURR.NO` | `RegionTaxes_CurrNo` | String |  |  |
| 19 | `REG.TAX.INPUTTER` | `RegionTaxes_Inputter` |  |  |  |
| 20 | `REG.TAX.DATE.TIME` | `RegionTaxes_DateTime` |  |  |  |
| 21 | `REG.TAX.AUTHORISER` | `RegionTaxes_Authoriser` | String |  |  |
| 22 | `REG.TAX.CO.CODE` | `RegionTaxes_CoCode` | String |  |  |
| 23 | `REG.TAX.DEPT.CODE` | `RegionTaxes_DeptCode` | String |  |  |
| 24 | `REG.TAX.AUDITOR.CODE` | `RegionTaxes_AuditorCode` | String |  |  |
| 25 | `REG.TAX.AUDIT.DATE.TIME` | `RegionTaxes_AuditDateTime` | String |  |  |
