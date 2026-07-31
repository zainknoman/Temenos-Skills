# PPTNCL.CLEAR.PENDING.CHEQUE — Table Schema

> Source: `INSERTS/I_F.PPTNCL.CLEAR.PENDING.CHEQUE` in `PPTNCL_ChequeClearing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTNCL.CQ.INTEREST.CALCULATED` | `PptnclClearPendingCheque_InterestCalculated` | TField |  |  |
| 2 | `PPTNCL.CQ.BAILIFF.CHARGES` | `PptnclClearPendingCheque_BailiffCharges` | TField |  |  |
| 3 | `PPTNCL.CQ.TREASURY.CHARGES` | `PptnclClearPendingCheque_TreasuryCharges` | TField |  |  |
| 4 | `PPTNCL.CQ.BAILIFF.NOTIFICATION.DATE` | `PptnclClearPendingCheque_BailiffNotificationDate` | TField |  |  |
| 5 | `PPTNCL.CQ.TOTAL.AMOUNT` | `PptnclClearPendingCheque_TotalAmount` | TField |  |  |
| 6 | `PPTNCL.CQ.JUDGEMENT.DATE` | `PptnclClearPendingCheque_JudgementDate` | TField |  |  |
| 7 | `PPTNCL.CQ.APPROVE.CHEQUE` | `PptnclClearPendingCheque_ApproveCheque` | TField |  |  |
| 8 | `PPTNCL.CQ.STATUS` | `PptnclClearPendingCheque_Status` | TField |  |  |
| 9 | `PPTNCL.CQ.SENDING.BANK.CODE` | `PptnclClearPendingCheque_SendingBankCode` | TField |  |  |
| 10 | `PPTNCL.CQ.LOT.NUMBER` | `PptnclClearPendingCheque_LotNumber` | TField |  |  |
| 11 | `PPTNCL.CQ.VALUE.CODE` | `PptnclClearPendingCheque_ValueCode` | TField |  |  |
| 12 | `PPTNCL.CQ.CHEQUE.AMOUNT` | `PptnclClearPendingCheque_ChequeAmount` | TField |  |  |
| 13 | `PPTNCL.CQ.BALANCE.CHEQUE.AMOUNT` | `PptnclClearPendingCheque_BalanceChequeAmount` | TField |  |  |
| 14 | `PPTNCL.CQ.CHEQUE.ISSUE.DATE` | `PptnclClearPendingCheque_ChequeIssueDate` | TField |  |  |
| 15 | `PPTNCL.CQ.CHEQUE.NUMBER` | `PptnclClearPendingCheque_ChequeNumber` | TField |  |  |
| 16 | `PPTNCL.CQ.PAYER.ACCOUNT.NO` | `PptnclClearPendingCheque_PayerAccountNo` | TField |  |  |
| 17 | `PPTNCL.CQ.PAYER.BANK.CODE` | `PptnclClearPendingCheque_PayerBankCode` | TField |  |  |
| 18 | `PPTNCL.CQ.PAYEE.ACCOUNT.NO` | `PptnclClearPendingCheque_PayeeAccountNo` | TField |  |  |
| 19 | `PPTNCL.CQ.PLACE.OF.ISSUE` | `PptnclClearPendingCheque_PlaceOfIssue` | TField |  |  |
| 20 | `PPTNCL.CQ.CNP.NUMBER` | `PptnclClearPendingCheque_CnpNumber` | TField |  |  |
| 21 | `PPTNCL.CQ.REGULARIZED.AMOUNT` | `PptnclClearPendingCheque_RegularizedAmount` | TField |  |  |
| 22 | `PPTNCL.CQ.RESERVED.9` | `PptnclClearPendingCheque_Reserved9` | TField |  |  |
| 23 | `PPTNCL.CQ.RESERVED.8` | `PptnclClearPendingCheque_Reserved8` | TField |  |  |
| 24 | `PPTNCL.CQ.RESERVED.7` | `PptnclClearPendingCheque_Reserved7` | TField |  |  |
| 25 | `PPTNCL.CQ.RESERVED.6` | `PptnclClearPendingCheque_Reserved6` | TField |  |  |
| 26 | `PPTNCL.CQ.RESERVED.5` | `PptnclClearPendingCheque_Reserved5` | TField |  |  |
| 27 | `PPTNCL.CQ.RESERVED.4` | `PptnclClearPendingCheque_Reserved4` | TField |  |  |
| 28 | `PPTNCL.CQ.RESERVED.3` | `PptnclClearPendingCheque_Reserved3` | TField |  |  |
| 29 | `PPTNCL.CQ.RESERVED.2` | `PptnclClearPendingCheque_Reserved2` | TField |  |  |
| 30 | `PPTNCL.CQ.RESERVED.1` | `PptnclClearPendingCheque_Reserved1` | TField |  |  |
| 31 | `PPTNCL.CQ.LOCAL.REF` | `PptnclClearPendingCheque_LocalRef` |  |  |  |
| 32 | `PPTNCL.CQ.OVERRIDE` | `PptnclClearPendingCheque_Override` |  |  |  |
| 33 | `PPTNCL.CQ.RECORD.STATUS` | `PptnclClearPendingCheque_RecordStatus` | String |  |  |
| 34 | `PPTNCL.CQ.CURR.NO` | `PptnclClearPendingCheque_CurrNo` | String |  |  |
| 35 | `PPTNCL.CQ.INPUTTER` | `PptnclClearPendingCheque_Inputter` |  |  |  |
| 36 | `PPTNCL.CQ.DATE.TIME` | `PptnclClearPendingCheque_DateTime` |  |  |  |
| 37 | `PPTNCL.CQ.AUTHORISER` | `PptnclClearPendingCheque_Authoriser` | String |  |  |
| 38 | `PPTNCL.CQ.CO.CODE` | `PptnclClearPendingCheque_CoCode` | String |  |  |
| 39 | `PPTNCL.CQ.DEPT.CODE` | `PptnclClearPendingCheque_DeptCode` | String |  |  |
| 40 | `PPTNCL.CQ.AUDITOR.CODE` | `PptnclClearPendingCheque_AuditorCode` | String |  |  |
| 41 | `PPTNCL.CQ.AUDIT.DATE.TIME` | `PptnclClearPendingCheque_AuditDateTime` | String |  |  |
