# CUSTOMER.TAX.DETS — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.TAX.DETS` in `CATCIB_TCIBOnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.TAX.FORM.TYPE` | `CustomerTaxDets_FormType` |  |  |  |
| 2 | `CUS.TAX.TAX.KEYS` | `CustomerTaxDets_TaxKeys` |  |  |  |
| 3 | `CUS.TAX.RESERVED.1` | `CustomerTaxDets_Reserved1` | TField |  |  |
| 4 | `CUS.TAX.RESERVED.2` | `CustomerTaxDets_Reserved2` | TField |  |  |
| 5 | `CUS.TAX.RESERVED.3` | `CustomerTaxDets_Reserved3` | TField |  |  |
| 6 | `CUS.TAX.RESERVED.4` | `CustomerTaxDets_Reserved4` | TField |  |  |
| 7 | `CUS.TAX.RESERVED.5` | `CustomerTaxDets_Reserved5` | TField |  |  |
| 8 | `CUS.TAX.RESERVED.6` | `CustomerTaxDets_Reserved6` | TField |  |  |
| 9 | `CUS.TAX.RESERVED.7` | `CustomerTaxDets_Reserved7` | TField |  |  |
| 10 | `CUS.TAX.RESERVED.8` | `CustomerTaxDets_Reserved8` | TField |  |  |
| 11 | `CUS.TAX.RESERVED.9` | `CustomerTaxDets_Reserved9` | TField |  |  |
| 12 | `CUS.TAX.RESERVED.10` | `CustomerTaxDets_Reserved10` | TField |  |  |
| 13 | `CUS.TAX.OVERRIDE` | `CustomerTaxDets_Override` |  |  |  |
| 14 | `CUS.TAX.RECORD.STATUS` | `CustomerTaxDets_RecordStatus` | String |  |  |
| 15 | `CUS.TAX.CURR.NO` | `CustomerTaxDets_CurrNo` | String |  |  |
| 16 | `CUS.TAX.INPUTTER` | `CustomerTaxDets_Inputter` |  |  |  |
| 17 | `CUS.TAX.DATE.TIME` | `CustomerTaxDets_DateTime` |  |  |  |
| 18 | `CUS.TAX.AUTHORISER` | `CustomerTaxDets_Authoriser` | String |  |  |
| 19 | `CUS.TAX.CO.CODE` | `CustomerTaxDets_CoCode` | String |  |  |
| 20 | `CUS.TAX.DEPT.CODE` | `CustomerTaxDets_DeptCode` | String |  |  |
| 21 | `CUS.TAX.AUDITOR.CODE` | `CustomerTaxDets_AuditorCode` | String |  |  |
| 22 | `CUS.TAX.AUDIT.DATE.TIME` | `CustomerTaxDets_AuditDateTime` | String |  |  |
