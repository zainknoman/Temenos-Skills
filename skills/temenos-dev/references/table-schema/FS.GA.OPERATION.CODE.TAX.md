# FS.GA.OPERATION.CODE.TAX — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPERATION.CODE.TAX` in `FS_Tax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPERATION.CODE.TAX.PARENT.REF.ID` | `FsGaOperationCodeTax_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPERATION.CODE.TAX.ORA.ROWID` | `FsGaOperationCodeTax_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPERATION.CODE.TAX.OPERATION.CODE` | `FsGaOperationCodeTax_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.OPERATION.CODE.TAX.WITHOLDING.TAX.PERCENTAGE` | `FsGaOperationCodeTax_WitholdingTaxPercentage` | TField |  | The &apos;Withholding tax %&apos; field is defined with a default tax rate to be applied to deposit transactions if a tax rate is not setup for deposit transaction operation codes taxes. Multifonds DB Column is PCT_IMPOT. |
| 5 | `FS.GA.OPERATION.CODE.TAX.DEPOSIT.ROUNDING` | `FsGaOperationCodeTax_DepositRounding` | TField |  | Flag to activate rounding for specifc operation codes 040/043/060 Multifonds DB Column is FLG_DEP_ROUNDING. |
| 6 | `FS.GA.OPERATION.CODE.TAX.WHT.ROUND.DOWN.CURRENCY` | `FsGaOperationCodeTax_WhtRoundDownCurrency` | TField |  | Currency of WHT round down Multifonds DB Column is CMON_WHT_ROUND_DOWN. |
| 7 | `FS.GA.OPERATION.CODE.TAX.FUND.ID` | `FsGaOperationCodeTax_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 8 | `FS.GA.OPERATION.CODE.TAX.RESERVED10` | `FsGaOperationCodeTax_Reserved10` | TField |  |  |
| 9 | `FS.GA.OPERATION.CODE.TAX.RESERVED9` | `FsGaOperationCodeTax_Reserved9` | TField |  |  |
| 10 | `FS.GA.OPERATION.CODE.TAX.RESERVED8` | `FsGaOperationCodeTax_Reserved8` | TField |  |  |
| 11 | `FS.GA.OPERATION.CODE.TAX.RESERVED7` | `FsGaOperationCodeTax_Reserved7` | TField |  |  |
| 12 | `FS.GA.OPERATION.CODE.TAX.RESERVED6` | `FsGaOperationCodeTax_Reserved6` | TField |  |  |
| 13 | `FS.GA.OPERATION.CODE.TAX.RESERVED5` | `FsGaOperationCodeTax_Reserved5` | TField |  |  |
| 14 | `FS.GA.OPERATION.CODE.TAX.RESERVED4` | `FsGaOperationCodeTax_Reserved4` | TField |  |  |
| 15 | `FS.GA.OPERATION.CODE.TAX.RESERVED3` | `FsGaOperationCodeTax_Reserved3` | TField |  |  |
| 16 | `FS.GA.OPERATION.CODE.TAX.RESERVED2` | `FsGaOperationCodeTax_Reserved2` | TField |  |  |
| 17 | `FS.GA.OPERATION.CODE.TAX.RESERVED1` | `FsGaOperationCodeTax_Reserved1` | TField |  |  |
| 18 | `FS.GA.OPERATION.CODE.TAX.LOCAL.REF` | `FsGaOperationCodeTax_LocalRef` |  |  |  |
| 19 | `FS.GA.OPERATION.CODE.TAX.OVERRIDE` | `FsGaOperationCodeTax_Override` |  |  |  |
| 20 | `FS.GA.OPERATION.CODE.TAX.RECORD.STATUS` | `FsGaOperationCodeTax_RecordStatus` | String |  |  |
| 21 | `FS.GA.OPERATION.CODE.TAX.CURR.NO` | `FsGaOperationCodeTax_CurrNo` | String |  |  |
| 22 | `FS.GA.OPERATION.CODE.TAX.INPUTTER` | `FsGaOperationCodeTax_Inputter` |  |  |  |
| 23 | `FS.GA.OPERATION.CODE.TAX.DATE.TIME` | `FsGaOperationCodeTax_DateTime` |  |  |  |
| 24 | `FS.GA.OPERATION.CODE.TAX.AUTHORISER` | `FsGaOperationCodeTax_Authoriser` | String |  |  |
| 25 | `FS.GA.OPERATION.CODE.TAX.CO.CODE` | `FsGaOperationCodeTax_CoCode` | String |  |  |
| 26 | `FS.GA.OPERATION.CODE.TAX.DEPT.CODE` | `FsGaOperationCodeTax_DeptCode` | String |  |  |
| 27 | `FS.GA.OPERATION.CODE.TAX.AUDITOR.CODE` | `FsGaOperationCodeTax_AuditorCode` | String |  |  |
| 28 | `FS.GA.OPERATION.CODE.TAX.AUDIT.DATE.TIME` | `FsGaOperationCodeTax_AuditDateTime` | String |  |  |
