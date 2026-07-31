# ID.ACCOUNT.TRACKER.HIST — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.TRACKER.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.ATH.OPENING.DATE` | `IdAccountTrackerHist_OpeningDate` | TField |  | This field will hold the effective date of the arrangement. Validation Rules: 1. Standard T24 date field. |
| 2 | `ID.ATH.CURRENT.POOL` | `IdAccountTrackerHist_CurrentPool` | TField |  | This field will hold the pool to which the arrangement is linked to it currently. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Must be a valid record from the file ID.POOL.PARAMETER. |
| 3 | `ID.ATH.POOL.CHANGE.DATE` | `IdAccountTrackerHist_PoolChangeDate` | TField |  | This field will specify the date when the pool was changed from the current pool. Validation Rules: 1. Standard T24 date field. |
| 4 | `ID.ATH.PREVIOUS.POOL` | `IdAccountTrackerHist_PreviousPool` |  |  |  |
| 5 | `ID.ATH.POOL.START.DATE` | `IdAccountTrackerHist_PoolStartDate` |  |  |  |
| 6 | `ID.ATH.POOL.END.DATE` | `IdAccountTrackerHist_PoolEndDate` |  |  |  |
| 7 | `ID.ATH.RESERVED.5` | `IdAccountTrackerHist_Reserved5` |  |  |  |
| 8 | `ID.ATH.RESERVED.4` | `IdAccountTrackerHist_Reserved4` |  |  |  |
| 9 | `ID.ATH.RESERVED.3` | `IdAccountTrackerHist_Reserved3` |  |  |  |
| 10 | `ID.ATH.RESERVED.2` | `IdAccountTrackerHist_Reserved2` |  |  |  |
| 11 | `ID.ATH.RESERVED.1` | `IdAccountTrackerHist_Reserved1` |  |  |  |
| 12 | `ID.ATH.ACCOUNT.TYPE` | `IdAccountTrackerHist_AccountType` | TField |  | This field will specify the type of account. |
| 13 | `ID.ATH.DISTRIBUTION.ID` | `IdAccountTrackerHist_DistributionId` |  |  |  |
| 14 | `ID.ATH.PAID.DISTRIB.ID` | `IdAccountTrackerHist_PaidDistribId` |  |  |  |
| 15 | `ID.ATH.ELIGIBILITY.TO.CLOSE.ON.PDS` | `IdAccountTrackerHist_EligibilityToCloseOnPds` | TField |  | This field is used to know if an Islamic accounts arrangement is marked to close during PDS. This field will contain the value 'YES' if the account is marked to close during PDS. |
| 16 | `ID.ATH.CLOSE.REQUEST.DATE` | `IdAccountTrackerHist_CloseRequestDate` | TField |  | This field is updated with the closure requested date whenever an Islamic accounts arrangement is marked to close during PDS. |
