# LI.TIME.CODE — Table Schema

> Source: `INSERTS/I_F.LI.TIME.CODE` in `LI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.TC.DESCRIPTION` | `LiTimeCode_Description` | TField |  | A meaningful description pertaining to the record |
| 2 | `LI.TC.NO.OF.DAYS` | `LiTimeCode_NoOfDays` | TField | Yes | Specifies time sub-divisions of a Limit, each of which is available for a different maturity period. Validation rule: Mandatory and No change field |
| 3 | `LI.TC.RESERVED05` | `LiTimeCode_Reserved05` | TField |  |  |
| 4 | `LI.TC.RESERVED04` | `LiTimeCode_Reserved04` | TField |  |  |
| 5 | `LI.TC.RESERVED03` | `LiTimeCode_Reserved03` | TField |  |  |
| 6 | `LI.TC.RESERVED02` | `LiTimeCode_Reserved02` | TField |  |  |
| 7 | `LI.TC.RESERVED01` | `LiTimeCode_Reserved01` | TField |  |  |
| 8 | `LI.TC.LOCAL.REF` | `LiTimeCode_LocalRef` |  |  |  |
| 9 | `LI.TC.OVERRIDE` | `LiTimeCode_Override` |  |  |  |
| 10 | `LI.TC.RECORD.STATUS` | `LiTimeCode_RecordStatus` | String |  |  |
| 11 | `LI.TC.CURR.NO` | `LiTimeCode_CurrNo` | String |  |  |
| 12 | `LI.TC.INPUTTER` | `LiTimeCode_Inputter` |  |  |  |
| 13 | `LI.TC.DATE.TIME` | `LiTimeCode_DateTime` |  |  |  |
| 14 | `LI.TC.AUTHORISER` | `LiTimeCode_Authoriser` | String |  |  |
| 15 | `LI.TC.CO.CODE` | `LiTimeCode_CoCode` | String |  |  |
| 16 | `LI.TC.DEPT.CODE` | `LiTimeCode_DeptCode` | String |  |  |
| 17 | `LI.TC.AUDITOR.CODE` | `LiTimeCode_AuditorCode` | String |  |  |
| 18 | `LI.TC.AUDIT.DATE.TIME` | `LiTimeCode_AuditDateTime` | String |  |  |
