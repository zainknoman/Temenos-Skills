# FS.GA.FUTURE.VARIATION.MARGIN — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.VARIATION.MARGIN` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.VARIATION.MARGIN.PARENT.REF.ID` | `FsGaFutureVariationMargin_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.VARIATION.MARGIN.ORA.ROWID` | `FsGaFutureVariationMargin_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.VARIATION.MARGIN.SEQ.NUMBER` | `FsGaFutureVariationMargin_SeqNumber` | TField |  | Sequence Number Multifonds DB Column is NOTXFLT. |
| 4 | `FS.GA.FUTURE.VARIATION.MARGIN.FUTURE.ID.CODE` | `FsGaFutureVariationMargin_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 5 | `FS.GA.FUTURE.VARIATION.MARGIN.FROM.DT` | `FsGaFutureVariationMargin_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 6 | `FS.GA.FUTURE.VARIATION.MARGIN.TO.DATE` | `FsGaFutureVariationMargin_ToDate` | TField |  | To Date Multifonds DB Column is DFIN. |
| 7 | `FS.GA.FUTURE.VARIATION.MARGIN.VARIATION.MARGIN.PERCENTAGE` | `FsGaFutureVariationMargin_VariationMarginPercentage` | TField |  | Variation Margin Percentage Multifonds DB Column is PCT_VAR_MARG. |
| 8 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED10` | `FsGaFutureVariationMargin_Reserved10` | TField |  |  |
| 9 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED9` | `FsGaFutureVariationMargin_Reserved9` | TField |  |  |
| 10 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED8` | `FsGaFutureVariationMargin_Reserved8` | TField |  |  |
| 11 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED7` | `FsGaFutureVariationMargin_Reserved7` | TField |  |  |
| 12 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED6` | `FsGaFutureVariationMargin_Reserved6` | TField |  |  |
| 13 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED5` | `FsGaFutureVariationMargin_Reserved5` | TField |  |  |
| 14 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED4` | `FsGaFutureVariationMargin_Reserved4` | TField |  |  |
| 15 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED3` | `FsGaFutureVariationMargin_Reserved3` | TField |  |  |
| 16 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED2` | `FsGaFutureVariationMargin_Reserved2` | TField |  |  |
| 17 | `FS.GA.FUTURE.VARIATION.MARGIN.RESERVED1` | `FsGaFutureVariationMargin_Reserved1` | TField |  |  |
| 18 | `FS.GA.FUTURE.VARIATION.MARGIN.LOCAL.REF` | `FsGaFutureVariationMargin_LocalRef` |  |  |  |
| 19 | `FS.GA.FUTURE.VARIATION.MARGIN.OVERRIDE` | `FsGaFutureVariationMargin_Override` |  |  |  |
| 20 | `FS.GA.FUTURE.VARIATION.MARGIN.RECORD.STATUS` | `FsGaFutureVariationMargin_RecordStatus` | String |  |  |
| 21 | `FS.GA.FUTURE.VARIATION.MARGIN.CURR.NO` | `FsGaFutureVariationMargin_CurrNo` | String |  |  |
| 22 | `FS.GA.FUTURE.VARIATION.MARGIN.INPUTTER` | `FsGaFutureVariationMargin_Inputter` |  |  |  |
| 23 | `FS.GA.FUTURE.VARIATION.MARGIN.DATE.TIME` | `FsGaFutureVariationMargin_DateTime` |  |  |  |
| 24 | `FS.GA.FUTURE.VARIATION.MARGIN.AUTHORISER` | `FsGaFutureVariationMargin_Authoriser` | String |  |  |
| 25 | `FS.GA.FUTURE.VARIATION.MARGIN.CO.CODE` | `FsGaFutureVariationMargin_CoCode` | String |  |  |
| 26 | `FS.GA.FUTURE.VARIATION.MARGIN.DEPT.CODE` | `FsGaFutureVariationMargin_DeptCode` | String |  |  |
| 27 | `FS.GA.FUTURE.VARIATION.MARGIN.AUDITOR.CODE` | `FsGaFutureVariationMargin_AuditorCode` | String |  |  |
| 28 | `FS.GA.FUTURE.VARIATION.MARGIN.AUDIT.DATE.TIME` | `FsGaFutureVariationMargin_AuditDateTime` | String |  |  |
