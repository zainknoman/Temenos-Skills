# TY.CURRENCY.PAIR — Table Schema

> Source: `INSERTS/I_F.TY.CURRENCY.PAIR` in `TY_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.CP.DESCRIPTION` | `TyCurrencyPair_Description` |  |  |  |
| 2 | `TY.CP.RESERVED.10` | `TyCurrencyPair_Reserved10` |  |  |  |
| 3 | `TY.CP.RESERVED.9` | `TyCurrencyPair_Reserved9` |  |  |  |
| 4 | `TY.CP.RESERVED.8` | `TyCurrencyPair_Reserved8` |  |  |  |
| 5 | `TY.CP.RESERVED.7` | `TyCurrencyPair_Reserved7` |  |  |  |
| 6 | `TY.CP.RESERVED.6` | `TyCurrencyPair_Reserved6` |  |  |  |
| 7 | `TY.CP.RESERVED.5` | `TyCurrencyPair_Reserved5` |  |  |  |
| 8 | `TY.CP.RESERVED.4` | `TyCurrencyPair_Reserved4` |  |  |  |
| 9 | `TY.CP.RESERVED.3` | `TyCurrencyPair_Reserved3` |  |  |  |
| 10 | `TY.CP.RESERVED.2` | `TyCurrencyPair_Reserved2` |  |  |  |
| 11 | `TY.CP.RESERVED.1` | `TyCurrencyPair_Reserved1` |  |  |  |
| 12 | `TY.CP.LOCAL.REF` | `TyCurrencyPair_LocalRef` |  |  |  |
| 13 | `TY.CP.OVERRIDE` | `TyCurrencyPair_Override` |  |  |  |
| 14 | `TY.CP.RECORD.STATUS` | `TyCurrencyPair_RecordStatus` | String |  |  |
| 15 | `TY.CP.CURR.NO` | `TyCurrencyPair_CurrNo` | String |  |  |
| 16 | `TY.CP.INPUTTER` | `TyCurrencyPair_Inputter` |  |  |  |
| 17 | `TY.CP.DATE.TIME` | `TyCurrencyPair_DateTime` |  |  |  |
| 18 | `TY.CP.AUTHORISER` | `TyCurrencyPair_Authoriser` | String |  |  |
| 19 | `TY.CP.CO.CODE` | `TyCurrencyPair_CoCode` | String |  |  |
| 20 | `TY.CP.DEPT.CODE` | `TyCurrencyPair_DeptCode` | String |  |  |
| 21 | `TY.CP.AUDITOR.CODE` | `TyCurrencyPair_AuditorCode` | String |  |  |
| 22 | `TY.CP.AUDIT.DATE.TIME` | `TyCurrencyPair_AuditDateTime` | String |  |  |
