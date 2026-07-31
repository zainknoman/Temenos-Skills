# OA.FORMLET — Table Schema

> Source: `INSERTS/I_F.OA.FORMLET` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.FLT.DESCRIPTION` | `OaFormlet_Description` |  |  |  |
| 2 | `OA.FLT.FULL.DESC` | `OaFormlet_FullDesc` |  |  |  |
| 3 | `OA.FLT.FORMLET.CLASS` | `OaFormlet_FormletClass` | TField | Yes | Mandatory field. The formlet class to which this formlet belongs to. |
| 4 | `OA.FLT.RESERVED.10` | `OaFormlet_Reserved10` | TField |  |  |
| 5 | `OA.FLT.RESERVED.9` | `OaFormlet_Reserved9` | TField |  |  |
| 6 | `OA.FLT.RESERVED.8` | `OaFormlet_Reserved8` | TField |  |  |
| 7 | `OA.FLT.RESERVED.7` | `OaFormlet_Reserved7` | TField |  |  |
| 8 | `OA.FLT.RESERVED.6` | `OaFormlet_Reserved6` | TField |  |  |
| 9 | `OA.FLT.RESERVED.5` | `OaFormlet_Reserved5` | TField |  |  |
| 10 | `OA.FLT.RESERVED.4` | `OaFormlet_Reserved4` | TField |  |  |
| 11 | `OA.FLT.RESERVED.3` | `OaFormlet_Reserved3` | TField |  |  |
| 12 | `OA.FLT.RESERVED.2` | `OaFormlet_Reserved2` | TField |  |  |
| 13 | `OA.FLT.RESERVED.1` | `OaFormlet_Reserved1` | TField |  |  |
| 14 | `OA.FLT.LOCAL.REF` | `OaFormlet_LocalRef` |  |  |  |
| 15 | `OA.FLT.OVERRIDE` | `OaFormlet_Override` |  |  |  |
| 16 | `OA.FLT.RECORD.STATUS` | `OaFormlet_RecordStatus` | String |  |  |
| 17 | `OA.FLT.CURR.NO` | `OaFormlet_CurrNo` | String |  |  |
| 18 | `OA.FLT.INPUTTER` | `OaFormlet_Inputter` |  |  |  |
| 19 | `OA.FLT.DATE.TIME` | `OaFormlet_DateTime` |  |  |  |
| 20 | `OA.FLT.AUTHORISER` | `OaFormlet_Authoriser` | String |  |  |
| 21 | `OA.FLT.CO.CODE` | `OaFormlet_CoCode` | String |  |  |
| 22 | `OA.FLT.DEPT.CODE` | `OaFormlet_DeptCode` | String |  |  |
| 23 | `OA.FLT.AUDITOR.CODE` | `OaFormlet_AuditorCode` | String |  |  |
| 24 | `OA.FLT.AUDIT.DATE.TIME` | `OaFormlet_AuditDateTime` | String |  |  |
