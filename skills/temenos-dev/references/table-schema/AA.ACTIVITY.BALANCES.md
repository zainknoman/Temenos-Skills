# AA.ACTIVITY.BALANCES — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.BALANCES` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACT.BAL.CURRENCY` | `AaActivityBalances_Currency` | TField |  | This field stores the Currency of the Arrangement contract |
| 2 | `AA.ACT.BAL.ACTIVITY.REF` | `AaActivityBalances_ActivityRef` |  |  |  |
| 3 | `AA.ACT.BAL.ACTIVITY` | `AaActivityBalances_Activity` |  |  |  |
| 4 | `AA.ACT.BAL.ACTIVITY.DATE` | `AaActivityBalances_ActivityDate` |  |  |  |
| 5 | `AA.ACT.BAL.PROPERTY` | `AaActivityBalances_Property` |  |  |  |
| 6 | `AA.ACT.BAL.PROPERTY.AMT` | `AaActivityBalances_PropertyAmt` |  |  |  |
| 7 | `AA.ACT.BAL.BILL.REF` | `AaActivityBalances_BillRef` |  |  |  |
| 8 | `AA.ACT.BAL.LAST.UPDATE.DATE` | `AaActivityBalances_LastUpdateDate` | TField |  | Stores the date time stamp as to when this file was last updated |
| 9 | `AA.ACT.BAL.DELIN.REPAY.REF` | `AaActivityBalances_DelinRepayRef` |  |  |  |
| 10 | `AA.ACT.BAL.DELIN.REPAY.AMT` | `AaActivityBalances_DelinRepayAmt` |  |  |  |
| 11 | `AA.ACT.BAL.DELIN.TOT.AMT` | `AaActivityBalances_DelinTotAmt` | TField |  | This field is updated with the total delinquency amount across all bills |
| 12 | `AA.ACT.BAL.MASTER.REF` | `AaActivityBalances_MasterRef` |  |  |  |
