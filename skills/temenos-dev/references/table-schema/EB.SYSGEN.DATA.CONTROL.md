# EB.SYSGEN.DATA.CONTROL — Table Schema

> Source: `INSERTS/I_F.EB.SYSGEN.DATA.CONTROL` in `EB_InternalUtility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESDC.SELECT.CRIT` | `EbSysgenDataControl_SelectCrit` |  |  |  |
| 2 | `ESDC.PRODUCT.ID` | `EbSysgenDataControl_ProductId` | TField |  | This field indicates which product the target application is in. It is automatically updated by the system during input by referencing PGM.FILE. It is a NOINPUT field and users cannot alter it. Validation Rules: Alphanumeric characters of length 35 |
| 3 | `ESDC.RESERVED.10` | `EbSysgenDataControl_Reserved10` | TField |  |  |
| 4 | `ESDC.RESERVED.09` | `EbSysgenDataControl_Reserved09` | TField |  |  |
| 5 | `ESDC.RESERVED.08` | `EbSysgenDataControl_Reserved08` | TField |  |  |
| 6 | `ESDC.FIELD.NAME` | `EbSysgenDataControl_FieldName` |  |  |  |
| 7 | `ESDC.FIELD.POS` | `EbSysgenDataControl_FieldPos` |  |  |  |
| 8 | `ESDC.FIELD.TYPE` | `EbSysgenDataControl_FieldType` |  |  |  |
| 9 | `ESDC.CHNG.START.POS` | `EbSysgenDataControl_ChngStartPos` |  |  |  |
| 10 | `ESDC.CHNG.END.POS` | `EbSysgenDataControl_ChngEndPos` |  |  |  |
| 11 | `ESDC.CONV.FMT.RTN` | `EbSysgenDataControl_ConvFmtRtn` |  |  |  |
| 12 | `ESDC.RESERVED.07` | `EbSysgenDataControl_Reserved07` |  |  |  |
| 13 | `ESDC.RESERVED.06` | `EbSysgenDataControl_Reserved06` |  |  |  |
| 14 | `ESDC.RESERVED.05` | `EbSysgenDataControl_Reserved05` |  |  |  |
| 15 | `ESDC.RESERVED.04` | `EbSysgenDataControl_Reserved04` |  |  |  |
| 16 | `ESDC.SELECT.FROM` | `EbSysgenDataControl_SelectFrom` | TField | Yes | This field is intended for future use and is currently not used. All records are selected from $NAU regardless of the value of this field. Validation Rules: Option Field, allowed values: LIVE and $NAU. Mandatory field, defaulted to $NAU automatically. |
| 17 | `ESDC.WRITE.STATUS` | `EbSysgenDataControl_WriteStatus` | TField | Yes | This field is intended for future use and is currently not used. All records are written to the $NAU table without changing their status regardless of the value of this field. Validation Rules: Option Field, allowed values: IHLD, LIVE and INAU. Mandatory field, defaulted to INAU automatically. |
| 18 | `ESDC.AVBL.MARKER` | `EbSysgenDataControl_AvblMarker` | TField |  | Flag to indicate whether the record should be processed or not. If set to 'NO' the record will be skipped during SYSGEN processing. Validation Rules: Option Field, allowed values: blank or 'NO'. |
| 19 | `ESDC.RESERVED.03` | `EbSysgenDataControl_Reserved03` | TField |  |  |
| 20 | `ESDC.RESERVED.02` | `EbSysgenDataControl_Reserved02` | TField |  |  |
| 21 | `ESDC.RESERVED.01` | `EbSysgenDataControl_Reserved01` | TField |  |  |
| 22 | `ESDC.LOCAL.REF` | `EbSysgenDataControl_LocalRef` |  |  |  |
| 23 | `ESDC.OVERRIDE` | `EbSysgenDataControl_Override` |  |  |  |
| 24 | `ESDC.RECORD.STATUS` | `EbSysgenDataControl_RecordStatus` | String |  |  |
| 25 | `ESDC.CURR.NO` | `EbSysgenDataControl_CurrNo` | String |  |  |
| 26 | `ESDC.INPUTTER` | `EbSysgenDataControl_Inputter` |  |  |  |
| 27 | `ESDC.DATE.TIME` | `EbSysgenDataControl_DateTime` |  |  |  |
| 28 | `ESDC.AUTHORISER` | `EbSysgenDataControl_Authoriser` | String |  |  |
| 29 | `ESDC.CO.CODE` | `EbSysgenDataControl_CoCode` | String |  |  |
| 30 | `ESDC.DEPT.CODE` | `EbSysgenDataControl_DeptCode` | String |  |  |
| 31 | `ESDC.AUDITOR.CODE` | `EbSysgenDataControl_AuditorCode` | String |  |  |
| 32 | `ESDC.AUDIT.DATE.TIME` | `EbSysgenDataControl_AuditDateTime` | String |  |  |
