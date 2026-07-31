# FS.GI.RECEIPT.MATCH.GROUPS — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.MATCH.GROUPS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.STATUS` | `FsGiReceiptMatchGroups_MatchGroupStatus` |  |  |  |
| 2 | `GI.REC.MATCH.GROUPS.DATE.OF.MATCHING` | `FsGiReceiptMatchGroups_DateOfMatching` |  |  |  |
| 3 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.ID` | `FsGiReceiptMatchGroups_MatchGroupId` |  |  |  |
| 4 | `GI.REC.MATCH.GROUPS.MATCHING.METHOD` | `FsGiReceiptMatchGroups_MatchingMethod` |  |  |  |
| 5 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.MAKER` | `FsGiReceiptMatchGroups_MatchGroupMaker` |  |  |  |
| 6 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.CHECKER` | `FsGiReceiptMatchGroups_MatchGroupChecker` |  |  |  |
| 7 | `GI.REC.MATCH.GROUPS.REMITTER.CHECK.STATUS` | `FsGiReceiptMatchGroups_RemitterCheckStatus` |  |  |  |
| 8 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.SETTLEMENT.METHOD` | `FsGiReceiptMatchGroups_MatchGroupSettlementMethod` |  |  |  |
| 9 | `GI.REC.MATCH.GROUPS.SETTLEMENT.DATE` | `FsGiReceiptMatchGroups_SettlementDate` |  |  |  |
| 10 | `GI.REC.MATCH.GROUPS.FORCED.TRADE.DATE` | `FsGiReceiptMatchGroups_ForcedTradeDate` |  |  |  |
| 11 | `GI.REC.MATCH.GROUPS.NEXT.STATUS` | `FsGiReceiptMatchGroups_NextStatus` |  |  |  |
| 12 | `GI.REC.MATCH.GROUPS.COLLECTION.ACCOUNT.GROUP` | `FsGiReceiptMatchGroups_CollectionAccountGroup` |  |  |  |
| 13 | `GI.REC.MATCH.GROUPS.RECEIPT.CURRENCY` | `FsGiReceiptMatchGroups_ReceiptCurrency` |  |  |  |
| 14 | `GI.REC.MATCH.GROUPS.TOLERANCE.AMOUNT` | `FsGiReceiptMatchGroups_ToleranceAmount` |  |  |  |
| 15 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.MAKER.DATE` | `FsGiReceiptMatchGroups_MatchGroupMakerDate` |  |  |  |
| 16 | `GI.REC.MATCH.GROUPS.MATCH.GROUP.CHECKER.DATE` | `FsGiReceiptMatchGroups_MatchGroupCheckerDate` |  |  |  |
| 17 | `GI.REC.MATCH.GROUPS.MATCH.GRP.APPROVAL.CHECKER1` | `FsGiReceiptMatchGroups_MatchGrpApprovalChecker1` |  |  |  |
| 18 | `GI.REC.MATCH.GROUPS.MATCH.GRP.APPROV.CHECKER1.DATE` | `FsGiReceiptMatchGroups_MatchGrpApprovChecker1Date` |  |  |  |
| 19 | `GI.REC.MATCH.GROUPS.MEMO` | `FsGiReceiptMatchGroups_Memo` |  |  |  |
| 20 | `GI.REC.MATCH.GROUPS.PROCESS.FLAG` | `FsGiReceiptMatchGroups_ProcessFlag` |  |  |  |
| 21 | `GI.REC.MATCH.GROUPS.PROCESS.DATE` | `FsGiReceiptMatchGroups_ProcessDate` |  |  |  |
| 22 | `GI.REC.MATCH.GROUPS.REMITTER.CHECKS.ID` | `FsGiReceiptMatchGroups_RemitterChecksId` |  |  |  |
| 23 | `GI.REC.MATCH.GROUPS.UNMATCH.GROUP.MAKER` | `FsGiReceiptMatchGroups_UnmatchGroupMaker` |  |  |  |
| 24 | `GI.REC.MATCH.GROUPS.UNMATCH.GROUP.CHECKER` | `FsGiReceiptMatchGroups_UnmatchGroupChecker` |  |  |  |
| 25 | `GI.REC.MATCH.GROUPS.UNMATCH.GROUP.DATE.TIME` | `FsGiReceiptMatchGroups_UnmatchGroupDateTime` |  |  |  |
| 26 | `GI.REC.MATCH.GROUPS.UNMATCH.GRP.CHECKER.DATE.TIME` | `FsGiReceiptMatchGroups_UnmatchGrpCheckerDateTime` |  |  |  |
| 27 | `GI.REC.MATCH.GROUPS.PARTIAL.UNMATCH.GROUP.MAKER` | `FsGiReceiptMatchGroups_PartialUnmatchGroupMaker` |  |  |  |
| 28 | `GI.REC.MATCH.GROUPS.PARTIAL.UNMATCH.GROUP.CHECKER` | `FsGiReceiptMatchGroups_PartialUnmatchGroupChecker` |  |  |  |
| 29 | `GI.REC.MATCH.GROUPS.PARTIAL.UNMATCH.GRP.DATE.TIME` | `FsGiReceiptMatchGroups_PartialUnmatchGrpDateTime` |  |  |  |
| 30 | `GI.REC.MATCH.GROUPS.PARTIAL.UNMATCH.GRP.CHECKER.DT` | `FsGiReceiptMatchGroups_PartialUnmatchGrpCheckerDt` |  |  |  |
| 31 | `GI.REC.MATCH.GROUPS.RESERVED10` | `FsGiReceiptMatchGroups_Reserved10` |  |  |  |
| 32 | `GI.REC.MATCH.GROUPS.RESERVED9` | `FsGiReceiptMatchGroups_Reserved9` |  |  |  |
| 33 | `GI.REC.MATCH.GROUPS.RESERVED8` | `FsGiReceiptMatchGroups_Reserved8` |  |  |  |
| 34 | `GI.REC.MATCH.GROUPS.RESERVED7` | `FsGiReceiptMatchGroups_Reserved7` |  |  |  |
| 35 | `GI.REC.MATCH.GROUPS.RESERVED6` | `FsGiReceiptMatchGroups_Reserved6` |  |  |  |
| 36 | `GI.REC.MATCH.GROUPS.RESERVED5` | `FsGiReceiptMatchGroups_Reserved5` |  |  |  |
| 37 | `GI.REC.MATCH.GROUPS.RESERVED4` | `FsGiReceiptMatchGroups_Reserved4` |  |  |  |
| 38 | `GI.REC.MATCH.GROUPS.RESERVED3` | `FsGiReceiptMatchGroups_Reserved3` |  |  |  |
| 39 | `GI.REC.MATCH.GROUPS.RESERVED2` | `FsGiReceiptMatchGroups_Reserved2` |  |  |  |
| 40 | `GI.REC.MATCH.GROUPS.RESERVED1` | `FsGiReceiptMatchGroups_Reserved1` |  |  |  |
| 41 | `GI.REC.MATCH.GROUPS.LOCAL.REF` | `FsGiReceiptMatchGroups_LocalRef` |  |  |  |
| 42 | `GI.REC.MATCH.GROUPS.OVERRIDE` | `FsGiReceiptMatchGroups_Override` |  |  |  |
| 43 | `GI.REC.MATCH.GROUPS.RECORD.STATUS` | `FsGiReceiptMatchGroups_RecordStatus` |  |  |  |
| 44 | `GI.REC.MATCH.GROUPS.CURR.NO` | `FsGiReceiptMatchGroups_CurrNo` |  |  |  |
| 45 | `GI.REC.MATCH.GROUPS.INPUTTER` | `FsGiReceiptMatchGroups_Inputter` |  |  |  |
| 46 | `GI.REC.MATCH.GROUPS.DATE.TIME` | `FsGiReceiptMatchGroups_DateTime` |  |  |  |
| 47 | `GI.REC.MATCH.GROUPS.AUTHORISER` | `FsGiReceiptMatchGroups_Authoriser` |  |  |  |
| 48 | `GI.REC.MATCH.GROUPS.CO.CODE` | `FsGiReceiptMatchGroups_CoCode` |  |  |  |
| 49 | `GI.REC.MATCH.GROUPS.DEPT.CODE` | `FsGiReceiptMatchGroups_DeptCode` |  |  |  |
| 50 | `GI.REC.MATCH.GROUPS.AUDITOR.CODE` | `FsGiReceiptMatchGroups_AuditorCode` |  |  |  |
| 51 | `GI.REC.MATCH.GROUPS.AUDIT.DATE.TIME` | `FsGiReceiptMatchGroups_AuditDateTime` |  |  |  |
