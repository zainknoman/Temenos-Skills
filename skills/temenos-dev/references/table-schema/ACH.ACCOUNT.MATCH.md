# ACH.ACCOUNT.MATCH — Table Schema

> Source: `INSERTS/I_F.ACH.ACCOUNT.MATCH` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.MATCH.INVALID.ACCOUNT.NUMBER` | `AchAccountMatch_InvalidAcctNumber` |  |  |  |
| 2 | `ACH.MATCH.CUSTOMER.NAME` | `AchAccountMatch_CustomerName` | TField |  | 50 Positions - Beneficiary name from the incoming ACH payment |
| 3 | `ACH.MATCH.MATCH.ACCOUNT.NUMBER` | `AchAccountMatch_MatchAcctNumber` |  |  |  |
| 4 | `ACH.MATCH.MATCH.CUSTOMER.NAME` | `AchAccountMatch_MatchCustomerName` |  |  |  |
| 5 | `ACH.MATCH.STATUS` | `AchAccountMatch_Status` | TField |  | Dropdown box - Valid values are:Match PendingMatch CompleteMatch Not FoundClearedCleared |
| 6 | `ACH.MATCH.OVERRIDE` | `AchAccountMatch_Override` |  |  |  |
| 7 | `ACH.MATCH.RECORD.STATUS` | `AchAccountMatch_RecordStatus` | String |  |  |
| 8 | `ACH.MATCH.CURR.NO` | `AchAccountMatch_CurrNo` | String |  |  |
| 9 | `ACH.MATCH.INPUTTER` | `AchAccountMatch_Inputter` |  |  |  |
| 10 | `ACH.MATCH.DATE.TIME` | `AchAccountMatch_DateTime` |  |  |  |
| 11 | `ACH.MATCH.AUTHORISER` | `AchAccountMatch_Authoriser` | String |  |  |
| 12 | `ACH.MATCH.CO.CODE` | `AchAccountMatch_CoCode` | String |  |  |
| 13 | `ACH.MATCH.DEPT.CODE` | `AchAccountMatch_DeptCode` | String |  |  |
| 14 | `ACH.MATCH.AUDITOR.CODE` | `AchAccountMatch_AuditorCode` | String |  |  |
| 15 | `ACH.MATCH.AUDIT.DATE.TIME` | `AchAccountMatch_AuditDateTime` | String |  |  |
