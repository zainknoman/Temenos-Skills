# MDI.STMT.SUMM.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.STMT.SUMM.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STMT.SUMM.ACCOUNT.NO` | `MdiStmtSummWork_AccountNo` | TField |  |  |
| 2 | `STMT.SUMM.RETRIVAL.OPTION` | `MdiStmtSummWork_RetrivalOption` | TField |  |  |
| 3 | `STMT.SUMM.ATTRIBUTE.IND` | `MdiStmtSummWork_AttributeInd` | TField |  |  |
| 4 | `STMT.SUMM.FROM.DATE` | `MdiStmtSummWork_FromDate` | TField |  |  |
| 5 | `STMT.SUMM.TO.DATE` | `MdiStmtSummWork_ToDate` | TField |  |  |
| 6 | `STMT.SUMM.SEARCH.CRITERIA` | `MdiStmtSummWork_SearchCriteria` | TField |  |  |
| 7 | `STMT.SUMM.CURRENT.END.BAL` | `MdiStmtSummWork_CurrentEndBal` | TField |  |  |
| 8 | `STMT.SUMM.ITEM.REQ` | `MdiStmtSummWork_ItemReq` | TField |  |  |
| 9 | `STMT.SUMM.ITEM.SENT` | `MdiStmtSummWork_ItemSent` | TField |  |  |
| 10 | `STMT.SUMM.MORE.FLAG` | `MdiStmtSummWork_MoreFlag` | TField |  |  |
| 11 | `STMT.SUMM.NO.OF.TXN` | `MdiStmtSummWork_NoOfTxn` | TField |  |  |
| 12 | `STMT.SUMM.EFF.DATE` | `MdiStmtSummWork_EffDate` |  |  |  |
| 13 | `STMT.SUMM.ENTRY.DATE` | `MdiStmtSummWork_EntryDate` |  |  |  |
| 14 | `STMT.SUMM.DESC.1` | `MdiStmtSummWork_Desc1` |  |  |  |
| 15 | `STMT.SUMM.DESC.2` | `MdiStmtSummWork_Desc2` |  |  |  |
| 16 | `STMT.SUMM.DESC.3` | `MdiStmtSummWork_Desc3` |  |  |  |
| 17 | `STMT.SUMM.AMOUNT` | `MdiStmtSummWork_Amount` |  |  |  |
| 18 | `STMT.SUMM.RUN.BAL` | `MdiStmtSummWork_RunBal` |  |  |  |
| 19 | `STMT.SUMM.TXN.SOURCE.CODE` | `MdiStmtSummWork_TxnSourceCode` |  |  |  |
| 20 | `STMT.SUMM.NO.OF.ATTRIBUTE` | `MdiStmtSummWork_NoOfAttribute` |  |  |  |
| 21 | `STMT.SUMM.ATTRIBUTE` | `MdiStmtSummWork_Attribute` |  |  |  |
| 22 | `STMT.SUMM.T24.STMT.ID` | `MdiStmtSummWork_T24StmtId` |  |  |  |
| 23 | `STMT.SUMM.CAPL.SE.ID` | `MdiStmtSummWork_CaplSeId` |  |  |  |
| 24 | `STMT.SUMM.TXN.RUN.BAL` | `MdiStmtSummWork_TxnRunBal` | TField |  |  |
| 25 | `STMT.SUMM.RESERVED.7` | `MdiStmtSummWork_Reserved7` | TField |  |  |
| 26 | `STMT.SUMM.RESERVED.6` | `MdiStmtSummWork_Reserved6` | TField |  |  |
| 27 | `STMT.SUMM.RESERVED.5` | `MdiStmtSummWork_Reserved5` | TField |  |  |
| 28 | `STMT.SUMM.RESERVED.4` | `MdiStmtSummWork_Reserved4` | TField |  |  |
| 29 | `STMT.SUMM.RESERVED.3` | `MdiStmtSummWork_Reserved3` | TField |  |  |
| 30 | `STMT.SUMM.RESERVED.2` | `MdiStmtSummWork_Reserved2` | TField |  |  |
| 31 | `STMT.SUMM.RESERVED.1` | `MdiStmtSummWork_Reserved1` | TField |  |  |
| 32 | `STMT.SUMM.LOCAL.REF` | `MdiStmtSummWork_LocalRef` |  |  |  |
