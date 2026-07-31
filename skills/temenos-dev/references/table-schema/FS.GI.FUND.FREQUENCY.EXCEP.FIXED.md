# FS.GI.FUND.FREQUENCY.EXCEP.FIXED — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.FREQUENCY.EXCEP.FIXED` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.PARENT.REF.ID` | `FsGiFundFrequencyExcepFixed_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.ORA.ROWID` | `FsGiFundFrequencyExcepFixed_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.FUND.ID` | `FsGiFundFrequencyExcepFixed_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.OPERATION.CODE` | `FsGiFundFrequencyExcepFixed_OperationCode` | TField |  | Operation code applicable for frequency exception. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.SHARE.CLASS.CODE` | `FsGiFundFrequencyExcepFixed_ShareClassCode` | TField |  | Share class code applicable for frequency exception. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.FREQUENCY` | `FsGiFundFrequencyExcepFixed_Frequency` | TField |  | NAV Frequency code. Multifonds DB Column is CFREQ. |
| 7 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.FIXED.NAV.DAY` | `FsGiFundFrequencyExcepFixed_FixedNavDay` | TField |  | The NAV day on which the NAV calculation will be carried out for the Fund. Multifonds DB Column is FIXED_NAV_DAY. |
| 8 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.FIXED.WEEK` | `FsGiFundFrequencyExcepFixed_FixedWeek` | TField |  | The week of the month for NAV calculation. Multifonds DB Column is FIXED_WEEK. |
| 9 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.PAYMENT.WEEK.DAY` | `FsGiFundFrequencyExcepFixed_PaymentWeekDay` | TField |  | It specifies the week day code. Multifonds DB Column is WEEK_DAY. |
| 10 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.SEQUENCE.NUMBER` | `FsGiFundFrequencyExcepFixed_SequenceNumber` | TField |  | Sequence number of the frequence exception. Multifonds DB Column is SEQ_NO. |
| 11 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.INTERNAL.ID` | `FsGiFundFrequencyExcepFixed_InternalId` | TField |  | Unique internal Identifier for frequence exception record. Multifonds DB Column is INTERNAL_ID. |
| 12 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED10` | `FsGiFundFrequencyExcepFixed_Reserved10` | TField |  |  |
| 13 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED9` | `FsGiFundFrequencyExcepFixed_Reserved9` | TField |  |  |
| 14 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED8` | `FsGiFundFrequencyExcepFixed_Reserved8` | TField |  |  |
| 15 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED7` | `FsGiFundFrequencyExcepFixed_Reserved7` | TField |  |  |
| 16 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED6` | `FsGiFundFrequencyExcepFixed_Reserved6` | TField |  |  |
| 17 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED5` | `FsGiFundFrequencyExcepFixed_Reserved5` | TField |  |  |
| 18 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED4` | `FsGiFundFrequencyExcepFixed_Reserved4` | TField |  |  |
| 19 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED3` | `FsGiFundFrequencyExcepFixed_Reserved3` | TField |  |  |
| 20 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED2` | `FsGiFundFrequencyExcepFixed_Reserved2` | TField |  |  |
| 21 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RESERVED1` | `FsGiFundFrequencyExcepFixed_Reserved1` | TField |  |  |
| 22 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.LOCAL.REF` | `FsGiFundFrequencyExcepFixed_LocalRef` |  |  |  |
| 23 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.OVERRIDE` | `FsGiFundFrequencyExcepFixed_Override` |  |  |  |
| 24 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.RECORD.STATUS` | `FsGiFundFrequencyExcepFixed_RecordStatus` | String |  |  |
| 25 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.CURR.NO` | `FsGiFundFrequencyExcepFixed_CurrNo` | String |  |  |
| 26 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.INPUTTER` | `FsGiFundFrequencyExcepFixed_Inputter` |  |  |  |
| 27 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.DATE.TIME` | `FsGiFundFrequencyExcepFixed_DateTime` |  |  |  |
| 28 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.AUTHORISER` | `FsGiFundFrequencyExcepFixed_Authoriser` | String |  |  |
| 29 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.CO.CODE` | `FsGiFundFrequencyExcepFixed_CoCode` | String |  |  |
| 30 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.DEPT.CODE` | `FsGiFundFrequencyExcepFixed_DeptCode` | String |  |  |
| 31 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.AUDITOR.CODE` | `FsGiFundFrequencyExcepFixed_AuditorCode` | String |  |  |
| 32 | `FS.GI.FUND.FREQUENCY.EXCEP.FIXED.AUDIT.DATE.TIME` | `FsGiFundFrequencyExcepFixed_AuditDateTime` | String |  |  |
