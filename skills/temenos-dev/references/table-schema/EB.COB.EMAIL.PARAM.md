# EB.COB.EMAIL.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.COB.EMAIL.PARAM` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COB.PRM.FROM.ID` | `EbCobEmailParam_FromId` | TField |  |  |
| 2 | `COB.PRM.TO.ID` | `EbCobEmailParam_ToId` |  |  |  |
| 3 | `COB.PRM.CC.ID` | `EbCobEmailParam_CcId` |  |  |  |
| 4 | `COB.PRM.BCC.ID` | `EbCobEmailParam_BccId` |  |  |  |
| 5 | `COB.PRM.SUBJECT` | `EbCobEmailParam_Subject` |  |  |  |
| 6 | `COB.PRM.MESSAGE.ID` | `EbCobEmailParam_MessageId` | TField |  |  |
| 7 | `COB.PRM.MESSAGE.TYPE` | `EbCobEmailParam_MessageType` | TField |  |  |
| 8 | `COB.PRM.DEFAULT.HDR.MSG` | `EbCobEmailParam_DefaultHdrMsg` |  |  |  |
| 9 | `COB.PRM.DEFAULT.FOOTER.MSG` | `EbCobEmailParam_DefaultFooterMsg` |  |  |  |
| 10 | `COB.PRM.MAIL.ACTION` | `EbCobEmailParam_MailAction` |  |  |  |
| 11 | `COB.PRM.MAIL.CONTENT` | `EbCobEmailParam_MailContent` |  |  |  |
| 12 | `COB.PRM.BATCH.COMP.TIME` | `EbCobEmailParam_BatchCompTime` | TField |  |  |
| 13 | `COB.PRM.BATCH.CHECK.COUNTER` | `EbCobEmailParam_BatchCheckCounter` | TField |  |  |
| 14 | `COB.PRM.COB.RUN.INTERVAL` | `EbCobEmailParam_CobRunInterval` | TField |  |  |
| 15 | `COB.PRM.COBAUTOM.OFS.SRC` | `EbCobEmailParam_CobautomOfsSrc` | TField |  |  |
| 16 | `COB.PRM.COBAUTOM.VERS` | `EbCobEmailParam_CobautomVers` | TField |  |  |
| 17 | `COB.PRM.COBAUTOM.USER` | `EbCobEmailParam_CobautomUser` | TField |  |  |
| 18 | `COB.PRM.ERROR.KEYWORD` | `EbCobEmailParam_ErrorKeyword` |  |  |  |
| 19 | `COB.PRM.JOBS.TO.IGNORE.CRASH` | `EbCobEmailParam_JobsToIgnoreCrash` |  |  |  |
| 20 | `COB.PRM.JOBS.TO.IGNORE.HANG` | `EbCobEmailParam_JobsToIgnoreHang` |  |  |  |
| 21 | `COB.PRM.JL.HANG.COUNTER` | `EbCobEmailParam_JlHangCounter` | TField |  |  |
| 22 | `COB.PRM.JL.CHECK.TIME` | `EbCobEmailParam_JlCheckTime` | TField |  |  |
| 23 | `COB.PRM.EB.EOD.REQD` | `EbCobEmailParam_EbEodReqd` | TField |  |  |
| 24 | `COB.PRM.RESERVED.10` | `EbCobEmailParam_Reserved10` | TField |  |  |
| 25 | `COB.PRM.RESERVED.9` | `EbCobEmailParam_Reserved9` | TField |  |  |
| 26 | `COB.PRM.RESERVED.8` | `EbCobEmailParam_Reserved8` | TField |  |  |
| 27 | `COB.PRM.RESERVED.7` | `EbCobEmailParam_Reserved7` | TField |  |  |
| 28 | `COB.PRM.RESERVED.6` | `EbCobEmailParam_Reserved6` | TField |  |  |
| 29 | `COB.PRM.RESERVED.5` | `EbCobEmailParam_Reserved5` | TField |  |  |
| 30 | `COB.PRM.RESERVED.4` | `EbCobEmailParam_Reserved4` | TField |  |  |
| 31 | `COB.PRM.RESERVED.3` | `EbCobEmailParam_Reserved3` | TField |  |  |
| 32 | `COB.PRM.RESERVED.2` | `EbCobEmailParam_Reserved2` | TField |  |  |
| 33 | `COB.PRM.RESERVED.1` | `EbCobEmailParam_Reserved1` | TField |  |  |
| 34 | `COB.PRM.LOCAL.REF` | `EbCobEmailParam_LocalRef` |  |  |  |
| 35 | `COB.PRM.OVERRIDE` | `EbCobEmailParam_Override` |  |  |  |
| 36 | `COB.PRM.RECORD.STATUS` | `EbCobEmailParam_RecordStatus` | String |  |  |
| 37 | `COB.PRM.CURR.NO` | `EbCobEmailParam_CurrNo` | String |  |  |
| 38 | `COB.PRM.INPUTTER` | `EbCobEmailParam_Inputter` |  |  |  |
| 39 | `COB.PRM.DATE.TIME` | `EbCobEmailParam_DateTime` |  |  |  |
| 40 | `COB.PRM.AUTHORISER` | `EbCobEmailParam_Authoriser` | String |  |  |
| 41 | `COB.PRM.CO.CODE` | `EbCobEmailParam_CoCode` | String |  |  |
| 42 | `COB.PRM.DEPT.CODE` | `EbCobEmailParam_DeptCode` | String |  |  |
| 43 | `COB.PRM.AUDITOR.CODE` | `EbCobEmailParam_AuditorCode` | String |  |  |
| 44 | `COB.PRM.AUDIT.DATE.TIME` | `EbCobEmailParam_AuditDateTime` | String |  |  |
