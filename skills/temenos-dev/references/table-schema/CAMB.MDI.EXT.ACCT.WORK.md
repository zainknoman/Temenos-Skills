# CAMB.MDI.EXT.ACCT.WORK — Table Schema

> Source: `INSERTS/I_F.CAMB.MDI.EXT.ACCT.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.MDI.EXTACCT.ITEM.REQ` | `CambMdiExtAcctWork_ItemReq` |  |  |  |
| 2 | `CAMB.MDI.EXTACCT.ITEM.SENT` | `CambMdiExtAcctWork_ItemSent` |  |  |  |
| 3 | `CAMB.MDI.EXTACCT.SRCH.ITEM` | `CambMdiExtAcctWork_SrchItem` |  |  |  |
| 4 | `CAMB.MDI.EXTACCT.MORE.FLAG` | `CambMdiExtAcctWork_MoreFlag` |  |  |  |
| 5 | `CAMB.MDI.EXTACCT.BIN` | `CambMdiExtAcctWork_Bin` |  |  |  |
| 6 | `CAMB.MDI.EXTACCT.BRANCH` | `CambMdiExtAcctWork_Branch` |  |  |  |
| 7 | `CAMB.MDI.EXTACCT.MEMBER.NUMBER` | `CambMdiExtAcctWork_MemberNumber` |  |  |  |
| 8 | `CAMB.MDI.EXTACCT.OCC.NUMBER` | `CambMdiExtAcctWork_OccNumber` |  |  |  |
| 9 | `CAMB.MDI.EXTACCT.EXT.ACCT.CNT` | `CambMdiExtAcctWork_ExtAcctCnt` |  |  |  |
| 10 | `CAMB.MDI.EXTACCT.EXT.ACCT` | `CambMdiExtAcctWork_ExtAcct` |  |  |  |
| 11 | `CAMB.MDI.EXTACCT.EXT.ACCT.ID` | `CambMdiExtAcctWork_ExtAcctId` |  |  |  |
| 12 | `CAMB.MDI.EXTACCT.ACCT.FORMAT.CODE` | `CambMdiExtAcctWork_AcctFormatCode` |  |  |  |
| 13 | `CAMB.MDI.EXTACCT.EXT.OCC.NO` | `CambMdiExtAcctWork_ExtOccNo` |  |  |  |
| 14 | `CAMB.MDI.EXTACCT.ACCT.NUMBER` | `CambMdiExtAcctWork_AcctNumber` |  |  |  |
| 15 | `CAMB.MDI.EXTACCT.CCY.CODE` | `CambMdiExtAcctWork_CcyCode` |  |  |  |
| 16 | `CAMB.MDI.EXTACCT.DESCRIPTION` | `CambMdiExtAcctWork_Description` |  |  |  |
| 17 | `CAMB.MDI.EXTACCT.TF.TO.FLAG` | `CambMdiExtAcctWork_TfToFlag` |  |  |  |
| 18 | `CAMB.MDI.EXTACCT.TF.FR.FLAG` | `CambMdiExtAcctWork_TfFrFlag` |  |  |  |
| 19 | `CAMB.MDI.EXTACCT.PAYEE.NAME` | `CambMdiExtAcctWork_PayeeName` |  |  |  |
| 20 | `CAMB.MDI.EXTACCT.FILLER.ADD1` | `CambMdiExtAcctWork_FillerAdd1` |  |  |  |
| 21 | `CAMB.MDI.EXTACCT.FILLER.ADD2` | `CambMdiExtAcctWork_FillerAdd2` |  |  |  |
| 22 | `CAMB.MDI.EXTACCT.FILLER.ADD3` | `CambMdiExtAcctWork_FillerAdd3` |  |  |  |
| 23 | `CAMB.MDI.EXTACCT.FILLER.ADD4` | `CambMdiExtAcctWork_FillerAdd4` |  |  |  |
| 24 | `CAMB.MDI.EXTACCT.FILLER.ADD5` | `CambMdiExtAcctWork_FillerAdd5` |  |  |  |
| 25 | `CAMB.MDI.EXTACCT.ACCT.STATUS.FLAG` | `CambMdiExtAcctWork_AcctStatusFlag` |  |  |  |
| 26 | `CAMB.MDI.EXTACCT.ACCOUNT.TYPE` | `CambMdiExtAcctWork_AccountType` |  |  |  |
| 27 | `CAMB.MDI.EXTACCT.RESERVED.4` | `CambMdiExtAcctWork_Reserved4` |  |  |  |
| 28 | `CAMB.MDI.EXTACCT.RESERVED.3` | `CambMdiExtAcctWork_Reserved3` |  |  |  |
| 29 | `CAMB.MDI.EXTACCT.RESERVED.2` | `CambMdiExtAcctWork_Reserved2` |  |  |  |
| 30 | `CAMB.MDI.EXTACCT.RESERVED.1` | `CambMdiExtAcctWork_Reserved1` |  |  |  |
