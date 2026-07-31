# ESCROW.BILL.MAINTENANCE — Table Schema

> Source: `INSERTS/I_F.ESCROW.BILL.MAINTENANCE` in `ESCROW_PaymentProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.BM.ESCROW.ACCOUNT.ID` | `EscrowBillMaintenance_EscrowAccountId` | TField |  | Accepts valid T24 account number Defaulted from @id No-input field. |
| 2 | `ESCROW.BM.MainteNANCE.DATE` | `EscrowBillMaintenance_MaintenanceDate` | TField |  | Accepts date in valid T24 format Defaulted from @id No-input field. |
| 3 | `ESCROW.BM.PAYEE.BILL.ID` | `EscrowBillMaintenance_PayeeBillId` |  |  |  |
| 4 | `ESCROW.BM.PAYEE.ID` | `EscrowBillMaintenance_PayeeId` |  |  |  |
| 5 | `ESCROW.BM.PAYEE.REF.NO` | `EscrowBillMaintenance_PayeeRefNo` |  |  |  |
| 6 | `ESCROW.BM.DISBURSE.DATE` | `EscrowBillMaintenance_DisburseDate` |  |  |  |
| 7 | `ESCROW.BM.REASON` | `EscrowBillMaintenance_Reason` |  |  |  |
| 8 | `ESCROW.BM.ORIG.AMOUNT` | `EscrowBillMaintenance_OrigAmount` |  |  |  |
| 9 | `ESCROW.BM.LATE.FEE` | `EscrowBillMaintenance_LateFee` |  |  |  |
| 10 | `ESCROW.BM.PENALTYINT.AMT` | `EscrowBillMaintenance_PenaltyintAmt` |  |  |  |
| 11 | `ESCROW.BM.TOTAL.AMT` | `EscrowBillMaintenance_TotalAmt` |  |  |  |
| 12 | `ESCROW.BM.NEW.AMOUNT` | `EscrowBillMaintenance_NewAmount` |  |  |  |
| 13 | `ESCROW.BM.NEW.LATE.FEE` | `EscrowBillMaintenance_NewLateFee` |  |  |  |
| 14 | `ESCROW.BM.NEW.PENALTYINT.AMT` | `EscrowBillMaintenance_NewPenaltyintAmt` |  |  |  |
| 15 | `ESCROW.BM.NEW.TOTAL.AMOUNT` | `EscrowBillMaintenance_NewTotalAmount` |  |  |  |
| 16 | `ESCROW.BM.ACTION` | `EscrowBillMaintenance_Action` |  |  |  |
| 17 | `ESCROW.BM.RESERVED.18` | `EscrowBillMaintenance_Reserved18` |  |  |  |
| 18 | `ESCROW.BM.RESERVED.17` | `EscrowBillMaintenance_Reserved17` |  |  |  |
| 19 | `ESCROW.BM.RESERVED.16` | `EscrowBillMaintenance_Reserved16` |  |  |  |
| 20 | `ESCROW.BM.RESERVED.15` | `EscrowBillMaintenance_Reserved15` | TField |  |  |
| 21 | `ESCROW.BM.RESERVED.14` | `EscrowBillMaintenance_Reserved14` | TField |  |  |
| 22 | `ESCROW.BM.RESERVED.13` | `EscrowBillMaintenance_Reserved13` | TField |  |  |
| 23 | `ESCROW.BM.RESERVED.12` | `EscrowBillMaintenance_Reserved12` | TField |  |  |
| 24 | `ESCROW.BM.RESERVED.11` | `EscrowBillMaintenance_Reserved11` | TField |  |  |
| 25 | `ESCROW.BM.RESERVED.10` | `EscrowBillMaintenance_Reserved10` | TField |  |  |
| 26 | `ESCROW.BM.RESERVED.9` | `EscrowBillMaintenance_Reserved9` | TField |  |  |
| 27 | `ESCROW.BM.RESERVED.8` | `EscrowBillMaintenance_Reserved8` | TField |  |  |
| 28 | `ESCROW.BM.RESERVED.7` | `EscrowBillMaintenance_Reserved7` | TField |  |  |
| 29 | `ESCROW.BM.RESERVED.6` | `EscrowBillMaintenance_Reserved6` | TField |  |  |
| 30 | `ESCROW.BM.RESERVED.5` | `EscrowBillMaintenance_Reserved5` | TField |  |  |
| 31 | `ESCROW.BM.RESERVED.4` | `EscrowBillMaintenance_Reserved4` | TField |  |  |
| 32 | `ESCROW.BM.RESERVED.3` | `EscrowBillMaintenance_Reserved3` | TField |  |  |
| 33 | `ESCROW.BM.RESERVED.2` | `EscrowBillMaintenance_Reserved2` | TField |  |  |
| 34 | `ESCROW.BM.RESERVED.1` | `EscrowBillMaintenance_Reserved1` | TField |  |  |
| 35 | `ESCROW.BM.RECORD.STATUS` | `EscrowBillMaintenance_RecordStatus` | String |  |  |
| 36 | `ESCROW.BM.CURR.NO` | `EscrowBillMaintenance_CurrNo` | String |  |  |
| 37 | `ESCROW.BM.INPUTTER` | `EscrowBillMaintenance_Inputter` |  |  |  |
| 38 | `ESCROW.BM.DATE.TIME` | `EscrowBillMaintenance_DateTime` |  |  |  |
| 39 | `ESCROW.BM.AUTHORISER` | `EscrowBillMaintenance_Authoriser` | String |  |  |
| 40 | `ESCROW.BM.CO.CODE` | `EscrowBillMaintenance_CoCode` | String |  |  |
| 41 | `ESCROW.BM.DEPT.CODE` | `EscrowBillMaintenance_DeptCode` | String |  |  |
| 42 | `ESCROW.BM.AUDITOR.CODE` | `EscrowBillMaintenance_AuditorCode` | String |  |  |
| 43 | `ESCROW.BM.AUDIT.DATE.TIME` | `EscrowBillMaintenance_AuditDateTime` | String |  |  |
