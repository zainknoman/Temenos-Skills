# FS.GI.FUND.FREQUENCY.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.FREQUENCY.EXCEPTION` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.FREQUENCY.EXCEPTION.PARENT.REF.ID` | `FsGiFundFrequencyException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.FREQUENCY.EXCEPTION.ORA.ROWID` | `FsGiFundFrequencyException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.FREQUENCY.EXCEPTION.FUND.ID` | `FsGiFundFrequencyException_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.FREQUENCY.EXCEPTION.SHARE.CLASS.CODE` | `FsGiFundFrequencyException_ShareClassCode` | TField |  | Share class code applicable for frequency exception. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.FREQUENCY.EXCEPTION.OPERATION.CODE` | `FsGiFundFrequencyException_OperationCode` | TField |  | Operation code applicable for frequency exception. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.FREQUENCY.EXCEPTION.INITIAL.DATE` | `FsGiFundFrequencyException_InitialDate` | TField |  | The first date when the fund calculates the NAV. Multifonds DB Column is DT_BASE_CALC. |
| 7 | `FS.GI.FUND.FREQUENCY.EXCEPTION.FREQUENCY` | `FsGiFundFrequencyException_Frequency` | TField |  | NAV Frequency code . Multifonds DB Column is CFREQ. |
| 8 | `FS.GI.FUND.FREQUENCY.EXCEPTION.NEXT.THEORETICAL.NAV.DATE` | `FsGiFundFrequencyException_NextTheoreticalNavDate` | TField |  | The next theoretical NAV date based on the initial NAV date. Multifonds DB Column is DATE_SUIV. |
| 9 | `FS.GI.FUND.FREQUENCY.EXCEPTION.PREVIOUS.THEORETICAL.NAV.DATE` | `FsGiFundFrequencyException_PreviousTheoreticalNavDate` | TField |  | The previous theoretical NAV date. Multifonds DB Column is DATE_PREC. |
| 10 | `FS.GI.FUND.FREQUENCY.EXCEPTION.NEXT.THEORETICAL.NAV.DATE.TA` | `FsGiFundFrequencyException_NextTheoreticalNavDateTa` | TField |  | The next theoretical NAV date for TA based on the initial NAV date. Multifonds DB Column is DATE_SUIV_TA. |
| 11 | `FS.GI.FUND.FREQUENCY.EXCEPTION.MONTH.END.DATE.TYPE` | `FsGiFundFrequencyException_MonthEndDateType` | TField |  | The month end type code to apply for NAV date calculation if the month end falls on a week end or holiday. Multifonds DB Column is CTR_DATE_MONTHEND. |
| 12 | `FS.GI.FUND.FREQUENCY.EXCEPTION.NUMBER.OF.DAYS.TO.CALCULAE` | `FsGiFundFrequencyException_NumberOfDaysToCalculae` | TField |  | The number of days to add to the initial date for NAV date calculation. Multifonds DB Column is NB_FIX_JOUR. |
| 13 | `FS.GI.FUND.FREQUENCY.EXCEPTION.WEEK.NUMBER` | `FsGiFundFrequencyException_WeekNumber` | TField |  | The week number. Multifonds DB Column is NUM_SEM. |
| 14 | `FS.GI.FUND.FREQUENCY.EXCEPTION.DAY.NUMBER.IN.WEEK` | `FsGiFundFrequencyException_DayNumberInWeek` | TField |  | The day number in a week. Multifonds DB Column is NUM_JOUR. |
| 15 | `FS.GI.FUND.FREQUENCY.EXCEPTION.TYPE.OF.DATE` | `FsGiFundFrequencyException_TypeOfDate` | TField |  | Type of date code for NAV calculation. Multifonds DB Column is CTR_DATE. |
| 16 | `FS.GI.FUND.FREQUENCY.EXCEPTION.INTERNAL.ID` | `FsGiFundFrequencyException_InternalId` | TField |  | Unique internal identifier of the record. Multifonds DB Column is INTERNAL_ID. |
| 17 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED10` | `FsGiFundFrequencyException_Reserved10` | TField |  |  |
| 18 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED9` | `FsGiFundFrequencyException_Reserved9` | TField |  |  |
| 19 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED8` | `FsGiFundFrequencyException_Reserved8` | TField |  |  |
| 20 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED7` | `FsGiFundFrequencyException_Reserved7` | TField |  |  |
| 21 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED6` | `FsGiFundFrequencyException_Reserved6` | TField |  |  |
| 22 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED5` | `FsGiFundFrequencyException_Reserved5` | TField |  |  |
| 23 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED4` | `FsGiFundFrequencyException_Reserved4` | TField |  |  |
| 24 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED3` | `FsGiFundFrequencyException_Reserved3` | TField |  |  |
| 25 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED2` | `FsGiFundFrequencyException_Reserved2` | TField |  |  |
| 26 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RESERVED1` | `FsGiFundFrequencyException_Reserved1` | TField |  |  |
| 27 | `FS.GI.FUND.FREQUENCY.EXCEPTION.LOCAL.REF` | `FsGiFundFrequencyException_LocalRef` |  |  |  |
| 28 | `FS.GI.FUND.FREQUENCY.EXCEPTION.OVERRIDE` | `FsGiFundFrequencyException_Override` |  |  |  |
| 29 | `FS.GI.FUND.FREQUENCY.EXCEPTION.RECORD.STATUS` | `FsGiFundFrequencyException_RecordStatus` | String |  |  |
| 30 | `FS.GI.FUND.FREQUENCY.EXCEPTION.CURR.NO` | `FsGiFundFrequencyException_CurrNo` | String |  |  |
| 31 | `FS.GI.FUND.FREQUENCY.EXCEPTION.INPUTTER` | `FsGiFundFrequencyException_Inputter` |  |  |  |
| 32 | `FS.GI.FUND.FREQUENCY.EXCEPTION.DATE.TIME` | `FsGiFundFrequencyException_DateTime` |  |  |  |
| 33 | `FS.GI.FUND.FREQUENCY.EXCEPTION.AUTHORISER` | `FsGiFundFrequencyException_Authoriser` | String |  |  |
| 34 | `FS.GI.FUND.FREQUENCY.EXCEPTION.CO.CODE` | `FsGiFundFrequencyException_CoCode` | String |  |  |
| 35 | `FS.GI.FUND.FREQUENCY.EXCEPTION.DEPT.CODE` | `FsGiFundFrequencyException_DeptCode` | String |  |  |
| 36 | `FS.GI.FUND.FREQUENCY.EXCEPTION.AUDITOR.CODE` | `FsGiFundFrequencyException_AuditorCode` | String |  |  |
| 37 | `FS.GI.FUND.FREQUENCY.EXCEPTION.AUDIT.DATE.TIME` | `FsGiFundFrequencyException_AuditDateTime` | String |  |  |
