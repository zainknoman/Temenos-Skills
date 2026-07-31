# CAMB.L.ACCOUNT.OVERDRAWN.HIST — Table Schema

> Source: `INSERTS/I_F.CAMB.L.ACCOUNT.OVERDRAWN.HIST` in `CACSIT_CoverdraftSweep.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CWB.AO.REPORT.DATE` | `CwbLAccountOverdrawnHist_ReportDate` |  |  |  |
| 2 | `CWB.AO.CUSTOMER.NO` | `CwbLAccountOverdrawnHist_CustomerNo` |  |  |  |
| 3 | `CWB.AO.CUSTOMER.NAME` | `CwbLAccountOverdrawnHist_CustomerName` |  |  |  |
| 4 | `CWB.AO.ACCOUNT.NO` | `CwbLAccountOverdrawnHist_AccountNo` |  |  |  |
| 5 | `CWB.AO.ACCT.COMPANY` | `CwbLAccountOverdrawnHist_AcctCompany` |  |  |  |
| 6 | `CWB.AO.ACCOUNT.DAO` | `CwbLAccountOverdrawnHist_AccountDao` |  |  |  |
| 7 | `CWB.AO.DAO.BRANCH` | `CwbLAccountOverdrawnHist_DaoBranch` |  |  |  |
| 8 | `CWB.AO.AC.START.BALANCE` | `CwbLAccountOverdrawnHist_AcStartBalance` |  |  |  |
| 9 | `CWB.AO.CURRENT.BALANCE` | `CwbLAccountOverdrawnHist_CurrentBalance` |  |  |  |
| 10 | `CWB.AO.LIMIT.AMOUNT` | `CwbLAccountOverdrawnHist_LimitAmount` |  |  |  |
| 11 | `CWB.AO.OD.STATUS` | `CwbLAccountOverdrawnHist_OdStatus` |  |  |  |
| 12 | `CWB.AO.DATE.FIRST.OD` | `CwbLAccountOverdrawnHist_DateFirstOd` |  |  |  |
| 13 | `CWB.AO.DATE.LAST.MOVE` | `CwbLAccountOverdrawnHist_DateLastMove` |  |  |  |
| 14 | `CWB.AO.OVERDRAFT.CHANGE` | `CwbLAccountOverdrawnHist_OverdraftChange` |  |  |  |
| 15 | `CWB.AO.STMT.IDS` | `CwbLAccountOverdrawnHist_StmtIds` |  |  |  |
| 16 | `CWB.AO.RESERVED.10` | `CwbLAccountOverdrawnHist_Reserved10` |  |  |  |
| 17 | `CWB.AO.RESERVED.9` | `CwbLAccountOverdrawnHist_Reserved9` |  |  |  |
| 18 | `CWB.AO.RESERVED.8` | `CwbLAccountOverdrawnHist_Reserved8` |  |  |  |
| 19 | `CWB.AO.RESERVED.7` | `CwbLAccountOverdrawnHist_Reserved7` |  |  |  |
| 20 | `CWB.AO.RESERVED.6` | `CwbLAccountOverdrawnHist_Reserved6` |  |  |  |
| 21 | `CWB.AO.RESERVED.5` | `CwbLAccountOverdrawnHist_Reserved5` |  |  |  |
| 22 | `CWB.AO.RESERVED.4` | `CwbLAccountOverdrawnHist_Reserved4` |  |  |  |
| 23 | `CWB.AO.RESERVED.3` | `CwbLAccountOverdrawnHist_Reserved3` |  |  |  |
| 24 | `CWB.AO.RESERVED.2` | `CwbLAccountOverdrawnHist_Reserved2` |  |  |  |
| 25 | `CWB.AO.RESERVED.1` | `CwbLAccountOverdrawnHist_Reserved1` |  |  |  |
