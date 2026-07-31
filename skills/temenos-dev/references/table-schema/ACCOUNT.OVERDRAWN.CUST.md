# ACCOUNT.OVERDRAWN.CUST — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.OVERDRAWN.CUST` in `AC_BalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AOC.ACCOUNT.OVERDRAWN.ID` | `AccountOverdrawnCust_AccountOverdrawnId` | TField |  | This field holds ACCOUNT.OVERDRAWN's ID. This can be combination of ACCOUNT.OVERDRAWN id's of limit &amp; accounts. |
