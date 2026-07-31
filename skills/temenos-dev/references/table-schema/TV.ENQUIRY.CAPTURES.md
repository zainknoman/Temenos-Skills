# TV.ENQUIRY.CAPTURES — Table Schema

> Source: `INSERTS/I_F.TV.ENQUIRY.CAPTURES` in `TV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.EC.CAPTURE.ENQUIRY` | `TvEnquiryCaptures_CaptureEnquiry` |  |  |  |
| 2 | `EB.EC.RESERVED.8` | `TvEnquiryCaptures_Reserved8` | TField |  |  |
| 3 | `EB.EC.RESERVED.7` | `TvEnquiryCaptures_Reserved7` | TField |  |  |
| 4 | `EB.EC.RESERVED.6` | `TvEnquiryCaptures_Reserved6` | TField |  |  |
| 5 | `EB.EC.RESERVED.5` | `TvEnquiryCaptures_Reserved5` | TField |  |  |
| 6 | `EB.EC.RESERVED.4` | `TvEnquiryCaptures_Reserved4` | TField |  |  |
| 7 | `EB.EC.RESERVED.3` | `TvEnquiryCaptures_Reserved3` | TField |  |  |
| 8 | `EB.EC.RESERVED.2` | `TvEnquiryCaptures_Reserved2` | TField |  |  |
| 9 | `EB.EC.RESERVED.1` | `TvEnquiryCaptures_Reserved1` | TField |  |  |
| 10 | `EB.EC.RECORD.STATUS` | `TvEnquiryCaptures_RecordStatus` | String |  |  |
| 11 | `EB.EC.CURR.NO` | `TvEnquiryCaptures_CurrNo` | String |  |  |
| 12 | `EB.EC.INPUTTER` | `TvEnquiryCaptures_Inputter` |  |  |  |
| 13 | `EB.EC.DATE.TIME` | `TvEnquiryCaptures_DateTime` |  |  |  |
| 14 | `EB.EC.AUTHORISER` | `TvEnquiryCaptures_Authoriser` | String |  |  |
| 15 | `EB.EC.CO.CODE` | `TvEnquiryCaptures_CoCode` | String |  |  |
| 16 | `EB.EC.DEPT.CODE` | `TvEnquiryCaptures_DeptCode` | String |  |  |
| 17 | `EB.EC.AUDITOR.CODE` | `TvEnquiryCaptures_AuditorCode` | String |  |  |
| 18 | `EB.EC.AUDIT.DATE.TIME` | `TvEnquiryCaptures_AuditDateTime` | String |  |  |
