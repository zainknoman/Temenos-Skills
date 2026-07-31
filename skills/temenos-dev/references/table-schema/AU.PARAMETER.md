# AU.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AU.PARAMETER` in `AU_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AU.PAR.BUSINESS.UNIT` | `AuParameter_BusinessUnit` | TField |  | Company code of parent company Validation Rules: This business unit value should be same as Record id |
| 2 | `AU.PAR.ACCOUNTING.CO` | `AuParameter_AccountingCo` |  |  |  |
| 3 | `AU.PAR.MANDATORY.CCY` | `AuParameter_MandatoryCcy` |  |  |  |
| 4 | `AU.PAR.APP.RULE` | `AuParameter_AppRule` |  |  |  |
| 5 | `AU.PAR.DEFAULT.ACCT.CO` | `AuParameter_DefaultAcctCo` | TField | Yes | Default Accounting Company when the Mandatory currency rule does not satisfy Validation Rules: Single value field A valid Company Record. |
| 6 | `AU.PAR.ACCOUNTING.COMPANY` | `AuParameter_AccountingCompany` |  |  |  |
| 7 | `AU.PAR.BOOK.CODE` | `AuParameter_BookCode` |  |  |  |
| 8 | `AU.PAR.DEALER.DESK` | `AuParameter_DealerDesk` |  |  |  |
| 9 | `AU.PAR.MIGRATION.DATE` | `AuParameter_MigrationDate` | TField |  | This field holds the value for migration date If MIGRATION.DATE is null then MIGRATION.STATUS also will be set to null If TODAY less than MIGRATION.DATE then MIGRATION.STATUS will be set to VERIFYING If TODAY equals MIGRATION.DATE then MIGRATION.STATUS will be set to MIGRATING Validation Rules: Valid Date record. |
| 10 | `AU.PAR.MIGRATION.STATUS` | `AuParameter_MigrationStatus` | TField |  | Migration status set based on MIGRATION.DATE Validation Rules: Value can be either VERIFYING, MIGRATING, INACTIVE or null. |
| 11 | `AU.PAR.MIG.TRANS.CODE` | `AuParameter_MigTransCode` | TField |  | This field holds the transaction code Validation Rules: A Valid Record in TRANSACTION application. |
| 12 | `AU.PAR.GPACK.JOBS` | `AuParameter_GpackJobs` |  |  |  |
| 13 | `AU.PAR.DECOMMISSION.DATE` | `AuParameter_DecommissionDate` | TField |  | Holds the date from which the system will not follow the AU rules. If this field has a value, then all the accounting units under the processing company was or will be decommissioned. Validation Rules: AU setup can be decommissioned on any date only when CONT.SELF.BAL as Y set in CONSOLIDATE.COND. |
| 14 | `AU.PAR.DECOMM.DR.TXN.CODE` | `AuParameter_DecommDrTxnCode` | TField | Yes | The debit transaction code specified will be used during AU.PL.MOVEMENT job. Validation Rules: Should hold a valid debit transaction code. This field is mandatory when DECOMMISSION.DATE is specified. |
| 15 | `AU.PAR.DECOMM.CR.TXN.CODE` | `AuParameter_DecommCrTxnCode` | TField | Yes | The credit transaction code specified will be used during AU.PL.MOVEMENT job. Validation Rules: Should hold a valid credit transaction code. This field is mandatory when DECOMMISSION.DATE is specified. |
| 16 | `AU.PAR.RESERVED.2` | `AuParameter_Reserved2` | TField |  |  |
| 17 | `AU.PAR.RESERVED.1` | `AuParameter_Reserved1` | TField |  |  |
| 18 | `AU.PAR.LOCAL.REF` | `AuParameter_LocalRef` |  |  |  |
| 19 | `AU.PAR.OVERRIDE` | `AuParameter_Override` |  |  |  |
| 20 | `AU.PAR.RECORD.STATUS` | `AuParameter_RecordStatus` | String |  |  |
| 21 | `AU.PAR.CURR.NO` | `AuParameter_CurrNo` | String |  |  |
| 22 | `AU.PAR.INPUTTER` | `AuParameter_Inputter` |  |  |  |
| 23 | `AU.PAR.DATE.TIME` | `AuParameter_DateTime` |  |  |  |
| 24 | `AU.PAR.AUTHORISER` | `AuParameter_Authoriser` | String |  |  |
| 25 | `AU.PAR.CO.CODE` | `AuParameter_CoCode` | String |  |  |
| 26 | `AU.PAR.DEPT.CODE` | `AuParameter_DeptCode` | String |  |  |
| 27 | `AU.PAR.AUDITOR.CODE` | `AuParameter_AuditorCode` | String |  |  |
| 28 | `AU.PAR.AUDIT.DATE.TIME` | `AuParameter_AuditDateTime` | String |  |  |
