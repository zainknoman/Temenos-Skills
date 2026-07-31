# PPT.CLIENTCONDITIONPRODUCT — Table Schema

> Source: `INSERTS/I_F.PPT.CLIENTCONDITIONPRODUCT` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCP.CompanyID` | `PptClientconditionproduct_Companyid` |  |  |  |
| 2 | `PPCCP.ClientConditionProduct` | `PptClientconditionproduct_Clientconditionproduct` |  |  |  |
| 3 | `PPCCP.Description` | `PptClientconditionproduct_Description` |  |  |  |
| 4 | `PPCCP.RACClientConditionProduct` | `PptClientconditionproduct_Racclientconditionproduct` |  |  |  |
| 5 | `PPCCP.RSCClientConditionProduct` | `PptClientconditionproduct_Rscclientconditionproduct` |  |  |  |
| 6 | `PPCCP.EntryUserID` | `PptClientconditionproduct_Entryuserid` |  |  |  |
| 7 | `PPCCP.EntryDateTime` | `PptClientconditionproduct_Entrydatetime` |  |  |  |
| 8 | `PPCCP.ApproverUserID` | `PptClientconditionproduct_Approveruserid` |  |  |  |
| 9 | `PPCCP.ApprovedDateTime` | `PptClientconditionproduct_Approveddatetime` |  |  |  |
