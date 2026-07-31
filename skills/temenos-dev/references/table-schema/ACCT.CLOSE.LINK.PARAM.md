# ACCT.CLOSE.LINK.PARAM — Table Schema

> Source: `INSERTS/I_F.ACCT.CLOSE.LINK.PARAM` in `CABASE_AccountClosure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCT.CLOSE.PARAM.DESCRIPTION` | `AcctCloseLinkParam_Description` | TField |  | The value in the field will be used to display the override message, if the account linkage exist. |
| 2 | `ACCT.CLOSE.PARAM.SEL.CRITERIA` | `AcctCloseLinkParam_SelCriteria` |  |  |  |
| 3 | `ACCT.CLOSE.PARAM.RP.LINK.CHECK` | `AcctCloseLinkParam_RpLinkCheck` | TField |  | YES/NO/BOTHBoth Refer to Linkage check to be performed for both Register plan Payout and Normal Account closure.Yes Means - Record Applicable only for RP Payout linkage CheckNo or Blank - means the record is NOT applicable for RP Payout linkage Check |
| 4 | `ACCT.CLOSE.PARAM.RESERVED.7` | `AcctCloseLinkParam_Reserved7` | TField |  |  |
| 5 | `ACCT.CLOSE.PARAM.RESERVED.6` | `AcctCloseLinkParam_Reserved6` | TField |  |  |
| 6 | `ACCT.CLOSE.PARAM.RESERVED.5` | `AcctCloseLinkParam_Reserved5` | TField |  |  |
| 7 | `ACCT.CLOSE.PARAM.RESERVED.4` | `AcctCloseLinkParam_Reserved4` | TField |  |  |
| 8 | `ACCT.CLOSE.PARAM.RESERVED.3` | `AcctCloseLinkParam_Reserved3` | TField |  |  |
| 9 | `ACCT.CLOSE.PARAM.RESERVED.2` | `AcctCloseLinkParam_Reserved2` | TField |  |  |
| 10 | `ACCT.CLOSE.PARAM.RESERVED.1` | `AcctCloseLinkParam_Reserved1` | TField |  |  |
| 11 | `ACCT.CLOSE.PARAM.RECORD.STATUS` | `AcctCloseLinkParam_RecordStatus` | String |  |  |
| 12 | `ACCT.CLOSE.PARAM.CURR.NO` | `AcctCloseLinkParam_CurrNo` | String |  |  |
| 13 | `ACCT.CLOSE.PARAM.INPUTTER` | `AcctCloseLinkParam_Inputter` |  |  |  |
| 14 | `ACCT.CLOSE.PARAM.DATE.TIME` | `AcctCloseLinkParam_DateTime` |  |  |  |
| 15 | `ACCT.CLOSE.PARAM.AUTHORISER` | `AcctCloseLinkParam_Authoriser` | String |  |  |
| 16 | `ACCT.CLOSE.PARAM.CO.CODE` | `AcctCloseLinkParam_CoCode` | String |  |  |
| 17 | `ACCT.CLOSE.PARAM.DEPT.CODE` | `AcctCloseLinkParam_DeptCode` | String |  |  |
| 18 | `ACCT.CLOSE.PARAM.AUDITOR.CODE` | `AcctCloseLinkParam_AuditorCode` | String |  |  |
| 19 | `ACCT.CLOSE.PARAM.AUDIT.DATE.TIME` | `AcctCloseLinkParam_AuditDateTime` | String |  |  |
