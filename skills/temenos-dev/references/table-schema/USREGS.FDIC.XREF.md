# USREGS.FDIC.XREF — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.XREF` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.XREF.DESCRIPTION` | `UsregsFdicXref_Description` |  |  |  |
| 2 | `FDIC.XREF.FIELD.DESCRIPTION` | `UsregsFdicXref_FieldDescription` |  |  |  |
| 3 | `FDIC.XREF.FDIC.VALUE` | `UsregsFdicXref_FdicValue` |  |  |  |
| 4 | `FDIC.XREF.T24.VALUE` | `UsregsFdicXref_T24Value` |  |  |  |
| 5 | `FDIC.XREF.RESERVED.15` | `UsregsFdicXref_Reserved15` |  |  |  |
| 6 | `FDIC.XREF.RESERVED.14` | `UsregsFdicXref_Reserved14` |  |  |  |
| 7 | `FDIC.XREF.RESERVED.13` | `UsregsFdicXref_Reserved13` |  |  |  |
| 8 | `FDIC.XREF.RESERVED.12` | `UsregsFdicXref_Reserved12` |  |  |  |
| 9 | `FDIC.XREF.RESERVED.11` | `UsregsFdicXref_Reserved11` |  |  |  |
| 10 | `FDIC.XREF.RESERVED.10` | `UsregsFdicXref_Reserved10` | TField |  |  |
| 11 | `FDIC.XREF.RESERVED.9` | `UsregsFdicXref_Reserved9` | TField |  |  |
| 12 | `FDIC.XREF.RESERVED.8` | `UsregsFdicXref_Reserved8` | TField |  |  |
| 13 | `FDIC.XREF.RESERVED.7` | `UsregsFdicXref_Reserved7` | TField |  |  |
| 14 | `FDIC.XREF.RESERVED.6` | `UsregsFdicXref_Reserved6` | TField |  |  |
| 15 | `FDIC.XREF.RESERVED.5` | `UsregsFdicXref_Reserved5` | TField |  |  |
| 16 | `FDIC.XREF.RESERVED.4` | `UsregsFdicXref_Reserved4` | TField |  |  |
| 17 | `FDIC.XREF.RESERVED.3` | `UsregsFdicXref_Reserved3` | TField |  |  |
| 18 | `FDIC.XREF.RESERVED.2` | `UsregsFdicXref_Reserved2` | TField |  |  |
| 19 | `FDIC.XREF.RESERVED.1` | `UsregsFdicXref_Reserved1` | TField |  |  |
| 20 | `FDIC.XREF.LOCAL.REF` | `UsregsFdicXref_LocalRef` |  |  |  |
| 21 | `FDIC.XREF.OVERRIDE` | `UsregsFdicXref_Override` |  |  |  |
| 22 | `FDIC.XREF.RECORD.STATUS` | `UsregsFdicXref_RecordStatus` | String |  |  |
| 23 | `FDIC.XREF.CURR.NO` | `UsregsFdicXref_CurrNo` | String |  |  |
| 24 | `FDIC.XREF.INPUTTER` | `UsregsFdicXref_Inputter` |  |  |  |
| 25 | `FDIC.XREF.DATE.TIME` | `UsregsFdicXref_DateTime` |  |  |  |
| 26 | `FDIC.XREF.AUTHORISER` | `UsregsFdicXref_Authoriser` | String |  |  |
| 27 | `FDIC.XREF.CO.CODE` | `UsregsFdicXref_CoCode` | String |  |  |
| 28 | `FDIC.XREF.DEPT.CODE` | `UsregsFdicXref_DeptCode` | String |  |  |
| 29 | `FDIC.XREF.AUDITOR.CODE` | `UsregsFdicXref_AuditorCode` | String |  |  |
| 30 | `FDIC.XREF.AUDIT.DATE.TIME` | `UsregsFdicXref_AuditDateTime` | String |  |  |
