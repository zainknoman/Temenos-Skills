# DC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DC.PARAMETER` in `DC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DC.PA.DC.POS.TYPE` | `DcParameter_DcPosType` |  |  |  |
| 2 | `DC.PA.DC.SUSP.CATEG` | `DcParameter_DcSuspCateg` |  |  |  |
| 3 | `DC.PA.DC.DIFF.CATEG` | `DcParameter_DcDiffCateg` |  |  |  |
| 4 | `DC.PA.DC.CONT.SUS.CAT` | `DcParameter_DcContSusCat` |  |  |  |
| 5 | `DC.PA.DC.CONT.DIF.CAT` | `DcParameter_DcContDifCat` |  |  |  |
| 6 | `DC.PA.RESERVED.10` | `DcParameter_Reserved10` | TField |  |  |
| 7 | `DC.PA.RESERVED.9` | `DcParameter_Reserved9` | TField |  |  |
| 8 | `DC.PA.RESERVED.8` | `DcParameter_Reserved8` | TField |  |  |
| 9 | `DC.PA.RESERVED.7` | `DcParameter_Reserved7` | TField |  |  |
| 10 | `DC.PA.RESERVED.6` | `DcParameter_Reserved6` | TField |  |  |
| 11 | `DC.PA.RESERVED.5` | `DcParameter_Reserved5` | TField |  |  |
| 12 | `DC.PA.RESERVED.4` | `DcParameter_Reserved4` | TField |  |  |
| 13 | `DC.PA.RESERVED.3` | `DcParameter_Reserved3` | TField |  |  |
| 14 | `DC.PA.RESERVED.2` | `DcParameter_Reserved2` | TField |  |  |
| 15 | `DC.PA.RESERVED.1` | `DcParameter_Reserved1` | TField |  |  |
| 16 | `DC.PA.OVERRIDE` | `DcParameter_Override` |  |  |  |
| 17 | `DC.PA.RECORD.STATUS` | `DcParameter_RecordStatus` | String |  |  |
| 18 | `DC.PA.CURR.NO` | `DcParameter_CurrNo` | String |  |  |
| 19 | `DC.PA.INPUTTER` | `DcParameter_Inputter` |  |  |  |
| 20 | `DC.PA.DATE.TIME` | `DcParameter_DateTime` |  |  |  |
| 21 | `DC.PA.AUTHORISER` | `DcParameter_Authoriser` | String |  |  |
| 22 | `DC.PA.CO.CODE` | `DcParameter_CoCode` | String |  |  |
| 23 | `DC.PA.DEPT.CODE` | `DcParameter_DeptCode` | String |  |  |
| 24 | `DC.PA.AUDITOR.CODE` | `DcParameter_AuditorCode` | String |  |  |
| 25 | `DC.PA.AUDIT.DATE.TIME` | `DcParameter_AuditDateTime` | String |  |  |
