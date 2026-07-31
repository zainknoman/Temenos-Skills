# FS.GA.FUND.CURRENCY.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.CURRENCY.EXCEPTION` in `FS_FundMasterException.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.CURRENCY.EXCEPTION.PARENT.REF.ID` | `FsGaFundCurrencyException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.CURRENCY.EXCEPTION.ORA.ROWID` | `FsGaFundCurrencyException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.CURRENCY.EXCEPTION.FUND.ID` | `FsGaFundCurrencyException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUND.CURRENCY.EXCEPTION.LOCAL.CURRENCY` | `FsGaFundCurrencyException_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 5 | `FS.GA.FUND.CURRENCY.EXCEPTION.ARCHIVE` | `FsGaFundCurrencyException_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 6 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED10` | `FsGaFundCurrencyException_Reserved10` | TField |  |  |
| 7 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED9` | `FsGaFundCurrencyException_Reserved9` | TField |  |  |
| 8 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED8` | `FsGaFundCurrencyException_Reserved8` | TField |  |  |
| 9 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED7` | `FsGaFundCurrencyException_Reserved7` | TField |  |  |
| 10 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED6` | `FsGaFundCurrencyException_Reserved6` | TField |  |  |
| 11 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED5` | `FsGaFundCurrencyException_Reserved5` | TField |  |  |
| 12 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED4` | `FsGaFundCurrencyException_Reserved4` | TField |  |  |
| 13 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED3` | `FsGaFundCurrencyException_Reserved3` | TField |  |  |
| 14 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED2` | `FsGaFundCurrencyException_Reserved2` | TField |  |  |
| 15 | `FS.GA.FUND.CURRENCY.EXCEPTION.RESERVED1` | `FsGaFundCurrencyException_Reserved1` | TField |  |  |
| 16 | `FS.GA.FUND.CURRENCY.EXCEPTION.LOCAL.REF` | `FsGaFundCurrencyException_LocalRef` |  |  |  |
| 17 | `FS.GA.FUND.CURRENCY.EXCEPTION.OVERRIDE` | `FsGaFundCurrencyException_Override` |  |  |  |
| 18 | `FS.GA.FUND.CURRENCY.EXCEPTION.RECORD.STATUS` | `FsGaFundCurrencyException_RecordStatus` | String |  |  |
| 19 | `FS.GA.FUND.CURRENCY.EXCEPTION.CURR.NO` | `FsGaFundCurrencyException_CurrNo` | String |  |  |
| 20 | `FS.GA.FUND.CURRENCY.EXCEPTION.INPUTTER` | `FsGaFundCurrencyException_Inputter` |  |  |  |
| 21 | `FS.GA.FUND.CURRENCY.EXCEPTION.DATE.TIME` | `FsGaFundCurrencyException_DateTime` |  |  |  |
| 22 | `FS.GA.FUND.CURRENCY.EXCEPTION.AUTHORISER` | `FsGaFundCurrencyException_Authoriser` | String |  |  |
| 23 | `FS.GA.FUND.CURRENCY.EXCEPTION.CO.CODE` | `FsGaFundCurrencyException_CoCode` | String |  |  |
| 24 | `FS.GA.FUND.CURRENCY.EXCEPTION.DEPT.CODE` | `FsGaFundCurrencyException_DeptCode` | String |  |  |
| 25 | `FS.GA.FUND.CURRENCY.EXCEPTION.AUDITOR.CODE` | `FsGaFundCurrencyException_AuditorCode` | String |  |  |
| 26 | `FS.GA.FUND.CURRENCY.EXCEPTION.AUDIT.DATE.TIME` | `FsGaFundCurrencyException_AuditDateTime` | String |  |  |
