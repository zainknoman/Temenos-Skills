# IS.BROKER.FEE.BALANCES — Table Schema

> Source: `INSERTS/I_F.IS.BROKER.FEE.BALANCES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.BFB.PURCHASE.REF` | `IsBrokerFeeBalances_PurchaseRef` |  |  |  |
| 2 | `IS.BFB.BROKER.SHARE.AMOUNT` | `IsBrokerFeeBalances_BrokerShareAmount` |  |  |  |
| 3 | `IS.BFB.TOTAL.AMOUNT` | `IsBrokerFeeBalances_TotalAmount` | TField |  | The Total amount to be paid to the broker This field will hold the sum of all the broker share amounts for the broker |
| 4 | `IS.BFB.FT.REFERENCE` | `IsBrokerFeeBalances_FtReference` | TField |  | The FT reference for the broker share payment made. Will be updated upon completion of the payment via the COB job based on the frequency mentioned BROKER.PAYMENt.FREQ mentioned in the broker record |
| 5 | `IS.BFB.BROKER` | `IsBrokerFeeBalances_Broker` | TField |  | The Broker id under whom the purchase references were booked |
| 6 | `IS.BFB.COMPANY` | `IsBrokerFeeBalances_Company` | TField |  | The company to which the purchase references belong to |
| 7 | `IS.BFB.PRODUCT` | `IsBrokerFeeBalances_Product` | TField |  | The IS.PRODUCT linked to the purchase references |
| 8 | `IS.BFB.CURRENCY` | `IsBrokerFeeBalances_Currency` | TField |  | The broker fee currency of the purchase references |
| 9 | `IS.BFB.VALUE.DATE` | `IsBrokerFeeBalances_ValueDate` | TField |  | The value date on which the purchase refernces were moved to purchase stage |
