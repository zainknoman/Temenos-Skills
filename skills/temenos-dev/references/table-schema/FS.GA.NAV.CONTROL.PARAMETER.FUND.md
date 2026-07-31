# FS.GA.NAV.CONTROL.PARAMETER.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CONTROL.PARAMETER.FUND` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.PARENT.REF.ID` | `FsGaNavControlParameterFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.ORA.ROWID` | `FsGaNavControlParameterFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.FUND.ID` | `FsGaNavControlParameterFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.SEQUENCE.NO` | `FsGaNavControlParameterFund_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 5 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.TARGET.VARIATION` | `FsGaNavControlParameterFund_TargetVariation` | TField |  | Applc for control 0020. The no of days of var between NAV date and last price date of the tax fig should be defined in the &apos;Target Variation&apos; field which the error type gets triggered on NAV sim. Multifonds DB Column is TARGET_VARIATION. |
| 6 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.NAV.GROUP.CODE` | `FsGaNavControlParameterFund_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 7 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.UNSWUNG.NAV` | `FsGaNavControlParameterFund_UnswungNav` | TField |  | Applicable for control 0103(Text upon benchmark breach). If the field unswung is selected the system compares between the benchmark and unswung NAV else compares between the benchmark and swung NAV Multifonds DB Column is FLG_UNSWUNG. |
| 8 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED10` | `FsGaNavControlParameterFund_Reserved10` | TField |  |  |
| 9 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED9` | `FsGaNavControlParameterFund_Reserved9` | TField |  |  |
| 10 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED8` | `FsGaNavControlParameterFund_Reserved8` | TField |  |  |
| 11 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED7` | `FsGaNavControlParameterFund_Reserved7` | TField |  |  |
| 12 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED6` | `FsGaNavControlParameterFund_Reserved6` | TField |  |  |
| 13 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED5` | `FsGaNavControlParameterFund_Reserved5` | TField |  |  |
| 14 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED4` | `FsGaNavControlParameterFund_Reserved4` | TField |  |  |
| 15 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED3` | `FsGaNavControlParameterFund_Reserved3` | TField |  |  |
| 16 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED2` | `FsGaNavControlParameterFund_Reserved2` | TField |  |  |
| 17 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RESERVED1` | `FsGaNavControlParameterFund_Reserved1` | TField |  |  |
| 18 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.LOCAL.REF` | `FsGaNavControlParameterFund_LocalRef` |  |  |  |
| 19 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.OVERRIDE` | `FsGaNavControlParameterFund_Override` |  |  |  |
| 20 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.RECORD.STATUS` | `FsGaNavControlParameterFund_RecordStatus` | String |  |  |
| 21 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.CURR.NO` | `FsGaNavControlParameterFund_CurrNo` | String |  |  |
| 22 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.INPUTTER` | `FsGaNavControlParameterFund_Inputter` |  |  |  |
| 23 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.DATE.TIME` | `FsGaNavControlParameterFund_DateTime` |  |  |  |
| 24 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.AUTHORISER` | `FsGaNavControlParameterFund_Authoriser` | String |  |  |
| 25 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.CO.CODE` | `FsGaNavControlParameterFund_CoCode` | String |  |  |
| 26 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.DEPT.CODE` | `FsGaNavControlParameterFund_DeptCode` | String |  |  |
| 27 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.AUDITOR.CODE` | `FsGaNavControlParameterFund_AuditorCode` | String |  |  |
| 28 | `FS.GA.NAV.CONTROL.PARAMETER.FUND.AUDIT.DATE.TIME` | `FsGaNavControlParameterFund_AuditDateTime` | String |  |  |
