# REVALUATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.REVALUATION.PARAMETER` in `AC_CurrencyPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REVAL.P.APPLIC.ID` | `RevaluationParameter_ApplicId` |  |  |  |
| 2 | `REVAL.P.REVAL.TYPE` | `RevaluationParameter_RevalType` |  |  |  |
| 3 | `REVAL.P.REVAL.SYS.ID` | `RevaluationParameter_RevalSysId` |  |  |  |
| 4 | `REVAL.P.BOOK.PROFITS` | `RevaluationParameter_BookProfits` |  |  |  |
| 5 | `REVAL.P.POSTING.STYLE` | `RevaluationParameter_PostingStyle` |  |  |  |
| 6 | `REVAL.P.LOSS.CATEG` | `RevaluationParameter_LossCateg` |  |  |  |
| 7 | `REVAL.P.PRFT.CATEG` | `RevaluationParameter_PrftCateg` |  |  |  |
| 8 | `REVAL.P.LOSS.INT.CATEG` | `RevaluationParameter_LossIntCateg` |  |  |  |
| 9 | `REVAL.P.PRFT.INT.CATEG` | `RevaluationParameter_PrftIntCateg` |  |  |  |
| 10 | `REVAL.P.LOSS.PROD.CATEG` | `RevaluationParameter_LossProdCateg` |  |  |  |
| 11 | `REVAL.P.PRFT.PROD.CATEG` | `RevaluationParameter_PrftProdCateg` |  |  |  |
| 12 | `REVAL.P.LOSS.CR.TXN.CD` | `RevaluationParameter_LossCrTxnCd` |  |  |  |
| 13 | `REVAL.P.LOSS.DB.TXN.CD` | `RevaluationParameter_LossDbTxnCd` |  |  |  |
| 14 | `REVAL.P.PRFT.CR.TXN.CD` | `RevaluationParameter_PrftCrTxnCd` |  |  |  |
| 15 | `REVAL.P.PRFT.DB.TXN.CD` | `RevaluationParameter_PrftDbTxnCd` |  |  |  |
| 16 | `REVAL.P.LOSS.FIX.CAT` | `RevaluationParameter_LossFixCat` |  |  |  |
| 17 | `REVAL.P.PRFT.FIX.CAT` | `RevaluationParameter_PrftFixCat` |  |  |  |
| 18 | `REVAL.P.LOSS.FIX.INT.CT` | `RevaluationParameter_LossFixIntCt` |  |  |  |
| 19 | `REVAL.P.PRFT.FIX.INT.CT` | `RevaluationParameter_PrftFixIntCt` |  |  |  |
| 20 | `REVAL.P.REVAL.RATE` | `RevaluationParameter_RevalRate` |  |  |  |
| 21 | `REVAL.P.IFRS.REVALUE` | `RevaluationParameter_IfrsRevalue` | TField |  | If this field is set to 'YES', then the re-valuation profit or loss for Forex and Non Deliverable Forward Deals will be booked in Local currency at deal level. The deal level unrealized Profit or Loss will be booked at discounted value for Forex Deals under RB Method of Revaluation and for NDF Deals. For more details, Please refer to User Guide for FOREX Application. Values allowed are YES, NO and NULL. Will become a No Change field once the record is authorized with a value set to YES A value with NULL is same as value with NO. |
| 22 | `REVAL.P.FASB.REVALUATION` | `RevaluationParameter_FasbRevaluation` | TField | No | Defines whether the revaluation uses the mid rate or the bid and offer rates. YES = Bid and Offer rates NO = Mid rate (Default) Validation Rules: Valid values are 'Y'ES or 'N'O Optional input |
| 23 | `REVAL.P.REVAL.CCY` | `RevaluationParameter_RevalCcy` | TField | No | Defines whether the revaluation is calculated against the local currency or the currency specified. Validation Rules: 3 Alpha-numeric currency code (type CCY). Optional input Input can only be made if there are no POS.TRANSACTION records on the system. |
| 24 | `REVAL.P.REVAL.DEAL.POST` | `RevaluationParameter_RevalDealPost` | TField |  | Validation Rules: A maximum of 3 characters may be entered. The following values are permitted: YES NO |
| 25 | `REVAL.P.INTERPOLATION.MKR` | `RevaluationParameter_InterpolationMkr` | TField |  | Identifies whether forward exchange rates are to be interpolated or not. Interpolation occurs when a rate can be established from two known rates. For example, let us say that the one month forward rate for a particular currency is 1.50 and that the three month forward for the same currency is 1.60. Using interpolation, the two-month forward rate will be calculated at 1.55. The value of this marker is important for the revaluation of Forward contracts using the REBATE revaluation method. Details of the interpolation formula can be found in the Forex Main File documentation. When '2' has been selected in this field, revaluation of forward contracts using the Rebate revaluation method will not interpolate an exchange rate but instead, pick from the FORWARD.RATES table the rate defined on the nearest date compared to the value date of the Foreign Exchange deal. When '1' has been selected, the next available rate will instead be selected. Validation Rules: 'Blank' - Rate will be interpolated '1' - Takes the next available rate '2' - Takes the closest rate |
| 26 | `REVAL.P.DETAIL.REVAL.REP` | `RevaluationParameter_DetailRevalRep` | TField |  | Identifies the frequency for the production of the 'Detailed Revaluation Report' produced by the Forex End of Day process. Validation Rules: M - Monthly D - Daily |
| 27 | `REVAL.P.SPOT.REVAL.BOOKING` | `RevaluationParameter_SpotRevalBooking` | TField | Yes | Defines whether or not P/L and EXCHADS entries are to be booked when contracts with a REVALUATION TYPE that is NOT 'RB', are revalued. After authorisation of the record, if the value in this field is ever changed the original value used the last business day is retained in in the file REVAL.PARAM.ENT.TODAY Validation Rules: Valid values are 'Y'ES or 'N'O Mandatory input On Amending the field from YES to NO, during COB the outstanding revaluation Profit or Loss will be reversed and no further revaluation entries will be posted thereafter. On amending the field from NO to YES, system starts raising revaluation entries from there onwards |
| 28 | `REVAL.P.FWD.REVAL.BOOKING` | `RevaluationParameter_FwdRevalBooking` | TField | Yes | Defines whether or not P/L and EXCHADS entries are to be booked when contracts with a REVALUATION TYPE of 'RB' are revalued. After authorisation of this record, the value in this field is changed the original value is retained in the record of the REVAL.PARAM.ENT.TODAY file. Validation Rules: Valid values are 'Y'ES or 'N'O Mandatory Input On Amending the field from YES to NO, during COB the outstanding revaluation amount will be reversed and no further revaluation entries will be posted thereafter. On amending the field from NO to YES, system starts raising revaluation entries from there onwards. |
| 29 | `REVAL.P.POS.DATE.SAME.CCY` | `RevaluationParameter_PosDateSameCcy` | TField |  | Validation Rules: A maximum of 5 characters may be entered. The following values are permitted: CALL VALUE FIRST LAST |
| 30 | `REVAL.P.POS.DATE.DIFF.CCY` | `RevaluationParameter_PosDateDiffCcy` | TField |  | Validation Rules: A maximum of 5 characters may be entered. The following values are permitted: CALL VALUE FIRST LAST |
| 31 | `REVAL.P.SPLIT.POSITIONS` | `RevaluationParameter_SplitPositions` | TField | No | This field is used to default the value in the field SPLIT.POSITION in the application DEALER.DESK when a new DEALER.DESK record is created Validation Rules: YES, NO or NULL Optional Input Default is NULL |
| 32 | `REVAL.P.IFRS.DISC.RATE.KEY` | `RevaluationParameter_IfrsDiscRateKey` | TField | Yes | The key specified in this field is used to obtain the discount rate from PERIODIC.INTEREST table for the Local Currency. The value should be in the range from 01 to 99. Input not allowed when IFRS.REVALUE is not set; Input is Mandatory when IFRS.REVALUE is set to 'YES'. If the specified key for LOCAL currency does not exist in PI table, system raises the error message. |
| 33 | `REVAL.P.REVAL.WITHIN.SP` | `RevaluationParameter_RevalWithinSp` | TField |  | To indicate whether the contracts within spot period must be revalued at different rates for finer revaluation results. When set to �Yes�, the revaluation of contracts maturing TOM and SPOT will happen at different rates , provided the rates for �ON� and �TOM� are defined in FORWARD. RATES table as -1D and -2D. Provision is also available to calculate Today�s Rate by applying the sum of ON and TOM Premium/Discount to the Mid.Reval.Rate/Reval.Rate. However, population of the same into the field �Reval.Rate� is left to the User�s option which can be done by using a local routine. When left blank, the revaluation of contract within spot period will be revalued at spot rate i.e. contracts maturing Tomorrow and Spot will be revalued at the same rate. Validation Rules: Valid values - �YES� or �null� |
| 34 | `REVAL.P.IFRS.DISC.PERIOD` | `RevaluationParameter_IfrsDiscPeriod` | TField |  | To indicate whether the net unrealized revaluation amount must be discounted either from TODAY or SPOT to arrive the present value of the contracts under IFRS framework. When set to SPOT, the discounting of contracts in forward period will happen from spot date to value date and the contracts within the spot period will not be subjected to discounting. When set to TODAY, the discounting of contracts will happen from Today to value date, so the contracts either in spot period or forward period will be discounted from Today. Validation Rules:- Valid values are �TODAY� or �SPOT� Input allowed only when IFRS.REVALUE is set to �Yes�. |
| 35 | `REVAL.P.RESERVED.5` | `RevaluationParameter_Reserved5` |  |  |  |
| 36 | `REVAL.P.RESERVED.4` | `RevaluationParameter_Reserved4` |  |  |  |
| 37 | `REVAL.P.RESERVED.3` | `RevaluationParameter_Reserved3` |  |  |  |
| 38 | `REVAL.P.RESERVED.2` | `RevaluationParameter_Reserved2` |  |  |  |
| 39 | `REVAL.P.RESERVED.1` | `RevaluationParameter_Reserved1` | TField |  |  |
| 40 | `REVAL.P.LOCAL.REF` | `RevaluationParameter_LocalRef` |  |  |  |
| 41 | `REVAL.P.RECORD.STATUS` | `RevaluationParameter_RecordStatus` | String |  |  |
| 42 | `REVAL.P.CURR.NO` | `RevaluationParameter_CurrNo` | String |  |  |
| 43 | `REVAL.P.INPUTTER` | `RevaluationParameter_Inputter` |  |  |  |
| 44 | `REVAL.P.DATE.TIME` | `RevaluationParameter_DateTime` |  |  |  |
| 45 | `REVAL.P.AUTHORISER` | `RevaluationParameter_Authoriser` | String |  |  |
| 46 | `REVAL.P.CO.CODE` | `RevaluationParameter_CoCode` | String |  |  |
| 47 | `REVAL.P.DEPT.CODE` | `RevaluationParameter_DeptCode` | String |  |  |
| 48 | `REVAL.P.AUDITOR.CODE` | `RevaluationParameter_AuditorCode` | String |  |  |
| 49 | `REVAL.P.AUDIT.DATE.TIME` | `RevaluationParameter_AuditDateTime` | String |  |  |
