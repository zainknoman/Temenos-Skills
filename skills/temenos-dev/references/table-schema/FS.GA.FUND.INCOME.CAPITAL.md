# FS.GA.FUND.INCOME.CAPITAL — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.INCOME.CAPITAL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.INCOME.CAPITAL.PARENT.REF.ID` | `FsGaFundIncomeCapital_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.INCOME.CAPITAL.ORA.ROWID` | `FsGaFundIncomeCapital_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.INCOME.CAPITAL.FUND.ID` | `FsGaFundIncomeCapital_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUND.INCOME.CAPITAL.BS.GROUPING` | `FsGaFundIncomeCapital_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 5 | `FS.GA.FUND.INCOME.CAPITAL.DESCRIPTIONS` | `FsGaFundIncomeCapital_Descriptions` | TField |  | The fund description is a 40 character alphanumeric field. The fund description appears on all Multifonds reports. Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.FUND.INCOME.CAPITAL.QUOTATION.TYPE` | `FsGaFundIncomeCapital_QuotationType` | TField |  | Quatation Type Multifonds DB Column is CTYPE. |
| 7 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED10` | `FsGaFundIncomeCapital_Reserved10` | TField |  |  |
| 8 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED9` | `FsGaFundIncomeCapital_Reserved9` | TField |  |  |
| 9 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED8` | `FsGaFundIncomeCapital_Reserved8` | TField |  |  |
| 10 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED7` | `FsGaFundIncomeCapital_Reserved7` | TField |  |  |
| 11 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED6` | `FsGaFundIncomeCapital_Reserved6` | TField |  |  |
| 12 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED5` | `FsGaFundIncomeCapital_Reserved5` | TField |  |  |
| 13 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED4` | `FsGaFundIncomeCapital_Reserved4` | TField |  |  |
| 14 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED3` | `FsGaFundIncomeCapital_Reserved3` | TField |  |  |
| 15 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED2` | `FsGaFundIncomeCapital_Reserved2` | TField |  |  |
| 16 | `FS.GA.FUND.INCOME.CAPITAL.RESERVED1` | `FsGaFundIncomeCapital_Reserved1` | TField |  |  |
| 17 | `FS.GA.FUND.INCOME.CAPITAL.LOCAL.REF` | `FsGaFundIncomeCapital_LocalRef` |  |  |  |
| 18 | `FS.GA.FUND.INCOME.CAPITAL.OVERRIDE` | `FsGaFundIncomeCapital_Override` |  |  |  |
| 19 | `FS.GA.FUND.INCOME.CAPITAL.RECORD.STATUS` | `FsGaFundIncomeCapital_RecordStatus` | String |  |  |
| 20 | `FS.GA.FUND.INCOME.CAPITAL.CURR.NO` | `FsGaFundIncomeCapital_CurrNo` | String |  |  |
| 21 | `FS.GA.FUND.INCOME.CAPITAL.INPUTTER` | `FsGaFundIncomeCapital_Inputter` |  |  |  |
| 22 | `FS.GA.FUND.INCOME.CAPITAL.DATE.TIME` | `FsGaFundIncomeCapital_DateTime` |  |  |  |
| 23 | `FS.GA.FUND.INCOME.CAPITAL.AUTHORISER` | `FsGaFundIncomeCapital_Authoriser` | String |  |  |
| 24 | `FS.GA.FUND.INCOME.CAPITAL.CO.CODE` | `FsGaFundIncomeCapital_CoCode` | String |  |  |
| 25 | `FS.GA.FUND.INCOME.CAPITAL.DEPT.CODE` | `FsGaFundIncomeCapital_DeptCode` | String |  |  |
| 26 | `FS.GA.FUND.INCOME.CAPITAL.AUDITOR.CODE` | `FsGaFundIncomeCapital_AuditorCode` | String |  |  |
| 27 | `FS.GA.FUND.INCOME.CAPITAL.AUDIT.DATE.TIME` | `FsGaFundIncomeCapital_AuditDateTime` | String |  |  |
