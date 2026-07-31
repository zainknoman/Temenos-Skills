# EB.TABLE.DATA.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.TABLE.DATA.TYPE` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TBL.TYP.DESCRIPTION` | `EbTableDataType_Description` |  |  |  |
| 2 | `EB.TBL.TYP.VAL.PROG` | `EbTableDataType_ValProg` |  |  |  |
| 3 | `EB.TBL.TYP.MAX.CHAR` | `EbTableDataType_MaxChar` | TField | Yes | To define the maximum size of the field created for EB.TABLE.DEFINITION. if MAX.CHAR filed in EB.TABLE.DEFINITION is not present and DATA.TYPE of the record is a EB.TABLE.DATA.TYPE record then this MAX.CHAR will applied to the corresponding ETD. Validation Rules: 1.Mandatory field 2.should allow only Numeric characters |
| 4 | `EB.TBL.TYP.RESERVED.1` | `EbTableDataType_Reserved1` | TField |  |  |
| 5 | `EB.TBL.TYP.RESERVED.2` | `EbTableDataType_Reserved2` | TField |  |  |
| 6 | `EB.TBL.TYP.RESERVED.3` | `EbTableDataType_Reserved3` | TField |  |  |
| 7 | `EB.TBL.TYP.RESERVED.4` | `EbTableDataType_Reserved4` | TField |  |  |
| 8 | `EB.TBL.TYP.RESERVED.5` | `EbTableDataType_Reserved5` | TField |  |  |
| 9 | `EB.TBL.TYP.RESERVED.6` | `EbTableDataType_Reserved6` | TField |  |  |
| 10 | `EB.TBL.TYP.RESERVED.7` | `EbTableDataType_Reserved7` | TField |  |  |
| 11 | `EB.TBL.TYP.RESERVED.8` | `EbTableDataType_Reserved8` | TField |  |  |
| 12 | `EB.TBL.TYP.RESERVED.9` | `EbTableDataType_Reserved9` | TField |  |  |
| 13 | `EB.TBL.TYP.RESERVED.10` | `EbTableDataType_Reserved10` | TField |  |  |
| 14 | `EB.TBL.TYP.LOCAL.REF` | `EbTableDataType_LocalRef` |  |  |  |
| 15 | `EB.TBL.TYP.OVERRIDE` | `EbTableDataType_Override` |  |  |  |
| 16 | `EB.TBL.TYP.RECORD.STATUS` | `EbTableDataType_RecordStatus` | String |  |  |
| 17 | `EB.TBL.TYP.CURR.NO` | `EbTableDataType_CurrNo` | String |  |  |
| 18 | `EB.TBL.TYP.INPUTTER` | `EbTableDataType_Inputter` |  |  |  |
| 19 | `EB.TBL.TYP.DATE.TIME` | `EbTableDataType_DateTime` |  |  |  |
| 20 | `EB.TBL.TYP.AUTHORISER` | `EbTableDataType_Authoriser` | String |  |  |
| 21 | `EB.TBL.TYP.CO.CODE` | `EbTableDataType_CoCode` | String |  |  |
| 22 | `EB.TBL.TYP.DEPT.CODE` | `EbTableDataType_DeptCode` | String |  |  |
| 23 | `EB.TBL.TYP.AUDITOR.CODE` | `EbTableDataType_AuditorCode` | String |  |  |
| 24 | `EB.TBL.TYP.AUDIT.DATE.TIME` | `EbTableDataType_AuditDateTime` | String |  |  |
