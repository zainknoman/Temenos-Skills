# ST.TAX.CALC.DETAILS — Table Schema

> Source: `INSERTS/I_F.ST.TAX.CALC.DETAILS` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCD.CONTRACT.REF` | `StTaxCalcDetails_ContractRef` | TField |  | Specifies the Contract Reference. |
| 2 | `TCD.TRANS.COMP` | `StTaxCalcDetails_TransComp` | TField |  |  |
| 3 | `TCD.TAX.CUST.ID` | `StTaxCalcDetails_TaxCustId` |  |  |  |
| 4 | `TCD.TAX.TYPE` | `StTaxCalcDetails_TaxType` |  |  |  |
| 5 | `TCD.TAX.PERIOD.START` | `StTaxCalcDetails_TaxPeriodStart` |  |  |  |
| 6 | `TCD.TAX.PERIOD.END` | `StTaxCalcDetails_TaxPeriodEnd` |  |  |  |
| 7 | `TCD.PERIOD.INCOME` | `StTaxCalcDetails_PeriodIncome` |  |  |  |
| 8 | `TCD.TAX.RATE` | `StTaxCalcDetails_TaxRate` |  |  |  |
| 9 | `TCD.TAX.AMOUNT` | `StTaxCalcDetails_TaxAmount` |  |  |  |
| 10 | `TCD.TAX.ACCOUNT` | `StTaxCalcDetails_TaxAccount` |  |  |  |
| 11 | `TCD.TR.CODE.CR` | `StTaxCalcDetails_TrCodeCr` |  |  |  |
| 12 | `TCD.TR.CODE.DR` | `StTaxCalcDetails_TrCodeDr` |  |  |  |
| 13 | `TCD.RESERVED10` | `StTaxCalcDetails_Reserved10` | TField |  | Reserved for future use |
| 14 | `TCD.RESERVED09` | `StTaxCalcDetails_Reserved09` | TField |  | Reserved for future use |
| 15 | `TCD.RESERVED08` | `StTaxCalcDetails_Reserved08` | TField |  | Reserved for future use |
| 16 | `TCD.RESERVED07` | `StTaxCalcDetails_Reserved07` | TField |  | Reserved for future use |
| 17 | `TCD.RESERVED06` | `StTaxCalcDetails_Reserved06` | TField |  | Reserved for future use |
| 18 | `TCD.RESERVED05` | `StTaxCalcDetails_Reserved05` | TField |  | Reserved for future use |
| 19 | `TCD.RESERVED04` | `StTaxCalcDetails_Reserved04` | TField |  | Reserved for future use |
| 20 | `TCD.RESERVED03` | `StTaxCalcDetails_Reserved03` | TField |  | Reserved for future use |
| 21 | `TCD.RESERVED02` | `StTaxCalcDetails_Reserved02` | TField |  | Reserved for future use |
| 22 | `TCD.RESERVED01` | `StTaxCalcDetails_Reserved01` | TField |  | Reserved for future use |
