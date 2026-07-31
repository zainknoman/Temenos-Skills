# SE.NDBL.APPLICATION — Table Schema

> Source: `INSERTS/I_F.SE.NDBL.APPLICATION` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NDBL.JOB.LIST.ID` | `SeNdblApplication_JobListId` | TField |  |  |
| 2 | `NDBL.AGENT.NUMBER` | `SeNdblApplication_AgentNumber` | TField |  |  |
| 3 | `NDBL.TIME.DETAILS` | `SeNdblApplication_TimeDetails` | TField |  |  |
| 4 | `NDBL.RESERVED.10` | `SeNdblApplication_Reserved10` | TField |  |  |
| 5 | `NDBL.RESERVED.09` | `SeNdblApplication_Reserved09` | TField |  |  |
| 6 | `NDBL.RESERVED.08` | `SeNdblApplication_Reserved08` | TField |  |  |
| 7 | `NDBL.RESERVED.07` | `SeNdblApplication_Reserved07` | TField |  |  |
| 8 | `NDBL.RESERVED.06` | `SeNdblApplication_Reserved06` | TField |  |  |
| 9 | `NDBL.RESERVED.05` | `SeNdblApplication_Reserved05` | TField |  |  |
| 10 | `NDBL.RESERVED.04` | `SeNdblApplication_Reserved04` | TField |  |  |
| 11 | `NDBL.RESERVED.03` | `SeNdblApplication_Reserved03` | TField |  |  |
| 12 | `NDBL.RESERVED.02` | `SeNdblApplication_Reserved02` | TField |  |  |
| 13 | `NDBL.RESERVED.01` | `SeNdblApplication_Reserved01` | TField |  |  |
| 14 | `NDBL.RECORD.STATUS` | `SeNdblApplication_RecordStatus` | String |  |  |
| 15 | `NDBL.CURR.NO` | `SeNdblApplication_CurrNo` | String |  |  |
| 16 | `NDBL.INPUTTER` | `SeNdblApplication_Inputter` |  |  |  |
| 17 | `NDBL.DATE.TIME` | `SeNdblApplication_DateTime` |  |  |  |
| 18 | `NDBL.AUTHORISER` | `SeNdblApplication_Authoriser` | String |  |  |
| 19 | `NDBL.CO.CODE` | `SeNdblApplication_CoCode` | String |  |  |
| 20 | `NDBL.DEPT.CODE` | `SeNdblApplication_DeptCode` | String |  |  |
| 21 | `NDBL.AUDITOR.CODE` | `SeNdblApplication_AuditorCode` | String |  |  |
| 22 | `NDBL.AUDIT.DATE.TIME` | `SeNdblApplication_AuditDateTime` | String |  |  |
