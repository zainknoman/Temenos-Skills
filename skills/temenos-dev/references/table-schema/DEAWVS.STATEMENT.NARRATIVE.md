# DEAWVS.STATEMENT.NARRATIVE — Table Schema

> Source: `INSERTS/I_F.DEAWVS.STATEMENT.NARRATIVE` in `DEAWVS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCT.PARAM.THRESHOLD.AMOUNT` | `DeawvsStatementNarrative_ThresholdAmount` | TField |  | The threshold limit for the transaction to be qualified for regulatory reporting. Amount indicated in this field, indicates the Local Currency Amount. |
| 2 | `ACCT.PARAM.SHORT.TEXT` | `DeawvsStatementNarrative_ShortText` |  |  |  |
| 3 | `ACCT.PARAM.RESIDENCY` | `DeawvsStatementNarrative_Residency` | TField |  |  |
| 4 | `ACCT.PARAM.CURRENCY.MARKET` | `DeawvsStatementNarrative_CurrencyMarket` | TField |  | Default Value: '1' This will determine the Currency Market against which the Exchange Rate will be chosen. |
| 5 | `ACCT.PARAM.LOCAL.REF` | `DeawvsStatementNarrative_LocalRef` |  |  |  |
| 6 | `ACCT.PARAM.RESERVED.8` | `DeawvsStatementNarrative_Reserved8` | TField |  |  |
| 7 | `ACCT.PARAM.RESERVED.7` | `DeawvsStatementNarrative_Reserved7` | TField |  |  |
| 8 | `ACCT.PARAM.RESERVED.6` | `DeawvsStatementNarrative_Reserved6` | TField |  |  |
| 9 | `ACCT.PARAM.RESERVED.5` | `DeawvsStatementNarrative_Reserved5` | TField |  |  |
| 10 | `ACCT.PARAM.RESERVED.4` | `DeawvsStatementNarrative_Reserved4` | TField |  |  |
| 11 | `ACCT.PARAM.RESERVED.3` | `DeawvsStatementNarrative_Reserved3` | TField |  |  |
| 12 | `ACCT.PARAM.RESERVED.2` | `DeawvsStatementNarrative_Reserved2` | TField |  |  |
| 13 | `ACCT.PARAM.RESERVED.1` | `DeawvsStatementNarrative_Reserved1` | TField |  |  |
| 14 | `ACCT.PARAM.OVERRIDE` | `DeawvsStatementNarrative_Override` |  |  |  |
| 15 | `ACCT.PARAM.RECORD.STATUS` | `DeawvsStatementNarrative_RecordStatus` | String |  |  |
| 16 | `ACCT.PARAM.CURR.NO` | `DeawvsStatementNarrative_CurrNo` | String |  |  |
| 17 | `ACCT.PARAM.INPUTTER` | `DeawvsStatementNarrative_Inputter` |  |  |  |
| 18 | `ACCT.PARAM.DATE.TIME` | `DeawvsStatementNarrative_DateTime` |  |  |  |
| 19 | `ACCT.PARAM.AUTHORISER` | `DeawvsStatementNarrative_Authoriser` | String |  |  |
| 20 | `ACCT.PARAM.CO.CODE` | `DeawvsStatementNarrative_CoCode` | String |  |  |
| 21 | `ACCT.PARAM.DEPT.CODE` | `DeawvsStatementNarrative_DeptCode` | String |  |  |
| 22 | `ACCT.PARAM.AUDITOR.CODE` | `DeawvsStatementNarrative_AuditorCode` | String |  |  |
| 23 | `ACCT.PARAM.AUDIT.DATE.TIME` | `DeawvsStatementNarrative_AuditDateTime` | String |  |  |
