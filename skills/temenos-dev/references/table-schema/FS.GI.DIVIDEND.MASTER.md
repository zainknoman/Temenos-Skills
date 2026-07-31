# FS.GI.DIVIDEND.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.MASTER` in `FS_Dividend.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIVIDEND.MASTER.FUND.ID` | `FsGiDividendMaster_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.DIVIDEND.MASTER.LEGAL.ENTITY.ID` | `FsGiDividendMaster_LegalEntityId` | TField |  | Legal entity internal ID. Multifonds DB Column is NTFC. |
| 3 | `FS.GI.DIVIDEND.MASTER.SHARE.CLASS.CODE` | `FsGiDividendMaster_ShareClassCode` | TField |  | Fund share class is in scope for the dividend. Multifonds DB Column is TPART. |
| 4 | `FS.GI.DIVIDEND.MASTER.COUPON.NUMBER` | `FsGiDividendMaster_CouponNumber` | TField |  | Coupon number. Multifonds DB Column is NCOUPON. |
| 5 | `FS.GI.DIVIDEND.MASTER.SEQUENCE.NUMBER` | `FsGiDividendMaster_SequenceNumber` | TField |  | Dividend sequence number for the fund share class. Multifonds DB Column is SEQUENCE_NUMBER. |
| 6 | `FS.GI.DIVIDEND.MASTER.DIVIDEND.PER.SHARE` | `FsGiDividendMaster_DividendPerShare` | TField |  | Dividend amount per share distributed by Legal Entity. Multifonds DB Column is UNIT_DIVIDEND_AMT. |
| 7 | `FS.GI.DIVIDEND.MASTER.TISD` | `FsGiDividendMaster_Tisd` | TField |  | Taxable interest amount per share for distribution available for transparent TA Fund share classes. Multifonds DB Column is TISD. |
| 8 | `FS.GI.DIVIDEND.MASTER.COMMISSION.TYPE` | `FsGiDividendMaster_CommissionType` | TField |  | Commission type. Multifonds DB Column is COMMISSION_TYPE. |
| 9 | `FS.GI.DIVIDEND.MASTER.PERCENTAGE` | `FsGiDividendMaster_Percentage` | TField |  | Instruction percentage of investment or redemption. Multifonds DB Column is PERCENTAGE. |
| 10 | `FS.GI.DIVIDEND.MASTER.AMOUNT` | `FsGiDividendMaster_Amount` | TField |  | Specific amount value for the choosen profile criteria. Multifonds DB Column is AMOUNT. |
| 11 | `FS.GI.DIVIDEND.MASTER.RECORD.DATE` | `FsGiDividendMaster_RecordDate` | TField |  | Date on which the system will calculate the register position for the Dividend payment. The system takes into account all positions available at the end of this date. Multifonds DB Column is DRECORD. |
| 12 | `FS.GI.DIVIDEND.MASTER.EXECUTION.DATE` | `FsGiDividendMaster_ExecutionDate` | TField |  | Dividend exercise / execution date. Multifonds DB Column is EX_DATE. |
| 13 | `FS.GI.DIVIDEND.MASTER.TRADE.DATE` | `FsGiDividendMaster_TradeDate` | TField |  | Trade date of the reinvestment orders. Multifonds DB Column is TRADE_DATE. |
| 14 | `FS.GI.DIVIDEND.MASTER.VALUE.DATE` | `FsGiDividendMaster_ValueDate` | TField |  | Value date for non-daily dividend payment. Multifonds DB Column is VALUE_DATE. |
| 15 | `FS.GI.DIVIDEND.MASTER.PAYOUT.DATE` | `FsGiDividendMaster_PayoutDate` | TField |  | Value date in case of dividend distribution and dividend reinvestment. Multifonds DB Column is PAYOUT_DATE. |
| 16 | `FS.GI.DIVIDEND.MASTER.GROUP.DIVIDEND.RECORD.DATE` | `FsGiDividendMaster_GroupDividendRecordDate` | TField |  | Record date for grouped dividend. Multifonds DB Column is DREC_GRP_DIV. |
| 17 | `FS.GI.DIVIDEND.MASTER.RATE.TYPE` | `FsGiDividendMaster_RateType` | TField |  | Rate type. Multifonds DB Column is CRATE_TYPE. |
| 18 | `FS.GI.DIVIDEND.MASTER.INCOME.TYPE` | `FsGiDividendMaster_IncomeType` | TField |  | Income type. Multifonds DB Column is CINCOME_TYPE. |
| 19 | `FS.GI.DIVIDEND.MASTER.DISTRIBUTION.TYPE` | `FsGiDividendMaster_DistributionType` | TField |  | Distribution type. Multifonds DB Column is CDISTRIB_TYPE. |
| 20 | `FS.GI.DIVIDEND.MASTER.EQUALIZATION.RATE` | `FsGiDividendMaster_EqualizationRate` | TField |  | Equalization rate. Multifonds DB Column is NEQU_RATE. |
| 21 | `FS.GI.DIVIDEND.MASTER.INDIVIDUAL.EQUALIZATION.FLAG` | `FsGiDividendMaster_IndividualEqualizationFlag` | TField |  | Individual income equalization flag. Multifonds DB Column is IND_EQUI_FLG. |
| 22 | `FS.GI.DIVIDEND.MASTER.TAX.RATE` | `FsGiDividendMaster_TaxRate` | TField |  | Tax rate. Multifonds DB Column is NTAX_RATE. |
| 23 | `FS.GI.DIVIDEND.MASTER.FRANKED.INCOME.PERCENT` | `FsGiDividendMaster_FrankedIncomePercent` | TField |  | Franked income percentage. Multifonds DB Column is NFRANK_INCOME. |
| 24 | `FS.GI.DIVIDEND.MASTER.ELIGIBLE.INCOME` | `FsGiDividendMaster_EligibleIncome` | TField |  | Eligible income percentage. Multifonds DB Column is NELIGIB_INCOME. |
| 25 | `FS.GI.DIVIDEND.MASTER.CORPORATION.TAX` | `FsGiDividendMaster_CorporationTax` | TField |  | Corporation tax. Multifonds DB Column is NCORPORATION_TAX. |
| 26 | `FS.GI.DIVIDEND.MASTER.CORPORATION.TAX.PER.UNIT` | `FsGiDividendMaster_CorporationTaxPerUnit` | TField |  | Corporation tax per unit. Multifonds DB Column is UNIT_CORP_TAX. |
| 27 | `FS.GI.DIVIDEND.MASTER.PERIOD.FROM` | `FsGiDividendMaster_PeriodFrom` | TField |  | Beginning date of the fiscal period from which the tax is applicable. Multifonds DB Column is PERIOD_FROM. |
| 28 | `FS.GI.DIVIDEND.MASTER.PERIOD.TO` | `FsGiDividendMaster_PeriodTo` | TField |  | Ending fiscal period for the tax. Multifonds DB Column is PERIOD_TO. |
| 29 | `FS.GI.DIVIDEND.MASTER.REDEMPTION.TRADE.DATE` | `FsGiDividendMaster_RedemptionTradeDate` | TField |  | Redemption Trade date Multifonds DB Column is RED_TRADE_DATE. |
| 30 | `FS.GI.DIVIDEND.MASTER.REDEMPTION.VALUE.DATE` | `FsGiDividendMaster_RedemptionValueDate` | TField |  | Redemption Value date Multifonds DB Column is RED_VALUE_DATE. |
| 31 | `FS.GI.DIVIDEND.MASTER.CONFIRMED.BY` | `FsGiDividendMaster_ConfirmedBy` | TField |  | User who confirmed the record. Multifonds DB Column is CONFIRMED_BY. |
| 32 | `FS.GI.DIVIDEND.MASTER.VALIDATED.DATE` | `FsGiDividendMaster_ValidatedDate` | TField |  | Dividend validated date. Multifonds DB Column is VALIDATED_DATE. |
| 33 | `FS.GI.DIVIDEND.MASTER.BATCH.STATUS` | `FsGiDividendMaster_BatchStatus` | TField |  | Dividend batch status code. Multifonds DB Column is BATCH_STATUS. |
| 34 | `FS.GI.DIVIDEND.MASTER.DIVIDEND.DISTRIBUTION` | `FsGiDividendMaster_DividendDistribution` | TField |  | Flag to indicate dividend distribution. Multifonds DB Column is DIV_DISTRIB. |
| 35 | `FS.GI.DIVIDEND.MASTER.PAYMENT.STATUS` | `FsGiDividendMaster_PaymentStatus` | TField |  | Dividend payment status at share class level. Multifonds DB Column is PAYMENT_STATUS. |
| 36 | `FS.GI.DIVIDEND.MASTER.MONTHLY.DIVIDEND` | `FsGiDividendMaster_MonthlyDividend` | TField |  | Dividend Month expressed as the date for the first day of that month. Multifonds DB Column is DMONTH_DIV. |
| 37 | `FS.GI.DIVIDEND.MASTER.GROUP.UPDATE.FLAG` | `FsGiDividendMaster_GroupUpdateFlag` | TField |  | Flag to enable share group to update, when a dividend period ends and no dividend has to be paid out. Multifonds DB Column is FLG_GRP_UPD. |
| 38 | `FS.GI.DIVIDEND.MASTER.DIVIDEND.TYPE` | `FsGiDividendMaster_DividendType` | TField |  | Dividend type code. Multifonds DB Column is DIVIDEND_TYPE. |
| 39 | `FS.GI.DIVIDEND.MASTER.CANCELLED.DIVIDEND` | `FsGiDividendMaster_CancelledDividend` | TField |  | Flag indicate dividend cancelled. Multifonds DB Column is FLG_CANCEL_DIV. |
| 40 | `FS.GI.DIVIDEND.MASTER.TAXABLE.FLAG` | `FsGiDividendMaster_TaxableFlag` | TField |  | Flag to calculate EUSD tax on the Dividend to be distributed by the fund in scope on dividend under EUSD. Multifonds DB Column is FLG_TAXABLE. |
| 41 | `FS.GI.DIVIDEND.MASTER.GROUP.2.RATE` | `FsGiDividendMaster_Group2Rate` | TField |  | Group 2 rate. Multifonds DB Column is NGROUP2_RATE. |
| 42 | `FS.GI.DIVIDEND.MASTER.DEEMED.DISTRIBUTION.FLAG` | `FsGiDividendMaster_DeemedDistributionFlag` | TField |  | Flag to enable deemed distribution. Multifonds DB Column is DIM_DISTRIB. |
| 43 | `FS.GI.DIVIDEND.MASTER.BATCH.CONFIRM.DATE` | `FsGiDividendMaster_BatchConfirmDate` | TField |  | Batch confirmation date. Multifonds DB Column is BATCH_DCONFIRM. |
| 44 | `FS.GI.DIVIDEND.MASTER.DIVIDEND.QUOTATION.CURRENCY` | `FsGiDividendMaster_DividendQuotationCurrency` | TField |  | Dividend to be paid in fund quotation currency only (instead of register payment ccy) Multifonds DB Column is FLG_DIV_QUOT_CCY. |
| 45 | `FS.GI.DIVIDEND.MASTER.TOTAL.GROSS.DIVIDEND.AMOUNT` | `FsGiDividendMaster_TotalGrossDividendAmount` | TField |  | Total gross dividend amount for all registers linked to the dividend distribution in fund currency. Multifonds DB Column is TOT_GRS_DIV_AMT. |
| 46 | `FS.GI.DIVIDEND.MASTER.TOTAL.GROSS.AMT.ROUNDING.DIFF` | `FsGiDividendMaster_TotalGrossAmtRoundingDiff` | TField |  | Total gross dividend amount rounding difference for registers linked to the dividiend distribution in fund currency. Multifonds DB Column is TOT_GRS_DIV_AMT_RNDG. |
| 47 | `FS.GI.DIVIDEND.MASTER.GROUP.ID` | `FsGiDividendMaster_GroupId` | TField |  | Fund group code. Multifonds DB Column is GRP_ID. |
| 48 | `FS.GI.DIVIDEND.MASTER.TEMPLATE` | `FsGiDividendMaster_Template` | TField |  | Dividend reporting Template. Multifonds DB Column is TEMPLATE_ID. |
| 49 | `FS.GI.DIVIDEND.MASTER.TOTAL.NET.DIVIDEND.AMOUNT` | `FsGiDividendMaster_TotalNetDividendAmount` | TField |  | Total net dividend amount for all registers linked to the dividend distribution in fund currency. Multifonds DB Column is TOT_NET_DIVD_AMT. |
| 50 | `FS.GI.DIVIDEND.MASTER.TOTAL.DIVIDEND.TAX.AMOUNT` | `FsGiDividendMaster_TotalDividendTaxAmount` | TField |  | Total dividend tax amount. Multifonds DB Column is TOT_DIVD_TAX_AMT. |
| 51 | `FS.GI.DIVIDEND.MASTER.TOTAL.GROSS.DIV.PAYMENT.AMT` | `FsGiDividendMaster_TotalGrossDivPaymentAmt` | TField |  | Total gross dividend amount for all registers linked to the dividend distribution in payment currency. Multifonds DB Column is TOT_GRS_DIVD_PAY_AMT. |
| 52 | `FS.GI.DIVIDEND.MASTER.TOTAL.NET.DIV.PAYMENT.AMT` | `FsGiDividendMaster_TotalNetDivPaymentAmt` | TField |  | Total net dividend amount for all registers linked to the dividend distribution in payment currency. Multifonds DB Column is TOT_NET_DIVD_PAY_AMT. |
| 53 | `FS.GI.DIVIDEND.MASTER.BATCH.MESSAGE` | `FsGiDividendMaster_BatchMessage` | TField |  | Batch result message. Multifonds DB Column is BATCH_MESSAGE. |
| 54 | `FS.GI.DIVIDEND.MASTER.RESERVED10` | `FsGiDividendMaster_Reserved10` | TField |  |  |
| 55 | `FS.GI.DIVIDEND.MASTER.RESERVED9` | `FsGiDividendMaster_Reserved9` | TField |  |  |
| 56 | `FS.GI.DIVIDEND.MASTER.RESERVED8` | `FsGiDividendMaster_Reserved8` | TField |  |  |
| 57 | `FS.GI.DIVIDEND.MASTER.RESERVED7` | `FsGiDividendMaster_Reserved7` | TField |  |  |
| 58 | `FS.GI.DIVIDEND.MASTER.RESERVED6` | `FsGiDividendMaster_Reserved6` | TField |  |  |
| 59 | `FS.GI.DIVIDEND.MASTER.RESERVED5` | `FsGiDividendMaster_Reserved5` | TField |  |  |
| 60 | `FS.GI.DIVIDEND.MASTER.RESERVED4` | `FsGiDividendMaster_Reserved4` | TField |  |  |
| 61 | `FS.GI.DIVIDEND.MASTER.RESERVED3` | `FsGiDividendMaster_Reserved3` | TField |  |  |
| 62 | `FS.GI.DIVIDEND.MASTER.RESERVED2` | `FsGiDividendMaster_Reserved2` | TField |  |  |
| 63 | `FS.GI.DIVIDEND.MASTER.RESERVED1` | `FsGiDividendMaster_Reserved1` | TField |  |  |
| 64 | `FS.GI.DIVIDEND.MASTER.LOCAL.REF` | `FsGiDividendMaster_LocalRef` |  |  |  |
| 65 | `FS.GI.DIVIDEND.MASTER.OVERRIDE` | `FsGiDividendMaster_Override` |  |  |  |
| 66 | `FS.GI.DIVIDEND.MASTER.RECORD.STATUS` | `FsGiDividendMaster_RecordStatus` | String |  |  |
| 67 | `FS.GI.DIVIDEND.MASTER.CURR.NO` | `FsGiDividendMaster_CurrNo` | String |  |  |
| 68 | `FS.GI.DIVIDEND.MASTER.INPUTTER` | `FsGiDividendMaster_Inputter` |  |  |  |
| 69 | `FS.GI.DIVIDEND.MASTER.DATE.TIME` | `FsGiDividendMaster_DateTime` |  |  |  |
| 70 | `FS.GI.DIVIDEND.MASTER.AUTHORISER` | `FsGiDividendMaster_Authoriser` | String |  |  |
| 71 | `FS.GI.DIVIDEND.MASTER.CO.CODE` | `FsGiDividendMaster_CoCode` | String |  |  |
| 72 | `FS.GI.DIVIDEND.MASTER.DEPT.CODE` | `FsGiDividendMaster_DeptCode` | String |  |  |
| 73 | `FS.GI.DIVIDEND.MASTER.AUDITOR.CODE` | `FsGiDividendMaster_AuditorCode` | String |  |  |
| 74 | `FS.GI.DIVIDEND.MASTER.AUDIT.DATE.TIME` | `FsGiDividendMaster_AuditDateTime` | String |  |  |
