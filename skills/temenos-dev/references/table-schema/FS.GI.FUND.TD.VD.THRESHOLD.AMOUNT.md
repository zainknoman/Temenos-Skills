# FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.PARENT.REF.ID` | `FsGiFundTdVdThresholdAmount_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.ORA.ROWID` | `FsGiFundTdVdThresholdAmount_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.TA.FUND.ID` | `FsGiFundTdVdThresholdAmount_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.FUND.MASTER.CCY` | `FsGiFundTdVdThresholdAmount_FundMasterCcy` | TField |  | Base currency (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMONREF. |
| 5 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.OPERATION.CODE` | `FsGiFundTdVdThresholdAmount_OperationCode` | TField |  | Tranaction types which are in scope of the Fund transaction threshould amount TD or VD manual control. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.SHARE.CLASS.CODE` | `FsGiFundTdVdThresholdAmount_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 7 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.PAYMENT.CURRENCY` | `FsGiFundTdVdThresholdAmount_PaymentCurrency` | TField |  | Currency (in 3 letter ISO code, Eg: EUR) in which threshold is expressed. Multifonds DB Column is CMON. |
| 8 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.THRESHOLD.AMOUNT` | `FsGiFundTdVdThresholdAmount_ThresholdAmount` | TField |  | Threshold amount defined to apply manual control on Trade date/value date for a fund transaction. Multifonds DB Column is TLD_AMT. |
| 9 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.FUND.ID` | `FsGiFundTdVdThresholdAmount_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.CLASS.CURRENCY` | `FsGiFundTdVdThresholdAmount_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED10` | `FsGiFundTdVdThresholdAmount_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED9` | `FsGiFundTdVdThresholdAmount_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED8` | `FsGiFundTdVdThresholdAmount_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED7` | `FsGiFundTdVdThresholdAmount_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED6` | `FsGiFundTdVdThresholdAmount_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED5` | `FsGiFundTdVdThresholdAmount_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED4` | `FsGiFundTdVdThresholdAmount_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED3` | `FsGiFundTdVdThresholdAmount_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED2` | `FsGiFundTdVdThresholdAmount_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RESERVED1` | `FsGiFundTdVdThresholdAmount_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.LOCAL.REF` | `FsGiFundTdVdThresholdAmount_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.OVERRIDE` | `FsGiFundTdVdThresholdAmount_Override` |  |  |  |
| 23 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.RECORD.STATUS` | `FsGiFundTdVdThresholdAmount_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.CURR.NO` | `FsGiFundTdVdThresholdAmount_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.INPUTTER` | `FsGiFundTdVdThresholdAmount_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.DATE.TIME` | `FsGiFundTdVdThresholdAmount_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.AUTHORISER` | `FsGiFundTdVdThresholdAmount_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.CO.CODE` | `FsGiFundTdVdThresholdAmount_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.DEPT.CODE` | `FsGiFundTdVdThresholdAmount_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.AUDITOR.CODE` | `FsGiFundTdVdThresholdAmount_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.TD.VD.THRESHOLD.AMOUNT.AUDIT.DATE.TIME` | `FsGiFundTdVdThresholdAmount_AuditDateTime` | String |  |  |
