# ETFXOP.ACCOUNT.LIST — Table Schema

> Source: `INSERTS/I_F.ETFXOP.ACCOUNT.LIST` in `ETFXOP_RetentionAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.AL.RETENTION.ACCOUNT.A` | `EtfxopAccountList_RetentionAccountA` | TField |  | This Will contain Retention A/c A |
| 2 | `ETFXOP.AL.RETENTION.ACCOUNT.B` | `EtfxopAccountList_RetentionAccountB` | TField |  | This Will contain Retention A/c B |
| 3 | `ETFXOP.AL.LOCAL.REF` | `EtfxopAccountList_LocalRef` |  |  |  |
