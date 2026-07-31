# LQ.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LQ.PARAMETER` in `LQ_LiquidityManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LQ.PARAM.ATTRIBUTES.ENRICH.API` | `LqParameter_AttributesEnrichApi` | TField |  | The name of the API used to derive the attributes of Liquidity Management payments. This program supersedes the default derived attributes. Some of the attributes that can be influenced by the API are external account details, internal account details, account residing service and BIC. The API is applicable for: 1. Liquidity Transfer Advices (LTA) 2. Liquidity Transfer Requests (LTR) booked in TPH from Order Entry screens. |
| 2 | `LQ.PARAM.LOCAL.REF` | `LqParameter_LocalRef` |  |  |  |
| 3 | `LQ.PARAM.OVERRIDE` | `LqParameter_Override` |  |  |  |
| 4 | `LQ.PARAM.RECORD.STATUS` | `LqParameter_RecordStatus` | String |  |  |
| 5 | `LQ.PARAM.CURR.NO` | `LqParameter_CurrNo` | String |  |  |
| 6 | `LQ.PARAM.INPUTTER` | `LqParameter_Inputter` |  |  |  |
| 7 | `LQ.PARAM.DATE.TIME` | `LqParameter_DateTime` |  |  |  |
| 8 | `LQ.PARAM.AUTHORISER` | `LqParameter_Authoriser` | String |  |  |
| 9 | `LQ.PARAM.CO.CODE` | `LqParameter_CoCode` | String |  |  |
| 10 | `LQ.PARAM.DEPT.CODE` | `LqParameter_DeptCode` | String |  |  |
| 11 | `LQ.PARAM.AUDITOR.CODE` | `LqParameter_AuditorCode` | String |  |  |
| 12 | `LQ.PARAM.AUDIT.DATE.TIME` | `LqParameter_AuditDateTime` | String |  |  |
