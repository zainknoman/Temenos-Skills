# ID.ACCOUNT.TRACKER — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.TRACKER` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAT.OPENING.DATE` | `IdAccountTracker_OpeningDate` | TField |  | This field will hold the effective date of the arrangement. Validation Rules: 1. Standard T24 date field. |
| 2 | `ID.IAT.CURRENT.POOL` | `IdAccountTracker_CurrentPool` | TField |  | This field will hold the pool to which the arrangement is linked to it currently. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Must be a valid record from the file ID.POOL.PARAMETER. |
| 3 | `ID.IAT.POOL.CHANGE.DATE` | `IdAccountTracker_PoolChangeDate` | TField |  | This field will specify the date when the pool was changed from the current pool. Validation Rules: 1. Standard T24 date field. |
| 4 | `ID.IAT.PREVIOUS.POOL` | `IdAccountTracker_PreviousPool` |  |  |  |
| 5 | `ID.IAT.POOL.START.DATE` | `IdAccountTracker_PoolStartDate` |  |  |  |
| 6 | `ID.IAT.POOL.END.DATE` | `IdAccountTracker_PoolEndDate` |  |  |  |
| 7 | `ID.IAT.RESERVED.5` | `IdAccountTracker_Reserved5` |  |  |  |
| 8 | `ID.IAT.RESERVED.4` | `IdAccountTracker_Reserved4` |  |  |  |
| 9 | `ID.IAT.RESERVED.3` | `IdAccountTracker_Reserved3` |  |  |  |
| 10 | `ID.IAT.RESERVED.2` | `IdAccountTracker_Reserved2` |  |  |  |
| 11 | `ID.IAT.RESERVED.1` | `IdAccountTracker_Reserved1` |  |  |  |
| 12 | `ID.IAT.ACCOUNT.TYPE` | `IdAccountTracker_AccountType` | TField |  | This field will specify the type of account. |
| 13 | `ID.IAT.DISTRIBUTION.ID` | `IdAccountTracker_DistributionId` |  |  |  |
| 14 | `ID.IAT.PAID.DISTRIB.ID` | `IdAccountTracker_PaidDistribId` |  |  |  |
| 15 | `ID.IAT.ELIGIBILITY.TO.CLOSE.ON.PDS` | `IdAccountTracker_EligibilityToCloseOnPds` | TField |  | This field is used to know if an Islamic accounts arrangement is marked to close during PDS. This field will contain the value 'YES' if the account is marked to close during PDS. |
| 16 | `ID.IAT.CLOSE.REQUEST.DATE` | `IdAccountTracker_CloseRequestDate` | TField |  | This field is updated with the closure requested date whenever an Islamic accounts arrangement is marked to close during PDS. |
