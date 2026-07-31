# US.STMT.HANDOFF — Table Schema

> Source: `INSERTS/I_F.US.STMT.HANDOFF` in `USRETL_CombinedStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.CST.FROM.DATE` | `UsStmtHandoff_FromDate` | TField |  | Not Used |
| 2 | `US.CST.TO.DATE` | `UsStmtHandoff_ToDate` | TField |  | Not Used |
| 3 | `US.CST.COMBINED.ID` | `UsStmtHandoff_CombinedId` | TField |  | Not Used |
| 4 | `US.CST.IMAGE.COUNT` | `UsStmtHandoff_ImageCount` | TField |  | Not Used |
| 5 | `US.CST.APYE` | `UsStmtHandoff_Apye` | TField |  | Not Used |
| 6 | `US.CST.INTEREST.EARNED` | `UsStmtHandoff_InterestEarned` | TField |  | Not Used |
| 7 | `US.CST.PRODUCT.NAME` | `UsStmtHandoff_ProductName` | TField |  | Not Used |
| 8 | `US.CST.OD.COUNT` | `UsStmtHandoff_OdCount` | TField |  | Not Used |
| 9 | `US.CST.OD.PERIOD` | `UsStmtHandoff_OdPeriod` | TField |  | Not Used |
| 10 | `US.CST.OD.YTD` | `UsStmtHandoff_OdYtd` | TField |  | Not Used |
| 11 | `US.CST.NFS.PERIOD` | `UsStmtHandoff_NfsPeriod` | TField |  | Not Used |
| 12 | `US.CST.NFS.YTD` | `UsStmtHandoff_NfsYtd` | TField |  | Not Used |
| 13 | `US.CST.RESERVED.26` | `UsStmtHandoff_Reserved26` | TField |  |  |
| 14 | `US.CST.RESERVED.25` | `UsStmtHandoff_Reserved25` | TField |  |  |
| 15 | `US.CST.RESERVED.24` | `UsStmtHandoff_Reserved24` | TField |  |  |
| 16 | `US.CST.RESERVED.23` | `UsStmtHandoff_Reserved23` | TField |  |  |
| 17 | `US.CST.RESERVED.22` | `UsStmtHandoff_Reserved22` | TField |  |  |
| 18 | `US.CST.RESERVED.21` | `UsStmtHandoff_Reserved21` | TField |  |  |
| 19 | `US.CST.RESERVED.20` | `UsStmtHandoff_Reserved20` | TField |  |  |
| 20 | `US.CST.RESERVED.19` | `UsStmtHandoff_Reserved19` | TField |  |  |
| 21 | `US.CST.RESERVED.18` | `UsStmtHandoff_Reserved18` | TField |  |  |
| 22 | `US.CST.RESERVED.17` | `UsStmtHandoff_Reserved17` | TField |  |  |
| 23 | `US.CST.RESERVED.16` | `UsStmtHandoff_Reserved16` | TField |  |  |
| 24 | `US.CST.RESERVED.15` | `UsStmtHandoff_Reserved15` | TField |  |  |
| 25 | `US.CST.RESERVED.14` | `UsStmtHandoff_Reserved14` | TField |  |  |
| 26 | `US.CST.RESERVED.13` | `UsStmtHandoff_Reserved13` | TField |  |  |
| 27 | `US.CST.RESERVED.12` | `UsStmtHandoff_Reserved12` | TField |  |  |
| 28 | `US.CST.RESERVED.11` | `UsStmtHandoff_Reserved11` | TField |  |  |
| 29 | `US.CST.RESERVED.10` | `UsStmtHandoff_Reserved10` | TField |  |  |
| 30 | `US.CST.RESERVED.9` | `UsStmtHandoff_Reserved9` | TField |  |  |
| 31 | `US.CST.RESERVED.8` | `UsStmtHandoff_Reserved8` | TField |  |  |
| 32 | `US.CST.RESERVED.7` | `UsStmtHandoff_Reserved7` | TField |  |  |
| 33 | `US.CST.RESERVED.6` | `UsStmtHandoff_Reserved6` | TField |  |  |
| 34 | `US.CST.RESERVED.5` | `UsStmtHandoff_Reserved5` | TField |  |  |
| 35 | `US.CST.RESERVED.4` | `UsStmtHandoff_Reserved4` | TField |  |  |
| 36 | `US.CST.RESERVED.3` | `UsStmtHandoff_Reserved3` | TField |  |  |
| 37 | `US.CST.RESERVED.2` | `UsStmtHandoff_Reserved2` | TField |  |  |
| 38 | `US.CST.RESERVED.1` | `UsStmtHandoff_Reserved1` | TField |  |  |
| 39 | `US.CST.RECORD.STATUS` | `UsStmtHandoff_RecordStatus` | String |  |  |
| 40 | `US.CST.CURR.NO` | `UsStmtHandoff_CurrNo` | String |  |  |
| 41 | `US.CST.INPUTTER` | `UsStmtHandoff_Inputter` |  |  |  |
| 42 | `US.CST.DATE.TIME` | `UsStmtHandoff_DateTime` |  |  |  |
| 43 | `US.CST.AUTHORISER` | `UsStmtHandoff_Authoriser` | String |  |  |
| 44 | `US.CST.CO.CODE` | `UsStmtHandoff_CoCode` | String |  |  |
| 45 | `US.CST.DEPT.CODE` | `UsStmtHandoff_DeptCode` | String |  |  |
| 46 | `US.CST.AUDITOR.CODE` | `UsStmtHandoff_AuditorCode` | String |  |  |
| 47 | `US.CST.AUDIT.DATE.TIME` | `UsStmtHandoff_AuditDateTime` | String |  |  |
