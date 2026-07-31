# TNCUIN.GARNISH.SURVEILLANCE — Table Schema

> Source: `INSERTS/I_F.TNCUIN.GARNISH.SURVEILLANCE` in `TNCUIN_Garnishment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.GARNISH.SURVEILLANCE.CHEQUE.COLLECTION` | `TncuinGarnishSurveillance_ChequeCollection` |  |  |  |
| 2 | `TNCUIN.GARNISH.SURVEILLANCE.CHEQUE.NUMBER` | `TncuinGarnishSurveillance_ChequeNumber` |  |  |  |
| 3 | `TNCUIN.GARNISH.SURVEILLANCE.CREDIT.ACCOUNT.NUMBER` | `TncuinGarnishSurveillance_CreditAccountNumber` |  |  |  |
| 4 | `TNCUIN.GARNISH.SURVEILLANCE.CHEQUE.AMOUNT` | `TncuinGarnishSurveillance_ChequeAmount` |  |  |  |
| 5 | `TNCUIN.GARNISH.SURVEILLANCE.BILL.REGISTER.ID` | `TncuinGarnishSurveillance_BillRegisterId` |  |  |  |
| 6 | `TNCUIN.GARNISH.SURVEILLANCE.ACCOUNT.NUMBER` | `TncuinGarnishSurveillance_AccountNumber` |  |  |  |
| 7 | `TNCUIN.GARNISH.SURVEILLANCE.BILL.NUMBER` | `TncuinGarnishSurveillance_BillNumber` |  |  |  |
| 8 | `TNCUIN.GARNISH.SURVEILLANCE.BILL.AMOUNT` | `TncuinGarnishSurveillance_BillAmount` |  |  |  |
