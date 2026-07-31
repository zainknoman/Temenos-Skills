# FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.PARENT.REF.ID` | `FsGiLpFeeExcludeTransacTypes_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.ORA.ROWID` | `FsGiLpFeeExcludeTransacTypes_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.OPERATION.CODE` | `FsGiLpFeeExcludeTransacTypes_OperationCode` | TField |  | Allows specifying a list of transaction types to be excluded from the capital basis before calculating the asset-based fee for the current payment period; e.g. Redemption. The withdrawals from the capital balance, in order to avoid a reduction of the fees if the investor redeems part of its capital within the payment period. Multifonds DB Column is COPERATION. |
| 4 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.TA.FUND.ID` | `FsGiLpFeeExcludeTransacTypes_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.SHARE.CLASS.CODE` | `FsGiLpFeeExcludeTransacTypes_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.FEE.SEQUENCE.NO` | `FsGiLpFeeExcludeTransacTypes_FeeSequenceNo` | TField |  | Asset based fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 7 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.FEE.TYPE.FLAG` | `FsGiLpFeeExcludeTransacTypes_FeeTypeFlag` | TField |  | Specifies the applied asset based fee type. Multifonds DB Column is FLG_FEE_TYPE. |
| 8 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.FUND.ID` | `FsGiLpFeeExcludeTransacTypes_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.CLASS.CURRENCY` | `FsGiLpFeeExcludeTransacTypes_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED10` | `FsGiLpFeeExcludeTransacTypes_Reserved10` | TField |  |  |
| 11 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED9` | `FsGiLpFeeExcludeTransacTypes_Reserved9` | TField |  |  |
| 12 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED8` | `FsGiLpFeeExcludeTransacTypes_Reserved8` | TField |  |  |
| 13 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED7` | `FsGiLpFeeExcludeTransacTypes_Reserved7` | TField |  |  |
| 14 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED6` | `FsGiLpFeeExcludeTransacTypes_Reserved6` | TField |  |  |
| 15 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED5` | `FsGiLpFeeExcludeTransacTypes_Reserved5` | TField |  |  |
| 16 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED4` | `FsGiLpFeeExcludeTransacTypes_Reserved4` | TField |  |  |
| 17 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED3` | `FsGiLpFeeExcludeTransacTypes_Reserved3` | TField |  |  |
| 18 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED2` | `FsGiLpFeeExcludeTransacTypes_Reserved2` | TField |  |  |
| 19 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RESERVED1` | `FsGiLpFeeExcludeTransacTypes_Reserved1` | TField |  |  |
| 20 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.LOCAL.REF` | `FsGiLpFeeExcludeTransacTypes_LocalRef` |  |  |  |
| 21 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.OVERRIDE` | `FsGiLpFeeExcludeTransacTypes_Override` |  |  |  |
| 22 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.RECORD.STATUS` | `FsGiLpFeeExcludeTransacTypes_RecordStatus` | String |  |  |
| 23 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.CURR.NO` | `FsGiLpFeeExcludeTransacTypes_CurrNo` | String |  |  |
| 24 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.INPUTTER` | `FsGiLpFeeExcludeTransacTypes_Inputter` |  |  |  |
| 25 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.DATE.TIME` | `FsGiLpFeeExcludeTransacTypes_DateTime` |  |  |  |
| 26 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.AUTHORISER` | `FsGiLpFeeExcludeTransacTypes_Authoriser` | String |  |  |
| 27 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.CO.CODE` | `FsGiLpFeeExcludeTransacTypes_CoCode` | String |  |  |
| 28 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.DEPT.CODE` | `FsGiLpFeeExcludeTransacTypes_DeptCode` | String |  |  |
| 29 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.AUDITOR.CODE` | `FsGiLpFeeExcludeTransacTypes_AuditorCode` | String |  |  |
| 30 | `FS.GI.LP.FEE.EXCLUDE.TRANSAC.TYPES.AUDIT.DATE.TIME` | `FsGiLpFeeExcludeTransacTypes_AuditDateTime` | String |  |  |
