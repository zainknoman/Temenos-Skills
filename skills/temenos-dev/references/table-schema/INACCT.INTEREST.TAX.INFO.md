# INACCT.INTEREST.TAX.INFO — Table Schema

> Source: `INSERTS/I_F.INACCT.INTEREST.TAX.INFO` in `INACCT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INACCT.INT.TAX.ARRANGEMENT.NO` | `InacctInterestTaxInfo_ArrangementNo` |  |  |  |
| 2 | `INACCT.INT.TAX.INTEREST.CAPITALISED.DATE` | `InacctInterestTaxInfo_InterestCapitalisedDate` |  |  |  |
| 3 | `INACCT.INT.TAX.INTEREST.CAPITALISED` | `InacctInterestTaxInfo_InterestCapitalised` |  |  |  |
| 4 | `INACCT.INT.TAX.TDS.DEDUCTED` | `InacctInterestTaxInfo_TdsDeducted` |  |  |  |
| 5 | `INACCT.INT.TAX.RESERVED.16` | `InacctInterestTaxInfo_Reserved16` |  |  |  |
| 6 | `INACCT.INT.TAX.RESERVED.15` | `InacctInterestTaxInfo_Reserved15` |  |  |  |
| 7 | `INACCT.INT.TAX.RESERVED.14` | `InacctInterestTaxInfo_Reserved14` |  |  |  |
| 8 | `INACCT.INT.TAX.PREV.INT.AMT` | `InacctInterestTaxInfo_PrevIntAmt` |  |  |  |
| 9 | `INACCT.INT.TAX.PREV.TDS.AMT` | `InacctInterestTaxInfo_PrevTdsAmt` |  |  |  |
| 10 | `INACCT.INT.TAX.TAX.RVRSL.SUSP.ACC` | `InacctInterestTaxInfo_TaxRvrslSuspAcc` |  |  |  |
| 11 | `INACCT.INT.TAX.TAX.RVRSL.CUS.ACC` | `InacctInterestTaxInfo_TaxRvrslCusAcc` |  |  |  |
| 12 | `INACCT.INT.TAX.TAX.RVRSL.DATE` | `InacctInterestTaxInfo_TaxRvrslDate` |  |  |  |
| 13 | `INACCT.INT.TAX.THRESHOLD.AMOUNT` | `InacctInterestTaxInfo_ThresholdAmount` | TField |  | This will be calcualte the Threshold Amount for each year. |
| 14 | `INACCT.INT.TAX.CUST.TAX.GEN.ID` | `InacctInterestTaxInfo_CustTaxGenId` | TField |  | Contains the TAX.GEN.ID of the customer, TAX.GEN.CONDITION application is used to group the customer for the purposes of levying taxes. |
| 15 | `INACCT.INT.TAX.CUST.TAX.CODE` | `InacctInterestTaxInfo_CustTaxCode` | TField |  | Contains the TAX.CODE of the customer. |
| 16 | `INACCT.INT.TAX.CUST.TAX.RATE` | `InacctInterestTaxInfo_CustTaxRate` | TField |  | Contains the tax rate of the Customer. |
| 17 | `INACCT.INT.TAX.FORM.13.APPL` | `InacctInterestTaxInfo_Form13Appl` | TField |  | Y-If customer has submitted FORM 13 N-If customer has No FORM 13 |
| 18 | `INACCT.INT.TAX.RESERVED.3` | `InacctInterestTaxInfo_Reserved3` | TField |  | Reserved for future use. |
| 19 | `INACCT.INT.TAX.RESERVED.2` | `InacctInterestTaxInfo_Reserved2` | TField |  | Reserved for future use. |
| 20 | `INACCT.INT.TAX.RESERVED.1` | `InacctInterestTaxInfo_Reserved1` | TField |  | Reserved for future use. |
| 21 | `INACCT.INT.TAX.INTEREST.ACCR.DATE` | `InacctInterestTaxInfo_InterestAccrDate` |  |  |  |
| 22 | `INACCT.INT.TAX.INTEREST.ACCRUED` | `InacctInterestTaxInfo_InterestAccrued` |  |  |  |
| 23 | `INACCT.INT.TAX.ACCR.INT.TDS.DEDUCTED` | `InacctInterestTaxInfo_AccrIntTdsDeducted` |  |  |  |
| 24 | `INACCT.INT.TAX.INT.ACCR.REVERSAL` | `InacctInterestTaxInfo_IntAccrReversal` |  |  |  |
| 25 | `INACCT.INT.TAX.PREV.TAX.YEAR.INTEREST.ACCRUED` | `InacctInterestTaxInfo_PrevTaxYearInterestAccrued` |  |  |  |
| 26 | `INACCT.INT.TAX.PREV.TAX.YEAR.ACCR.INT.TDS` | `InacctInterestTaxInfo_PrevTaxYearAccrIntTds` |  |  |  |
| 27 | `INACCT.INT.TAX.ACC.INT.TDS.REVERSED.DATE` | `InacctInterestTaxInfo_AccIntTdsReversedDate` |  |  |  |
| 28 | `INACCT.INT.TAX.ACC.INT.TDS.REVERSED.AMOUNT` | `InacctInterestTaxInfo_AccIntTdsReversedAmount` |  |  |  |
| 29 | `INACCT.INT.TAX.PREV.TAX.YEAR.INT.ACCR.RVRSL` | `InacctInterestTaxInfo_PrevTaxYearIntAccrRvrsl` |  |  |  |
| 30 | `INACCT.INT.TAX.FORM.13.RATE` | `InacctInterestTaxInfo_Form13Rate` |  |  |  |
| 31 | `INACCT.INT.TAX.ARRANGEMENT.CURRENCY` | `InacctInterestTaxInfo_ArrangementCurrency` |  |  |  |
| 32 | `INACCT.INT.TAX.PENDING.INT.TAX.INDICATOR` | `InacctInterestTaxInfo_PendingIntTaxIndicator` |  |  |  |
| 33 | `INACCT.INT.TAX.TOT.PEN.INT.TAX.AMT.ADJ` | `InacctInterestTaxInfo_TotPenIntTaxAmtAdj` |  |  |  |
| 34 | `INACCT.INT.TAX.LATEST.PENDING.TXN.DATE` | `InacctInterestTaxInfo_LatestPendingTxnDate` |  |  |  |
| 35 | `INACCT.INT.TAX.LATEST.PENDING.INT.TAX.AMT` | `InacctInterestTaxInfo_LatestPendingIntTaxAmt` |  |  |  |
| 36 | `INACCT.INT.TAX.PEN.TAX.RECVD.FROM.MAINTAX` | `InacctInterestTaxInfo_PenTaxRecvdFromMaintax` |  |  |  |
| 37 | `INACCT.INT.TAX.INT.CAP.TILL.DATE` | `InacctInterestTaxInfo_IntCapTillDate` |  |  |  |
