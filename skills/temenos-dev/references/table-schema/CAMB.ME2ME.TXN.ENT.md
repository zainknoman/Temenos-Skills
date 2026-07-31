# CAMB.ME2ME.TXN.ENT — Table Schema

> Source: `INSERTS/I_F.CAMB.ME2ME.TXN.ENT` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ME2ME.ENT.DATE.TIME` | `CambMe2meTxnEnt_DateTime` |  |  |  |
| 2 | `ME2ME.ENT.DEBIT.AMOUNT` | `CambMe2meTxnEnt_DebitAmount` |  |  |  |
| 3 | `ME2ME.ENT.CREDIT.AMOUNT` | `CambMe2meTxnEnt_CreditAmount` |  |  |  |
| 4 | `ME2ME.ENT.RESERVED.1` | `CambMe2meTxnEnt_Reserved1` |  |  |  |
| 5 | `ME2ME.ENT.RESERVED.2` | `CambMe2meTxnEnt_Reserved2` |  |  |  |
| 6 | `ME2ME.ENT.RESERVED.3` | `CambMe2meTxnEnt_Reserved3` |  |  |  |
| 7 | `ME2ME.ENT.RESERVED.4` | `CambMe2meTxnEnt_Reserved4` |  |  |  |
| 8 | `ME2ME.ENT.RESERVED.5` | `CambMe2meTxnEnt_Reserved5` |  |  |  |
| 9 | `ME2ME.ENT.RESERVED.6` | `CambMe2meTxnEnt_Reserved6` |  |  |  |
| 10 | `ME2ME.ENT.RESERVED.7` | `CambMe2meTxnEnt_Reserved7` |  |  |  |
| 11 | `ME2ME.ENT.RESERVED.8` | `CambMe2meTxnEnt_Reserved8` |  |  |  |
| 12 | `ME2ME.ENT.RESERVED.9` | `CambMe2meTxnEnt_Reserved9` |  |  |  |
| 13 | `ME2ME.ENT.OVERRIDE` | `CambMe2meTxnEnt_Override` |  |  |  |
