# CANNEX.TRAILER.ENTRY.TABLE — Table Schema

> Source: `INSERTS/I_F.CANNEX.TRAILER.ENTRY.TABLE` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.TRA.RECORD.TYPE` | `CannexTrailerEntryTable_RecordType` | TField |  | This field is used to define the Fixed value to indicate Batch Summary trailer record type. |
| 2 | `CANNEX.TRA.RECORD.COUNT` | `CannexTrailerEntryTable_RecordCount` | TField |  | Field is used to define the record count.The total number of records in this file including this record. |
| 3 | `CANNEX.TRA.APP.COUNT` | `CannexTrailerEntryTable_AppCount` | TField |  | This field is used to define the total number of order in the file. |
| 4 | `CANNEX.TRA.APP.TOTAL.AMT` | `CannexTrailerEntryTable_AppTotalAmt` | TField |  | This field is used to define the total dollar amount of all the orders in the file. |
| 5 | `CANNEX.TRA.RESERVED.1` | `CannexTrailerEntryTable_Reserved1` | TField |  |  |
| 6 | `CANNEX.TRA.RESERVED.2` | `CannexTrailerEntryTable_Reserved2` | TField |  |  |
| 7 | `CANNEX.TRA.RESERVED.3` | `CannexTrailerEntryTable_Reserved3` | TField |  |  |
| 8 | `CANNEX.TRA.RESERVED.4` | `CannexTrailerEntryTable_Reserved4` | TField |  |  |
| 9 | `CANNEX.TRA.RESERVED.5` | `CannexTrailerEntryTable_Reserved5` | TField |  |  |
| 10 | `CANNEX.TRA.RESERVED.6` | `CannexTrailerEntryTable_Reserved6` | TField |  |  |
| 11 | `CANNEX.TRA.RESERVED.7` | `CannexTrailerEntryTable_Reserved7` | TField |  |  |
| 12 | `CANNEX.TRA.RESERVED.8` | `CannexTrailerEntryTable_Reserved8` | TField |  |  |
| 13 | `CANNEX.TRA.RESERVED.9` | `CannexTrailerEntryTable_Reserved9` | TField |  |  |
| 14 | `CANNEX.TRA.RESERVED.10` | `CannexTrailerEntryTable_Reserved10` | TField |  |  |
| 15 | `CANNEX.TRA.LOCAL.REF` | `CannexTrailerEntryTable_LocalRef` |  |  |  |
| 16 | `CANNEX.TRA.OVERRIDE` | `CannexTrailerEntryTable_Override` |  |  |  |
| 17 | `CANNEX.TRA.RECORD.STATUS` | `CannexTrailerEntryTable_RecordStatus` | String |  |  |
| 18 | `CANNEX.TRA.CURR.NO` | `CannexTrailerEntryTable_CurrNo` | String |  |  |
| 19 | `CANNEX.TRA.INPUTTER` | `CannexTrailerEntryTable_Inputter` |  |  |  |
| 20 | `CANNEX.TRA.DATE.TIME` | `CannexTrailerEntryTable_DateTime` |  |  |  |
| 21 | `CANNEX.TRA.AUTHORISER` | `CannexTrailerEntryTable_Authoriser` | String |  |  |
| 22 | `CANNEX.TRA.CO.CODE` | `CannexTrailerEntryTable_CoCode` | String |  |  |
| 23 | `CANNEX.TRA.DEPT.CODE` | `CannexTrailerEntryTable_DeptCode` | String |  |  |
| 24 | `CANNEX.TRA.AUDITOR.CODE` | `CannexTrailerEntryTable_AuditorCode` | String |  |  |
| 25 | `CANNEX.TRA.AUDIT.DATE.TIME` | `CannexTrailerEntryTable_AuditDateTime` | String |  |  |
