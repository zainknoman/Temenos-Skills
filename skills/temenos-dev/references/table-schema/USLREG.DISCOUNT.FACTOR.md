# USLREG.DISCOUNT.FACTOR — Table Schema

> Source: `INSERTS/I_F.USLREG.DISCOUNT.FACTOR` in `USLREG_RebatableInsurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DISC.FAC.DISCOUNT.FACTOR` | `UslregDiscountFactor_DiscountFactor` | TField |  |  |
| 2 | `DISC.FAC.RESERVED.10` | `UslregDiscountFactor_Reserved10` | TField |  |  |
| 3 | `DISC.FAC.RESERVED.9` | `UslregDiscountFactor_Reserved9` | TField |  |  |
| 4 | `DISC.FAC.RESERVED.8` | `UslregDiscountFactor_Reserved8` | TField |  |  |
| 5 | `DISC.FAC.RESERVED.7` | `UslregDiscountFactor_Reserved7` | TField |  |  |
| 6 | `DISC.FAC.RESERVED.6` | `UslregDiscountFactor_Reserved6` | TField |  |  |
| 7 | `DISC.FAC.RESERVED.5` | `UslregDiscountFactor_Reserved5` | TField |  |  |
| 8 | `DISC.FAC.RESERVED.4` | `UslregDiscountFactor_Reserved4` | TField |  |  |
| 9 | `DISC.FAC.RESERVED.3` | `UslregDiscountFactor_Reserved3` | TField |  |  |
| 10 | `DISC.FAC.RESERVED.2` | `UslregDiscountFactor_Reserved2` | TField |  |  |
| 11 | `DISC.FAC.RESERVED.1` | `UslregDiscountFactor_Reserved1` | TField |  |  |
| 12 | `DISC.FAC.RECORD.STATUS` | `UslregDiscountFactor_RecordStatus` | String |  |  |
| 13 | `DISC.FAC.CURR.NO` | `UslregDiscountFactor_CurrNo` | String |  |  |
| 14 | `DISC.FAC.INPUTTER` | `UslregDiscountFactor_Inputter` |  |  |  |
| 15 | `DISC.FAC.DATE.TIME` | `UslregDiscountFactor_DateTime` |  |  |  |
| 16 | `DISC.FAC.AUTHORISER` | `UslregDiscountFactor_Authoriser` | String |  |  |
| 17 | `DISC.FAC.CO.CODE` | `UslregDiscountFactor_CoCode` | String |  |  |
| 18 | `DISC.FAC.DEPT.CODE` | `UslregDiscountFactor_DeptCode` | String |  |  |
| 19 | `DISC.FAC.AUDITOR.CODE` | `UslregDiscountFactor_AuditorCode` | String |  |  |
| 20 | `DISC.FAC.AUDIT.DATE.TIME` | `UslregDiscountFactor_AuditDateTime` | String |  |  |
