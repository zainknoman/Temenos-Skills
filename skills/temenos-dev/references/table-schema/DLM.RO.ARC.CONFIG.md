# DLM.RO.ARC.CONFIG — Table Schema

> Source: `INSERTS/I_F.DLM.RO.ARC.CONFIG` in `DL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLM.ARC.RO.SCHEMA` | `DlmRoArcConfig_RoSchema` | TField |  | Schema name in which the Read only datas available Validation Rules: |
| 2 | `DLM.ARC.RO.TABLENAME` | `DlmRoArcConfig_RoTableName` | TField |  | Auto populated field which will have the database table name for the configured application Validation Rules: |
| 3 | `DLM.ARC.RETENTION.PERIOD` | `DlmRoArcConfig_RetentionPeriod` | TField |  | Mention How many month of data needs to be maintained in Read Only database in the format of nn where nn is a number of Months. Records older than the retention period will then be archived. If today's date is 13/06/95 and a retention period of 3 months is specified (3M), three months is calculated from the Today date. Therefore, any records from before 13/3/95 will be archived. Validation Rules: Upto 3 Numeric value |
| 4 | `DLM.ARC.ARCHIVE.ACTION` | `DlmRoArcConfig_ArchiveAction` | TField |  | Option field MOVE - Records will be moved to new file system DELETE - The condition matched records will be deleted from the table |
| 5 | `DLM.ARC.ARCHIVE.MODE` | `DlmRoArcConfig_ArchiveMode` | TField |  | Option field.Choose the mechanism used to move the datas from live system to Read only database TRICKLE FEED - No business validation is done during the data movement to Read only database so requires to do business validation before moving the data's to other file system which is not accessible. FULL - Business validation is done during the data movement from Live to read only database. So move the data's from Read only database to other file system without any validation |
| 6 | `DLM.ARC.RESERVED.9` | `DlmRoArcConfig_Reserved9` |  |  |  |
| 7 | `DLM.ARC.RESERVED.8` | `DlmRoArcConfig_Reserved8` |  |  |  |
| 8 | `DLM.ARC.RESERVED.7` | `DlmRoArcConfig_Reserved7` | TField |  |  |
| 9 | `DLM.ARC.RESERVED.6` | `DlmRoArcConfig_Reserved6` | TField |  |  |
| 10 | `DLM.ARC.RESERVED.5` | `DlmRoArcConfig_Reserved5` | TField |  |  |
| 11 | `DLM.ARC.RESERVED.4` | `DlmRoArcConfig_Reserved4` | TField |  |  |
| 12 | `DLM.ARC.RESERVED.3` | `DlmRoArcConfig_Reserved3` | TField |  |  |
| 14 | `DLM.ARC.RESERVED.1` | `DlmRoArcConfig_Reserved1` | TField |  |  |
