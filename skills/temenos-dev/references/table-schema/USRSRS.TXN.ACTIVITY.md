# USRSRS.TXN.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.USRSRS.TXN.ACTIVITY` in `USRSRS_RetailSweepPgm.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXN.ACT.PRIMARY.ACCOUNT` | `UsrsrsTxnActivity_PrimaryAccount` | TField |  |  |
| 2 | `TXN.ACT.BOOKING.DATE` | `UsrsrsTxnActivity_BookingDate` |  |  |  |
| 3 | `TXN.ACT.TXN.AMOUNT` | `UsrsrsTxnActivity_TxnAmount` |  |  |  |
| 4 | `TXN.ACT.BALANCE` | `UsrsrsTxnActivity_Balance` |  |  |  |
| 5 | `TXN.ACT.REFERENCE.ID` | `UsrsrsTxnActivity_ReferenceId` |  |  |  |
| 6 | `TXN.ACT.TXN.DESCRIPTION` | `UsrsrsTxnActivity_TxnDescription` |  |  |  |
| 7 | `TXN.ACT.RESERVED.15` | `UsrsrsTxnActivity_Reserved15` | TField |  |  |
| 8 | `TXN.ACT.RESERVED.14` | `UsrsrsTxnActivity_Reserved14` | TField |  |  |
| 9 | `TXN.ACT.RESERVED.13` | `UsrsrsTxnActivity_Reserved13` | TField |  |  |
| 10 | `TXN.ACT.RESERVED.12` | `UsrsrsTxnActivity_Reserved12` | TField |  |  |
| 11 | `TXN.ACT.RESERVED.11` | `UsrsrsTxnActivity_Reserved11` | TField |  |  |
| 12 | `TXN.ACT.RESERVED.10` | `UsrsrsTxnActivity_Reserved10` | TField |  |  |
| 13 | `TXN.ACT.RESERVED.9` | `UsrsrsTxnActivity_Reserved9` | TField |  |  |
| 14 | `TXN.ACT.RESERVED.8` | `UsrsrsTxnActivity_Reserved8` | TField |  |  |
| 15 | `TXN.ACT.RESERVED.7` | `UsrsrsTxnActivity_Reserved7` | TField |  |  |
| 16 | `TXN.ACT.RESERVED.6` | `UsrsrsTxnActivity_Reserved6` | TField |  |  |
| 17 | `TXN.ACT.RESERVED.5` | `UsrsrsTxnActivity_Reserved5` | TField |  |  |
| 18 | `TXN.ACT.RESERVED.4` | `UsrsrsTxnActivity_Reserved4` | TField |  |  |
| 19 | `TXN.ACT.RESERVED.3` | `UsrsrsTxnActivity_Reserved3` | TField |  |  |
| 20 | `TXN.ACT.RESERVED.2` | `UsrsrsTxnActivity_Reserved2` | TField |  |  |
| 21 | `TXN.ACT.RESERVED.1` | `UsrsrsTxnActivity_Reserved1` | TField |  |  |
| 22 | `TXN.ACT.LOCAL.REF` | `UsrsrsTxnActivity_LocalRef` |  |  |  |
