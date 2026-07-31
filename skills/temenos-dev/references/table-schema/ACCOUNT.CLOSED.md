# ACCOUNT.CLOSED — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.CLOSED` in `AC_AccountClosure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CLD.ACCT.CLOSE.DATE` | `AccountClosed_AcctCloseDate` | TField |  | Holds the date on which the Account has been moved to History. |
| 2 | `AC.CLD.CUSTOMER.ID` | `AccountClosed_CustomerId` | TField |  | Contains the ID of the customer who owns the Account. |
| 3 | `AC.CLD.ACCOUNT.OFFICER` | `AccountClosed_AccountOfficer` | TField |  | Contains the Account Officer responsible for the Account. |
| 4 | `AC.CLD.ACCOUNT.BRANCH` | `AccountClosed_AccountBranch` | TField |  | Holds the branch in which the Account existed. |
| 5 | `AC.CLD.CLOSURE.REASON` | `AccountClosed_ClosureReason` | TField |  | Holds the reason for closing the Account which gets updated from ACCOUNT.CLOSURE record. |
| 6 | `AC.CLD.CLOSURE.INPUTTER` | `AccountClosed_ClosureInputter` |  |  |  |
| 7 | `AC.CLD.CLOSURE.AUTHORISER` | `AccountClosed_ClosureAuthoriser` |  |  |  |
| 8 | `AC.CLD.CLOSE.MODE` | `AccountClosed_CloseMode` | TField |  | Allowed values are ONLINE and Blank. This will be updated as 'ONLINE' if the closure is online. It will remain blank for COB closure. |
| 9 | `AC.CLD.CLOSURE.NOTES` | `AccountClosed_ClosureNotes` |  |  |  |
