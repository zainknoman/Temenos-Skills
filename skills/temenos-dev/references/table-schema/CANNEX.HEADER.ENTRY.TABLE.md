# CANNEX.HEADER.ENTRY.TABLE — Table Schema

> Source: `INSERTS/I_F.CANNEX.HEADER.ENTRY.TABLE` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.HDR.RECORD.TYPE` | `CannexHeaderEntryTable_RecordType` | TField |  | This field is used to defient the Fixed value to indicate the header record type. |
| 2 | `CANNEX.HDR.FILE.TYPE` | `CannexHeaderEntryTable_FileType` | TField |  | This field is to define the Term Deposit/GIC Product Order eventfile.E.g. TERMO |
| 3 | `CANNEX.HDR.DATE.CREATED` | `CannexHeaderEntryTable_DateCreated` | TField |  | This field indicates the date on which file created. |
| 4 | `CANNEX.HDR.TIME.CREATED` | `CannexHeaderEntryTable_TimeCreated` | TField |  | This field indicates the time on which file created. |
| 5 | `CANNEX.HDR.VERSION.NO` | `CannexHeaderEntryTable_VersionNo` | TField |  | This field will hold the current file specification version. |
| 6 | `CANNEX.HDR.RESERVED.2` | `CannexHeaderEntryTable_Reserved2` | TField |  |  |
| 7 | `CANNEX.HDR.RESERVED.3` | `CannexHeaderEntryTable_Reserved3` | TField |  |  |
| 8 | `CANNEX.HDR.RESERVED.4` | `CannexHeaderEntryTable_Reserved4` | TField |  |  |
| 9 | `CANNEX.HDR.RESERVED.5` | `CannexHeaderEntryTable_Reserved5` | TField |  |  |
| 10 | `CANNEX.HDR.RESERVED.6` | `CannexHeaderEntryTable_Reserved6` | TField |  |  |
| 11 | `CANNEX.HDR.RESERVED.7` | `CannexHeaderEntryTable_Reserved7` | TField |  |  |
| 12 | `CANNEX.HDR.RESERVED.8` | `CannexHeaderEntryTable_Reserved8` | TField |  |  |
| 13 | `CANNEX.HDR.RESERVED.9` | `CannexHeaderEntryTable_Reserved9` | TField |  |  |
| 14 | `CANNEX.HDR.RESERVED.10` | `CannexHeaderEntryTable_Reserved10` | TField |  |  |
| 15 | `CANNEX.HDR.LOCAL.REF` | `CannexHeaderEntryTable_LocalRef` |  |  |  |
| 16 | `CANNEX.HDR.OVERRIDE` | `CannexHeaderEntryTable_Override` |  |  |  |
| 17 | `CANNEX.HDR.RECORD.STATUS` | `CannexHeaderEntryTable_RecordStatus` | String |  |  |
| 18 | `CANNEX.HDR.CURR.NO` | `CannexHeaderEntryTable_CurrNo` | String |  |  |
| 19 | `CANNEX.HDR.INPUTTER` | `CannexHeaderEntryTable_Inputter` |  |  |  |
| 20 | `CANNEX.HDR.DATE.TIME` | `CannexHeaderEntryTable_DateTime` |  |  |  |
| 21 | `CANNEX.HDR.AUTHORISER` | `CannexHeaderEntryTable_Authoriser` | String |  |  |
| 22 | `CANNEX.HDR.CO.CODE` | `CannexHeaderEntryTable_CoCode` | String |  |  |
| 23 | `CANNEX.HDR.DEPT.CODE` | `CannexHeaderEntryTable_DeptCode` | String |  |  |
| 24 | `CANNEX.HDR.AUDITOR.CODE` | `CannexHeaderEntryTable_AuditorCode` | String |  |  |
| 25 | `CANNEX.HDR.AUDIT.DATE.TIME` | `CannexHeaderEntryTable_AuditDateTime` | String |  |  |
