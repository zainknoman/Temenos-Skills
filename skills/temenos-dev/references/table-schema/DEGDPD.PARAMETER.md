# DEGDPD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DEGDPD.PARAMETER` in `DEGDPD_AccountReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEGDPD.PARAMETER.CATEGORY.START` | `DegdpdParameter_CategoryStart` |  |  |  |
| 2 | `DEGDPD.PARAMETER.CATEGORY.END` | `DegdpdParameter_CategoryEnd` |  |  |  |
| 3 | `DEGDPD.PARAMETER.RESERVED.8` | `DegdpdParameter_Reserved8` | TField |  |  |
| 4 | `DEGDPD.PARAMETER.RESERVED.7` | `DegdpdParameter_Reserved7` | TField |  |  |
| 5 | `DEGDPD.PARAMETER.RESERVED.6` | `DegdpdParameter_Reserved6` | TField |  |  |
| 6 | `DEGDPD.PARAMETER.RESERVED.5` | `DegdpdParameter_Reserved5` | TField |  |  |
| 7 | `DEGDPD.PARAMETER.RESERVED.4` | `DegdpdParameter_Reserved4` | TField |  |  |
| 8 | `DEGDPD.PARAMETER.RESERVED.3` | `DegdpdParameter_Reserved3` | TField |  |  |
| 9 | `DEGDPD.PARAMETER.RESERVED.2` | `DegdpdParameter_Reserved2` | TField |  |  |
| 10 | `DEGDPD.PARAMETER.RESERVED.1` | `DegdpdParameter_Reserved1` | TField |  |  |
| 11 | `DEGDPD.PARAMETER.LOCAL.REF` | `DegdpdParameter_LocalRef` |  |  |  |
| 12 | `DEGDPD.PARAMETER.OVERRIDE` | `DegdpdParameter_Override` |  |  |  |
| 13 | `DEGDPD.PARAMETER.RECORD.STATUS` | `DegdpdParameter_RecordStatus` | String |  |  |
| 14 | `DEGDPD.PARAMETER.CURR.NO` | `DegdpdParameter_CurrNo` | String |  |  |
| 15 | `DEGDPD.PARAMETER.INPUTTER` | `DegdpdParameter_Inputter` |  |  |  |
| 16 | `DEGDPD.PARAMETER.DATE.TIME` | `DegdpdParameter_DateTime` |  |  |  |
| 17 | `DEGDPD.PARAMETER.AUTHORISER` | `DegdpdParameter_Authoriser` | String |  |  |
| 18 | `DEGDPD.PARAMETER.CO.CODE` | `DegdpdParameter_CoCode` | String |  |  |
| 19 | `DEGDPD.PARAMETER.DEPT.CODE` | `DegdpdParameter_DeptCode` | String |  |  |
| 20 | `DEGDPD.PARAMETER.AUDITOR.CODE` | `DegdpdParameter_AuditorCode` | String |  |  |
| 21 | `DEGDPD.PARAMETER.AUDIT.DATE.TIME` | `DegdpdParameter_AuditDateTime` | String |  |  |
