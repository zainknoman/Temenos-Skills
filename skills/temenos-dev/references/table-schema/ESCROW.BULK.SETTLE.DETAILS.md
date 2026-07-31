# ESCROW.BULK.SETTLE.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESCROW.BULK.SETTLE.DETAILS` in `ESCROW_PaymentProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.BSD.AMOUNT` | `EscrowBulkSettleDetails_Amount` | TField |  |  |
| 2 | `ESCROW.BSD.ORDER.ID` | `EscrowBulkSettleDetails_OrderId` | TField |  |  |
| 3 | `ESCROW.BSD.RESERVED.5` | `EscrowBulkSettleDetails_Reserved5` | TField |  |  |
| 4 | `ESCROW.BSD.RESERVED.4` | `EscrowBulkSettleDetails_Reserved4` | TField |  |  |
| 5 | `ESCROW.BSD.RESERVED.3` | `EscrowBulkSettleDetails_Reserved3` | TField |  |  |
| 6 | `ESCROW.BSD.RESERVED.2` | `EscrowBulkSettleDetails_Reserved2` | TField |  |  |
| 7 | `ESCROW.BSD.RESERVED.1` | `EscrowBulkSettleDetails_Reserved1` | TField |  |  |
