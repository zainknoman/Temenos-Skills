# ESCROW.BLOCKED.FUNDS — Table Schema

> Source: `INSERTS/I_F.ESCROW.BLOCKED.FUNDS` in `ESCROW_PaymentProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.BF.PAYEE` | `EscrowBlockedFunds_Payee` |  |  |  |
| 2 | `ESCROW.BF.REFERENCE.NO` | `EscrowBlockedFunds_ReferenceNo` |  |  |  |
| 3 | `ESCROW.BF.FROM.DATE` | `EscrowBlockedFunds_FromDate` |  |  |  |
| 4 | `ESCROW.BF.AMOUNT` | `EscrowBlockedFunds_Amount` |  |  |  |
| 5 | `ESCROW.BF.TO.DATE` | `EscrowBlockedFunds_ToDate` |  |  |  |
| 6 | `ESCROW.BF.BILL.REF` | `EscrowBlockedFunds_BillRef` |  |  |  |
| 7 | `ESCROW.BF.BLOCK.TYPE` | `EscrowBlockedFunds_BlockType` |  |  |  |
| 8 | `ESCROW.BF.RESERVED.19` | `EscrowBlockedFunds_Reserved19` |  |  |  |
| 9 | `ESCROW.BF.RESERVED.18` | `EscrowBlockedFunds_Reserved18` |  |  |  |
| 10 | `ESCROW.BF.RESERVED.17` | `EscrowBlockedFunds_Reserved17` |  |  |  |
| 11 | `ESCROW.BF.RESERVED.16` | `EscrowBlockedFunds_Reserved16` |  |  |  |
| 12 | `ESCROW.BF.RESERVED.15` | `EscrowBlockedFunds_Reserved15` | TField |  |  |
| 13 | `ESCROW.BF.RESERVED.14` | `EscrowBlockedFunds_Reserved14` | TField |  |  |
| 14 | `ESCROW.BF.RESERVED.13` | `EscrowBlockedFunds_Reserved13` | TField |  |  |
| 15 | `ESCROW.BF.RESERVED.12` | `EscrowBlockedFunds_Reserved12` | TField |  |  |
| 16 | `ESCROW.BF.RESERVED.11` | `EscrowBlockedFunds_Reserved11` | TField |  |  |
| 17 | `ESCROW.BF.RESERVED.10` | `EscrowBlockedFunds_Reserved10` | TField |  |  |
| 18 | `ESCROW.BF.RESERVED.9` | `EscrowBlockedFunds_Reserved9` | TField |  |  |
| 19 | `ESCROW.BF.RESERVED.8` | `EscrowBlockedFunds_Reserved8` | TField |  |  |
| 20 | `ESCROW.BF.RESERVED.7` | `EscrowBlockedFunds_Reserved7` | TField |  |  |
| 21 | `ESCROW.BF.RESERVED.6` | `EscrowBlockedFunds_Reserved6` | TField |  |  |
| 22 | `ESCROW.BF.RESERVED.5` | `EscrowBlockedFunds_Reserved5` | TField |  |  |
| 23 | `ESCROW.BF.RESERVED.4` | `EscrowBlockedFunds_Reserved4` | TField |  |  |
| 24 | `ESCROW.BF.RESERVED.3` | `EscrowBlockedFunds_Reserved3` | TField |  |  |
| 25 | `ESCROW.BF.RESERVED.2` | `EscrowBlockedFunds_Reserved2` | TField |  |  |
| 26 | `ESCROW.BF.RESERVED.1` | `EscrowBlockedFunds_Reserved1` | TField |  |  |
