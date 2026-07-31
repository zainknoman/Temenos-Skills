# FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.PARENT.REF.ID` | `FsGiFundAccrualAdjustmentParam_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.ORA.ROWID` | `FsGiFundAccrualAdjustmentParam_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.TA.FUND.ID` | `FsGiFundAccrualAdjustmentParam_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.SHARE.CLASS.CODE` | `FsGiFundAccrualAdjustmentParam_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.OPERATION.CODE` | `FsGiFundAccrualAdjustmentParam_OperationCode` | TField |  | Transaction type in scope of the accrual calculation. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.ACCRUAL.ADJUSTMENT.DAYS` | `FsGiFundAccrualAdjustmentParam_AccrualAdjustmentDays` | TField |  | Number of days to be delayed from trade date for Accrual calculation. Multifonds DB Column is ACCRUAL_ADJUST_DAYS. |
| 7 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.FUND.ID` | `FsGiFundAccrualAdjustmentParam_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.CLASS.CURRENCY` | `FsGiFundAccrualAdjustmentParam_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED10` | `FsGiFundAccrualAdjustmentParam_Reserved10` | TField |  |  |
| 10 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED9` | `FsGiFundAccrualAdjustmentParam_Reserved9` | TField |  |  |
| 11 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED8` | `FsGiFundAccrualAdjustmentParam_Reserved8` | TField |  |  |
| 12 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED7` | `FsGiFundAccrualAdjustmentParam_Reserved7` | TField |  |  |
| 13 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED6` | `FsGiFundAccrualAdjustmentParam_Reserved6` | TField |  |  |
| 14 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED5` | `FsGiFundAccrualAdjustmentParam_Reserved5` | TField |  |  |
| 15 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED4` | `FsGiFundAccrualAdjustmentParam_Reserved4` | TField |  |  |
| 16 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED3` | `FsGiFundAccrualAdjustmentParam_Reserved3` | TField |  |  |
| 17 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED2` | `FsGiFundAccrualAdjustmentParam_Reserved2` | TField |  |  |
| 18 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RESERVED1` | `FsGiFundAccrualAdjustmentParam_Reserved1` | TField |  |  |
| 19 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.LOCAL.REF` | `FsGiFundAccrualAdjustmentParam_LocalRef` |  |  |  |
| 20 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.OVERRIDE` | `FsGiFundAccrualAdjustmentParam_Override` |  |  |  |
| 21 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.RECORD.STATUS` | `FsGiFundAccrualAdjustmentParam_RecordStatus` | String |  |  |
| 22 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.CURR.NO` | `FsGiFundAccrualAdjustmentParam_CurrNo` | String |  |  |
| 23 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.INPUTTER` | `FsGiFundAccrualAdjustmentParam_Inputter` |  |  |  |
| 24 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.DATE.TIME` | `FsGiFundAccrualAdjustmentParam_DateTime` |  |  |  |
| 25 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.AUTHORISER` | `FsGiFundAccrualAdjustmentParam_Authoriser` | String |  |  |
| 26 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.CO.CODE` | `FsGiFundAccrualAdjustmentParam_CoCode` | String |  |  |
| 27 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.DEPT.CODE` | `FsGiFundAccrualAdjustmentParam_DeptCode` | String |  |  |
| 28 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.AUDITOR.CODE` | `FsGiFundAccrualAdjustmentParam_AuditorCode` | String |  |  |
| 29 | `FS.GI.FUND.ACCRUAL.ADJUSTMENT.PARAM.AUDIT.DATE.TIME` | `FsGiFundAccrualAdjustmentParam_AuditDateTime` | String |  |  |
