# FS.GI.FUND.VALUE.DATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.VALUE.DATE` in `FS_FundDealing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.VALUE.DATE.PARENT.REF.ID` | `FsGiFundValueDate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.VALUE.DATE.ORA.ROWID` | `FsGiFundValueDate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.VALUE.DATE.TA.FUND.ID` | `FsGiFundValueDate_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.VALUE.DATE.SHARE.CLASS.CODE` | `FsGiFundValueDate_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.VALUE.DATE.OPERATION.CODE` | `FsGiFundValueDate_OperationCode` | TField |  | Operation code in scope of fund value date management. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.VALUE.DATE.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiFundValueDate_ValueDateNumberOfDays` | TField |  | Number of days to be added to Trade date to arrive at the value date. Multifonds DB Column is NUMBER_DAYS. |
| 7 | `FS.GI.FUND.VALUE.DATE.VALUE.DATE.METHOD` | `FsGiFundValueDate_ValueDateMethod` | TField |  | Method which defines holiday management to be considered for value date calculations. Multifonds DB Column is WORKING_DAY. |
| 8 | `FS.GI.FUND.VALUE.DATE.INTERNAL.ID` | `FsGiFundValueDate_InternalId` | TField |  | Uniquer internal idenfitier for the record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.FUND.VALUE.DATE.FUND.ID` | `FsGiFundValueDate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.FUND.VALUE.DATE.CLASS.CURRENCY` | `FsGiFundValueDate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.FUND.VALUE.DATE.RESERVED10` | `FsGiFundValueDate_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.VALUE.DATE.RESERVED9` | `FsGiFundValueDate_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.VALUE.DATE.RESERVED8` | `FsGiFundValueDate_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.VALUE.DATE.RESERVED7` | `FsGiFundValueDate_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.VALUE.DATE.RESERVED6` | `FsGiFundValueDate_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.VALUE.DATE.RESERVED5` | `FsGiFundValueDate_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.VALUE.DATE.RESERVED4` | `FsGiFundValueDate_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.VALUE.DATE.RESERVED3` | `FsGiFundValueDate_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.VALUE.DATE.RESERVED2` | `FsGiFundValueDate_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.VALUE.DATE.RESERVED1` | `FsGiFundValueDate_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.VALUE.DATE.LOCAL.REF` | `FsGiFundValueDate_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.VALUE.DATE.OVERRIDE` | `FsGiFundValueDate_Override` |  |  |  |
| 23 | `FS.GI.FUND.VALUE.DATE.RECORD.STATUS` | `FsGiFundValueDate_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.VALUE.DATE.CURR.NO` | `FsGiFundValueDate_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.VALUE.DATE.INPUTTER` | `FsGiFundValueDate_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.VALUE.DATE.DATE.TIME` | `FsGiFundValueDate_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.VALUE.DATE.AUTHORISER` | `FsGiFundValueDate_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.VALUE.DATE.CO.CODE` | `FsGiFundValueDate_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.VALUE.DATE.DEPT.CODE` | `FsGiFundValueDate_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.VALUE.DATE.AUDITOR.CODE` | `FsGiFundValueDate_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.VALUE.DATE.AUDIT.DATE.TIME` | `FsGiFundValueDate_AuditDateTime` | String |  |  |
