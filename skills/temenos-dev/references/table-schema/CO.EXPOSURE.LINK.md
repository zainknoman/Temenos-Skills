# CO.EXPOSURE.LINK — Table Schema

> Source: `INSERTS/I_F.CO.EXPOSURE.LINK` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.EXP.PARENT.POOL.ID` | `CoExposuresLink_ParentPoolId` |  |  |  |
| 2 | `CO.EXP.CHILD.EXPOSURE.ID` | `CoExposuresLink_ChildExposureId` |  |  |  |
| 3 | `CO.EXP.CHILD.POOL.ID` | `CoExposuresLink_ChildPoolId` |  |  |  |
| 4 | `CO.EXP.CHILD.POOL.EXC.ID` | `CoExposuresLink_ChildPoolExcId` |  |  |  |
| 6 | `CO.EXP.PARENT.EXPOSURE.ID` | `CoExposuresLink_ParentExposureId` |  |  |  |
