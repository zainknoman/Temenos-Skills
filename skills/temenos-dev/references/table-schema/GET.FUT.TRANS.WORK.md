# GET.FUT.TRANS.WORK — Table Schema

> Source: `INSERTS/I_F.GET.FUT.TRANS.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FUT.TXN.WRK.MEMBER.NO` | `GetFutTransWork_MemberNo` |  |  |  |
| 2 | `FUT.TXN.WRK.ITEM.REQ` | `GetFutTransWork_ItemReq` |  |  |  |
| 3 | `FUT.TXN.WRK.ITEM.SENT` | `GetFutTransWork_ItemSent` |  |  |  |
| 4 | `FUT.TXN.WRK.MORE.FLAG` | `GetFutTransWork_MoreFlag` |  |  |  |
| 5 | `FUT.TXN.WRK.AUTO.FROM.BIN` | `GetFutTransWork_AutoFromBin` |  |  |  |
| 6 | `FUT.TXN.WRK.FROM.BRANCH.NO` | `GetFutTransWork_FromBranchNo` |  |  |  |
| 7 | `FUT.TXN.WRK.RES.MEMBER.NO` | `GetFutTransWork_ResMemberNo` |  |  |  |
| 8 | `FUT.TXN.WRK.OCC.NO` | `GetFutTransWork_OccNo` |  |  |  |
| 9 | `FUT.TXN.WRK.SEQ.NO` | `GetFutTransWork_SeqNo` |  |  |  |
| 10 | `FUT.TXN.WRK.AUTO.EFF.DATE` | `GetFutTransWork_AutoEffDate` |  |  |  |
| 11 | `FUT.TXN.WRK.AUTO.EXP.DATE` | `GetFutTransWork_AutoExpDate` |  |  |  |
| 12 | `FUT.TXN.WRK.AUTO.AMOUNT` | `GetFutTransWork_AutoAmount` |  |  |  |
| 13 | `FUT.TXN.WRK.AUTO.FROM.PROD.TYPE` | `GetFutTransWork_AutoFromProdType` |  |  |  |
| 14 | `FUT.TXN.WRK.AUTO.FROM.PROD.ID` | `GetFutTransWork_AutoFromProdId` |  |  |  |
| 15 | `FUT.TXN.WRK.FROM.CCY` | `GetFutTransWork_FromCcy` |  |  |  |
| 16 | `FUT.TXN.WRK.AUTO.TO.BIN` | `GetFutTransWork_AutoToBin` |  |  |  |
| 17 | `FUT.TXN.WRK.AUTO.TO.BRANCH.NO` | `GetFutTransWork_AutoToBranchNo` |  |  |  |
| 18 | `FUT.TXN.WRK.AUTO.TO.CUSTOMER` | `GetFutTransWork_AutoToCustomer` |  |  |  |
| 19 | `FUT.TXN.WRK.AUTO.TO.PROD.TYPE` | `GetFutTransWork_AutoToProdType` |  |  |  |
| 20 | `FUT.TXN.WRK.AUTO.TO.PROD.ID` | `GetFutTransWork_AutoToProdId` |  |  |  |
| 21 | `FUT.TXN.WRK.AUTO.TO.CCY` | `GetFutTransWork_AutoToCcy` |  |  |  |
| 22 | `FUT.TXN.WRK.AUTO.LENGTH` | `GetFutTransWork_AutoLength` |  |  |  |
| 23 | `FUT.TXN.WRK.AUTO.FQU` | `GetFutTransWork_AutoFqu` |  |  |  |
| 24 | `FUT.TXN.WRK.AUTO.DAY` | `GetFutTransWork_AutoDay` |  |  |  |
| 25 | `FUT.TXN.WRK.AUTO.DESC` | `GetFutTransWork_AutoDesc` |  |  |  |
| 26 | `FUT.TXN.WRK.NEXT.TRANS.DATE` | `GetFutTransWork_NextTransDate` |  |  |  |
| 27 | `FUT.TXN.WRK.FROM.CATEG` | `GetFutTransWork_FromCateg` |  |  |  |
| 28 | `FUT.TXN.WRK.TO.CATEG` | `GetFutTransWork_ToCateg` |  |  |  |
| 29 | `FUT.TXN.WRK.RESERVED.1` | `GetFutTransWork_Reserved1` |  |  |  |
| 30 | `FUT.TXN.WRK.RESERVED.2` | `GetFutTransWork_Reserved2` |  |  |  |
| 31 | `FUT.TXN.WRK.RESERVED.3` | `GetFutTransWork_Reserved3` |  |  |  |
| 32 | `FUT.TXN.WRK.RESERVED.4` | `GetFutTransWork_Reserved4` |  |  |  |
| 33 | `FUT.TXN.WRK.RESERVED.5` | `GetFutTransWork_Reserved5` |  |  |  |
| 34 | `FUT.TXN.WRK.RESERVED.6` | `GetFutTransWork_Reserved6` |  |  |  |
| 35 | `FUT.TXN.WRK.RESERVED.7` | `GetFutTransWork_Reserved7` |  |  |  |
| 36 | `FUT.TXN.WRK.RESERVED.8` | `GetFutTransWork_Reserved8` |  |  |  |
| 37 | `FUT.TXN.WRK.RESERVED.9` | `GetFutTransWork_Reserved9` |  |  |  |
| 38 | `FUT.TXN.WRK.RESERVED.10` | `GetFutTransWork_Reserved10` |  |  |  |
