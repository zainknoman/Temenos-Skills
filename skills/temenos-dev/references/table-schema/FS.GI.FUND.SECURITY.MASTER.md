# FS.GI.FUND.SECURITY.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SECURITY.MASTER` in `FS_FundShareClassStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SECURITY.MASTER.PARENT.REF.ID` | `FsGiFundSecurityMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SECURITY.MASTER.ORA.ROWID` | `FsGiFundSecurityMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SECURITY.MASTER.SECURITY.ID` | `FsGiFundSecurityMaster_SecurityId` | TField |  | Security internal Id. Multifonds DB Column is NOVAL. |
| 4 | `FS.GI.FUND.SECURITY.MASTER.NAME` | `FsGiFundSecurityMaster_Name` | TField |  | Name of the security. Multifonds DB Column is NOMVAL. |
| 5 | `FS.GI.FUND.SECURITY.MASTER.SHORT.NAME` | `FsGiFundSecurityMaster_ShortName` | TField |  | Short Name of the Security. Multifonds DB Column is ABREGE. |
| 6 | `FS.GI.FUND.SECURITY.MASTER.ENTITY.STATUS` | `FsGiFundSecurityMaster_EntityStatus` | TField |  | Entity status. Multifonds DB Column is ACTIF. |
| 7 | `FS.GI.FUND.SECURITY.MASTER.CUSIP` | `FsGiFundSecurityMaster_Cusip` | TField |  | CUSIP is a nine-digit numeric or nine-character alphanumeric code for the purposes of facilitating clearing and settlement of trades. Multifonds DB Column is CUSIP. |
| 8 | `FS.GI.FUND.SECURITY.MASTER.NSCC.FLAG` | `FsGiFundSecurityMaster_NsccFlag` | TField |  | Flag allows to enable to link the security to a CUSIP. Multifonds DB Column is FLG_NSCC. |
| 9 | `FS.GI.FUND.SECURITY.MASTER.REPORTING.CODE` | `FsGiFundSecurityMaster_ReportingCode` | TField |  | The Reporting Code of the security which are used for the performance fees and Series of shares modules. Multifonds DB Column is CODE_RAPPORT. |
| 10 | `FS.GI.FUND.SECURITY.MASTER.HURDLE.RATE` | `FsGiFundSecurityMaster_HurdleRate` | TField |  | Hurdle rate. Multifonds DB Column is HURDLE_RATE. |
| 11 | `FS.GI.FUND.SECURITY.MASTER.HURDLE.FOR.SERIES.FLAG` | `FsGiFundSecurityMaster_HurdleForSeriesFlag` | TField |  | Hurdle for series flag. Multifonds DB Column is FLG_HURDLE. |
| 12 | `FS.GI.FUND.SECURITY.MASTER.CALCULATION.TYPE` | `FsGiFundSecurityMaster_CalculationType` | TField |  | Security Calculation type. Multifonds DB Column is CCALCUL. |
| 13 | `FS.GI.FUND.SECURITY.MASTER.TYPE` | `FsGiFundSecurityMaster_Type` | TField |  | Security Type ID code. Multifonds DB Column is CGTI. |
| 14 | `FS.GI.FUND.SECURITY.MASTER.LOCAL.TYPE` | `FsGiFundSecurityMaster_LocalType` | TField |  | Local Type Code which are used to generate statutory reports as required by the authorities. Multifonds DB Column is COTLOCALE. |
| 15 | `FS.GI.FUND.SECURITY.MASTER.QUOTATION.PLACE.CODE` | `FsGiFundSecurityMaster_QuotationPlaceCode` | TField |  | The stock exchange from which a market price of the security is required. Multifonds DB Column is CPLACE. |
| 16 | `FS.GI.FUND.SECURITY.MASTER.FEES.CODE` | `FsGiFundSecurityMaster_FeesCode` | TField |  | Fee code which allows the user to exclude / Include certain securities for accrued expenses calculation. Multifonds DB Column is FFEES. |
| 17 | `FS.GI.FUND.SECURITY.MASTER.ISSUER.EXTERNAL.ID` | `FsGiFundSecurityMaster_IssuerExternalId` | TField |  | The External ID of the Issuer. The issuer is mainly used for compliance purposes. Issuers needs to be defined in the central register list. Multifonds DB Column is NISSUING. |
| 18 | `FS.GI.FUND.SECURITY.MASTER.BRANCH.CODE` | `FsGiFundSecurityMaster_BranchCode` | TField |  | Branch Ccode applicable to the security. Multifonds DB Column is SCO. |
| 19 | `FS.GI.FUND.SECURITY.MASTER.INCOME.TYPE` | `FsGiFundSecurityMaster_IncomeType` | TField |  | Income type for the security. Multifonds DB Column is TREVENU. |
| 20 | `FS.GI.FUND.SECURITY.MASTER.ISIN.COUNTRY.CODE` | `FsGiFundSecurityMaster_IsinCountryCode` | TField |  | Two letter word country code allocated to the secruity where fund is domiciled by the International Organization for Standardization (ISO). Multifonds DB Column is CODISIN. |
| 21 | `FS.GI.FUND.SECURITY.MASTER.ISIN.IDENTIFIER` | `FsGiFundSecurityMaster_IsinIdentifier` | TField |  | Identifier of the security. With combination of ISIN Country code, it will derive the ISIN code. Multifonds DB Column is SEQISIN. |
| 22 | `FS.GI.FUND.SECURITY.MASTER.CURRENCY` | `FsGiFundSecurityMaster_Currency` | TField |  | Currency of the security. Multifonds DB Column is CMONCOTA. |
| 23 | `FS.GI.FUND.SECURITY.MASTER.DOMICILE` | `FsGiFundSecurityMaster_Domicile` | TField |  | Country of the security Multifonds DB Column is CPAYSVAL. |
| 24 | `FS.GI.FUND.SECURITY.MASTER.INTEREST.CALC.TYPE` | `FsGiFundSecurityMaster_InterestCalcType` | TField |  | Interest calcuation type of the security. Multifonds DB Column is CUSANCE. |
| 25 | `FS.GI.FUND.SECURITY.MASTER.DEPOSITARY.BANK.ID` | `FsGiFundSecurityMaster_DepositaryBankId` | TField |  | Depository bank identification. Multifonds DB Column is NRACINE. |
| 26 | `FS.GI.FUND.SECURITY.MASTER.SEDOL` | `FsGiFundSecurityMaster_Sedol` | TField |  | Sedol Identifier Multifonds DB Column is SEDOL. |
| 27 | `FS.GI.FUND.SECURITY.MASTER.ONE.ISIN.FLAG` | `FsGiFundSecurityMaster_OneIsinFlag` | TField |  | One ISIN flag. Multifonds DB Column is FLG_ONE_ISIN. |
| 28 | `FS.GI.FUND.SECURITY.MASTER.ISSUE.CAPITAL` | `FsGiFundSecurityMaster_IssueCapital` | TField |  | Issue capital. Multifonds DB Column is CAPITAL_EMISSION. |
| 29 | `FS.GI.FUND.SECURITY.MASTER.RESERVED10` | `FsGiFundSecurityMaster_Reserved10` | TField |  |  |
| 30 | `FS.GI.FUND.SECURITY.MASTER.RESERVED9` | `FsGiFundSecurityMaster_Reserved9` | TField |  |  |
| 31 | `FS.GI.FUND.SECURITY.MASTER.RESERVED8` | `FsGiFundSecurityMaster_Reserved8` | TField |  |  |
| 32 | `FS.GI.FUND.SECURITY.MASTER.RESERVED7` | `FsGiFundSecurityMaster_Reserved7` | TField |  |  |
| 33 | `FS.GI.FUND.SECURITY.MASTER.RESERVED6` | `FsGiFundSecurityMaster_Reserved6` | TField |  |  |
| 34 | `FS.GI.FUND.SECURITY.MASTER.RESERVED5` | `FsGiFundSecurityMaster_Reserved5` | TField |  |  |
| 35 | `FS.GI.FUND.SECURITY.MASTER.RESERVED4` | `FsGiFundSecurityMaster_Reserved4` | TField |  |  |
| 36 | `FS.GI.FUND.SECURITY.MASTER.RESERVED3` | `FsGiFundSecurityMaster_Reserved3` | TField |  |  |
| 37 | `FS.GI.FUND.SECURITY.MASTER.RESERVED2` | `FsGiFundSecurityMaster_Reserved2` | TField |  |  |
| 38 | `FS.GI.FUND.SECURITY.MASTER.RESERVED1` | `FsGiFundSecurityMaster_Reserved1` | TField |  |  |
| 39 | `FS.GI.FUND.SECURITY.MASTER.LOCAL.REF` | `FsGiFundSecurityMaster_LocalRef` |  |  |  |
| 40 | `FS.GI.FUND.SECURITY.MASTER.OVERRIDE` | `FsGiFundSecurityMaster_Override` |  |  |  |
| 41 | `FS.GI.FUND.SECURITY.MASTER.RECORD.STATUS` | `FsGiFundSecurityMaster_RecordStatus` | String |  |  |
| 42 | `FS.GI.FUND.SECURITY.MASTER.CURR.NO` | `FsGiFundSecurityMaster_CurrNo` | String |  |  |
| 43 | `FS.GI.FUND.SECURITY.MASTER.INPUTTER` | `FsGiFundSecurityMaster_Inputter` |  |  |  |
| 44 | `FS.GI.FUND.SECURITY.MASTER.DATE.TIME` | `FsGiFundSecurityMaster_DateTime` |  |  |  |
| 45 | `FS.GI.FUND.SECURITY.MASTER.AUTHORISER` | `FsGiFundSecurityMaster_Authoriser` | String |  |  |
| 46 | `FS.GI.FUND.SECURITY.MASTER.CO.CODE` | `FsGiFundSecurityMaster_CoCode` | String |  |  |
| 47 | `FS.GI.FUND.SECURITY.MASTER.DEPT.CODE` | `FsGiFundSecurityMaster_DeptCode` | String |  |  |
| 48 | `FS.GI.FUND.SECURITY.MASTER.AUDITOR.CODE` | `FsGiFundSecurityMaster_AuditorCode` | String |  |  |
| 49 | `FS.GI.FUND.SECURITY.MASTER.AUDIT.DATE.TIME` | `FsGiFundSecurityMaster_AuditDateTime` | String |  |  |
