# AFRACP.CUS.ASSET.DETAILS — Table Schema

> Source: `INSERTS/I_F.AFRACP.CUS.ASSET.DETAILS` in `AFRACP_ProvisionCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRACP.ASSET.CUST.ASSET.CLASSIFICATION` | `AfracpAsset_CustAssetClassification` |  |  |  |
| 2 | `AFRACP.ASSET.DATE.CUST.ASSET.CLASSIFICATION` | `AfracpAsset_DateCustAssetClassification` |  |  |  |
| 3 | `AFRACP.ASSET.YEAR.START.DATE` | `AfracpAsset_YearStartDate` |  |  |  |
| 4 | `AFRACP.ASSET.YEAR.END.DATE` | `AfracpAsset_YearEndDate` |  |  |  |
