# FS.GA.TAX.DEFINITION.COUNTRY — Table Schema

> Source: `INSERTS/I_F.FS.GA.TAX.DEFINITION.COUNTRY` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TAX.DEFINITION.COUNTRY.FUND.ID` | `FsGaTaxDefinitionCountry_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.TAX.DEFINITION.COUNTRY.INTERNAL.SECURITY.ID` | `FsGaTaxDefinitionCountry_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 3 | `FS.GA.TAX.DEFINITION.COUNTRY.SHARE.CLASS.CODE` | `FsGaTaxDefinitionCountry_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 4 | `FS.GA.TAX.DEFINITION.COUNTRY.COUPON.ENTRY` | `FsGaTaxDefinitionCountry_CouponEntry` | TField |  | Coupon Entry Multifonds DB Column is NECRITUR_COUP. |
| 5 | `FS.GA.TAX.DEFINITION.COUNTRY.CURRENCY.CODE` | `FsGaTaxDefinitionCountry_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 6 | `FS.GA.TAX.DEFINITION.COUNTRY.TAX.DOMICILE` | `FsGaTaxDefinitionCountry_TaxDomicile` | TField |  | Shows the tax domicile of the securities Multifonds DB Column is CPAYS_TAX. |
| 7 | `FS.GA.TAX.DEFINITION.COUNTRY.TAX.SECURITY.TYPE` | `FsGaTaxDefinitionCountry_TaxSecurityType` | TField |  | Select the appropriate code which can be retrieved under 'TAX_SEC'. Allows to make an equivalence with the tax tables definition under Static data\Tax tables Multifonds DB Column is TAX_SEC_TYPE. |
| 8 | `FS.GA.TAX.DEFINITION.COUNTRY.TAX.REGIME` | `FsGaTaxDefinitionCountry_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 9 | `FS.GA.TAX.DEFINITION.COUNTRY.ENTITLEMENT.DATE` | `FsGaTaxDefinitionCountry_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 10 | `FS.GA.TAX.DEFINITION.COUNTRY.UNREC.TAX.IN.PERCENT.TYPE.1` | `FsGaTaxDefinitionCountry_UnrecTaxInPercentType1` | TField |  | Unrecoverable tax percentage on Income , type 1 Multifonds DB Column is PUNRECTAX. |
| 11 | `FS.GA.TAX.DEFINITION.COUNTRY.UNRECOVERABLE.TAX.PERCENT.2` | `FsGaTaxDefinitionCountry_UnrecoverableTaxPercent2` | TField |  | Unrecoverable tax percentage on Income , type 2 Multifonds DB Column is PUNRECTAX_2. |
| 12 | `FS.GA.TAX.DEFINITION.COUNTRY.REC.TAX.IN.PERCENT.TYPE.1` | `FsGaTaxDefinitionCountry_RecTaxInPercentType1` | TField |  | Recoverable tax percentage on Income , type 1 Multifonds DB Column is PRECTAX. |
| 13 | `FS.GA.TAX.DEFINITION.COUNTRY.RECOVERABLE.TAX.PERCENT.2` | `FsGaTaxDefinitionCountry_RecoverableTaxPercent2` | TField |  | Recoverable tax percentage on Income , type 2 Multifonds DB Column is PRECTAX_2. |
| 14 | `FS.GA.TAX.DEFINITION.COUNTRY.SECURITY.LENDING.TAX` | `FsGaTaxDefinitionCountry_SecurityLendingTax` | TField |  | corresponds to the security tax at coupon level Multifonds DB Column is SEC_LEN_TAX. |
| 15 | `FS.GA.TAX.DEFINITION.COUNTRY.TAX.BASIS` | `FsGaTaxDefinitionCountry_TaxBasis` | TField |  | Tax Basis Multifonds DB Column is TAX_BASIS. |
| 16 | `FS.GA.TAX.DEFINITION.COUNTRY.SETTLE.DATE` | `FsGaTaxDefinitionCountry_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 17 | `FS.GA.TAX.DEFINITION.COUNTRY.DATE.OF.ENTITLEMENT` | `FsGaTaxDefinitionCountry_DateOfEntitlement` | TField |  | Date Of Entitlement Multifonds DB Column is DENTITL. |
| 18 | `FS.GA.TAX.DEFINITION.COUNTRY.EX.DATE` | `FsGaTaxDefinitionCountry_ExDate` | TField |  |  |
| 19 | `FS.GA.TAX.DEFINITION.COUNTRY.BOND.MARKET.TYPE` | `FsGaTaxDefinitionCountry_BondMarketType` | TField |  | Bond Market Type Multifonds DB Column is BOND_MARKET_TYPE. |
| 20 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED10` | `FsGaTaxDefinitionCountry_Reserved10` | TField |  |  |
| 21 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED9` | `FsGaTaxDefinitionCountry_Reserved9` | TField |  |  |
| 22 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED8` | `FsGaTaxDefinitionCountry_Reserved8` | TField |  |  |
| 23 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED7` | `FsGaTaxDefinitionCountry_Reserved7` | TField |  |  |
| 24 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED6` | `FsGaTaxDefinitionCountry_Reserved6` | TField |  |  |
| 25 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED5` | `FsGaTaxDefinitionCountry_Reserved5` | TField |  |  |
| 26 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED4` | `FsGaTaxDefinitionCountry_Reserved4` | TField |  |  |
| 27 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED3` | `FsGaTaxDefinitionCountry_Reserved3` | TField |  |  |
| 28 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED2` | `FsGaTaxDefinitionCountry_Reserved2` | TField |  |  |
| 29 | `FS.GA.TAX.DEFINITION.COUNTRY.RESERVED1` | `FsGaTaxDefinitionCountry_Reserved1` | TField |  |  |
| 30 | `FS.GA.TAX.DEFINITION.COUNTRY.RECORD.STATUS` | `FsGaTaxDefinitionCountry_RecordStatus` | String |  |  |
| 31 | `FS.GA.TAX.DEFINITION.COUNTRY.CURR.NO` | `FsGaTaxDefinitionCountry_CurrNo` | String |  |  |
| 32 | `FS.GA.TAX.DEFINITION.COUNTRY.INPUTTER` | `FsGaTaxDefinitionCountry_Inputter` |  |  |  |
| 33 | `FS.GA.TAX.DEFINITION.COUNTRY.DATE.TIME` | `FsGaTaxDefinitionCountry_DateTime` |  |  |  |
| 34 | `FS.GA.TAX.DEFINITION.COUNTRY.AUTHORISER` | `FsGaTaxDefinitionCountry_Authoriser` | String |  |  |
| 35 | `FS.GA.TAX.DEFINITION.COUNTRY.CO.CODE` | `FsGaTaxDefinitionCountry_CoCode` | String |  |  |
| 36 | `FS.GA.TAX.DEFINITION.COUNTRY.DEPT.CODE` | `FsGaTaxDefinitionCountry_DeptCode` | String |  |  |
| 37 | `FS.GA.TAX.DEFINITION.COUNTRY.AUDITOR.CODE` | `FsGaTaxDefinitionCountry_AuditorCode` | String |  |  |
| 38 | `FS.GA.TAX.DEFINITION.COUNTRY.AUDIT.DATE.TIME` | `FsGaTaxDefinitionCountry_AuditDateTime` | String |  |  |
