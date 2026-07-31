# ETBROP.LMTS.TRANS — Table Schema

> Source: `INSERTS/I_F.ETBROP.LMTS.TRANS` in `ETBROP_LocalMoneyTransferService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETBROP.LMTS.FT.TXN.NO` | `EtbropLmtsTrans_FtTxnNo` | TField |  | This is the transaction reference number resulted in transfer of funds from branch payable account to HO payable account. This will be auto generated as per FT application. |
| 2 | `ETBROP.LMTS.TRANSFER.STATUS` | `EtbropLmtsTrans_TransferStatus` | TField |  | �D� for Deposits �P� for Paid �T� for Transferred to Unclaimed. |
| 3 | `ETBROP.LMTS.SEC.CODE` | `EtbropLmtsTrans_SecCode` | TField |  | A unique security number generated automatically for all LMTS transactions. |
| 4 | `ETBROP.LMTS.DEPOSIT.DATE` | `EtbropLmtsTrans_DepositDate` | TField |  | Defines the deposit value date. |
| 5 | `ETBROP.LMTS.TRANSFER.DATE` | `EtbropLmtsTrans_TransferDate` | TField |  | Defines the date on which funds are transferred from Branch payable account to HO unclaimed account. |
| 6 | `ETBROP.LMTS.STOP.PAYMENT.REASON` | `EtbropLmtsTrans_StopPaymentReason` | TField |  | Defines the reason for stop payment entered by the user. |
| 7 | `ETBROP.LMTS.REM.NAME` | `EtbropLmtsTrans_RemName` | TField |  | Defines the Remitter Name. |
| 8 | `ETBROP.LMTS.PAYEE.NAME` | `EtbropLmtsTrans_PayeeName` | TField |  | Defines the the Beneficiary Name. |
| 9 | `ETBROP.LMTS.TEL.NO.REM` | `EtbropLmtsTrans_TelNoRem` | TField |  | Defines the Telephone Number of Remitter. |
| 10 | `ETBROP.LMTS.TEL.NO.BEN` | `EtbropLmtsTrans_TelNoBen` | TField |  | Defines the Telephone Number of Beneficiary. |
| 11 | `ETBROP.LMTS.LEGAL.ID` | `EtbropLmtsTrans_LegalId` | TField |  | Defines the Legal ID Number . |
| 12 | `ETBROP.LMTS.LOCAL.REF` | `EtbropLmtsTrans_LocalRef` |  |  |  |
| 13 | `ETBROP.LMTS.OVERRIDE` | `EtbropLmtsTrans_Override` |  |  |  |
| 14 | `ETBROP.LMTS.RECORD.STATUS` | `EtbropLmtsTrans_RecordStatus` | String |  |  |
| 15 | `ETBROP.LMTS.CURR.NO` | `EtbropLmtsTrans_CurrNo` | String |  |  |
| 16 | `ETBROP.LMTS.INPUTTER` | `EtbropLmtsTrans_Inputter` |  |  |  |
| 17 | `ETBROP.LMTS.DATE.TIME` | `EtbropLmtsTrans_DateTime` |  |  |  |
| 18 | `ETBROP.LMTS.AUTHORISER` | `EtbropLmtsTrans_Authoriser` | String |  |  |
| 19 | `ETBROP.LMTS.CO.CODE` | `EtbropLmtsTrans_CoCode` | String |  |  |
| 20 | `ETBROP.LMTS.DEPT.CODE` | `EtbropLmtsTrans_DeptCode` | String |  |  |
| 21 | `ETBROP.LMTS.AUDITOR.CODE` | `EtbropLmtsTrans_AuditorCode` | String |  |  |
| 22 | `ETBROP.LMTS.AUDIT.DATE.TIME` | `EtbropLmtsTrans_AuditDateTime` | String |  |  |
