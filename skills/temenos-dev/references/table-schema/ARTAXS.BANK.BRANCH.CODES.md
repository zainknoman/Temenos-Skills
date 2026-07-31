# ARTAXS.BANK.BRANCH.CODES — Table Schema

> Source: `INSERTS/I_F.ARTAXS.BANK.BRANCH.CODES` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BANK.BRANCH.JURISDICTION` | `ArtaxsBankBranchCodes_Jurisdiction` | TField |  | Jurisdiction - Jurisdiction code- EB.LOOKUP field attached to EB.LOOKUP>PROVINCE. |
| 2 | `BANK.BRANCH.BANK.CODE` | `ArtaxsBankBranchCodes_BankCode` | TField |  | Bank Code is a number with a maximum 3 digits corresponding to the bank code. |
| 3 | `BANK.BRANCH.BRANCH.CODE` | `ArtaxsBankBranchCodes_BranchCode` | TField |  | Branch Code is a number with a maximum 4 digits corresponding to the branch code. |
| 4 | `BANK.BRANCH.RESERVED.1` | `ArtaxsBankBranchCodes_Reserved1` | TField |  | Field for future use. |
| 5 | `BANK.BRANCH.RESERVED.2` | `ArtaxsBankBranchCodes_Reserved2` | TField |  | Field for future use. |
| 6 | `BANK.BRANCH.RESERVED.3` | `ArtaxsBankBranchCodes_Reserved3` | TField |  | Field for future use. |
| 7 | `BANK.BRANCH.RESERVED.4` | `ArtaxsBankBranchCodes_Reserved4` | TField |  | Field for future use. |
| 8 | `BANK.BRANCH.RESERVED.5` | `ArtaxsBankBranchCodes_Reserved5` | TField |  | Field for future use. |
| 9 | `BANK.BRANCH.RESERVED.6` | `ArtaxsBankBranchCodes_Reserved6` | TField |  | Field for future use. |
| 10 | `BANK.BRANCH.RESERVED.7` | `ArtaxsBankBranchCodes_Reserved7` | TField |  | Field for future use. |
| 11 | `BANK.BRANCH.RESERVED.8` | `ArtaxsBankBranchCodes_Reserved8` | TField |  | Field for future use. |
| 12 | `BANK.BRANCH.RESERVED.9` | `ArtaxsBankBranchCodes_Reserved9` | TField |  | Field for future use. |
| 13 | `BANK.BRANCH.RESERVED.10` | `ArtaxsBankBranchCodes_Reserved10` | TField |  | Field for future use. |
| 14 | `BANK.BRANCH.LOCAL.REF` | `ArtaxsBankBranchCodes_LocalRef` |  |  |  |
| 15 | `BANK.BRANCH.OVERRIDE` | `ArtaxsBankBranchCodes_Override` |  |  |  |
| 16 | `BANK.BRANCH.RECORD.STATUS` | `ArtaxsBankBranchCodes_RecordStatus` | String |  |  |
| 17 | `BANK.BRANCH.CURR.NO` | `ArtaxsBankBranchCodes_CurrNo` | String |  |  |
| 18 | `BANK.BRANCH.INPUTTER` | `ArtaxsBankBranchCodes_Inputter` |  |  |  |
| 19 | `BANK.BRANCH.DATE.TIME` | `ArtaxsBankBranchCodes_DateTime` |  |  |  |
| 20 | `BANK.BRANCH.AUTHORISER` | `ArtaxsBankBranchCodes_Authoriser` | String |  |  |
| 21 | `BANK.BRANCH.CO.CODE` | `ArtaxsBankBranchCodes_CoCode` | String |  |  |
| 22 | `BANK.BRANCH.DEPT.CODE` | `ArtaxsBankBranchCodes_DeptCode` | String |  |  |
| 23 | `BANK.BRANCH.AUDITOR.CODE` | `ArtaxsBankBranchCodes_AuditorCode` | String |  |  |
| 24 | `BANK.BRANCH.AUDIT.DATE.TIME` | `ArtaxsBankBranchCodes_AuditDateTime` | String |  |  |
