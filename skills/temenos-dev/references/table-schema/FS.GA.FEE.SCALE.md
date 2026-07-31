# FS.GA.FEE.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FEE.SCALE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FEE.SCALE.PARENT.REF.ID` | `FsGaFeeScale_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FEE.SCALE.ORA.ROWID` | `FsGaFeeScale_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FEE.SCALE.FUND.ID` | `FsGaFeeScale_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FEE.SCALE.SHARE.CLASS.CODE` | `FsGaFeeScale_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.FEE.SCALE.TRANSACTION.CODE` | `FsGaFeeScale_TransactionCode` | TField |  | Select an appropriate operation code which indicates the type of transaction Multifonds DB Column is CTYP. |
| 6 | `FS.GA.FEE.SCALE.FEE.CODE` | `FsGaFeeScale_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 7 | `FS.GA.FEE.SCALE.HIGHEST` | `FsGaFeeScale_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 8 | `FS.GA.FEE.SCALE.FEES.RATE` | `FsGaFeeScale_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 9 | `FS.GA.FEE.SCALE.RESERVED10` | `FsGaFeeScale_Reserved10` | TField |  |  |
| 10 | `FS.GA.FEE.SCALE.RESERVED9` | `FsGaFeeScale_Reserved9` | TField |  |  |
| 11 | `FS.GA.FEE.SCALE.RESERVED8` | `FsGaFeeScale_Reserved8` | TField |  |  |
| 12 | `FS.GA.FEE.SCALE.RESERVED7` | `FsGaFeeScale_Reserved7` | TField |  |  |
| 13 | `FS.GA.FEE.SCALE.RESERVED6` | `FsGaFeeScale_Reserved6` | TField |  |  |
| 14 | `FS.GA.FEE.SCALE.RESERVED5` | `FsGaFeeScale_Reserved5` | TField |  |  |
| 15 | `FS.GA.FEE.SCALE.RESERVED4` | `FsGaFeeScale_Reserved4` | TField |  |  |
| 16 | `FS.GA.FEE.SCALE.RESERVED3` | `FsGaFeeScale_Reserved3` | TField |  |  |
| 17 | `FS.GA.FEE.SCALE.RESERVED2` | `FsGaFeeScale_Reserved2` | TField |  |  |
| 18 | `FS.GA.FEE.SCALE.RESERVED1` | `FsGaFeeScale_Reserved1` | TField |  |  |
| 19 | `FS.GA.FEE.SCALE.LOCAL.REF` | `FsGaFeeScale_LocalRef` |  |  |  |
| 20 | `FS.GA.FEE.SCALE.OVERRIDE` | `FsGaFeeScale_Override` |  |  |  |
| 21 | `FS.GA.FEE.SCALE.RECORD.STATUS` | `FsGaFeeScale_RecordStatus` | String |  |  |
| 22 | `FS.GA.FEE.SCALE.CURR.NO` | `FsGaFeeScale_CurrNo` | String |  |  |
| 23 | `FS.GA.FEE.SCALE.INPUTTER` | `FsGaFeeScale_Inputter` |  |  |  |
| 24 | `FS.GA.FEE.SCALE.DATE.TIME` | `FsGaFeeScale_DateTime` |  |  |  |
| 25 | `FS.GA.FEE.SCALE.AUTHORISER` | `FsGaFeeScale_Authoriser` | String |  |  |
| 26 | `FS.GA.FEE.SCALE.CO.CODE` | `FsGaFeeScale_CoCode` | String |  |  |
| 27 | `FS.GA.FEE.SCALE.DEPT.CODE` | `FsGaFeeScale_DeptCode` | String |  |  |
| 28 | `FS.GA.FEE.SCALE.AUDITOR.CODE` | `FsGaFeeScale_AuditorCode` | String |  |  |
| 29 | `FS.GA.FEE.SCALE.AUDIT.DATE.TIME` | `FsGaFeeScale_AuditDateTime` | String |  |  |
