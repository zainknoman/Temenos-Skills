# SL.LOAN.INT.PART.BALANCES — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.INT.PART.BALANCES` in `SL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SIP.INT.RATE` | `SlLoanIntPartBalances_IntRate` |  |  |  |
| 2 | `SIP.CAP.RATE` | `SlLoanIntPartBalances_CapRate` |  |  |  |
| 3 | `SIP.INT.SPREAD` | `SlLoanIntPartBalances_IntSpread` |  |  |  |
| 4 | `SIP.INT.CAP.SPREAD` | `SlLoanIntPartBalances_IntCapSpread` |  |  |  |
| 5 | `SIP.SPL.INT.SPREAD` | `SlLoanIntPartBalances_SplIntSpread` |  |  |  |
| 6 | `SIP.SPL.INT.CAP.SPR` | `SlLoanIntPartBalances_SplIntCapSpr` |  |  |  |
| 7 | `SIP.INT.BASIS` | `SlLoanIntPartBalances_IntBasis` |  |  |  |
| 8 | `SIP.INT.EFF.DT` | `SlLoanIntPartBalances_IntEffDt` |  |  |  |
| 9 | `SIP.INT.RATE.TYPE` | `SlLoanIntPartBalances_IntRateType` |  |  |  |
| 10 | `SIP.RESERVED.2` | `SlLoanIntPartBalances_Reserved2` |  |  |  |
| 11 | `SIP.RESERVED.3` | `SlLoanIntPartBalances_Reserved3` |  |  |  |
| 12 | `SIP.RESERVED.4` | `SlLoanIntPartBalances_Reserved4` |  |  |  |
| 13 | `SIP.RESERVED.5` | `SlLoanIntPartBalances_Reserved5` |  |  |  |
| 14 | `SIP.RESERVED.6` | `SlLoanIntPartBalances_Reserved6` | TField |  |  |
| 15 | `SIP.RESERVED.7` | `SlLoanIntPartBalances_Reserved7` | TField |  |  |
| 16 | `SIP.RESERVED.8` | `SlLoanIntPartBalances_Reserved8` | TField |  |  |
| 17 | `SIP.RESERVED.9` | `SlLoanIntPartBalances_Reserved9` | TField |  |  |
| 18 | `SIP.RESERVED.10` | `SlLoanIntPartBalances_Reserved10` | TField |  |  |
