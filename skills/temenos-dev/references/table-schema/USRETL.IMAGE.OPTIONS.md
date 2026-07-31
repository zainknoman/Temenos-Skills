# USRETL.IMAGE.OPTIONS — Table Schema

> Source: `INSERTS/I_F.USRETL.IMAGE.OPTIONS` in `USRETL_CombinedStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IMG.OPT.VERTICAL` | `UsretlImageOptions_Vertical` | TField |  | Reserved for future use. This field defines how many images should be placed on the statement vertically |
| 2 | `AC.IMG.OPT.HORIZONTAL` | `UsretlImageOptions_Horizontal` | TField |  | Reserved for future use. This field defines how many images should be placed on the statement horizontally |
| 3 | `AC.IMG.OPT.DRFRONT` | `UsretlImageOptions_Drfront` | TField |  | Yes/No field. Indicates if debit transaction front check images should be included on the statement |
| 4 | `AC.IMG.OPT.DRBACK` | `UsretlImageOptions_Drback` | TField |  | Yes/No field. Indicates if debit transaction back check images should be included on the statement |
| 5 | `AC.IMG.OPT.CRFRONT` | `UsretlImageOptions_Crfront` | TField |  | Yes/No field. Indicates if credit transaction front check images should be included on the statement |
| 6 | `AC.IMG.OPT.CRBACK` | `UsretlImageOptions_Crback` | TField |  | Yes/No field. Indicates if credit transaction back check images should be included on the statement |
| 7 | `AC.IMG.OPT.RESERVED.15` | `UsretlImageOptions_Reserved15` | TField |  |  |
| 8 | `AC.IMG.OPT.RESERVED.14` | `UsretlImageOptions_Reserved14` | TField |  |  |
| 9 | `AC.IMG.OPT.RESERVED.13` | `UsretlImageOptions_Reserved13` | TField |  |  |
| 10 | `AC.IMG.OPT.RESERVED.12` | `UsretlImageOptions_Reserved12` | TField |  |  |
| 11 | `AC.IMG.OPT.RESERVED.11` | `UsretlImageOptions_Reserved11` | TField |  |  |
| 12 | `AC.IMG.OPT.RESERVED.10` | `UsretlImageOptions_Reserved10` | TField |  |  |
| 13 | `AC.IMG.OPT.RESERVED.9` | `UsretlImageOptions_Reserved9` | TField |  |  |
| 14 | `AC.IMG.OPT.RESERVED.8` | `UsretlImageOptions_Reserved8` | TField |  |  |
| 15 | `AC.IMG.OPT.RESERVED.7` | `UsretlImageOptions_Reserved7` | TField |  |  |
| 16 | `AC.IMG.OPT.RESERVED.6` | `UsretlImageOptions_Reserved6` | TField |  |  |
| 17 | `AC.IMG.OPT.RESERVED.5` | `UsretlImageOptions_Reserved5` | TField |  |  |
| 18 | `AC.IMG.OPT.RESERVED.4` | `UsretlImageOptions_Reserved4` | TField |  |  |
| 19 | `AC.IMG.OPT.RESERVED.3` | `UsretlImageOptions_Reserved3` | TField |  |  |
| 20 | `AC.IMG.OPT.RESERVED.2` | `UsretlImageOptions_Reserved2` | TField |  |  |
| 21 | `AC.IMG.OPT.RESERVED.1` | `UsretlImageOptions_Reserved1` | TField |  |  |
| 22 | `AC.IMG.OPT.RECORD.STATUS` | `UsretlImageOptions_RecordStatus` | String |  |  |
| 23 | `AC.IMG.OPT.CURR.NO` | `UsretlImageOptions_CurrNo` | String |  |  |
| 24 | `AC.IMG.OPT.INPUTTER` | `UsretlImageOptions_Inputter` |  |  |  |
| 25 | `AC.IMG.OPT.DATE.TIME` | `UsretlImageOptions_DateTime` |  |  |  |
| 26 | `AC.IMG.OPT.AUTHORISER` | `UsretlImageOptions_Authoriser` | String |  |  |
| 27 | `AC.IMG.OPT.CO.CODE` | `UsretlImageOptions_CoCode` | String |  |  |
| 28 | `AC.IMG.OPT.DEPT.CODE` | `UsretlImageOptions_DeptCode` | String |  |  |
| 29 | `AC.IMG.OPT.AUDITOR.CODE` | `UsretlImageOptions_AuditorCode` | String |  |  |
| 30 | `AC.IMG.OPT.AUDIT.DATE.TIME` | `UsretlImageOptions_AuditDateTime` | String |  |  |
