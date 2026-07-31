# FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.PARENT.REF.ID` | `FsGiLpFeeExcludeSidePocketfee_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.ORA.ROWID` | `FsGiLpFeeExcludeSidePocketfee_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.SIDE.POCKET.ABF.TYPE.EXCLUSION` | `FsGiLpFeeExcludeSidePocketfee_SidePocketAbfTypeExclusion` | TField |  | Specfies the internal code of the incentive fee type Multifonds DB Column is FEE_EXCL. |
| 4 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.TA.FUND.ID` | `FsGiLpFeeExcludeSidePocketfee_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.SHARE.CLASS.CODE` | `FsGiLpFeeExcludeSidePocketfee_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 6 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.FEE.SEQUENCE.NO` | `FsGiLpFeeExcludeSidePocketfee_FeeSequenceNo` | TField |  | Incentive fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 7 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.FEE.TYPE.FLAG` | `FsGiLpFeeExcludeSidePocketfee_FeeTypeFlag` | TField |  | This specifies the applied incentive fee exclusion type Multifonds DB Column is FLG_FEE_TYPE. |
| 8 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.FUND.ID` | `FsGiLpFeeExcludeSidePocketfee_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.CLASS.CURRENCY` | `FsGiLpFeeExcludeSidePocketfee_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED10` | `FsGiLpFeeExcludeSidePocketfee_Reserved10` | TField |  |  |
| 11 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED9` | `FsGiLpFeeExcludeSidePocketfee_Reserved9` | TField |  |  |
| 12 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED8` | `FsGiLpFeeExcludeSidePocketfee_Reserved8` | TField |  |  |
| 13 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED7` | `FsGiLpFeeExcludeSidePocketfee_Reserved7` | TField |  |  |
| 14 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED6` | `FsGiLpFeeExcludeSidePocketfee_Reserved6` | TField |  |  |
| 15 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED5` | `FsGiLpFeeExcludeSidePocketfee_Reserved5` | TField |  |  |
| 16 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED4` | `FsGiLpFeeExcludeSidePocketfee_Reserved4` | TField |  |  |
| 17 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED3` | `FsGiLpFeeExcludeSidePocketfee_Reserved3` | TField |  |  |
| 18 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED2` | `FsGiLpFeeExcludeSidePocketfee_Reserved2` | TField |  |  |
| 19 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RESERVED1` | `FsGiLpFeeExcludeSidePocketfee_Reserved1` | TField |  |  |
| 20 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.LOCAL.REF` | `FsGiLpFeeExcludeSidePocketfee_LocalRef` |  |  |  |
| 21 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.OVERRIDE` | `FsGiLpFeeExcludeSidePocketfee_Override` |  |  |  |
| 22 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.RECORD.STATUS` | `FsGiLpFeeExcludeSidePocketfee_RecordStatus` | String |  |  |
| 23 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.CURR.NO` | `FsGiLpFeeExcludeSidePocketfee_CurrNo` | String |  |  |
| 24 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.INPUTTER` | `FsGiLpFeeExcludeSidePocketfee_Inputter` |  |  |  |
| 25 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.DATE.TIME` | `FsGiLpFeeExcludeSidePocketfee_DateTime` |  |  |  |
| 26 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.AUTHORISER` | `FsGiLpFeeExcludeSidePocketfee_Authoriser` | String |  |  |
| 27 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.CO.CODE` | `FsGiLpFeeExcludeSidePocketfee_CoCode` | String |  |  |
| 28 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.DEPT.CODE` | `FsGiLpFeeExcludeSidePocketfee_DeptCode` | String |  |  |
| 29 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.AUDITOR.CODE` | `FsGiLpFeeExcludeSidePocketfee_AuditorCode` | String |  |  |
| 30 | `FS.GI.LP.FEE.EXCLUDE.SIDE.POCKETFEE.AUDIT.DATE.TIME` | `FsGiLpFeeExcludeSidePocketfee_AuditDateTime` | String |  |  |
