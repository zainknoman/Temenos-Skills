# EB.DATA.QUALITY.CHECK — Table Schema

> Source: `INSERTS/I_F.EB.DATA.QUALITY.CHECK` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DATA.QTY.TENANT.ID` | `EbDataQualityCheck_TenantId` | TField |  |  |
| 2 | `DATA.QTY.EVENT.TYPE` | `EbDataQualityCheck_EventType` | TField |  |  |
| 3 | `DATA.QTY.OBJECT.ID` | `EbDataQualityCheck_ObjectId` | TField |  |  |
| 4 | `DATA.QTY.OBJECT.REFERENCE` | `EbDataQualityCheck_ObjectReference` | TField |  |  |
| 5 | `DATA.QTY.SEVERITY` | `EbDataQualityCheck_Severity` | TField |  |  |
| 6 | `DATA.QTY.ERROR.CODE` | `EbDataQualityCheck_ErrorCode` |  |  |  |
| 7 | `DATA.QTY.COLUMN.NAME` | `EbDataQualityCheck_ColumnName` |  |  |  |
| 8 | `DATA.QTY.CUSTOM.ERROR.MESSAGE` | `EbDataQualityCheck_CustomErrorMessage` |  |  |  |
| 9 | `DATA.QTY.ACTUAL.CAUSE` | `EbDataQualityCheck_ActualCause` |  |  |  |
| 10 | `DATA.QTY.ADDITIONAL.DETAILS` | `EbDataQualityCheck_AdditionalDetails` |  |  |  |
| 11 | `DATA.QTY.SCRIPTS` | `EbDataQualityCheck_Scripts` |  |  |  |
| 12 | `DATA.QTY.BUSINESS.DATE` | `EbDataQualityCheck_BusinessDate` | TField |  |  |
| 13 | `DATA.QTY.COMPANY.CODE` | `EbDataQualityCheck_CompanyCode` | TField |  |  |
| 14 | `DATA.QTY.ORIGIN.OF.TRANSACTION` | `EbDataQualityCheck_OriginOfTransaction` | TField |  |  |
| 15 | `DATA.QTY.STATUS` | `EbDataQualityCheck_Status` | TField |  |  |
| 16 | `DATA.QTY.RESERVED10` | `EbDataQualityCheck_Reserved10` | TField |  |  |
| 17 | `DATA.QTY.RESERVED9` | `EbDataQualityCheck_Reserved9` | TField |  |  |
| 18 | `DATA.QTY.RESERVED8` | `EbDataQualityCheck_Reserved8` | TField |  |  |
| 19 | `DATA.QTY.RESERVED7` | `EbDataQualityCheck_Reserved7` | TField |  |  |
| 20 | `DATA.QTY.RESERVED6` | `EbDataQualityCheck_Reserved6` | TField |  |  |
| 21 | `DATA.QTY.RESERVED5` | `EbDataQualityCheck_Reserved5` | TField |  |  |
| 22 | `DATA.QTY.RESERVED4` | `EbDataQualityCheck_Reserved4` | TField |  |  |
| 23 | `DATA.QTY.RESERVED3` | `EbDataQualityCheck_Reserved3` | TField |  |  |
| 24 | `DATA.QTY.RESERVED2` | `EbDataQualityCheck_Reserved2` | TField |  |  |
| 25 | `DATA.QTY.RESERVED1` | `EbDataQualityCheck_Reserved1` | TField |  |  |
| 26 | `DATA.QTY.OVERRIDE` | `EbDataQualityCheck_Override` |  |  |  |
| 27 | `DATA.QTY.RECORD.STATUS` | `EbDataQualityCheck_RecordStatus` | String |  |  |
| 28 | `DATA.QTY.CURR.NO` | `EbDataQualityCheck_CurrNo` | String |  |  |
| 29 | `DATA.QTY.INPUTTER` | `EbDataQualityCheck_Inputter` |  |  |  |
| 30 | `DATA.QTY.DATE.TIME` | `EbDataQualityCheck_DateTime` |  |  |  |
| 31 | `DATA.QTY.AUTHORISER` | `EbDataQualityCheck_Authoriser` | String |  |  |
| 32 | `DATA.QTY.CO.CODE` | `EbDataQualityCheck_CoCode` | String |  |  |
| 33 | `DATA.QTY.DEPT.CODE` | `EbDataQualityCheck_DeptCode` | String |  |  |
| 34 | `DATA.QTY.AUDITOR.CODE` | `EbDataQualityCheck_AuditorCode` | String |  |  |
| 35 | `DATA.QTY.AUDIT.DATE.TIME` | `EbDataQualityCheck_AuditDateTime` | String |  |  |
