# ETFXOP.RETENTION.TRANSFER — Table Schema

> Source: `INSERTS/I_F.ETFXOP.RETENTION.TRANSFER` in `ETFXOP_RetentionAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.RT.TXN.REFERENCE` | `EtfxopRetentionTransfer_TxnReference` |  |  |  |
| 2 | `ETFXOP.RT.RETENTION.BALANCE` | `EtfxopRetentionTransfer_RetentionBalance` | TField |  | This will be the amount left in this account for redemption |
| 3 | `ETFXOP.RT.LOCAL.REF` | `EtfxopRetentionTransfer_LocalRef` |  |  |  |
