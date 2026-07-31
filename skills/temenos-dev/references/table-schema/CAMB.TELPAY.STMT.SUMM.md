# CAMB.TELPAY.STMT.SUMM — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.STMT.SUMM` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.STMT.MSG.TYPE` | `CambTelpayStmtSumm_MsgType` |  |  |  |
| 2 | `CAMB.TP.STMT.MSG.FROM` | `CambTelpayStmtSumm_MsgFrom` |  |  |  |
| 3 | `CAMB.TP.STMT.MSG.REPLY` | `CambTelpayStmtSumm_MsgReply` |  |  |  |
| 4 | `CAMB.TP.STMT.MSG.TRACE` | `CambTelpayStmtSumm_MsgTrace` |  |  |  |
| 5 | `CAMB.TP.STMT.MSG.DATE` | `CambTelpayStmtSumm_MsgDate` |  |  |  |
| 6 | `CAMB.TP.STMT.MSG.TIME` | `CambTelpayStmtSumm_MsgTime` |  |  |  |
| 7 | `CAMB.TP.STMT.MSG.EXTRA` | `CambTelpayStmtSumm_MsgExtra` |  |  |  |
| 8 | `CAMB.TP.STMT.MSG.SESSION` | `CambTelpayStmtSumm_MsgSession` |  |  |  |
| 9 | `CAMB.TP.STMT.MSG.MEMBER` | `CambTelpayStmtSumm_MsgMember` |  |  |  |
| 10 | `CAMB.TP.STMT.MSG.RECORD` | `CambTelpayStmtSumm_MsgRecord` |  |  |  |
| 11 | `CAMB.TP.STMT.PRODCAT` | `CambTelpayStmtSumm_Prodcat` |  |  |  |
| 12 | `CAMB.TP.STMT.PRODCCY` | `CambTelpayStmtSumm_Prodccy` |  |  |  |
| 13 | `CAMB.TP.STMT.PRODTYPE` | `CambTelpayStmtSumm_Prodtype` |  |  |  |
| 14 | `CAMB.TP.STMT.PRODNUM` | `CambTelpayStmtSumm_Prodnum` |  |  |  |
| 15 | `CAMB.TP.STMT.SRCH.OPTION` | `CambTelpayStmtSumm_SrchOption` |  |  |  |
| 16 | `CAMB.TP.STMT.ATT.OPTION` | `CambTelpayStmtSumm_AttOption` |  |  |  |
| 17 | `CAMB.TP.STMT.FROM.DATE` | `CambTelpayStmtSumm_FromDate` |  |  |  |
| 18 | `CAMB.TP.STMT.TO.DATE` | `CambTelpayStmtSumm_ToDate` |  |  |  |
| 19 | `CAMB.TP.STMT.SRCH.AMT` | `CambTelpayStmtSumm_SrchAmt` |  |  |  |
| 20 | `CAMB.TP.STMT.SRCH.MINUS.SIGN` | `CambTelpayStmtSumm_SrchMinusSign` |  |  |  |
| 21 | `CAMB.TP.STMT.SRCH.RECON` | `CambTelpayStmtSumm_SrchRecon` |  |  |  |
| 22 | `CAMB.TP.STMT.TXN.REQUEST` | `CambTelpayStmtSumm_TxnRequest` |  |  |  |
| 23 | `CAMB.TP.STMT.TXN.RECEIVED` | `CambTelpayStmtSumm_TxnReceived` |  |  |  |
| 24 | `CAMB.TP.STMT.TXN.SENT` | `CambTelpayStmtSumm_TxnSent` |  |  |  |
| 25 | `CAMB.TP.STMT.TXN.FLAG` | `CambTelpayStmtSumm_TxnFlag` |  |  |  |
| 26 | `CAMB.TP.STMT.NO.OF.TXNS` | `CambTelpayStmtSumm_NoOfTxns` |  |  |  |
| 27 | `CAMB.TP.STMT.TXN.EFDAT` | `CambTelpayStmtSumm_TxnEfdat` |  |  |  |
| 28 | `CAMB.TP.STMT.TXN.ENDAT` | `CambTelpayStmtSumm_TxnEndat` |  |  |  |
| 29 | `CAMB.TP.STMT.TXN.DESC1` | `CambTelpayStmtSumm_TxnDesc1` |  |  |  |
| 30 | `CAMB.TP.STMT.TXN.DESC2` | `CambTelpayStmtSumm_TxnDesc2` |  |  |  |
| 31 | `CAMB.TP.STMT.TXN.DESC3` | `CambTelpayStmtSumm_TxnDesc3` |  |  |  |
| 32 | `CAMB.TP.STMT.TXN.SOURCE` | `CambTelpayStmtSumm_TxnSource` |  |  |  |
| 33 | `CAMB.TP.STMT.TXN.PMT` | `CambTelpayStmtSumm_TxnPmt` |  |  |  |
| 34 | `CAMB.TP.STMT.TXN.MINUS` | `CambTelpayStmtSumm_TxnMinus` |  |  |  |
| 35 | `CAMB.TP.STMT.TXN.RECON` | `CambTelpayStmtSumm_TxnRecon` |  |  |  |
| 36 | `CAMB.TP.STMT.MSG.ASOFDATE` | `CambTelpayStmtSumm_MsgAsofdate` |  |  |  |
| 37 | `CAMB.TP.STMT.MSG.REC.ID` | `CambTelpayStmtSumm_MsgRecId` |  |  |  |
