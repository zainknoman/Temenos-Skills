# FS.GA.TAXES.FEES.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.TAXES.FEES.FUND` in `FS_TransactionConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TAXES.FEES.FUND.PARENT.REF.ID` | `FsGaTaxesFeesFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.TAXES.FEES.FUND.ORA.ROWID` | `FsGaTaxesFeesFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.TAXES.FEES.FUND.FUND.ID` | `FsGaTaxesFeesFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.TAXES.FEES.FUND.SERVICE.CODE` | `FsGaTaxesFeesFund_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.TAXES.FEES.FUND.TRANSACTION.NUMBER` | `FsGaTaxesFeesFund_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.TAXES.FEES.FUND.FEE.CODE` | `FsGaTaxesFeesFund_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 7 | `FS.GA.TAXES.FEES.FUND.AMOUNT.OR.PERCENTAGE` | `FsGaTaxesFeesFund_AmountOrPercentage` | TField |  | Percentage of transaction fees Multifonds DB Column is TAX_COM. |
| 8 | `FS.GA.TAXES.FEES.FUND.AMOUNT.IN.SECURITY.CURRENCY` | `FsGaTaxesFeesFund_AmountInSecurityCurrency` | TField |  | Amount in deal currency Multifonds DB Column is AMOUNT. |
| 9 | `FS.GA.TAXES.FEES.FUND.AMOUNT.IN.SETTLEMENT.CURRENCY` | `FsGaTaxesFeesFund_AmountInSettlementCurrency` | TField |  | Fees amount in settlement currency Multifonds DB Column is AMOUNT_FAC. |
| 10 | `FS.GA.TAXES.FEES.FUND.CURRENCY.OF.FEES` | `FsGaTaxesFeesFund_CurrencyOfFees` | TField |  | The currency in which the fees are denoted in a transaction. Multifonds DB Column is CMON_FAC. |
| 11 | `FS.GA.TAXES.FEES.FUND.ARCHIVE` | `FsGaTaxesFeesFund_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 12 | `FS.GA.TAXES.FEES.FUND.BROKER` | `FsGaTaxesFeesFund_Broker` | TField |  | Broker Multifonds DB Column is FLG_BROKER. |
| 13 | `FS.GA.TAXES.FEES.FUND.FEES.TEMP` | `FsGaTaxesFeesFund_FeesTemp` | TField |  | Fees Temp Multifonds DB Column is MFRAIS_TEMP. |
| 14 | `FS.GA.TAXES.FEES.FUND.FEES.AMOUNT.FEES.CCY` | `FsGaTaxesFeesFund_FeesAmountFeesCcy` | TField |  | Amount of fees in fees currency. Multifonds DB Column is AMOUNT_ORIG. |
| 15 | `FS.GA.TAXES.FEES.FUND.ORIG.3.DECIMAL.AMOUNT` | `FsGaTaxesFeesFund_Orig3DecimalAmount` | TField |  | Original 3 decimal amount in currencies like Baharaini Dinar Multifonds DB Column is AMOUNT_FAC_3DEC. |
| 16 | `FS.GA.TAXES.FEES.FUND.CONV.3.DECIMAL.AMOUNT` | `FsGaTaxesFeesFund_Conv3DecimalAmount` | TField |  | Converted 3 decimal amount Multifonds DB Column is AMOUNT_3DEC. |
| 17 | `FS.GA.TAXES.FEES.FUND.FUND.VCI.LOC` | `FsGaTaxesFeesFund_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 18 | `FS.GA.TAXES.FEES.FUND.NEXT` | `FsGaTaxesFeesFund_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 19 | `FS.GA.TAXES.FEES.FUND.ACCRUAL.TYPE` | `FsGaTaxesFeesFund_AccrualType` | TField |  | Accrual Type Multifonds DB Column is ACCRUAL_TYPE. |
| 20 | `FS.GA.TAXES.FEES.FUND.FEES.CURRENCY` | `FsGaTaxesFeesFund_FeesCurrency` | TField |  | Fees Currency Multifonds DB Column is CMON_FEES. |
| 21 | `FS.GA.TAXES.FEES.FUND.CAPITAL` | `FsGaTaxesFeesFund_Capital` | TField |  | Capital Multifonds DB Column is FLG_CAPITALIZE. |
| 22 | `FS.GA.TAXES.FEES.FUND.CAPITALIZATION.FEE` | `FsGaTaxesFeesFund_CapitalizationFee` | TField |  | Capitalisation Fee Multifonds DB Column is CAPITALIZED_FEE. |
| 23 | `FS.GA.TAXES.FEES.FUND.CAPITALIZATION.FEE.SETTLEMENT` | `FsGaTaxesFeesFund_CapitalizationFeeSettlement` | TField |  | Capitalisation Fee Settlement Multifonds DB Column is CAP_FEE_SETTLE. |
| 24 | `FS.GA.TAXES.FEES.FUND.CAPITALIZATION.FEE.EX.FUND` | `FsGaTaxesFeesFund_CapitalizationFeeExFund` | TField |  | Capitalisation Fee Ex Fund Multifonds DB Column is CAP_FEE_EXCL_FUND. |
| 25 | `FS.GA.TAXES.FEES.FUND.NON.CAPITALISATION.FEE.SETTLMT` | `FsGaTaxesFeesFund_NonCapitalisationFeeSettlmt` | TField |  | Non Capitalisation Fee Settlmt Multifonds DB Column is NON_CAP_FEE_SETTLE. |
| 26 | `FS.GA.TAXES.FEES.FUND.NON.CAPITALIZATION.FEE` | `FsGaTaxesFeesFund_NonCapitalizationFee` | TField |  | Non Capitalisation Fee Multifonds DB Column is NON_CAP_FEE. |
| 27 | `FS.GA.TAXES.FEES.FUND.NON.CAPITALIZATION.FEE.EX.FUND` | `FsGaTaxesFeesFund_NonCapitalizationFeeExFund` | TField |  | Non Capitalisation Fee Ex Fund Multifonds DB Column is NON_CAP_FEE_EXCL_FUND. |
| 28 | `FS.GA.TAXES.FEES.FUND.EXCLUDING.FEES` | `FsGaTaxesFeesFund_ExcludingFees` | TField |  | Excluding Fees Multifonds DB Column is EXCLUDE_FEE. |
| 29 | `FS.GA.TAXES.FEES.FUND.MANUAL.TAX` | `FsGaTaxesFeesFund_ManualTax` | TField |  | Manual Tax Multifonds DB Column is FLG_TAX_MANUAL. |
| 30 | `FS.GA.TAXES.FEES.FUND.RESERVED10` | `FsGaTaxesFeesFund_Reserved10` | TField |  |  |
| 31 | `FS.GA.TAXES.FEES.FUND.RESERVED9` | `FsGaTaxesFeesFund_Reserved9` | TField |  |  |
| 32 | `FS.GA.TAXES.FEES.FUND.RESERVED8` | `FsGaTaxesFeesFund_Reserved8` | TField |  |  |
| 33 | `FS.GA.TAXES.FEES.FUND.RESERVED7` | `FsGaTaxesFeesFund_Reserved7` | TField |  |  |
| 34 | `FS.GA.TAXES.FEES.FUND.RESERVED6` | `FsGaTaxesFeesFund_Reserved6` | TField |  |  |
| 35 | `FS.GA.TAXES.FEES.FUND.RESERVED5` | `FsGaTaxesFeesFund_Reserved5` | TField |  |  |
| 36 | `FS.GA.TAXES.FEES.FUND.RESERVED4` | `FsGaTaxesFeesFund_Reserved4` | TField |  |  |
| 37 | `FS.GA.TAXES.FEES.FUND.RESERVED3` | `FsGaTaxesFeesFund_Reserved3` | TField |  |  |
| 38 | `FS.GA.TAXES.FEES.FUND.RESERVED2` | `FsGaTaxesFeesFund_Reserved2` | TField |  |  |
| 39 | `FS.GA.TAXES.FEES.FUND.RESERVED1` | `FsGaTaxesFeesFund_Reserved1` | TField |  |  |
| 40 | `FS.GA.TAXES.FEES.FUND.LOCAL.REF` | `FsGaTaxesFeesFund_LocalRef` |  |  |  |
| 41 | `FS.GA.TAXES.FEES.FUND.OVERRIDE` | `FsGaTaxesFeesFund_Override` |  |  |  |
| 42 | `FS.GA.TAXES.FEES.FUND.RECORD.STATUS` | `FsGaTaxesFeesFund_RecordStatus` | String |  |  |
| 43 | `FS.GA.TAXES.FEES.FUND.CURR.NO` | `FsGaTaxesFeesFund_CurrNo` | String |  |  |
| 44 | `FS.GA.TAXES.FEES.FUND.INPUTTER` | `FsGaTaxesFeesFund_Inputter` |  |  |  |
| 45 | `FS.GA.TAXES.FEES.FUND.DATE.TIME` | `FsGaTaxesFeesFund_DateTime` |  |  |  |
| 46 | `FS.GA.TAXES.FEES.FUND.AUTHORISER` | `FsGaTaxesFeesFund_Authoriser` | String |  |  |
| 47 | `FS.GA.TAXES.FEES.FUND.CO.CODE` | `FsGaTaxesFeesFund_CoCode` | String |  |  |
| 48 | `FS.GA.TAXES.FEES.FUND.DEPT.CODE` | `FsGaTaxesFeesFund_DeptCode` | String |  |  |
| 49 | `FS.GA.TAXES.FEES.FUND.AUDITOR.CODE` | `FsGaTaxesFeesFund_AuditorCode` | String |  |  |
| 50 | `FS.GA.TAXES.FEES.FUND.AUDIT.DATE.TIME` | `FsGaTaxesFeesFund_AuditDateTime` | String |  |  |
