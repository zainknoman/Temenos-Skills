# DW.BULK.EXTRACT — Table Schema

> Source: `INSERTS/I_F.DW.BULK.EXTRACT` in `DW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.BX.DESCRIPTION` | `DwBulkExtract_Description` |  |  |  |
| 2 | `DW.BX.T24.TABLE` | `DwBulkExtract_T24Table` |  |  |  |
| 3 | `DW.BX.FLD.SELECTION` | `DwBulkExtract_FldSelection` |  |  |  |
| 4 | `DW.BX.SELECTION.OPER` | `DwBulkExtract_SelectionOper` |  |  |  |
| 5 | `DW.BX.SELECTION.CRIT` | `DwBulkExtract_SelectionCrit` |  |  |  |
| 6 | `DW.BX.RULES.ROUTINE` | `DwBulkExtract_RulesRoutine` |  |  |  |
| 7 | `DW.BX.EXTRACT.REG` | `DwBulkExtract_ExtractReg` |  |  |  |
| 8 | `DW.BX.COMPANY.CODE` | `DwBulkExtract_CompanyCode` |  |  |  |
| 9 | `DW.BX.STATUS` | `DwBulkExtract_Status` | TField |  | Defines the status of DW.BULK.EXTRACT record. Validation Rules :1) Can be PENDING,RUNNING and MIGRATED.2) Record can't be edited when it is in RUNNING status.3) Record in PENDING and MIGRATED status can be edited and re-used |
| 10 | `DW.BX.RESERVED.10` | `DwBulkExtract_Reserved10` | TField |  |  |
| 11 | `DW.BX.RESERVED.9` | `DwBulkExtract_Reserved9` | TField |  |  |
| 12 | `DW.BX.RESERVED.8` | `DwBulkExtract_Reserved8` | TField |  |  |
| 13 | `DW.BX.RESERVED.7` | `DwBulkExtract_Reserved7` | TField |  |  |
| 14 | `DW.BX.RESERVED.6` | `DwBulkExtract_Reserved6` | TField |  |  |
| 15 | `DW.BX.RESERVED.5` | `DwBulkExtract_Reserved5` | TField |  |  |
| 16 | `DW.BX.RESERVED.4` | `DwBulkExtract_Reserved4` | TField |  |  |
| 17 | `DW.BX.RESERVED.3` | `DwBulkExtract_Reserved3` | TField |  |  |
| 18 | `DW.BX.RESERVED.2` | `DwBulkExtract_Reserved2` | TField |  |  |
| 19 | `DW.BX.RESERVED.1` | `DwBulkExtract_Reserved1` | TField |  |  |
| 20 | `DW.BX.RECORD.STATUS` | `DwBulkExtract_RecordStatus` | String |  |  |
| 21 | `DW.BX.CURR.NO` | `DwBulkExtract_CurrNo` | String |  |  |
| 22 | `DW.BX.INPUTTER` | `DwBulkExtract_Inputter` |  |  |  |
| 23 | `DW.BX.DATE.TIME` | `DwBulkExtract_DateTime` |  |  |  |
| 24 | `DW.BX.AUTHORISER` | `DwBulkExtract_Authoriser` | String |  |  |
| 25 | `DW.BX.CO.CODE` | `DwBulkExtract_CoCode` | String |  |  |
| 26 | `DW.BX.DEPT.CODE` | `DwBulkExtract_DeptCode` | String |  |  |
| 27 | `DW.BX.AUDITOR.CODE` | `DwBulkExtract_AuditorCode` | String |  |  |
| 28 | `DW.BX.AUDIT.DATE.TIME` | `DwBulkExtract_AuditDateTime` | String |  |  |
