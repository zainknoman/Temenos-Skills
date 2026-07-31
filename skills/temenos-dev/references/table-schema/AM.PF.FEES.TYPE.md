# AM.PF.FEES.TYPE — Table Schema

> Source: `INSERTS/I_F.AM.PF.FEES.TYPE` in `AM_PerformanceFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PFT.DESCRIPTION` | `AmPfFeesType_Description` |  |  |  |
| 2 | `AM.PFT.EFFECTIVE.DATE` | `AmPfFeesType_EffectiveDate` | TField |  | Effective date of this change. Should be either today or forward. |
| 3 | `AM.PFT.BENCHMARK` | `AmPfFeesType_Benchmark` | TField |  | Its a Valid record in AM.BENCHMARK |
| 4 | `AM.PFT.FLAT.RATE` | `AmPfFeesType_FlatRate` | TField |  | Flat rate to calculate the performance fees. |
| 5 | `AM.PFT.FT.COMM.TYPE` | `AmPfFeesType_FtCommType` | TField | Yes | The valid record from FT.COMMISSION.TYPE. Either FLAT.RATE or FT.COMM.TYPE is mandatory. |
| 6 | `AM.PFT.RESERVED.10` | `AmPfFeesType_Reserved10` | TField |  |  |
| 7 | `AM.PFT.RESERVED.9` | `AmPfFeesType_Reserved9` | TField |  |  |
| 8 | `AM.PFT.RESERVED.8` | `AmPfFeesType_Reserved8` | TField |  |  |
| 9 | `AM.PFT.RESERVED.7` | `AmPfFeesType_Reserved7` | TField |  |  |
| 10 | `AM.PFT.RESERVED.6` | `AmPfFeesType_Reserved6` | TField |  |  |
| 11 | `AM.PFT.RESERVED.5` | `AmPfFeesType_Reserved5` | TField |  |  |
| 12 | `AM.PFT.RESERVED.4` | `AmPfFeesType_Reserved4` | TField |  |  |
| 13 | `AM.PFT.RESERVED.3` | `AmPfFeesType_Reserved3` | TField |  |  |
| 14 | `AM.PFT.RESERVED.2` | `AmPfFeesType_Reserved2` | TField |  |  |
| 15 | `AM.PFT.RESERVED.1` | `AmPfFeesType_Reserved1` | TField |  |  |
| 16 | `AM.PFT.RECORD.STATUS` | `AmPfFeesType_RecordStatus` | String |  |  |
| 17 | `AM.PFT.CURR.NO` | `AmPfFeesType_CurrNo` | String |  |  |
| 18 | `AM.PFT.INPUTTER` | `AmPfFeesType_Inputter` |  |  |  |
| 19 | `AM.PFT.DATE.TIME` | `AmPfFeesType_DateTime` |  |  |  |
| 20 | `AM.PFT.AUTHORISER` | `AmPfFeesType_Authoriser` | String |  |  |
| 21 | `AM.PFT.CO.CODE` | `AmPfFeesType_CoCode` | String |  |  |
| 22 | `AM.PFT.DEPT.CODE` | `AmPfFeesType_DeptCode` | String |  |  |
| 23 | `AM.PFT.AUDITOR.CODE` | `AmPfFeesType_AuditorCode` | String |  |  |
| 24 | `AM.PFT.AUDIT.DATE.TIME` | `AmPfFeesType_AuditDateTime` | String |  |  |
