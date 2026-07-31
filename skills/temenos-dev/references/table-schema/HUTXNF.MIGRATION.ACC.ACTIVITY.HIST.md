# HUTXNF.MIGRATION.ACC.ACTIVITY.HIST — Table Schema

> Source: `INSERTS/I_F.HUTXNF.MIGRATION.ACC.ACTIVITY.HIST` in `HUTXNF_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUTMIG.DATE` | `HutxnfMigrationAccActivityHist_Date` |  |  |  |
| 2 | `HUTMIG.ACTIVITY.NAME` | `HutxnfMigrationAccActivityHist_ActivityName` |  |  |  |
| 3 | `HUTMIG.TRANSACTION.AMOUNT` | `HutxnfMigrationAccActivityHist_TransactionAmount` |  |  |  |
| 4 | `HUTMIG.LOCAL.REF` | `HutxnfMigrationAccActivityHist_LocalRef` |  |  |  |
| 5 | `HUTMIG.OVERRIDE` | `HutxnfMigrationAccActivityHist_Override` |  |  |  |
| 6 | `HUTMIG.RECORD.STATUS` | `HutxnfMigrationAccActivityHist_RecordStatus` | String |  |  |
| 7 | `HUTMIG.CURR.NO` | `HutxnfMigrationAccActivityHist_CurrNo` | String |  |  |
| 8 | `HUTMIG.INPUTTER` | `HutxnfMigrationAccActivityHist_Inputter` |  |  |  |
| 9 | `HUTMIG.DATE.TIME` | `HutxnfMigrationAccActivityHist_DateTime` |  |  |  |
| 10 | `HUTMIG.AUTHORISER` | `HutxnfMigrationAccActivityHist_Authoriser` | String |  |  |
| 11 | `HUTMIG.CO.CODE` | `HutxnfMigrationAccActivityHist_CoCode` | String |  |  |
| 12 | `HUTMIG.DEPT.CODE` | `HutxnfMigrationAccActivityHist_DeptCode` | String |  |  |
| 13 | `HUTMIG.AUDITOR.CODE` | `HutxnfMigrationAccActivityHist_AuditorCode` | String |  |  |
| 14 | `HUTMIG.AUDIT.DATE.TIME` | `HutxnfMigrationAccActivityHist_AuditDateTime` | String |  |  |
