# ESCROW.PAYEE.BILL — Table Schema

> Source: `INSERTS/I_F.ESCROW.PAYEE.BILL` in `ESCROW_PaymentProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.PB.ESCROW.ACCOUNT.ID` | `EscrowPayeeBill_EscrowAccountId` | TField |  | Escrow Account Number. No-input field |
| 2 | `ESCROW.PB.PAYEE.ID` | `EscrowPayeeBill_PayeeId` | TField |  | The payee for whom the payment has to be remitted No-input field |
| 3 | `ESCROW.PB.PAYEE.REF.NO` | `EscrowPayeeBill_PayeeRefNo` | TField |  | The reference related to the tax payment. No-input field |
| 4 | `ESCROW.PB.CURRENCY` | `EscrowPayeeBill_Currency` | TField |  | Currency of escrow account No-input field |
| 5 | `ESCROW.PB.DISBURSE.DATE` | `EscrowPayeeBill_DisburseDate` | TField |  | T24 Date when disbursement attempted was failed. No-input field |
| 6 | `ESCROW.PB.ISSUE.DATE` | `EscrowPayeeBill_IssueDate` | TField |  |  |
| 7 | `ESCROW.PB.RESERVED.16` | `EscrowPayeeBill_Reserved16` | TField |  |  |
| 8 | `ESCROW.PB.RESERVED.15` | `EscrowPayeeBill_Reserved15` | TField |  |  |
| 9 | `ESCROW.PB.REASON` | `EscrowPayeeBill_Reason` |  |  |  |
| 10 | `ESCROW.PB.AVAIL.BALANCE` | `EscrowPayeeBill_AvailBalance` | TField |  | Available Escrow Balance when disbursement was attempted. No-input field |
| 11 | `ESCROW.PB.INITIATION.TYPE` | `EscrowPayeeBill_InitiationType` | TField |  | The attempted activity was initiated during COB by the system or by the USER. No-input field. |
| 12 | `ESCROW.PB.LAST.UPDATE` | `EscrowPayeeBill_LastUpdate` | TField |  | Date and time when this activity was updated here. No-input field. |
| 13 | `ESCROW.PB.ORIG.AMOUNT` | `EscrowPayeeBill_OrigAmount` | TField |  | Disbursement Amount. No-input field. |
| 14 | `ESCROW.PB.LATE.FEE` | `EscrowPayeeBill_LateFee` | TField |  | Any late fee configured for the payee. |
| 15 | `ESCROW.PB.PENALTYINT.AMT` | `EscrowPayeeBill_PenaltyintAmt` | TField |  | Any penalty interest calculated. This amount will be re-calculated and defaulted as of today. |
| 16 | `ESCROW.PB.TOTAL.AMT` | `EscrowPayeeBill_TotalAmt` | TField |  | Total of ORIG.AMOUNT, LATE.FEE and PENALTYINT.AMT. No-input field. |
| 17 | `ESCROW.PB.NEW.AMOUNT` | `EscrowPayeeBill_NewAmount` | TField |  | User can override the Original Disbursement Amount |
| 18 | `ESCROW.PB.NEW.LATE.FEE` | `EscrowPayeeBill_NewLateFee` | TField |  | User can provide a new late fee |
| 19 | `ESCROW.PB.NEW.PENALTYINT.AMT` | `EscrowPayeeBill_NewPenaltyintAmt` | TField |  | User can provide a new penalty interest amount. |
| 20 | `ESCROW.PB.NEW.TOTAL.AMOUNT` | `EscrowPayeeBill_NewTotalAmount` | TField |  | New Total adjusted amount, sum of New Amount, New Late Fee and New Penalty Interest Amount. |
| 21 | `ESCROW.PB.WAIVE.BILL` | `EscrowPayeeBill_WaiveBill` | TField |  | If checked then this bill will be marked as waived and will not be disbursed anymore. |
| 22 | `ESCROW.PB.DISBURSE.MODE` | `EscrowPayeeBill_DisburseMode` | TField |  | Field to determine how the bill was changed to DISBURSED status. Possible values: AUTOMATIC MANUAL RETRY |
| 23 | `ESCROW.PB.STATUS` | `EscrowPayeeBill_Status` |  |  |  |
| 24 | `ESCROW.PB.STATUS.CHG.DATE` | `EscrowPayeeBill_StatusChgDate` |  |  |  |
| 25 | `ESCROW.PB.RESERVED.14` | `EscrowPayeeBill_Reserved14` |  |  |  |
| 26 | `ESCROW.PB.RESERVED.13` | `EscrowPayeeBill_Reserved13` |  |  |  |
| 27 | `ESCROW.PB.RESERVED.12` | `EscrowPayeeBill_Reserved12` |  |  |  |
| 28 | `ESCROW.PB.FT.REF` | `EscrowPayeeBill_FtRef` | TField |  | FUNDS.TRANSFER reference that raised accounting entries. No-input field. |
| 29 | `ESCROW.PB.PAYMENT.ORDER.ID` | `EscrowPayeeBill_PaymentOrderId` | TField |  | Contains the payment order Id which was used to settle the bill to the actual payee account.. No-input field. |
| 30 | `ESCROW.PB.RESERVED.11` | `EscrowPayeeBill_Reserved11` | TField |  |  |
| 31 | `ESCROW.PB.RESERVED.10` | `EscrowPayeeBill_Reserved10` | TField |  |  |
| 32 | `ESCROW.PB.RESERVED.9` | `EscrowPayeeBill_Reserved9` | TField |  |  |
| 33 | `ESCROW.PB.RESERVED.8` | `EscrowPayeeBill_Reserved8` | TField |  |  |
| 34 | `ESCROW.PB.RESERVED.7` | `EscrowPayeeBill_Reserved7` | TField |  |  |
| 35 | `ESCROW.PB.RESERVED.6` | `EscrowPayeeBill_Reserved6` | TField |  |  |
| 36 | `ESCROW.PB.RESERVED.5` | `EscrowPayeeBill_Reserved5` | TField |  |  |
| 37 | `ESCROW.PB.RESERVED.4` | `EscrowPayeeBill_Reserved4` | TField |  |  |
| 38 | `ESCROW.PB.RESERVED.3` | `EscrowPayeeBill_Reserved3` | TField |  |  |
| 39 | `ESCROW.PB.RESERVED.2` | `EscrowPayeeBill_Reserved2` | TField |  |  |
| 40 | `ESCROW.PB.RESERVED.1` | `EscrowPayeeBill_Reserved1` | TField |  |  |
