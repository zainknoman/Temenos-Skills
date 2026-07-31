# NORACC.ACSTMT.PRENOTICE.DATA — Table Schema

> Source: `INSERTS/I_F.NORACC.ACSTMT.PRENOTICE.DATA` in `NORACC_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORACC.START.DATE` | `NoraccAcstmtPrenoticeData_StartDate` |  |  |  |
| 2 | `NORACC.END.DATE` | `NoraccAcstmtPrenoticeData_EndDate` |  |  |  |
| 3 | `NORACC.DR.INT.AMT` | `NoraccAcstmtPrenoticeData_DrIntAmt` |  |  |  |
| 4 | `NORACC.CURRENCY` | `NoraccAcstmtPrenoticeData_Currency` |  |  |  |
| 5 | `NORACC.INT.DEF.DT` | `NoraccAcstmtPrenoticeData_IntDefDt` |  |  |  |
| 6 | `NORACC.INT.ST.DT` | `NoraccAcstmtPrenoticeData_IntStDt` |  |  |  |
| 7 | `NORACC.INT.END.DT` | `NoraccAcstmtPrenoticeData_IntEndDt` |  |  |  |
| 8 | `NORACC.INT.RATE` | `NoraccAcstmtPrenoticeData_IntRate` |  |  |  |
| 9 | `NORACC.DRSTATICTEXT` | `NoraccAcstmtPrenoticeData_Drstatictext` |  |  |  |
| 10 | `NORACC.PAYMENT.STO.DATE` | `NoraccAcstmtPrenoticeData_PaymentStoDate` |  |  |  |
| 11 | `NORACC.PAYMENT.STO.BANK.CUS.INDICATOR` | `NoraccAcstmtPrenoticeData_PaymentStoBankCusIndicator` |  |  |  |
| 12 | `NORACC.PAYMENT.STO.BENEFICIARY` | `NoraccAcstmtPrenoticeData_PaymentStoBeneficiary` |  |  |  |
| 13 | `NORACC.PAYMENT.STO.CURRENCY` | `NoraccAcstmtPrenoticeData_PaymentStoCurrency` |  |  |  |
| 14 | `NORACC.PAYMENT.STO.AMOUNT` | `NoraccAcstmtPrenoticeData_PaymentStoAmount` |  |  |  |
| 15 | `NORACC.ADVICE.INDICATOR` | `NoraccAcstmtPrenoticeData_AdviceIndicator` |  |  |  |
| 16 | `NORACC.FEE.INTEREST.AMOUNT` | `NoraccAcstmtPrenoticeData_FeeInterestAmount` |  |  |  |
| 17 | `NORACC.PROPERTY.NAME` | `NoraccAcstmtPrenoticeData_PropertyName` |  |  |  |
| 18 | `NORACC.PAYMENT.STO.TEXT` | `NoraccAcstmtPrenoticeData_PaymentStoText` |  |  |  |
