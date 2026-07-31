# ST.RATE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ST.RATE.PARAMETER` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.RP.PI.COUNTRY` | `StRateParameter_PiCountry` |  |  |  |
| 2 | `ST.RP.PI.REGION` | `StRateParameter_PiRegion` |  |  |  |
| 3 | `ST.RP.FWD.COUNTRY` | `StRateParameter_FwdCountry` |  |  |  |
| 4 | `ST.RP.FWD.REGION` | `StRateParameter_FwdRegion` |  |  |  |
| 5 | `ST.RP.RESERVED10` | `StRateParameter_Reserved10` | TField |  |  |
| 6 | `ST.RP.RESERVED09` | `StRateParameter_Reserved09` | TField |  |  |
| 7 | `ST.RP.RESERVED08` | `StRateParameter_Reserved08` | TField |  |  |
| 8 | `ST.RP.RESERVED07` | `StRateParameter_Reserved07` | TField |  |  |
| 9 | `ST.RP.RESERVED06` | `StRateParameter_Reserved06` | TField |  |  |
| 10 | `ST.RP.RESERVED05` | `StRateParameter_Reserved05` | TField |  |  |
| 11 | `ST.RP.RESERVED04` | `StRateParameter_Reserved04` | TField |  |  |
| 12 | `ST.RP.RESERVED03` | `StRateParameter_Reserved03` | TField |  |  |
| 13 | `ST.RP.RESERVED02` | `StRateParameter_Reserved02` | TField |  |  |
| 14 | `ST.RP.RESERVED01` | `StRateParameter_Reserved01` | TField |  |  |
| 15 | `ST.RP.LOCAL.REF` | `StRateParameter_LocalRef` |  |  |  |
| 16 | `ST.RP.RECORD.STATUS` | `StRateParameter_RecordStatus` | String |  |  |
| 17 | `ST.RP.CURR.NO` | `StRateParameter_CurrNo` | String |  |  |
| 18 | `ST.RP.INPUTTER` | `StRateParameter_Inputter` |  |  |  |
| 19 | `ST.RP.DATE.TIME` | `StRateParameter_DateTime` |  |  |  |
| 20 | `ST.RP.AUTHORISER` | `StRateParameter_Authoriser` | String |  |  |
| 21 | `ST.RP.CO.CODE` | `StRateParameter_CoCode` | String |  |  |
| 22 | `ST.RP.DEPT.CODE` | `StRateParameter_DeptCode` | String |  |  |
| 23 | `ST.RP.AUDITOR.CODE` | `StRateParameter_AuditorCode` | String |  |  |
| 24 | `ST.RP.AUDIT.DATE.TIME` | `StRateParameter_AuditDateTime` | String |  |  |
