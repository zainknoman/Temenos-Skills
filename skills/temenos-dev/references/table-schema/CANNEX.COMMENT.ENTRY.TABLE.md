# CANNEX.COMMENT.ENTRY.TABLE — Table Schema

> Source: `INSERTS/I_F.CANNEX.COMMENT.ENTRY.TABLE` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.COM.RECORD.TYPE` | `CannexCommentEntryTable_RecordType` | TField |  | This field is used to store the Fixed value to indicate Order Comment record type. |
| 2 | `CANNEX.COM.COMMENT` | `CannexCommentEntryTable_Comment` | TField |  | This field is used to store the Free format comments or notes regarding the application. |
| 3 | `CANNEX.COM.RESERVED.1` | `CannexCommentEntryTable_Reserved1` | TField |  |  |
| 4 | `CANNEX.COM.RESERVED.2` | `CannexCommentEntryTable_Reserved2` | TField |  |  |
| 5 | `CANNEX.COM.RESERVED.3` | `CannexCommentEntryTable_Reserved3` | TField |  |  |
| 6 | `CANNEX.COM.RESERVED.4` | `CannexCommentEntryTable_Reserved4` | TField |  |  |
| 7 | `CANNEX.COM.RESERVED.5` | `CannexCommentEntryTable_Reserved5` | TField |  |  |
| 8 | `CANNEX.COM.RESERVED.6` | `CannexCommentEntryTable_Reserved6` | TField |  |  |
| 9 | `CANNEX.COM.RESERVED.7` | `CannexCommentEntryTable_Reserved7` | TField |  |  |
| 10 | `CANNEX.COM.RESERVED.8` | `CannexCommentEntryTable_Reserved8` | TField |  |  |
| 11 | `CANNEX.COM.RESERVED.9` | `CannexCommentEntryTable_Reserved9` | TField |  |  |
| 12 | `CANNEX.COM.RESERVED.10` | `CannexCommentEntryTable_Reserved10` | TField |  |  |
| 13 | `CANNEX.COM.LOCAL.REF` | `CannexCommentEntryTable_LocalRef` |  |  |  |
| 14 | `CANNEX.COM.OVERRIDE` | `CannexCommentEntryTable_Override` |  |  |  |
| 15 | `CANNEX.COM.RECORD.STATUS` | `CannexCommentEntryTable_RecordStatus` | String |  |  |
| 16 | `CANNEX.COM.CURR.NO` | `CannexCommentEntryTable_CurrNo` | String |  |  |
| 17 | `CANNEX.COM.INPUTTER` | `CannexCommentEntryTable_Inputter` |  |  |  |
| 18 | `CANNEX.COM.DATE.TIME` | `CannexCommentEntryTable_DateTime` |  |  |  |
| 19 | `CANNEX.COM.AUTHORISER` | `CannexCommentEntryTable_Authoriser` | String |  |  |
| 20 | `CANNEX.COM.CO.CODE` | `CannexCommentEntryTable_CoCode` | String |  |  |
| 21 | `CANNEX.COM.DEPT.CODE` | `CannexCommentEntryTable_DeptCode` | String |  |  |
| 22 | `CANNEX.COM.AUDITOR.CODE` | `CannexCommentEntryTable_AuditorCode` | String |  |  |
| 23 | `CANNEX.COM.AUDIT.DATE.TIME` | `CannexCommentEntryTable_AuditDateTime` | String |  |  |
