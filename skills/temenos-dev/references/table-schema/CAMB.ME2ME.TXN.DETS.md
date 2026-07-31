# CAMB.ME2ME.TXN.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.ME2ME.TXN.DETS` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ME2ME.DETS.DEBIT.ACCT` | `CambMe2meTxnDets_DebitAcct` |  |  |  |
| 2 | `ME2ME.DETS.CREDIT.ACCT` | `CambMe2meTxnDets_CreditAcct` |  |  |  |
| 3 | `ME2ME.DETS.DEBIT.CURRENCY` | `CambMe2meTxnDets_DebitCurrency` |  |  |  |
| 4 | `ME2ME.DETS.CREDIT.CURRENCY` | `CambMe2meTxnDets_CreditCurrency` |  |  |  |
| 5 | `ME2ME.DETS.TXN.AMOUNT` | `CambMe2meTxnDets_TxnAmount` |  |  |  |
| 6 | `ME2ME.DETS.FT.REFERENCE` | `CambMe2meTxnDets_FtReference` |  |  |  |
| 7 | `ME2ME.DETS.STATUS` | `CambMe2meTxnDets_Status` |  |  |  |
| 8 | `ME2ME.DETS.EFT.TXN` | `CambMe2meTxnDets_EftTxn` |  |  |  |
| 9 | `ME2ME.DETS.RESERVED.1` | `CambMe2meTxnDets_Reserved1` |  |  |  |
| 10 | `ME2ME.DETS.RESERVED.2` | `CambMe2meTxnDets_Reserved2` |  |  |  |
| 11 | `ME2ME.DETS.RESERVED.3` | `CambMe2meTxnDets_Reserved3` |  |  |  |
| 12 | `ME2ME.DETS.RESERVED.4` | `CambMe2meTxnDets_Reserved4` |  |  |  |
| 13 | `ME2ME.DETS.RESERVED.5` | `CambMe2meTxnDets_Reserved5` |  |  |  |
| 14 | `ME2ME.DETS.RESERVED.6` | `CambMe2meTxnDets_Reserved6` |  |  |  |
| 15 | `ME2ME.DETS.RESERVED.7` | `CambMe2meTxnDets_Reserved7` |  |  |  |
| 16 | `ME2ME.DETS.RESERVED.8` | `CambMe2meTxnDets_Reserved8` |  |  |  |
| 17 | `ME2ME.DETS.RESERVED.9` | `CambMe2meTxnDets_Reserved9` |  |  |  |
| 18 | `ME2ME.DETS.OVERRIDE` | `CambMe2meTxnDets_Override` |  |  |  |
