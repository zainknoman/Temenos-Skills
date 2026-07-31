# FS.GA.MULTICLASS.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.MULTICLASS.GROUP` in `FS_FundMasterAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MULTICLASS.GROUP.PARENT.REF.ID` | `FsGaMulticlassGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.MULTICLASS.GROUP.ORA.ROWID` | `FsGaMulticlassGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.MULTICLASS.GROUP.FUND.ID` | `FsGaMulticlassGroup_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.MULTICLASS.GROUP.MULTICLASS.CODE.TYPE` | `FsGaMulticlassGroup_MulticlassCodeType` | TField |  | Funds are applicable for muliple share classes or plans, produces multiple NAVs per class within the fund.Different codes are available, most generally used is Multiclass 2. Multifonds DB Column is CODE_MULTICLASS. |
| 5 | `FS.GA.MULTICLASS.GROUP.SHARE.CLASS.CODE` | `FsGaMulticlassGroup_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 6 | `FS.GA.MULTICLASS.GROUP.ACC.TYPE.CODE` | `FsGaMulticlassGroup_AccTypeCode` | TField |  | Account type code like with fee or without fee. Generally set up as With Fee 1 Multifonds DB Column is ACC_TYPE. |
| 7 | `FS.GA.MULTICLASS.GROUP.RESERVED10` | `FsGaMulticlassGroup_Reserved10` | TField |  |  |
| 8 | `FS.GA.MULTICLASS.GROUP.RESERVED9` | `FsGaMulticlassGroup_Reserved9` | TField |  |  |
| 9 | `FS.GA.MULTICLASS.GROUP.RESERVED8` | `FsGaMulticlassGroup_Reserved8` | TField |  |  |
| 10 | `FS.GA.MULTICLASS.GROUP.RESERVED7` | `FsGaMulticlassGroup_Reserved7` | TField |  |  |
| 11 | `FS.GA.MULTICLASS.GROUP.RESERVED6` | `FsGaMulticlassGroup_Reserved6` | TField |  |  |
| 12 | `FS.GA.MULTICLASS.GROUP.RESERVED5` | `FsGaMulticlassGroup_Reserved5` | TField |  |  |
| 13 | `FS.GA.MULTICLASS.GROUP.RESERVED4` | `FsGaMulticlassGroup_Reserved4` | TField |  |  |
| 14 | `FS.GA.MULTICLASS.GROUP.RESERVED3` | `FsGaMulticlassGroup_Reserved3` | TField |  |  |
| 15 | `FS.GA.MULTICLASS.GROUP.RESERVED2` | `FsGaMulticlassGroup_Reserved2` | TField |  |  |
| 16 | `FS.GA.MULTICLASS.GROUP.RESERVED1` | `FsGaMulticlassGroup_Reserved1` | TField |  |  |
| 17 | `FS.GA.MULTICLASS.GROUP.LOCAL.REF` | `FsGaMulticlassGroup_LocalRef` |  |  |  |
| 18 | `FS.GA.MULTICLASS.GROUP.OVERRIDE` | `FsGaMulticlassGroup_Override` |  |  |  |
| 19 | `FS.GA.MULTICLASS.GROUP.RECORD.STATUS` | `FsGaMulticlassGroup_RecordStatus` | String |  |  |
| 20 | `FS.GA.MULTICLASS.GROUP.CURR.NO` | `FsGaMulticlassGroup_CurrNo` | String |  |  |
| 21 | `FS.GA.MULTICLASS.GROUP.INPUTTER` | `FsGaMulticlassGroup_Inputter` |  |  |  |
| 22 | `FS.GA.MULTICLASS.GROUP.DATE.TIME` | `FsGaMulticlassGroup_DateTime` |  |  |  |
| 23 | `FS.GA.MULTICLASS.GROUP.AUTHORISER` | `FsGaMulticlassGroup_Authoriser` | String |  |  |
| 24 | `FS.GA.MULTICLASS.GROUP.CO.CODE` | `FsGaMulticlassGroup_CoCode` | String |  |  |
| 25 | `FS.GA.MULTICLASS.GROUP.DEPT.CODE` | `FsGaMulticlassGroup_DeptCode` | String |  |  |
| 26 | `FS.GA.MULTICLASS.GROUP.AUDITOR.CODE` | `FsGaMulticlassGroup_AuditorCode` | String |  |  |
| 27 | `FS.GA.MULTICLASS.GROUP.AUDIT.DATE.TIME` | `FsGaMulticlassGroup_AuditDateTime` | String |  |  |
