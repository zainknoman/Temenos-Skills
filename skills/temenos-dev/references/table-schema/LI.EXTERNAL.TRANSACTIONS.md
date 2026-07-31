# LI.EXTERNAL.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.LI.EXTERNAL.TRANSACTIONS` in `LI_ExternalTxn.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.LET.EVENT.TYPE` | `LiExternalTransactions_EventType` | TField | Yes | This field indicates that whether the External transaction exposure update is created for commitment or utilization or repayment purpose. Validation Rules: Non-mandatory field. For information purpose |
| 2 | `LI.LET.EVENT.REFERENCE` | `LiExternalTransactions_EventReference` | TField | Yes | Contains the External Event Reference which led to the creation external transaction in limit system. Validation Rules: Non-mandatory field. For information purpose |
| 3 | `LI.LET.LIMIT.ID` | `LiExternalTransactions_LimitId` |  |  |  |
| 4 | `LI.LET.LIMIT.ACTION` | `LiExternalTransactions_LimitAction` |  |  |  |
| 5 | `LI.LET.OVERRIDE.ACTION` | `LiExternalTransactions_OverrideAction` |  |  |  |
| 6 | `LI.LET.TRANSACTION.APPLICATION` | `LiExternalTransactions_TransactionApplication` |  |  |  |
| 7 | `LI.LET.TRANSACTION.REFERENCE` | `LiExternalTransactions_TransactionReference` |  |  |  |
| 8 | `LI.LET.TRANSACTION.COMPANY` | `LiExternalTransactions_TransactionCompany` |  |  |  |
| 9 | `LI.LET.CONTRACT.ID` | `LiExternalTransactions_ContractId` |  |  |  |
| 10 | `LI.LET.CONTRACT.COMPANY` | `LiExternalTransactions_ContractCompany` |  |  |  |
| 11 | `LI.LET.BOOKING.DATE` | `LiExternalTransactions_BookingDate` |  |  |  |
| 12 | `LI.LET.VALUE.DATE` | `LiExternalTransactions_ValueDate` |  |  |  |
| 13 | `LI.LET.MATURITY.DATE` | `LiExternalTransactions_MaturityDate` |  |  |  |
| 14 | `LI.LET.TRANSACTION.CURRENCY` | `LiExternalTransactions_TransactionCurrency` |  |  |  |
| 15 | `LI.LET.TRANSACTION.AMOUNT` | `LiExternalTransactions_TransactionAmount` |  |  |  |
| 16 | `LI.LET.FX.OTHER.CURRENCY` | `LiExternalTransactions_FxOtherCurrency` |  |  |  |
| 17 | `LI.LET.FX.OTHER.AMOUNT` | `LiExternalTransactions_FxOtherAmount` |  |  |  |
| 18 | `LI.LET.CR.DR.MARKER` | `LiExternalTransactions_CrDrMarker` |  |  |  |
| 19 | `LI.LET.COMMITMENT.CONTRACT` | `LiExternalTransactions_CommitmentContract` |  |  |  |
| 20 | `LI.LET.DRAWING.CONTRACT` | `LiExternalTransactions_DrawingContract` |  |  |  |
| 21 | `LI.LET.REVOLVING` | `LiExternalTransactions_Revolving` |  |  |  |
| 22 | `LI.LET.TRANSACTION.STATUS` | `LiExternalTransactions_TransactionStatus` |  |  |  |
| 23 | `LI.LET.DELETE.REASON` | `LiExternalTransactions_DeleteReason` |  |  |  |
| 24 | `LI.LET.SYSTEM.ID` | `LiExternalTransactions_SystemId` |  |  |  |
| 25 | `LI.LET.SOURCE.SYSTEM` | `LiExternalTransactions_SourceSystem` |  |  |  |
| 26 | `LI.LET.SOURCE.SYSTEM.DATE` | `LiExternalTransactions_SourceSystemDate` |  |  |  |
| 27 | `LI.LET.REVERSAL.FLAG` | `LiExternalTransactions_ReversalFlag` |  |  |  |
| 28 | `LI.LET.BALANCE.TYPE` | `LiExternalTransactions_BalanceType` |  |  |  |
| 29 | `LI.LET.ADDITIONAL.DETAILS.LABEL` | `LiExternalTransactions_AdditionalDetailsLabel` |  |  |  |
| 30 | `LI.LET.ADDITIONAL.DETAILS.VALUE` | `LiExternalTransactions_AdditionalDetailsValue` |  |  |  |
| 31 | `LI.LET.OVERRIDE` | `LiExternalTransactions_Override` |  |  |  |
| 32 | `LI.LET.RECORD.STATUS` | `LiExternalTransactions_RecordStatus` | String |  |  |
| 33 | `LI.LET.CURR.NO` | `LiExternalTransactions_CurrNo` | String |  |  |
| 34 | `LI.LET.INPUTTER` | `LiExternalTransactions_Inputter` |  |  |  |
| 35 | `LI.LET.DATE.TIME` | `LiExternalTransactions_DateTime` |  |  |  |
| 36 | `LI.LET.AUTHORISER` | `LiExternalTransactions_Authoriser` | String |  |  |
| 37 | `LI.LET.CO.CODE` | `LiExternalTransactions_CoCode` | String |  |  |
| 38 | `LI.LET.DEPT.CODE` | `LiExternalTransactions_DeptCode` | String |  |  |
| 39 | `LI.LET.AUDITOR.CODE` | `LiExternalTransactions_AuditorCode` | String |  |  |
| 40 | `LI.LET.AUDIT.DATE.TIME` | `LiExternalTransactions_AuditDateTime` | String |  |  |
