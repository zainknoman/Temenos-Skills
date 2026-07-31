# PPT.FEEPRODUCT — Table Schema

> Source: `INSERTS/I_F.PPT.FEEPRODUCT` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPFEP.CompanyID` | `PptFeeproduct_Companyid` |  |  |  |
| 2 | `PPFEP.FeeProduct` | `PptFeeproduct_Feeproduct` |  |  |  |
| 3 | `PPFEP.Description` | `PptFeeproduct_Description` |  |  |  |
| 4 | `PPFEP.RACFeeProduct` | `PptFeeproduct_Racfeeproduct` |  |  |  |
| 5 | `PPFEP.RSCFeeProduct` | `PptFeeproduct_Rscfeeproduct` |  |  |  |
| 6 | `PPFEP.EntryUserID` | `PptFeeproduct_Entryuserid` |  |  |  |
| 7 | `PPFEP.EntryDateTime` | `PptFeeproduct_Entrydatetime` |  |  |  |
| 8 | `PPFEP.ApproverUserID` | `PptFeeproduct_Approveruserid` |  |  |  |
| 9 | `PPFEP.ApprovedDateTime` | `PptFeeproduct_Approveddatetime` |  |  |  |
