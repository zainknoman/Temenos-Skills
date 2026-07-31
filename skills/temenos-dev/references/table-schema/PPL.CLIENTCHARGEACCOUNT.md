# PPL.CLIENTCHARGEACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCHARGEACCOUNT` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCA.ClientChargeAccountID` | `PplClientchargeaccount_Clientchargeaccountid` |  |  |  |
| 2 | `PPCCA.ClientConditionsID` | `PplClientchargeaccount_Clientconditionsid` |  |  |  |
| 3 | `PPCCA.TransactionCurrency` | `PplClientchargeaccount_Transactioncurrency` |  |  |  |
| 4 | `PPCCA.DebitCreditIndicator` | `PplClientchargeaccount_Debitcreditindicator` |  |  |  |
| 5 | `PPCCA.ChargeAccountCompanyID` | `PplClientchargeaccount_Chargeaccountcompanyid` |  |  |  |
| 6 | `PPCCA.ChargeAccountNumber` | `PplClientchargeaccount_Chargeaccountnumber` |  |  |  |
| 7 | `PPCCA.ChargeAccountCurrency` | `PplClientchargeaccount_Chargeaccountcurrency` |  |  |  |
