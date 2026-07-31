# FS.GA.EXCEPTION.THRESHOLD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.EXCEPTION.THRESHOLD.PARAMETER` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.PARENT.REF.ID` | `FsGaExceptionThresholdParameter_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.ORA.ROWID` | `FsGaExceptionThresholdParameter_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.GROUP.OF.ACCOUNT` | `FsGaExceptionThresholdParameter_GroupOfAccount` | TField |  | Groups which are created in the Group of account button is parameterized in this field. Every single account included in the group of account are subject to control. Multifonds DB Column is GROUP_NRUBR. |
| 4 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.FROM.ACCOUNT` | `FsGaExceptionThresholdParameter_FromAccount` | TField |  | If the user want to make a control on all the inc acc then user could set-up a control on a group of acc composed by all the account starting with 5, user can set up a group from 500000 to 599999. Multifonds DB Column is NRUBR_FROM. |
| 5 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.TO.ACCOUNT` | `FsGaExceptionThresholdParameter_ToAccount` | TField |  | If the user want to make a control on all the inc acc then user could set-up a control on a grp of account composed by all the account starting with 5, user can set up a group from 500000 to 599999. Multifonds DB Column is NRUBR_TO. |
| 6 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.SUFFIX.NUMBER.FROM` | `FsGaExceptionThresholdParameter_SuffixNumberFrom` | TField |  | Account Suffix Number Minimum Multifonds DB Column is NSUFF_FROM. |
| 7 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.SUFFIX.NUMBER.TO` | `FsGaExceptionThresholdParameter_SuffixNumberTo` | TField |  | Account Suffix Number Maximum Multifonds DB Column is NSUFF_TO. |
| 8 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.SEQUENCE.NO` | `FsGaExceptionThresholdParameter_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 9 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.LOCAL.CURRENCY` | `FsGaExceptionThresholdParameter_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 10 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED10` | `FsGaExceptionThresholdParameter_Reserved10` | TField |  |  |
| 11 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED9` | `FsGaExceptionThresholdParameter_Reserved9` | TField |  |  |
| 12 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED8` | `FsGaExceptionThresholdParameter_Reserved8` | TField |  |  |
| 13 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED7` | `FsGaExceptionThresholdParameter_Reserved7` | TField |  |  |
| 14 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED6` | `FsGaExceptionThresholdParameter_Reserved6` | TField |  |  |
| 15 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED5` | `FsGaExceptionThresholdParameter_Reserved5` | TField |  |  |
| 16 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED4` | `FsGaExceptionThresholdParameter_Reserved4` | TField |  |  |
| 17 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED3` | `FsGaExceptionThresholdParameter_Reserved3` | TField |  |  |
| 18 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED2` | `FsGaExceptionThresholdParameter_Reserved2` | TField |  |  |
| 19 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RESERVED1` | `FsGaExceptionThresholdParameter_Reserved1` | TField |  |  |
| 20 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.LOCAL.REF` | `FsGaExceptionThresholdParameter_LocalRef` |  |  |  |
| 21 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.OVERRIDE` | `FsGaExceptionThresholdParameter_Override` |  |  |  |
| 22 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.RECORD.STATUS` | `FsGaExceptionThresholdParameter_RecordStatus` | String |  |  |
| 23 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.CURR.NO` | `FsGaExceptionThresholdParameter_CurrNo` | String |  |  |
| 24 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.INPUTTER` | `FsGaExceptionThresholdParameter_Inputter` |  |  |  |
| 25 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.DATE.TIME` | `FsGaExceptionThresholdParameter_DateTime` |  |  |  |
| 26 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.AUTHORISER` | `FsGaExceptionThresholdParameter_Authoriser` | String |  |  |
| 27 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.CO.CODE` | `FsGaExceptionThresholdParameter_CoCode` | String |  |  |
| 28 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.DEPT.CODE` | `FsGaExceptionThresholdParameter_DeptCode` | String |  |  |
| 29 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.AUDITOR.CODE` | `FsGaExceptionThresholdParameter_AuditorCode` | String |  |  |
| 30 | `FS.GA.EXCEPTION.THRESHOLD.PARAMETER.AUDIT.DATE.TIME` | `FsGaExceptionThresholdParameter_AuditDateTime` | String |  |  |
