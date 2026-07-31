# CNTELL.CUSTOMER.SETTLEMENT.DTLS — Table Schema

> Source: `INSERTS/I_F.CNTELL.CUSTOMER.SETTLEMENT.DTLS` in `CNTELL_Settlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUST.SETTL.CURRENCY` | `CntellCustomerSettlementDtls_Currency` |  |  |  |
| 2 | `CUST.SETTL.DEPOSIT.AMOUNT` | `CntellCustomerSettlementDtls_DepositAmount` |  |  |  |
| 3 | `CUST.SETTL.DEPOSIT.AMOUNT.LCY` | `CntellCustomerSettlementDtls_DepositAmountLcy` |  |  |  |
| 4 | `CUST.SETTL.WITHDRAW.AMOUNT` | `CntellCustomerSettlementDtls_WithdrawAmount` |  |  |  |
| 5 | `CUST.SETTL.WITHDRAW.AMOUNT.LCY` | `CntellCustomerSettlementDtls_WithdrawAmountLcy` |  |  |  |
| 6 | `CUST.SETTL.TRANSACTION.REFERENCE` | `CntellCustomerSettlementDtls_TransactionReference` |  |  |  |
