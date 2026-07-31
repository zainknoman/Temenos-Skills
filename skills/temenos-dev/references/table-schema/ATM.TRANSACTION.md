# ATM.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.ATM.TRANSACTION` in `ATMFRM_TransactionReference.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AT.REV.TRANS.REF` | `AtmTransaction_TransRef` |  |  |  |
| 2 | `AT.REV.COMPANY.CODE` | `AtmTransaction_CompanyCode` | TField |  |  |
| 3 | `AT.REV.VALUE.DATE` | `AtmTransaction_ValueDate` | TField |  |  |
| 4 | `AT.REV.BOOKING.DATE` | `AtmTransaction_BookingDate` | TField |  |  |
| 5 | `AT.REV.DEBIT.ACCT.NO` | `AtmTransaction_DebitAcctNo` | TField |  |  |
| 6 | `AT.REV.DR.CUSTOMER.ID` | `AtmTransaction_DrCustomerId` | TField |  |  |
| 7 | `AT.REV.CREDIT.ACCT.NO` | `AtmTransaction_CreditAcctNo` | TField |  |  |
| 8 | `AT.REV.TXN.AMOUNT` | `AtmTransaction_TxnAmount` |  |  |  |
| 9 | `AT.REV.DR.TXN.CODE` | `AtmTransaction_DrTxnCode` | TField |  |  |
| 10 | `AT.REV.CR.TXN.CODE` | `AtmTransaction_CrTxnCode` | TField |  |  |
| 11 | `AT.REV.CHARGE.CODE` | `AtmTransaction_ChargeCode` |  |  |  |
| 12 | `AT.REV.CHRG.AMOUNT` | `AtmTransaction_ChrgAmount` | TField |  |  |
| 13 | `AT.REV.CHRG.ACCOUNT` | `AtmTransaction_ChrgAccount` | TField |  |  |
| 14 | `AT.REV.CHRG.CUST.ID` | `AtmTransaction_ChrgCustId` | TField |  |  |
| 15 | `AT.REV.CHRG.CR.ACCT` | `AtmTransaction_ChrgCrAcct` |  |  |  |
| 16 | `AT.REV.CHRG.DR.TXN.CODE` | `AtmTransaction_ChrgDrTxnCode` | TField |  |  |
| 17 | `AT.REV.CHRG.CR.TXN.CODE` | `AtmTransaction_ChrgCrTxnCode` |  |  |  |
| 18 | `AT.REV.NARRATIVE` | `AtmTransaction_Narrative` | TField |  |  |
| 19 | `AT.REV.CURRENCY.MARKET` | `AtmTransaction_CurrencyMarket` | TField |  |  |
| 20 | `AT.REV.TRANS.STATUS` | `AtmTransaction_TransStatus` | TField |  |  |
| 21 | `AT.REV.REVERSAL.FLAG` | `AtmTransaction_ReversalFlag` | TField |  |  |
| 22 | `AT.REV.ORIG.STMT.NOS` | `AtmTransaction_OrigStmtNos` | TField |  |  |
| 23 | `AT.REV.STMT.NOS` | `AtmTransaction_StmtNos` | TField |  |  |
| 24 | `AT.REV.NETWORK.TYPE` | `AtmTransaction_NetworkType` | TField |  |  |
| 25 | `AT.REV.BIN.REFERENCE` | `AtmTransaction_BinReference` | TField |  |  |
| 26 | `AT.REV.PAN.NUMBER` | `AtmTransaction_PanNumber` | TField |  |  |
| 27 | `AT.REV.LOCKED.AMOUNT` | `AtmTransaction_LockedAmount` | TField |  |  |
| 28 | `AT.REV.LINKED.TRANS` | `AtmTransaction_LinkedTrans` | TField |  |  |
| 29 | `AT.REV.AUTH.CODE` | `AtmTransaction_AuthCode` | TField |  |  |
| 30 | `AT.REV.RETRIEVAL.REF.NO` | `AtmTransaction_RetrievalRefNo` | TField |  |  |
| 31 | `AT.REV.ACQ.OR.ISS` | `AtmTransaction_AcqOrIss` | TField |  |  |
| 32 | `AT.REV.ATM.OR.POS` | `AtmTransaction_AtmOrPos` | TField |  |  |
| 33 | `AT.REV.MTI.CODE` | `AtmTransaction_MtiCode` |  |  |  |
| 34 | `AT.REV.PROC.CODE` | `AtmTransaction_ProcCode` | TField |  |  |
| 35 | `AT.REV.MERCHANT.ID` | `AtmTransaction_MerchantId` | TField |  |  |
| 36 | `AT.REV.VERSION.NAME` | `AtmTransaction_VersionName` | TField |  |  |
| 37 | `AT.REV.CARD.ACC.ID` | `AtmTransaction_CardAccId` | TField |  |  |
| 38 | `AT.REV.CARD.ACC.NAME.LOC` | `AtmTransaction_CardAccNameLoc` | TField |  |  |
| 39 | `AT.REV.CHRG.VERSION.NAME` | `AtmTransaction_ChrgVersionName` | TField |  |  |
| 40 | `AT.REV.CHRG.TRANS.REF` | `AtmTransaction_ChrgTransRef` |  |  |  |
| 41 | `AT.REV.CHRG.DEBIT.AC` | `AtmTransaction_ChrgDebitAc` |  |  |  |
| 42 | `AT.REV.CHRG.CREDIT.AC` | `AtmTransaction_ChrgCreditAc` |  |  |  |
| 43 | `AT.REV.CHRG.AMT` | `AtmTransaction_ChrgAmt` |  |  |  |
| 44 | `AT.REV.CHRG.STMT.NOS` | `AtmTransaction_ChrgStmtNos` |  |  |  |
| 45 | `AT.REV.ERROR.MSG` | `AtmTransaction_ErrorMsg` | TField |  |  |
| 46 | `AT.REV.ERROR.CODE` | `AtmTransaction_ErrorCode` | TField |  |  |
| 47 | `AT.REV.ISO.NUMBER` | `AtmTransaction_IsoNumber` | TField |  |  |
| 48 | `AT.REV.STAN.NO` | `AtmTransaction_StanNo` | TField |  |  |
| 49 | `AT.REV.TIMESTAMP` | `AtmTransaction_Timestamp` | TField |  |  |
| 50 | `AT.REV.TXN.TYPE` | `AtmTransaction_TxnType` | TField |  |  |
| 51 | `AT.REV.DEPARTMENT.CODE` | `AtmTransaction_DepartmentCode` | TField |  |  |
| 52 | `AT.REV.ACCOUNT.OFFICER` | `AtmTransaction_AccountOfficer` | TField |  |  |
| 53 | `AT.REV.BAL.AFT.TXN` | `AtmTransaction_BalAftTxn` | TField |  |  |
| 54 | `AT.REV.GEN.MAPPING.ID` | `AtmTransaction_GenMappingId` | TField |  |  |
| 55 | `AT.REV.LOCAL.REF` | `AtmTransaction_LocalRef` |  |  |  |
| 56 | `AT.REV.RETRY.MESSAGE` | `AtmTransaction_RetryMessage` | TField |  |  |
| 57 | `AT.REV.DUPLICATE.COUNT` | `AtmTransaction_DuplicateCount` | TField |  |  |
| 58 | `AT.REV.REVERSAL.TRANS.REF` | `AtmTransaction_ReversalTransRef` |  |  |  |
| 59 | `AT.REV.REVERSAL.CHRG.TRANS.REF` | `AtmTransaction_ReversalChrgTransRef` |  |  |  |
| 60 | `AT.REV.REQUEST.TIME` | `AtmTransaction_RequestTime` | TField |  | Request date and start time captured on this field |
| 61 | `AT.REV.RESPONSE.TIME` | `AtmTransaction_ResponseTime` | TField |  | Response date and end time captured on this field |
| 62 | `AT.REV.PARTIAL.AUTH.FLAG` | `AtmTransaction_PartialAuthFlag` | TField |  | Stores YES if Transaction is partially authorised |
| 63 | `AT.REV.ALT.UNIQUE.ID` | `AtmTransaction_AlternateUniqueId` |  |  |  |
| 64 | `AT.REV.RESERVED.2` | `AtmTransaction_Reserved2` | TField |  |  |
| 65 | `AT.REV.RESERVED.1` | `AtmTransaction_Reserved1` | TField |  |  |
| 66 | `AT.REV.RECORD.STATUS` | `AtmTransaction_RecordStatus` | String |  |  |
| 67 | `AT.REV.CURR.NO` | `AtmTransaction_CurrNo` | String |  |  |
| 68 | `AT.REV.INPUTTER` | `AtmTransaction_Inputter` |  |  |  |
| 69 | `AT.REV.DATE.TIME` | `AtmTransaction_DateTime` |  |  |  |
| 70 | `AT.REV.AUTHORISER` | `AtmTransaction_Authoriser` | String |  |  |
| 71 | `AT.REV.CO.CODE` | `AtmTransaction_CoCode` | String |  |  |
| 72 | `AT.REV.DEPT.CODE` | `AtmTransaction_DeptCode` | String |  |  |
| 73 | `AT.REV.AUDITOR.CODE` | `AtmTransaction_AuditorCode` | String |  |  |
| 74 | `AT.REV.AUDIT.DATE.TIME` | `AtmTransaction_AuditDateTime` | String |  |  |
| 75 | `AT.REV.CHRG.TXN.CODE` | `AtmTransaction_ChargeTxnCode` |  |  |  |
