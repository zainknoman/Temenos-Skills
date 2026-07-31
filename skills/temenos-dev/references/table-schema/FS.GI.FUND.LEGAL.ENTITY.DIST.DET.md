# FS.GI.FUND.LEGAL.ENTITY.DIST.DET — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.LEGAL.ENTITY.DIST.DET` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.PARENT.REF.ID` | `FsGiFundLegalEntityDistDet_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.ORA.ROWID` | `FsGiFundLegalEntityDistDet_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.LEGAL.ENTITY.ID` | `FsGiFundLegalEntityDistDet_LegalEntityId` | TField |  | Legal Entity internal ID. Multifonds DB Column is NTFC. |
| 4 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.FX.INPUT` | `FsGiFundLegalEntityDistDet_FxInput` | TField |  | It specifies if the dividend distribution FX input can be entered manually and/or through interface. Multifonds DB Column is FX_INPUT. |
| 5 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.FX.EXPORT` | `FsGiFundLegalEntityDistDet_FxExport` | TField |  | It spcifies if the dividend distribution FX reports can be generated individually or bulked. Multifonds DB Column is FX_EXPORT. |
| 6 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.FX.REVERSAL` | `FsGiFundLegalEntityDistDet_FxReversal` | TField |  | It allows to activate or deactivate FX automatic reversal process (posting of opposite FX, P&amp;L calculation). Multifonds DB Column is FX_REVERSAL. |
| 7 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED10` | `FsGiFundLegalEntityDistDet_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED9` | `FsGiFundLegalEntityDistDet_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED8` | `FsGiFundLegalEntityDistDet_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED7` | `FsGiFundLegalEntityDistDet_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED6` | `FsGiFundLegalEntityDistDet_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED5` | `FsGiFundLegalEntityDistDet_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED4` | `FsGiFundLegalEntityDistDet_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED3` | `FsGiFundLegalEntityDistDet_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED2` | `FsGiFundLegalEntityDistDet_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RESERVED1` | `FsGiFundLegalEntityDistDet_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.LOCAL.REF` | `FsGiFundLegalEntityDistDet_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.OVERRIDE` | `FsGiFundLegalEntityDistDet_Override` |  |  |  |
| 19 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.RECORD.STATUS` | `FsGiFundLegalEntityDistDet_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.CURR.NO` | `FsGiFundLegalEntityDistDet_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.INPUTTER` | `FsGiFundLegalEntityDistDet_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.DATE.TIME` | `FsGiFundLegalEntityDistDet_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.AUTHORISER` | `FsGiFundLegalEntityDistDet_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.CO.CODE` | `FsGiFundLegalEntityDistDet_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.DEPT.CODE` | `FsGiFundLegalEntityDistDet_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.AUDITOR.CODE` | `FsGiFundLegalEntityDistDet_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.LEGAL.ENTITY.DIST.DET.AUDIT.DATE.TIME` | `FsGiFundLegalEntityDistDet_AuditDateTime` | String |  |  |
