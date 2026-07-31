# TNCUIN.GARNISHMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.TNCUIN.GARNISHMENT.PARAM` in `TNCUIN_Garnishment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.GARNISH.PARAM.CCY.PRIORITY` | `TncuinGarnishmentParam_CcyPriority` |  |  |  |
| 2 | `TNCUIN.GARNISH.PARAM.CUSTOMER.ROLE` | `TncuinGarnishmentParam_CustomerRole` |  |  |  |
| 3 | `TNCUIN.GARNISH.PARAM.EXCLUDE.PRODUCT` | `TncuinGarnishmentParam_ExcludeProduct` |  |  |  |
| 4 | `TNCUIN.GARNISH.PARAM.EXCLUDE.STATUS` | `TncuinGarnishmentParam_ExcludeStatus` |  |  |  |
| 5 | `TNCUIN.GARNISH.PARAM.INTERNAL.CATEG` | `TncuinGarnishmentParam_InternalCateg` | TField |  | This field is to store the Category which has to be considered for creating internal account to transfer the funds from the customer account when the judgement is to pay to the creditor.Vetted with CATEGORY application |
| 6 | `TNCUIN.GARNISH.PARAM.CURRENCY.MARKET` | `TncuinGarnishmentParam_CurrencyMarket` | TField |  | This field is to store currency market value for currency exchange from garnish currency to account currency |
| 7 | `TNCUIN.GARNISH.PARAM.LOCK.CREATE.STATUS` | `TncuinGarnishmentParam_LockCreateStatus` | TField |  | This field stores the status of the Garnishment order on which the lock for funds has to be created |
| 8 | `TNCUIN.GARNISH.PARAM.LOCK.RELEASE.STATUS` | `TncuinGarnishmentParam_LockReleaseStatus` |  |  |  |
| 9 | `TNCUIN.GARNISH.PARAM.LOCK.TRANSFER.STATUS` | `TncuinGarnishmentParam_LockTransferStatus` | TField |  | This field stores the status on when the funds from the Locked account has to be transferred to the internal account |
| 10 | `TNCUIN.GARNISH.PARAM.LOCAL.REF` | `TncuinGarnishmentParam_LocalRef` |  |  |  |
| 11 | `TNCUIN.GARNISH.PARAM.SECURITY.CUST.ROLE` | `TncuinGarnishmentParam_SecurityCustRole` |  |  |  |
| 12 | `TNCUIN.GARNISH.PARAM.SECURITY.PRIORITY` | `TncuinGarnishmentParam_SecurityPriority` | TField |  | To configure Bond or Share. As SECURITY.MASTER>BOND.OR.SHARE |
| 13 | `TNCUIN.GARNISH.PARAM.EXCLUDE.REPORT.TYPE` | `TncuinGarnishmentParam_ExcludeReportType` | TField |  | It is vetted against the EB.LOOKUP for the fieldREPORT.TYPE. The report type configured here willnot be considered for freezing of securities. |
| 14 | `TNCUIN.GARNISH.PARAM.POSTING.RESTRICTION.TYPE` | `TncuinGarnishmentParam_PostingRestrictionType` | TField |  | This field stores the status on when the postingrestriction to be applied for the customer |
| 15 | `TNCUIN.GARNISH.PARAM.POSTING.RESTRICTION` | `TncuinGarnishmentParam_PostingRestriction` | TField |  | This field stores the type of Posting Restriction whichhas to be applied for the customer. This is vettedagainst the POSTING.RESTRICT table. |
| 16 | `TNCUIN.GARNISH.PARAM.OVERRIDE` | `TncuinGarnishmentParam_Override` |  |  |  |
| 17 | `TNCUIN.GARNISH.PARAM.RECORD.STATUS` | `TncuinGarnishmentParam_RecordStatus` | String |  |  |
| 18 | `TNCUIN.GARNISH.PARAM.CURR.NO` | `TncuinGarnishmentParam_CurrNo` | String |  |  |
| 19 | `TNCUIN.GARNISH.PARAM.INPUTTER` | `TncuinGarnishmentParam_Inputter` |  |  |  |
| 20 | `TNCUIN.GARNISH.PARAM.DATE.TIME` | `TncuinGarnishmentParam_DateTime` |  |  |  |
| 21 | `TNCUIN.GARNISH.PARAM.AUTHORISER` | `TncuinGarnishmentParam_Authoriser` | String |  |  |
| 22 | `TNCUIN.GARNISH.PARAM.CO.CODE` | `TncuinGarnishmentParam_CoCode` | String |  |  |
| 23 | `TNCUIN.GARNISH.PARAM.DEPT.CODE` | `TncuinGarnishmentParam_DeptCode` | String |  |  |
| 24 | `TNCUIN.GARNISH.PARAM.AUDITOR.CODE` | `TncuinGarnishmentParam_AuditorCode` | String |  |  |
| 25 | `TNCUIN.GARNISH.PARAM.AUDIT.DATE.TIME` | `TncuinGarnishmentParam_AuditDateTime` | String |  |  |
| 26 | `TNCUIN.GARNISH.PARAM.RESTRICT.RELEASE.STATUS` | `TncuinGarnishmentParam_RestrictReleaseStatus` | TField |  | This field stores the status on when the postingrestriction to be released for the customer |
| 27 | `TNCUIN.GARNISH.PARAM.EXCLUDE.SURVEILLANCE` | `TncuinGarnishmentParam_ExcludeSurveillance` |  |  |  |
| 28 | `TNCUIN.GARNISH.PARAM.CHQ.BILL.TXN.CODES` | `TncuinGarnishmentParam_ChqBillTxnCodes` |  |  |  |
