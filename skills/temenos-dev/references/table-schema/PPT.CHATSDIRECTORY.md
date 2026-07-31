# PPT.CHATSDIRECTORY — Table Schema

> Source: `INSERTS/I_F.PPT.CHATSDIRECTORY` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTCD.ChatsDirectoryID` | `PptChatsdirectory_Chatsdirectoryid` |  |  |  |
| 2 | `PPTCD.CompanyID` | `PptChatsdirectory_Companyid` |  |  |  |
| 3 | `PPTCD.MemberIdentifierBIC` | `PptChatsdirectory_Memberidentifierbic` |  |  |  |
| 4 | `PPTCD.ClearingCode` | `PptChatsdirectory_Clearingcode` |  |  |  |
| 5 | `PPTCD.CurrencyCode` | `PptChatsdirectory_Currencycode` |  |  |  |
| 6 | `PPTCD.TargetBankBIC` | `PptChatsdirectory_Targetbankbic` |  |  |  |
| 7 | `PPTCD.StartDateCHATSDirectory` | `PptChatsdirectory_Startdatechatsdirectory` |  |  |  |
| 8 | `PPTCD.InstitutionName` | `PptChatsdirectory_Institutionname` |  |  |  |
| 9 | `PPTCD.ParticipationType` | `PptChatsdirectory_Participationtype` |  |  |  |
| 10 | `PPTCD.DirectParticipantIdentifier` | `PptChatsdirectory_Directparticipantidentifier` |  |  |  |
| 11 | `PPTCD.ClearingCodeTargetBank` | `PptChatsdirectory_Clearingcodetargetbank` |  |  |  |
| 12 | `PPTCD.ClearingCodeMemberBank` | `PptChatsdirectory_Clearingcodememberbank` |  |  |  |
| 13 | `PPTCD.EndDateCHATSDirectory` | `PptChatsdirectory_Enddatechatsdirectory` |  |  |  |
| 14 | `PPTCD.RACCHATSDirectory` | `PptChatsdirectory_Racchatsdirectory` |  |  |  |
| 15 | `PPTCD.RSCCHATSDirectory` | `PptChatsdirectory_Rscchatsdirectory` |  |  |  |
| 16 | `PPTCD.EntryUserID` | `PptChatsdirectory_Entryuserid` |  |  |  |
| 17 | `PPTCD.EntryDateTime` | `PptChatsdirectory_Entrydatetime` |  |  |  |
| 18 | `PPTCD.ApproverUserID` | `PptChatsdirectory_Approveruserid` |  |  |  |
| 19 | `PPTCD.ApprovedDateTime` | `PptChatsdirectory_Approveddatetime` |  |  |  |
| 20 | `PPTCD.OverrideThroughUpload` | `PptChatsdirectory_Overridethroughupload` |  |  |  |
