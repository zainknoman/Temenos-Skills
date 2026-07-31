# ID.DEPOSIT.TRACKER.HIST — Table Schema

> Source: `INSERTS/I_F.ID.DEPOSIT.TRACKER.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.DTH.OPENING.DATE` | `IdDepositTrackerHist_OpeningDate` | TField |  |  |
| 2 | `ID.DTH.CURRENT.POOL` | `IdDepositTrackerHist_CurrentPool` | TField |  |  |
| 3 | `ID.DTH.POOL.CHANGE.DATE` | `IdDepositTrackerHist_PoolChangeDate` | TField |  |  |
| 4 | `ID.DTH.PREVIOUS.POOL` | `IdDepositTrackerHist_PreviousPool` |  |  |  |
| 5 | `ID.DTH.POOL.START.DATE` | `IdDepositTrackerHist_PoolStartDate` |  |  |  |
| 6 | `ID.DTH.POOL.END.DATE` | `IdDepositTrackerHist_PoolEndDate` |  |  |  |
| 7 | `ID.DTH.RESERVED.5` | `IdDepositTrackerHist_Reserved5` |  |  |  |
| 8 | `ID.DTH.RESERVED.4` | `IdDepositTrackerHist_Reserved4` |  |  |  |
| 9 | `ID.DTH.RESERVED.3` | `IdDepositTrackerHist_Reserved3` |  |  |  |
| 10 | `ID.DTH.RESERVED.2` | `IdDepositTrackerHist_Reserved2` |  |  |  |
| 11 | `ID.DTH.RESERVED.1` | `IdDepositTrackerHist_Reserved1` |  |  |  |
| 12 | `ID.DTH.DEPOSIT.TYPE` | `IdDepositTrackerHist_DepositType` | TField |  |  |
| 13 | `ID.DTH.PROFIT.PAY.METHOD` | `IdDepositTrackerHist_ProfitPayMethod` | TField |  |  |
| 14 | `ID.DTH.DISTRIBUTION.ID` | `IdDepositTrackerHist_DistributionId` |  |  |  |
| 15 | `ID.DTH.PAID.DISTRIB.ID` | `IdDepositTrackerHist_PaidDistribId` |  |  |  |
