# SL.LOAN.INT.BALANCES — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.INT.BALANCES` in `SL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SIB.INT.RATE` | `SlLoanIntBalances_IntRate` |  |  |  |
| 2 | `SIB.CAP.RATE` | `SlLoanIntBalances_CapRate` |  |  |  |
| 3 | `SIB.INT.SPREAD` | `SlLoanIntBalances_IntSpread` |  |  |  |
| 4 | `SIB.INT.CAP.SPREAD` | `SlLoanIntBalances_IntCapSpread` |  |  |  |
| 5 | `SIB.SPL.INT.SPREAD` | `SlLoanIntBalances_SplIntSpread` |  |  |  |
| 6 | `SIB.SPL.INT.CAP.SPR` | `SlLoanIntBalances_SplIntCapSpr` |  |  |  |
| 7 | `SIB.INT.BASIS` | `SlLoanIntBalances_IntBasis` |  |  |  |
| 8 | `SIB.INT.EFF.DT` | `SlLoanIntBalances_IntEffDt` |  |  |  |
| 9 | `SIB.INT.RATE.TYPE` | `SlLoanIntBalances_IntRateType` |  |  |  |
| 10 | `SIB.RESERVED.2` | `SlLoanIntBalances_Reserved2` |  |  |  |
| 11 | `SIB.RESERVED.3` | `SlLoanIntBalances_Reserved3` |  |  |  |
| 12 | `SIB.RESERVED.4` | `SlLoanIntBalances_Reserved4` |  |  |  |
| 13 | `SIB.RESERVED.5` | `SlLoanIntBalances_Reserved5` |  |  |  |
| 14 | `SIB.RESERVED.6` | `SlLoanIntBalances_Reserved6` | TField |  |  |
| 15 | `SIB.RESERVED.7` | `SlLoanIntBalances_Reserved7` | TField |  |  |
| 16 | `SIB.RESERVED.8` | `SlLoanIntBalances_Reserved8` | TField |  |  |
| 17 | `SIB.RESERVED.9` | `SlLoanIntBalances_Reserved9` | TField |  |  |
| 18 | `SIB.RESERVED.10` | `SlLoanIntBalances_Reserved10` | TField |  |  |
