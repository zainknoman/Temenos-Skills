# PP.PROGRAM.CHARACTERISTIC — Table Schema

> Source: `INSERTS/I_F.PP.PROGRAM.CHARACTERISTIC` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PGC.ProgramType` | `PpProgramCharacteristic_Programtype` | TField |  | Indicates the type of program. Possible values: Script Service Batch External |
| 2 | `PP.PGC.ComponentName` | `PpProgramCharacteristic_Componentname` | TField | Yes | Indicates the name of the file/program/batch/script etc. Validation Rules: Mandatory field. 32 alphanumeric characters. |
| 3 | `PP.PGC.ComponentService` | `PpProgramCharacteristic_Componentservice` | TField |  | Specifies the home path for execution of a component. Validation Rules: 32 alphanumeric characters. |
| 4 | `PP.PGC.RESERVED.5` | `PpProgramCharacteristic_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.PGC.RESERVED.4` | `PpProgramCharacteristic_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.PGC.RESERVED.3` | `PpProgramCharacteristic_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.PGC.RESERVED.2` | `PpProgramCharacteristic_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.PGC.RESERVED.1` | `PpProgramCharacteristic_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.PGC.LOCAL.REF` | `PpProgramCharacteristic_LocalRef` |  |  |  |
| 10 | `PP.PGC.OVERRIDE` | `PpProgramCharacteristic_Override` |  |  |  |
| 11 | `PP.PGC.RECORD.STATUS` | `PpProgramCharacteristic_RecordStatus` | String |  |  |
| 12 | `PP.PGC.CURR.NO` | `PpProgramCharacteristic_CurrNo` | String |  |  |
| 13 | `PP.PGC.INPUTTER` | `PpProgramCharacteristic_Inputter` |  |  |  |
| 14 | `PP.PGC.DATE.TIME` | `PpProgramCharacteristic_DateTime` |  |  |  |
| 15 | `PP.PGC.AUTHORISER` | `PpProgramCharacteristic_Authoriser` | String |  |  |
| 16 | `PP.PGC.CO.CODE` | `PpProgramCharacteristic_CoCode` | String |  |  |
| 17 | `PP.PGC.DEPT.CODE` | `PpProgramCharacteristic_DeptCode` | String |  |  |
| 18 | `PP.PGC.AUDITOR.CODE` | `PpProgramCharacteristic_AuditorCode` | String |  |  |
| 19 | `PP.PGC.AUDIT.DATE.TIME` | `PpProgramCharacteristic_AuditDateTime` | String |  |  |
