# CL.LN.PAY.WRK — Table Schema

> Source: `INSERTS/I_F.CL.LN.PAY.WRK` in `LMSCOL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LN.WRK.FILE.AC.ID` | `ClLnPayWrk_AcId` | TField |  | Account Number. |
| 2 | `LN.WRK.FILE.AAA.ID` | `ClLnPayWrk_AaaId` | TField |  | Activity Reference. |
| 3 | `LN.WRK.FILE.TRANS.REFERENCE` | `ClLnPayWrk_TransReference` | TField |  | Transaction Reference. |
| 4 | `LN.WRK.FILE.VALUE.DATE` | `ClLnPayWrk_ValueDate` | TField |  | Value date of the Payment transaction. |
| 5 | `LN.WRK.FILE.TXN.CODE` | `ClLnPayWrk_TxnCode` | TField |  | Transaction code for the payment transaction . |
| 6 | `LN.WRK.FILE.AMOUNT.LCY` | `ClLnPayWrk_AmountLcy` | TField |  | Repayment amount. |
| 7 | `LN.WRK.FILE.PRINCIPAL` | `ClLnPayWrk_Principal` | TField |  | Principal amount repaid through the transaction. |
| 8 | `LN.WRK.FILE.INTEREST` | `ClLnPayWrk_Interest` | TField |  | Interest amount repaid through the transaction. |
| 9 | `LN.WRK.FILE.CHARGE` | `ClLnPayWrk_Charge` | TField |  | Charge amount repaid through the transaction. |
