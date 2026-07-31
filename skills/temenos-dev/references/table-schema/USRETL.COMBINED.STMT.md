# USRETL.COMBINED.STMT — Table Schema

> Source: `INSERTS/I_F.USRETL.COMBINED.STMT` in `USRETL_CombinedStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CST.LEAD.ACCOUNT` | `UsretlCombinedStmt_LeadAccount` | TField | Yes | Single value field. Defines the Customer Account considered as a Lead account. Valid Account Number from ACCOUNT table. Mandatory Input. System does not allow opening new Combined statements prefernces record with Lead Account if it is dormant or closed at the time of record's creation. |
| 2 | `AC.CST.STMT.FREQ` | `UsretlCombinedStmt_StmtFreq` | TField |  | Combined statement frequency. This frequency is used for combined statements generation. Once defined it is defaulted to all accounts belonging to combined statement set. |
| 3 | `AC.CST.SEC.ACCOUNT` | `UsretlCombinedStmt_SecAccount` |  |  |  |
| 4 | `AC.CST.PRINTING` | `UsretlCombinedStmt_Printing` | TField |  | This field is used to determine the printing mode. The list of options available in the dropdown attached to the field are: Both/Print and Email (B), Print (P), Do not mail (D), Hold (H), Email (E) and Dormant (X). Based on the value in this field there will be one letter code added in the top right corner of the first page of the statment: B for Both, P for Print, D for Do not mail, H for Hold, E for Email and X for Dormant (in case lead account becomes dormant). |
| 5 | `AC.CST.IMAGE.OPTIONS` | `UsretlCombinedStmt_ImageOptions` | TField |  | Valid entry from USRETL.IMAGE.OPTIONS table to define the presence of images in the combined statement. |
| 6 | `AC.CST.STMT.FREQ.2` | `UsretlCombinedStmt_StmtFreq2` |  |  |  |
| 7 | `AC.CST.FREQ.NO` | `UsretlCombinedStmt_FreqNo` |  |  |  |
| 8 | `AC.CST.RESERVED.13` | `UsretlCombinedStmt_Reserved13` | TField |  |  |
| 9 | `AC.CST.RESERVED.12` | `UsretlCombinedStmt_Reserved12` | TField |  |  |
| 10 | `AC.CST.RESERVED.11` | `UsretlCombinedStmt_Reserved11` | TField |  |  |
| 11 | `AC.CST.RESERVED.10` | `UsretlCombinedStmt_Reserved10` | TField |  |  |
| 12 | `AC.CST.RESERVED.9` | `UsretlCombinedStmt_Reserved9` | TField |  |  |
| 13 | `AC.CST.RESERVED.8` | `UsretlCombinedStmt_Reserved8` | TField |  |  |
| 14 | `AC.CST.RESERVED.7` | `UsretlCombinedStmt_Reserved7` | TField |  |  |
| 15 | `AC.CST.RESERVED.6` | `UsretlCombinedStmt_Reserved6` | TField |  |  |
| 16 | `AC.CST.RESERVED.5` | `UsretlCombinedStmt_Reserved5` | TField |  |  |
| 17 | `AC.CST.RESERVED.4` | `UsretlCombinedStmt_Reserved4` | TField |  |  |
| 18 | `AC.CST.RESERVED.3` | `UsretlCombinedStmt_Reserved3` | TField |  |  |
| 19 | `AC.CST.RESERVED.2` | `UsretlCombinedStmt_Reserved2` | TField |  |  |
| 20 | `AC.CST.OVERRIDE` | `UsretlCombinedStmt_Override` |  |  |  |
| 21 | `AC.CST.RECORD.STATUS` | `UsretlCombinedStmt_RecordStatus` | String |  |  |
| 22 | `AC.CST.CURR.NO` | `UsretlCombinedStmt_CurrNo` | String |  |  |
| 23 | `AC.CST.INPUTTER` | `UsretlCombinedStmt_Inputter` |  |  |  |
| 24 | `AC.CST.DATE.TIME` | `UsretlCombinedStmt_DateTime` |  |  |  |
| 25 | `AC.CST.AUTHORISER` | `UsretlCombinedStmt_Authoriser` | String |  |  |
| 26 | `AC.CST.CO.CODE` | `UsretlCombinedStmt_CoCode` | String |  |  |
| 27 | `AC.CST.DEPT.CODE` | `UsretlCombinedStmt_DeptCode` | String |  |  |
| 28 | `AC.CST.AUDITOR.CODE` | `UsretlCombinedStmt_AuditorCode` | String |  |  |
| 29 | `AC.CST.AUDIT.DATE.TIME` | `UsretlCombinedStmt_AuditDateTime` | String |  |  |
