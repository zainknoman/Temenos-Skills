# POR.BATCHINFO — Table Schema

> Source: `INSERTS/I_F.POR.BATCHINFO` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPBA.CompanyID` | `PorBatchinfo_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 |
| 2 | `PPPBA.ParentFTNumber` | `PorBatchinfo_Parentftnumber` | TField |  | Unique ID that is used to identify the parent transactions |
| 3 | `PPPBA.ChildFTNumber` | `PorBatchinfo_Childftnumber` | TField |  | Unique ID that is used to identify the child transactions |
| 4 | `PPPBA.FeeType` | `PorBatchinfo_Feetype` | TField |  | Indicates the Fee type applied for the respective child payment. |
| 5 | `PPPBA.FeeAmount` | `PorBatchinfo_Feeamount` | TField |  | Indicates the Fee amount calculated for the child payment |
| 6 | `PPPBA.FeeCurrency` | `PorBatchinfo_Feecurrency` | TField |  | Indicates the currency based on which the fee is calculated for the child payment |
| 7 | `PPPBA.BatchReference` | `PorBatchinfo_Batchreference` | TField |  | Holds the reference id which relates the parent and child payment |
