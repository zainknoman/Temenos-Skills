# CAMB.TELPAY.GET.STMT.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.GET.STMT.DETS` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TELPAY.STMT.MSG.TYPE` | `CambTelpayGetStmtDets_MsgType` |  |  |  |
| 2 | `CAMB.TELPAY.STMT.MSG.FROM` | `CambTelpayGetStmtDets_MsgFrom` |  |  |  |
| 3 | `CAMB.TELPAY.STMT.MSG.REPLY` | `CambTelpayGetStmtDets_MsgReply` |  |  |  |
| 4 | `CAMB.TELPAY.STMT.MSG.TRACE` | `CambTelpayGetStmtDets_MsgTrace` |  |  |  |
| 5 | `CAMB.TELPAY.STMT.MSG.DATE` | `CambTelpayGetStmtDets_MsgDate` |  |  |  |
| 6 | `CAMB.TELPAY.STMT.MSG.TIME` | `CambTelpayGetStmtDets_MsgTime` |  |  |  |
| 7 | `CAMB.TELPAY.STMT.MSG.EXTRA` | `CambTelpayGetStmtDets_MsgExtra` |  |  |  |
| 8 | `CAMB.TELPAY.STMT.MSG.SESSION` | `CambTelpayGetStmtDets_MsgSession` |  |  |  |
| 9 | `CAMB.TELPAY.STMT.MSG.MEMBER` | `CambTelpayGetStmtDets_MsgMember` |  |  |  |
| 10 | `CAMB.TELPAY.STMT.MSG.RECORD` | `CambTelpayGetStmtDets_MsgRecord` |  |  |  |
| 11 | `CAMB.TELPAY.STMT.PROD.CAT` | `CambTelpayGetStmtDets_ProdCat` |  |  |  |
| 12 | `CAMB.TELPAY.STMT.PROD.TYPE` | `CambTelpayGetStmtDets_ProdType` |  |  |  |
| 13 | `CAMB.TELPAY.STMT.MSG.NO.RSP` | `CambTelpayGetStmtDets_MsgNoRsp` |  |  |  |
| 14 | `CAMB.TELPAY.STMT.PROD.NUM` | `CambTelpayGetStmtDets_ProdNum` |  |  |  |
| 15 | `CAMB.TELPAY.STMT.PRT.OPTION` | `CambTelpayGetStmtDets_PrtOption` |  |  |  |
| 16 | `CAMB.TELPAY.STMT.ATT.OPTION` | `CambTelpayGetStmtDets_AttOption` |  |  |  |
| 17 | `CAMB.TELPAY.STMT.PRT.DATE` | `CambTelpayGetStmtDets_PrtDate` |  |  |  |
| 18 | `CAMB.TELPAY.STMT.PRT.ENDBAL` | `CambTelpayGetStmtDets_PrtEndbal` |  |  |  |
| 19 | `CAMB.TELPAY.STMT.MINUS.SIGN.PRD` | `CambTelpayGetStmtDets_MinusSignPrd` |  |  |  |
| 20 | `CAMB.TELPAY.STMT.TXN.REQUEST` | `CambTelpayGetStmtDets_TxnRequest` |  |  |  |
| 21 | `CAMB.TELPAY.STMT.TXN.RECEIVED` | `CambTelpayGetStmtDets_TxnReceived` |  |  |  |
| 22 | `CAMB.TELPAY.STMT.TXN.FLAG` | `CambTelpayGetStmtDets_TxnFlag` |  |  |  |
| 23 | `CAMB.TELPAY.STMT.SRCH.EF.DATE` | `CambTelpayGetStmtDets_SrchEfDate` |  |  |  |
| 24 | `CAMB.TELPAY.STMT.SRCH.END.DAT` | `CambTelpayGetStmtDets_SrchEndDat` |  |  |  |
| 25 | `CAMB.TELPAY.STMT.SRCH.TIME` | `CambTelpayGetStmtDets_SrchTime` |  |  |  |
| 26 | `CAMB.TELPAY.STMT.SRCH.SOURCE` | `CambTelpayGetStmtDets_SrchSource` |  |  |  |
| 27 | `CAMB.TELPAY.STMT.SRCH.AMT` | `CambTelpayGetStmtDets_SrchAmt` |  |  |  |
| 28 | `CAMB.TELPAY.STMT.MINUS.SIGN1` | `CambTelpayGetStmtDets_MinusSign1` |  |  |  |
| 29 | `CAMB.TELPAY.STMT.SRCH.TID` | `CambTelpayGetStmtDets_SrchTid` |  |  |  |
| 30 | `CAMB.TELPAY.STMT.SRCH.MID` | `CambTelpayGetStmtDets_SrchMid` |  |  |  |
| 31 | `CAMB.TELPAY.STMT.SRCH.RECON` | `CambTelpayGetStmtDets_SrchRecon` |  |  |  |
| 32 | `CAMB.TELPAY.STMT.SRCH.CNT` | `CambTelpayGetStmtDets_SrchCnt` |  |  |  |
| 33 | `CAMB.TELPAY.STMT.PRT.TILL` | `CambTelpayGetStmtDets_PrtTill` |  |  |  |
| 34 | `CAMB.TELPAY.STMT.TXN.SENT` | `CambTelpayGetStmtDets_TxnSent` |  |  |  |
| 35 | `CAMB.TELPAY.STMT.TXN.REMAIN` | `CambTelpayGetStmtDets_TxnRemain` |  |  |  |
| 36 | `CAMB.TELPAY.STMT.TXN.EFDATE` | `CambTelpayGetStmtDets_TxnEfdate` |  |  |  |
| 37 | `CAMB.TELPAY.STMT.TXN.ENDDATE` | `CambTelpayGetStmtDets_TxnEnddate` |  |  |  |
| 38 | `CAMB.TELPAY.STMT.TXN.DESC` | `CambTelpayGetStmtDets_TxnDesc` |  |  |  |
| 39 | `CAMB.TELPAY.STMT.TXN.AMT` | `CambTelpayGetStmtDets_TxnAmt` |  |  |  |
| 40 | `CAMB.TELPAY.STMT.TXN.MINUS` | `CambTelpayGetStmtDets_TxnMinus` |  |  |  |
| 41 | `CAMB.TELPAY.STMT.MINUS.SIGN.END` | `CambTelpayGetStmtDets_MinusSignEnd` |  |  |  |
| 42 | `CAMB.TELPAY.STMT.MINUS.SIGN2` | `CambTelpayGetStmtDets_MinusSign2` |  |  |  |
| 43 | `CAMB.TELPAY.STMT.TXN.ENDBAL` | `CambTelpayGetStmtDets_TxnEndbal` |  |  |  |
| 44 | `CAMB.TELPAY.STMT.ENDBAL.MINUS.SIGN1` | `CambTelpayGetStmtDets_EndbalMinusSign1` |  |  |  |
| 45 | `CAMB.TELPAY.STMT.TXN.SOURCE` | `CambTelpayGetStmtDets_TxnSource` |  |  |  |
| 46 | `CAMB.TELPAY.STMT.TXN.ATT.CNT` | `CambTelpayGetStmtDets_TxnAttCnt` |  |  |  |
| 47 | `CAMB.TELPAY.STMT.CLEARING.ACCT` | `CambTelpayGetStmtDets_ClearingAcct` |  |  |  |
| 48 | `CAMB.TELPAY.STMT.STMT.ATTR` | `CambTelpayGetStmtDets_StmtAttr` |  |  |  |
| 49 | `CAMB.TELPAY.STMT.MSG.REC.ID` | `CambTelpayGetStmtDets_MsgRecId` |  |  |  |
