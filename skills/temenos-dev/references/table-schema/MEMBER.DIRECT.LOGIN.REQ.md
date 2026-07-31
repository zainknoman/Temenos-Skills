# MEMBER.DIRECT.LOGIN.REQ — Table Schema

> Source: `INSERTS/I_F.MEMBER.DIRECT.LOGIN.REQ` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MEMDIR.LR.SHORT.DESCRP` | `MemberDirectLoginReq_ShortDescrp` |  |  |  |
| 2 | `MEMDIR.LR.DESCRIPTION` | `MemberDirectLoginReq_Description` |  |  |  |
| 3 | `MEMDIR.LR.INCOMING.BIN` | `MemberDirectLoginReq_IncomingBin` | TField |  |  |
| 4 | `MEMDIR.LR.MESSAGE.SEQ` | `MemberDirectLoginReq_MessageSeq` | TField |  |  |
| 5 | `MEMDIR.LR.TRANS.DT.TIME` | `MemberDirectLoginReq_TransDtTime` | TField |  |  |
| 6 | `MEMDIR.LR.SYS.TRACE` | `MemberDirectLoginReq_SysTrace` | TField |  |  |
| 7 | `MEMDIR.LR.DISCLAIMER.FLAG` | `MemberDirectLoginReq_DisclaimerFlag` | TField |  |  |
| 8 | `MEMDIR.LR.PAC` | `MemberDirectLoginReq_Pac` | TField |  |  |
| 9 | `MEMDIR.LR.NETWORK.ID` | `MemberDirectLoginReq_NetworkId` | TField |  |  |
| 10 | `MEMDIR.LR.ERROR.MSG` | `MemberDirectLoginReq_ErrorMsg` | TField |  |  |
| 11 | `MEMDIR.LR.RESPONSE` | `MemberDirectLoginReq_Response` | TField |  |  |
| 12 | `MEMDIR.LR.UMID` | `MemberDirectLoginReq_Umid` | TField |  |  |
| 13 | `MEMDIR.LR.CNT.MEMBERSHIP` | `MemberDirectLoginReq_CntMembership` | TField |  |  |
| 14 | `MEMDIR.LR.BIN` | `MemberDirectLoginReq_Bin` |  |  |  |
| 15 | `MEMDIR.LR.BRANCH` | `MemberDirectLoginReq_Branch` |  |  |  |
| 16 | `MEMDIR.LR.MEMBER.NO` | `MemberDirectLoginReq_MemberNo` |  |  |  |
| 17 | `MEMDIR.LR.NO.OF.MEM` | `MemberDirectLoginReq_NoOfMem` |  |  |  |
| 18 | `MEMDIR.LR.MEMBER.NAME` | `MemberDirectLoginReq_MemberName` |  |  |  |
| 19 | `MEMDIR.LR.BIRTH.DATE` | `MemberDirectLoginReq_BirthDate` |  |  |  |
| 20 | `MEMDIR.LR.BENEFIT.TYPE` | `MemberDirectLoginReq_BenefitType` |  |  |  |
| 21 | `MEMDIR.LR.MESSAGE.IND` | `MemberDirectLoginReq_MessageInd` |  |  |  |
| 22 | `MEMDIR.LR.FILLER` | `MemberDirectLoginReq_Filler` |  |  |  |
| 23 | `MEMDIR.LR.PAN.NO` | `MemberDirectLoginReq_PanNo` | TField |  |  |
| 24 | `MEMDIR.LR.MEMBERSHIP.TYPE` | `MemberDirectLoginReq_MembershipType` | TField |  |  |
| 25 | `MEMDIR.LR.UMID.OF.BC` | `MemberDirectLoginReq_UmidOfBc` | TField |  |  |
| 26 | `MEMDIR.LR.NAME.OF.BC` | `MemberDirectLoginReq_NameOfBc` | TField |  |  |
| 27 | `MEMDIR.LR.RESERVED.6` | `MemberDirectLoginReq_Reserved6` | TField |  |  |
| 28 | `MEMDIR.LR.RESERVED.5` | `MemberDirectLoginReq_Reserved5` | TField |  |  |
| 29 | `MEMDIR.LR.RESERVED.4` | `MemberDirectLoginReq_Reserved4` | TField |  |  |
| 30 | `MEMDIR.LR.RESERVED.3` | `MemberDirectLoginReq_Reserved3` | TField |  |  |
| 31 | `MEMDIR.LR.RESERVED.2` | `MemberDirectLoginReq_Reserved2` | TField |  |  |
| 32 | `MEMDIR.LR.RESERVED.1` | `MemberDirectLoginReq_Reserved1` | TField |  |  |
| 33 | `MEMDIR.LR.LOCAL.REF` | `MemberDirectLoginReq_LocalRef` |  |  |  |
| 34 | `MEMDIR.LR.OVERRIDE` | `MemberDirectLoginReq_Override` |  |  |  |
| 35 | `MEMDIR.LR.RECORD.STATUS` | `MemberDirectLoginReq_RecordStatus` | String |  |  |
| 36 | `MEMDIR.LR.CURR.NO` | `MemberDirectLoginReq_CurrNo` | String |  |  |
| 37 | `MEMDIR.LR.INPUTTER` | `MemberDirectLoginReq_Inputter` |  |  |  |
| 38 | `MEMDIR.LR.DATE.TIME` | `MemberDirectLoginReq_DateTime` |  |  |  |
| 39 | `MEMDIR.LR.AUTHORISER` | `MemberDirectLoginReq_Authoriser` | String |  |  |
| 40 | `MEMDIR.LR.CO.CODE` | `MemberDirectLoginReq_CoCode` | String |  |  |
| 41 | `MEMDIR.LR.DEPT.CODE` | `MemberDirectLoginReq_DeptCode` | String |  |  |
| 42 | `MEMDIR.LR.AUDITOR.CODE` | `MemberDirectLoginReq_AuditorCode` | String |  |  |
| 43 | `MEMDIR.LR.AUDIT.DATE.TIME` | `MemberDirectLoginReq_AuditDateTime` | String |  |  |
