# MDI.CUS.PAYEE.LIST.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.CUS.PAYEE.LIST.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.PAYEE.ITEM.REQ` | `MdiCusPayeeListWork_ItemReq` |  |  |  |
| 2 | `MDI.PAYEE.ITEM.SENT` | `MdiCusPayeeListWork_ItemSent` |  |  |  |
| 3 | `MDI.PAYEE.MORE.FLAG` | `MdiCusPayeeListWork_MoreFlag` |  |  |  |
| 4 | `MDI.PAYEE.CNT.MEMBERS` | `MdiCusPayeeListWork_CntMembers` |  |  |  |
| 5 | `MDI.PAYEE.BIN.OWNER` | `MdiCusPayeeListWork_BinOwner` |  |  |  |
| 6 | `MDI.PAYEE.BRANCH.OWNER` | `MdiCusPayeeListWork_BranchOwner` |  |  |  |
| 7 | `MDI.PAYEE.MEMBER.OWNER` | `MdiCusPayeeListWork_MemberOwner` |  |  |  |
| 8 | `MDI.PAYEE.SUB.CNT.VENDOR` | `MdiCusPayeeListWork_SubCntVendor` |  |  |  |
| 9 | `MDI.PAYEE.VENDOR.CATEG` | `MdiCusPayeeListWork_VendorCateg` |  |  |  |
| 10 | `MDI.PAYEE.VENDOR.ID` | `MdiCusPayeeListWork_VendorId` |  |  |  |
| 11 | `MDI.PAYEE.VENDOR.ACC.NO` | `MdiCusPayeeListWork_VendorAccNo` |  |  |  |
| 12 | `MDI.PAYEE.LONG.DESC` | `MdiCusPayeeListWork_LongDesc` |  |  |  |
| 13 | `MDI.PAYEE.RESERVED.10` | `MdiCusPayeeListWork_Reserved10` |  |  |  |
| 14 | `MDI.PAYEE.RESERVED.9` | `MdiCusPayeeListWork_Reserved9` |  |  |  |
| 15 | `MDI.PAYEE.RESERVED.8` | `MdiCusPayeeListWork_Reserved8` |  |  |  |
| 16 | `MDI.PAYEE.RESERVED.7` | `MdiCusPayeeListWork_Reserved7` |  |  |  |
| 17 | `MDI.PAYEE.RESERVED.6` | `MdiCusPayeeListWork_Reserved6` |  |  |  |
| 18 | `MDI.PAYEE.RESERVED.5` | `MdiCusPayeeListWork_Reserved5` |  |  |  |
| 19 | `MDI.PAYEE.RESERVED.4` | `MdiCusPayeeListWork_Reserved4` |  |  |  |
| 20 | `MDI.PAYEE.RESERVED.3` | `MdiCusPayeeListWork_Reserved3` |  |  |  |
| 21 | `MDI.PAYEE.RESERVED.2` | `MdiCusPayeeListWork_Reserved2` |  |  |  |
| 22 | `MDI.PAYEE.RESERVED.1` | `MdiCusPayeeListWork_Reserved1` |  |  |  |
