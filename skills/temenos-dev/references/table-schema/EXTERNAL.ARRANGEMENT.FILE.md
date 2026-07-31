# EXTERNAL.ARRANGEMENT.FILE — Table Schema

> Source: `INSERTS/I_F.EXTERNAL.ARRANGEMENT.FILE` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EX.ARR.CUS.POS.FIELD.NAME` | `ExternalArrangementFile_CusPosFieldName` |  |  |  |
| 2 | `EX.ARR.CUS.POS.FIELD.VAL` | `ExternalArrangementFile_CusPosFieldVal` |  |  |  |
| 3 | `EX.ARR.UPLOAD.DATE` | `ExternalArrangementFile_UploadDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `EX.ARR.EXPIRY.DATE` | `ExternalArrangementFile_ExpiryDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `EX.ARR.RESERVED.1` | `ExternalArrangementFile_Reserved1` | TField |  |  |
| 6 | `EX.ARR.RESERVED.2` | `ExternalArrangementFile_Reserved2` | TField |  |  |
| 7 | `EX.ARR.RESERVED.3` | `ExternalArrangementFile_Reserved3` | TField |  |  |
| 8 | `EX.ARR.RECORD.STATUS` | `ExternalArrangementFile_RecordStatus` | String |  |  |
| 9 | `EX.ARR.CURR.NO` | `ExternalArrangementFile_CurrNo` | String |  |  |
| 10 | `EX.ARR.INPUTTER` | `ExternalArrangementFile_Inputter` |  |  |  |
| 11 | `EX.ARR.DATE.TIME` | `ExternalArrangementFile_DateTime` |  |  |  |
| 12 | `EX.ARR.AUTHORISER` | `ExternalArrangementFile_Authoriser` | String |  |  |
| 13 | `EX.ARR.CO.CODE` | `ExternalArrangementFile_CoCode` | String |  |  |
| 14 | `EX.ARR.DEPT.CODE` | `ExternalArrangementFile_DeptCode` | String |  |  |
| 15 | `EX.ARR.AUDITOR.CODE` | `ExternalArrangementFile_AuditorCode` | String |  |  |
| 16 | `EX.ARR.AUDIT.DATE.TIME` | `ExternalArrangementFile_AuditDateTime` | String |  |  |
