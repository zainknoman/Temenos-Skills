# SY.TXN.LINK — Table Schema

> Source: `INSERTS/I_F.SY.TXN.LINK` in `SY_Trading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.TL.USER.APPLICATION` | `SyTxnLink_UserApplication` | TField |  | The application into which the user has placed a transaction. |
| 2 | `SY.TL.USER.APP.ID` | `SyTxnLink_UserAppId` | TField |  | The ID of the transaction has placed in the satellite application. |
| 3 | `SY.TL.SY.TXN.ID` | `SyTxnLink_SyTxnId` | TField |  | The SY.TRANSACTION ID of the transaction the user has placed. |
| 4 | `SY.TL.RESERVED.10` | `SyTxnLink_Reserved10` | TField |  |  |
| 5 | `SY.TL.RESERVED.9` | `SyTxnLink_Reserved9` | TField |  |  |
| 6 | `SY.TL.RESERVED.8` | `SyTxnLink_Reserved8` | TField |  |  |
| 7 | `SY.TL.RESERVED.7` | `SyTxnLink_Reserved7` | TField |  |  |
| 8 | `SY.TL.RESERVED.6` | `SyTxnLink_Reserved6` | TField |  |  |
| 9 | `SY.TL.RESERVED.5` | `SyTxnLink_Reserved5` | TField |  |  |
| 10 | `SY.TL.RESERVED.4` | `SyTxnLink_Reserved4` | TField |  |  |
| 11 | `SY.TL.RESERVED.3` | `SyTxnLink_Reserved3` | TField |  |  |
| 12 | `SY.TL.RESERVED.2` | `SyTxnLink_Reserved2` | TField |  |  |
| 13 | `SY.TL.RESERVED.1` | `SyTxnLink_Reserved1` | TField |  |  |
| 14 | `SY.TL.LOCAL.REF` | `SyTxnLink_LocalRef` |  |  |  |
| 15 | `SY.TL.OVERRIDE` | `SyTxnLink_Override` |  |  |  |
