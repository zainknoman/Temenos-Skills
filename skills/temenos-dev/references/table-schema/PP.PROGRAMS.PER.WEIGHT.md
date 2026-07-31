# PP.PROGRAMS.PER.WEIGHT — Table Schema

> Source: `INSERTS/I_F.PP.PROGRAMS.PER.WEIGHT` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PGW.CompanyID` | `PpProgramsPerWeight_Companyid` | TField |  | Indicates the Financial Table Descriptive(FTD) company for which the record is created. This is the NoInput field It gets autopopulated after the validation Example : BNK,GB1 |
| 2 | `PP.PGW.Ranking` | `PpProgramsPerWeight_Ranking` |  |  |  |
| 3 | `PP.PGW.SpecificWeightCode` | `PpProgramsPerWeight_Specificweightcode` |  |  |  |
| 4 | `PP.PGW.ProgramName` | `PpProgramsPerWeight_Programname` |  |  |  |
| 5 | `PP.PGW.ProgramsPerWeightDescription` | `PpProgramsPerWeight_Programsperweightdescription` |  |  |  |
| 6 | `PP.PGW.ProgramSkipIndicator` | `PpProgramsPerWeight_Programskipindicator` |  |  |  |
| 7 | `PP.PGW.RESERVED.5` | `PpProgramsPerWeight_Reserved5` | TField |  |  |
| 8 | `PP.PGW.RESERVED.4` | `PpProgramsPerWeight_Reserved4` | TField |  |  |
| 9 | `PP.PGW.RESERVED.3` | `PpProgramsPerWeight_Reserved3` | TField |  |  |
| 10 | `PP.PGW.RESERVED.2` | `PpProgramsPerWeight_Reserved2` | TField |  |  |
| 11 | `PP.PGW.RESERVED.1` | `PpProgramsPerWeight_Reserved1` | TField |  |  |
| 12 | `PP.PGW.LOCAL.REF` | `PpProgramsPerWeight_LocalRef` |  |  |  |
| 13 | `PP.PGW.OVERRIDE` | `PpProgramsPerWeight_Override` |  |  |  |
| 14 | `PP.PGW.RECORD.STATUS` | `PpProgramsPerWeight_RecordStatus` | String |  |  |
| 15 | `PP.PGW.CURR.NO` | `PpProgramsPerWeight_CurrNo` | String |  |  |
| 16 | `PP.PGW.INPUTTER` | `PpProgramsPerWeight_Inputter` |  |  |  |
| 17 | `PP.PGW.DATE.TIME` | `PpProgramsPerWeight_DateTime` |  |  |  |
| 18 | `PP.PGW.AUTHORISER` | `PpProgramsPerWeight_Authoriser` | String |  |  |
| 19 | `PP.PGW.CO.CODE` | `PpProgramsPerWeight_CoCode` | String |  |  |
| 20 | `PP.PGW.DEPT.CODE` | `PpProgramsPerWeight_DeptCode` | String |  |  |
| 21 | `PP.PGW.AUDITOR.CODE` | `PpProgramsPerWeight_AuditorCode` | String |  |  |
| 22 | `PP.PGW.AUDIT.DATE.TIME` | `PpProgramsPerWeight_AuditDateTime` | String |  |  |
