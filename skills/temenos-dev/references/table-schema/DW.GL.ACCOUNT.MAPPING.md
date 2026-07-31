# DW.GL.ACCOUNT.MAPPING — Table Schema

> Source: `INSERTS/I_F.DW.GL.ACCOUNT.MAPPING` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.GL.ACCOUNT.CODE` | `DwGlAccountMapping_AccountCode` | TField |  | This field is used to mention the name for extraction. Example: If you extract the CASH accounts from the Account application, then specify the value as CASH ACCOUNT. |
| 2 | `DW.GL.EXTRACT.FROM.FILE` | `DwGlAccountMapping_ExtractFromFile` | TField |  | This field specifies from which application that is to be extracted (E.g.: ACCOUNT). |
| 3 | `DW.GL.EXTRACT.FROM.RECID` | `DwGlAccountMapping_ExtractFromRecid` | TField | No | This field specifies from which record to extract. If you need to extract any particular record then specify that id. (It is optional). |
| 4 | `DW.GL.MULTIVAL.MARKUPFLD` | `DwGlAccountMapping_MultivalMarkupfld` | TField |  | This field use to store the markup filed name. |
| 5 | `DW.GL.MULTIVAL.FLD.VAL` | `DwGlAccountMapping_MultivalFldVal` | TField |  | This field is used to store the markup filed value. |
| 6 | `DW.GL.MAP.FIELD` | `DwGlAccountMapping_MapField` |  |  |  |
| 7 | `DW.GL.MAP.VALUE` | `DwGlAccountMapping_MapValue` |  |  |  |
| 8 | `DW.GL.EXTRACT.SELECTION` | `DwGlAccountMapping_ExtractSelection` | TField |  | This field is used to mention the selection criteria for the selection record on the table. |
| 9 | `DW.GL.RESERVED.10` | `DwGlAccountMapping_Reserved10` | TField |  |  |
| 10 | `DW.GL.RESERVED.9` | `DwGlAccountMapping_Reserved9` | TField |  |  |
| 11 | `DW.GL.RESERVED.8` | `DwGlAccountMapping_Reserved8` | TField |  |  |
| 12 | `DW.GL.RESERVED.7` | `DwGlAccountMapping_Reserved7` | TField |  |  |
| 13 | `DW.GL.RESERVED.6` | `DwGlAccountMapping_Reserved6` | TField |  |  |
| 14 | `DW.GL.RESERVED.5` | `DwGlAccountMapping_Reserved5` | TField |  |  |
| 15 | `DW.GL.RESERVED.4` | `DwGlAccountMapping_Reserved4` | TField |  |  |
| 16 | `DW.GL.RESERVED.3` | `DwGlAccountMapping_Reserved3` | TField |  |  |
| 17 | `DW.GL.RESERVED.2` | `DwGlAccountMapping_Reserved2` | TField |  |  |
| 18 | `DW.GL.RESERVED.1` | `DwGlAccountMapping_Reserved1` | TField |  |  |
| 19 | `DW.GL.RECORD.STATUS` | `DwGlAccountMapping_RecordStatus` | String |  |  |
| 20 | `DW.GL.CURR.NO` | `DwGlAccountMapping_CurrNo` | String |  |  |
| 21 | `DW.GL.INPUTTER` | `DwGlAccountMapping_Inputter` |  |  |  |
| 22 | `DW.GL.DATE.TIME` | `DwGlAccountMapping_DateTime` |  |  |  |
| 23 | `DW.GL.AUTHORISER` | `DwGlAccountMapping_Authoriser` | String |  |  |
| 24 | `DW.GL.CO.CODE` | `DwGlAccountMapping_CoCode` | String |  |  |
| 25 | `DW.GL.DEPT.CODE` | `DwGlAccountMapping_DeptCode` | String |  |  |
| 26 | `DW.GL.AUDITOR.CODE` | `DwGlAccountMapping_AuditorCode` | String |  |  |
| 27 | `DW.GL.AUDIT.DATE.TIME` | `DwGlAccountMapping_AuditDateTime` | String |  |  |
