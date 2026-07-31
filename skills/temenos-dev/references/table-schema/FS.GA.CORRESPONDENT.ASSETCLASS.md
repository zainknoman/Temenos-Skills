# FS.GA.CORRESPONDENT.ASSETCLASS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.ASSETCLASS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORRESPONDENT.ASSETCLASS.CORRESPONDENT` | `FsGaCorrespondentAssetclass_Correspondent` | TField |  | Correspondent Multifonds DB Column is NCORRESP. |
| 2 | `CORRESPONDENT.ASSETCLASS.DERIVATIVE.TYPE` | `FsGaCorrespondentAssetclass_DerivativeType` | TField |  | Derivative Type Multifonds DB Column is CGTI. |
| 3 | `CORRESPONDENT.ASSETCLASS.MARGIN.GL.ACCOUNT` | `FsGaCorrespondentAssetclass_MarginGlAccount` | TField |  | Margin GL Account Multifonds DB Column is NRUBR_MARG. |
| 4 | `CORRESPONDENT.ASSETCLASS.MARGIN.SUFFIX.ACCOUNT` | `FsGaCorrespondentAssetclass_MarginSuffixAccount` | TField |  | Margin Suffix Account Multifonds DB Column is NSUFF_MARG. |
| 5 | `CORRESPONDENT.ASSETCLASS.DWH.EXPORT` | `FsGaCorrespondentAssetclass_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 6 | `CORRESPONDENT.ASSETCLASS.RECORD.STATUS` | `FsGaCorrespondentAssetclass_RecordStatus` | String |  |  |
| 7 | `CORRESPONDENT.ASSETCLASS.CURR.NO` | `FsGaCorrespondentAssetclass_CurrNo` | String |  |  |
| 8 | `CORRESPONDENT.ASSETCLASS.INPUTTER` | `FsGaCorrespondentAssetclass_Inputter` |  |  |  |
| 9 | `CORRESPONDENT.ASSETCLASS.DATE.TIME` | `FsGaCorrespondentAssetclass_DateTime` |  |  |  |
| 10 | `CORRESPONDENT.ASSETCLASS.AUTHORISER` | `FsGaCorrespondentAssetclass_Authoriser` | String |  |  |
| 11 | `CORRESPONDENT.ASSETCLASS.CO.CODE` | `FsGaCorrespondentAssetclass_CoCode` | String |  |  |
| 12 | `CORRESPONDENT.ASSETCLASS.DEPT.CODE` | `FsGaCorrespondentAssetclass_DeptCode` | String |  |  |
| 13 | `CORRESPONDENT.ASSETCLASS.AUDITOR.CODE` | `FsGaCorrespondentAssetclass_AuditorCode` | String |  |  |
| 14 | `CORRESPONDENT.ASSETCLASS.AUDIT.DATE.TIME` | `FsGaCorrespondentAssetclass_AuditDateTime` | String |  |  |
