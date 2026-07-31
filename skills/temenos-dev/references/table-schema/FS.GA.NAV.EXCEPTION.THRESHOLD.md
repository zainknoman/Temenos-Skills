# FS.GA.NAV.EXCEPTION.THRESHOLD — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.EXCEPTION.THRESHOLD` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.EXCEPTION.THRESHOLD.PARENT.REF.ID` | `FsGaNavExceptionThreshold_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.EXCEPTION.THRESHOLD.ORA.ROWID` | `FsGaNavExceptionThreshold_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.EXCEPTION.THRESHOLD.FUND.ID` | `FsGaNavExceptionThreshold_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.EXCEPTION.THRESHOLD.SERVICE.CODE` | `FsGaNavExceptionThreshold_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.NAV.EXCEPTION.THRESHOLD.GTI.CODE` | `FsGaNavExceptionThreshold_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.NAV.EXCEPTION.THRESHOLD.EFFECTIVE.DATE` | `FsGaNavExceptionThreshold_EffectiveDate` | TField |  | Effective date in the NAV_EXP_THRESHOLD.CTL file Multifonds DB Column is EFT_DATE. |
| 7 | `FS.GA.NAV.EXCEPTION.THRESHOLD.CONTROL.NUMBER` | `FsGaNavExceptionThreshold_ControlNumber` | TField |  | Control Number linked to Process Multifonds DB Column is TYP_CONTROLE. |
| 8 | `FS.GA.NAV.EXCEPTION.THRESHOLD.TYPE.OF.EXCEPTION.MONITOR` | `FsGaNavExceptionThreshold_TypeOfExceptionMonitor` | TField |  | Refers to different Type of Exceptions. E.g., Amount, Percent, or Percentage of the Portfolio etc. Multifonds DB Column is TYP_CONNAV. |
| 9 | `FS.GA.NAV.EXCEPTION.THRESHOLD.VALUE.OF.EXCEPTION.MONITOR` | `FsGaNavExceptionThreshold_ValueOfExceptionMonitor` | TField |  | User has to define the threshold amount or absolute figure for control in this field. This is in relation to the Type defined. Multifonds DB Column is MNT_PCT. |
| 10 | `FS.GA.NAV.EXCEPTION.THRESHOLD.SEQUENCE.NO` | `FsGaNavExceptionThreshold_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 11 | `FS.GA.NAV.EXCEPTION.THRESHOLD.NAV.GROUP.CODE` | `FsGaNavExceptionThreshold_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 12 | `FS.GA.NAV.EXCEPTION.THRESHOLD.ISSUE.COUNTRY` | `FsGaNavExceptionThreshold_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 13 | `FS.GA.NAV.EXCEPTION.THRESHOLD.LOCAL.CURRENCY` | `FsGaNavExceptionThreshold_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 14 | `FS.GA.NAV.EXCEPTION.THRESHOLD.EXTERNAL.STATUS.CODE` | `FsGaNavExceptionThreshold_ExternalStatusCode` | TField |  | Refers to the External Status code of EXCEPTION THRESHOLD PARAM &amp; TRADE ORDER MANAGEMENT screen Multifonds DB Column is CSTATUS_EXT. |
| 15 | `FS.GA.NAV.EXCEPTION.THRESHOLD.HIGH.VARIANCE.PERCENT` | `FsGaNavExceptionThreshold_HighVariancePercent` | TField |  | It refers to Threshold filed in Exception Threshold Parameter screen - FDESC02 - High percentage of Variance per share check Multifonds DB Column is HIGH_PCT. |
| 16 | `FS.GA.NAV.EXCEPTION.THRESHOLD.LOW.VARIANCE.PERCENT` | `FsGaNavExceptionThreshold_LowVariancePercent` | TField |  | It refers to Threshold filed in Exception Threshold Parameter screen - FDESC02 - Low percentage of Variance per share check Multifonds DB Column is LOW_PCT. |
| 17 | `FS.GA.NAV.EXCEPTION.THRESHOLD.ID.CODE` | `FsGaNavExceptionThreshold_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 18 | `FS.GA.NAV.EXCEPTION.THRESHOLD.MANAGER.CODE` | `FsGaNavExceptionThreshold_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 19 | `FS.GA.NAV.EXCEPTION.THRESHOLD.JUSTIFICATION.SOURCE` | `FsGaNavExceptionThreshold_JustificationSource` | TField |  | Justification Source Multifonds DB Column is JUSTI_SOURCE. |
| 20 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED10` | `FsGaNavExceptionThreshold_Reserved10` | TField |  |  |
| 21 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED9` | `FsGaNavExceptionThreshold_Reserved9` | TField |  |  |
| 22 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED8` | `FsGaNavExceptionThreshold_Reserved8` | TField |  |  |
| 23 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED7` | `FsGaNavExceptionThreshold_Reserved7` | TField |  |  |
| 24 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED6` | `FsGaNavExceptionThreshold_Reserved6` | TField |  |  |
| 25 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED5` | `FsGaNavExceptionThreshold_Reserved5` | TField |  |  |
| 26 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED4` | `FsGaNavExceptionThreshold_Reserved4` | TField |  |  |
| 27 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED3` | `FsGaNavExceptionThreshold_Reserved3` | TField |  |  |
| 28 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED2` | `FsGaNavExceptionThreshold_Reserved2` | TField |  |  |
| 29 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RESERVED1` | `FsGaNavExceptionThreshold_Reserved1` | TField |  |  |
| 30 | `FS.GA.NAV.EXCEPTION.THRESHOLD.LOCAL.REF` | `FsGaNavExceptionThreshold_LocalRef` |  |  |  |
| 31 | `FS.GA.NAV.EXCEPTION.THRESHOLD.OVERRIDE` | `FsGaNavExceptionThreshold_Override` |  |  |  |
| 32 | `FS.GA.NAV.EXCEPTION.THRESHOLD.RECORD.STATUS` | `FsGaNavExceptionThreshold_RecordStatus` | String |  |  |
| 33 | `FS.GA.NAV.EXCEPTION.THRESHOLD.CURR.NO` | `FsGaNavExceptionThreshold_CurrNo` | String |  |  |
| 34 | `FS.GA.NAV.EXCEPTION.THRESHOLD.INPUTTER` | `FsGaNavExceptionThreshold_Inputter` |  |  |  |
| 35 | `FS.GA.NAV.EXCEPTION.THRESHOLD.DATE.TIME` | `FsGaNavExceptionThreshold_DateTime` |  |  |  |
| 36 | `FS.GA.NAV.EXCEPTION.THRESHOLD.AUTHORISER` | `FsGaNavExceptionThreshold_Authoriser` | String |  |  |
| 37 | `FS.GA.NAV.EXCEPTION.THRESHOLD.CO.CODE` | `FsGaNavExceptionThreshold_CoCode` | String |  |  |
| 38 | `FS.GA.NAV.EXCEPTION.THRESHOLD.DEPT.CODE` | `FsGaNavExceptionThreshold_DeptCode` | String |  |  |
| 39 | `FS.GA.NAV.EXCEPTION.THRESHOLD.AUDITOR.CODE` | `FsGaNavExceptionThreshold_AuditorCode` | String |  |  |
| 40 | `FS.GA.NAV.EXCEPTION.THRESHOLD.AUDIT.DATE.TIME` | `FsGaNavExceptionThreshold_AuditDateTime` | String |  |  |
