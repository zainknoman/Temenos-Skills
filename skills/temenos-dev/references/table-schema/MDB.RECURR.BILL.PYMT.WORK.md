# MDB.RECURR.BILL.PYMT.WORK — Table Schema

> Source: `INSERTS/I_F.MDB.RECURR.BILL.PYMT.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDB.RBPW.ITEM.REQ` | `MdbRecurrBillPymtWork_ItemReq` |  |  |  |
| 2 | `MDB.RBPW.ITEM.SENT` | `MdbRecurrBillPymtWork_ItemSent` |  |  |  |
| 3 | `MDB.RBPW.MORE.FLAG` | `MdbRecurrBillPymtWork_MoreFlag` |  |  |  |
| 4 | `MDB.RBPW.MEMBER.NO` | `MdbRecurrBillPymtWork_MemberNo` |  |  |  |
| 5 | `MDB.RBPW.MEMBER.BIN` | `MdbRecurrBillPymtWork_MemberBin` |  |  |  |
| 6 | `MDB.RBPW.MEMBER.BRANCH` | `MdbRecurrBillPymtWork_MemberBranch` |  |  |  |
| 7 | `MDB.RBPW.CNT.OF.PYMT` | `MdbRecurrBillPymtWork_CntOfPymt` |  |  |  |
| 8 | `MDB.RBPW.VENDOR.ID` | `MdbRecurrBillPymtWork_VendorId` |  |  |  |
| 9 | `MDB.RBPW.VENDOR.AC.NO` | `MdbRecurrBillPymtWork_VendorAcNo` |  |  |  |
| 10 | `MDB.RBPW.LONG.DESC` | `MdbRecurrBillPymtWork_LongDesc` |  |  |  |
| 11 | `MDB.RBPW.SRC.BIN` | `MdbRecurrBillPymtWork_SrcBin` |  |  |  |
| 12 | `MDB.RBPW.SRC.BRANCH` | `MdbRecurrBillPymtWork_SrcBranch` |  |  |  |
| 13 | `MDB.RBPW.SRC.MEMBER` | `MdbRecurrBillPymtWork_SrcMember` |  |  |  |
| 14 | `MDB.RBPW.SRC.PRD.TYPE` | `MdbRecurrBillPymtWork_SrcPrdType` |  |  |  |
| 15 | `MDB.RBPW.SRC.PRD.ID` | `MdbRecurrBillPymtWork_SrcPrdId` |  |  |  |
| 16 | `MDB.RBPW.EFF.DATE` | `MdbRecurrBillPymtWork_EffDate` |  |  |  |
| 17 | `MDB.RBPW.ENTRY.DATE` | `MdbRecurrBillPymtWork_EntryDate` |  |  |  |
| 18 | `MDB.RBPW.NEXT.PYMT.DATE` | `MdbRecurrBillPymtWork_NextPymtDate` |  |  |  |
| 19 | `MDB.RBPW.EXPIRY.DATE` | `MdbRecurrBillPymtWork_ExpiryDate` |  |  |  |
| 20 | `MDB.RBPW.AMOUNT` | `MdbRecurrBillPymtWork_Amount` |  |  |  |
| 21 | `MDB.RBPW.ORG.TRACE.NO` | `MdbRecurrBillPymtWork_OrgTraceNo` |  |  |  |
| 22 | `MDB.RBPW.FREQ.LEN` | `MdbRecurrBillPymtWork_FreqLen` |  |  |  |
| 23 | `MDB.RBPW.FREQ.PERIOD` | `MdbRecurrBillPymtWork_FreqPeriod` |  |  |  |
| 24 | `MDB.RBPW.RESERVED.1` | `MdbRecurrBillPymtWork_Reserved1` |  |  |  |
| 25 | `MDB.RBPW.RESERVED.2` | `MdbRecurrBillPymtWork_Reserved2` |  |  |  |
| 26 | `MDB.RBPW.RESERVED.3` | `MdbRecurrBillPymtWork_Reserved3` |  |  |  |
| 27 | `MDB.RBPW.RESERVED.4` | `MdbRecurrBillPymtWork_Reserved4` |  |  |  |
| 28 | `MDB.RBPW.RESERVED.5` | `MdbRecurrBillPymtWork_Reserved5` |  |  |  |
| 29 | `MDB.RBPW.RESERVED.6` | `MdbRecurrBillPymtWork_Reserved6` |  |  |  |
| 30 | `MDB.RBPW.RESERVED.7` | `MdbRecurrBillPymtWork_Reserved7` |  |  |  |
| 31 | `MDB.RBPW.RESERVED.8` | `MdbRecurrBillPymtWork_Reserved8` |  |  |  |
| 32 | `MDB.RBPW.RESERVED.9` | `MdbRecurrBillPymtWork_Reserved9` |  |  |  |
| 33 | `MDB.RBPW.RESERVED.10` | `MdbRecurrBillPymtWork_Reserved10` |  |  |  |
| 34 | `MDB.RBPW.RESERVED.11` | `MdbRecurrBillPymtWork_Reserved11` |  |  |  |
| 35 | `MDB.RBPW.RESERVED.12` | `MdbRecurrBillPymtWork_Reserved12` |  |  |  |
| 36 | `MDB.RBPW.RESERVED.13` | `MdbRecurrBillPymtWork_Reserved13` |  |  |  |
| 37 | `MDB.RBPW.RESERVED.14` | `MdbRecurrBillPymtWork_Reserved14` |  |  |  |
| 38 | `MDB.RBPW.RESERVED.15` | `MdbRecurrBillPymtWork_Reserved15` |  |  |  |
| 39 | `MDB.RBPW.LOCAL.REF` | `MdbRecurrBillPymtWork_LocalRef` |  |  |  |
| 40 | `MDB.RBPW.OVERRIDES` | `MdbRecurrBillPymtWork_Overrides` |  |  |  |
