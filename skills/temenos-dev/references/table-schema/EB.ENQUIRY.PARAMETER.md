# EB.ENQUIRY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.ENQUIRY.PARAMETER` in `EB_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENQ.PARAM.DESCRIPTION` | `EbEnquiryParameter_Description` |  |  |  |
| 2 | `ENQ.PARAM.EMBEDDED.FLAG` | `EbEnquiryParameter_EmbeddedFlag` | TField | Yes | If this field set to 'YES', then the Obligation will be enabled by default for this channel. This field can be overridden with the definition in EB.CHANNEL (embedded.flag). Validation Rules: It is a non-mandatory field. it needs to be exclusively setup to 'YES' when needed. |
| 3 | `ENQ.PARAM.RETAIN.ENQ.COMMON` | `EbEnquiryParameter_RetainEnqCommon` | TField | Yes | If this field is set to 'YES', then the enquiry selection common variables(D.FIELDS, D.LOGICAL.OPERANDS, D.RANGE.AND.VALUE) will not be reset between each R type field defined in a standard selection Validation Rules: It is a non-mandatory field. It allows 'YES' or 'NULL', Null will be default. It needs to be exclusively setup to 'YES' when needed. |
| 4 | `ENQ.PARAM.CACHED.TABLE` | `EbEnquiryParameter_CachedTable` |  |  |  |
| 5 | `ENQ.PARAM.API.GEN.FLD.NAME` | `EbEnquiryParameter_ApiGenFldName` |  |  |  |
| 6 | `ENQ.PARAM.API.GEN.FLD.LABEL` | `EbEnquiryParameter_ApiGenFldLabel` |  |  |  |
| 7 | `ENQ.PARAM.API.GEN.FLD.TYPE` | `EbEnquiryParameter_ApiGenFldType` |  |  |  |
| 8 | `ENQ.PARAM.RESERVED.5` | `EbEnquiryParameter_Reserved5` |  |  |  |
| 9 | `ENQ.PARAM.RESERVED.4` | `EbEnquiryParameter_Reserved4` |  |  |  |
| 10 | `ENQ.PARAM.RESERVED.3` | `EbEnquiryParameter_Reserved3` | TField |  |  |
| 11 | `ENQ.PARAM.RESERVED.2` | `EbEnquiryParameter_Reserved2` | TField |  |  |
| 12 | `ENQ.PARAM.RESERVED.1` | `EbEnquiryParameter_Reserved1` | TField |  |  |
| 13 | `ENQ.PARAM.RECORD.STATUS` | `EbEnquiryParameter_RecordStatus` | String |  |  |
| 14 | `ENQ.PARAM.CURR.NO` | `EbEnquiryParameter_CurrNo` | String |  |  |
| 15 | `ENQ.PARAM.INPUTTER` | `EbEnquiryParameter_Inputter` |  |  |  |
| 16 | `ENQ.PARAM.DATE.TIME` | `EbEnquiryParameter_DateTime` |  |  |  |
| 17 | `ENQ.PARAM.AUTHORISER` | `EbEnquiryParameter_Authoriser` | String |  |  |
| 18 | `ENQ.PARAM.CO.CODE` | `EbEnquiryParameter_CoCode` | String |  |  |
| 19 | `ENQ.PARAM.DEPT.CODE` | `EbEnquiryParameter_DeptCode` | String |  |  |
| 20 | `ENQ.PARAM.AUDITOR.CODE` | `EbEnquiryParameter_AuditorCode` | String |  |  |
| 21 | `ENQ.PARAM.AUDIT.DATE.TIME` | `EbEnquiryParameter_AuditDateTime` | String |  |  |
