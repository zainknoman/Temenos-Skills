# CUSTOMER.BONUS.DETAILS — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.BONUS.DETAILS` in `USRETL_Bonus.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBD.BONUS.YTD` | `CustomerBonusDetails_BonusYtd` | TField |  | Bonus amount paid to the customer. |
| 2 | `CBD.BONUS.ACTIVITY` | `CustomerBonusDetails_BonusActivity` |  |  |  |
| 3 | `CBD.BONUS.AMOUNT` | `CustomerBonusDetails_BonusAmount` |  |  |  |
