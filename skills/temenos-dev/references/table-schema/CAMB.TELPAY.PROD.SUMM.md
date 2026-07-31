# CAMB.TELPAY.PROD.SUMM — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.PROD.SUMM` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.PRD.SUM.MSG.TYPE` | `CambTelpayProdSumm_MsgType` |  |  |  |
| 2 | `CAMB.TP.PRD.SUM.MSG.FROM` | `CambTelpayProdSumm_MsgFrom` |  |  |  |
| 3 | `CAMB.TP.PRD.SUM.MSG.REPLY` | `CambTelpayProdSumm_MsgReply` |  |  |  |
| 4 | `CAMB.TP.PRD.SUM.MSG.TRACE` | `CambTelpayProdSumm_MsgTrace` |  |  |  |
| 5 | `CAMB.TP.PRD.SUM.MSG.DATE` | `CambTelpayProdSumm_MsgDate` |  |  |  |
| 6 | `CAMB.TP.PRD.SUM.MSG.TIME` | `CambTelpayProdSumm_MsgTime` |  |  |  |
| 7 | `CAMB.TP.PRD.SUM.MSG.SESSION` | `CambTelpayProdSumm_MsgSession` |  |  |  |
| 8 | `CAMB.TP.PRD.SUM.MSG.MEMBER` | `CambTelpayProdSumm_MsgMember` |  |  |  |
| 9 | `CAMB.TP.PRD.SUM.MSG.RECORD` | `CambTelpayProdSumm_MsgRecord` |  |  |  |
| 10 | `CAMB.TP.PRD.SUM.REQ.PRODCAT` | `CambTelpayProdSumm_ReqProdcat` |  |  |  |
| 11 | `CAMB.TP.PRD.SUM.REQ.PRODTYPE` | `CambTelpayProdSumm_ReqProdtype` |  |  |  |
| 12 | `CAMB.TP.PRD.SUM.REQ.PRODNUM` | `CambTelpayProdSumm_ReqProdnum` |  |  |  |
| 13 | `CAMB.TP.PRD.SUM.MSG.STATUS` | `CambTelpayProdSumm_MsgStatus` |  |  |  |
| 14 | `CAMB.TP.PRD.SUM.MSG.SUBSTATUS` | `CambTelpayProdSumm_MsgSubstatus` |  |  |  |
| 15 | `CAMB.TP.PRD.SUM.TXN.REQUEST` | `CambTelpayProdSumm_TxnRequest` |  |  |  |
| 16 | `CAMB.TP.PRD.SUM.TXN.RECEIVED` | `CambTelpayProdSumm_TxnReceived` |  |  |  |
| 17 | `CAMB.TP.PRD.SUM.TXN.SENT` | `CambTelpayProdSumm_TxnSent` |  |  |  |
| 18 | `CAMB.TP.PRD.SUM.SRCH.MID` | `CambTelpayProdSumm_SrchMid` |  |  |  |
| 19 | `CAMB.TP.PRD.SUM.SRCH.MNUM` | `CambTelpayProdSumm_SrchMnum` |  |  |  |
| 20 | `CAMB.TP.PRD.SUM.TXN.FLAG` | `CambTelpayProdSumm_TxnFlag` |  |  |  |
| 21 | `CAMB.TP.PRD.SUM.NO.OF.ACCTS` | `CambTelpayProdSumm_NoOfAccts` |  |  |  |
| 22 | `CAMB.TP.PRD.SUM.PRODCAT` | `CambTelpayProdSumm_Prodcat` |  |  |  |
| 23 | `CAMB.TP.PRD.SUM.PRODCCY` | `CambTelpayProdSumm_Prodccy` |  |  |  |
| 24 | `CAMB.TP.PRD.SUM.PRODTYPE` | `CambTelpayProdSumm_Prodtype` |  |  |  |
| 25 | `CAMB.TP.PRD.SUM.PRODNUM` | `CambTelpayProdSumm_Prodnum` |  |  |  |
| 26 | `CAMB.TP.PRD.SUM.PRODDESC` | `CambTelpayProdSumm_Proddesc` |  |  |  |
| 27 | `CAMB.TP.PRD.SUM.PRT.ENDBAL` | `CambTelpayProdSumm_PrtEndbal` |  |  |  |
| 28 | `CAMB.TP.PRD.SUM.MINUS.SIGN` | `CambTelpayProdSumm_MinusSign` |  |  |  |
| 29 | `CAMB.TP.PRD.SUM.PRODRATE` | `CambTelpayProdSumm_Prodrate` |  |  |  |
| 30 | `CAMB.TP.PRD.SUM.LINE.OF.CREDIT` | `CambTelpayProdSumm_LineOfCredit` |  |  |  |
| 31 | `CAMB.TP.PRD.SUM.HOLD.AMOUNT` | `CambTelpayProdSumm_HoldAmount` |  |  |  |
| 32 | `CAMB.TP.PRD.SUM.MSG.ASOFDATE` | `CambTelpayProdSumm_MsgAsofdate` |  |  |  |
| 33 | `CAMB.TP.PRD.SUM.MSG.EXTRA` | `CambTelpayProdSumm_MsgExtra` |  |  |  |
| 34 | `CAMB.TP.PRD.SUM.MSG.REC.ID` | `CambTelpayProdSumm_MsgRecId` |  |  |  |
| 35 | `CAMB.TP.PRD.SUM.MSG.NO.ITEMS` | `CambTelpayProdSumm_MsgNoItems` |  |  |  |
