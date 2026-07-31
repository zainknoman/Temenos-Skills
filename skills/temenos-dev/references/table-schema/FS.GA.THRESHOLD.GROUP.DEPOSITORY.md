# FS.GA.THRESHOLD.GROUP.DEPOSITORY — Table Schema

> Source: `INSERTS/I_F.FS.GA.THRESHOLD.GROUP.DEPOSITORY` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.PARENT.REF.ID` | `FsGaThresholdGroupDepository_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.ORA.ROWID` | `FsGaThresholdGroupDepository_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.CONTROL.NUMBER` | `FsGaThresholdGroupDepository_ControlNumber` | TField |  | Control Number linked to Process Multifonds DB Column is TYP_CONTROLE. |
| 4 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.SEQUENCE.NO` | `FsGaThresholdGroupDepository_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 5 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.GROUP.OF.DEPOSITORY` | `FsGaThresholdGroupDepository_GroupOfDepository` | TField |  | Group of Depository Multifonds DB Column is GRP_DEPOSI. |
| 6 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.CUSTODIAN` | `FsGaThresholdGroupDepository_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 7 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED10` | `FsGaThresholdGroupDepository_Reserved10` | TField |  |  |
| 8 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED9` | `FsGaThresholdGroupDepository_Reserved9` | TField |  |  |
| 9 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED8` | `FsGaThresholdGroupDepository_Reserved8` | TField |  |  |
| 10 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED7` | `FsGaThresholdGroupDepository_Reserved7` | TField |  |  |
| 11 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED6` | `FsGaThresholdGroupDepository_Reserved6` | TField |  |  |
| 12 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED5` | `FsGaThresholdGroupDepository_Reserved5` | TField |  |  |
| 13 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED4` | `FsGaThresholdGroupDepository_Reserved4` | TField |  |  |
| 14 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED3` | `FsGaThresholdGroupDepository_Reserved3` | TField |  |  |
| 15 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED2` | `FsGaThresholdGroupDepository_Reserved2` | TField |  |  |
| 16 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RESERVED1` | `FsGaThresholdGroupDepository_Reserved1` | TField |  |  |
| 17 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.LOCAL.REF` | `FsGaThresholdGroupDepository_LocalRef` |  |  |  |
| 18 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.OVERRIDE` | `FsGaThresholdGroupDepository_Override` |  |  |  |
| 19 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.RECORD.STATUS` | `FsGaThresholdGroupDepository_RecordStatus` | String |  |  |
| 20 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.CURR.NO` | `FsGaThresholdGroupDepository_CurrNo` | String |  |  |
| 21 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.INPUTTER` | `FsGaThresholdGroupDepository_Inputter` |  |  |  |
| 22 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.DATE.TIME` | `FsGaThresholdGroupDepository_DateTime` |  |  |  |
| 23 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.AUTHORISER` | `FsGaThresholdGroupDepository_Authoriser` | String |  |  |
| 24 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.CO.CODE` | `FsGaThresholdGroupDepository_CoCode` | String |  |  |
| 25 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.DEPT.CODE` | `FsGaThresholdGroupDepository_DeptCode` | String |  |  |
| 26 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.AUDITOR.CODE` | `FsGaThresholdGroupDepository_AuditorCode` | String |  |  |
| 27 | `FS.GA.THRESHOLD.GROUP.DEPOSITORY.AUDIT.DATE.TIME` | `FsGaThresholdGroupDepository_AuditDateTime` | String |  |  |
