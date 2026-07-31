# EB.MCI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.MCI.PARAMETER` in `EI_MCI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MCI.PAR.RETENTION.PERIOD` | `EbMciParameter_RetentionPeriod` | TField |  | This field is reserved for future use. |
| 2 | `EB.MCI.PAR.EXECUTION.SIZE` | `EbMciParameter_ExecutionSize` | TField |  | Defines the maximum number of records that can be processed in a single Mass Change Instruction. This can again be specified when setting up an individual Business Operation level but that can never be greater than the Company wide number. |
| 3 | `EB.MCI.PAR.RESERVED.1` | `EbMciParameter_Reserved1` | TField |  |  |
| 4 | `EB.MCI.PAR.RESERVED.2` | `EbMciParameter_Reserved2` | TField |  |  |
| 5 | `EB.MCI.PAR.RESERVED.3` | `EbMciParameter_Reserved3` | TField |  |  |
| 6 | `EB.MCI.PAR.RESERVED.4` | `EbMciParameter_Reserved4` | TField |  |  |
| 7 | `EB.MCI.PAR.RESERVED.5` | `EbMciParameter_Reserved5` | TField |  |  |
| 8 | `EB.MCI.PAR.LOCAL.REF` | `EbMciParameter_LocalRef` |  |  |  |
| 9 | `EB.MCI.PAR.RECORD.STATUS` | `EbMciParameter_RecordStatus` | String |  |  |
| 10 | `EB.MCI.PAR.CURR.NO` | `EbMciParameter_CurrNo` | String |  |  |
| 11 | `EB.MCI.PAR.INPUTTER` | `EbMciParameter_Inputter` |  |  |  |
| 12 | `EB.MCI.PAR.DATE.TIME` | `EbMciParameter_DateTime` |  |  |  |
| 13 | `EB.MCI.PAR.AUTHORISER` | `EbMciParameter_Authoriser` | String |  |  |
| 14 | `EB.MCI.PAR.CO.CODE` | `EbMciParameter_CoCode` | String |  |  |
| 15 | `EB.MCI.PAR.DEPT.CODE` | `EbMciParameter_DeptCode` | String |  |  |
| 16 | `EB.MCI.PAR.AUDITOR.CODE` | `EbMciParameter_AuditorCode` | String |  |  |
| 17 | `EB.MCI.PAR.AUDIT.DATE.TIME` | `EbMciParameter_AuditDateTime` | String |  |  |
