# USLEND.ESCROW.DISB.DETS — Table Schema

> Source: `INSERTS/I_F.USLEND.ESCROW.DISB.DETS` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.ESC.DD.DISB.DATE` | `UslendEscrowDisbDets_DisbDate` |  |  |  |
| 2 | `US.ESC.DD.LOAN.NO` | `UslendEscrowDisbDets_LoanNo` |  |  |  |
| 3 | `US.ESC.DD.INITIATION.TYPE` | `UslendEscrowDisbDets_InitiationType` |  |  |  |
| 4 | `US.ESC.DD.CUSTOMER.NO` | `UslendEscrowDisbDets_CustomerNo` |  |  |  |
| 5 | `US.ESC.DD.CUSTOMER.NAME` | `UslendEscrowDisbDets_CustomerName` |  |  |  |
| 6 | `US.ESC.DD.ESCROW.PAYEE` | `UslendEscrowDisbDets_EscrowPayee` |  |  |  |
| 7 | `US.ESC.DD.ESCROW.PAYEE.ACCOUNT` | `UslendEscrowDisbDets_EscrowPayeeAccount` |  |  |  |
| 8 | `US.ESC.DD.DISB.AMT` | `UslendEscrowDisbDets_DisbAmt` |  |  |  |
| 9 | `US.ESC.DD.ESCROW.BAL` | `UslendEscrowDisbDets_EscrowBal` |  |  |  |
| 10 | `US.ESC.DD.REASON` | `UslendEscrowDisbDets_Reason` |  |  |  |
| 11 | `US.ESC.DD.AAA.ID` | `UslendEscrowDisbDets_AaaId` |  |  |  |
