# FS.GA.CURRENCY.CODES.EQUIVALENCES — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCY.CODES.EQUIVALENCES` in `FS_StaticEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.PARENT.REF.ID` | `FsGaCurrencyCodesEquivalences_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.ORA.ROWID` | `FsGaCurrencyCodesEquivalences_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.REPRISE.CURRENCY` | `FsGaCurrencyCodesEquivalences_RepriseCurrency` | TField |  | Currency Multifonds DB Column is CMON_REPRISE. |
| 4 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.MULTIFONDS.CURRENCY` | `FsGaCurrencyCodesEquivalences_MultifondsCurrency` | TField |  | Multifonds Currency Multifonds DB Column is CMON_MULTIFONDS. |
| 5 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.CCY.FOR.SEC.EXCHANGE.INT.RATE` | `FsGaCurrencyCodesEquivalences_CcyForSecExchangeIntRate` | TField |  | Currency code for securities, currencies and interest Multifonds DB Column is CMON_COURS. |
| 6 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.CCY.FOR.SEC.EXCH.INT.RATE` | `FsGaCurrencyCodesEquivalences_CcyForSecExchIntRate` | TField |  | Currency code for securities, currencies and interest Multifonds DB Column is CMON_ISO. |
| 7 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.ISIN.CODE` | `FsGaCurrencyCodesEquivalences_IsinCode` | TField |  | International security identification number (ISIN) Multifonds DB Column is CODISIN. |
| 8 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.ISIN.SEQUENCE` | `FsGaCurrencyCodesEquivalences_IsinSequence` | TField |  | ISIN sequence of the security. Multifonds DB Column is SEQISIN. |
| 9 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.CUSIP` | `FsGaCurrencyCodesEquivalences_Cusip` | TField |  | Committee on Uniform Securities Identification Procedures. A CUSIP is a nine digit numeric or alphanumeric code that identifies security and facilitates clearing and settlement of trades Multifonds DB Column is CUSIP. |
| 10 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.FUND.ID` | `FsGaCurrencyCodesEquivalences_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 11 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.MULTIPLIER` | `FsGaCurrencyCodesEquivalences_Multiplier` | TField |  | Multiplier Multifonds DB Column is MULTIPLIER. |
| 12 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.INPUT.CONTROL.FOR.MULTIPLIER` | `FsGaCurrencyCodesEquivalences_InputControlForMultiplier` | TField |  | Input Ctrl For Multiplier Multifonds DB Column is FLG_INPUT_CTR. |
| 13 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED10` | `FsGaCurrencyCodesEquivalences_Reserved10` | TField |  |  |
| 14 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED9` | `FsGaCurrencyCodesEquivalences_Reserved9` | TField |  |  |
| 15 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED8` | `FsGaCurrencyCodesEquivalences_Reserved8` | TField |  |  |
| 16 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED7` | `FsGaCurrencyCodesEquivalences_Reserved7` | TField |  |  |
| 17 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED6` | `FsGaCurrencyCodesEquivalences_Reserved6` | TField |  |  |
| 18 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED5` | `FsGaCurrencyCodesEquivalences_Reserved5` | TField |  |  |
| 19 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED4` | `FsGaCurrencyCodesEquivalences_Reserved4` | TField |  |  |
| 20 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED3` | `FsGaCurrencyCodesEquivalences_Reserved3` | TField |  |  |
| 21 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED2` | `FsGaCurrencyCodesEquivalences_Reserved2` | TField |  |  |
| 22 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RESERVED1` | `FsGaCurrencyCodesEquivalences_Reserved1` | TField |  |  |
| 23 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.LOCAL.REF` | `FsGaCurrencyCodesEquivalences_LocalRef` |  |  |  |
| 24 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.OVERRIDE` | `FsGaCurrencyCodesEquivalences_Override` |  |  |  |
| 25 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.RECORD.STATUS` | `FsGaCurrencyCodesEquivalences_RecordStatus` | String |  |  |
| 26 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.CURR.NO` | `FsGaCurrencyCodesEquivalences_CurrNo` | String |  |  |
| 27 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.INPUTTER` | `FsGaCurrencyCodesEquivalences_Inputter` |  |  |  |
| 28 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.DATE.TIME` | `FsGaCurrencyCodesEquivalences_DateTime` |  |  |  |
| 29 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.AUTHORISER` | `FsGaCurrencyCodesEquivalences_Authoriser` | String |  |  |
| 30 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.CO.CODE` | `FsGaCurrencyCodesEquivalences_CoCode` | String |  |  |
| 31 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.DEPT.CODE` | `FsGaCurrencyCodesEquivalences_DeptCode` | String |  |  |
| 32 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.AUDITOR.CODE` | `FsGaCurrencyCodesEquivalences_AuditorCode` | String |  |  |
| 33 | `FS.GA.CURRENCY.CODES.EQUIVALENCES.AUDIT.DATE.TIME` | `FsGaCurrencyCodesEquivalences_AuditDateTime` | String |  |  |
