# PC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PC.PARAMETER` in `PC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PC.PCP.DBASE.NAME` | `PcParameter_DbaseName` | TField | Yes | Enter a path where the Post Closing Database for this period will be created. Mandatory for parameter of master company. For other lead companies, value is copied from master company parameter. Validation Rules: The pathname specified must be a valid, existing path. Mandatory for parameter of master company. No input for other lead companies. The mandatory property of this field is relaxed with new license code (PCC). The auto-creation and closure of PC database and PC.PERIOD will depend on the availability of the data base path defined in this field. This field will be blocked for input once the database path is defined |
| 2 | `PC.PCP.CYCLE.FREQUENCY` | `PcParameter_CycleFrequency` | TField | Conditional | Frequency based on which Post Closing period is created for the company. Date of frequency is cycled when Post Closing creation job has run for the current frequency date. Validation Rules: Frequency can be Monthly, Quarterly, Half-yearly or Yearly. It can also be a specific occurrence such as last of Quarter. Optional for master company. Mandatory for other lead companies. If not defined for master company then PC.PERIOD will not be created for master company. Path given in DBase Name will be used while creating PC.PERIOD for lead companies. If contract adjustment is enabled, then this field becomes mandatory and the frequencies supported will be monthly, quarterly, half yearly or yearly but with the last date of the month (Eg: M0131, M0331, M0631 and M1231). |
| 3 | `PC.PCP.LAST.PC.DATE` | `PcParameter_LastPcDate` |  |  |  |
| 4 | `PC.PCP.STATUS` | `PcParameter_Status` |  |  |  |
| 5 | `PC.PCP.NEXT.FREQ.DATE` | `PcParameter_NextFreqDate` | TField |  | Next date for which Post Closing period should be created. This field is updated based on the frequency defined. Validation Rules: No input field. Automatically updated by the system. |
| 6 | `PC.PCP.RECORD.STATUS` | `PcParameter_RecordStatus` | String |  |  |
| 7 | `PC.PCP.CURR.NO` | `PcParameter_CurrNo` | String |  |  |
| 8 | `PC.PCP.INPUTTER` | `PcParameter_Inputter` |  |  |  |
| 9 | `PC.PCP.DATE.TIME` | `PcParameter_DateTime` |  |  |  |
| 10 | `PC.PCP.AUTHORISER` | `PcParameter_Authoriser` | String |  |  |
| 11 | `PC.PCP.CO.CODE` | `PcParameter_CoCode` | String |  |  |
| 12 | `PC.PCP.DEPT.CODE` | `PcParameter_DeptCode` | String |  |  |
| 13 | `PC.PCP.AUDITOR.CODE` | `PcParameter_AuditorCode` | String |  |  |
| 14 | `PC.PCP.AUDIT.DATE.TIME` | `PcParameter_AuditDateTime` | String |  |  |
