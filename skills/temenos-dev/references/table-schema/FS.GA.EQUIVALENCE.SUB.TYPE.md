# FS.GA.EQUIVALENCE.SUB.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.SUB.TYPE` in `FS_AccountingSchema.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.SUB.TYPE.PARENT.REF.ID` | `FsGaEquivalenceSubType_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.SUB.TYPE.ORA.ROWID` | `FsGaEquivalenceSubType_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.SUB.TYPE.CHART.OF.ACCOUNTS.CODE` | `FsGaEquivalenceSubType_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.EQUIVALENCE.SUB.TYPE.SERVICE.CODE` | `FsGaEquivalenceSubType_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.EQUIVALENCE.SUB.TYPE.EQUIVALENCE.SUB.TYPE.IML` | `FsGaEquivalenceSubType_EquivalenceSubTypeIml` | TField |  | Display required element from CMESS table SUB_TYPE The equiv between SUB_TYPE and TPARTS for service code (eg NA) results in entries getting posted to the class specific share classes Multifonds DB Column is EQUI_CTABLE. |
| 6 | `FS.GA.EQUIVALENCE.SUB.TYPE.IFRS.CATEGORY` | `FsGaEquivalenceSubType_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 7 | `FS.GA.EQUIVALENCE.SUB.TYPE.REFERENCE.TABLE.IML.SUB.TYPE` | `FsGaEquivalenceSubType_ReferenceTableImlSubType` | TField |  | User links the corresp share class TPARTS for a chart of accounts If there is no equiv between SUB_TYPE and TPARTS for service code (eg NA), there will be no expenses which are class specific Multifonds DB Column is REF_CTABLE. |
| 8 | `FS.GA.EQUIVALENCE.SUB.TYPE.SHARE.CLASS.CODE` | `FsGaEquivalenceSubType_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 9 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED10` | `FsGaEquivalenceSubType_Reserved10` | TField |  |  |
| 10 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED9` | `FsGaEquivalenceSubType_Reserved9` | TField |  |  |
| 11 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED8` | `FsGaEquivalenceSubType_Reserved8` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED7` | `FsGaEquivalenceSubType_Reserved7` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED6` | `FsGaEquivalenceSubType_Reserved6` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED5` | `FsGaEquivalenceSubType_Reserved5` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED4` | `FsGaEquivalenceSubType_Reserved4` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED3` | `FsGaEquivalenceSubType_Reserved3` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED2` | `FsGaEquivalenceSubType_Reserved2` | TField |  |  |
| 18 | `FS.GA.EQUIVALENCE.SUB.TYPE.RESERVED1` | `FsGaEquivalenceSubType_Reserved1` | TField |  |  |
| 19 | `FS.GA.EQUIVALENCE.SUB.TYPE.LOCAL.REF` | `FsGaEquivalenceSubType_LocalRef` |  |  |  |
| 20 | `FS.GA.EQUIVALENCE.SUB.TYPE.OVERRIDE` | `FsGaEquivalenceSubType_Override` |  |  |  |
| 21 | `FS.GA.EQUIVALENCE.SUB.TYPE.RECORD.STATUS` | `FsGaEquivalenceSubType_RecordStatus` | String |  |  |
| 22 | `FS.GA.EQUIVALENCE.SUB.TYPE.CURR.NO` | `FsGaEquivalenceSubType_CurrNo` | String |  |  |
| 23 | `FS.GA.EQUIVALENCE.SUB.TYPE.INPUTTER` | `FsGaEquivalenceSubType_Inputter` |  |  |  |
| 24 | `FS.GA.EQUIVALENCE.SUB.TYPE.DATE.TIME` | `FsGaEquivalenceSubType_DateTime` |  |  |  |
| 25 | `FS.GA.EQUIVALENCE.SUB.TYPE.AUTHORISER` | `FsGaEquivalenceSubType_Authoriser` | String |  |  |
| 26 | `FS.GA.EQUIVALENCE.SUB.TYPE.CO.CODE` | `FsGaEquivalenceSubType_CoCode` | String |  |  |
| 27 | `FS.GA.EQUIVALENCE.SUB.TYPE.DEPT.CODE` | `FsGaEquivalenceSubType_DeptCode` | String |  |  |
| 28 | `FS.GA.EQUIVALENCE.SUB.TYPE.AUDITOR.CODE` | `FsGaEquivalenceSubType_AuditorCode` | String |  |  |
| 29 | `FS.GA.EQUIVALENCE.SUB.TYPE.AUDIT.DATE.TIME` | `FsGaEquivalenceSubType_AuditDateTime` | String |  |  |
