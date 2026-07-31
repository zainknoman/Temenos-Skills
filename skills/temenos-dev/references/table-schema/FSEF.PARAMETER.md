# FSEF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FSEF.PARAMETER` in `CAATMD_DCPInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSEF.CARD.STATUS` | `FsefParameter_CardStatus` |  |  |  |
| 2 | `FSEF.FILE.SEQUENCE` | `FsefParameter_FileSequence` | TField |  |  |
| 3 | `FSEF.FIN.INST.ID` | `FsefParameter_FinInstId` | TField |  |  |
| 4 | `FSEF.RESERVED.10` | `FsefParameter_Reserved10` | TField |  |  |
| 5 | `FSEF.RESERVED.9` | `FsefParameter_Reserved9` | TField |  |  |
| 6 | `FSEF.RESERVED.8` | `FsefParameter_Reserved8` | TField |  |  |
| 7 | `FSEF.RESERVED.7` | `FsefParameter_Reserved7` | TField |  |  |
| 8 | `FSEF.RESERVED.6` | `FsefParameter_Reserved6` | TField |  |  |
| 9 | `FSEF.RESERVED.5` | `FsefParameter_Reserved5` | TField |  |  |
| 10 | `FSEF.RESERVED.4` | `FsefParameter_Reserved4` | TField |  |  |
| 11 | `FSEF.RESERVED.3` | `FsefParameter_Reserved3` | TField |  |  |
| 12 | `FSEF.RESERVED.2` | `FsefParameter_Reserved2` | TField |  |  |
| 13 | `FSEF.RESERVED.1` | `FsefParameter_Reserved1` | TField |  |  |
| 14 | `FSEF.RECORD.STATUS` | `FsefParameter_RecordStatus` | String |  |  |
| 15 | `FSEF.CURR.NO` | `FsefParameter_CurrNo` | String |  |  |
| 16 | `FSEF.INPUTTER` | `FsefParameter_Inputter` |  |  |  |
| 17 | `FSEF.DATE.TIME` | `FsefParameter_DateTime` |  |  |  |
| 18 | `FSEF.AUTHORISER` | `FsefParameter_Authoriser` | String |  |  |
| 19 | `FSEF.CO.CODE` | `FsefParameter_CoCode` | String |  |  |
| 20 | `FSEF.DEPT.CODE` | `FsefParameter_DeptCode` | String |  |  |
| 21 | `FSEF.AUDITOR.CODE` | `FsefParameter_AuditorCode` | String |  |  |
| 22 | `FSEF.AUDIT.DATE.TIME` | `FsefParameter_AuditDateTime` | String |  |  |
