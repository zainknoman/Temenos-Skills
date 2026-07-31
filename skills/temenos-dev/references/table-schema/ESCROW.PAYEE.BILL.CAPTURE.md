# ESCROW.PAYEE.BILL.CAPTURE — Table Schema

> Source: `INSERTS/I_F.ESCROW.PAYEE.BILL.CAPTURE` in `ESCROW_PaymentProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.PBC.ESCROW.ACCOUNT.ID` | `EscrowPayeeBillCapture_EscrowAccountId` | TField |  | The escrow account for which an ad-hoc request is input |
| 2 | `ESCROW.PBC.PAYEE.ID` | `EscrowPayeeBillCapture_PayeeId` | TField |  | The payee for whom the payment has to be remitted |
| 3 | `ESCROW.PBC.PAYEE.REF.NO` | `EscrowPayeeBillCapture_PayeeRefNo` | TField |  | The reference related to the tax payment. |
| 4 | `ESCROW.PBC.CURRENCY` | `EscrowPayeeBillCapture_Currency` | TField |  | Currency of escrow account |
| 5 | `ESCROW.PBC.DISBURSE.DATE` | `EscrowPayeeBillCapture_DisburseDate` | TField |  | The date on which the tax payment has to be remitted to the escrow payee. |
| 6 | `ESCROW.PBC.RESERVED.23` | `EscrowPayeeBillCapture_Reserved23` | TField |  |  |
| 7 | `ESCROW.PBC.RESERVED.22` | `EscrowPayeeBillCapture_Reserved22` | TField |  |  |
| 8 | `ESCROW.PBC.RESERVED.21` | `EscrowPayeeBillCapture_Reserved21` | TField |  |  |
| 9 | `ESCROW.PBC.REASON` | `EscrowPayeeBillCapture_Reason` |  |  |  |
| 10 | `ESCROW.PBC.INITIATION.TYPE` | `EscrowPayeeBillCapture_InitiationType` | TField |  | Reserved for future use. No-input field. |
| 11 | `ESCROW.PBC.ORIG.AMOUNT` | `EscrowPayeeBillCapture_OrigAmount` | TField |  | The original payment amount that has to be remited to the payee |
| 12 | `ESCROW.PBC.RESERVED.20` | `EscrowPayeeBillCapture_Reserved20` | TField |  |  |
| 13 | `ESCROW.PBC.RESERVED.19` | `EscrowPayeeBillCapture_Reserved19` | TField |  |  |
| 14 | `ESCROW.PBC.RESERVED.18` | `EscrowPayeeBillCapture_Reserved18` | TField |  |  |
| 15 | `ESCROW.PBC.RESERVED.17` | `EscrowPayeeBillCapture_Reserved17` | TField |  |  |
| 16 | `ESCROW.PBC.RESERVED.16` | `EscrowPayeeBillCapture_Reserved16` | TField |  |  |
| 17 | `ESCROW.PBC.RESERVED.15` | `EscrowPayeeBillCapture_Reserved15` | TField |  |  |
| 18 | `ESCROW.PBC.RESERVED.14` | `EscrowPayeeBillCapture_Reserved14` | TField |  |  |
| 19 | `ESCROW.PBC.RESERVED.13` | `EscrowPayeeBillCapture_Reserved13` | TField |  |  |
| 20 | `ESCROW.PBC.RESERVED.12` | `EscrowPayeeBillCapture_Reserved12` | TField |  |  |
| 21 | `ESCROW.PBC.RESERVED.11` | `EscrowPayeeBillCapture_Reserved11` | TField |  |  |
| 22 | `ESCROW.PBC.RESERVED.10` | `EscrowPayeeBillCapture_Reserved10` | TField |  |  |
| 23 | `ESCROW.PBC.RESERVED.9` | `EscrowPayeeBillCapture_Reserved9` | TField |  |  |
| 24 | `ESCROW.PBC.RESERVED.8` | `EscrowPayeeBillCapture_Reserved8` | TField |  |  |
| 25 | `ESCROW.PBC.RESERVED.7` | `EscrowPayeeBillCapture_Reserved7` | TField |  |  |
| 26 | `ESCROW.PBC.RESERVED.6` | `EscrowPayeeBillCapture_Reserved6` | TField |  |  |
| 27 | `ESCROW.PBC.RESERVED.5` | `EscrowPayeeBillCapture_Reserved5` | TField |  |  |
| 28 | `ESCROW.PBC.RESERVED.4` | `EscrowPayeeBillCapture_Reserved4` | TField |  |  |
| 29 | `ESCROW.PBC.RESERVED.3` | `EscrowPayeeBillCapture_Reserved3` | TField |  |  |
| 30 | `ESCROW.PBC.RESERVED.2` | `EscrowPayeeBillCapture_Reserved2` | TField |  |  |
| 31 | `ESCROW.PBC.RESERVED.1` | `EscrowPayeeBillCapture_Reserved1` | TField |  |  |
| 32 | `ESCROW.PBC.OVERRIDE` | `EscrowPayeeBillCapture_Override` |  |  |  |
| 33 | `ESCROW.PBC.RECORD.STATUS` | `EscrowPayeeBillCapture_RecordStatus` | String |  |  |
| 34 | `ESCROW.PBC.CURR.NO` | `EscrowPayeeBillCapture_CurrNo` | String |  |  |
| 35 | `ESCROW.PBC.INPUTTER` | `EscrowPayeeBillCapture_Inputter` |  |  |  |
| 36 | `ESCROW.PBC.DATE.TIME` | `EscrowPayeeBillCapture_DateTime` |  |  |  |
| 37 | `ESCROW.PBC.AUTHORISER` | `EscrowPayeeBillCapture_Authoriser` | String |  |  |
| 38 | `ESCROW.PBC.CO.CODE` | `EscrowPayeeBillCapture_CoCode` | String |  |  |
| 39 | `ESCROW.PBC.DEPT.CODE` | `EscrowPayeeBillCapture_DeptCode` | String |  |  |
| 40 | `ESCROW.PBC.AUDITOR.CODE` | `EscrowPayeeBillCapture_AuditorCode` | String |  |  |
| 41 | `ESCROW.PBC.AUDIT.DATE.TIME` | `EscrowPayeeBillCapture_AuditDateTime` | String |  |  |
