# CWB.L.ACCOUNT.OVERDRAWN — Table Schema

> Source: `INSERTS/I_F.CWB.L.ACCOUNT.OVERDRAWN` in `CACSIT_CoverdraftSweep.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CWB.AO.REPORT.DATE` | `CwbLAccountOverdrawn_ReportDate` |  |  |  |
| 2 | `CWB.AO.CUSTOMER.NO` | `CwbLAccountOverdrawn_CustomerNo` |  |  |  |
| 3 | `CWB.AO.CUSTOMER.NAME` | `CwbLAccountOverdrawn_CustomerName` |  |  |  |
| 4 | `CWB.AO.ACCOUNT.NO` | `CwbLAccountOverdrawn_AccountNo` |  |  |  |
| 5 | `CWB.AO.ACCT.COMPANY` | `CwbLAccountOverdrawn_AcctCompany` |  |  |  |
| 6 | `CWB.AO.ACCOUNT.DAO` | `CwbLAccountOverdrawn_AccountDao` |  |  |  |
| 7 | `CWB.AO.DAO.BRANCH` | `CwbLAccountOverdrawn_DaoBranch` |  |  |  |
| 8 | `CWB.AO.AC.START.BALANCE` | `CwbLAccountOverdrawn_AcStartBalance` |  |  |  |
| 9 | `CWB.AO.CURRENT.BALANCE` | `CwbLAccountOverdrawn_CurrentBalance` |  |  |  |
| 10 | `CWB.AO.LIMIT.AMOUNT` | `CwbLAccountOverdrawn_LimitAmount` |  |  |  |
| 11 | `CWB.AO.OD.STATUS` | `CwbLAccountOverdrawn_OdStatus` |  |  |  |
| 12 | `CWB.AO.DATE.FIRST.OD` | `CwbLAccountOverdrawn_DateFirstOd` |  |  |  |
| 13 | `CWB.AO.DATE.LAST.MOVE` | `CwbLAccountOverdrawn_DateLastMove` |  |  |  |
| 14 | `CWB.AO.OVERDRAFT.CHANGE` | `CwbLAccountOverdrawn_OverdraftChange` |  |  |  |
| 15 | `CWB.AO.STMT.IDS` | `CwbLAccountOverdrawn_StmtIds` |  |  |  |
| 16 | `CWB.AO.RESERVED.10` | `CwbLAccountOverdrawn_Reserved10` |  |  |  |
| 17 | `CWB.AO.RESERVED.9` | `CwbLAccountOverdrawn_Reserved9` |  |  |  |
| 18 | `CWB.AO.RESERVED.8` | `CwbLAccountOverdrawn_Reserved8` |  |  |  |
| 19 | `CWB.AO.RESERVED.7` | `CwbLAccountOverdrawn_Reserved7` |  |  |  |
| 20 | `CWB.AO.RESERVED.6` | `CwbLAccountOverdrawn_Reserved6` |  |  |  |
| 21 | `CWB.AO.RESERVED.5` | `CwbLAccountOverdrawn_Reserved5` |  |  |  |
| 22 | `CWB.AO.RESERVED.4` | `CwbLAccountOverdrawn_Reserved4` |  |  |  |
| 23 | `CWB.AO.RESERVED.3` | `CwbLAccountOverdrawn_Reserved3` |  |  |  |
| 24 | `CWB.AO.RESERVED.2` | `CwbLAccountOverdrawn_Reserved2` |  |  |  |
| 25 | `CWB.AO.RESERVED.1` | `CwbLAccountOverdrawn_Reserved1` |  |  |  |
