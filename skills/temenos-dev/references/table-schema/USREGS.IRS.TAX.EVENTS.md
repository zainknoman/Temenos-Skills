# USREGS.IRS.TAX.EVENTS — Table Schema

> Source: `INSERTS/I_F.USREGS.IRS.TAX.EVENTS` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TX.EVNT.CUSTOMER` | `UsregsIrsTaxEvents_Customer` | TField | Yes | Shows the valid customer number Must be a valid T24 customer. Mandatory field Max 10 Numeric characters |
| 2 | `TX.EVNT.TAX.FORM.TYPE` | `UsregsIrsTaxEvents_TaxFormType` | TField | Yes | Shows the list of Tax Form Types. Dropdown Field Must have dropdown values from USREGS.TAX.FORM.TYPE - Allowed values: 1099A, 1099C, 1099INT, 1099DIV, 1099MISC Mandatory field Max 8 alphanumeric characters |
| 3 | `TX.EVNT.YEAR` | `UsregsIrsTaxEvents_Year` | TField | Yes | Indicates the year of tax. Mandatory field. Max 4 numeric characters |
| 4 | `TX.EVNT.VALUE.DATE` | `UsregsIrsTaxEvents_ValueDate` | TField | Yes | Shows the Date on which the event happened, For example Date of Lender�s Acquisition or Knowledge of Abandonment for 1099-A)/Identifiable Event date for 1099-C or Value date of the tax entry for others. This is a mandatory field. Max 11 DATE field |
| 5 | `TX.EVNT.ORD.DIVIDEND` | `UsregsIrsTaxEvents_OrdDividend` | TField | No | Shows total ordinary dividends that are taxable for IRS form 1099DIV Optional field, This is applicable only to form 1099DIV. Max 19 AMOUNT field |
| 6 | `TX.EVNT.QUALIFIED.DIVIDEND` | `UsregsIrsTaxEvents_QualifiedDividend` | TField | No | Shows the portion of the amount in total ordinary dividends that may be eligible for reduced capital gains rates. for IRS form 1099DIV Optional field, This is applicable only to form 1099DIV Max 19 AMOUNT field |
| 7 | `TX.EVNT.CAPITAL.GAIN.DISTRIB` | `UsregsIrsTaxEvents_CapitalGainDistrib` | TField | No | Shows total capital gain distributions from a regulated investment company or real estate investment trust for IRS form 1099DIV Optional field, This is applicable only to form 1099DIV Max 19 AMOUNT field |
| 8 | `TX.EVNT.SEC.1250.GAIN` | `UsregsIrsTaxEvents_Sec1250Gain` | TField | No | Shows the portion of the amount in b total capital gain distributions ox 2a that is unrecaptured section 1250 gain from certain depreciable real property for 1099DIV Optional field, This is applicable only to form 1099DIV Max 19 AMOUNT field |
| 9 | `TX.EVNT.SEC.1202.GAIN` | `UsregsIrsTaxEvents_Sec1202Gain` | TField | No | Shows the portion of the amount in total capital gain distributions that is section 1202 gain from certain small business stock that may be subject to an exclusion for 1099DIV Optional field Max 19 AMOUNT field |
| 10 | `TX.EVNT.COLLECTIBLE.GAIN` | `UsregsIrsTaxEvents_CollectibleGain` | TField | No | Shows 28% rate gain from sales or exchanges of collectibles. If required for 1099DIV Optional field Max 19 AMOUNT field |
| 11 | `TX.EVNT.NONDIV.DISTRIB` | `UsregsIrsTaxEvents_NondivDistrib` | TField | No | Shows the part of the distribution that is nontaxable because it is a return of your cost (or other basis). Optional field Max 19 AMOUNT field |
| 12 | `TX.EVNT.FEDERAL.WHT` | `UsregsIrsTaxEvents_FederalWht` | TField | No | Shows backup withholding. A payer must backup withhold on certain payments if you did not give your taxpayer identification number to the payer for 1099DIV / backup withholding or withholding on Indian gaming profits for 1099MISC Optional field Max 19 AMOUNT field |
| 13 | `TX.EVNT.INVEST.EXPENSE` | `UsregsIrsTaxEvents_InvestExpense` | TField | No | Shows your share of expenses of a nonpublicly offered regulated investment company, generally a nonpublicly offered mutual fund. for 1099DIV Optional field Max 19 AMOUNT field |
| 14 | `TX.EVNT.FOREIGN.TAX.PAID` | `UsregsIrsTaxEvents_ForeignTaxPaid` | TField | No | Shows the foreign tax that you may be able to claim as a deduction or a credit on Form 1040. Optional field Max 19 AMOUNT field |
| 15 | `TX.EVNT.CASH.DISTRIB` | `UsregsIrsTaxEvents_CashDistrib` | TField | No | Shows Cash liquidation distributions for 1099DIV Optional field Max 19 AMOUNT field |
| 16 | `TX.EVNT.NONCASH.DISTRIB` | `UsregsIrsTaxEvents_NoncashDistrib` | TField | No | Shows Non-cash liquidation distributions for 1099DIV Optional field Max 19 AMOUNT field |
| 17 | `TX.EVNT.TAX.EXEMPT.INT` | `UsregsIrsTaxEvents_TaxExemptInt` | TField | No | Shows exempt-interest dividends from a mutual fund or other regulated investment company paid to you during the calendar year. Optional field Max 19 AMOUNT field |
| 18 | `TX.EVNT.PRIVATE.ACT.BOND` | `UsregsIrsTaxEvents_PrivateActBond` | TField |  | Shows exempt-interest dividends subject to the alternative minimum tax for Specified Private Activity Bond Interest Dividend. Max 19 AMOUNT field |
| 19 | `TX.EVNT.NONEMP.COMPENSATE` | `UsregsIrsTaxEvents_NonempCompensate` | TField | No | Shows nonemployee compensation such as fees, commissions, prizes and awards for services performed as a nonemployee, other forms of compensation for services performed for your trade or business by an individual who is not your employee for 1099MISC Optional field Max 19 AMOUNT field |
| 20 | `TX.EVNT.BOND.INTEREST` | `UsregsIrsTaxEvents_BondInterest` | TField | No | Shows interest on U.S. Savings Bonds, Treasury bills, Treasury notes, and Treasury bonds. for 1099INT Optional field Max 19 AMOUNT field |
| 21 | `TX.EVNT.PRINCIPAL.BAL` | `UsregsIrsTaxEvents_PrincipalBal` | TField | No | The balance of the debt outstanding at the time the interest in the property was acquired or abandoned for 1099A Optional field Max 19 AMOUNT field |
| 22 | `TX.EVNT.AC.FAIR.VALUE` | `UsregsIrsTaxEvents_AcFairValue` | TField | No | Fair market value (FMV) of Property For a foreclosure, execution, or similar sale for 1099A and 1099C Optional field Max 19 AMOUNT field |
| 23 | `TX.EVNT.DISCHARGE.DEBT` | `UsregsIrsTaxEvents_DischargeDebt` | TField | No | The amount of the cancelled debt. The amount of the cancelled debt cannot be greater than the total debt less any amount the lender receives in satisfaction of the debt by means of a settlement agreement,foreclosure sale, a short sale that partially satisfied the debt, etc. for 1099C Optional field Max 19 AMOUNT field |
| 24 | `TX.EVNT.DEBT.INTEREST` | `UsregsIrsTaxEvents_DebtInterest` | TField | No | Shows any interest you included in the canceled debt for 1099C Optional field Max 19 AMOUNT field |
| 25 | `TX.EVNT.Q.RETURN.TYPE.IND` | `UsregsIrsTaxEvents_QReturnTypeInd` | TField |  | Shows the type of return Radio button 0 or 1 Max 1 numeric character |
| 26 | `TX.EVNT.CORRECTED.RETURN.IND` | `UsregsIrsTaxEvents_CorrectedReturnInd` | TField |  | Indicates corrected return type:G or Blank Max 1 character |
| 27 | `TX.EVNT.PERSON.LIAB.IND` | `UsregsIrsTaxEvents_PersonLiabInd` | TField | Yes | Shows If the debtor was personally liable for repayment of the debt at the time the debt was created or, if modified, at the time of the last modification, Radio button 1 or Blank. Only for 1099A and 1099C.Default option �Blank� Mandatory field |
| 28 | `TX.EVNT.DESCRIPTION` | `UsregsIrsTaxEvents_Description` | TField |  | A general description of the property. For real property, generally you must enter the address of the property, (1099-A) / description of the origin of the debt, such as student loan, mortgage, or credit card expenditure for 1099C Text field Max 40 alphanumeric characters |
| 29 | `TX.EVNT.IDENT.EVENT.CODE` | `UsregsIrsTaxEvents_IdentEventCode` | TField | Yes | Shows the appropriate code to report the nature of the identifiable event. Drop down values from EB.LOOKUP - IDENT.EVNT.CD Mandatory for 1099C only. |
| 30 | `TX.EVNT.PAYEE.ACC.NO` | `UsregsIrsTaxEvents_PayeeAccNo` | TField | No | Holds the USREGS.IRS.TAX.DETAILS id for corrected returns Optional field Max 35 alphanumeric characters. |
| 31 | `TX.EVNT.SEC.199A.DIVIDENDS` | `UsregsIrsTaxEvents_Sec199aDividends` | TField | No | A qualified dividend under Section 199A of the Internal Revenue Code. Optional field Max 19 AMOUNT field |
| 32 | `TX.EVNT.RESERVED.14` | `UsregsIrsTaxEvents_Reserved14` | TField |  |  |
| 33 | `TX.EVNT.RESERVED.13` | `UsregsIrsTaxEvents_Reserved13` | TField |  |  |
| 34 | `TX.EVNT.RESERVED.12` | `UsregsIrsTaxEvents_Reserved12` | TField |  |  |
| 35 | `TX.EVNT.RESERVED.11` | `UsregsIrsTaxEvents_Reserved11` | TField |  |  |
| 36 | `TX.EVNT.RESERVED.10` | `UsregsIrsTaxEvents_Reserved10` | TField |  |  |
| 37 | `TX.EVNT.RESERVED.9` | `UsregsIrsTaxEvents_Reserved9` | TField |  |  |
| 38 | `TX.EVNT.RESERVED.8` | `UsregsIrsTaxEvents_Reserved8` | TField |  |  |
| 39 | `TX.EVNT.RESERVED.7` | `UsregsIrsTaxEvents_Reserved7` | TField |  |  |
| 40 | `TX.EVNT.RESERVED.6` | `UsregsIrsTaxEvents_Reserved6` | TField |  |  |
| 41 | `TX.EVNT.RESERVED.5` | `UsregsIrsTaxEvents_Reserved5` | TField |  |  |
| 42 | `TX.EVNT.RESERVED.4` | `UsregsIrsTaxEvents_Reserved4` | TField |  |  |
| 43 | `TX.EVNT.RESERVED.3` | `UsregsIrsTaxEvents_Reserved3` | TField |  |  |
| 44 | `TX.EVNT.RESERVED.2` | `UsregsIrsTaxEvents_Reserved2` | TField |  |  |
| 45 | `TX.EVNT.LOCAL.REF` | `UsregsIrsTaxEvents_LocalRef` |  |  |  |
| 46 | `TX.EVNT.OVERRIDE` | `UsregsIrsTaxEvents_Override` |  |  |  |
| 47 | `TX.EVNT.RECORD.STATUS` | `UsregsIrsTaxEvents_RecordStatus` | String |  |  |
| 48 | `TX.EVNT.CURR.NO` | `UsregsIrsTaxEvents_CurrNo` | String |  |  |
| 49 | `TX.EVNT.INPUTTER` | `UsregsIrsTaxEvents_Inputter` |  |  |  |
| 50 | `TX.EVNT.DATE.TIME` | `UsregsIrsTaxEvents_DateTime` |  |  |  |
| 51 | `TX.EVNT.AUTHORISER` | `UsregsIrsTaxEvents_Authoriser` | String |  |  |
| 52 | `TX.EVNT.CO.CODE` | `UsregsIrsTaxEvents_CoCode` | String |  |  |
| 53 | `TX.EVNT.DEPT.CODE` | `UsregsIrsTaxEvents_DeptCode` | String |  |  |
| 54 | `TX.EVNT.AUDITOR.CODE` | `UsregsIrsTaxEvents_AuditorCode` | String |  |  |
| 55 | `TX.EVNT.AUDIT.DATE.TIME` | `UsregsIrsTaxEvents_AuditDateTime` | String |  |  |
