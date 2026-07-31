# ID.PROFIT.RATE.HISTORY — Table Schema

> Source: `INSERTS/I_F.ID.PROFIT.RATE.HISTORY` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.HIS.PDS.ACTION.ID` | `IdProfitRateHistory_PdsActionId` |  |  |  |
| 2 | `ID.HIS.DIST.START.DATE` | `IdProfitRateHistory_DistStartDate` |  |  |  |
| 3 | `ID.HIS.DIST.END.DATE` | `IdProfitRateHistory_DistEndDate` |  |  |  |
| 4 | `ID.HIS.POOL.LINK.ST.DATE` | `IdProfitRateHistory_PoolLinkStDate` |  |  |  |
| 5 | `ID.HIS.POOL.LINK.END.DATE` | `IdProfitRateHistory_PoolLinkEndDate` |  |  |  |
| 6 | `ID.HIS.DAYS.IN.POOL` | `IdProfitRateHistory_DaysInPool` |  |  |  |
| 7 | `ID.HIS.PROFIT.RATE` | `IdProfitRateHistory_ProfitRate` |  |  |  |
