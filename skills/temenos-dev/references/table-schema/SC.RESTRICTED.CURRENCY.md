# SC.RESTRICTED.CURRENCY — Table Schema

> Source: `INSERTS/I_F.SC.RESTRICTED.CURRENCY` in `SC_SccConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.RES.RESTRICTED.CCY` | `ScRestrictedCurrency_RestrictedCcy` |  |  |  |
| 2 | `SC.RES.SETTLEMENT.CCY` | `ScRestrictedCurrency_SettlementCcy` |  |  |  |
| 3 | `SC.RES.DEFAULT.RATE` | `ScRestrictedCurrency_DefaultRate` | TField |  | If this field is set to 'YES',the exchange rate will default from CURRENCY table of T24. Else, the rate will have to be manually input Validation Rules 1.Allowed Option are YES or NO or blank. |
| 4 | `SC.RES.RESERVED5` | `ScRestrictedCurrency_Reserved5` | TField |  |  |
| 5 | `SC.RES.RESERVED4` | `ScRestrictedCurrency_Reserved4` | TField |  |  |
| 6 | `SC.RES.RESERVED3` | `ScRestrictedCurrency_Reserved3` | TField |  |  |
| 7 | `SC.RES.RESERVED2` | `ScRestrictedCurrency_Reserved2` | TField |  |  |
| 8 | `SC.RES.RESERVED1` | `ScRestrictedCurrency_Reserved1` | TField |  |  |
| 9 | `SC.RES.LOCAL.REF` | `ScRestrictedCurrency_LocalRef` |  |  |  |
| 10 | `SC.RES.OVERRIDE` | `ScRestrictedCurrency_Override` |  |  |  |
| 11 | `SC.RES.RECORD.STATUS` | `ScRestrictedCurrency_RecordStatus` | String |  |  |
| 12 | `SC.RES.CURR.NO` | `ScRestrictedCurrency_CurrNo` | String |  |  |
| 13 | `SC.RES.INPUTTER` | `ScRestrictedCurrency_Inputter` |  |  |  |
| 14 | `SC.RES.DATE.TIME` | `ScRestrictedCurrency_DateTime` |  |  |  |
| 15 | `SC.RES.AUTHORISER` | `ScRestrictedCurrency_Authoriser` | String |  |  |
| 16 | `SC.RES.CO.CODE` | `ScRestrictedCurrency_CoCode` | String |  |  |
| 17 | `SC.RES.DEPT.CODE` | `ScRestrictedCurrency_DeptCode` | String |  |  |
| 18 | `SC.RES.AUDITOR.CODE` | `ScRestrictedCurrency_AuditorCode` | String |  |  |
| 19 | `SC.RES.AUDIT.DATE.TIME` | `ScRestrictedCurrency_AuditDateTime` | String |  |  |
