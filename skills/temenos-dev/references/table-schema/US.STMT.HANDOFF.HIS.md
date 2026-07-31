# US.STMT.HANDOFF.HIS — Table Schema

> Source: `INSERTS/I_F.US.STMT.HANDOFF.HIS` in `USRETL_CombinedStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.CST.HIS.FROM.DATE` | `UsStmtHandoffHis_FromDate` | TField |  | Not Used |
| 2 | `US.CST.HIS.TO.DATE` | `UsStmtHandoffHis_ToDate` | TField |  | Not Used |
| 3 | `US.CST.HIS.COMBINED.ID` | `UsStmtHandoffHis_CombinedId` | TField |  | Not Used |
| 4 | `US.CST.HIS.IMAGE.COUNT` | `UsStmtHandoffHis_ImageCount` | TField |  | Not Used |
| 5 | `US.CST.HIS.APYE` | `UsStmtHandoffHis_Apye` | TField |  | Not Used |
| 6 | `US.CST.HIS.INTEREST.EARNED` | `UsStmtHandoffHis_InterestEarned` | TField |  | Not Used |
| 7 | `US.CST.HIS.PRODUCT.NAME` | `UsStmtHandoffHis_ProductName` | TField |  | Not Used |
| 8 | `US.CST.HIS.OD.COUNT` | `UsStmtHandoffHis_OdCount` | TField |  | Not Used |
| 9 | `US.CST.HIS.OD.PERIOD` | `UsStmtHandoffHis_OdPeriod` | TField |  | Not Used |
| 10 | `US.CST.HIS.OD.YTD` | `UsStmtHandoffHis_OdYtd` | TField |  | Not Used |
| 11 | `US.CST.HIS.NFS.PERIOD` | `UsStmtHandoffHis_NfsPeriod` | TField |  | Not Used |
| 12 | `US.CST.HIS.NFS.YTD` | `UsStmtHandoffHis_NfsYtd` | TField |  | Not Used |
| 13 | `US.CST.HIS.RESERVED.26` | `UsStmtHandoffHis_Reserved26` | TField |  |  |
| 14 | `US.CST.HIS.RESERVED.25` | `UsStmtHandoffHis_Reserved25` | TField |  |  |
| 15 | `US.CST.HIS.RESERVED.24` | `UsStmtHandoffHis_Reserved24` | TField |  |  |
| 16 | `US.CST.HIS.RESERVED.23` | `UsStmtHandoffHis_Reserved23` | TField |  |  |
| 17 | `US.CST.HIS.RESERVED.22` | `UsStmtHandoffHis_Reserved22` | TField |  |  |
| 18 | `US.CST.HIS.RESERVED.21` | `UsStmtHandoffHis_Reserved21` | TField |  |  |
| 19 | `US.CST.HIS.RESERVED.20` | `UsStmtHandoffHis_Reserved20` | TField |  |  |
| 20 | `US.CST.HIS.RESERVED.19` | `UsStmtHandoffHis_Reserved19` | TField |  |  |
| 21 | `US.CST.HIS.RESERVED.18` | `UsStmtHandoffHis_Reserved18` | TField |  |  |
| 22 | `US.CST.HIS.RESERVED.17` | `UsStmtHandoffHis_Reserved17` | TField |  |  |
| 23 | `US.CST.HIS.RESERVED.16` | `UsStmtHandoffHis_Reserved16` | TField |  |  |
| 24 | `US.CST.HIS.RESERVED.15` | `UsStmtHandoffHis_Reserved15` | TField |  |  |
| 25 | `US.CST.HIS.RESERVED.14` | `UsStmtHandoffHis_Reserved14` | TField |  |  |
| 26 | `US.CST.HIS.RESERVED.13` | `UsStmtHandoffHis_Reserved13` | TField |  |  |
| 27 | `US.CST.HIS.RESERVED.12` | `UsStmtHandoffHis_Reserved12` | TField |  |  |
| 28 | `US.CST.HIS.RESERVED.11` | `UsStmtHandoffHis_Reserved11` | TField |  |  |
| 29 | `US.CST.HIS.RESERVED.10` | `UsStmtHandoffHis_Reserved10` | TField |  |  |
| 30 | `US.CST.HIS.RESERVED.9` | `UsStmtHandoffHis_Reserved9` | TField |  |  |
| 31 | `US.CST.HIS.RESERVED.8` | `UsStmtHandoffHis_Reserved8` | TField |  |  |
| 32 | `US.CST.HIS.RESERVED.7` | `UsStmtHandoffHis_Reserved7` | TField |  |  |
| 33 | `US.CST.HIS.RESERVED.6` | `UsStmtHandoffHis_Reserved6` | TField |  |  |
| 34 | `US.CST.HIS.RESERVED.5` | `UsStmtHandoffHis_Reserved5` | TField |  |  |
| 35 | `US.CST.HIS.RESERVED.4` | `UsStmtHandoffHis_Reserved4` | TField |  |  |
| 36 | `US.CST.HIS.RESERVED.3` | `UsStmtHandoffHis_Reserved3` | TField |  |  |
| 37 | `US.CST.HIS.RESERVED.2` | `UsStmtHandoffHis_Reserved2` | TField |  |  |
| 38 | `US.CST.HIS.RESERVED.1` | `UsStmtHandoffHis_Reserved1` | TField |  |  |
| 39 | `US.CST.HIS.RECORD.STATUS` | `UsStmtHandoffHis_RecordStatus` | String |  |  |
| 40 | `US.CST.HIS.CURR.NO` | `UsStmtHandoffHis_CurrNo` | String |  |  |
| 41 | `US.CST.HIS.INPUTTER` | `UsStmtHandoffHis_Inputter` |  |  |  |
| 42 | `US.CST.HIS.DATE.TIME` | `UsStmtHandoffHis_DateTime` |  |  |  |
| 43 | `US.CST.HIS.AUTHORISER` | `UsStmtHandoffHis_Authoriser` | String |  |  |
| 44 | `US.CST.HIS.CO.CODE` | `UsStmtHandoffHis_CoCode` | String |  |  |
| 45 | `US.CST.HIS.DEPT.CODE` | `UsStmtHandoffHis_DeptCode` | String |  |  |
| 46 | `US.CST.HIS.AUDITOR.CODE` | `UsStmtHandoffHis_AuditorCode` | String |  |  |
| 47 | `US.CST.HIS.AUDIT.DATE.TIME` | `UsStmtHandoffHis_AuditDateTime` | String |  |  |
