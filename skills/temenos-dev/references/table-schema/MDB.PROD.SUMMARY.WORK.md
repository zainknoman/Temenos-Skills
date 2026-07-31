# MDB.PROD.SUMMARY.WORK — Table Schema

> Source: `INSERTS/I_F.MDB.PROD.SUMMARY.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDB.PSW.MEMBER.ID` | `MdbProdSummaryWork_MemberId` |  |  |  |
| 2 | `MDB.PSW.ITEM.REQ` | `MdbProdSummaryWork_ItemReq` |  |  |  |
| 3 | `MDB.PSW.ITEM.SENT` | `MdbProdSummaryWork_ItemSent` |  |  |  |
| 4 | `MDB.PSW.MORE.FLAG` | `MdbProdSummaryWork_MoreFlag` |  |  |  |
| 5 | `MDB.PSW.NO.OF.PROD` | `MdbProdSummaryWork_NoOfProd` |  |  |  |
| 6 | `MDB.PSW.MEMBER.BIN` | `MdbProdSummaryWork_MemberBin` |  |  |  |
| 7 | `MDB.PSW.MEMBER.BRANCH` | `MdbProdSummaryWork_MemberBranch` |  |  |  |
| 8 | `MDB.PSW.RES.MEMBER.NO` | `MdbProdSummaryWork_ResMemberNo` |  |  |  |
| 9 | `MDB.PSW.RES.PROD.CATEG` | `MdbProdSummaryWork_ResProdCateg` |  |  |  |
| 10 | `MDB.PSW.RES.PROD.CCY` | `MdbProdSummaryWork_ResProdCcy` |  |  |  |
| 11 | `MDB.PSW.RES.PROD.TYPE` | `MdbProdSummaryWork_ResProdType` |  |  |  |
| 12 | `MDB.PSW.RES.PROD.ID` | `MdbProdSummaryWork_ResProdId` |  |  |  |
| 13 | `MDB.PSW.RES.PROD.DESC` | `MdbProdSummaryWork_ResProdDesc` |  |  |  |
| 14 | `MDB.PSW.PROD.BALANCE` | `MdbProdSummaryWork_ProdBalance` |  |  |  |
| 15 | `MDB.PSW.PROD.RATE` | `MdbProdSummaryWork_ProdRate` |  |  |  |
| 16 | `MDB.PSW.LINE.OF.CREDIT` | `MdbProdSummaryWork_LineOfCredit` |  |  |  |
| 17 | `MDB.PSW.HOLD.AMOUNT` | `MdbProdSummaryWork_HoldAmount` |  |  |  |
| 18 | `MDB.PSW.RRSP.CONT.NO` | `MdbProdSummaryWork_RrspContNo` |  |  |  |
| 19 | `MDB.PSW.FILLER` | `MdbProdSummaryWork_Filler` |  |  |  |
| 20 | `MDB.PSW.ERROR.CODE` | `MdbProdSummaryWork_ErrorCode` |  |  |  |
| 21 | `MDB.PSW.ERROR.MSG` | `MdbProdSummaryWork_ErrorMsg` |  |  |  |
| 22 | `MDB.PSW.RESERVED.1` | `MdbProdSummaryWork_Reserved1` |  |  |  |
| 23 | `MDB.PSW.RESERVED.2` | `MdbProdSummaryWork_Reserved2` |  |  |  |
| 24 | `MDB.PSW.RESERVED.3` | `MdbProdSummaryWork_Reserved3` |  |  |  |
| 25 | `MDB.PSW.RESERVED.4` | `MdbProdSummaryWork_Reserved4` |  |  |  |
| 26 | `MDB.PSW.RESERVED.5` | `MdbProdSummaryWork_Reserved5` |  |  |  |
| 27 | `MDB.PSW.RESERVED.6` | `MdbProdSummaryWork_Reserved6` |  |  |  |
| 28 | `MDB.PSW.RESERVED.7` | `MdbProdSummaryWork_Reserved7` |  |  |  |
| 29 | `MDB.PSW.RESERVED.8` | `MdbProdSummaryWork_Reserved8` |  |  |  |
| 30 | `MDB.PSW.RESERVED.9` | `MdbProdSummaryWork_Reserved9` |  |  |  |
| 31 | `MDB.PSW.RESERVED.10` | `MdbProdSummaryWork_Reserved10` |  |  |  |
| 32 | `MDB.PSW.LOCAL.REF` | `MdbProdSummaryWork_LocalRef` |  |  |  |
| 33 | `MDB.PSW.OVERRIDES` | `MdbProdSummaryWork_Overrides` |  |  |  |
