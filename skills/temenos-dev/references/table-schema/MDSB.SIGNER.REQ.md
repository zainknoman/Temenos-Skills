# MDSB.SIGNER.REQ — Table Schema

> Source: `INSERTS/I_F.MDSB.SIGNER.REQ` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDSB.SR.INCOMING.BIN` | `MdsbSignerReq_IncomingBin` |  |  |  |
| 2 | `MDSB.SR.MESSAGE.SEQ` | `MdsbSignerReq_MessageSeq` |  |  |  |
| 3 | `MDSB.SR.TRANS.DT.TIME` | `MdsbSignerReq_TransDtTime` |  |  |  |
| 4 | `MDSB.SR.SYS.TRACE` | `MdsbSignerReq_SysTrace` |  |  |  |
| 5 | `MDSB.SR.PAN` | `MdsbSignerReq_Pan` |  |  |  |
| 6 | `MDSB.SR.PROCESSING.CODE` | `MdsbSignerReq_ProcessingCode` |  |  |  |
| 7 | `MDSB.SR.SIGNER.BLOCK` | `MdsbSignerReq_SignerBlock` |  |  |  |
| 8 | `MDSB.SR.NETWORK.ID` | `MdsbSignerReq_NetworkId` |  |  |  |
| 9 | `MDSB.SR.PRIMARY.MEMBER` | `MdsbSignerReq_PrimaryMember` |  |  |  |
| 10 | `MDSB.SR.CNT.MEMBERSHIP` | `MdsbSignerReq_CntMembership` |  |  |  |
| 11 | `MDSB.SR.BIN` | `MdsbSignerReq_Bin` |  |  |  |
| 12 | `MDSB.SR.BRANCH` | `MdsbSignerReq_Branch` |  |  |  |
| 13 | `MDSB.SR.MEMBER.ID` | `MdsbSignerReq_MemberId` |  |  |  |
| 14 | `MDSB.SR.BUSINESS.ID` | `MdsbSignerReq_BusinessId` |  |  |  |
| 15 | `MDSB.SR.BUSINESS.NAME` | `MdsbSignerReq_BusinessName` |  |  |  |
| 16 | `MDSB.SR.NO.OF.PRODUCTS` | `MdsbSignerReq_NoOfProducts` |  |  |  |
| 17 | `MDSB.SR.CATEGORY` | `MdsbSignerReq_Category` |  |  |  |
| 18 | `MDSB.SR.CURRENCY` | `MdsbSignerReq_Currency` |  |  |  |
| 19 | `MDSB.SR.PRODUCT.TYPE` | `MdsbSignerReq_ProductType` |  |  |  |
| 20 | `MDSB.SR.PRODUCT.ID` | `MdsbSignerReq_ProductId` |  |  |  |
| 21 | `MDSB.SR.NO.OF.SIGNERS` | `MdsbSignerReq_NoOfSigners` |  |  |  |
| 22 | `MDSB.SR.SIGNER.UMID` | `MdsbSignerReq_SignerUmid` |  |  |  |
| 23 | `MDSB.SR.SIGNER.MANDATORY` | `MdsbSignerReq_SignerMandatory` |  |  |  |
| 24 | `MDSB.SR.ITEMS.REQUESTED` | `MdsbSignerReq_ItemsRequested` |  |  |  |
| 25 | `MDSB.SR.ITEMS.RECEIVED` | `MdsbSignerReq_ItemsReceived` |  |  |  |
| 26 | `MDSB.SR.LOCAL.REF` | `MdsbSignerReq_LocalRef` |  |  |  |
| 27 | `MDSB.SR.OVERRIDE` | `MdsbSignerReq_Override` |  |  |  |
| 28 | `MDSB.SR.MORE.INDICATOR` | `MdsbSignerReq_MoreIndicator` |  |  |  |
| 29 | `MDSB.SR.RESERVED.6` | `MdsbSignerReq_Reserved6` |  |  |  |
| 30 | `MDSB.SR.RESERVED.7` | `MdsbSignerReq_Reserved7` |  |  |  |
| 31 | `MDSB.SR.RESERVED.8` | `MdsbSignerReq_Reserved8` |  |  |  |
| 32 | `MDSB.SR.RESERVED.9` | `MdsbSignerReq_Reserved9` |  |  |  |
| 33 | `MDSB.SR.RESERVED.10` | `MdsbSignerReq_Reserved10` |  |  |  |
| 34 | `MDSB.SR.RESERVED.11` | `MdsbSignerReq_Reserved11` |  |  |  |
| 35 | `MDSB.SR.RESERVED.12` | `MdsbSignerReq_Reserved12` |  |  |  |
| 36 | `MDSB.SR.RESERVED.13` | `MdsbSignerReq_Reserved13` |  |  |  |
| 37 | `MDSB.SR.RESERVED.14` | `MdsbSignerReq_Reserved14` |  |  |  |
| 38 | `MDSB.SR.RESERVED.15` | `MdsbSignerReq_Reserved15` |  |  |  |
| 39 | `MDSB.SR.RECORD.STATUS` | `MdsbSignerReq_RecordStatus` |  |  |  |
| 40 | `MDSB.SR.CURR.NO` | `MdsbSignerReq_CurrNo` |  |  |  |
| 41 | `MDSB.SR.INPUTTER` | `MdsbSignerReq_Inputter` |  |  |  |
| 42 | `MDSB.SR.DATE.TIME` | `MdsbSignerReq_DateTime` |  |  |  |
| 43 | `MDSB.SR.AUTHORISER` | `MdsbSignerReq_Authoriser` |  |  |  |
| 44 | `MDSB.SR.CO.CODE` | `MdsbSignerReq_CoCode` |  |  |  |
| 45 | `MDSB.SR.DEPT.CODE` | `MdsbSignerReq_DeptCode` |  |  |  |
| 46 | `MDSB.SR.AUDITOR.CODE` | `MdsbSignerReq_AuditorCode` |  |  |  |
| 47 | `MDSB.SR.AUDIT.DATE.TIME` | `MdsbSignerReq_AuditDateTime` |  |  |  |
