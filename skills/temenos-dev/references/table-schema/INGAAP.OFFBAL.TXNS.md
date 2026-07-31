# INGAAP.OFFBAL.TXNS — Table Schema

> Source: `INSERTS/I_F.INGAAP.OFFBAL.TXNS` in `INGAAP_Offbalance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INOFF.BAL.APPLICATION` | `IngaapOffbalTxns_Application` | TField |  |  |
| 2 | `INOFF.BAL.YR.MONTH` | `IngaapOffbalTxns_YrMonth` | TField |  |  |
| 3 | `INOFF.BAL.CONTRACT.ID` | `IngaapOffbalTxns_ContractId` | TField |  |  |
| 4 | `INOFF.BAL.CURRENCY` | `IngaapOffbalTxns_Currency` | TField |  |  |
| 5 | `INOFF.BAL.TXN.TYPE` | `IngaapOffbalTxns_TxnType` | TField |  |  |
| 6 | `INOFF.BAL.CONTRACT.TYPE` | `IngaapOffbalTxns_ContractType` | TField |  |  |
| 7 | `INOFF.BAL.NOMINAL.AMT` | `IngaapOffbalTxns_NominalAmt` | TField |  |  |
| 8 | `INOFF.BAL.PL.AMT` | `IngaapOffbalTxns_PlAmt` | TField |  |  |
| 9 | `INOFF.BAL.PORTFOLIO.NO` | `IngaapOffbalTxns_PortfolioNo` | TField |  |  |
| 10 | `INOFF.BAL.DEAL.TYPE` | `IngaapOffbalTxns_DealType` | TField |  |  |
| 11 | `INOFF.BAL.MATURITY.DATE` | `IngaapOffbalTxns_MaturityDate` | TField |  |  |
