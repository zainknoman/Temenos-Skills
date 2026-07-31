# AA.ACCRUAL.MISMATCH.REPORT — Table Schema

> Source: `INSERTS/I_F.AA.ACCRUAL.MISMATCH.REPORT` in `AA_Util.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AR.ACCOUNT.ID` | `AaAccrualMismatchReport_AccountId` | TField |  |  |
| 2 | `AA.AR.CUSTOMER` | `AaAccrualMismatchReport_Customer` |  |  |  |
| 3 | `AA.AR.DRAWDOWN.DATE` | `AaAccrualMismatchReport_DrawdownDate` | TField |  |  |
| 4 | `AA.AR.PRODUCT.LINE` | `AaAccrualMismatchReport_ProductLine` | TField |  |  |
| 5 | `AA.AR.RUN.DATE` | `AaAccrualMismatchReport_RunDate` |  |  |  |
| 6 | `AA.AR.PRODUCT` | `AaAccrualMismatchReport_Product` |  |  |  |
| 7 | `AA.AR.STATUS` | `AaAccrualMismatchReport_Status` |  |  |  |
| 8 | `AA.AR.PROBLEM.CATEGORY` | `AaAccrualMismatchReport_ProblemCategory` |  |  |  |
| 9 | `AA.AR.CATEGORY.SEVERITY` | `AaAccrualMismatchReport_CategorySeverity` |  |  |  |
| 10 | `AA.AR.PROBLEM.DETAILS` | `AaAccrualMismatchReport_ProblemDetails` |  |  |  |
| 11 | `AA.AR.TOTAL.PROBLEMS` | `AaAccrualMismatchReport_TotalProblems` |  |  |  |
