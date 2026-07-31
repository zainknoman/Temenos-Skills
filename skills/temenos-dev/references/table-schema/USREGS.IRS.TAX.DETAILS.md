# USREGS.IRS.TAX.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.IRS.TAX.DETAILS` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TX.DETS.DEPOSIT.INCOME` | `UsregsIrsTaxDetails_DepositIncome` | TField | No | Shows the Deposit Income or Interest income not included in BOND.INTEREST field Optional field Max 19 AMOUNT field |
| 2 | `TX.DETS.AMOUNT.REPAID` | `UsregsIrsTaxDetails_AmountRepaid` | TField | No | Shows if there is any Amount Repaid Optional field Max 19 AMOUNT field |
| 3 | `TX.DETS.FEDERAL.WHT` | `UsregsIrsTaxDetails_FederalWht` | TField | No | US Federal income tax withheld backup withholding or withholding on Indian gaming profits Optional field Max 19 AMOUNT field |
| 4 | `TX.DETS.OTHER.WHT` | `UsregsIrsTaxDetails_OtherWht` | TField | No | Shows any amount withheld by other agents Optional field Max 19 AMOUNT field |
| 5 | `TX.DETS.STATE.INCOME.TAX` | `UsregsIrsTaxDetails_StateIncomeTax` | TField | No | Shows the State Income tax amount Optional field Max 19 AMOUNT field |
| 6 | `TX.DETS.WITHDRAW.PENALTY` | `UsregsIrsTaxDetails_WithdrawPenalty` | TField | No | Shows if there is any Early withdrawal penalty Optional field Max 19 AMOUNT field |
| 7 | `TX.DETS.BOND.INTEREST` | `UsregsIrsTaxDetails_BondInterest` | TField | No | Interest on U.S. Savings Bonds and Treasury obligations Optional field Max 19 AMOUNT field |
| 8 | `TX.DETS.INVEST.EXPENSE` | `UsregsIrsTaxDetails_InvestExpense` | TField | No | Shows the Investment expenses occurred for the product Optional field Max 19 AMOUNT field |
| 9 | `TX.DETS.FOREIGN.TAX.PAID` | `UsregsIrsTaxDetails_ForeignTaxPaid` | TField | No | Shows any foreign tax paid Optional field Max 19 AMOUNT field |
| 10 | `TX.DETS.TAX.EXEMPT.INT` | `UsregsIrsTaxDetails_TaxExemptInt` | TField | No | Displays the tax exempt interest Exempt Interest Dividends Optional field Max 19 AMOUNT field |
| 11 | `TX.DETS.PRIVATE.ACT.BOND` | `UsregsIrsTaxDetails_PrivateActBond` | TField | No | Specified Private Activity Bond Specified Private Activity Bond Interest Dividend Optional field Max 19 AMOUNT field |
| 12 | `TX.DETS.SEC.199A.DIVIDENDS` | `UsregsIrsTaxDetails_Sec199aDividends` | TField | No | A qualified dividend under Section 199A of the Internal Revenue Code. Optional field Max 19 AMOUNT field |
| 13 | `TX.DETS.OBSOLETE.REC` | `UsregsIrsTaxDetails_ObsoleteRec` | TField | No | Yes or Null value allowed. If indicated as Yes, this tax record should be excluded from submission in the tax extract file. Optional field Max 19 AMOUNT field |
| 14 | `TX.DETS.UNIQUE.IDENTIFIER` | `UsregsIrsTaxDetails_UniqueIdentifier` | TField |  | The sequence number will be generated for form 1042-S by tax update service.This value will be used while tax file generation Max 10 Numeric field |
| 15 | `TX.DETS.GROSS.DISTRIB` | `UsregsIrsTaxDetails_GrossDistrib` | TField | No | Shows Gross Distribution amount Optional field Max 19 AMOUNT field |
| 16 | `TX.DETS.PROFIT.LOSS` | `UsregsIrsTaxDetails_ProfitLoss` | TField | No | Shows any Earnings or Loss occurred for the year Optional field Max 19 AMOUNT field |
| 17 | `TX.DETS.BASIS` | `UsregsIrsTaxDetails_Basis` | TField | No | Show Basis amount Optional field Max 19 AMOUNT field |
| 18 | `TX.DETS.TAXABLE.AMT` | `UsregsIrsTaxDetails_TaxableAmt` | TField | No | Shows the Taxable amount for the product Optional field Max 19 AMOUNT field |
| 19 | `TX.DETS.CAPITAL.GAIN` | `UsregsIrsTaxDetails_CapitalGain` | TField | No | Shows the ant Capital gain included in Amount Code 2 Optional field Max 19 AMOUNT field |
| 20 | `TX.DETS.ROTH.EMP.CONTRIB` | `UsregsIrsTaxDetails_RothEmpContrib` | TField | No | Shows the yearly Employee contributions for Roth contributions or insurance premiums Optional field Max 19 AMOUNT field |
| 21 | `TX.DETS.NET.UNREAL.PROFT` | `UsregsIrsTaxDetails_NetUnrealProft` | TField | No | Net unrealized appreciation on in employer�s securities Optional field Max 19 AMOUNT field |
| 22 | `TX.DETS.OTHER.IRA` | `UsregsIrsTaxDetails_OtherIra` | TField | No | Other IRA amount details Optional field Max 19 AMOUNT field |
| 23 | `TX.DETS.TOTAL.EMP.CONTRI` | `UsregsIrsTaxDetails_TotalEmpContri` | TField | No | Shows the Total employee contributions made for a financial year Optional field Max 19 AMOUNT field |
| 24 | `TX.DETS.IRA.DISTRIB` | `UsregsIrsTaxDetails_IraDistrib` | TField | No | Shows the amount which distributed to the customers from Traditional IRA/SEP/SIMPLE distribution or Roth Conversion Optional field Max 19 AMOUNT field |
| 25 | `TX.DETS.AMOUNT.IRR` | `UsregsIrsTaxDetails_AmountIrr` | TField | No | Amount allocable to IRR within 5 years Optional field Max 19 AMOUNT field |
| 26 | `TX.DETS.OTHER.IRA.CONTRI` | `UsregsIrsTaxDetails_OtherIraContri` | TField | No | Any IRA contributions other than amounts in Amount Codes 2, 3, 4, 8, 9, and A, C, and D. Optional field Max 19 AMOUNT field |
| 27 | `TX.DETS.ROLLOVER.CONTRI` | `UsregsIrsTaxDetails_RolloverContri` | TField | No | Shows any Rollover contributions made to the IRA for a year Optional field Max 19 AMOUNT field |
| 28 | `TX.DETS.ROTH.CONV.AMT` | `UsregsIrsTaxDetails_RothConvAmt` | TField | No | Roth conversion amount made to the IRA for a year Optional field Max 19 AMOUNT field |
| 29 | `TX.DETS.RECHAR.CONTRIB` | `UsregsIrsTaxDetails_RecharContrib` | TField | No | Displays Recharacterized contributions amount made to the IRA for a year Optional field Max 19 AMOUNT field |
| 30 | `TX.DETS.AC.FAIR.VALUE` | `UsregsIrsTaxDetails_AcFairValue` | TField | No | Fair market value of account Fair market value of property Optional field Max 19 AMOUNT field |
| 31 | `TX.DETS.LIFE.INS.COST` | `UsregsIrsTaxDetails_LifeInsCost` | TField | No | Life insurance cost included in Amount Code 1 Optional field Max 19 AMOUNT field |
| 32 | `TX.DETS.SEP.CONTRIB` | `UsregsIrsTaxDetails_SepContrib` | TField | No | Shows the amount which is contributed to SEP IRA Optional field Max 19 AMOUNT field |
| 33 | `TX.DETS.SIMPLE.CONTRIB` | `UsregsIrsTaxDetails_SimpleContrib` | TField | No | Shows the contributions amount made to the SIMPLE IRA accounts Optional field Max 19 AMOUNT field |
| 34 | `TX.DETS.ROTH.CONTRIB` | `UsregsIrsTaxDetails_RothContrib` | TField | No | Shows the contributions amount made to the ROTH IRA accounts Optional field Max 19 AMOUNT field |
| 35 | `TX.DETS.IRA.RMD` | `UsregsIrsTaxDetails_IraRmd` | TField | No | Display the amount which is eligible as RMD for an IRA holder. Optional field Max 19 AMOUNT field |
| 36 | `TX.DETS.POSTPONE.CONTRI` | `UsregsIrsTaxDetails_PostponeContri` | TField | No | Postponed Contribution amount if any Optional field Max 19 AMOUNT field |
| 37 | `TX.DETS.IRA.REPAY` | `UsregsIrsTaxDetails_IraRepay` | TField | No | Displays the repayment amount if any Optional field Max 19 AMOUNT field |
| 38 | `TX.DETS.ESA.CONTRIB` | `UsregsIrsTaxDetails_EsaContrib` | TField | No | Coverdell ESA contributions Optional field Max 19 AMOUNT field |
| 39 | `TX.DETS.ESA.ROLL.CONTRIB` | `UsregsIrsTaxDetails_EsaRollContrib` | TField | No | Rollover Contributions Optional field Max 19 AMOUNT field |
| 40 | `TX.DETS.ORD.DIVIDEND` | `UsregsIrsTaxDetails_OrdDividend` | TField | No | Total ordinary dividends Optional field Max 19 AMOUNT field |
| 41 | `TX.DETS.QUALFIED.DIVDEND` | `UsregsIrsTaxDetails_QualfiedDivdend` | TField | No | Qualified dividends Optional field Max 19 AMOUNT field |
| 42 | `TX.DETS.CAPTL.G.DISTR` | `UsregsIrsTaxDetails_CaptlGDistr` | TField | No | Total capital gain distribution Optional field Max 19 AMOUNT field |
| 43 | `TX.DETS.SEC.1250.GAIN` | `UsregsIrsTaxDetails_Sec1250Gain` | TField | No | Unrecaptured Section 1250 gain Optional field Max 19 AMOUNT field |
| 44 | `TX.DETS.SEC.1202.GAIN` | `UsregsIrsTaxDetails_Sec1202Gain` | TField | No | Section 1202 gain Optional field Max 19 AMOUNT field |
| 45 | `TX.DETS.COLLECTIBLE.GAIN` | `UsregsIrsTaxDetails_CollectibleGain` | TField | No | Collectibles (28% rate) gain Optional field Max 19 AMOUNT field |
| 46 | `TX.DETS.NONDIV.DISTRIB` | `UsregsIrsTaxDetails_NondivDistrib` | TField | No | Nondividend distributions Optional field Max 19 AMOUNT field |
| 47 | `TX.DETS.CASH.DISTRIB` | `UsregsIrsTaxDetails_CashDistrib` | TField | No | Cash liquidation distributions Optional field Max 19 AMOUNT field |
| 48 | `TX.DETS.NONCASH.DISTRIB` | `UsregsIrsTaxDetails_NoncashDistrib` | TField | No | Non-cash liquidation distributions Optional field Max 19 AMOUNT field |
| 49 | `TX.DETS.MORTGAGE.INTREST` | `UsregsIrsTaxDetails_MortgageIntrest` | TField | No | Mortgage interest received from payer(s)/borrower(s) Optional field Max 19 AMOUNT field |
| 50 | `TX.DETS.RESI.POINT.PAID` | `UsregsIrsTaxDetails_ResiPointPaid` | TField | No | Points paid on the purchase of a principal residence Optional field Max 19 AMOUNT field |
| 51 | `TX.DETS.REFUND.INTEREST` | `UsregsIrsTaxDetails_RefundInterest` | TField | No | Refund or credit of overpaid interest Optional field Max 19 AMOUNT field |
| 52 | `TX.DETS.INSURANCE.PREMIUM` | `UsregsIrsTaxDetails_InsurancePremium` | TField | No | Mortgage Insurance Premium amount for the year Optional field Max 19 AMOUNT field |
| 53 | `TX.DETS.PRINCIPAL.BAL` | `UsregsIrsTaxDetails_PrincipalBal` | TField | No | Displays the Balance of Principal Outstanding Optional field Max 19 AMOUNT field |
| 54 | `TX.DETS.DISCHARGE.DEBT` | `UsregsIrsTaxDetails_DischargeDebt` | TField | No | Shows the Amount of debt discharged Optional field Max 19 AMOUNT field |
| 55 | `TX.DETS.DEBT.INTEREST` | `UsregsIrsTaxDetails_DebtInterest` | TField | No | Interest, if included in amount of debt discharged Optional field Max 19 AMOUNT field |
| 56 | `TX.DETS.RENT` | `UsregsIrsTaxDetails_Rent` | TField | No | Shows the Rental income Optional field Max 19 AMOUNT field |
| 57 | `TX.DETS.ROYALTY` | `UsregsIrsTaxDetails_Royalty` | TField | No | Shows the Royalty income Optional field Max 19 AMOUNT field |
| 58 | `TX.DETS.OTHER.INCOME` | `UsregsIrsTaxDetails_OtherIncome` | TField | No | Other income , if any Optional field Max 19 AMOUNT field |
| 59 | `TX.DETS.BOAT.SALE` | `UsregsIrsTaxDetails_BoatSale` | TField | No | Income from Fishing boat proceeds Optional field Max 19 AMOUNT field |
| 60 | `TX.DETS.MEDICAL.PAYMENTS` | `UsregsIrsTaxDetails_MedicalPayments` | TField | No | Medical and health care payments Optional field Max 19 AMOUNT field |
| 61 | `TX.DETS.NONEMP.COMPENSAT` | `UsregsIrsTaxDetails_NonempCompensat` | TField | No | Nonemployee compensation Optional field Max 19 AMOUNT field |
| 62 | `TX.DETS.SUBSTITUTE.PAY` | `UsregsIrsTaxDetails_SubstitutePay` | TField | No | Substitute payments in lieu of dividends or interest Optional field Max 19 AMOUNT field |
| 63 | `TX.DETS.CROP.INSURANCE` | `UsregsIrsTaxDetails_CropInsurance` | TField | No | Crop insurance proceeds Optional field Max 19 AMOUNT field |
| 64 | `TX.DETS.GOLDEN.PARACHUTE` | `UsregsIrsTaxDetails_GoldenParachute` | TField | No | Excess golden parachute payment Optional field Max 19 AMOUNT field |
| 65 | `TX.DETS.ATTORNEY.FEE` | `UsregsIrsTaxDetails_AttorneyFee` | TField | No | Gross proceeds paid to an attorney in connection with legal services Optional field Max 19 AMOUNT field |
| 66 | `TX.DETS.SEC.409A.DEFFERED` | `UsregsIrsTaxDetails_Sec409aDeffered` | TField | No | Shows Section 409A Deferrals Optional field Max 19 AMOUNT field |
| 67 | `TX.DETS.SEC.409A.INCOME` | `UsregsIrsTaxDetails_Sec409aIncome` | TField | No | Shows Section 409A Income Optional field Max 19 AMOUNT field |
| 68 | `TX.DETS.Q.RETURN.TYPE.IND` | `UsregsIrsTaxDetails_QReturnTypeInd` | TField |  | Shows the type of return Values 0 or 1 Max 1 numeric character |
| 69 | `TX.DETS.CORRECTED.RETURN.IND` | `UsregsIrsTaxDetails_CorrectedReturnInd` | TField |  | G or Blank Max 1 alpha character |
| 70 | `TX.DETS.PERSON.LIAB.IND` | `UsregsIrsTaxDetails_PersonLiabInd` | TField |  | Personal Liability Indicator Values 1 or Blank |
| 71 | `TX.DETS.DATE.OF.EVENT` | `UsregsIrsTaxDetails_DateOfEvent` | TField |  | Date for the event held Max 11 DATE format |
| 72 | `TX.DETS.DESCRIPTION` | `UsregsIrsTaxDetails_Description` | TField |  | Description about the products and filing Max 35 alphanumeric characters |
| 73 | `TX.DETS.IDENT.EVENT.CODE` | `UsregsIrsTaxDetails_IdentEventCode` | TField |  | Shows the any Event Code |
| 74 | `TX.DETS.OLD.TIN` | `UsregsIrsTaxDetails_OldTin` | TField | No | Shows the any old TIN number Optional field Max 9 numeric characters |
| 75 | `TX.DETS.PAYEE.ACC` | `UsregsIrsTaxDetails_PayeeAcc` | TField |  | Shows the unique Payee account number for B record Max 20 numeric characters |
| 76 | `TX.DETS.IRA.RMD.DATE` | `UsregsIrsTaxDetails_IraRmdDate` | TField |  |  |
| 77 | `TX.DETS.BONUS` | `UsregsIrsTaxDetails_Bonus` | TField |  |  |
| 78 | `TX.DETS.CHANGE.DATE` | `UsregsIrsTaxDetails_ChangeDate` | TField |  | The Bank date will be stored in this field. This will allow any extraction processes to select the data that has been modified. System update field; not available for user input. |
| 79 | `TX.DETS.CUSTOMER.CORRECTED` | `UsregsIrsTaxDetails_CustomerCorrected` | TField |  | The field should be flagged if the in case the change is made after the tax forms have been mailed to the customer. Once the correction made, user will flag the field. |
| 80 | `TX.DETS.CORRECTION.FILED` | `UsregsIrsTaxDetails_CorrectionFiled` | TField |  | Flag to indicate the correction has already extracted by IRS file generation process. It will be updated by the process which generate the IRS Fire file The flag will reset when user make any correction in the tax data. Allowed value is Y or null. |
| 81 | `TX.DETS.YEAR` | `UsregsIrsTaxDetails_Year` | TField |  | Year from record id will be stored here. This will allow any extraction process to select data of a year. System populate the value; Not input able to the user. |
| 82 | `TX.DETS.FORM.TYPE` | `UsregsIrsTaxDetails_FormType` | TField |  | Form type from record id will be stored here. This will allow any extraction process to select data of a specific form. System populate the value; Not input able to the user. |
| 83 | `TX.DETS.CUSTOMER` | `UsregsIrsTaxDetails_Customer` | TField |  | Customer id from record id will be stored here. This will allow any extraction process to select data of a customer. System populate the value; Not input able to the user. |
| 84 | `TX.DETS.ACCOUNT` | `UsregsIrsTaxDetails_Account` | TField |  | Account id from record id will be stored here. This will allow any extraction process to select data of an Account. System populate the value; Not input able to the user. |
| 85 | `TX.DETS.STATE` | `UsregsIrsTaxDetails_State` | TField |  | US State from record id will be stored here. This will allow any extraction process to select data of a state. System populate the value; Not input able to the user. |
| 86 | `TX.DETS.POSTPONE.CONTRIB.YEAR` | `UsregsIrsTaxDetails_PostponeContribYear` | TField | No | Year of postponed contribution Optional field 4 Digits Numeric field |
| 87 | `TX.DETS.POSTPONE.CONTRIB.CODE` | `UsregsIrsTaxDetails_PostponeContribCode` | TField | No | The code used for postponed contribution Optional field Linked to EB.LOOKUP table POSTPONE.CONTRIB.CODE |
| 88 | `TX.DETS.POSTPONE.CONTRIB.REASON` | `UsregsIrsTaxDetails_PostponeContribReason` | TField | No | The federally declared disaster area, public law number or executive order number will be stored in this field Optional field 6 digits Alphanumeric field |
| 89 | `TX.DETS.LOCAL.REF` | `UsregsIrsTaxDetails_LocalRef` |  |  |  |
| 90 | `TX.DETS.OVERRIDE` | `UsregsIrsTaxDetails_Override` |  |  |  |
| 91 | `TX.DETS.RECORD.STATUS` | `UsregsIrsTaxDetails_RecordStatus` | String |  |  |
| 92 | `TX.DETS.CURR.NO` | `UsregsIrsTaxDetails_CurrNo` | String |  |  |
| 93 | `TX.DETS.INPUTTER` | `UsregsIrsTaxDetails_Inputter` |  |  |  |
| 94 | `TX.DETS.DATE.TIME` | `UsregsIrsTaxDetails_DateTime` |  |  |  |
| 95 | `TX.DETS.AUTHORISER` | `UsregsIrsTaxDetails_Authoriser` | String |  |  |
| 96 | `TX.DETS.CO.CODE` | `UsregsIrsTaxDetails_CoCode` | String |  |  |
| 97 | `TX.DETS.DEPT.CODE` | `UsregsIrsTaxDetails_DeptCode` | String |  |  |
| 98 | `TX.DETS.AUDITOR.CODE` | `UsregsIrsTaxDetails_AuditorCode` | String |  |  |
| 99 | `TX.DETS.AUDIT.DATE.TIME` | `UsregsIrsTaxDetails_AuditDateTime` | String |  |  |
| 100 | `TX.DETS.AMENDMENT.NO` | `UsregsIrsTaxDetails_AmendmentNo` | TField |  | Amendment number, updates the value by 1 each time correction is done 1 digit numeric field |
