# FS.GI.FUND.CALENDAR.FREQ.FIXED — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.CALENDAR.FREQ.FIXED` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.PARENT.REF.ID` | `FsGiFundCalendarFreqFixed_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.ORA.ROWID` | `FsGiFundCalendarFreqFixed_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.FUND.ID` | `FsGiFundCalendarFreqFixed_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.FREQUENCY` | `FsGiFundCalendarFreqFixed_Frequency` | TField |  | NAV Frequency code. Multifonds DB Column is CFREQ. |
| 5 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.FIXED.NAV.DAY` | `FsGiFundCalendarFreqFixed_FixedNavDay` | TField |  | The NAV day on which the NAV calculation will be carried out for the Fund. Multifonds DB Column is FIXED_NAV_DAY. |
| 6 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.FIXED.WEEK` | `FsGiFundCalendarFreqFixed_FixedWeek` | TField |  | The week of the month for NAV calculation. Multifonds DB Column is FIXED_WEEK. |
| 7 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.PAYMENT.WEEK.DAY` | `FsGiFundCalendarFreqFixed_PaymentWeekDay` | TField |  | It specifies the payment week day code. Multifonds DB Column is WEEK_DAY. |
| 8 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.SEQUENCE.NUMBER` | `FsGiFundCalendarFreqFixed_SequenceNumber` | TField |  | Sequence number. Multifonds DB Column is SEQ_NO. |
| 9 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.INTERNAL.ID` | `FsGiFundCalendarFreqFixed_InternalId` | TField |  | Unique internal Identifier of the record. Multifonds DB Column is INTERNAL_ID. |
| 10 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED10` | `FsGiFundCalendarFreqFixed_Reserved10` | TField |  |  |
| 11 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED9` | `FsGiFundCalendarFreqFixed_Reserved9` | TField |  |  |
| 12 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED8` | `FsGiFundCalendarFreqFixed_Reserved8` | TField |  |  |
| 13 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED7` | `FsGiFundCalendarFreqFixed_Reserved7` | TField |  |  |
| 14 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED6` | `FsGiFundCalendarFreqFixed_Reserved6` | TField |  |  |
| 15 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED5` | `FsGiFundCalendarFreqFixed_Reserved5` | TField |  |  |
| 16 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED4` | `FsGiFundCalendarFreqFixed_Reserved4` | TField |  |  |
| 17 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED3` | `FsGiFundCalendarFreqFixed_Reserved3` | TField |  |  |
| 18 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED2` | `FsGiFundCalendarFreqFixed_Reserved2` | TField |  |  |
| 19 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RESERVED1` | `FsGiFundCalendarFreqFixed_Reserved1` | TField |  |  |
| 20 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.LOCAL.REF` | `FsGiFundCalendarFreqFixed_LocalRef` |  |  |  |
| 21 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.OVERRIDE` | `FsGiFundCalendarFreqFixed_Override` |  |  |  |
| 22 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.RECORD.STATUS` | `FsGiFundCalendarFreqFixed_RecordStatus` | String |  |  |
| 23 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.CURR.NO` | `FsGiFundCalendarFreqFixed_CurrNo` | String |  |  |
| 24 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.INPUTTER` | `FsGiFundCalendarFreqFixed_Inputter` |  |  |  |
| 25 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.DATE.TIME` | `FsGiFundCalendarFreqFixed_DateTime` |  |  |  |
| 26 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.AUTHORISER` | `FsGiFundCalendarFreqFixed_Authoriser` | String |  |  |
| 27 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.CO.CODE` | `FsGiFundCalendarFreqFixed_CoCode` | String |  |  |
| 28 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.DEPT.CODE` | `FsGiFundCalendarFreqFixed_DeptCode` | String |  |  |
| 29 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.AUDITOR.CODE` | `FsGiFundCalendarFreqFixed_AuditorCode` | String |  |  |
| 30 | `FS.GI.FUND.CALENDAR.FREQ.FIXED.AUDIT.DATE.TIME` | `FsGiFundCalendarFreqFixed_AuditDateTime` | String |  |  |
