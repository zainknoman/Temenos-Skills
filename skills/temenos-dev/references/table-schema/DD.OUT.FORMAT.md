# DD.OUT.FORMAT — Table Schema

> Source: `INSERTS/I_F.DD.OUT.FORMAT` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.OF.DESCRIPTION` | `DdOutFormat_Description` |  |  |  |
| 2 | `DD.OF.HDR.FIELD.NAME` | `DdOutFormat_HdrFieldName` |  |  |  |
| 3 | `DD.OF.HDR.FIELD.LINK` | `DdOutFormat_HdrFieldLink` |  |  |  |
| 4 | `DD.OF.HDR.SPL.TEXT` | `DdOutFormat_HdrSplText` |  |  |  |
| 5 | `DD.OF.HDR.LEN.MASK` | `DdOutFormat_HdrLenMask` |  |  |  |
| 6 | `DD.OF.HDR.FIELD.RTN` | `DdOutFormat_HdrFieldRtn` |  |  |  |
| 7 | `DD.OF.HDR.INCL.FIELD` | `DdOutFormat_HdrInclField` |  |  |  |
| 8 | `DD.OF.HDR.RESERVED` | `DdOutFormat_HdrReserved` |  |  |  |
| 9 | `DD.OF.DATA.FIELD.NAME` | `DdOutFormat_DataFieldName` |  |  |  |
| 10 | `DD.OF.DATA.FIELD.LINK` | `DdOutFormat_DataFieldLink` |  |  |  |
| 11 | `DD.OF.DATA.SPL.TEXT` | `DdOutFormat_DataSplText` |  |  |  |
| 12 | `DD.OF.DATA.LEN.MASK` | `DdOutFormat_DataLenMask` |  |  |  |
| 13 | `DD.OF.DATA.FIELD.RTN` | `DdOutFormat_DataFieldRtn` |  |  |  |
| 14 | `DD.OF.DATA.INCL.FIELD` | `DdOutFormat_DataInclField` |  |  |  |
| 15 | `DD.OF.FTR.FIELD.NAME` | `DdOutFormat_FtrFieldName` |  |  |  |
| 16 | `DD.OF.FTR.FIELD.LINK` | `DdOutFormat_FtrFieldLink` |  |  |  |
| 17 | `DD.OF.FTR.SPL.TEXT` | `DdOutFormat_FtrSplText` |  |  |  |
| 18 | `DD.OF.FTR.LEN.MASK` | `DdOutFormat_FtrLenMask` |  |  |  |
| 19 | `DD.OF.FTR.FIELD.RTN` | `DdOutFormat_FtrFieldRtn` |  |  |  |
| 20 | `DD.OF.FTR.INCL.FIELD` | `DdOutFormat_FtrInclField` |  |  |  |
| 21 | `DD.OF.FTR.RESERVED` | `DdOutFormat_FtrReserved` |  |  |  |
| 22 | `DD.OF.RAISE.DELIVERY.MSG` | `DdOutFormat_RaiseDeliveryMsg` | TField |  | This field is used to identify whether to map the DD collection details into pain.008 format. Validation Details Allowed values : Y or Null. |
| 23 | `DD.OF.LCL.MAP.RTN` | `DdOutFormat_LocalMappingRtn` |  |  |  |
| 24 | `DD.OF.RESERVED08` | `DdOutFormat_Reserved08` |  |  |  |
| 25 | `DD.OF.RESERVED07` | `DdOutFormat_Reserved07` | TField |  |  |
| 26 | `DD.OF.RESERVED06` | `DdOutFormat_Reserved06` | TField |  |  |
| 27 | `DD.OF.RESERVED05` | `DdOutFormat_Reserved05` | TField |  |  |
| 28 | `DD.OF.RESERVED04` | `DdOutFormat_Reserved04` | TField |  |  |
| 29 | `DD.OF.RESERVED03` | `DdOutFormat_Reserved03` | TField |  |  |
| 30 | `DD.OF.RESERVED02` | `DdOutFormat_Reserved02` | TField |  |  |
| 31 | `DD.OF.RESERVED01` | `DdOutFormat_Reserved01` | TField |  |  |
| 32 | `DD.OF.LOCAL.REF` | `DdOutFormat_LocalRef` |  |  |  |
| 33 | `DD.OF.OVERRIDE` | `DdOutFormat_Override` |  |  |  |
| 34 | `DD.OF.RECORD.STATUS` | `DdOutFormat_RecordStatus` | String |  |  |
| 35 | `DD.OF.CURR.NO` | `DdOutFormat_CurrNo` | String |  |  |
| 36 | `DD.OF.INPUTTER` | `DdOutFormat_Inputter` |  |  |  |
| 37 | `DD.OF.DATE.TIME` | `DdOutFormat_DateTime` |  |  |  |
| 38 | `DD.OF.AUTHORISER` | `DdOutFormat_Authoriser` | String |  |  |
| 39 | `DD.OF.CO.CODE` | `DdOutFormat_CoCode` | String |  |  |
| 40 | `DD.OF.DEPT.CODE` | `DdOutFormat_DeptCode` | String |  |  |
| 41 | `DD.OF.AUDITOR.CODE` | `DdOutFormat_AuditorCode` | String |  |  |
| 42 | `DD.OF.AUDIT.DATE.TIME` | `DdOutFormat_AuditDateTime` | String |  |  |
