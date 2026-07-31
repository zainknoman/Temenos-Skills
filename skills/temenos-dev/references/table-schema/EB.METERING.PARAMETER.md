# EB.METERING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.METERING.PARAMETER` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MET.PAR.DESCRIPTION` | `EbMeteringParameter_Description` | TField | Yes | This field is used to give a description for Parameter It is a mandatory field |
| 2 | `MET.PAR.METRIC.NAME` | `EbMeteringParameter_MetricName` |  |  |  |
| 3 | `MET.PAR.OPEN.BRACKET` | `EbMeteringParameter_OpenBracket` |  |  |  |
| 4 | `MET.PAR.SELECTION.FIELD` | `EbMeteringParameter_SelectionField` |  |  |  |
| 5 | `MET.PAR.OPERAND` | `EbMeteringParameter_Operand` |  |  |  |
| 6 | `MET.PAR.SELECTION.VALUE` | `EbMeteringParameter_SelectionValue` |  |  |  |
| 7 | `MET.PAR.RESERVEDFLD.6` | `EbMeteringParameter_Reservedfld6` |  |  |  |
| 8 | `MET.PAR.RESERVEDFLD.5` | `EbMeteringParameter_Reservedfld5` |  |  |  |
| 9 | `MET.PAR.RESERVEDFLD.4` | `EbMeteringParameter_Reservedfld4` |  |  |  |
| 10 | `MET.PAR.RESERVEDFLD.3` | `EbMeteringParameter_Reservedfld3` |  |  |  |
| 11 | `MET.PAR.RESERVEDFLD.2` | `EbMeteringParameter_Reservedfld2` |  |  |  |
| 12 | `MET.PAR.RESERVEDFLD.1` | `EbMeteringParameter_Reservedfld1` |  |  |  |
| 13 | `MET.PAR.CLOSE.BRACKET` | `EbMeteringParameter_CloseBracket` |  |  |  |
| 14 | `MET.PAR.JOIN` | `EbMeteringParameter_Join` |  |  |  |
| 15 | `MET.PAR.GROUP.BY.FIELD` | `EbMeteringParameter_GroupByField` |  |  |  |
| 16 | `MET.PAR.SELECT.STMT` | `EbMeteringParameter_SelectStmt` |  |  |  |
| 17 | `MET.PAR.COMPANIES` | `EbMeteringParameter_Companies` |  |  |  |
| 18 | `MET.PAR.RESERVED.15` | `EbMeteringParameter_Reserved15` | TField |  |  |
| 19 | `MET.PAR.RESERVED.14` | `EbMeteringParameter_Reserved14` | TField |  |  |
| 20 | `MET.PAR.RESERVED.13` | `EbMeteringParameter_Reserved13` | TField |  |  |
| 21 | `MET.PAR.RESERVED.12` | `EbMeteringParameter_Reserved12` | TField |  |  |
| 22 | `MET.PAR.RESERVED.11` | `EbMeteringParameter_Reserved11` | TField |  |  |
| 23 | `MET.PAR.RESERVED.10` | `EbMeteringParameter_Reserved10` | TField |  |  |
| 24 | `MET.PAR.RESERVED.9` | `EbMeteringParameter_Reserved9` | TField |  |  |
| 25 | `MET.PAR.RESERVED.8` | `EbMeteringParameter_Reserved8` | TField |  |  |
| 26 | `MET.PAR.RESERVED.7` | `EbMeteringParameter_Reserved7` | TField |  |  |
| 27 | `MET.PAR.RESERVED.6` | `EbMeteringParameter_Reserved6` | TField |  |  |
| 28 | `MET.PAR.RESERVED.5` | `EbMeteringParameter_Reserved5` | TField |  |  |
| 29 | `MET.PAR.RESERVED.4` | `EbMeteringParameter_Reserved4` | TField |  |  |
| 30 | `MET.PAR.RESERVED.3` | `EbMeteringParameter_Reserved3` | TField |  |  |
| 31 | `MET.PAR.RESERVED.2` | `EbMeteringParameter_Reserved2` | TField |  |  |
| 32 | `MET.PAR.RESERVED.1` | `EbMeteringParameter_Reserved1` | TField |  |  |
| 33 | `MET.PAR.RECORD.STATUS` | `EbMeteringParameter_RecordStatus` | String |  |  |
| 34 | `MET.PAR.CURR.NO` | `EbMeteringParameter_CurrNo` | String |  |  |
| 35 | `MET.PAR.INPUTTER` | `EbMeteringParameter_Inputter` |  |  |  |
| 36 | `MET.PAR.DATE.TIME` | `EbMeteringParameter_DateTime` |  |  |  |
| 37 | `MET.PAR.AUTHORISER` | `EbMeteringParameter_Authoriser` | String |  |  |
| 38 | `MET.PAR.CO.CODE` | `EbMeteringParameter_CoCode` | String |  |  |
| 39 | `MET.PAR.DEPT.CODE` | `EbMeteringParameter_DeptCode` | String |  |  |
| 40 | `MET.PAR.AUDITOR.CODE` | `EbMeteringParameter_AuditorCode` | String |  |  |
| 41 | `MET.PAR.AUDIT.DATE.TIME` | `EbMeteringParameter_AuditDateTime` | String |  |  |
