# PPL.BANKCONDCHARGEACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCONDCHARGEACCOUNT` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCC.BankCondChargeID` | `PplBankcondchargeaccount_Bankcondchargeid` |  |  |  |
| 2 | `PPBCC.BankConditionsID` | `PplBankcondchargeaccount_Bankconditionsid` |  |  |  |
| 3 | `PPBCC.TransactionCurrency` | `PplBankcondchargeaccount_Transactioncurrency` |  |  |  |
| 4 | `PPBCC.ChargeAccountCompanyID` | `PplBankcondchargeaccount_Chargeaccountcompanyid` |  |  |  |
| 5 | `PPBCC.ChargeAccountNumber` | `PplBankcondchargeaccount_Chargeaccountnumber` |  |  |  |
| 6 | `PPBCC.ChargeAccountCurrency` | `PplBankcondchargeaccount_Chargeaccountcurrency` |  |  |  |
