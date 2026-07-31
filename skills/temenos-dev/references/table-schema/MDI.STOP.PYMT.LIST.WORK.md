# MDI.STOP.PYMT.LIST.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.STOP.PYMT.LIST.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.STOP.PYMT.ITEM.REQ` | `MdiStopPymtListWork_ItemReq` |  |  |  |
| 2 | `MDI.STOP.PYMT.ITEM.SENT` | `MdiStopPymtListWork_ItemSent` |  |  |  |
| 3 | `MDI.STOP.PYMT.MORE.FLAG` | `MdiStopPymtListWork_MoreFlag` |  |  |  |
| 4 | `MDI.STOP.PYMT.MEMBER.NO` | `MdiStopPymtListWork_MemberNo` |  |  |  |
| 5 | `MDI.STOP.PYMT.OCC.NO` | `MdiStopPymtListWork_OccNo` |  |  |  |
| 6 | `MDI.STOP.PYMT.SEQ.NO` | `MdiStopPymtListWork_SeqNo` |  |  |  |
| 7 | `MDI.STOP.PYMT.PROD.TYPE` | `MdiStopPymtListWork_ProdType` |  |  |  |
| 8 | `MDI.STOP.PYMT.PROD.ID` | `MdiStopPymtListWork_ProdId` |  |  |  |
| 9 | `MDI.STOP.PYMT.EFFECTIVE.DATE` | `MdiStopPymtListWork_EffectiveDate` |  |  |  |
| 10 | `MDI.STOP.PYMT.EXPIRY.DATE` | `MdiStopPymtListWork_ExpiryDate` |  |  |  |
| 11 | `MDI.STOP.PYMT.TRANS.TYPE` | `MdiStopPymtListWork_TransType` |  |  |  |
| 12 | `MDI.STOP.PYMT.STOP.REASON` | `MdiStopPymtListWork_StopReason` |  |  |  |
| 13 | `MDI.STOP.PYMT.CHQ.NUMBER` | `MdiStopPymtListWork_ChqNumber` |  |  |  |
| 14 | `MDI.STOP.PYMT.CHQ.DATE` | `MdiStopPymtListWork_ChqDate` |  |  |  |
| 15 | `MDI.STOP.PYMT.CHQ.AMOUNT` | `MdiStopPymtListWork_ChqAmount` |  |  |  |
| 16 | `MDI.STOP.PYMT.PAYEE.NAME1` | `MdiStopPymtListWork_PayeeName1` |  |  |  |
| 17 | `MDI.STOP.PYMT.PAYEE.NAME2` | `MdiStopPymtListWork_PayeeName2` |  |  |  |
| 18 | `MDI.STOP.PYMT.RESERVED.10` | `MdiStopPymtListWork_Reserved10` |  |  |  |
| 19 | `MDI.STOP.PYMT.RESERVED.9` | `MdiStopPymtListWork_Reserved9` |  |  |  |
| 20 | `MDI.STOP.PYMT.RESERVED.8` | `MdiStopPymtListWork_Reserved8` |  |  |  |
| 21 | `MDI.STOP.PYMT.RESERVED.7` | `MdiStopPymtListWork_Reserved7` |  |  |  |
| 22 | `MDI.STOP.PYMT.RESERVED.6` | `MdiStopPymtListWork_Reserved6` |  |  |  |
| 23 | `MDI.STOP.PYMT.RESERVED.5` | `MdiStopPymtListWork_Reserved5` |  |  |  |
| 24 | `MDI.STOP.PYMT.RESERVED.4` | `MdiStopPymtListWork_Reserved4` |  |  |  |
| 25 | `MDI.STOP.PYMT.RESERVED.3` | `MdiStopPymtListWork_Reserved3` |  |  |  |
| 26 | `MDI.STOP.PYMT.RESERVED.2` | `MdiStopPymtListWork_Reserved2` |  |  |  |
| 27 | `MDI.STOP.PYMT.RESERVED.1` | `MdiStopPymtListWork_Reserved1` |  |  |  |
