# SC.SM.MC.DEFINITION — Table Schema

> Source: `INSERTS/I_F.SC.SM.MC.DEFINITION` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SMC.COUPON.TAX.CODE` | `ScSmMcDefinition_CouponTaxCode` | TField | Yes | Indicates the tax position regarding the interest, coupons, dividends etc. This field is used to define whether interest, coupons, dividends etc., are taxed, non taxed, net of tax etc. Validation Rules: 1-5 Alphanumeric characters. (Mandatory input) Must exist on the COUPON.TAX.CODE file. |
| 2 | `SC.SMC.SAFE.CUSTODY.CODE` | `ScSmMcDefinition_SafeCustodyCode` | TField | No | Indicates whether or not a safe custody charge is to be levied on this particular Security. Field will always default to Y. In the event that the underlying security attracts no safe custody fees at all,you may enter N. Validation Rules: 0 - 2 Alphabetic characters (Optional input but will default) Default value Y. Only Y or NO can be entered in this field. |
| 3 | `SC.SMC.SHARE.REGISTER` | `ScSmMcDefinition_ShareRegister` | TField | No | Indicates whether or not the Security has to be registered under the Clients name. Normally these conditions will be specified at Transaction level. Any input at SECURITY.MASTER level can beoverridden. Validation Rules: 1 Alphabetic character. (Optional input) Only Y or N can be entered in this field. |
| 4 | `SC.SMC.REACQ.PRD` | `ScSmMcDefinition_ReacqPrd` | TField | Yes | This field holds a time period that is to be used to treat a purchase after a sale of a security as areacquisition of the security. Reacquisition of a security can trigger a situation that drops that loss associated with the sale transaction. Validation Rules: Mandatory input if the REACQ.DROP.LOSS field has been entered. Must be of the format nnD, nnB, nnW, nnM, nnY. Where: nn - number of the days D - Calendar Days B - Business Days W - Weeks M - Months Y - Years |
| 5 | `SC.SMC.REACQ.DROP.LOSS` | `ScSmMcDefinition_ReacqDropLoss` | TField | Yes | This field may have a value of YES to denote that the loss will be dropped on reacquisition of a security Or NO if the loss will not be dropped. Validation Rules: Valid values of YES or NO Input mandatory if the REACQ.PRD field is entered Nulls is treated like NO |
| 6 | `SC.SMC.CG.INCL.ACCR.INT` | `ScSmMcDefinition_CgInclAccrInt` | TField | No | This field may have a value of YES to indicate that the accrued interest will be included into the calculation ofthe CG PL Or a value of NO to indicate that the accrued interest will not be included into the CG PL calculation. Validation Rules: Valid values YES or NO Nulls treated like NO Optional input |
| 7 | `SC.SMC.CG.INCL.EXPENSE` | `ScSmMcDefinition_CgInclExpense` | TField | No | This field may have a value of YES to indicate that the expenses will be included into the calculation of the CGPL Or a value of NO to indicate that the expenses will not be included into the CG PL calculation. Validation Rules: Valid values YES or NO Nulls treated like NO Optional input |
| 8 | `SC.SMC.WCG.INCL.ACCR.INT` | `ScSmMcDefinition_WcgInclAccrInt` | TField | No | This field may have a value of YES to indicate that the accrued interest will be included into the calculation ofthe CG PL withheld tax Or a value of NO to indicate that the accrued interest will not be included into the CG PL withheld taxcalculation. Validation Rules: Valid values YES or NO Nulls treated like NO Optional input |
| 9 | `SC.SMC.WCG.INCL.EXPENSE` | `ScSmMcDefinition_WcgInclExpense` | TField | No | This field may have a value of YES to indicate that the expenses will be included into the calculation of the CGPL withheld tax Or a value of NO to indicate that the expenses will not be included into the CG PL withheld tax calculation. Validation Rules: Valid values YES or NO Nulls treated like NO Optional input |
| 10 | `SC.SMC.BLOCKING.DATE` | `ScSmMcDefinition_BlockingDate` | TField |  | Date from which all activity in this security is to be prohibited. Validation Rules: Standard date format - ddmmyy. |
| 11 | `SC.SMC.BLOCKING.NARR` | `ScSmMcDefinition_BlockingNarr` | TField |  | Narrative the user wishes to be displayed in the override when a blocked security is used. Validation Rules: Free format message- alpha-numeric. |
| 12 | `SC.SMC.RECOMMEND` | `ScSmMcDefinition_Recommend` | TField |  | Whether the instrument is recommended or not, can be STRONG.BUY, BUY, HOLD, SELL or STRONG.SELL. |
| 13 | `SC.SMC.TXN.TAX.CODE` | `ScSmMcDefinition_TxnTaxCode` | TField |  | Indicates the tax code based on which tax is to be charged from the transaction on sale of this security. Validation Rules: 1-5 Alphanumeric characters. Must exist on the TXN.TAX.CODE file. |
| 14 | `SC.SMC.SC.TAX.CODE` | `ScSmMcDefinition_ScTaxCode` |  |  |  |
| 15 | `SC.SMC.TAX.BASIS` | `ScSmMcDefinition_TaxBasis` | TField |  | Tax basis for calculating tax due, either FIFO, LIFO or AVERAGE. |
| 16 | `SC.SMC.RISK.LEVEL` | `ScSmMcDefinition_RiskLevel` | TField |  | Risk level, defined by EB.LOOKUP table from RISK.LEVEL. |
| 17 | `SC.SMC.ALLOWED.INVESTOR` | `ScSmMcDefinition_AllowedInvestor` | TField |  | This field indicates the type of investor (Accredited Investor, Professional) that are allowed to invest in thisproduct.This field is associated multi value with COMP.LEVEL.ATTRIB and RISK.LEVEL Validation Rules: Input to this field accepts valid record from EB.LOOKUP table whose id starts with INVESTOR*Text |
| 18 | `SC.SMC.MARGINABLE` | `ScSmMcDefinition_Marginable` | TField |  | This field will accept a value NO. If set to NO, margin value, Top-up margin value and sell out margin valuewill not be calculated(i.e. will be zero) in SC.POS.ASSET for the security. Validation Rules: Maximum of 32 characters is allowed |
| 19 | `SC.SMC.COMPLEXITY` | `ScSmMcDefinition_Complexity` | TField |  | This field records the level of complexity of the instrument Validation Rules: Accepts free format input of 35 characters from the EB.LOOKUP table whose id starts with SM.COMPLEXITY*Text. |
| 20 | `SC.SMC.ALERT.PRICE.PERC` | `ScSmMcDefinition_AlertPricePerc` | TField |  | This field accepts two numeric values. When the percentage of price change, for the security is greater thanALERT.PRICE.PERC, then an alert will be sent to the portfolio owner, if the portfolio has subscribed for pricemovement alert. |
| 21 | `SC.SMC.RESTRICTED` | `ScSmMcDefinition_Restricted` | TField |  | This field accept value YES. If this field is set to YES then security is considered as restricted stock andfield MARGINABLE should be set to NO. The security value for these stocks will be calculated using the diversified margins specified for these stocks,provided they are held in a diversified portfolio. If the field is not set, then the margin value of these stocks will be zero. |
| 22 | `SC.SMC.PL.SETT` | `ScSmMcDefinition_PlSett` | TField | Yes | Input to this field can be any one of the following ALL, COUNTRY code prefixed by C-, BIC CODE prefixed by B-,SC.AGENT.PLACE id prefixed by A- or any free format narrative. This field will allow maximum of 15 characters and it is not a mandatory field. While committing a SEC.TRADE or SECURITY.TRANSFER the value from this field will be taken to build SSI key and ifthis field is null then it will be taken as ALL. |
| 23 | `SC.SMC.LOSS.MARGIN.CNTRL` | `ScSmMcDefinition_LossMarginCntrl` | TField | No | Indicates the percentage of loss margin allowable on this Security. If not entered, the margin allowed for the SUB.ASSET.TYPE will be used. Validation Rules 1-5 Alphanumeric characters. (Optional input) Must exist on the MARGIN.CONTROL file. |
| 24 | `SC.SMC.STP` | `ScSmMcDefinition_Stp` | TField |  | Allowed options are YES ,MX and NULL . YES indicates that the message MT502 will be sent from order throughSWIFT. MX will generate MX message from order instead of SWIFT message. |
| 25 | `SC.SMC.BROKER` | `ScSmMcDefinition_Broker` | TField | Yes | Allowed only valid Customer security id of the type Broker. This field will be mandatory while STP field is set. |
| 26 | `SC.SMC.EXE.HLT` | `ScSmMcDefinition_ExeHlt` | TField |  | Allowed option are YES or NULL . YES will Indicate whether the execution should be flagged for halt. |
| 27 | `SC.SMC.TRADE.HLT` | `ScSmMcDefinition_TradeHlt` | TField |  | Allowed option are YES or NULL . YES will indicate if the authorisation of the trade should be halted. |
| 28 | `SC.SMC.APPL.INFL.INDEX` | `ScSmMcDefinition_ApplInflIndex` | TField |  | The behaviour of the field APPL.INFL.INDEX is as shown below: 1.Interest- When the inflation index needs to be applied to accrued interest at the time of purchase, Dailyaccrual and coupon payment 2.Principal- When the inflation index needs to be applied only to the principal/ final maturity value at thetime of redemption/ maturity. 3.Both- For both interest and principal adjustment. |
| 29 | `SC.SMC.RESERVED11` | `ScSmMcDefinition_Reserved11` | TField |  |  |
| 30 | `SC.SMC.PAY.OUT.ROUTINE` | `ScSmMcDefinition_PayOutRoutine` | TField |  | This field is applicable only for structured note instruments The routine defined in this field will be invoked at the time of Note pay out processing. The logic within theroutine can be used to arrive at the pay-out price Validation Rules: if left blank, the value would default from SUB.ASSET.TYPE pay out routine field |
| 31 | `SC.SMC.INTEG.DATA.ITEM` | `ScSmMcDefinition_IntegDataItem` |  |  |  |
| 32 | `SC.SMC.INTEG.DATA.VALUE` | `ScSmMcDefinition_IntegDataValue` |  |  |  |
| 33 | `SC.SMC.COOL.CANCEL.PERIOD` | `ScSmMcDefinition_CoolCancelPeriod` | TField |  | This field indicates the Cooling Off period applicable for Unit Trusts / Mutual Funds and Debentures. Theinvestor has a right to cancel the contract within this period.Value in this field indicates that the issuer allowsa cooling-off or cancellation period for the instrument Validation Rules: This field accepts alpha numeric input of length 4 Input to this field must specify D for Days, M for Months, Y for Years as last character of input. The remainingshould be Numeric e.g. 360D meaning 360 Days |
| 34 | `SC.SMC.INSTRUMENT.TYPE` | `ScSmMcDefinition_InstrumentType` |  |  |  |
| 35 | `SC.SMC.INST.CLASSIFICATION` | `ScSmMcDefinition_InstClassification` |  |  |  |
| 36 | `SC.SMC.RESERVED12` | `ScSmMcDefinition_Reserved12` | TField |  |  |
| 37 | `SC.SMC.IPO.STATUS` | `ScSmMcDefinition_IpoStatus` | TField |  | This field indicates that the IPO is open, closed, alloted, listed, reopened and so on. |
| 38 | `SC.SMC.IPO.START.DATE` | `ScSmMcDefinition_IpoStartDate` | TField |  | Subscription opens on this date |
| 39 | `SC.SMC.IPO.START.TIME` | `ScSmMcDefinition_IpoStartTime` | TField |  | Subscriptions can be submitted after this time Only for information purpose |
| 40 | `SC.SMC.IPO.END.DATE` | `ScSmMcDefinition_IpoEndDate` | TField |  | IPO Book closes on this date It would be possible to amend this field. This would cater to the scenarios where the subscription window isextended on an adhoc basis This field would also act as the external cut-off date for the IPO |
| 41 | `SC.SMC.IPO.END.TIME` | `ScSmMcDefinition_IpoEndTime` | TField |  | Subscriptions cannot be submitted after this time Only for information purpose |
| 42 | `SC.SMC.TYPE.OF.ISSUE` | `ScSmMcDefinition_TypeOfIssue` | TField |  | When set to 'SINGLE BID', only one bid can be submitted per order. The bid can be placed only at the issue offerprice When set to 'BOOKBUILD', multiple bids can be placed, however, the price should be within the price band(MIN.OFFER.PRICE, MAX.OFFER.PRICE) Validation Rules Accept - SINGLEBID , BOOKBUILD |
| 43 | `SC.SMC.MIN.OFFER.PRICE` | `ScSmMcDefinition_MinOfferPrice` | TField |  | The minimum price that can be bid Validation Rules Input allowed only when type of issue is BOOKBUILD |
| 44 | `SC.SMC.MAX.OFFER.PRICE` | `ScSmMcDefinition_MaxOfferPrice` | TField |  | The maximum price that can be bid Validation Rules Input allowed only when type of issue is BOOKBUILD |
| 45 | `SC.SMC.ISSUE.OFFER.PRICE` | `ScSmMcDefinition_IssueOfferPrice` | TField |  | For fixed price issues, this is the fixed offer price Validation Rules Input allowed only when type of issue is SINGLEBID |
| 46 | `SC.SMC.MIN.INVESTMENT.VALUE` | `ScSmMcDefinition_MinInvestmentValue` | TField |  | Minimum subscription value of an application |
| 47 | `SC.SMC.MAX.INVESTMENT.VALUE` | `ScSmMcDefinition_MaxInvestmentValue` | TField |  | Maximum subscription value of an application |
| 48 | `SC.SMC.IPO.LOT.SIZE` | `ScSmMcDefinition_IpoLotSize` | TField |  | The minimum number of shares that can be bid. Shares can only be bid in multiples of the IPO.LOT.SIZE |
| 49 | `SC.SMC.IPO.ALLOTMENT.DATE` | `ScSmMcDefinition_IpoAllotmentDate` | TField |  | Shares will be allotted on this date. Only for information purpose |
| 50 | `SC.SMC.IPO.REFUND.DATE` | `ScSmMcDefinition_IpoRefundDate` | TField |  | Refund will be processed on this date Only for information purpose |
| 51 | `SC.SMC.IPO.LISTING.DATE` | `ScSmMcDefinition_IpoListingDate` | TField |  | Shares will be available for secondary market trading on this date. Only for information purpose |
| 52 | `SC.SMC.BLOCK.TYPE` | `ScSmMcDefinition_BlockType` | TField |  | When set to 'BLOCK', the funds will be blocked on the customer's account for the subscription amount When set to 'DEBIT', the funds will be debited from the customer's account. This field is applicable only for IPO Validation Rules Accept - BLOCK or DEBIT |
| 53 | `SC.SMC.DEBIT.TIME` | `ScSmMcDefinition_DebitTime` | TField |  | When set to 'Immediately', cash will be debited as soon as the transaction is authorized When set to 'Book Closure', cash will be debited on book closure date This field is applicable only for IPO Validation Rules Accept - IMMEDIATELY or BOOKCLOSURE Input allowed only when BLOCK.TYPE is set to 'DEBIT' |
| 54 | `SC.SMC.IPO.LEAD.MANAGER` | `ScSmMcDefinition_IpoLeadManager` | TField |  | This field will hold the details of the lead manager Only for information purpose |
| 55 | `SC.SMC.IPO.INT.CUT.OFF.DATE` | `ScSmMcDefinition_IpoIntCutOffDate` | TField |  | The fields holds the internal cut-off date. New orders are not allowed after this date. Existing orders can beamended. It would be possible to amend after authorization. Validation Rules This date cannot be later than IPO.END.DATE |
| 56 | `SC.SMC.IPO.INT.CUT.OFF.TIME` | `ScSmMcDefinition_IpoIntCutOffTime` | TField |  | The field holds the internal cut off time on the internal cut-off date. Only for information purpose |
| 57 | `SC.SMC.IPO.COMM.CODE` | `ScSmMcDefinition_IpoCommCode` | TField |  | The IPO application processing fee can set up in FT.COMMISSION.TYPE application and attached here Validation Rules Valid FT.COMMISSION.TYPE record |
| 58 | `SC.SMC.GRP.DEPT.CODE` | `ScSmMcDefinition_GrpDeptCode` |  |  |  |
| 59 | `SC.SMC.UPFRONT.INT.ACC` | `ScSmMcDefinition_UpfrontIntAcc` | TField |  | If this field is set, then when the order is placed for this security the system will automatically post entriesvia internal account for this order. Forward entry will be posted for customer account to block the funds. Validation: Accepted values : YES or Blank |
| 60 | `SC.SMC.SETTLEMENT.ACC` | `ScSmMcDefinition_SettlementAcc` | TField |  | This can be a Nostro or internal category account or any cash account. Validation: This field can only be given for funds |
| 61 | `SC.SMC.UPFRONT.INT.CATEG` | `ScSmMcDefinition_UpfrontIntCateg` | TField |  | When an order is placed for this security, System will debit the upfront amount from this internal account Validation: Will accept a valid internal account category This field can be input only if UPFRONT.INT.ACC is YES. |
| 62 | `SC.SMC.DEFAULT.DEPOSITORY` | `ScSmMcDefinition_DefaultDepository` | TField | No | Specifies the depository in which this particular stock is to be kept. Note: The user may override this Depository at transaction level. Validation Rules: 1-9 Numeric characters. (Optional input) The depository must exist on the CUSTOMER.SECURITY file and must have a CUSTOMER.TYPE Depository. |
| 63 | `SC.SMC.ISSUER` | `ScSmMcDefinition_Issuer` |  |  |  |
| 64 | `SC.SMC.LIMIT.REF` | `ScSmMcDefinition_LimitRef` |  |  |  |
| 65 | `SC.SMC.OV.ISSUER` | `ScSmMcDefinition_OvIssuer` | TField |  | Issuer to be used for performing issuer diversification checks. Input to be prefixed with I- for entering issuerfrom SC.ISSUER. Input to be prefixed with C- for entering T24 customer |
| 66 | `SC.SMC.INVEST.OPTION.TYPE` | `ScSmMcDefinition_InvestOptionType` |  |  |  |
| 67 | `SC.SMC.OPTION.DEPOSITORY` | `ScSmMcDefinition_OptionDepository` |  |  |  |
| 68 | `SC.SMC.RESERVED01` | `ScSmMcDefinition_Reserved01` | TField |  |  |
| 69 | `SC.SMC.RESERVED02` | `ScSmMcDefinition_Reserved02` | TField |  |  |
| 70 | `SC.SMC.RESERVED03` | `ScSmMcDefinition_Reserved03` | TField |  |  |
| 71 | `SC.SMC.RESERVED04` | `ScSmMcDefinition_Reserved04` | TField |  |  |
| 72 | `SC.SMC.RESERVED05` | `ScSmMcDefinition_Reserved05` | TField |  |  |
| 73 | `SC.SMC.RESERVED06` | `ScSmMcDefinition_Reserved06` | TField |  |  |
| 74 | `SC.SMC.RESERVED07` | `ScSmMcDefinition_Reserved07` | TField |  |  |
| 75 | `SC.SMC.RESERVED08` | `ScSmMcDefinition_Reserved08` | TField |  |  |
| 76 | `SC.SMC.RESERVED09` | `ScSmMcDefinition_Reserved09` | TField |  |  |
| 77 | `SC.SMC.RESERVED10` | `ScSmMcDefinition_Reserved10` | TField |  |  |
| 78 | `SC.SMC.LOCAL.REF` | `ScSmMcDefinition_LocalRef` |  |  |  |
| 79 | `SC.SMC.OVERRIDE` | `ScSmMcDefinition_Override` |  |  |  |
| 80 | `SC.SMC.RECORD.STATUS` | `ScSmMcDefinition_RecordStatus` | String |  |  |
| 81 | `SC.SMC.CURR.NO` | `ScSmMcDefinition_CurrNo` | String |  |  |
| 82 | `SC.SMC.INPUTTER` | `ScSmMcDefinition_Inputter` |  |  |  |
| 83 | `SC.SMC.DATE.TIME` | `ScSmMcDefinition_DateTime` |  |  |  |
| 84 | `SC.SMC.AUTHORISER` | `ScSmMcDefinition_Authoriser` | String |  |  |
| 85 | `SC.SMC.CO.CODE` | `ScSmMcDefinition_CoCode` | String |  |  |
| 86 | `SC.SMC.DEPT.CODE` | `ScSmMcDefinition_DeptCode` | String |  |  |
| 87 | `SC.SMC.AUDITOR.CODE` | `ScSmMcDefinition_AuditorCode` | String |  |  |
| 88 | `SC.SMC.AUDIT.DATE.TIME` | `ScSmMcDefinition_AuditDateTime` | String |  |  |
| 89 | `SC.SMC.ISSUER.LEI` | `ScSmMcDefinition_IssuerLei` | TField |  | When the field OV.ISSUER is populated with C-nnnnnn, where nnnnnn is the CUSTOMER.ID,then LEI of the customer will be populated in this field If LEI of the customer is available in OC.CUSTOMER record then the same will be populatedelse LEI from CUSTOMER record based on Legal doc Name will be populated The LEI will only be used for Reporting or for interfacing with Greenomyand will not replace the existing ISSUER functionality. Validation Rules: This field will be a no input field. |
