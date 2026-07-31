# USRSRS.SWEEP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USRSRS.SWEEP.PARAMETER` in `USRSRS_RetailSweepPgm.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RSS.SWEEP.DESCRIPTION` | `UsrsrsSweepParameter_Description` |  |  |  |
| 2 | `RSS.SWEEP.SWEEP.REFERENCE` | `UsrsrsSweepParameter_SweepReference` |  |  |  |
| 3 | `RSS.SWEEP.TARGET.BALANCE` | `UsrsrsSweepParameter_TargetBalance` |  |  |  |
| 4 | `RSS.SWEEP.UPTO.BAL` | `UsrsrsSweepParameter_UptoBal` |  |  |  |
| 5 | `RSS.SWEEP.RESERVED.20` | `UsrsrsSweepParameter_Reserved20` |  |  |  |
| 6 | `RSS.SWEEP.RESERVED.19` | `UsrsrsSweepParameter_Reserved19` |  |  |  |
| 7 | `RSS.SWEEP.RESERVED.18` | `UsrsrsSweepParameter_Reserved18` |  |  |  |
| 8 | `RSS.SWEEP.RESERVED.17` | `UsrsrsSweepParameter_Reserved17` |  |  |  |
| 9 | `RSS.SWEEP.RESERVED.16` | `UsrsrsSweepParameter_Reserved16` |  |  |  |
| 10 | `RSS.SWEEP.TXN.ACCT.CAT` | `UsrsrsSweepParameter_TxnAcctCat` | TField | Yes | The unique CATEGORY code used for all AC accounts when creating the Transaction Sub-Account (Sub-Account 1) for an arrangement. Must be a CATEGORY code defined as Contingent category in ACCOUNT.PARAMETE Validation Rules Mandatory Field. Category range allowed should be less than 10000. Category should match the contingent category defined for Customer Accounts |
| 11 | `RSS.SWEEP.NONTXN.ACCT.CAT` | `UsrsrsSweepParameter_NontxnAcctCat` | TField | Yes | The unique CATEGORY code used for all AC accounts when creating the Non-Transaction Sub-Account (Sub-Account 2) for an arrangement. Must be a CATEGORY code defined as Contingent category in ACCOUNT.PARAMETER. Validation Rules Mandatory Field. Category range allowed should be less than 10000. Category should match the contingent category defined for Customer Accounts |
| 12 | `RSS.SWEEP.SETTLEMENT.ACCT` | `UsrsrsSweepParameter_SettlementAcct` | TField |  | Must be a valid INTERNAL ACCOUNT used as the offset entry for the Sub-Account 1. These entries are the "daily net activity" entries based upon the net daily transaction activity of the customer's primary account. The Category of the INTERNAL ACCOUNT defined must be a contingent category as defined in ACCOUNT.PARAMETER. Validation Rules Category range allowed should in the range 10000 to 19999. Category should fall within the the contingent category defined in ACCOUNT.PARAMETER. |
| 13 | `RSS.SWEEP.RES.REGD.VIO.COUNT` | `UsrsrsSweepParameter_ResRegdVioCount` | TField |  | The number of times funds can be moved from non-transaction account to transaction account, when the transaction account balance becomes negative. After reaching the count, there will be move further sweeps from transaction account to the non-transaction account for that month. Validation Rules |
| 14 | `RSS.SWEEP.RES.TXN.FTTC` | `UsrsrsSweepParameter_ResTxnFttc` | TField | Yes | Should be a valid FT.TXN.TYPE.CONDITION record. The record provided will be used as the transaction type for the sweeps done in transaction accounts and non-transaction accounts. Validation Rules Mandatory field. |
| 15 | `RSS.SWEEP.RESERVED.15` | `UsrsrsSweepParameter_Reserved15` | TField |  | Reserved for future use. Validation Rules |
| 16 | `RSS.SWEEP.RESERVED.14` | `UsrsrsSweepParameter_Reserved14` | TField |  | Reserved for future use. Validation Rules |
| 17 | `RSS.SWEEP.RESERVED.13` | `UsrsrsSweepParameter_Reserved13` | TField |  | Reserved for future use. Validation Rules |
| 18 | `RSS.SWEEP.RESERVED.12` | `UsrsrsSweepParameter_Reserved12` | TField |  | Reserved for future use. Validation Rules |
| 19 | `RSS.SWEEP.RESERVED.11` | `UsrsrsSweepParameter_Reserved11` | TField |  | Reserved for future use. Validation Rules |
| 20 | `RSS.SWEEP.RESERVED.10` | `UsrsrsSweepParameter_Reserved10` | TField |  | Reserved for future use. Validation Rules |
| 21 | `RSS.SWEEP.RESERVED.9` | `UsrsrsSweepParameter_Reserved9` | TField |  | Reserved for future use. Validation Rules |
| 22 | `RSS.SWEEP.RESERVED.8` | `UsrsrsSweepParameter_Reserved8` | TField |  | Reserved for future use. Validation Rules |
| 23 | `RSS.SWEEP.RESERVED.7` | `UsrsrsSweepParameter_Reserved7` | TField |  | Reserved for future use. Validation Rules |
| 24 | `RSS.SWEEP.RESERVED.6` | `UsrsrsSweepParameter_Reserved6` | TField |  | Reserved for future use. Validation Rules |
| 25 | `RSS.SWEEP.RESERVED.5` | `UsrsrsSweepParameter_Reserved5` | TField |  | Reserved for future use. Validation Rules |
| 26 | `RSS.SWEEP.RESERVED.4` | `UsrsrsSweepParameter_Reserved4` | TField |  | Reserved for future use. Validation Rules |
| 27 | `RSS.SWEEP.RESERVED.3` | `UsrsrsSweepParameter_Reserved3` | TField |  | Reserved for future use. Validation Rules |
| 28 | `RSS.SWEEP.RESERVED.2` | `UsrsrsSweepParameter_Reserved2` | TField |  | Reserved for future use. Validation Rules |
| 29 | `RSS.SWEEP.RESERVED.1` | `UsrsrsSweepParameter_Reserved1` | TField |  | Reserved for future use. Validation Rules |
| 30 | `RSS.SWEEP.LOCAL.REF` | `UsrsrsSweepParameter_LocalRef` |  |  |  |
| 31 | `RSS.SWEEP.OVERRIDE` | `UsrsrsSweepParameter_Override` |  |  |  |
| 32 | `RSS.SWEEP.RECORD.STATUS` | `UsrsrsSweepParameter_RecordStatus` | String |  |  |
| 33 | `RSS.SWEEP.CURR.NO` | `UsrsrsSweepParameter_CurrNo` | String |  |  |
| 34 | `RSS.SWEEP.INPUTTER` | `UsrsrsSweepParameter_Inputter` |  |  |  |
| 35 | `RSS.SWEEP.DATE.TIME` | `UsrsrsSweepParameter_DateTime` |  |  |  |
| 36 | `RSS.SWEEP.AUTHORISER` | `UsrsrsSweepParameter_Authoriser` | String |  |  |
| 37 | `RSS.SWEEP.CO.CODE` | `UsrsrsSweepParameter_CoCode` | String |  |  |
| 38 | `RSS.SWEEP.DEPT.CODE` | `UsrsrsSweepParameter_DeptCode` | String |  |  |
| 39 | `RSS.SWEEP.AUDITOR.CODE` | `UsrsrsSweepParameter_AuditorCode` | String |  |  |
| 40 | `RSS.SWEEP.AUDIT.DATE.TIME` | `UsrsrsSweepParameter_AuditDateTime` | String |  |  |
