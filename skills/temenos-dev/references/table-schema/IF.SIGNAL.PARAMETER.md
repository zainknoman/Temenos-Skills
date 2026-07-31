# IF.SIGNAL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.IF.SIGNAL.PARAMETER` in `IF_RuntimeFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.SIG.SIGNAL.NAME` | `IfSignalParameter_SignalName` |  |  |  |
| 2 | `IF.SIG.SIGNAL.VALUE` | `IfSignalParameter_SignalValue` |  |  |  |
| 3 | `IF.SIG.RESERVED.2` | `IfSignalParameter_Reserved2` |  |  |  |
| 4 | `IF.SIG.RESERVED.3` | `IfSignalParameter_Reserved3` |  |  |  |
| 5 | `IF.SIG.RESERVED.4` | `IfSignalParameter_Reserved4` |  |  |  |
| 6 | `IF.SIG.RESERVED.5` | `IfSignalParameter_Reserved5` |  |  |  |
| 7 | `IF.SIG.RESERVED.6` | `IfSignalParameter_Reserved6` |  |  |  |
| 8 | `IF.SIG.SIGNAL.MESSAGE` | `IfSignalParameter_SignalMessage` |  |  |  |
| 9 | `IF.SIG.FREQUENCY` | `IfSignalParameter_Frequency` | TField |  | Overview This indicates the Frequency of the signal. Validation Rules This field can have the below values: D - Every working day. Dnn - Every nnth working day. The possible frequencies can be D1, D2, D3,.. M - Last weekend of every month. Mnn - Every nnth day of each month or on the previous weekend day. The possible frequencies can be M2, M3,..,M31 W - Every friday or previous working day. Y - Last weekend day of the year. Ynn - Last weekend day of the nnth month in the year. The possible frequencies can be Y1, Y2, Y3,..,Y12 Input allowed. |
| 10 | `IF.SIG.LAST.RUN.DATE` | `IfSignalParameter_LastRunDate` | TField |  |  |
| 11 | `IF.SIG.NEXT.RUN.DATE` | `IfSignalParameter_NextRunDate` | TField |  |  |
| 12 | `IF.SIG.RESERVED.10` | `IfSignalParameter_Reserved10` | TField |  |  |
| 13 | `IF.SIG.RESERVED.11` | `IfSignalParameter_Reserved11` | TField |  |  |
| 14 | `IF.SIG.RESERVED.12` | `IfSignalParameter_Reserved12` | TField |  |  |
| 15 | `IF.SIG.RESERVED.13` | `IfSignalParameter_Reserved13` | TField |  |  |
| 16 | `IF.SIG.RESERVED.14` | `IfSignalParameter_Reserved14` | TField |  |  |
| 17 | `IF.SIG.OVERRIDE` | `IfSignalParameter_Override` |  |  |  |
| 18 | `IF.SIG.RECORD.STATUS` | `IfSignalParameter_RecordStatus` | String |  |  |
| 19 | `IF.SIG.CURR.NO` | `IfSignalParameter_CurrNo` | String |  |  |
| 20 | `IF.SIG.INPUTTER` | `IfSignalParameter_Inputter` |  |  |  |
| 21 | `IF.SIG.DATE.TIME` | `IfSignalParameter_DateTime` |  |  |  |
| 22 | `IF.SIG.AUTHORISER` | `IfSignalParameter_Authoriser` | String |  |  |
| 23 | `IF.SIG.CO.CODE` | `IfSignalParameter_CoCode` | String |  |  |
| 24 | `IF.SIG.DEPT.CODE` | `IfSignalParameter_DeptCode` | String |  |  |
| 25 | `IF.SIG.AUDITOR.CODE` | `IfSignalParameter_AuditorCode` | String |  |  |
| 26 | `IF.SIG.AUDIT.DATE.TIME` | `IfSignalParameter_AuditDateTime` | String |  |  |
