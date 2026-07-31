# ETFXOP.RETENTION.ACCOUNT.B.LIST — Table Schema

> Source: `INSERTS/I_F.ETFXOP.RETENTION.ACCOUNT.B.LIST` in `ETFXOP_RetentionAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.RTB.MAIN.ACCOUNT` | `EtfxopRetentionAccountBList_MainAccount` | TField |  | This Will contain the main account for which Retention Account is created |
| 2 | `ETFXOP.RTB.ARRANGEMENT.ID` | `EtfxopRetentionAccountBList_ArrangementId` | TField |  | This Will contain the Arrangement through which the main account is created |
| 3 | `ETFXOP.RTB.ETFXOP.RETENTION.TRANSFER.IDS` | `EtfxopRetentionAccountBList_EtfxopRetentionTransferIds` |  |  |  |
| 4 | `ETFXOP.RTB.LOCAL.REF` | `EtfxopRetentionAccountBList_LocalRef` |  |  |  |
