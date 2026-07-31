# ST.TAX.REPORT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ST.TAX.REPORT.DETAILS` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.REP.CONTRACT.ID` | `StTaxReportDetails_ContractId` | TField |  | Specifies the contract ID of the underlying transaction In case of AA deposit, it would be the arrangement ID, for credit interest it would be the account number itself and for security transactions it could be the portfolio number. Application to pass this ID |
| 2 | `TAX.REP.TRANS.COMPANY` | `StTaxReportDetails_TransCompany` | TField |  | Specifies the company ID of the transaction If not given, this would be default to the current company id |
| 3 | `TAX.REP.RESERVED01` | `StTaxReportDetails_Reserved01` | TField |  | Reserved for future use |
| 4 | `TAX.REP.RESERVED02` | `StTaxReportDetails_Reserved02` | TField |  | Reserved for future use |
| 5 | `TAX.REP.RESERVED03` | `StTaxReportDetails_Reserved03` | TField |  | Reserved for future use |
| 6 | `TAX.REP.CUST.INCOME.TYPE` | `StTaxReportDetails_CustIncomeType` |  |  |  |
| 7 | `TAX.REP.TRANS.DATE` | `StTaxReportDetails_TransDate` |  |  |  |
| 8 | `TAX.REP.PORTFOLIO.ID` | `StTaxReportDetails_PortfolioId` |  |  |  |
| 9 | `TAX.REP.TOTAL.INCOME` | `StTaxReportDetails_TotalIncome` |  |  |  |
| 10 | `TAX.REP.CUST.REL.ID` | `StTaxReportDetails_CustRelId` |  |  |  |
| 11 | `TAX.REP.INCOME.TYPE.DESC` | `StTaxReportDetails_IncomeTypeDesc` |  |  |  |
| 12 | `TAX.REP.RESERVED05` | `StTaxReportDetails_Reserved05` |  |  |  |
| 13 | `TAX.REP.RESERVED06` | `StTaxReportDetails_Reserved06` |  |  |  |
| 14 | `TAX.REP.JOINT.CUST.TAXID` | `StTaxReportDetails_JointCustTaxid` |  |  |  |
| 15 | `TAX.REP.OWNING.PERC` | `StTaxReportDetails_OwningPerc` |  |  |  |
| 16 | `TAX.REP.OWNING.AMT` | `StTaxReportDetails_OwningAmt` |  |  |  |
| 17 | `TAX.REP.TAX.TYPE` | `StTaxReportDetails_TaxType` |  |  |  |
| 18 | `TAX.REP.TAX.RATE` | `StTaxReportDetails_TaxRate` |  |  |  |
| 19 | `TAX.REP.TAX.AMT.SPLIT` | `StTaxReportDetails_TaxAmtSplit` |  |  |  |
| 20 | `TAX.REP.TAX.DATE` | `StTaxReportDetails_TaxDate` |  |  |  |
| 21 | `TAX.REP.TAX.ACCOUNT` | `StTaxReportDetails_TaxAccount` |  |  |  |
| 22 | `TAX.REP.TR.CODE.CR` | `StTaxReportDetails_TrCodeCr` |  |  |  |
| 23 | `TAX.REP.TR.CODE.DR` | `StTaxReportDetails_TrCodeDr` |  |  |  |
| 24 | `TAX.REP.RESERVED07` | `StTaxReportDetails_Reserved07` |  |  |  |
| 25 | `TAX.REP.RESERVED08` | `StTaxReportDetails_Reserved08` |  |  |  |
| 26 | `TAX.REP.RESERVED09` | `StTaxReportDetails_Reserved09` |  |  |  |
| 27 | `TAX.REP.RESERVED10` | `StTaxReportDetails_Reserved10` | TField |  | Reserved for future use |
