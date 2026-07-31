# CHSTMP.TAX.STATEMENT — Table Schema

> Source: `INSERTS/I_F.CHSTMP.TAX.STATEMENT` in `CHSTMP_SwissTaxStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAXSTMT.TXN.TYPE` | `ChstmpTaxStatement_TxnType` | TField |  | The field will hold the transaction description. |
| 2 | `TAXSTMT.DEPOSIT.CCY` | `ChstmpTaxStatement_DepositCcy` | TField |  | Deposit currency. |
| 3 | `TAXSTMT.LOAN.CCY` | `ChstmpTaxStatement_LoanCcy` | TField |  | Loan currency. |
| 4 | `TAXSTMT.BAL.EOY` | `ChstmpTaxStatement_BalEoy` | TField |  | Account balance determined during the end of the year in the account currency value. The field gets updated for the arrangement accounts. |
| 5 | `TAXSTMT.INT.PAID` | `ChstmpTaxStatement_IntPaid` | TField |  | Interest paid in the account currency value. The field gets updated for the arrangement accounts. |
| 6 | `TAXSTMT.FX.RATE` | `ChstmpTaxStatement_FxRate` | TField |  | Foreign exchange rate as on the transaction date to convert to CHF value. |
| 7 | `TAXSTMT.CURRENCY` | `ChstmpTaxStatement_Currency` | TField |  | Field always shows the local currency value as the statement is generated in local currency. |
| 8 | `TAXSTMT.BAL.EOY.CHF` | `ChstmpTaxStatement_BalEoyChf` | TField |  | Year end account or loan balance in local currency converted using the exchange rate as of the year end. |
| 9 | `TAXSTMT.INT.PAID.CHF` | `ChstmpTaxStatement_IntPaidChf` | TField |  | Interest paid for the loan in local currency converted using the exchange rate as of the transaction date. |
| 10 | `TAXSTMT.NOMINALS` | `ChstmpTaxStatement_Nominals` | TField |  | Year beginning or end balance position. If no balance during the year beginning or end,then the field will be updated as 0. |
| 11 | `TAXSTMT.TAX.VALUE.PER.SHARE` | `ChstmpTaxStatement_TaxValuePerShare` | TField |  | The field will hold the fiscal price received from the SIX serrver, with which the year end valuation is calculated. |
| 12 | `TAXSTMT.TAXABLE.VALUE` | `ChstmpTaxStatement_TaxableValue` | TField |  | Market value in local currency calculated using the fiscal price. |
| 13 | `TAXSTMT.SWISS.WHT.TAX` | `ChstmpTaxStatement_SwissWhtTax` | TField |  | The field gets updated for the swiss instruments. The field shows the withholding tax paid or deducted. |
| 14 | `TAXSTMT.RECLAIM.WHT.TAX` | `ChstmpTaxStatement_ReclaimWhtTax` | TField |  | Reclaimable Tax amount that is the investor is eligible to claim. |
| 15 | `TAXSTMT.WHLD.PERC` | `ChstmpTaxStatement_WhldPerc` | TField |  | The field shows the withholding tax percentage that was used to calculate the withholding tax amount for the Foreign or US instruments. |
| 16 | `TAXSTMT.WHLD.AMT` | `ChstmpTaxStatement_WhldAmt` | TField |  | Withholding tax amount for the foreign instruments calculated during the diary event. |
| 17 | `TAXSTMT.WHLD.CREDIT` | `ChstmpTaxStatement_WhldCredit` | TField |  | Withholding tax credit. |
| 18 | `TAXSTMT.ADD.US.WHLD.TAX` | `ChstmpTaxStatement_AddUsWhldTax` | TField |  | Additional US withholding tax amount deducted for the US investments. |
| 19 | `TAXSTMT.NON.TAXABLE.INCOME` | `ChstmpTaxStatement_NonTaxableIncome` | TField |  | The field will get updated for the non- taxable FUND.DISTRIBUTION, when the CAPITAL.GAIN = 1. The non-taxable income is determined using the fiscal data payment value. |
| 20 | `TAXSTMT.FEES.AMT` | `ChstmpTaxStatement_FeesAmt` | TField |  | The field will get updated only when advisory or safekeeping fees details are updated. |
| 21 | `TAXSTMT.LOCAL.REF` | `ChstmpTaxStatement_LocalRef` |  |  |  |
| 22 | `TAXSTMT.RESERVED.5` | `ChstmpTaxStatement_Reserved5` | TField |  |  |
| 23 | `TAXSTMT.RESERVED.4` | `ChstmpTaxStatement_Reserved4` | TField |  |  |
| 24 | `TAXSTMT.RESERVED.3` | `ChstmpTaxStatement_Reserved3` | TField |  |  |
| 25 | `TAXSTMT.RESERVED.2` | `ChstmpTaxStatement_Reserved2` | TField |  |  |
| 26 | `TAXSTMT.RESERVED.1` | `ChstmpTaxStatement_Reserved1` | TField |  |  |
