# EB.CHANNEL — Table Schema

> Source: `INSERTS/I_F.EB.CHANNEL` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CHAN.DESC` | `EbChannel_Desc` |  |  |  |
| 2 | `EB.CHAN.SHORT.NAME` | `EbChannel_ShortName` |  |  |  |
| 3 | `EB.CHAN.CHANNEL.TYPE` | `EbChannel_ChannelType` | TField |  | The Type of a channel. Valid values are :- Internal - Access internal to T24 (e.g. from T24 Browser) Internet - Access via the internet (e.g. from external users with ARC-IB) |
| 4 | `EB.CHAN.UNSUPPRESS` | `EbChannel_Unsuppress` |  |  |  |
| 5 | `EB.CHAN.EMBEDDED.OBLIGATION` | `EbChannel_EmbeddedObligation` | TField | Yes | This field will override the definition in EB.ENQUIRY.PARAMETER(embedded.flag). If this field set to 'YES', then the Obligation will be enabled by default for this channel. Validation Rules: It is a non-mandatory field. it needs to be exclusively set up 'YES' when need. |
| 6 | `EB.CHAN.RESERVED.2` | `EbChannel_Reserved2` | TField |  |  |
| 7 | `EB.CHAN.RESERVED.1` | `EbChannel_Reserved1` | TField |  |  |
| 8 | `EB.CHAN.LOCAL.REF` | `EbChannel_LocalRef` |  |  |  |
| 9 | `EB.CHAN.RECORD.STATUS` | `EbChannel_RecordStatus` | String |  |  |
| 10 | `EB.CHAN.CURR.NO` | `EbChannel_CurrNo` | String |  |  |
| 11 | `EB.CHAN.INPUTTER` | `EbChannel_Inputter` |  |  |  |
| 12 | `EB.CHAN.DATE.TIME` | `EbChannel_DateTime` |  |  |  |
| 13 | `EB.CHAN.AUTHORISER` | `EbChannel_Authoriser` | String |  |  |
| 14 | `EB.CHAN.CO.CODE` | `EbChannel_CoCode` | String |  |  |
| 15 | `EB.CHAN.DEPT.CODE` | `EbChannel_DeptCode` | String |  |  |
| 16 | `EB.CHAN.AUDITOR.CODE` | `EbChannel_AuditorCode` | String |  |  |
| 17 | `EB.CHAN.AUDIT.DATE.TIME` | `EbChannel_AuditDateTime` | String |  |  |
