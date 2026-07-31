# IS.BROKER.FEE.BAL.HIST — Table Schema

> Source: `INSERTS/I_F.IS.BROKER.FEE.BAL.HIST` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.BFH.PURCHASE.REF` | `IsBrokerFeeBalHist_PurchaseRef` |  |  |  |
| 2 | `IS.BFH.BROKER.SHARE.AMOUNT` | `IsBrokerFeeBalHist_BrokerShareAmount` |  |  |  |
| 3 | `IS.BFH.TOTAL.AMOUNT` | `IsBrokerFeeBalHist_TotalAmount` | TField |  | The Total amount to be paid to the broker This field will hold the sum of all the broker share amounts for the broker |
| 4 | `IS.BFH.FT.REFERENCE` | `IsBrokerFeeBalHist_FtReference` | TField |  | The FT reference for the broker share payment made |
| 5 | `IS.BFH.BROKER` | `IsBrokerFeeBalHist_Broker` | TField |  | The Broker id under whom the purchase references were booked |
| 6 | `IS.BFH.COMPANY` | `IsBrokerFeeBalHist_Company` | TField |  | The company to which the purchase references belong to |
| 7 | `IS.BFH.PRODUCT` | `IsBrokerFeeBalHist_Product` | TField |  | The IS.PRODUCT linked to the purchase references |
| 8 | `IS.BFH.CURRENCY` | `IsBrokerFeeBalHist_Currency` | TField |  | The broker fee currency of the purchase references |
| 9 | `IS.BFH.VALUE.DATE` | `IsBrokerFeeBalHist_ValueDate` | TField |  | The value date on which the purchase refernces were moved to purchase stage |
