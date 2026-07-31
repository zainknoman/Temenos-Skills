# USLREG.HUD.SCRA — Table Schema

> Source: `INSERTS/I_F.USLREG.HUD.SCRA` in `USLREG_OverdueNotices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLREG.HUDSCRA.HUD.SCRA` | `UslregHudScra_HudScra` | TField |  |  |
| 2 | `USLREG.HUDSCRA.SCRA.PERIOD` | `UslregHudScra_ScraPeriod` | TField |  |  |
| 3 | `USLREG.HUDSCRA.COMPANY.PHONE` | `UslregHudScra_CompanyPhone` | TField |  |  |
| 4 | `USLREG.HUDSCRA.HUD.PHONE` | `UslregHudScra_HudPhone` | TField |  |  |
| 5 | `USLREG.HUDSCRA.SMHC.PHONE` | `UslregHudScra_SmhcPhone` | TField |  |  |
| 6 | `USLREG.HUDSCRA.SMHC.WEBSITE` | `UslregHudScra_SmhcWebsite` | TField |  |  |
| 7 | `USLREG.HUDSCRA.RESERVED.10` | `UslregHudScra_Reserved10` | TField |  |  |
| 8 | `USLREG.HUDSCRA.RESERVED.9` | `UslregHudScra_Reserved9` | TField |  |  |
| 9 | `USLREG.HUDSCRA.RESERVED.8` | `UslregHudScra_Reserved8` | TField |  |  |
| 10 | `USLREG.HUDSCRA.RESERVED.7` | `UslregHudScra_Reserved7` | TField |  |  |
| 11 | `USLREG.HUDSCRA.RESERVED.6` | `UslregHudScra_Reserved6` | TField |  |  |
| 12 | `USLREG.HUDSCRA.RESERVED.5` | `UslregHudScra_Reserved5` | TField |  |  |
| 13 | `USLREG.HUDSCRA.RESERVED.4` | `UslregHudScra_Reserved4` | TField |  |  |
| 14 | `USLREG.HUDSCRA.RESERVED.3` | `UslregHudScra_Reserved3` | TField |  |  |
| 15 | `USLREG.HUDSCRA.RESERVED.2` | `UslregHudScra_Reserved2` | TField |  |  |
| 16 | `USLREG.HUDSCRA.RESERVED.1` | `UslregHudScra_Reserved1` | TField |  |  |
| 17 | `USLREG.HUDSCRA.RECORD.STATUS` | `UslregHudScra_RecordStatus` | String |  |  |
| 18 | `USLREG.HUDSCRA.CURR.NO` | `UslregHudScra_CurrNo` | String |  |  |
| 19 | `USLREG.HUDSCRA.INPUTTER` | `UslregHudScra_Inputter` |  |  |  |
| 20 | `USLREG.HUDSCRA.DATE.TIME` | `UslregHudScra_DateTime` |  |  |  |
| 21 | `USLREG.HUDSCRA.AUTHORISER` | `UslregHudScra_Authoriser` | String |  |  |
| 22 | `USLREG.HUDSCRA.CO.CODE` | `UslregHudScra_CoCode` | String |  |  |
| 23 | `USLREG.HUDSCRA.DEPT.CODE` | `UslregHudScra_DeptCode` | String |  |  |
| 24 | `USLREG.HUDSCRA.AUDITOR.CODE` | `UslregHudScra_AuditorCode` | String |  |  |
| 25 | `USLREG.HUDSCRA.AUDIT.DATE.TIME` | `UslregHudScra_AuditDateTime` | String |  |  |
