# PC.PERIOD — Table Schema

> Source: `INSERTS/I_F.PC.PERIOD` in `PC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PC.PER.PERIOD.STATUS` | `PcPeriod_PeriodStatus` | TField |  | Reflects the status of the period end If the period is closed, any adjustments posted to this period will be lost or ignored.Once closed,you may not alter this status,or any other field on the PC.PERIOD application Validation Rules: Must be OPEN or CLOSED You may not close a period whilst a previous one remains open A period cannot be closed when there are outstanding postings pending on the period you are trying to close,or a previous one |
| 2 | `PC.PER.COMPANY` | `PcPeriod_Company` |  |  |  |
| 3 | `PC.PER.COMP.STATUS` | `PcPeriod_CompStatus` |  |  |  |
| 4 | `PC.PER.DBASE.PATHNAME` | `PcPeriod_DbasePathname` | TField | Yes | Enter a path where the Post Closing Database for this period will be created. This is a mandatory field Validation Rules: The pathname specified must be a valid, existing path |
| 5 | `PC.PER.RESERVED.1` | `PcPeriod_Reserved1` | TField |  |  |
| 6 | `PC.PER.LOCAL.REF` | `PcPeriod_LocalRef` |  |  |  |
| 7 | `PC.PER.RESERVED.3` | `PcPeriod_Reserved3` | TField |  |  |
| 8 | `PC.PER.RECORD.STATUS` | `PcPeriod_RecordStatus` | String |  |  |
| 9 | `PC.PER.CURR.NO` | `PcPeriod_CurrNo` | String |  |  |
| 10 | `PC.PER.INPUTTER` | `PcPeriod_Inputter` |  |  |  |
| 11 | `PC.PER.DATE.TIME` | `PcPeriod_DateTime` |  |  |  |
| 12 | `PC.PER.AUTHORISER` | `PcPeriod_Authoriser` | String |  |  |
| 13 | `PC.PER.CO.CODE` | `PcPeriod_CoCode` | String |  |  |
| 14 | `PC.PER.DEPT.CODE` | `PcPeriod_DeptCode` | String |  |  |
| 15 | `PC.PER.AUDITOR.CODE` | `PcPeriod_AuditorCode` | String |  |  |
| 16 | `PC.PER.AUDIT.DATE.TIME` | `PcPeriod_AuditDateTime` | String |  |  |
