# SL.INT.PAY.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.SL.INT.PAY.EXCEPTION` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.INT.PAY.EXCEPTION.LOAN.NUMBER` | `SlIntPayException_LoanNumber` | TField |  | Field to store the credit account number towards which the repayment is done.Valid record of ACCOUNT application |
| 2 | `SL.INT.PAY.EXCEPTION.BILL.AMT.PRINCIPAL` | `SlIntPayException_BillAmtPrincipal` | TField |  | Field to store the Principal due amount of the latest bill for the current date. |
| 3 | `SL.INT.PAY.EXCEPTION.BILL.AMT.INTEREST` | `SlIntPayException_BillAmtInterest` | TField |  | Field to store the Interest due amount of the latest bill for the current date. |
| 4 | `SL.INT.PAY.EXCEPTION.PRI.AMT.RECD` | `SlIntPayException_PriAmtRecd` | TField |  | Field to store the principal amount which is received out of the total amount received.Validation: Amount in CREDIT.AMOUNT - (Minus) amount in INTEREST.AMT (Applicable only when there is value in INTEREST.AMT field in FT) |
| 5 | `SL.INT.PAY.EXCEPTION.INT.AMT.RECD` | `SlIntPayException_IntAmtRecd` | TField |  | Field to store the Interest amount which is received out of the total amount received.Mapped from the local field INTEREST.AMT from FT. |
| 6 | `SL.INT.PAY.EXCEPTION.BILL.DATE` | `SlIntPayException_BillDate` | TField |  | Field to store the latest bill date of the Current date. |
| 7 | `SL.INT.PAY.EXCEPTION.PAY.DATE` | `SlIntPayException_PayDate` | TField |  | Field to store the date of payment towards loan. |
| 8 | `SL.INT.PAY.EXCEPTION.RESERVED.1` | `SlIntPayException_Reserved1` | TField |  |  |
| 9 | `SL.INT.PAY.EXCEPTION.RESERVED.2` | `SlIntPayException_Reserved2` | TField |  |  |
| 10 | `SL.INT.PAY.EXCEPTION.RESERVED.3` | `SlIntPayException_Reserved3` | TField |  |  |
| 11 | `SL.INT.PAY.EXCEPTION.RESERVED.4` | `SlIntPayException_Reserved4` | TField |  |  |
| 12 | `SL.INT.PAY.EXCEPTION.RESERVED.5` | `SlIntPayException_Reserved5` | TField |  |  |
