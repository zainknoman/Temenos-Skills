# PP.IN.ENTRY.PARAM — Table Schema

> Source: `INSERTS/I_F.PP.IN.ENTRY.PARAM` in `PP_InwardFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPIEP.Description` | `PpInEntryParam_Description` | TField |  | Holds description of the mapping record |
| 2 | `PPIEP.FieldDelimiter` | `PpInEntryParam_Fielddelimiter` | TField |  | Holds the Field(FM) Delimiter in the Response received from the External System. |
| 3 | `PPIEP.VMDelimiter` | `PpInEntryParam_Vmdelimiter` | TField |  | Holds the Value(VM) Delimiter in the Response received from the External System. |
| 4 | `PPIEP.SMDelimiter` | `PpInEntryParam_Smdelimiter` | TField |  |  |
| 5 | `PPIEP.FieldName` | `PpInEntryParam_Fieldname` |  |  |  |
| 6 | `PPIEP.FieldPosition` | `PpInEntryParam_Fieldposition` |  |  |  |
| 7 | `PPIEP.FieldLength` | `PpInEntryParam_Fieldlength` |  |  |  |
| 8 | `PPIEP.ValRoutine` | `PpInEntryParam_Valroutine` |  |  |  |
| 9 | `PPIEP.Mandatory` | `PpInEntryParam_Mandatory` |  |  |  |
| 10 | `PPIEP.Constant` | `PpInEntryParam_Constant` |  |  |  |
| 11 | `PPIEP.LocalReference` | `PpInEntryParam_Localreference` |  |  |  |
| 12 | `PPIEP.RESERVED.8` | `PpInEntryParam_Reserved8` | TField |  |  |
| 13 | `PPIEP.RESERVED.7` | `PpInEntryParam_Reserved7` | TField |  |  |
| 14 | `PPIEP.RESERVED.6` | `PpInEntryParam_Reserved6` | TField |  |  |
| 15 | `PPIEP.RESERVED.5` | `PpInEntryParam_Reserved5` | TField |  |  |
| 16 | `PPIEP.RESERVED.4` | `PpInEntryParam_Reserved4` | TField |  |  |
| 17 | `PPIEP.RESERVED.3` | `PpInEntryParam_Reserved3` | TField |  |  |
| 18 | `PPIEP.RESERVED.2` | `PpInEntryParam_Reserved2` | TField |  |  |
| 19 | `PPIEP.RESERVED.1` | `PpInEntryParam_Reserved1` | TField |  |  |
| 20 | `PPIEP.OVERRIDE` | `PpInEntryParam_Override` |  |  |  |
| 21 | `PPIEP.RECORD.STATUS` | `PpInEntryParam_RecordStatus` | String |  |  |
| 22 | `PPIEP.CURR.NO` | `PpInEntryParam_CurrNo` | String |  |  |
| 23 | `PPIEP.INPUTTER` | `PpInEntryParam_Inputter` |  |  |  |
| 24 | `PPIEP.DATE.TIME` | `PpInEntryParam_DateTime` |  |  |  |
| 25 | `PPIEP.AUTHORISER` | `PpInEntryParam_Authoriser` | String |  |  |
| 26 | `PPIEP.CO.CODE` | `PpInEntryParam_CoCode` | String |  |  |
| 27 | `PPIEP.DEPT.CODE` | `PpInEntryParam_DeptCode` | String |  |  |
| 28 | `PPIEP.AUDITOR.CODE` | `PpInEntryParam_AuditorCode` | String |  |  |
| 29 | `PPIEP.AUDIT.DATE.TIME` | `PpInEntryParam_AuditDateTime` | String |  |  |
