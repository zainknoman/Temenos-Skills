# AA.INTEGRITY.REPORT — Table Schema

> Source: `INSERTS/I_F.AA.INTEGRITY.REPORT` in `AA_Util.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.IR.ACCOUNT.ID` | `AaIntegrityReport_AccountId` | TField |  |  |
| 2 | `AA.IR.CUSTOMER` | `AaIntegrityReport_Customer` |  |  |  |
| 3 | `AA.IR.DRAWDOWN.DATE` | `AaIntegrityReport_DrawdownDate` | TField |  |  |
| 4 | `AA.IR.PRODUCT.LINE` | `AaIntegrityReport_ProductLine` | TField |  |  |
| 5 | `AA.IR.RUN.DATE` | `AaIntegrityReport_RunDate` |  |  |  |
| 6 | `AA.IR.PRODUCT` | `AaIntegrityReport_Product` |  |  |  |
| 7 | `AA.IR.STATUS` | `AaIntegrityReport_Status` |  |  |  |
| 8 | `AA.IR.PROBLEM.CATEGORY` | `AaIntegrityReport_ProblemCategory` |  |  |  |
| 9 | `AA.IR.CATEGORY.SEVERITY` | `AaIntegrityReport_CategorySeverity` |  |  |  |
| 10 | `AA.IR.PROBLEM.DETAILS` | `AaIntegrityReport_ProblemDetails` |  |  |  |
| 11 | `AA.IR.TOTAL.PROBLEMS` | `AaIntegrityReport_TotalProblems` |  |  |  |
| 12 | `AA.IR.ACTIVITY.COUNT` | `AaIntegrityReport_ActivityCount` |  |  |  |
| 13 | `AA.IR.BRANCH.CODE` | `AaIntegrityReport_BranchCode` | TField |  |  |
