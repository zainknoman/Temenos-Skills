# EB.CONVERT.SCHEMA — Table Schema

> Source: `INSERTS/I_F.EB.CONVERT.SCHEMA` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CON.SC.DESCRIPTION` | `EbConvertSchema_Description` |  |  |  |
| 2 | `EB.CON.SC.RUN.STATUS` | `EbConvertSchema_RunStatus` | TField |  | This field is to store the current status of the migration record. Based on the RUN.STATUS, the service T24.CONVERT.SCHEMA will pick that particular record for processing. If RUN.STATUS is READY, service will pick it for processing. Validation Rules: System generated values are : 1. READY :- set when the record is authorised. T24.CONVERT.SCHEMA service picks the records having status as ready. 2. RUNNING :- set by the service, indicating that the record picked up for processing. 3. ERROR.IN.PROCESS :- set when there is any error while creating the migration list. 4. COMPLETED :- set when tables in the records are processed without errors and migration list is created. |
| 3 | `EB.CON.SC.SCHEMA.LIST.PATH` | `EbConvertSchema_SchemaListPath` | TField |  | Path where the T24.CONVERT.SCHEMA service writes the migration list as a .csv file. Validation Rules: Should be a valid path and should exist while creation of the record. |
| 4 | `EB.CON.SC.PRODUCT` | `EbConvertSchema_Product` |  |  |  |
| 5 | `EB.CON.SC.CRITERIA` | `EbConvertSchema_Criteria` |  |  |  |
| 6 | `EB.CON.SC.TABLE.NAME` | `EbConvertSchema_TableName` |  |  |  |
| 7 | `EB.CON.SC.SOURCE.SCHEMA` | `EbConvertSchema_SourceSchema` |  |  |  |
| 8 | `EB.CON.SC.TARGET.SCHEMA` | `EbConvertSchema_TargetSchema` |  |  |  |
| 9 | `EB.CON.SC.COMPANY.MNEMONIC` | `EbConvertSchema_CompanyMnemonic` |  |  |  |
| 10 | `EB.CON.SC.RESERVED.5` | `EbConvertSchema_Reserved5` | TField |  |  |
| 11 | `EB.CON.SC.RESERVED.4` | `EbConvertSchema_Reserved4` | TField |  |  |
| 12 | `EB.CON.SC.RESERVED.3` | `EbConvertSchema_Reserved3` | TField |  |  |
| 13 | `EB.CON.SC.RESERVED.2` | `EbConvertSchema_Reserved2` | TField |  |  |
| 14 | `EB.CON.SC.RESERVED.1` | `EbConvertSchema_Reserved1` | TField |  |  |
| 15 | `EB.CON.SC.OVERRIDE` | `EbConvertSchema_Override` |  |  |  |
| 16 | `EB.CON.SC.RECORD.STATUS` | `EbConvertSchema_RecordStatus` | String |  |  |
| 17 | `EB.CON.SC.CURR.NO` | `EbConvertSchema_CurrNo` | String |  |  |
| 18 | `EB.CON.SC.INPUTTER` | `EbConvertSchema_Inputter` |  |  |  |
| 19 | `EB.CON.SC.DATE.TIME` | `EbConvertSchema_DateTime` |  |  |  |
| 20 | `EB.CON.SC.AUTHORISER` | `EbConvertSchema_Authoriser` | String |  |  |
| 21 | `EB.CON.SC.CO.CODE` | `EbConvertSchema_CoCode` | String |  |  |
| 22 | `EB.CON.SC.DEPT.CODE` | `EbConvertSchema_DeptCode` | String |  |  |
| 23 | `EB.CON.SC.AUDITOR.CODE` | `EbConvertSchema_AuditorCode` | String |  |  |
| 24 | `EB.CON.SC.AUDIT.DATE.TIME` | `EbConvertSchema_AuditDateTime` | String |  |  |
