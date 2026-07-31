# EB.MANDATE — Table Schema

> Source: `INSERTS/I_F.EB.MANDATE` in `EB_Mandate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MAND.DESCRIPTION` | `EbMandate_Description` |  |  |  |
| 2 | `EB.MAND.UP.TO.AMOUNT` | `EbMandate_UpToAmount` |  |  |  |
| 3 | `EB.MAND.SIGNATORY.GROUP` | `EbMandate_SignatoryGroup` |  |  |  |
| 4 | `EB.MAND.MIN.NO.SIGNATORIES` | `EbMandate_MinNoSignatories` |  |  |  |
| 5 | `EB.MAND.LIMIT.CCY` | `EbMandate_LimitCcy` | TField | Yes | Currency used in this mandate for amounts. Need not be same as related account currency(s). Validation Rules: 1. Mandatory field when UP.TO.AMOUNT is defined. 2. Should be valid currency. |
| 6 | `EB.MAND.BNK.APPR.RTN` | `EbMandate_BnkApprRtn` | TField |  | Field to attach local hook routine to the mandates to check additional conditions or otherwise banks approval. When the hook routine is successful, then the transaction remains in INAO and an override message is thrown. The AUTHORISER field of such transaction will be appended with a key word '_SIGCOMPLETED' to identify such records. These transactions can be authorized by a T24 user with appropriate rights for that override. The hook routine should contain one single return argument and should return value as 2, if the bank's approval is required. A valid local routine Validation Rules: 1. Should be a valid record in EB.API application. |
| 7 | `EB.MAND.MANDATE.RULE` | `EbMandate_MandateRule` |  |  |  |
| 8 | `EB.MAND.RULE.SIGN.GROUP` | `EbMandate_RuleSignGroup` |  |  |  |
| 9 | `EB.MAND.RULE.MIN.NO.SIGN` | `EbMandate_RuleMinNoSign` |  |  |  |
| 10 | `EB.MAND.RULE.RESERVED.2` | `EbMandate_RuleReserved2` |  |  |  |
| 11 | `EB.MAND.RULE.RESERVED.1` | `EbMandate_RuleReserved1` |  |  |  |
| 12 | `EB.MAND.RESERVED.4` | `EbMandate_Reserved4` | TField |  |  |
| 13 | `EB.MAND.RESERVED.3` | `EbMandate_Reserved3` | TField |  |  |
| 14 | `EB.MAND.RESERVED.2` | `EbMandate_Reserved2` | TField |  |  |
| 15 | `EB.MAND.RESERVED.1` | `EbMandate_Reserved1` | TField |  |  |
| 16 | `EB.MAND.LOCAL.REF` | `EbMandate_LocalRef` |  |  |  |
| 17 | `EB.MAND.OVERRIDE` | `EbMandate_Override` |  |  |  |
| 18 | `EB.MAND.RECORD.STATUS` | `EbMandate_RecordStatus` | String |  |  |
| 19 | `EB.MAND.CURR.NO` | `EbMandate_CurrNo` | String |  |  |
| 20 | `EB.MAND.INPUTTER` | `EbMandate_Inputter` |  |  |  |
| 21 | `EB.MAND.DATE.TIME` | `EbMandate_DateTime` |  |  |  |
| 22 | `EB.MAND.AUTHORISER` | `EbMandate_Authoriser` | String |  |  |
| 23 | `EB.MAND.CO.CODE` | `EbMandate_CoCode` | String |  |  |
| 24 | `EB.MAND.DEPT.CODE` | `EbMandate_DeptCode` | String |  |  |
| 25 | `EB.MAND.AUDITOR.CODE` | `EbMandate_AuditorCode` | String |  |  |
| 26 | `EB.MAND.AUDIT.DATE.TIME` | `EbMandate_AuditDateTime` | String |  |  |
