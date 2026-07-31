# FS.GA.NAV.CHARGE.PER.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CHARGE.PER.FUND` in `FS_Charge.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CHARGE.PER.FUND.PARENT.REF.ID` | `FsGaNavChargePerFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CHARGE.PER.FUND.ORA.ROWID` | `FsGaNavChargePerFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CHARGE.PER.FUND.FUND.ID` | `FsGaNavChargePerFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.CHARGE.PER.FUND.CHARGE.CODE` | `FsGaNavChargePerFund_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 5 | `FS.GA.NAV.CHARGE.PER.FUND.DESCRIPTION` | `FsGaNavChargePerFund_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GA.NAV.CHARGE.PER.FUND.AMOUNT.OR.PCT` | `FsGaNavChargePerFund_AmountOrPct` | TField |  | Displays change in amount or percent made by user in audit trail. Multifonds DB Column is MNT. |
| 7 | `FS.GA.NAV.CHARGE.PER.FUND.LOCAL.CURRENCY` | `FsGaNavChargePerFund_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 8 | `FS.GA.NAV.CHARGE.PER.FUND.FROM.DT` | `FsGaNavChargePerFund_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 9 | `FS.GA.NAV.CHARGE.PER.FUND.LAST.PAYMENT.DATE` | `FsGaNavChargePerFund_LastPaymentDate` | TField |  | Specify the last payment date of fees in charges per fund. For more details refer accrued expenses topic. Multifonds DB Column is DLASTPAY. |
| 10 | `FS.GA.NAV.CHARGE.PER.FUND.TO.DATE` | `FsGaNavChargePerFund_ToDate` | TField |  | To Date Multifonds DB Column is DFIN. |
| 11 | `FS.GA.NAV.CHARGE.PER.FUND.END` | `FsGaNavChargePerFund_End` | TField |  | Set up the flag end in charges per fund screen. For more information please refer accrued expenses topic. Multifonds DB Column is FLAG_FIN. |
| 12 | `FS.GA.NAV.CHARGE.PER.FUND.WT.BEARERS.SHARES.QUANTITY` | `FsGaNavChargePerFund_WtBearersSharesQuantity` | TField |  | Quantity of shares under circulation at the beginning of the period (only used for performance fee calculation). Multifonds DB Column is QT_PART_AVG. |
| 13 | `FS.GA.NAV.CHARGE.PER.FUND.WATERMARK.PRICE` | `FsGaNavChargePerFund_WatermarkPrice` | TField |  | The Watermark start price has to be entered, for performance fee calculation. Multifonds DB Column is COURSVAL_WATER. |
| 14 | `FS.GA.NAV.CHARGE.PER.FUND.BASE.ACCOUNTING.DATE` | `FsGaNavChargePerFund_BaseAccountingDate` | TField |  | Displays Base Accounting Date Multifonds DB Column is FLG_ACC_DATE. |
| 15 | `FS.GA.NAV.CHARGE.PER.FUND.DEFAULT.AUTHORIZED.BASIS` | `FsGaNavChargePerFund_DefaultAuthorizedBasis` | TField |  | Basis for the price per unit for Subscription and redemption for the External fund share unit price. (B - Bid, M - Mid, O - Offer &amp; L - Middle). Multifonds DB Column is AUTH_BASIS. |
| 16 | `FS.GA.NAV.CHARGE.PER.FUND.NAV.CHARGES.ID` | `FsGaNavChargePerFund_NavChargesId` | TField |  | Field used to enter the charge ID of the Unit trust management fees. This field works with a charge defined with the amount types &apos;UK1&apos; and &apos;UK2&apos;. Please refer &apos;Unit Linked Life and pension funds&apos;. Multifonds DB Column is NOFRAIS_REF. |
| 17 | `FS.GA.NAV.CHARGE.PER.FUND.PROCESS.ID` | `FsGaNavChargePerFund_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 18 | `FS.GA.NAV.CHARGE.PER.FUND.DATE.OF.EFFECTIVE` | `FsGaNavChargePerFund_DateOfEffective` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 19 | `FS.GA.NAV.CHARGE.PER.FUND.YEAR.END.IDENTIFIER` | `FsGaNavChargePerFund_YearEndIdentifier` | TField |  | Flag Year End. Multifonds DB Column is FLG_YR_END. |
| 20 | `FS.GA.NAV.CHARGE.PER.FUND.COMPENSATION.RULE` | `FsGaNavChargePerFund_CompensationRule` | TField |  | This flag is used in the context of the UK Capital Gain Tax and allows managing the compensation rules of unrealized / realized results before relief In the report SDCGT01 (Capital gain calculation). Multifonds DB Column is FLG_COMP. |
| 21 | `FS.GA.NAV.CHARGE.PER.FUND.CHECK.PERIOD` | `FsGaNavChargePerFund_CheckPeriod` | TField |  | This field is used in the context of performance fee calculation. The check period is considered to find out the performance between two periods. Multifonds DB Column is CHECK_PERIOD. |
| 22 | `FS.GA.NAV.CHARGE.PER.FUND.GNAV.FEES.TYPE` | `FsGaNavChargePerFund_GnavFeesType` | TField |  | GNAV Fees Type Multifonds DB Column is GNAV_FEES_TYPE. |
| 23 | `FS.GA.NAV.CHARGE.PER.FUND.CALCULATION.PERIOD` | `FsGaNavChargePerFund_CalculationPeriod` | TField |  | Relates to the specific calculation period (D-Daily, M-Monthly, W-Weekly and Y-Yearly) of the performance fee. Multifonds DB Column is CALC_PERIOD. |
| 24 | `FS.GA.NAV.CHARGE.PER.FUND.RETROACTIVE.EXPENSE` | `FsGaNavChargePerFund_RetroactiveExpense` | TField |  | Enables the user to create adjustments to expense rates and/or VAT rates with an effective date less than the current accounting date. Refer Retroactive Expense Accrual for more details. Multifonds DB Column is FLG_RETRO. |
| 25 | `FS.GA.NAV.CHARGE.PER.FUND.SPREAD.IDENTIFIER` | `FsGaNavChargePerFund_SpreadIdentifier` | TField |  | Specify the spread percentage to be considered for NAV charges per fund. Multifonds DB Column is SPREAD. |
| 26 | `FS.GA.NAV.CHARGE.PER.FUND.PAYMENT.DATE.OF.CHARGES` | `FsGaNavChargePerFund_PaymentDateOfCharges` | TField |  | Specify NAV charge payment date of NAV charge for the fund. This need to be in DDMM format. Multifonds DB Column is DPAYMNT_PTF. |
| 27 | `FS.GA.NAV.CHARGE.PER.FUND.NAV.DATE` | `FsGaNavChargePerFund_NavDate` | TField |  | Displays NAV date of fund. Multifonds DB Column is NAV_DATE. |
| 28 | `FS.GA.NAV.CHARGE.PER.FUND.VALUE.DATE.OF.FEES.PAYMENT` | `FsGaNavChargePerFund_ValueDateOfFeesPayment` | TField |  | Used to define the value date related to the NAV charge fee payment, to determine the fee settlement. Multifonds DB Column is VALUE_DATE. |
| 29 | `FS.GA.NAV.CHARGE.PER.FUND.MANUAL.SETTLEMENT.FOR.FEES` | `FsGaNavChargePerFund_ManualSettlementForFees` | TField |  | To enable/disable manual settlements for fees amount Multifonds DB Column is FLG_MANUAL_SETT. |
| 30 | `FS.GA.NAV.CHARGE.PER.FUND.HIDE.FEES` | `FsGaNavChargePerFund_HideFees` | TField |  | If the flag &apos;Hide Fees&apos; is checked, then the system does not display dummy charges in the accrued expenses report SDNAU60. Dummy charge is also linked to the fund. Multifonds DB Column is FLG_HIDE_REP. |
| 31 | `FS.GA.NAV.CHARGE.PER.FUND.NOTIONAL.AMT.PER.SHARE` | `FsGaNavChargePerFund_NotionalAmtPerShare` | TField | Yes | This field is mandatory for amount type &apos;NFE&apos; (fees on notional) to have charge calculation. This fees calculated based on the number of outstanding shares * notional amt per share. Multifonds DB Column is NOTIONAL. |
| 32 | `FS.GA.NAV.CHARGE.PER.FUND.SYLVAN.EXPORT` | `FsGaNavChargePerFund_SylvanExport` | TField |  | Set the flag to enable Sylvan export. Multifonds DB Column is FLG_SYL. |
| 33 | `FS.GA.NAV.CHARGE.PER.FUND.MANAGER.CODE` | `FsGaNavChargePerFund_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 34 | `FS.GA.NAV.CHARGE.PER.FUND.REDUCED.MINIMUM` | `FsGaNavChargePerFund_ReducedMinimum` | TField |  | Flag to activate the functionality. When the calculated charge is &lt; the min Amt, aim is to reduce the min amt for the fund, that has invested in the target funds of the same mngt Co. Multifonds DB Column is FLG_RED_MIN. |
| 35 | `FS.GA.NAV.CHARGE.PER.FUND.SPLIT.INCOME.CAPITAL` | `FsGaNavChargePerFund_SplitIncomeCapital` | TField |  | It allows having a different treatment on cash accounts in case of capital movements (e.g. Purchase of bonds) or income movements (Coupon payment). Multifonds DB Column is CINCOME_FLG. |
| 36 | `FS.GA.NAV.CHARGE.PER.FUND.NEW.CORPORATION.TAX` | `FsGaNavChargePerFund_NewCorporationTax` | TField |  | Flag to enable the new offset rules for Bond Funds Corporation tax calculations. Multifonds DB Column is FLAG_NEW_CORP_TAX. |
| 37 | `FS.GA.NAV.CHARGE.PER.FUND.IFRS.CATEGORY` | `FsGaNavChargePerFund_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 38 | `FS.GA.NAV.CHARGE.PER.FUND.COEFFICIENT` | `FsGaNavChargePerFund_Coefficient` | TField |  | minimum confidence coefficient for a fair value price to be accepted and coefficient for equalisation Multifonds DB Column is COEFFICIENT. |
| 39 | `FS.GA.NAV.CHARGE.PER.FUND.FUND.LEVEL.SCALE.CODE` | `FsGaNavChargePerFund_FundLevelScaleCode` | TField |  | allows user to setup scale code at fund level and the fee rate will be determined by aggregated AUM size for fee type 8A for master funds Multifonds DB Column is CBAREME_PTF. |
| 40 | `FS.GA.NAV.CHARGE.PER.FUND.NET.SUB.OR.RED.ON.INCEP.DAY` | `FsGaNavChargePerFund_NetSubOrRedOnIncepDay` | TField |  | net capstock activity on day of inception of the fund used for performance based fees Multifonds DB Column is MNT_NET_INCEP. |
| 41 | `FS.GA.NAV.CHARGE.PER.FUND.INCEPTION.DAY.INDEX` | `FsGaNavChargePerFund_InceptionDayIndex` | TField |  | Index value on the day of inception of the fund for performance based fees Multifonds DB Column is MNT_INDEX_INCEP. |
| 42 | `FS.GA.NAV.CHARGE.PER.FUND.TARGET.RATE.OF.RETURN` | `FsGaNavChargePerFund_TargetRateOfReturn` | TField |  | target rate of return to be achieved Multifonds DB Column is TARGET_ROR. |
| 43 | `FS.GA.NAV.CHARGE.PER.FUND.ROR.EFFECTIVE.DATE` | `FsGaNavChargePerFund_RorEffectiveDate` | TField |  | Since ROR changes frequently, this field is used to identify the effective date of the ROR Multifonds DB Column is DATE_EFFECTIVE_ROR. |
| 44 | `FS.GA.NAV.CHARGE.PER.FUND.POSTING.CURRENCY` | `FsGaNavChargePerFund_PostingCurrency` | TField |  | Refers to the currency in which the amortization/accretion should be processed (FDMBS00) It also refers to the currency in which NAV charges/expenses setup at fund level (FDFPR12) Multifonds DB Column is CMON_POST. |
| 45 | `FS.GA.NAV.CHARGE.PER.FUND.APM.REDUCTION` | `FsGaNavChargePerFund_ApmReduction` | TField |  | Allows user to define the % of the fee reduce if the market value of the portfolio is less than 70% of the NAV Multifonds DB Column is APM_REDUCTION. |
| 46 | `FS.GA.NAV.CHARGE.PER.FUND.NAV.PERCENTAGE` | `FsGaNavChargePerFund_NavPercentage` | TField |  | Nav Percentage Multifonds DB Column is PCT_NAV. |
| 47 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED10` | `FsGaNavChargePerFund_Reserved10` | TField |  |  |
| 48 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED9` | `FsGaNavChargePerFund_Reserved9` | TField |  |  |
| 49 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED8` | `FsGaNavChargePerFund_Reserved8` | TField |  |  |
| 50 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED7` | `FsGaNavChargePerFund_Reserved7` | TField |  |  |
| 51 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED6` | `FsGaNavChargePerFund_Reserved6` | TField |  |  |
| 52 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED5` | `FsGaNavChargePerFund_Reserved5` | TField |  |  |
| 53 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED4` | `FsGaNavChargePerFund_Reserved4` | TField |  |  |
| 54 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED3` | `FsGaNavChargePerFund_Reserved3` | TField |  |  |
| 55 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED2` | `FsGaNavChargePerFund_Reserved2` | TField |  |  |
| 56 | `FS.GA.NAV.CHARGE.PER.FUND.RESERVED1` | `FsGaNavChargePerFund_Reserved1` | TField |  |  |
| 57 | `FS.GA.NAV.CHARGE.PER.FUND.LOCAL.REF` | `FsGaNavChargePerFund_LocalRef` |  |  |  |
| 58 | `FS.GA.NAV.CHARGE.PER.FUND.OVERRIDE` | `FsGaNavChargePerFund_Override` |  |  |  |
| 59 | `FS.GA.NAV.CHARGE.PER.FUND.RECORD.STATUS` | `FsGaNavChargePerFund_RecordStatus` | String |  |  |
| 60 | `FS.GA.NAV.CHARGE.PER.FUND.CURR.NO` | `FsGaNavChargePerFund_CurrNo` | String |  |  |
| 61 | `FS.GA.NAV.CHARGE.PER.FUND.INPUTTER` | `FsGaNavChargePerFund_Inputter` |  |  |  |
| 62 | `FS.GA.NAV.CHARGE.PER.FUND.DATE.TIME` | `FsGaNavChargePerFund_DateTime` |  |  |  |
| 63 | `FS.GA.NAV.CHARGE.PER.FUND.AUTHORISER` | `FsGaNavChargePerFund_Authoriser` | String |  |  |
| 64 | `FS.GA.NAV.CHARGE.PER.FUND.CO.CODE` | `FsGaNavChargePerFund_CoCode` | String |  |  |
| 65 | `FS.GA.NAV.CHARGE.PER.FUND.DEPT.CODE` | `FsGaNavChargePerFund_DeptCode` | String |  |  |
| 66 | `FS.GA.NAV.CHARGE.PER.FUND.AUDITOR.CODE` | `FsGaNavChargePerFund_AuditorCode` | String |  |  |
| 67 | `FS.GA.NAV.CHARGE.PER.FUND.AUDIT.DATE.TIME` | `FsGaNavChargePerFund_AuditDateTime` | String |  |  |
