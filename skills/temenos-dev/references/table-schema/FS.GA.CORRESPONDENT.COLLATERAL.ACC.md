# FS.GA.CORRESPONDENT.COLLATERAL.ACC — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.COLLATERAL.ACC` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.PARENT.REF.ID` | `FsGaCorrespondentCollateralAcc_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.ORA.ROWID` | `FsGaCorrespondentCollateralAcc_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.CORRESPONDENT` | `FsGaCorrespondentCollateralAcc_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.GL.ACCOUNT` | `FsGaCorrespondentCollateralAcc_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.GL.ACCOUNT.SUFFIX` | `FsGaCorrespondentCollateralAcc_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 6 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.CPT.TYPE` | `FsGaCorrespondentCollateralAcc_CptType` | TField |  | CPT Type Multifonds DB Column is TYPE_CPT. |
| 7 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.GFDB.CC` | `FsGaCorrespondentCollateralAcc_GfdbCc` | TField |  | GFDB CC Multifonds DB Column is FLG_GFDB_CC. |
| 8 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.CHART.OF.ACCOUNTS.CODE` | `FsGaCorrespondentCollateralAcc_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 9 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED10` | `FsGaCorrespondentCollateralAcc_Reserved10` | TField |  |  |
| 10 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED9` | `FsGaCorrespondentCollateralAcc_Reserved9` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED8` | `FsGaCorrespondentCollateralAcc_Reserved8` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED7` | `FsGaCorrespondentCollateralAcc_Reserved7` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED6` | `FsGaCorrespondentCollateralAcc_Reserved6` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED5` | `FsGaCorrespondentCollateralAcc_Reserved5` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED4` | `FsGaCorrespondentCollateralAcc_Reserved4` | TField |  |  |
| 16 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED3` | `FsGaCorrespondentCollateralAcc_Reserved3` | TField |  |  |
| 17 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED2` | `FsGaCorrespondentCollateralAcc_Reserved2` | TField |  |  |
| 18 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RESERVED1` | `FsGaCorrespondentCollateralAcc_Reserved1` | TField |  |  |
| 19 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.LOCAL.REF` | `FsGaCorrespondentCollateralAcc_LocalRef` |  |  |  |
| 20 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.OVERRIDE` | `FsGaCorrespondentCollateralAcc_Override` |  |  |  |
| 21 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.RECORD.STATUS` | `FsGaCorrespondentCollateralAcc_RecordStatus` | String |  |  |
| 22 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.CURR.NO` | `FsGaCorrespondentCollateralAcc_CurrNo` | String |  |  |
| 23 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.INPUTTER` | `FsGaCorrespondentCollateralAcc_Inputter` |  |  |  |
| 24 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.DATE.TIME` | `FsGaCorrespondentCollateralAcc_DateTime` |  |  |  |
| 25 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.AUTHORISER` | `FsGaCorrespondentCollateralAcc_Authoriser` | String |  |  |
| 26 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.CO.CODE` | `FsGaCorrespondentCollateralAcc_CoCode` | String |  |  |
| 27 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.DEPT.CODE` | `FsGaCorrespondentCollateralAcc_DeptCode` | String |  |  |
| 28 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.AUDITOR.CODE` | `FsGaCorrespondentCollateralAcc_AuditorCode` | String |  |  |
| 29 | `FS.GA.CORRESPONDENT.COLLATERAL.ACC.AUDIT.DATE.TIME` | `FsGaCorrespondentCollateralAcc_AuditDateTime` | String |  |  |
