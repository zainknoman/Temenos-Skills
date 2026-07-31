# FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.PARENT.REF.ID` | `FsGiFundLegalEntityFxExExcep_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.ORA.ROWID` | `FsGiFundLegalEntityFxExExcep_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.LEGAL.ENTITY.ID` | `FsGiFundLegalEntityFxExExcep_LegalEntityId` | TField |  | Legal Entity internal ID. Multifonds DB Column is NTFC. |
| 4 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.OPERATION.CODE` | `FsGiFundLegalEntityFxExExcep_OperationCode` | TField |  | Operation code excluded for FX exporting. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED10` | `FsGiFundLegalEntityFxExExcep_Reserved10` | TField |  |  |
| 6 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED9` | `FsGiFundLegalEntityFxExExcep_Reserved9` | TField |  |  |
| 7 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED8` | `FsGiFundLegalEntityFxExExcep_Reserved8` | TField |  |  |
| 8 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED7` | `FsGiFundLegalEntityFxExExcep_Reserved7` | TField |  |  |
| 9 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED6` | `FsGiFundLegalEntityFxExExcep_Reserved6` | TField |  |  |
| 10 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED5` | `FsGiFundLegalEntityFxExExcep_Reserved5` | TField |  |  |
| 11 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED4` | `FsGiFundLegalEntityFxExExcep_Reserved4` | TField |  |  |
| 12 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED3` | `FsGiFundLegalEntityFxExExcep_Reserved3` | TField |  |  |
| 13 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED2` | `FsGiFundLegalEntityFxExExcep_Reserved2` | TField |  |  |
| 14 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RESERVED1` | `FsGiFundLegalEntityFxExExcep_Reserved1` | TField |  |  |
| 15 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.LOCAL.REF` | `FsGiFundLegalEntityFxExExcep_LocalRef` |  |  |  |
| 16 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.OVERRIDE` | `FsGiFundLegalEntityFxExExcep_Override` |  |  |  |
| 17 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.RECORD.STATUS` | `FsGiFundLegalEntityFxExExcep_RecordStatus` | String |  |  |
| 18 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.CURR.NO` | `FsGiFundLegalEntityFxExExcep_CurrNo` | String |  |  |
| 19 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.INPUTTER` | `FsGiFundLegalEntityFxExExcep_Inputter` |  |  |  |
| 20 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.DATE.TIME` | `FsGiFundLegalEntityFxExExcep_DateTime` |  |  |  |
| 21 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.AUTHORISER` | `FsGiFundLegalEntityFxExExcep_Authoriser` | String |  |  |
| 22 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.CO.CODE` | `FsGiFundLegalEntityFxExExcep_CoCode` | String |  |  |
| 23 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.DEPT.CODE` | `FsGiFundLegalEntityFxExExcep_DeptCode` | String |  |  |
| 24 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.AUDITOR.CODE` | `FsGiFundLegalEntityFxExExcep_AuditorCode` | String |  |  |
| 25 | `FS.GI.FUND.LEGAL.ENTITY.FX.EX.EXCEP.AUDIT.DATE.TIME` | `FsGiFundLegalEntityFxExExcep_AuditDateTime` | String |  |  |
