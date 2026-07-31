# PP.POSTING.TOKENS — Table Schema

> Source: `INSERTS/I_F.PP.POSTING.TOKENS` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.POT.Token` | `PpPostingTokens_Token` |  |  |  |
| 2 | `PP.POT.UserToken` | `PpPostingTokens_Usertoken` |  |  |  |
| 3 | `PP.POT.UserTokenAPI` | `PpPostingTokens_Usertokenapi` |  |  |  |
| 4 | `PP.POT.RESERVED.3` | `PpPostingTokens_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.POT.RESERVED.2` | `PpPostingTokens_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.POT.RESERVED.1` | `PpPostingTokens_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.POT.LOCAL.REF` | `PpPostingTokens_LocalRef` |  |  |  |
| 8 | `PP.POT.OVERRIDE` | `PpPostingTokens_Override` |  |  |  |
| 9 | `PP.POT.RECORD.STATUS` | `PpPostingTokens_RecordStatus` | String |  |  |
| 10 | `PP.POT.CURR.NO` | `PpPostingTokens_CurrNo` | String |  |  |
| 11 | `PP.POT.INPUTTER` | `PpPostingTokens_Inputter` |  |  |  |
| 12 | `PP.POT.DATE.TIME` | `PpPostingTokens_DateTime` |  |  |  |
| 13 | `PP.POT.AUTHORISER` | `PpPostingTokens_Authoriser` | String |  |  |
| 14 | `PP.POT.CO.CODE` | `PpPostingTokens_CoCode` | String |  |  |
| 15 | `PP.POT.DEPT.CODE` | `PpPostingTokens_DeptCode` | String |  |  |
| 16 | `PP.POT.AUDITOR.CODE` | `PpPostingTokens_AuditorCode` | String |  |  |
| 17 | `PP.POT.AUDIT.DATE.TIME` | `PpPostingTokens_AuditDateTime` | String |  |  |
