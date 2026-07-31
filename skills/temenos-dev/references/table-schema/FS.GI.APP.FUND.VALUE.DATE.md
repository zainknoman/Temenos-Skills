# FS.GI.APP.FUND.VALUE.DATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.FUND.VALUE.DATE` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.FUND.VALUE.DATE.PARENT.REF.ID` | `FsGiAppFundValueDate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.FUND.VALUE.DATE.ORA.ROWID` | `FsGiAppFundValueDate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.FUND.VALUE.DATE.TA.FUND.ID` | `FsGiAppFundValueDate_TaFundId` | TField |  | Fund ID for which the value date method is defined. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.APP.FUND.VALUE.DATE.OPERATION.CODE` | `FsGiAppFundValueDate_OperationCode` | TField |  | Operation code for which the value date method is defined. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.APP.FUND.VALUE.DATE.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiAppFundValueDate_ValueDateNumberOfDays` | TField |  | Number of Days to add to the Trade date excluding the holidays to consider following the Value Date method for the specified fund and the operation defined. Multifonds DB Column is NUMBER_DAYS. |
| 6 | `FS.GI.APP.FUND.VALUE.DATE.VALUE.DATE.TYPE` | `FsGiAppFundValueDate_ValueDateType` | TField |  | Value date type code which allows the user to define a fixed or minimum number of days to be taken into account . Multifonds DB Column is VALUE_DATE_TYPE. |
| 7 | `FS.GI.APP.FUND.VALUE.DATE.VALUE.DATE.METHOD` | `FsGiAppFundValueDate_ValueDateMethod` | TField |  | Method which defines holiday management to be considered for value date calculations. Multifonds DB Column is WORKING_DAY. |
| 8 | `FS.GI.APP.FUND.VALUE.DATE.FUND.ID` | `FsGiAppFundValueDate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.APP.FUND.VALUE.DATE.CLASS.CURRENCY` | `FsGiAppFundValueDate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED10` | `FsGiAppFundValueDate_Reserved10` | TField |  |  |
| 11 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED9` | `FsGiAppFundValueDate_Reserved9` | TField |  |  |
| 12 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED8` | `FsGiAppFundValueDate_Reserved8` | TField |  |  |
| 13 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED7` | `FsGiAppFundValueDate_Reserved7` | TField |  |  |
| 14 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED6` | `FsGiAppFundValueDate_Reserved6` | TField |  |  |
| 15 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED5` | `FsGiAppFundValueDate_Reserved5` | TField |  |  |
| 16 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED4` | `FsGiAppFundValueDate_Reserved4` | TField |  |  |
| 17 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED3` | `FsGiAppFundValueDate_Reserved3` | TField |  |  |
| 18 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED2` | `FsGiAppFundValueDate_Reserved2` | TField |  |  |
| 19 | `FS.GI.APP.FUND.VALUE.DATE.RESERVED1` | `FsGiAppFundValueDate_Reserved1` | TField |  |  |
| 20 | `FS.GI.APP.FUND.VALUE.DATE.LOCAL.REF` | `FsGiAppFundValueDate_LocalRef` |  |  |  |
| 21 | `FS.GI.APP.FUND.VALUE.DATE.OVERRIDE` | `FsGiAppFundValueDate_Override` |  |  |  |
| 22 | `FS.GI.APP.FUND.VALUE.DATE.RECORD.STATUS` | `FsGiAppFundValueDate_RecordStatus` | String |  |  |
| 23 | `FS.GI.APP.FUND.VALUE.DATE.CURR.NO` | `FsGiAppFundValueDate_CurrNo` | String |  |  |
| 24 | `FS.GI.APP.FUND.VALUE.DATE.INPUTTER` | `FsGiAppFundValueDate_Inputter` |  |  |  |
| 25 | `FS.GI.APP.FUND.VALUE.DATE.DATE.TIME` | `FsGiAppFundValueDate_DateTime` |  |  |  |
| 26 | `FS.GI.APP.FUND.VALUE.DATE.AUTHORISER` | `FsGiAppFundValueDate_Authoriser` | String |  |  |
| 27 | `FS.GI.APP.FUND.VALUE.DATE.CO.CODE` | `FsGiAppFundValueDate_CoCode` | String |  |  |
| 28 | `FS.GI.APP.FUND.VALUE.DATE.DEPT.CODE` | `FsGiAppFundValueDate_DeptCode` | String |  |  |
| 29 | `FS.GI.APP.FUND.VALUE.DATE.AUDITOR.CODE` | `FsGiAppFundValueDate_AuditorCode` | String |  |  |
| 30 | `FS.GI.APP.FUND.VALUE.DATE.AUDIT.DATE.TIME` | `FsGiAppFundValueDate_AuditDateTime` | String |  |  |
