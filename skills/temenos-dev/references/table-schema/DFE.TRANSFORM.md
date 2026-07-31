# DFE.TRANSFORM — Table Schema

> Source: `INSERTS/I_F.DFE.TRANSFORM` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.TRANS.DESCRIPTION` | `DfeTransform_Description` |  |  |  |
| 2 | `DFE.TRANS.XSLT.MAPPING` | `DfeTransform_XsltMapping` | TField |  |  |
| 3 | `DFE.TRANS.RESERVED.10` | `DfeTransform_Reserved10` | TField |  |  |
| 4 | `DFE.TRANS.RESERVED.9` | `DfeTransform_Reserved9` | TField |  |  |
| 5 | `DFE.TRANS.RESERVED.8` | `DfeTransform_Reserved8` | TField |  |  |
| 6 | `DFE.TRANS.RESERVED.7` | `DfeTransform_Reserved7` | TField |  |  |
| 7 | `DFE.TRANS.RESERVED.6` | `DfeTransform_Reserved6` | TField |  |  |
| 8 | `DFE.TRANS.RESERVED.5` | `DfeTransform_Reserved5` | TField |  |  |
| 9 | `DFE.TRANS.RESERVED.4` | `DfeTransform_Reserved4` | TField |  |  |
| 10 | `DFE.TRANS.RESERVED.3` | `DfeTransform_Reserved3` | TField |  |  |
| 11 | `DFE.TRANS.RESERVED.2` | `DfeTransform_Reserved2` | TField |  |  |
| 12 | `DFE.TRANS.RESERVED.1` | `DfeTransform_Reserved1` | TField |  |  |
| 13 | `DFE.TRANS.RECORD.STATUS` | `DfeTransform_RecordStatus` | String |  |  |
| 14 | `DFE.TRANS.CURR.NO` | `DfeTransform_CurrNo` | String |  |  |
| 15 | `DFE.TRANS.INPUTTER` | `DfeTransform_Inputter` |  |  |  |
| 16 | `DFE.TRANS.DATE.TIME` | `DfeTransform_DateTime` |  |  |  |
| 17 | `DFE.TRANS.AUTHORISER` | `DfeTransform_Authoriser` | String |  |  |
| 18 | `DFE.TRANS.CO.CODE` | `DfeTransform_CoCode` | String |  |  |
| 19 | `DFE.TRANS.DEPT.CODE` | `DfeTransform_DeptCode` | String |  |  |
| 20 | `DFE.TRANS.AUDITOR.CODE` | `DfeTransform_AuditorCode` | String |  |  |
| 21 | `DFE.TRANS.AUDIT.DATE.TIME` | `DfeTransform_AuditDateTime` | String |  |  |
