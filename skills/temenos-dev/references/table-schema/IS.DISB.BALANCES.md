# IS.DISB.BALANCES — Table Schema

> Source: `INSERTS/I_F.IS.DISB.BALANCES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.DSB.DISBURSE.REF` | `IsDisbBalances_DisburseRef` |  |  |  |
| 2 | `IS.DSB.DISBURSE.AMT` | `IsDisbBalances_DisburseAmt` |  |  |  |
| 3 | `IS.DSB.DISBURSE.STATUS` | `IsDisbBalances_DisburseStatus` |  |  |  |
| 4 | `IS.DSB.COMMIT.DECR.REF` | `IsDisbBalances_CommitDecrRef` |  |  |  |
| 5 | `IS.DSB.COMMIT.DECR.AMT` | `IsDisbBalances_CommitDecrAmt` |  |  |  |
| 6 | `IS.DSB.CUST.CONTRB.REF` | `IsDisbBalances_CustContrbRef` |  |  |  |
| 7 | `IS.DSB.CUST.CONTRIB.AMT` | `IsDisbBalances_CustContribAmt` |  |  |  |
| 8 | `IS.DSB.IS.DISBURSE.REF` | `IsDisbBalances_IsDisburseRef` |  |  |  |
| 9 | `IS.DSB.IS.DISBURSE.STATUS` | `IsDisbBalances_IsDisburseStatus` |  |  |  |
| 10 | `IS.DSB.BILL.DATE` | `IsDisbBalances_BillDate` |  |  |  |
| 11 | `IS.DSB.BILL.AMOUNT` | `IsDisbBalances_BillAmount` |  |  |  |
| 12 | `IS.DSB.DISB.PAY.REF` | `IsDisbBalances_DisbPayRef` |  |  |  |
| 13 | `IS.DSB.RESERVED.5` | `IsDisbBalances_Reserved5` |  |  |  |
| 14 | `IS.DSB.RESERVED.4` | `IsDisbBalances_Reserved4` |  |  |  |
| 15 | `IS.DSB.RESERVED.3` | `IsDisbBalances_Reserved3` |  |  |  |
| 16 | `IS.DSB.RESERVED.2` | `IsDisbBalances_Reserved2` |  |  |  |
| 17 | `IS.DSB.RESERVED.1` | `IsDisbBalances_Reserved1` |  |  |  |
| 18 | `IS.DSB.TOT.DISBURSE.AMT` | `IsDisbBalances_TotDisburseAmt` | TField |  | The Total Amount disbursed from the AA finance contract. |
| 19 | `IS.DSB.TOT.BILL.AMOUNT` | `IsDisbBalances_TotBillAmount` | TField |  | The Total Bill Amount which is the sum of all the bill amount of IS.DISBURSEMENT performed for an asset/commodity. |
