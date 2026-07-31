# CO.DEFICIT — Table Schema

> Source: `INSERTS/I_F.CO.DEFICIT` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CODE.DEFICIT.CCY` | `CoDeficit_DeficitCcy` | TField |  | Currency in which the Deficit amount is reported (Local currency of customer company). |
| 2 | `CODE.TOTAL.DEFICIT` | `CoDeficit_TotalDeficit` | TField |  | The total amount of collateral deficit that the customer has. Deficit Amount (Total deficit amount for the customer in LCCY) When the Liabilities of a customer exceeds his collaterals, this field will hold the deficit amount. |
| 3 | `CODE.BUFFER.DEFICIT` | `CoDeficit_BufferDeficit` | TField |  | The amount of collateral deficit that the customer currently has when the collateral deficit does not exceed the buffer defined on the deficit. If the deficit amount is less than Buffer specified in OV parameter then, this field is updated |
| 4 | `CODE.TOP.UP.DEFICIT` | `CoDeficit_TopUpDeficit` | TField |  | The amount of collateral deficit that the customer currently has when the collateral deficit exceeds or is equal to the TOP-UP deficit percentage but is less that then SELL.OUT deficit percentage. If the deficit amount is greater than the Top up percentage specified in OV parameter then, this field is updated |
| 5 | `CODE.SELL.OUT.DEFICIT` | `CoDeficit_SellOutDeficit` | TField |  | The amount of collateral deficit that the customer currently has when the collateral deficit exceeds the SELL.OUT deficit percentage. If the deficit amount is greater than the Sell out percentage specified in OV parameter then, this field is updated |
| 6 | `CODE.DEFICIT.DATE` | `CoDeficit_DeficitDate` | TField |  | Date the customer�s collateral went into deficit. This is the Date on which CO.DEFICIT is updated for the first time. |
| 7 | `CODE.UPDATE.DATE` | `CoDeficit_UpdateDate` | TField |  | Date the customer�s collateral was re-calculated This is the Date on which CO.DEFICIT is rebuilt and the deficits are updated. |
| 8 | `CODE.ADVANCE.MESSAGE` | `CoDeficit_AdvanceMessage` |  |  |  |
| 9 | `CODE.TOT.DEFICIT.LAR` | `CoDeficit_TotDeficitLar` | TField |  | The total amount of collateral deficit that the customer has, before applying low advanced ratio. |
| 10 | `CODE.UPDATE.TIME` | `CoDeficit_UpdateTime` |  |  |  |
