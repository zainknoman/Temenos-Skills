# FSCS.LOG.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FSCS.LOG.ACCOUNT` in `UKFSCS_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSCS.ACCOUNT.SCV.NUMBER` | `FscsLogAccount_ScvNumber` | TField |  | PRA Firm Registration Number (FRN) prefix followed by unique customer number. Example: 12345600001215 |
| 2 | `FSCS.ACCOUNT.ACCOUNT.NO` | `FscsLogAccount_AccountNo` | TField |  | Unique number for this account. Validation Rule: Valid @id from ACCOUNT table |
| 3 | `FSCS.ACCOUNT.CUSTOMER.NO` | `FscsLogAccount_CustomerNo` | TField |  | Customer number for this account Validation Rule: Valid @id from CUSTOMER table |
| 4 | `FSCS.ACCOUNT.REFERENCE` | `FscsLogAccount_Reference` | TField |  | Account or Contract ID Validation Rule: This files refers to the T24 account number or deposit contract Id. |
| 5 | `FSCS.ACCOUNT.PRODUCT` | `FscsLogAccount_Product` | TField |  | T24 product code of the account or contact Validation Rule: T24 product code |
| 6 | `FSCS.ACCOUNT.DATE.TIME` | `FscsLogAccount_DateTime` |  |  |  |
| 7 | `FSCS.ACCOUNT.EXCLUSION` | `FscsLogAccount_Exclusion` | TField |  | Exclusion File Validation Rule: 'Y' or 'N' |
| 8 | `FSCS.ACCOUNT.FFSTP` | `FscsLogAccount_Ffstp` | TField |  | Fit For Straight Through Payout Validation Rule: 'Y' or 'N' |
| 9 | `FSCS.ACCOUNT.AC.TITLE` | `FscsLogAccount_AcTitle` | TField |  | Surname or company name, first name, any other account initials or middle name identifier. |
| 10 | `FSCS.ACCOUNT.BIC` | `FscsLogAccount_Bic` | TField |  | Business Identifier Code for the customer [if applicable and where held by the firm] ISO 9362 |
| 11 | `FSCS.ACCOUNT.IBAN` | `FscsLogAccount_Iban` | TField |  | International Bank Account Number- IBAN account number for accounts, null for contracts. |
| 12 | `FSCS.ACCOUNT.SORT.CODE` | `FscsLogAccount_SortCode` | TField |  | Sort Code |
| 13 | `FSCS.ACCOUNT.PRODUCT.TYPE` | `FscsLogAccount_ProductType` | TField |  | Firms must allocate products to one of the following categories: Instant Access Accounts (including current accounts); ISAs; Notice accounts; Fixed term deposits with a term of less than one year; Fixed term deposits with a term of one year or more but less than two years; Fixed term deposits with a term of two years or more but less than four years; Fixed term deposits with a term of four years or more. |
| 14 | `FSCS.ACCOUNT.PRODUCT.NAME` | `FscsLogAccount_ProductName` | TField |  | Name of the product |
| 15 | `FSCS.ACCOUNT.AC.HOLDER.IND` | `FscsLogAccount_AcHolderInd` | TField |  | The number of beneficial owners of the account. For accounts with a single owner, the field must show 001. Foraccounts with two joint owners, the field must show 002, and so on. |
| 16 | `FSCS.ACCOUNT.AC.STATUS.CODE` | `FscsLogAccount_AcStatusCode` | TField |  | Code to identify whether the account is fit for straight-through processing (FFSTP) or not fit forstraight-through processing (NFFSTP). The code and its definition (of whether it signifies the account is FFSTP or NFFSTP) must be provided to FSCS inthe SCV effectiveness report. If an account holder has multiple accounts, and one is deemed NFFSTP, then all oftheir other accounts must be deemed NFFSTP. |
| 17 | `FSCS.ACCOUNT.EXCLUSION.TYPE` | `FscsLogAccount_ExclusionType` | TField |  | Identify all of the following which apply: The account contains or may contain eligible deposits to which the account holder is not absolutely entitled; The account is a dormant account; The account is an account for which the firm has received formal notice of a legal dispute or competing claims tothe proceeds of the account; The account appears on the 'Consolidated list of financial sanctions targets in the United Kingdom' that ismaintained by HM Treasury or is otherwise subject to restrictive measures imposed by national governments orinternational bodies |
| 18 | `FSCS.ACCOUNT.RECENT` | `FscsLogAccount_Recent` | TField |  | This field indictes whether there been any transaction relating to the deposit within the 24 months prior toproduction of the single customer view. Validation Rule: 'Y' or 'N' |
| 19 | `FSCS.ACCOUNT.AC.BRANCH.JURISDICTION` | `FscsLogAccount_AcBranchJurisdiction` | TField |  | If the account is held in a branch outside the United Kingdom, please state in which jurisdiction the account isheld. ISO 3166-1 Alpha-3. Validation Rule: 'GBR' or 'GIB' |
| 20 | `FSCS.ACCOUNT.BRRD.FLAG` | `FscsLogAccount_BrrdFlag` | TField |  | A firm must mark accounts which hold: eligible deposits from natural persons and micro, small and medium-sized enterprises; and deposits that would be eligible deposits from natural persons or micro, small and medium-sized enterprises if thedeposit had not been made through a branch of the firm located outside the EEA Validation Rule: 'Y' or 'N' |
| 21 | `FSCS.ACCOUNT.STR.DEPO.AC` | `FscsLogAccount_StrDepoAc` | TField |  | Whether or not the account is a structured deposit account where the account balance is calculated in accordancewith Depositor Protection Rule 12.11. Validation Rule: 'Y' or 'N' |
| 22 | `FSCS.ACCOUNT.AC.BAL.STERLING` | `FscsLogAccount_AcBalSterling` | TField |  | Account balance including any interest, at end of business on: the date on which the deposit becomes an unavailable deposit; or the date of request from FSCS or PRA as applicable. Do not include any non-numeric symbols such as commas or currency symbols (e.g. �). Where there is a negative balance, the amount should be preceded by a minus symbol (�-�). All balances must be rounded up to two decimal places. |
| 23 | `FSCS.ACCOUNT.AUTHORISED` | `FscsLogAccount_Authorised` | TField |  | The maximum negative balance on the account authorised by the firm, in sterling. Do not include any non-numeric symbols such as commas or currency symbols (e.g. �). All figures must be roundedup to two decimal places. If the account does not accept negative balances, please insert 0.00. If the maximumnegative balance authorised is e.g. �50, please insert 50.00, not -50.00. Maximum number of characters in field: 15 |
| 24 | `FSCS.ACCOUNT.CCY.AC` | `FscsLogAccount_CcyAc` | TField |  | Currency of Account |
| 25 | `FSCS.ACCOUNT.AC.BALANCE.ORG.CCY` | `FscsLogAccount_AcBalanceOrgCcy` | TField |  | Account Balance in Original Currency.Do not include any non-numeric symbols such as commas, currency symbols(e.g., �). All balances must be rounded up to two decimal places. Where there is a negative balance, the amountshould be preceded by a minus symbol (�-�). |
| 26 | `FSCS.ACCOUNT.EXCHANGE.RATE` | `FscsLogAccount_ExchangeRate` | TField |  | The exchange rate used to calculate the sterling balance. This must be the ratio of Sterling to the Currency ofthe account. |
| 27 | `FSCS.ACCOUNT.ORG.AC.BAL.BEFORE.INT` | `FscsLogAccount_OrgAcBalBeforeInt` | TField |  | Original Account Balance Before Interest. Do not include any non-numeric symbols such as commas, currency symbols(e.g. �). All balances must be rounded up to two decimal places. Where there is a negative balance, the amountshould be preceded by a minus symbol (�-�). |
| 28 | `FSCS.ACCOUNT.TRANS.ELIGIBLE.DEPO` | `FscsLogAccount_TransEligibleDepo` | TField |  | The portion of an eligible deposit up to and including the coverage level provided for in Depositor ProtectionRule 4.2, identified in accordance with Chapter 13 and Rule 12.9. |
| 29 | `FSCS.ACCOUNT.RESERVED.10` | `FscsLogAccount_Reserved10` | TField |  |  |
| 30 | `FSCS.ACCOUNT.RESERVED.9` | `FscsLogAccount_Reserved9` | TField |  |  |
| 31 | `FSCS.ACCOUNT.RESERVED.8` | `FscsLogAccount_Reserved8` | TField |  |  |
| 32 | `FSCS.ACCOUNT.RESERVED.7` | `FscsLogAccount_Reserved7` | TField |  |  |
| 33 | `FSCS.ACCOUNT.RESERVED.6` | `FscsLogAccount_Reserved6` | TField |  |  |
| 34 | `FSCS.ACCOUNT.RESERVED.5` | `FscsLogAccount_Reserved5` | TField |  |  |
| 35 | `FSCS.ACCOUNT.RESERVED.4` | `FscsLogAccount_Reserved4` | TField |  |  |
| 36 | `FSCS.ACCOUNT.RESERVED.3` | `FscsLogAccount_Reserved3` | TField |  |  |
| 37 | `FSCS.ACCOUNT.RESERVED.2` | `FscsLogAccount_Reserved2` | TField |  |  |
| 38 | `FSCS.ACCOUNT.RESERVED.1` | `FscsLogAccount_Reserved1` | TField |  |  |
