# UKCRSR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.UKCRSR.PARAMETER` in `UKCRSR_CRSReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKCRSR.AEOI.ID` | `UkcrsrParameter_AeoiId` | TField |  |  |
| 2 | `UKCRSR.FI.REGISTER.ID` | `UkcrsrParameter_FiRegisterId` | TField |  |  |
| 3 | `UKCRSR.DUE.DILIGENCE.INDICATOR` | `UkcrsrParameter_DueDiligenceIndicator` | TField |  |  |
| 4 | `UKCRSR.THERSHOLD.INDICATOR` | `UkcrsrParameter_ThersholdIndicator` | TField |  |  |
| 5 | `UKCRSR.INSURANCE.ELECTION` | `UkcrsrParameter_InsuranceElection` | TField |  |  |
| 6 | `UKCRSR.DORMANT.ACC.ELECTION` | `UkcrsrParameter_DormantAccElection` | TField |  |  |
| 7 | `UKCRSR.RESERVED1` | `UkcrsrParameter_Reserved1` | TField |  |  |
| 8 | `UKCRSR.RESERVED2` | `UkcrsrParameter_Reserved2` | TField |  |  |
| 9 | `UKCRSR.RESERVED3` | `UkcrsrParameter_Reserved3` | TField |  |  |
| 10 | `UKCRSR.RESERVED4` | `UkcrsrParameter_Reserved4` | TField |  |  |
| 11 | `UKCRSR.RESERVED5` | `UkcrsrParameter_Reserved5` | TField |  |  |
| 12 | `UKCRSR.RESERVED6` | `UkcrsrParameter_Reserved6` | TField |  |  |
| 13 | `UKCRSR.RESERVED7` | `UkcrsrParameter_Reserved7` | TField |  |  |
| 14 | `UKCRSR.RESERVED8` | `UkcrsrParameter_Reserved8` | TField |  |  |
| 15 | `UKCRSR.RESERVED9` | `UkcrsrParameter_Reserved9` | TField |  |  |
| 16 | `UKCRSR.RESERVED10` | `UkcrsrParameter_Reserved10` | TField |  |  |
| 17 | `UKCRSR.OVERRIDE` | `UkcrsrParameter_Override` |  |  |  |
| 18 | `UKCRSR.RECORD.STATUS` | `UkcrsrParameter_RecordStatus` | String |  |  |
| 19 | `UKCRSR.CURR.NO` | `UkcrsrParameter_CurrNo` | String |  |  |
| 20 | `UKCRSR.INPUTTER` | `UkcrsrParameter_Inputter` |  |  |  |
| 21 | `UKCRSR.DATE.TIME` | `UkcrsrParameter_DateTime` |  |  |  |
| 22 | `UKCRSR.AUTHORISER` | `UkcrsrParameter_Authoriser` | String |  |  |
| 23 | `UKCRSR.CO.CODE` | `UkcrsrParameter_CoCode` | String |  |  |
| 24 | `UKCRSR.DEPT.CODE` | `UkcrsrParameter_DeptCode` | String |  |  |
| 25 | `UKCRSR.AUDITOR.CODE` | `UkcrsrParameter_AuditorCode` | String |  |  |
| 26 | `UKCRSR.AUDIT.DATE.TIME` | `UkcrsrParameter_AuditDateTime` | String |  |  |
