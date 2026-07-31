# ESTELL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESTELL.PARAMETER` in `ESTELL_NonCustomerCash.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESTELL.PARAM.DESCRIPTION` | `EstellParameter_Description` | TField |  | Limit about the threshold value |
| 2 | `ESTELL.PARAM.NONCUST.CASH.THRESHOLD` | `EstellParameter_NoncustCashThreshold` | TField |  | This field is used to set the Cash thresholdLimit for Non Customer Transactions, When a Non customer transactions is executed the limit set in the field will be checked |
| 3 | `ESTELL.PARAM.LOCAL.REF` | `EstellParameter_LocalRef` |  |  |  |
| 4 | `ESTELL.PARAM.LIMIT.TYPE` | `EstellParameter_LimitType` | TField |  | LIMIT.TYPE filed have values as TXN(indicates Transaction limit) or None |
| 5 | `ESTELL.PARAM.NONCUST.WITHDRAWAL.THRESHOLD` | `EstellParameter_NonCustWithdrawalThreshold` |  |  |  |
| 6 | `ESTELL.PARAM.RESERVED.3` | `EstellParameter_Reserved3` | TField |  | Reserved for future use |
| 7 | `ESTELL.PARAM.RESERVED.4` | `EstellParameter_Reserved4` | TField |  | Reserved for future use |
| 8 | `ESTELL.PARAM.RESERVED.5` | `EstellParameter_Reserved5` | TField |  | Reserved for future use |
| 9 | `ESTELL.PARAM.RESERVED.6` | `EstellParameter_Reserved6` | TField |  | Reserved for future use |
| 10 | `ESTELL.PARAM.RESERVED.7` | `EstellParameter_Reserved7` | TField |  | Reserved for future use |
| 11 | `ESTELL.PARAM.RESERVED.8` | `EstellParameter_Reserved8` | TField |  | Reserved for future use |
| 12 | `ESTELL.PARAM.RESERVED.9` | `EstellParameter_Reserved9` | TField |  | Reserved for future use |
| 13 | `ESTELL.PARAM.RESERVED.10` | `EstellParameter_Reserved10` | TField |  | Reserved for future use |
| 14 | `ESTELL.PARAM.RESERVED.11` | `EstellParameter_Reserved11` | TField |  | Reserved for future use |
| 15 | `ESTELL.PARAM.RESERVED.12` | `EstellParameter_Reserved12` | TField |  | Reserved for future use |
| 16 | `ESTELL.PARAM.RESERVED.13` | `EstellParameter_Reserved13` | TField |  | Reserved for future use |
| 17 | `ESTELL.PARAM.RESERVED.14` | `EstellParameter_Reserved14` | TField |  | Reserved for future use |
| 18 | `ESTELL.PARAM.RESERVED.15` | `EstellParameter_Reserved15` | TField |  | Reserved for future use |
| 19 | `ESTELL.PARAM.OVERRIDE` | `EstellParameter_Override` |  |  |  |
| 20 | `ESTELL.PARAM.RECORD.STATUS` | `EstellParameter_RecordStatus` | String |  |  |
| 21 | `ESTELL.PARAM.CURR.NO` | `EstellParameter_CurrNo` | String |  |  |
| 22 | `ESTELL.PARAM.INPUTTER` | `EstellParameter_Inputter` |  |  |  |
| 23 | `ESTELL.PARAM.DATE.TIME` | `EstellParameter_DateTime` |  |  |  |
| 24 | `ESTELL.PARAM.AUTHORISER` | `EstellParameter_Authoriser` | String |  |  |
| 25 | `ESTELL.PARAM.CO.CODE` | `EstellParameter_CoCode` | String |  |  |
| 26 | `ESTELL.PARAM.DEPT.CODE` | `EstellParameter_DeptCode` | String |  |  |
| 27 | `ESTELL.PARAM.AUDITOR.CODE` | `EstellParameter_AuditorCode` | String |  |  |
| 28 | `ESTELL.PARAM.AUDIT.DATE.TIME` | `EstellParameter_AuditDateTime` | String |  |  |
