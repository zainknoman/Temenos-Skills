# FS.GI.REFERENCE.NAV.CALC.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.REFERENCE.NAV.CALC.PROCESS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.PARENT.REF.ID` | `FsGiReferenceNavCalcProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.ORA.ROWID` | `FsGiReferenceNavCalcProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.HWM.VALUE` | `FsGiReferenceNavCalcProcess_HwmValue` | TField |  | HWM value. Multifonds DB Column is P_COURSVAL_HWM. |
| 4 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.BENCHMARK.VALUE` | `FsGiReferenceNavCalcProcess_BenchmarkValue` | TField |  | Benchmark value. Multifonds DB Column is P_COURSVAL_BMK. |
| 5 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.HURDLE.ADJUSTED.HWM.VALUE` | `FsGiReferenceNavCalcProcess_HurdleAdjustedHwmValue` | TField |  | Hurdle adjusted HWM value. Multifonds DB Column is P_HURDLE_ADJ_HWM. |
| 6 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.REFERENCE.NAV.VALUE` | `FsGiReferenceNavCalcProcess_ReferenceNavValue` | TField |  | Reference NAV value. Multifonds DB Column is P_COURSVAL. |
| 7 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED10` | `FsGiReferenceNavCalcProcess_Reserved10` | TField |  |  |
| 8 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED9` | `FsGiReferenceNavCalcProcess_Reserved9` | TField |  |  |
| 9 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED8` | `FsGiReferenceNavCalcProcess_Reserved8` | TField |  |  |
| 10 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED7` | `FsGiReferenceNavCalcProcess_Reserved7` | TField |  |  |
| 11 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED6` | `FsGiReferenceNavCalcProcess_Reserved6` | TField |  |  |
| 12 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED5` | `FsGiReferenceNavCalcProcess_Reserved5` | TField |  |  |
| 13 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED4` | `FsGiReferenceNavCalcProcess_Reserved4` | TField |  |  |
| 14 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED3` | `FsGiReferenceNavCalcProcess_Reserved3` | TField |  |  |
| 15 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED2` | `FsGiReferenceNavCalcProcess_Reserved2` | TField |  |  |
| 16 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RESERVED1` | `FsGiReferenceNavCalcProcess_Reserved1` | TField |  |  |
| 17 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.LOCAL.REF` | `FsGiReferenceNavCalcProcess_LocalRef` |  |  |  |
| 18 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.OVERRIDE` | `FsGiReferenceNavCalcProcess_Override` |  |  |  |
| 19 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.RECORD.STATUS` | `FsGiReferenceNavCalcProcess_RecordStatus` | String |  |  |
| 20 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.CURR.NO` | `FsGiReferenceNavCalcProcess_CurrNo` | String |  |  |
| 21 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.INPUTTER` | `FsGiReferenceNavCalcProcess_Inputter` |  |  |  |
| 22 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.DATE.TIME` | `FsGiReferenceNavCalcProcess_DateTime` |  |  |  |
| 23 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.AUTHORISER` | `FsGiReferenceNavCalcProcess_Authoriser` | String |  |  |
| 24 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.CO.CODE` | `FsGiReferenceNavCalcProcess_CoCode` | String |  |  |
| 25 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.DEPT.CODE` | `FsGiReferenceNavCalcProcess_DeptCode` | String |  |  |
| 26 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.AUDITOR.CODE` | `FsGiReferenceNavCalcProcess_AuditorCode` | String |  |  |
| 27 | `FS.GI.REFERENCE.NAV.CALC.PROCESS.AUDIT.DATE.TIME` | `FsGiReferenceNavCalcProcess_AuditDateTime` | String |  |  |
