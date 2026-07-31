# SC.SETT.PENALTY.RATES — Table Schema

> Source: `INSERTS/I_F.SC.SETT.PENALTY.RATES` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SETT.PEN.TRD.GRWTH.MRKT` | `ScSettPenaltyRates_TrdGrwthMrkt` |  |  |  |
| 2 | `SC.SETT.PEN.LIQUID.INSTRUMENT` | `ScSettPenaltyRates_LiquidInstrument` |  |  |  |
| 3 | `SC.SETT.PEN.SEC.PENALTY.RATE` | `ScSettPenaltyRates_SecPenaltyRate` |  |  |  |
| 4 | `SC.SETT.PEN.CASH.PENALTY.RATE` | `ScSettPenaltyRates_CashPenaltyRate` |  |  |  |
| 5 | `SC.SETT.PEN.PI.KEY` | `ScSettPenaltyRates_PiKey` | TField |  | This field holds the PI(PERIODIC.INTERST) Key which is used to compute the penalty for cash settlement failure This field accepts the PI key |
| 6 | `SC.SETT.PEN.RESERVED15` | `ScSettPenaltyRates_Reserved15` | TField |  |  |
| 7 | `SC.SETT.PEN.RESERVED14` | `ScSettPenaltyRates_Reserved14` | TField |  |  |
| 8 | `SC.SETT.PEN.RESERVED13` | `ScSettPenaltyRates_Reserved13` | TField |  |  |
| 9 | `SC.SETT.PEN.RESERVED12` | `ScSettPenaltyRates_Reserved12` | TField |  |  |
| 10 | `SC.SETT.PEN.RESERVED11` | `ScSettPenaltyRates_Reserved11` | TField |  |  |
| 11 | `SC.SETT.PEN.RESERVED10` | `ScSettPenaltyRates_Reserved10` | TField |  |  |
| 12 | `SC.SETT.PEN.RESERVED9` | `ScSettPenaltyRates_Reserved9` | TField |  |  |
| 13 | `SC.SETT.PEN.RESERVED8` | `ScSettPenaltyRates_Reserved8` | TField |  |  |
| 14 | `SC.SETT.PEN.RESERVED7` | `ScSettPenaltyRates_Reserved7` | TField |  |  |
| 15 | `SC.SETT.PEN.RESERVED6` | `ScSettPenaltyRates_Reserved6` | TField |  |  |
| 16 | `SC.SETT.PEN.RESERVED5` | `ScSettPenaltyRates_Reserved5` | TField |  |  |
| 17 | `SC.SETT.PEN.RESERVED4` | `ScSettPenaltyRates_Reserved4` | TField |  |  |
| 18 | `SC.SETT.PEN.RESERVED3` | `ScSettPenaltyRates_Reserved3` | TField |  |  |
| 19 | `SC.SETT.PEN.RESERVED2` | `ScSettPenaltyRates_Reserved2` | TField |  |  |
| 20 | `SC.SETT.PEN.RESERVED1` | `ScSettPenaltyRates_Reserved1` | TField |  |  |
| 21 | `SC.SETT.PEN.LOCAL.REF` | `ScSettPenaltyRates_LocalRef` |  |  |  |
| 22 | `SC.SETT.PEN.OVERRIDE` | `ScSettPenaltyRates_Override` |  |  |  |
| 23 | `SC.SETT.PEN.RECORD.STATUS` | `ScSettPenaltyRates_RecordStatus` | String |  |  |
| 24 | `SC.SETT.PEN.CURR.NO` | `ScSettPenaltyRates_CurrNo` | String |  |  |
| 25 | `SC.SETT.PEN.INPUTTER` | `ScSettPenaltyRates_Inputter` |  |  |  |
| 26 | `SC.SETT.PEN.DATE.TIME` | `ScSettPenaltyRates_DateTime` |  |  |  |
| 27 | `SC.SETT.PEN.AUTHORISER` | `ScSettPenaltyRates_Authoriser` | String |  |  |
| 28 | `SC.SETT.PEN.CO.CODE` | `ScSettPenaltyRates_CoCode` | String |  |  |
| 29 | `SC.SETT.PEN.DEPT.CODE` | `ScSettPenaltyRates_DeptCode` | String |  |  |
| 30 | `SC.SETT.PEN.AUDITOR.CODE` | `ScSettPenaltyRates_AuditorCode` | String |  |  |
| 31 | `SC.SETT.PEN.AUDIT.DATE.TIME` | `ScSettPenaltyRates_AuditDateTime` | String |  |  |
