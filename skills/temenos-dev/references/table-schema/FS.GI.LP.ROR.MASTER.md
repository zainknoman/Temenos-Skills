# FS.GI.LP.ROR.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.ROR.MASTER` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.ROR.MASTER.PARENT.REF.ID` | `FsGiLpRorMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.ROR.MASTER.ORA.ROWID` | `FsGiLpRorMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.ROR.MASTER.TA.FUND.ID` | `FsGiLpRorMaster_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.ROR.MASTER.ROR.CALC.BASIS` | `FsGiLpRorMaster_RorCalcBasis` | TField |  | ROR calculation basis. Multifonds DB Column is ROR_CALC_BASIS. |
| 5 | `FS.GI.LP.ROR.MASTER.ROR.DESCRIPTION` | `FsGiLpRorMaster_RorDescription` | TField |  | ROR description. Multifonds DB Column is ROR_DESCRIPTION. |
| 6 | `FS.GI.LP.ROR.MASTER.ROR.CALC.TYPE` | `FsGiLpRorMaster_RorCalcType` | TField |  | ROR calculation type. Multifonds DB Column is ROR_TYPE. |
| 7 | `FS.GI.LP.ROR.MASTER.EXCL.INC.FEE.ACCRUAL.FLAG` | `FsGiLpRorMaster_ExclIncFeeAccrualFlag` | TField |  | Flag to exclude incentive fee accrual from ROR calculation. Multifonds DB Column is FLG_EXCL_INC_ACCRUAL. |
| 8 | `FS.GI.LP.ROR.MASTER.EXCL.INC.FEE.CRYST.FLAG` | `FsGiLpRorMaster_ExclIncFeeCrystFlag` | TField |  | Flag to Exclude incentive fee crystallized from ROR calculation. Multifonds DB Column is FLG_EXCL_INC_CRYST. |
| 9 | `FS.GI.LP.ROR.MASTER.FUND.ID` | `FsGiLpRorMaster_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.LP.ROR.MASTER.CLASS.CURRENCY` | `FsGiLpRorMaster_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.LP.ROR.MASTER.RESERVED10` | `FsGiLpRorMaster_Reserved10` | TField |  |  |
| 12 | `FS.GI.LP.ROR.MASTER.RESERVED9` | `FsGiLpRorMaster_Reserved9` | TField |  |  |
| 13 | `FS.GI.LP.ROR.MASTER.RESERVED8` | `FsGiLpRorMaster_Reserved8` | TField |  |  |
| 14 | `FS.GI.LP.ROR.MASTER.RESERVED7` | `FsGiLpRorMaster_Reserved7` | TField |  |  |
| 15 | `FS.GI.LP.ROR.MASTER.RESERVED6` | `FsGiLpRorMaster_Reserved6` | TField |  |  |
| 16 | `FS.GI.LP.ROR.MASTER.RESERVED5` | `FsGiLpRorMaster_Reserved5` | TField |  |  |
| 17 | `FS.GI.LP.ROR.MASTER.RESERVED4` | `FsGiLpRorMaster_Reserved4` | TField |  |  |
| 18 | `FS.GI.LP.ROR.MASTER.RESERVED3` | `FsGiLpRorMaster_Reserved3` | TField |  |  |
| 19 | `FS.GI.LP.ROR.MASTER.RESERVED2` | `FsGiLpRorMaster_Reserved2` | TField |  |  |
| 20 | `FS.GI.LP.ROR.MASTER.RESERVED1` | `FsGiLpRorMaster_Reserved1` | TField |  |  |
| 21 | `FS.GI.LP.ROR.MASTER.LOCAL.REF` | `FsGiLpRorMaster_LocalRef` |  |  |  |
| 22 | `FS.GI.LP.ROR.MASTER.OVERRIDE` | `FsGiLpRorMaster_Override` |  |  |  |
| 23 | `FS.GI.LP.ROR.MASTER.RECORD.STATUS` | `FsGiLpRorMaster_RecordStatus` | String |  |  |
| 24 | `FS.GI.LP.ROR.MASTER.CURR.NO` | `FsGiLpRorMaster_CurrNo` | String |  |  |
| 25 | `FS.GI.LP.ROR.MASTER.INPUTTER` | `FsGiLpRorMaster_Inputter` |  |  |  |
| 26 | `FS.GI.LP.ROR.MASTER.DATE.TIME` | `FsGiLpRorMaster_DateTime` |  |  |  |
| 27 | `FS.GI.LP.ROR.MASTER.AUTHORISER` | `FsGiLpRorMaster_Authoriser` | String |  |  |
| 28 | `FS.GI.LP.ROR.MASTER.CO.CODE` | `FsGiLpRorMaster_CoCode` | String |  |  |
| 29 | `FS.GI.LP.ROR.MASTER.DEPT.CODE` | `FsGiLpRorMaster_DeptCode` | String |  |  |
| 30 | `FS.GI.LP.ROR.MASTER.AUDITOR.CODE` | `FsGiLpRorMaster_AuditorCode` | String |  |  |
| 31 | `FS.GI.LP.ROR.MASTER.AUDIT.DATE.TIME` | `FsGiLpRorMaster_AuditDateTime` | String |  |  |
