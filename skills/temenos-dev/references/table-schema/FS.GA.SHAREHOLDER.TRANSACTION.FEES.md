# FS.GA.SHAREHOLDER.TRANSACTION.FEES — Table Schema

> Source: `INSERTS/I_F.FS.GA.SHAREHOLDER.TRANSACTION.FEES` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.PARENT.REF.ID` | `FsGaShareholderTransactionFees_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.ORA.ROWID` | `FsGaShareholderTransactionFees_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.FUND.ID` | `FsGaShareholderTransactionFees_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.SHARE.CLASS.CODE` | `FsGaShareholderTransactionFees_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.SHAREHOLDER` | `FsGaShareholderTransactionFees_Shareholder` | TField |  | Share holder against whom the share class units are lodged. Multifonds DB Column is NACTIONNAIRE. |
| 6 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.INTERNAL.TRANSACTION.ENTRY.NUM` | `FsGaShareholderTransactionFees_InternalTransactionEntryNum` | TField |  | This is the internal entry number for a transaction. Multifonds DB Column is NECRITURE. |
| 7 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.FEE.CODE` | `FsGaShareholderTransactionFees_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 8 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.FEES.RATE` | `FsGaShareholderTransactionFees_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 9 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaShareholderTransactionFees_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 10 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.ARCHIVE` | `FsGaShareholderTransactionFees_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 11 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CURRENCY.OF.FEES` | `FsGaShareholderTransactionFees_CurrencyOfFees` | TField |  | The currency in which the fees are denoted in a transaction. Multifonds DB Column is CMON_FAC. |
| 12 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.FEES.AMOUNT.FEES.CCY` | `FsGaShareholderTransactionFees_FeesAmountFeesCcy` | TField |  | Amount of fees in fees currency. Multifonds DB Column is AMOUNT_ORIG. |
| 13 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.SIGN.IDENTIFIER` | `FsGaShareholderTransactionFees_SignIdentifier` | TField |  | It is to indicate if Amount &gt; 0 Add interest Multifonds DB Column is FLG_SIGN. |
| 14 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AMOUNT.IN.LOCAL.CCY` | `FsGaShareholderTransactionFees_AmountInLocalCcy` | TField |  | AMOUNT IN LOCAL CCY Multifonds DB Column is AMOUNT_ORIG_3DEC. |
| 15 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AMOUNT.3.DECIMAL` | `FsGaShareholderTransactionFees_Amount3Decimal` | TField |  | This field corresponds to the 3 decimal functionality of the amount Multifonds DB Column is MONTANT_3DEC. |
| 16 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.GL.ACCOUNT` | `FsGaShareholderTransactionFees_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 17 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.ACCRUAL.TYPE` | `FsGaShareholderTransactionFees_AccrualType` | TField |  | Accrual Type Multifonds DB Column is ACCRUAL_TYPE. |
| 18 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CAPITALIZATION.FEE` | `FsGaShareholderTransactionFees_CapitalizationFee` | TField |  | Capitalisation Fee Multifonds DB Column is CAPITALIZED_FEE. |
| 19 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CAPITALIZATION.FEE.SETTLEMENT` | `FsGaShareholderTransactionFees_CapitalizationFeeSettlement` | TField |  | Capitalisation Fee Settlement Multifonds DB Column is CAP_FEE_SETTLE. |
| 20 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CAPITALIZATION.FEE.EX.FUND` | `FsGaShareholderTransactionFees_CapitalizationFeeExFund` | TField |  | Capitalisation Fee Ex Fund Multifonds DB Column is CAP_FEE_EXCL_FUND. |
| 21 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.NON.CAPITALISATION.FEE.SETTLMT` | `FsGaShareholderTransactionFees_NonCapitalisationFeeSettlmt` | TField |  | Non Capitalisation Fee Settlmt Multifonds DB Column is NON_CAP_FEE_SETTLE. |
| 22 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.NON.CAPITALIZATION.FEE` | `FsGaShareholderTransactionFees_NonCapitalizationFee` | TField |  | Non Capitalisation Fee Multifonds DB Column is NON_CAP_FEE. |
| 23 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.NON.CAPITALIZATION.FEE.EX.FUND` | `FsGaShareholderTransactionFees_NonCapitalizationFeeExFund` | TField |  | Non Capitalisation Fee Ex Fund Multifonds DB Column is NON_CAP_FEE_EXCL_FUND. |
| 24 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.EXCLUDING.FEES` | `FsGaShareholderTransactionFees_ExcludingFees` | TField |  | Excluding Fees Multifonds DB Column is EXCLUDE_FEE. |
| 25 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED10` | `FsGaShareholderTransactionFees_Reserved10` | TField |  |  |
| 26 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED9` | `FsGaShareholderTransactionFees_Reserved9` | TField |  |  |
| 27 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED8` | `FsGaShareholderTransactionFees_Reserved8` | TField |  |  |
| 28 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED7` | `FsGaShareholderTransactionFees_Reserved7` | TField |  |  |
| 29 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED6` | `FsGaShareholderTransactionFees_Reserved6` | TField |  |  |
| 30 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED5` | `FsGaShareholderTransactionFees_Reserved5` | TField |  |  |
| 31 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED4` | `FsGaShareholderTransactionFees_Reserved4` | TField |  |  |
| 32 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED3` | `FsGaShareholderTransactionFees_Reserved3` | TField |  |  |
| 33 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED2` | `FsGaShareholderTransactionFees_Reserved2` | TField |  |  |
| 34 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RESERVED1` | `FsGaShareholderTransactionFees_Reserved1` | TField |  |  |
| 35 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.LOCAL.REF` | `FsGaShareholderTransactionFees_LocalRef` |  |  |  |
| 36 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.OVERRIDE` | `FsGaShareholderTransactionFees_Override` |  |  |  |
| 37 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.RECORD.STATUS` | `FsGaShareholderTransactionFees_RecordStatus` | String |  |  |
| 38 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CURR.NO` | `FsGaShareholderTransactionFees_CurrNo` | String |  |  |
| 39 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.INPUTTER` | `FsGaShareholderTransactionFees_Inputter` |  |  |  |
| 40 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.DATE.TIME` | `FsGaShareholderTransactionFees_DateTime` |  |  |  |
| 41 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AUTHORISER` | `FsGaShareholderTransactionFees_Authoriser` | String |  |  |
| 42 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.CO.CODE` | `FsGaShareholderTransactionFees_CoCode` | String |  |  |
| 43 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.DEPT.CODE` | `FsGaShareholderTransactionFees_DeptCode` | String |  |  |
| 44 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AUDITOR.CODE` | `FsGaShareholderTransactionFees_AuditorCode` | String |  |  |
| 45 | `FS.GA.SHAREHOLDER.TRANSACTION.FEES.AUDIT.DATE.TIME` | `FsGaShareholderTransactionFees_AuditDateTime` | String |  |  |
