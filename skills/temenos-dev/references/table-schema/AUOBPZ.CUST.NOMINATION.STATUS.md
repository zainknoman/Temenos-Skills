# AUOBPZ.CUST.NOMINATION.STATUS — Table Schema

> Source: `INSERTS/I_F.AUOBPZ.CUST.NOMINATION.STATUS` in `AUOBPZ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUST.NOM.STATUS.ACCOUNT.NUMBER` | `AuobpzCustNominationStatus_AccountNumber` |  |  |  |
| 2 | `CUST.NOM.STATUS.NOMINATION.STATUS` | `AuobpzCustNominationStatus_NominationStatus` | TField |  | Contains overall nomination status. Possible values are "ACTIVE" or "REVOKE". |
| 3 | `CUST.NOM.STATUS.NO.OF.ACCOUNTS` | `AuobpzCustNominationStatus_NoOfAccounts` | TField |  | Indicates no of accounts. |
| 4 | `CUST.NOM.STATUS.NOMINATOR.ID` | `AuobpzCustNominationStatus_NominatorId` | TField |  | Indicates the nominator id. |
| 5 | `CUST.NOM.STATUS.RESERVED.1` | `AuobpzCustNominationStatus_Reserved1` | TField |  |  |
| 6 | `CUST.NOM.STATUS.LOCAL.REF` | `AuobpzCustNominationStatus_LocalRef` |  |  |  |
| 7 | `CUST.NOM.STATUS.OVERRIDE` | `AuobpzCustNominationStatus_Override` |  |  |  |
| 8 | `CUST.NOM.STATUS.RECORD.STATUS` | `AuobpzCustNominationStatus_RecordStatus` | String |  |  |
| 9 | `CUST.NOM.STATUS.CURR.NO` | `AuobpzCustNominationStatus_CurrNo` | String |  |  |
| 10 | `CUST.NOM.STATUS.INPUTTER` | `AuobpzCustNominationStatus_Inputter` |  |  |  |
| 11 | `CUST.NOM.STATUS.DATE.TIME` | `AuobpzCustNominationStatus_DateTime` |  |  |  |
| 12 | `CUST.NOM.STATUS.AUTHORISER` | `AuobpzCustNominationStatus_Authoriser` | String |  |  |
| 13 | `CUST.NOM.STATUS.CO.CODE` | `AuobpzCustNominationStatus_CoCode` | String |  |  |
| 14 | `CUST.NOM.STATUS.DEPT.CODE` | `AuobpzCustNominationStatus_DeptCode` | String |  |  |
| 15 | `CUST.NOM.STATUS.AUDITOR.CODE` | `AuobpzCustNominationStatus_AuditorCode` | String |  |  |
| 16 | `CUST.NOM.STATUS.AUDIT.DATE.TIME` | `AuobpzCustNominationStatus_AuditDateTime` | String |  |  |
