# FS.GA.CONVERTIBLE.BOND.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CONVERTIBLE.BOND.DETAIL` in `FS_SecurityMasterConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CONVERTIBLE.BOND.DETAIL.PARENT.REF.ID` | `FsGaConvertibleBondDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CONVERTIBLE.BOND.DETAIL.ORA.ROWID` | `FsGaConvertibleBondDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CONVERTIBLE.BOND.DETAIL.INTERNAL.SECURITY.ID` | `FsGaConvertibleBondDetail_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.PERIOD.FROM` | `FsGaConvertibleBondDetail_ConversionPeriodFrom` | TField |  | This field displays the start date of conversion period related to conversion information for convertible securities Multifonds DB Column is CONV_DATE_FROM. |
| 5 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.PERIOD.TO` | `FsGaConvertibleBondDetail_ConversionPeriodTo` | TField |  | This field displays the end date of conversion period related to conversion information for convertible securities Multifonds DB Column is CONV_DATE_TO. |
| 6 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.RATIO` | `FsGaConvertibleBondDetail_ConversionRatio` | TField |  | This field displays whether the source security is converted into a new security or into cash for convertible securities Multifonds DB Column is CONV_RATIO. |
| 7 | `FS.GA.CONVERTIBLE.BOND.DETAIL.NOMINAL.VALUE` | `FsGaConvertibleBondDetail_NominalValue` | TField |  | Nominal of the Instrument Multifonds DB Column is NOMINAL. |
| 8 | `FS.GA.CONVERTIBLE.BOND.DETAIL.UNITS` | `FsGaConvertibleBondDetail_Units` | TField |  | Units of convertibles Multifonds DB Column is UNITS. |
| 9 | `FS.GA.CONVERTIBLE.BOND.DETAIL.EQUITY` | `FsGaConvertibleBondDetail_Equity` | TField |  | This field displays the id of the stock if converted to stocks Multifonds DB Column is EQUITY. |
| 10 | `FS.GA.CONVERTIBLE.BOND.DETAIL.AMOUNT.OF.CASH` | `FsGaConvertibleBondDetail_AmountOfCash` | TField |  | This field displays the cash amount to be received in addition for convertible securities Multifonds DB Column is CASH_MNT. |
| 11 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CASH.AMOUNT.CURRENCY` | `FsGaConvertibleBondDetail_CashAmountCurrency` | TField |  | This field displays the currency of cash amount to be received for convertible securities Multifonds DB Column is CASH_CMON. |
| 12 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CASH.AMOUNT.EX.RATE` | `FsGaConvertibleBondDetail_CashAmountExRate` | TField |  | This field displays the exchange rate(if fixed in the terms and condition of conversion) of cash amount for convertible securities Multifonds DB Column is CASH_TCHG. |
| 13 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.PREMIUM` | `FsGaConvertibleBondDetail_ConversionPremium` | TField |  | This field displays the conversion premium to be paid for convertible securities Multifonds DB Column is PREMIUM_MNT. |
| 14 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.PREMIUM.CCY` | `FsGaConvertibleBondDetail_ConversionPremiumCcy` | TField |  | This field displays the currency of conversion premium to be paid for convertible securities Multifonds DB Column is PREMIUM_CMON. |
| 15 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CONVERSION.PREMIUM.EX.RATE` | `FsGaConvertibleBondDetail_ConversionPremiumExRate` | TField |  | This field displays the exchange rate of conversion premium to be paid for convertible securities Multifonds DB Column is PREMIUM_TCHG. |
| 16 | `FS.GA.CONVERTIBLE.BOND.DETAIL.DESCRIPTION` | `FsGaConvertibleBondDetail_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 17 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED10` | `FsGaConvertibleBondDetail_Reserved10` | TField |  |  |
| 18 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED9` | `FsGaConvertibleBondDetail_Reserved9` | TField |  |  |
| 19 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED8` | `FsGaConvertibleBondDetail_Reserved8` | TField |  |  |
| 20 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED7` | `FsGaConvertibleBondDetail_Reserved7` | TField |  |  |
| 21 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED6` | `FsGaConvertibleBondDetail_Reserved6` | TField |  |  |
| 22 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED5` | `FsGaConvertibleBondDetail_Reserved5` | TField |  |  |
| 23 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED4` | `FsGaConvertibleBondDetail_Reserved4` | TField |  |  |
| 24 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED3` | `FsGaConvertibleBondDetail_Reserved3` | TField |  |  |
| 25 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED2` | `FsGaConvertibleBondDetail_Reserved2` | TField |  |  |
| 26 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RESERVED1` | `FsGaConvertibleBondDetail_Reserved1` | TField |  |  |
| 27 | `FS.GA.CONVERTIBLE.BOND.DETAIL.LOCAL.REF` | `FsGaConvertibleBondDetail_LocalRef` |  |  |  |
| 28 | `FS.GA.CONVERTIBLE.BOND.DETAIL.OVERRIDE` | `FsGaConvertibleBondDetail_Override` |  |  |  |
| 29 | `FS.GA.CONVERTIBLE.BOND.DETAIL.RECORD.STATUS` | `FsGaConvertibleBondDetail_RecordStatus` | String |  |  |
| 30 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CURR.NO` | `FsGaConvertibleBondDetail_CurrNo` | String |  |  |
| 31 | `FS.GA.CONVERTIBLE.BOND.DETAIL.INPUTTER` | `FsGaConvertibleBondDetail_Inputter` |  |  |  |
| 32 | `FS.GA.CONVERTIBLE.BOND.DETAIL.DATE.TIME` | `FsGaConvertibleBondDetail_DateTime` |  |  |  |
| 33 | `FS.GA.CONVERTIBLE.BOND.DETAIL.AUTHORISER` | `FsGaConvertibleBondDetail_Authoriser` | String |  |  |
| 34 | `FS.GA.CONVERTIBLE.BOND.DETAIL.CO.CODE` | `FsGaConvertibleBondDetail_CoCode` | String |  |  |
| 35 | `FS.GA.CONVERTIBLE.BOND.DETAIL.DEPT.CODE` | `FsGaConvertibleBondDetail_DeptCode` | String |  |  |
| 36 | `FS.GA.CONVERTIBLE.BOND.DETAIL.AUDITOR.CODE` | `FsGaConvertibleBondDetail_AuditorCode` | String |  |  |
| 37 | `FS.GA.CONVERTIBLE.BOND.DETAIL.AUDIT.DATE.TIME` | `FsGaConvertibleBondDetail_AuditDateTime` | String |  |  |
