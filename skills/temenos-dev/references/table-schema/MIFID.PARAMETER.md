# MIFID.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MIFID.PARAMETER` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.PARAM.DROP.PCT.VAL` | `MifidParameter_DropPctVal` | TField |  | This field stores the % drop in portfolio value (and multiples) that should be recorded for MiFID II purpose. |
| 2 | `MIFID.PARAM.PERF.LVL` | `MifidParameter_PerfLvl` | TField |  | This field indicates the level at which the performance needs to be computed. If group is selected, the group performance is considered while if Portfolio is selected, the portfolio performance is considered. |
| 3 | `MIFID.PARAM.REP.FREQ` | `MifidParameter_RepFreq` | TField |  | The field to indicate the reporting frequency at which the COB reports pertaining to Portfolio performance and TER costs would be extracted. Can be a T24 standard Frequency field. |
| 4 | `MIFID.PARAM.COMM.TXN.CODES` | `MifidParameter_CommTxnCodes` |  |  |  |
| 5 | `MIFID.PARAM.LOCAL.REF` | `MifidParameter_LocalRef` |  |  |  |
| 6 | `MIFID.PARAM.RESERVED.10` | `MifidParameter_Reserved10` | TField |  |  |
| 7 | `MIFID.PARAM.RESERVED.9` | `MifidParameter_Reserved9` | TField |  |  |
| 8 | `MIFID.PARAM.RESERVED.8` | `MifidParameter_Reserved8` | TField |  |  |
| 9 | `MIFID.PARAM.RESERVED.7` | `MifidParameter_Reserved7` | TField |  |  |
| 10 | `MIFID.PARAM.RESERVED.6` | `MifidParameter_Reserved6` | TField |  |  |
| 11 | `MIFID.PARAM.RESERVED.5` | `MifidParameter_Reserved5` | TField |  |  |
| 12 | `MIFID.PARAM.RESERVED.4` | `MifidParameter_Reserved4` | TField |  |  |
| 13 | `MIFID.PARAM.RESERVED.3` | `MifidParameter_Reserved3` | TField |  |  |
| 14 | `MIFID.PARAM.RESERVED.2` | `MifidParameter_Reserved2` | TField |  |  |
| 15 | `MIFID.PARAM.RESERVED.1` | `MifidParameter_Reserved1` | TField |  |  |
| 16 | `MIFID.PARAM.OVERRIDE` | `MifidParameter_Override` |  |  |  |
| 17 | `MIFID.PARAM.RECORD.STATUS` | `MifidParameter_RecordStatus` | String |  |  |
| 18 | `MIFID.PARAM.CURR.NO` | `MifidParameter_CurrNo` | String |  |  |
| 19 | `MIFID.PARAM.INPUTTER` | `MifidParameter_Inputter` |  |  |  |
| 20 | `MIFID.PARAM.DATE.TIME` | `MifidParameter_DateTime` |  |  |  |
| 21 | `MIFID.PARAM.AUTHORISER` | `MifidParameter_Authoriser` | String |  |  |
| 22 | `MIFID.PARAM.CO.CODE` | `MifidParameter_CoCode` | String |  |  |
| 23 | `MIFID.PARAM.DEPT.CODE` | `MifidParameter_DeptCode` | String |  |  |
| 24 | `MIFID.PARAM.AUDITOR.CODE` | `MifidParameter_AuditorCode` | String |  |  |
| 25 | `MIFID.PARAM.AUDIT.DATE.TIME` | `MifidParameter_AuditDateTime` | String |  |  |
