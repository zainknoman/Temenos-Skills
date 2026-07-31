# IAS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.IAS.PARAMETER` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IASP.DESCRIPTION` | `IasParameter_Description` |  |  |  |
| 2 | `IASP.CALCULATION.FREQ` | `IasParameter_CalculationFreq` | TField |  | This field can be used to specify the date and frequency of calculation of the IAS data. Validation Rules: 16 character standard date / frequency format - e.g. M0301 - indicates a Quarterly Frequency falling one the first of the month. The date given must be greater than today. |
| 3 | `IASP.ACCOUNTING.FREQ` | `IasParameter_AccountingFreq` | TField |  | This can be used to specify the frequency of posting of Accounting Entries. Validation Rules: 16 character standard date / frequency format - e.g. M0301 - indicates a Quarterly Frequency falling one the first of the month. The date given must be greater than today. |
| 4 | `IASP.HISTORY.PERIOD` | `IasParameter_HistoryPeriod` | TField |  | Specifies the period of time for which history is to be maintained for Contract Balances.Records in the IAS.CONTRACT.BALANCES.HIST file, exceeding the history period will be cleared at End-of-Day. Validation Rules: Alphanumeric 5 characters. Should be of the format nD/M/Y - where n is a number - a maximum of 4 digits , D - day(s) , M - month(s) , Y - year(s) e.g. 100D, 6M, 2Y. |
| 5 | `IASP.MAT.REV.TO.HIST` | `IasParameter_MatRevToHist` | TField | No | Specifies the time period for which Reversed / Matured Contracts (with STATUS field as REV / MAT) should be kept in the IAS.CONTRACT.BALANCES file before they are moved to the IAS.CONTRACT.BALANCES.HIST file. Records will be moved only if this field has a proper time period set. Validation Rules: Alphanumeric 5 characters. Optional Input. Should be of the format nD/M/Y - where n is a number - a maximum of 4 digits , D - day(s) , M - month(s) , Y - year(s) or it can take the value NEVER. e.g. 100D, 6M, 2Y. |
| 6 | `IASP.HEDGE.EFF.FREQ` | `IasParameter_HedgeEffFreq` | TField |  | This can be used to specify the frequency of processing of Hedged Amount Types which updates the HEDGING / HEDGED Amount Type details and effectiveness in IAS.HEDGE.GROUP. If the value of this field is ONLINE, then this processing is trigerred online. If a frequency is specified , then the processing happens at EOD - on the date specified. Validation Rules: 16 character standard date / frequency format or ONLINE - e.g. M0301 - indicates a Quarterly Frequency falling one the first of the month. The date given must be greater than today. |
| 7 | `IASP.HEDGE.ACC.FREQ` | `IasParameter_HedgeAccFreq` | TField |  | This can be used to specify the frequency of posting of Hedged Accounting Entries. Validation Rules: 16 character standard date / frequency format - e.g. M0301 - indicates a Quarterly Frequency falling one the first of the month. The date given must be greater than today. |
| 8 | `IASP.LAST.ACCT.DATE` | `IasParameter_LastAcctDate` | TField |  | Last date when the accounting entries are posted will be stored in this field. |
| 9 | `IASP.LAST.CALC.DATE` | `IasParameter_LastCalcDate` | TField |  | This field stores the last date when the IAS is calculated based on the setup in CALCULATION.FREQ. |
| 10 | `IASP.RESERVED8` | `IasParameter_Reserved8` | TField |  |  |
| 11 | `IASP.RESERVED7` | `IasParameter_Reserved7` | TField |  |  |
| 12 | `IASP.RESERVED6` | `IasParameter_Reserved6` | TField |  |  |
| 13 | `IASP.RESERVED5` | `IasParameter_Reserved5` | TField |  |  |
| 14 | `IASP.RESERVED4` | `IasParameter_Reserved4` | TField |  |  |
| 15 | `IASP.RESERVED3` | `IasParameter_Reserved3` | TField |  |  |
| 16 | `IASP.RESERVED2` | `IasParameter_Reserved2` | TField |  |  |
| 17 | `IASP.RESERVED1` | `IasParameter_Reserved1` | TField |  |  |
| 18 | `IASP.LOCAL.REF` | `IasParameter_LocalRef` |  |  |  |
| 19 | `IASP.OVERRIDE` | `IasParameter_Override` |  |  |  |
| 20 | `IASP.RECORD.STATUS` | `IasParameter_RecordStatus` | String |  |  |
| 21 | `IASP.CURR.NO` | `IasParameter_CurrNo` | String |  |  |
| 22 | `IASP.INPUTTER` | `IasParameter_Inputter` |  |  |  |
| 23 | `IASP.DATE.TIME` | `IasParameter_DateTime` |  |  |  |
| 24 | `IASP.AUTHORISER` | `IasParameter_Authoriser` | String |  |  |
| 25 | `IASP.CO.CODE` | `IasParameter_CoCode` | String |  |  |
| 26 | `IASP.DEPT.CODE` | `IasParameter_DeptCode` | String |  |  |
| 27 | `IASP.AUDITOR.CODE` | `IasParameter_AuditorCode` | String |  |  |
| 28 | `IASP.AUDIT.DATE.TIME` | `IasParameter_AuditDateTime` | String |  |  |
