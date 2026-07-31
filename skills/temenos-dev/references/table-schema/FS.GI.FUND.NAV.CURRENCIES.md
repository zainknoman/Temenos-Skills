# FS.GI.FUND.NAV.CURRENCIES — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.NAV.CURRENCIES` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.NAV.CURRENCIES.PARENT.REF.ID` | `FsGiFundNavCurrencies_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.NAV.CURRENCIES.ORA.ROWID` | `FsGiFundNavCurrencies_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.NAV.CURRENCIES.FUND.ID` | `FsGiFundNavCurrencies_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.NAV.CURRENCIES.CURRENCY` | `FsGiFundNavCurrencies_Currency` | TField |  | Reporting Currency (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 5 | `FS.GI.FUND.NAV.CURRENCIES.SHARE.CLASS.CODE` | `FsGiFundNavCurrencies_ShareClassCode` | TField |  | Fund share class for which the NAV per unit is defined. Multifonds DB Column is TPARTS. |
| 6 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.ONE` | `FsGiFundNavCurrencies_NavCurrencyOne` | TField |  | Curreny 1 into which the NAV prices will be translated. Does not indicate the fund reference currency. System will use the prevailing exchange rates selected for the NAV calculation to translate the NAV prices. Multifonds DB Column is CMON_1. |
| 7 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.ONE` | `FsGiFundNavCurrencies_NavCurrencyDecimalOne` | TField |  | Defines the number of decimals to be used for each price related to Currency 1. If left blank, system will use the number of decimals as defined for the respective currency in the currency master record. Multifonds DB Column is CDEC_1. |
| 8 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.TWO` | `FsGiFundNavCurrencies_NavCurrencyTwo` | TField |  | Curreny 2 into which the NAV prices will be translated. Multifonds DB Column is CMON_2. |
| 9 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.TWO` | `FsGiFundNavCurrencies_NavCurrencyDecimalTwo` | TField |  | Defines the number of decimals to be used for each price related to Currency 2. Multifonds DB Column is CDEC_2. |
| 10 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.THREE` | `FsGiFundNavCurrencies_NavCurrencyThree` | TField |  | Curreny 3 into which the NAV prices will be translated. Multifonds DB Column is CMON_3. |
| 11 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.THREE` | `FsGiFundNavCurrencies_NavCurrencyDecimalThree` | TField |  | Defines the number of decimals to be used for each price related to Currency 3. Multifonds DB Column is CDEC_3. |
| 12 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.FOUR` | `FsGiFundNavCurrencies_NavCurrencyFour` | TField |  | Curreny 4 into which the NAV prices will be translated. Multifonds DB Column is CMON_4. |
| 13 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.FOUR` | `FsGiFundNavCurrencies_NavCurrencyDecimalFour` | TField |  | Defines the number of decimals to be used for each price related to Currency 4. Multifonds DB Column is CDEC_4. |
| 14 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.FIVE` | `FsGiFundNavCurrencies_NavCurrencyFive` | TField |  | Curreny 5 into which the NAV prices will be translated. Multifonds DB Column is CMON_5. |
| 15 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.FIVE` | `FsGiFundNavCurrencies_NavCurrencyDecimalFive` | TField |  | Defines the number of decimals to be used for each price related to Currency 5. Multifonds DB Column is CDEC_5. |
| 16 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.SIX` | `FsGiFundNavCurrencies_NavCurrencySix` | TField |  | Curreny 6 into which the NAV prices will be translated. Multifonds DB Column is CMON_6. |
| 17 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.SIX` | `FsGiFundNavCurrencies_NavCurrencyDecimalSix` | TField |  | Defines the number of decimals to be used for each price related to Currency 6. Multifonds DB Column is CDEC_6. |
| 18 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.SEVEN` | `FsGiFundNavCurrencies_NavCurrencySeven` | TField |  | Curreny 7 into which the NAV prices will be translated. Multifonds DB Column is CMON_7. |
| 19 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.SEVEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalSeven` | TField |  | Defines the number of decimals to be used for each price related to Currency 7. Multifonds DB Column is CDEC_7. |
| 20 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.EIGHT` | `FsGiFundNavCurrencies_NavCurrencyEight` | TField |  | Curreny 8 into which the NAV prices will be translated. Multifonds DB Column is CMON_8. |
| 21 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.EIGHT` | `FsGiFundNavCurrencies_NavCurrencyDecimalEight` | TField |  | Defines the number of decimals to be used for each price related to Currency 8. Multifonds DB Column is CDEC_8. |
| 22 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.NINE` | `FsGiFundNavCurrencies_NavCurrencyNine` | TField |  | Curreny 9 into which the NAV prices will be translated. Multifonds DB Column is CMON_9. |
| 23 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.NINE` | `FsGiFundNavCurrencies_NavCurrencyDecimalNine` | TField |  | Defines the number of decimals to be used for each price related to Currency 9. Multifonds DB Column is CDEC_9. |
| 24 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.TEN` | `FsGiFundNavCurrencies_NavCurrencyTen` | TField |  | Curreny 10 into which the NAV prices will be translated. Multifonds DB Column is CMON_10. |
| 25 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.TEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalTen` | TField |  | Defines the number of decimals to be used for each price related to Currency 10. Multifonds DB Column is CDEC_10. |
| 26 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.ELEVEN` | `FsGiFundNavCurrencies_NavCurrencyEleven` | TField |  | Curreny 11 into which the NAV prices will be translated. Multifonds DB Column is CMON_11. |
| 27 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.ELEVEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalEleven` | TField |  | Defines the number of decimals to be used for each price related to Currency 11. Multifonds DB Column is CDEC_11. |
| 28 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.TWELVE` | `FsGiFundNavCurrencies_NavCurrencyTwelve` | TField |  | Curreny 12 into which the NAV prices will be translated. Multifonds DB Column is CMON_12. |
| 29 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.TWELVE` | `FsGiFundNavCurrencies_NavCurrencyDecimalTwelve` | TField |  | Defines the number of decimals to be used for each price related to Currency 12. Multifonds DB Column is CDEC_12. |
| 30 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.THIRTEEN` | `FsGiFundNavCurrencies_NavCurrencyThirteen` | TField |  | Curreny 13 into which the NAV prices will be translated. Multifonds DB Column is CMON_13. |
| 31 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.THIRTEEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalThirteen` | TField |  | Defines the number of decimals to be used for each price related to Currency 13. Multifonds DB Column is CDEC_13. |
| 32 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.FOURTEEN` | `FsGiFundNavCurrencies_NavCurrencyFourteen` | TField |  | Curreny 14 into which the NAV prices will be translated. Multifonds DB Column is CMON_14. |
| 33 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.FOURTEEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalFourteen` | TField |  | Defines the number of decimals to be used for each price related to Currency 14. Multifonds DB Column is CDEC_14. |
| 34 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.FIFTEEN` | `FsGiFundNavCurrencies_NavCurrencyFifteen` | TField |  | Curreny 15 into which the NAV prices will be translated. Multifonds DB Column is CMON_15. |
| 35 | `FS.GI.FUND.NAV.CURRENCIES.NAV.CURRENCY.DECIMAL.FIFTEEN` | `FsGiFundNavCurrencies_NavCurrencyDecimalFifteen` | TField |  | Defines the number of decimals to be used for each price related to Currency 15. Multifonds DB Column is CDEC_15. |
| 36 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED10` | `FsGiFundNavCurrencies_Reserved10` | TField |  |  |
| 37 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED9` | `FsGiFundNavCurrencies_Reserved9` | TField |  |  |
| 38 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED8` | `FsGiFundNavCurrencies_Reserved8` | TField |  |  |
| 39 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED7` | `FsGiFundNavCurrencies_Reserved7` | TField |  |  |
| 40 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED6` | `FsGiFundNavCurrencies_Reserved6` | TField |  |  |
| 41 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED5` | `FsGiFundNavCurrencies_Reserved5` | TField |  |  |
| 42 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED4` | `FsGiFundNavCurrencies_Reserved4` | TField |  |  |
| 43 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED3` | `FsGiFundNavCurrencies_Reserved3` | TField |  |  |
| 44 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED2` | `FsGiFundNavCurrencies_Reserved2` | TField |  |  |
| 45 | `FS.GI.FUND.NAV.CURRENCIES.RESERVED1` | `FsGiFundNavCurrencies_Reserved1` | TField |  |  |
| 46 | `FS.GI.FUND.NAV.CURRENCIES.LOCAL.REF` | `FsGiFundNavCurrencies_LocalRef` |  |  |  |
| 47 | `FS.GI.FUND.NAV.CURRENCIES.OVERRIDE` | `FsGiFundNavCurrencies_Override` |  |  |  |
| 48 | `FS.GI.FUND.NAV.CURRENCIES.RECORD.STATUS` | `FsGiFundNavCurrencies_RecordStatus` | String |  |  |
| 49 | `FS.GI.FUND.NAV.CURRENCIES.CURR.NO` | `FsGiFundNavCurrencies_CurrNo` | String |  |  |
| 50 | `FS.GI.FUND.NAV.CURRENCIES.INPUTTER` | `FsGiFundNavCurrencies_Inputter` |  |  |  |
| 51 | `FS.GI.FUND.NAV.CURRENCIES.DATE.TIME` | `FsGiFundNavCurrencies_DateTime` |  |  |  |
| 52 | `FS.GI.FUND.NAV.CURRENCIES.AUTHORISER` | `FsGiFundNavCurrencies_Authoriser` | String |  |  |
| 53 | `FS.GI.FUND.NAV.CURRENCIES.CO.CODE` | `FsGiFundNavCurrencies_CoCode` | String |  |  |
| 54 | `FS.GI.FUND.NAV.CURRENCIES.DEPT.CODE` | `FsGiFundNavCurrencies_DeptCode` | String |  |  |
| 55 | `FS.GI.FUND.NAV.CURRENCIES.AUDITOR.CODE` | `FsGiFundNavCurrencies_AuditorCode` | String |  |  |
| 56 | `FS.GI.FUND.NAV.CURRENCIES.AUDIT.DATE.TIME` | `FsGiFundNavCurrencies_AuditDateTime` | String |  |  |
