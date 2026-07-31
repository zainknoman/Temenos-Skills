# EB.JSN.RELEASE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.JSN.RELEASE.PARAMETER` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.JSN.DESCRIPTION` | `EbJsnReleaseParameter_Description` |  |  |  |
| 2 | `EB.JSN.HOLD.APPLICATION` | `EbJsnReleaseParameter_HoldApplication` |  |  |  |
| 3 | `EB.JSN.TO.FIELD` | `EbJsnReleaseParameter_ToField` |  |  |  |
| 4 | `EB.JSN.FROM.FIELD` | `EbJsnReleaseParameter_FromField` |  |  |  |
| 5 | `EB.JSN.FLD.CONV` | `EbJsnReleaseParameter_FldConv` |  |  |  |
| 6 | `EB.JSN.DATA.CONV.RTN` | `EbJsnReleaseParameter_DataConvRtn` | TField |  |  |
| 7 | `EB.JSN.HOLD.ALLOWED` | `EbJsnReleaseParameter_HoldAllowed` | TField |  |  |
| 8 | `EB.JSN.APPLN.FIELD.NAME` | `EbJsnReleaseParameter_ApplnFieldName` |  |  |  |
| 9 | `EB.JSN.CHECK.PRODUCT` | `EbJsnReleaseParameter_CheckProduct` |  |  |  |
| 10 | `EB.JSN.RESERVED.3` | `EbJsnReleaseParameter_Reserved3` | TField |  |  |
| 11 | `EB.JSN.RESERVED.2` | `EbJsnReleaseParameter_Reserved2` | TField |  |  |
| 12 | `EB.JSN.RESERVED.1` | `EbJsnReleaseParameter_Reserved1` | TField |  |  |
| 13 | `EB.JSN.LOCAL.REF` | `EbJsnReleaseParameter_LocalRef` |  |  |  |
| 14 | `EB.JSN.OVERRIDE` | `EbJsnReleaseParameter_Override` |  |  |  |
| 15 | `EB.JSN.RECORD.STATUS` | `EbJsnReleaseParameter_RecordStatus` | String |  |  |
| 16 | `EB.JSN.CURR.NO` | `EbJsnReleaseParameter_CurrNo` | String |  |  |
| 17 | `EB.JSN.INPUTTER` | `EbJsnReleaseParameter_Inputter` |  |  |  |
| 18 | `EB.JSN.DATE.TIME` | `EbJsnReleaseParameter_DateTime` |  |  |  |
| 19 | `EB.JSN.AUTHORISER` | `EbJsnReleaseParameter_Authoriser` | String |  |  |
| 20 | `EB.JSN.CO.CODE` | `EbJsnReleaseParameter_CoCode` | String |  |  |
| 21 | `EB.JSN.DEPT.CODE` | `EbJsnReleaseParameter_DeptCode` | String |  |  |
| 22 | `EB.JSN.AUDITOR.CODE` | `EbJsnReleaseParameter_AuditorCode` | String |  |  |
| 23 | `EB.JSN.AUDIT.DATE.TIME` | `EbJsnReleaseParameter_AuditDateTime` | String |  |  |
