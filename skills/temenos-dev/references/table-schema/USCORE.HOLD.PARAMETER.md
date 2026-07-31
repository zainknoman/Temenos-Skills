# USCORE.HOLD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USCORE.HOLD.PARAMETER` in `USCORE_Holds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.HLD.PAR.DESCRIPTION` | `UscoreHoldParameter_Description` |  |  |  |
| 2 | `US.HLD.PAR.EXPIRATION.PERIOD` | `UscoreHoldParameter_ExpirationPeriod` | TField |  | Field to define the expiration period. Value can be defined in days, weeks, months or years. Example: 5D, 2W, 3M or 1Y. |
| 3 | `US.HLD.PAR.PERIOD.TYPE` | `UscoreHoldParameter_PeriodType` | TField |  | If the Expiration Period is defined in days, then user will be prompted to select one of the two values in this field: Calendar Day or Business Day. Based on which it will be determined whether the Expiration Period. |
| 4 | `US.HLD.PAR.HOLD.FULL.BALANCE` | `UscoreHoldParameter_HoldFullBalance` | TField |  | If marked as YES, then entire balance in the account will be held. If marked as NULL, then user would need to manually update Hold amount at the Hold transaction input level. |
| 5 | `US.HLD.PAR.RESERVED.9` | `UscoreHoldParameter_Reserved9` |  |  |  |
| 6 | `US.HLD.PAR.RESERVED.8` | `UscoreHoldParameter_Reserved8` | TField |  |  |
| 7 | `US.HLD.PAR.RESERVED.7` | `UscoreHoldParameter_Reserved7` | TField |  |  |
| 8 | `US.HLD.PAR.RESERVED.6` | `UscoreHoldParameter_Reserved6` | TField |  |  |
| 9 | `US.HLD.PAR.RESERVED.5` | `UscoreHoldParameter_Reserved5` | TField |  |  |
| 10 | `US.HLD.PAR.RESERVED.4` | `UscoreHoldParameter_Reserved4` | TField |  |  |
| 11 | `US.HLD.PAR.RESERVED.3` | `UscoreHoldParameter_Reserved3` | TField |  |  |
| 12 | `US.HLD.PAR.RESERVED.2` | `UscoreHoldParameter_Reserved2` | TField |  |  |
| 13 | `US.HLD.PAR.RESERVED.1` | `UscoreHoldParameter_Reserved1` | TField |  |  |
| 14 | `US.HLD.PAR.LOCAL.REF` | `UscoreHoldParameter_LocalRef` |  |  |  |
| 15 | `US.HLD.PAR.OVERRIDE` | `UscoreHoldParameter_Override` |  |  |  |
| 16 | `US.HLD.PAR.RECORD.STATUS` | `UscoreHoldParameter_RecordStatus` | String |  |  |
| 17 | `US.HLD.PAR.CURR.NO` | `UscoreHoldParameter_CurrNo` | String |  |  |
| 18 | `US.HLD.PAR.INPUTTER` | `UscoreHoldParameter_Inputter` |  |  |  |
| 19 | `US.HLD.PAR.DATE.TIME` | `UscoreHoldParameter_DateTime` |  |  |  |
| 20 | `US.HLD.PAR.AUTHORISER` | `UscoreHoldParameter_Authoriser` | String |  |  |
| 21 | `US.HLD.PAR.CO.CODE` | `UscoreHoldParameter_CoCode` | String |  |  |
| 22 | `US.HLD.PAR.DEPT.CODE` | `UscoreHoldParameter_DeptCode` | String |  |  |
| 23 | `US.HLD.PAR.AUDITOR.CODE` | `UscoreHoldParameter_AuditorCode` | String |  |  |
| 24 | `US.HLD.PAR.AUDIT.DATE.TIME` | `UscoreHoldParameter_AuditDateTime` | String |  |  |
