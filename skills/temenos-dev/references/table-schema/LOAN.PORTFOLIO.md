# LOAN.PORTFOLIO — Table Schema

> Source: `INSERTS/I_F.LOAN.PORTFOLIO` in `FL_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LPF.DESCRIPTION` | `LoanPortfolio_Description` |  |  |  |
| 2 | `LPF.STATUS` | `LoanPortfolio_Status` | TField |  | This field specifies whether the portfolio is active or not. Two allowed values are �Active� and �Inactive�. The portfolio can participate or fund a loan arrangement only if the portfolio is active. If the portfolio is inactive, the portfolio cannot be part of any new facilities. But the inactive portfolios can continue to be part of existing facilities and drawings. By default, the portfolio is active |
| 3 | `LPF.BRANCH` | `LoanPortfolio_Branch` | TField |  | This field Specifies the branch to which the portfolio/business unit belongs to. It should be a valid record from the COMPANY application. Once created, it cannot be modified. |
| 4 | `LPF.DEPARTMENT` | `LoanPortfolio_Department` | TField |  | This field specifies the department to which the portfolio/business unit belongs to. It should be a valid record from the DEPARTMENT.ACCOUNT.OFFICER (DAO) application. Once created, it cannot be modified. |
| 5 | `LPF.RESERVED5` | `LoanPortfolio_Reserved5` |  |  |  |
| 6 | `LPF.RESERVED6` | `LoanPortfolio_Reserved6` |  |  |  |
| 7 | `LPF.RESERVED7` | `LoanPortfolio_Reserved7` |  |  |  |
| 8 | `LPF.RESERVED8` | `LoanPortfolio_Reserved8` |  |  |  |
| 9 | `LPF.RESERVED9` | `LoanPortfolio_Reserved9` |  |  |  |
| 10 | `LPF.RESERVED10` | `LoanPortfolio_Reserved10` |  |  |  |
| 11 | `LPF.RESERVED11` | `LoanPortfolio_Reserved11` |  |  |  |
| 12 | `LPF.RESERVED12` | `LoanPortfolio_Reserved12` | TField |  |  |
| 13 | `LPF.RESERVED13` | `LoanPortfolio_Reserved13` | TField |  |  |
| 14 | `LPF.RESERVED14` | `LoanPortfolio_Reserved14` | TField |  |  |
| 15 | `LPF.RESERVED15` | `LoanPortfolio_Reserved15` | TField |  |  |
| 16 | `LPF.RESERVED16` | `LoanPortfolio_Reserved16` | TField |  |  |
| 17 | `LPF.RESERVED17` | `LoanPortfolio_Reserved17` | TField |  |  |
| 18 | `LPF.RESERVED18` | `LoanPortfolio_Reserved18` | TField |  |  |
| 19 | `LPF.RESERVED19` | `LoanPortfolio_Reserved19` | TField |  |  |
| 20 | `LPF.LOCAL.REF` | `LoanPortfolio_LocalRef` |  |  |  |
| 21 | `LPF.RECORD.STATUS` | `LoanPortfolio_RecordStatus` | String |  |  |
| 22 | `LPF.CURR.NO` | `LoanPortfolio_CurrNo` | String |  |  |
| 23 | `LPF.INPUTTER` | `LoanPortfolio_Inputter` |  |  |  |
| 24 | `LPF.DATE.TIME` | `LoanPortfolio_DateTime` |  |  |  |
| 25 | `LPF.AUTHORISER` | `LoanPortfolio_Authoriser` | String |  |  |
| 26 | `LPF.CO.CODE` | `LoanPortfolio_CoCode` | String |  |  |
| 27 | `LPF.DEPT.CODE` | `LoanPortfolio_DeptCode` | String |  |  |
| 28 | `LPF.AUDITOR.CODE` | `LoanPortfolio_AuditorCode` | String |  |  |
| 29 | `LPF.AUDIT.DATE.TIME` | `LoanPortfolio_AuditDateTime` | String |  |  |
