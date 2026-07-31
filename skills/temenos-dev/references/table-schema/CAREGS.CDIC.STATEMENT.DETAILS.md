# CAREGS.CDIC.STATEMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.STATEMENT.DETAILS` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.STMT.DET.CUSTOMER` | `CaregsCdicStatementDetails_Customer` | TField |  | Field to store the Customer Id of the Account number received in CDIC Statement file. |
| 2 | `CDIC.STMT.DET.DATE` | `CaregsCdicStatementDetails_Date` | TField |  | Field to store the date received in CDIC Statement file. |
| 3 | `CDIC.STMT.DET.DESCRIPTION` | `CaregsCdicStatementDetails_Description` | TField |  | Field to store the date Account description received in CDIC Statement file. |
| 4 | `CDIC.STMT.DET.DEBIT.DETAILS` | `CaregsCdicStatementDetails_DebitDetails` | TField |  | Field to store the Debit amount details received in CDIC Statement file. |
| 5 | `CDIC.STMT.DET.CREDIT.DETAILS` | `CaregsCdicStatementDetails_CreditDetails` | TField |  | Field to store the Credit amount details received in CDIC Statement file. |
| 6 | `CDIC.STMT.DET.BALANCE.DETAILS` | `CaregsCdicStatementDetails_BalanceDetails` | TField |  | Field to store the Balance amount details of the account as on determinate date, received in CDIC Statement file. |
| 7 | `CDIC.STMT.DET.RESERVED.1` | `CaregsCdicStatementDetails_Reserved1` | TField |  |  |
| 8 | `CDIC.STMT.DET.RESERVED.2` | `CaregsCdicStatementDetails_Reserved2` | TField |  |  |
| 9 | `CDIC.STMT.DET.RESERVED.3` | `CaregsCdicStatementDetails_Reserved3` | TField |  |  |
| 10 | `CDIC.STMT.DET.RESERVED.4` | `CaregsCdicStatementDetails_Reserved4` | TField |  |  |
| 11 | `CDIC.STMT.DET.RESERVED.5` | `CaregsCdicStatementDetails_Reserved5` | TField |  |  |
| 12 | `CDIC.STMT.DET.RECORD.STATUS` | `CaregsCdicStatementDetails_RecordStatus` | String |  |  |
| 13 | `CDIC.STMT.DET.CURR.NO` | `CaregsCdicStatementDetails_CurrNo` | String |  |  |
| 14 | `CDIC.STMT.DET.INPUTTER` | `CaregsCdicStatementDetails_Inputter` |  |  |  |
| 15 | `CDIC.STMT.DET.DATE.TIME` | `CaregsCdicStatementDetails_DateTime` |  |  |  |
| 16 | `CDIC.STMT.DET.AUTHORISER` | `CaregsCdicStatementDetails_Authoriser` | String |  |  |
| 17 | `CDIC.STMT.DET.CO.CODE` | `CaregsCdicStatementDetails_CoCode` | String |  |  |
| 18 | `CDIC.STMT.DET.DEPT.CODE` | `CaregsCdicStatementDetails_DeptCode` | String |  |  |
| 19 | `CDIC.STMT.DET.AUDITOR.CODE` | `CaregsCdicStatementDetails_AuditorCode` | String |  |  |
| 20 | `CDIC.STMT.DET.AUDIT.DATE.TIME` | `CaregsCdicStatementDetails_AuditDateTime` | String |  |  |
