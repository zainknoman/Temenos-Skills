# FS.GA.NAV.CURRENCY — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CURRENCY` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CURRENCY.PARENT.REF.ID` | `FsGaNavCurrency_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CURRENCY.ORA.ROWID` | `FsGaNavCurrency_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CURRENCY.FUND.ID` | `FsGaNavCurrency_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.CURRENCY.SHARE.CLASS.CODE` | `FsGaNavCurrency_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.1` | `FsGaNavCurrency_NavCurrency1` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_1. |
| 6 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.2` | `FsGaNavCurrency_NavCurrency2` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_2. |
| 7 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.3` | `FsGaNavCurrency_NavCurrency3` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_3. |
| 8 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.4` | `FsGaNavCurrency_NavCurrency4` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_4. |
| 9 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.5` | `FsGaNavCurrency_NavCurrency5` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_5. |
| 10 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.6` | `FsGaNavCurrency_NavCurrency6` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_6. |
| 11 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.7` | `FsGaNavCurrency_NavCurrency7` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_7. |
| 12 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.8` | `FsGaNavCurrency_NavCurrency8` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_8. |
| 13 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.9` | `FsGaNavCurrency_NavCurrency9` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_9. |
| 14 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY.10` | `FsGaNavCurrency_NavCurrency10` | TField |  | NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CMON_10. |
| 15 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.1` | `FsGaNavCurrency_DecimalPlacesNavCurrency1` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_1. |
| 16 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.2` | `FsGaNavCurrency_DecimalPlacesNavCurrency2` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_2. |
| 17 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.3` | `FsGaNavCurrency_DecimalPlacesNavCurrency3` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_3. |
| 18 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.4` | `FsGaNavCurrency_DecimalPlacesNavCurrency4` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_4. |
| 19 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.5` | `FsGaNavCurrency_DecimalPlacesNavCurrency5` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_5. |
| 20 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.6` | `FsGaNavCurrency_DecimalPlacesNavCurrency6` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_6. |
| 21 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.7` | `FsGaNavCurrency_DecimalPlacesNavCurrency7` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_7. |
| 22 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.8` | `FsGaNavCurrency_DecimalPlacesNavCurrency8` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_8. |
| 23 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.9` | `FsGaNavCurrency_DecimalPlacesNavCurrency9` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_9. |
| 24 | `FS.GA.NAV.CURRENCY.DECIMAL.PLACES.NAV.CURRENCY.10` | `FsGaNavCurrency_DecimalPlacesNavCurrency10` | TField |  | NAV currency decimal places for that NAV currency based on Security Id, Country etc for a share type Multifonds DB Column is CDEC_10. |
| 25 | `FS.GA.NAV.CURRENCY.CC.CURRENCY` | `FsGaNavCurrency_CcCurrency` | TField |  | CC CMON Multifonds DB Column is CC_CMON. |
| 26 | `FS.GA.NAV.CURRENCY.CC.DECIMAL.CODE` | `FsGaNavCurrency_CcDecimalCode` | TField |  | CC Decimal Code Multifonds DB Column is CC_CDEC. |
| 27 | `FS.GA.NAV.CURRENCY.CURRENCY.NUMBER` | `FsGaNavCurrency_CurrencyNumber` | TField |  | CMON NO Multifonds DB Column is CMON_NO. |
| 28 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.1` | `FsGaNavCurrency_SecurityIdNavCurrency1` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_1. |
| 29 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.2` | `FsGaNavCurrency_SecurityIdNavCurrency2` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_2. |
| 30 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.3` | `FsGaNavCurrency_SecurityIdNavCurrency3` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_3. |
| 31 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.4` | `FsGaNavCurrency_SecurityIdNavCurrency4` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_4. |
| 32 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.5` | `FsGaNavCurrency_SecurityIdNavCurrency5` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_5. |
| 33 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.6` | `FsGaNavCurrency_SecurityIdNavCurrency6` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_6. |
| 34 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.7` | `FsGaNavCurrency_SecurityIdNavCurrency7` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_7. |
| 35 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.8` | `FsGaNavCurrency_SecurityIdNavCurrency8` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_8. |
| 36 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.9` | `FsGaNavCurrency_SecurityIdNavCurrency9` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_9. |
| 37 | `FS.GA.NAV.CURRENCY.SECURITY.ID.NAV.CURRENCY.10` | `FsGaNavCurrency_SecurityIdNavCurrency10` | TField |  | Security Id for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is NOVAL_10. |
| 38 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.1` | `FsGaNavCurrency_FxGroupNavCurrency1` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_1. |
| 39 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.2` | `FsGaNavCurrency_FxGroupNavCurrency2` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_2. |
| 40 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.3` | `FsGaNavCurrency_FxGroupNavCurrency3` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_3. |
| 41 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.4` | `FsGaNavCurrency_FxGroupNavCurrency4` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_4. |
| 42 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.5` | `FsGaNavCurrency_FxGroupNavCurrency5` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_5. |
| 43 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.6` | `FsGaNavCurrency_FxGroupNavCurrency6` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_6. |
| 44 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.7` | `FsGaNavCurrency_FxGroupNavCurrency7` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_7. |
| 45 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.8` | `FsGaNavCurrency_FxGroupNavCurrency8` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_8. |
| 46 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.9` | `FsGaNavCurrency_FxGroupNavCurrency9` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_9. |
| 47 | `FS.GA.NAV.CURRENCY.FX.GROUP.NAV.CURRENCY.10` | `FsGaNavCurrency_FxGroupNavCurrency10` | TField |  | FX group for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is FX_GROUP_10. |
| 48 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.1` | `FsGaNavCurrency_CountryCodeNavCurrency1` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_1. |
| 49 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.2` | `FsGaNavCurrency_CountryCodeNavCurrency2` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_2. |
| 50 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.3` | `FsGaNavCurrency_CountryCodeNavCurrency3` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_3. |
| 51 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.4` | `FsGaNavCurrency_CountryCodeNavCurrency4` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_4. |
| 52 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.5` | `FsGaNavCurrency_CountryCodeNavCurrency5` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_5. |
| 53 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.6` | `FsGaNavCurrency_CountryCodeNavCurrency6` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_6. |
| 54 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.7` | `FsGaNavCurrency_CountryCodeNavCurrency7` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_7. |
| 55 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.8` | `FsGaNavCurrency_CountryCodeNavCurrency8` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_8. |
| 56 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.9` | `FsGaNavCurrency_CountryCodeNavCurrency9` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_9. |
| 57 | `FS.GA.NAV.CURRENCY.COUNTRY.CODE.NAV.CURRENCY.10` | `FsGaNavCurrency_CountryCodeNavCurrency10` | TField |  | Country Code for which NAV currency is specified based on Security Id, Country etc for a share type Multifonds DB Column is CPAYSVAL_10. |
| 58 | `FS.GA.NAV.CURRENCY.NAV.ROUNDING.METHOD` | `FsGaNavCurrency_NavRoundingMethod` | TField |  | Displays the method code used for rounding the NAV Price (at share class level). Multifonds DB Column is CDEC_ARR_NAV. |
| 59 | `FS.GA.NAV.CURRENCY.NAV.CURRENCY` | `FsGaNavCurrency_NavCurrency` | TField |  | This field displays the share class currency to be used in FDACT04. If box is ticked then the corresponding CCY will be used in FDACT04 as the reference CCY of the share class. Multifonds DB Column is FLG_NAV_CCY. |
| 60 | `FS.GA.NAV.CURRENCY.RESERVED10` | `FsGaNavCurrency_Reserved10` | TField |  |  |
| 61 | `FS.GA.NAV.CURRENCY.RESERVED9` | `FsGaNavCurrency_Reserved9` | TField |  |  |
| 62 | `FS.GA.NAV.CURRENCY.RESERVED8` | `FsGaNavCurrency_Reserved8` | TField |  |  |
| 63 | `FS.GA.NAV.CURRENCY.RESERVED7` | `FsGaNavCurrency_Reserved7` | TField |  |  |
| 64 | `FS.GA.NAV.CURRENCY.RESERVED6` | `FsGaNavCurrency_Reserved6` | TField |  |  |
| 65 | `FS.GA.NAV.CURRENCY.RESERVED5` | `FsGaNavCurrency_Reserved5` | TField |  |  |
| 66 | `FS.GA.NAV.CURRENCY.RESERVED4` | `FsGaNavCurrency_Reserved4` | TField |  |  |
| 67 | `FS.GA.NAV.CURRENCY.RESERVED3` | `FsGaNavCurrency_Reserved3` | TField |  |  |
| 68 | `FS.GA.NAV.CURRENCY.RESERVED2` | `FsGaNavCurrency_Reserved2` | TField |  |  |
| 69 | `FS.GA.NAV.CURRENCY.RESERVED1` | `FsGaNavCurrency_Reserved1` | TField |  |  |
| 70 | `FS.GA.NAV.CURRENCY.LOCAL.REF` | `FsGaNavCurrency_LocalRef` |  |  |  |
| 71 | `FS.GA.NAV.CURRENCY.OVERRIDE` | `FsGaNavCurrency_Override` |  |  |  |
| 72 | `FS.GA.NAV.CURRENCY.RECORD.STATUS` | `FsGaNavCurrency_RecordStatus` | String |  |  |
| 73 | `FS.GA.NAV.CURRENCY.CURR.NO` | `FsGaNavCurrency_CurrNo` | String |  |  |
| 74 | `FS.GA.NAV.CURRENCY.INPUTTER` | `FsGaNavCurrency_Inputter` |  |  |  |
| 75 | `FS.GA.NAV.CURRENCY.DATE.TIME` | `FsGaNavCurrency_DateTime` |  |  |  |
| 76 | `FS.GA.NAV.CURRENCY.AUTHORISER` | `FsGaNavCurrency_Authoriser` | String |  |  |
| 77 | `FS.GA.NAV.CURRENCY.CO.CODE` | `FsGaNavCurrency_CoCode` | String |  |  |
| 78 | `FS.GA.NAV.CURRENCY.DEPT.CODE` | `FsGaNavCurrency_DeptCode` | String |  |  |
| 79 | `FS.GA.NAV.CURRENCY.AUDITOR.CODE` | `FsGaNavCurrency_AuditorCode` | String |  |  |
| 80 | `FS.GA.NAV.CURRENCY.AUDIT.DATE.TIME` | `FsGaNavCurrency_AuditDateTime` | String |  |  |
