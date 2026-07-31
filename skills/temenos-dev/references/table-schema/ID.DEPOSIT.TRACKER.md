# ID.DEPOSIT.TRACKER — Table Schema

> Source: `INSERTS/I_F.ID.DEPOSIT.TRACKER` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IDT.OPENING.DATE` | `IdDepositTracker_OpeningDate` | TField |  |  |
| 2 | `ID.IDT.CURRENT.POOL` | `IdDepositTracker_CurrentPool` | TField |  |  |
| 3 | `ID.IDT.POOL.CHANGE.DATE` | `IdDepositTracker_PoolChangeDate` | TField |  |  |
| 4 | `ID.IDT.PREVIOUS.POOL` | `IdDepositTracker_PreviousPool` |  |  |  |
| 5 | `ID.IDT.POOL.START.DATE` | `IdDepositTracker_PoolStartDate` |  |  |  |
| 6 | `ID.IDT.POOL.END.DATE` | `IdDepositTracker_PoolEndDate` |  |  |  |
| 7 | `ID.IDT.RESERVED.5` | `IdDepositTracker_Reserved5` |  |  |  |
| 8 | `ID.IDT.RESERVED.4` | `IdDepositTracker_Reserved4` |  |  |  |
| 9 | `ID.IDT.RESERVED.3` | `IdDepositTracker_Reserved3` |  |  |  |
| 10 | `ID.IDT.RESERVED.2` | `IdDepositTracker_Reserved2` |  |  |  |
| 11 | `ID.IDT.RESERVED.1` | `IdDepositTracker_Reserved1` |  |  |  |
| 12 | `ID.IDT.DEPOSIT.TYPE` | `IdDepositTracker_DepositType` | TField |  |  |
| 13 | `ID.IDT.PROFIT.PAY.METHOD` | `IdDepositTracker_ProfitPayMethod` | TField |  |  |
| 14 | `ID.IDT.DISTRIBUTION.ID` | `IdDepositTracker_DistributionId` |  |  |  |
| 15 | `ID.IDT.PAID.DISTRIB.ID` | `IdDepositTracker_PaidDistribId` |  |  |  |
