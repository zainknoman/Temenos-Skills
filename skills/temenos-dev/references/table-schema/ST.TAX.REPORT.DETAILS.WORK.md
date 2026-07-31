# ST.TAX.REPORT.DETAILS.WORK — Table Schema

> Source: `INSERTS/I_F.ST.TAX.REPORT.DETAILS.WORK` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.REP.CONTRACT.ID` | `StTaxReportDetailsWork_ContractId` | TField |  | Specifies the contract ID of the underlying transaction.In case of AA deposit, it would be the arrangement ID, for credit interest it would be the account number itself and for security transactions it could be the portfolio number. Application to pass this ID |
| 2 | `TAX.REP.TRANS.COMPANY` | `StTaxReportDetailsWork_TransCompany` | TField |  | Specifies the company ID of the transaction.If not given, this would be default to the current company id |
| 3 | `TAX.REP.RESERVED01` | `StTaxReportDetailsWork_Reserved01` | TField |  | Reserved for future use |
| 4 | `TAX.REP.RESERVED02` | `StTaxReportDetailsWork_Reserved02` | TField |  | Reserved for future use |
| 5 | `TAX.REP.RESERVED03` | `StTaxReportDetailsWork_Reserved03` | TField |  | Reserved for future use |
| 6 | `TAX.REP.CUST.INCOME.TYPE` | `StTaxReportDetailsWork_CustIncomeType` |  |  |  |
| 7 | `TAX.REP.TRANS.DATE` | `StTaxReportDetailsWork_TransDate` |  |  |  |
| 8 | `TAX.REP.PORTFOLIO.ID` | `StTaxReportDetailsWork_PortfolioId` |  |  |  |
| 9 | `TAX.REP.TOTAL.INCOME` | `StTaxReportDetailsWork_TotalIncome` |  |  |  |
| 10 | `TAX.REP.CUST.REL.ID` | `StTaxReportDetailsWork_CustRelId` |  |  |  |
| 11 | `TAX.REP.INCOME.TYPE.DESC` | `StTaxReportDetailsWork_IncomeTypeDesc` |  |  |  |
| 12 | `TAX.REP.RESERVED05` | `StTaxReportDetailsWork_Reserved05` |  |  |  |
| 13 | `TAX.REP.RESERVED06` | `StTaxReportDetailsWork_Reserved06` |  |  |  |
| 14 | `TAX.REP.JOINT.CUST.TAXID` | `StTaxReportDetailsWork_JointCustTaxid` |  |  |  |
| 15 | `TAX.REP.OWNING.PERC` | `StTaxReportDetailsWork_OwningPerc` |  |  |  |
| 16 | `TAX.REP.OWNING.AMT` | `StTaxReportDetailsWork_OwningAmt` |  |  |  |
| 17 | `TAX.REP.TAX.TYPE` | `StTaxReportDetailsWork_TaxType` |  |  |  |
| 18 | `TAX.REP.TAX.RATE` | `StTaxReportDetailsWork_TaxRate` |  |  |  |
| 19 | `TAX.REP.TAX.AMT.SPLIT` | `StTaxReportDetailsWork_TaxAmtSplit` |  |  |  |
| 20 | `TAX.REP.TAX.DATE` | `StTaxReportDetailsWork_TaxDate` |  |  |  |
| 21 | `TAX.REP.TAX.ACCOUNT` | `StTaxReportDetailsWork_TaxAccount` |  |  |  |
| 22 | `TAX.REP.TR.CODE.CR` | `StTaxReportDetailsWork_TrCodeCr` |  |  |  |
| 23 | `TAX.REP.TR.CODE.DR` | `StTaxReportDetailsWork_TrCodeDr` |  |  |  |
| 24 | `TAX.REP.RESERVED07` | `StTaxReportDetailsWork_Reserved07` |  |  |  |
| 25 | `TAX.REP.RESERVED08` | `StTaxReportDetailsWork_Reserved08` |  |  |  |
| 26 | `TAX.REP.RESERVED09` | `StTaxReportDetailsWork_Reserved09` |  |  |  |
| 27 | `TAX.REP.RESERVED10` | `StTaxReportDetailsWork_Reserved10` | TField |  | Reserved for future use |
