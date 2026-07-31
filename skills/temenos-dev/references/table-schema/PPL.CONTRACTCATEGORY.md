# PPL.CONTRACTCATEGORY — Table Schema

> Source: `INSERTS/I_F.PPL.CONTRACTCATEGORY` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCNC.ContractCategoryID` | `PplContractcategory_Contractcategoryid` |  |  |  |
| 2 | `PPCNC.ContractID` | `PplContractcategory_Contractid` |  |  |  |
| 3 | `PPCNC.SLACode` | `PplContractcategory_Slacode` |  |  |  |
| 4 | `PPCNC.Priority` | `PplContractcategory_Priority` |  |  |  |
| 5 | `PPCNC.CurrencyCode` | `PplContractcategory_Currencycode` |  |  |  |
| 6 | `PPCNC.TransactionLowerLimit` | `PplContractcategory_Transactionlowerlimit` |  |  |  |
| 7 | `PPCNC.TransactionUpperLimit` | `PplContractcategory_Transactionupperlimit` |  |  |  |
| 8 | `PPCNC.ChargeOption` | `PplContractcategory_Chargeoption` |  |  |  |
| 9 | `PPCNC.Ranking` | `PplContractcategory_Ranking` |  |  |  |
