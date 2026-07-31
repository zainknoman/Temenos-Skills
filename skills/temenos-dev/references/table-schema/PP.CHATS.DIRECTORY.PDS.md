# PP.CHATS.DIRECTORY.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CHATS.DIRECTORY.PDS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.TCD.CompanyID` | `PpChatsDirectoryPds_Companyid` | TField |  |  |
| 2 | `PP.TCD.MemberIdentifierBIC` | `PpChatsDirectoryPds_Memberidentifierbic` | TField |  |  |
| 3 | `PP.TCD.ClearingCode` | `PpChatsDirectoryPds_Clearingcode` | TField |  |  |
| 4 | `PP.TCD.CurrencyCode` | `PpChatsDirectoryPds_Currencycode` | TField |  |  |
| 5 | `PP.TCD.TargetBankBIC` | `PpChatsDirectoryPds_Targetbankbic` | TField |  |  |
| 6 | `PP.TCD.InstitutionName` | `PpChatsDirectoryPds_Institutionname` | TField |  |  |
| 7 | `PP.TCD.ParticipationType` | `PpChatsDirectoryPds_Participationtype` | TField |  |  |
| 8 | `PP.TCD.DirectParticipantIdentifier` | `PpChatsDirectoryPds_Directparticipantidentifier` | TField |  |  |
| 9 | `PP.TCD.ClearingCodeTargetBank` | `PpChatsDirectoryPds_Clearingcodetargetbank` | TField |  |  |
| 10 | `PP.TCD.ClearingCodeMemberBank` | `PpChatsDirectoryPds_Clearingcodememberbank` | TField |  |  |
| 11 | `PP.TCD.OverrideThroughUpload` | `PpChatsDirectoryPds_Overridethroughupload` | TField |  |  |
| 12 | `PP.TCD.StartDate` | `PpChatsDirectoryPds_Startdate` | TField |  |  |
| 13 | `PP.TCD.EndDate` | `PpChatsDirectoryPds_Enddate` | TField |  |  |
| 14 | `PP.TCD.RESERVED.5` | `PpChatsDirectoryPds_Reserved5` | TField |  |  |
| 15 | `PP.TCD.RESERVED.4` | `PpChatsDirectoryPds_Reserved4` | TField |  |  |
| 16 | `PP.TCD.RESERVED.3` | `PpChatsDirectoryPds_Reserved3` | TField |  |  |
| 17 | `PP.TCD.RESERVED.2` | `PpChatsDirectoryPds_Reserved2` | TField |  |  |
| 18 | `PP.TCD.RESERVED.1` | `PpChatsDirectoryPds_Reserved1` | TField |  |  |
| 19 | `PP.TCD.LOCAL.REF` | `PpChatsDirectoryPds_LocalRef` |  |  |  |
| 20 | `PP.TCD.LinkID` | `PpChatsDirectoryPds_Linkid` | TField |  |  |
| 21 | `PP.TCD.OVERRIDE` | `PpChatsDirectoryPds_Override` |  |  |  |
| 22 | `PP.TCD.RECORD.STATUS` | `PpChatsDirectoryPds_RecordStatus` | String |  |  |
| 23 | `PP.TCD.CURR.NO` | `PpChatsDirectoryPds_CurrNo` | String |  |  |
| 24 | `PP.TCD.INPUTTER` | `PpChatsDirectoryPds_Inputter` |  |  |  |
| 25 | `PP.TCD.DATE.TIME` | `PpChatsDirectoryPds_DateTime` |  |  |  |
| 26 | `PP.TCD.AUTHORISER` | `PpChatsDirectoryPds_Authoriser` | String |  |  |
| 27 | `PP.TCD.CO.CODE` | `PpChatsDirectoryPds_CoCode` | String |  |  |
| 28 | `PP.TCD.DEPT.CODE` | `PpChatsDirectoryPds_DeptCode` | String |  |  |
| 29 | `PP.TCD.AUDITOR.CODE` | `PpChatsDirectoryPds_AuditorCode` | String |  |  |
| 30 | `PP.TCD.AUDIT.DATE.TIME` | `PpChatsDirectoryPds_AuditDateTime` | String |  |  |
