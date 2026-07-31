# ETBROP.LMTS.TRANS.HIS — Table Schema

> Source: `INSERTS/I_F.ETBROP.LMTS.TRANS.HIS` in `ETBROP_LocalMoneyTransferService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETBROP.LMTS.HIS.FT.TXN.NO` | `EtbropLmtsTransHis_FtTxnNo` | TField |  | This is the transaction reference number resulted in transfer of funds from branch payable account to HO payable account. This will be auto generated as per FT application. |
| 2 | `ETBROP.LMTS.HIS.TRANSFER.STATUS` | `EtbropLmtsTransHis_TransferStatus` | TField |  | �D� for Deposits �P� for Paid �T� for Transferred to Unclaimed. |
| 3 | `ETBROP.LMTS.HIS.SEC.CODE` | `EtbropLmtsTransHis_SecCode` | TField |  | A unique security number generated automatically for all LMTS transactions. |
| 4 | `ETBROP.LMTS.HIS.DEPOSIT.DATE` | `EtbropLmtsTransHis_DepositDate` | TField |  | Will define the deposit value date.. |
| 5 | `ETBROP.LMTS.HIS.PAID.TXN.REF.NO` | `EtbropLmtsTransHis_PaidTxnRefNo` | TField |  | This is the transaction reference number which resulted in transfer of funds from Deposit and Transferred to Paid status. |
| 6 | `ETBROP.LMTS.HIS.PAID.DATE` | `EtbropLmtsTransHis_PaidDate` | TField |  | This is the date when the deposit or Transferred status changes to Paid status. |
| 7 | `ETBROP.LMTS.HIS.TRANSFER.DATE` | `EtbropLmtsTransHis_TransferDate` | TField |  | Will define the date on which funds are transferred from Branch payable account to HO unclaimed account. |
