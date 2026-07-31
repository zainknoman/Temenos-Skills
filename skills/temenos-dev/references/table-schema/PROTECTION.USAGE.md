# PROTECTION.USAGE — Table Schema

> Source: `INSERTS/I_F.PROTECTION.USAGE` in `AC_SoftAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.PRCTU.DATE.TIME.UPD` | `ProtectionUsage_DateTimeUpd` | TField |  | Last time the record was updated. |
| 2 | `AC.PRCTU.PROTECTION.RULE` | `ProtectionUsage_ProtectionRule` |  |  |  |
| 3 | `AC.PRCTU.AMOUNT` | `ProtectionUsage_Amount` |  |  |  |
| 4 | `AC.PRCTU.UTILISED` | `ProtectionUsage_Utilised` |  |  |  |
| 5 | `AC.PRCTU.CUSTOMER.NO` | `ProtectionUsage_CustomerNo` |  |  |  |
| 6 | `AC.PRCTU.CUSTOMER.LIM.AMT` | `ProtectionUsage_CustomerLimAmt` |  |  |  |
| 7 | `AC.PRCTU.CUSTOMER.UTILISED` | `ProtectionUsage_CustomerUtilised` |  |  |  |
| 8 | `AC.PRCTU.TRANS.REFERENCE` | `ProtectionUsage_TransReference` |  |  |  |
| 9 | `AC.PRCTU.RESERVED.6` | `ProtectionUsage_Reserved6` | TField |  |  |
| 10 | `AC.PRCTU.RESERVED.5` | `ProtectionUsage_Reserved5` | TField |  |  |
| 11 | `AC.PRCTU.RESERVED.4` | `ProtectionUsage_Reserved4` | TField |  |  |
| 12 | `AC.PRCTU.RESERVED.3` | `ProtectionUsage_Reserved3` | TField |  |  |
| 13 | `AC.PRCTU.RESERVED.2` | `ProtectionUsage_Reserved2` | TField |  |  |
| 14 | `AC.PRCTU.RESERVED.1` | `ProtectionUsage_Reserved1` | TField |  |  |
