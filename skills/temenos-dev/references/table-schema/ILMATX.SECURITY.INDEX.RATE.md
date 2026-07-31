# ILMATX.SECURITY.INDEX.RATE — Table Schema

> Source: `INSERTS/I_F.ILMATX.SECURITY.INDEX.RATE` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.SECURITY.INDEX.CODE` | `IlmatxSecurityIndexRate_IndexCode` | TField |  | This field indicates the Index code of the Index. |
| 2 | `ILMATX.SECURITY.INDEX.DATE` | `IlmatxSecurityIndexRate_IndexDate` | TField |  | This field indicates the date for which the index value is specified. |
| 3 | `ILMATX.SECURITY.INDEX.VALUE` | `IlmatxSecurityIndexRate_IndexValue` | TField |  | This field indicates the value of the Index as on the Index Date. |
| 4 | `ILMATX.SECURITY.RESERVED.5` | `IlmatxSecurityIndexRate_Reserved5` | TField |  | Reserved for future use. |
| 5 | `ILMATX.SECURITY.RESERVED.4` | `IlmatxSecurityIndexRate_Reserved4` | TField |  | Reserved for future use. |
| 6 | `ILMATX.SECURITY.RESERVED.3` | `IlmatxSecurityIndexRate_Reserved3` | TField |  | Reserved for future use. |
| 7 | `ILMATX.SECURITY.RESERVED.2` | `IlmatxSecurityIndexRate_Reserved2` | TField |  | Reserved for future use. |
| 8 | `ILMATX.SECURITY.RESERVED.1` | `IlmatxSecurityIndexRate_Reserved1` | TField |  | Reserved for future use. |
| 9 | `ILMATX.SECURITY.LOCAL.REF` | `IlmatxSecurityIndexRate_LocalRef` |  |  |  |
| 10 | `ILMATX.SECURITY.OVERRIDE` | `IlmatxSecurityIndexRate_Override` |  |  |  |
| 11 | `ILMATX.SECURITY.RECORD.STATUS` | `IlmatxSecurityIndexRate_RecordStatus` | String |  |  |
| 12 | `ILMATX.SECURITY.CURR.NO` | `IlmatxSecurityIndexRate_CurrNo` | String |  |  |
| 13 | `ILMATX.SECURITY.INPUTTER` | `IlmatxSecurityIndexRate_Inputter` |  |  |  |
| 14 | `ILMATX.SECURITY.DATE.TIME` | `IlmatxSecurityIndexRate_DateTime` |  |  |  |
| 15 | `ILMATX.SECURITY.AUTHORISER` | `IlmatxSecurityIndexRate_Authoriser` | String |  |  |
| 16 | `ILMATX.SECURITY.CO.CODE` | `IlmatxSecurityIndexRate_CoCode` | String |  |  |
| 17 | `ILMATX.SECURITY.DEPT.CODE` | `IlmatxSecurityIndexRate_DeptCode` | String |  |  |
| 18 | `ILMATX.SECURITY.AUDITOR.CODE` | `IlmatxSecurityIndexRate_AuditorCode` | String |  |  |
| 19 | `ILMATX.SECURITY.AUDIT.DATE.TIME` | `IlmatxSecurityIndexRate_AuditDateTime` | String |  |  |
