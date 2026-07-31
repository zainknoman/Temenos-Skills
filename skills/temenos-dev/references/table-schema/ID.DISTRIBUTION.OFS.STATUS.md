# ID.DISTRIBUTION.OFS.STATUS — Table Schema

> Source: `INSERTS/I_F.ID.DISTRIBUTION.OFS.STATUS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.DOS.PDS.ACTION.REF` | `IdDistributionOfsStatus_PdsActionRef` | TField |  |  |
| 2 | `ID.DOS.ARRANGEMENT.REF` | `IdDistributionOfsStatus_ArrangementRef` | TField |  |  |
| 3 | `ID.DOS.OVERALL.STATUS` | `IdDistributionOfsStatus_OverallStatus` | TField |  |  |
| 4 | `ID.DOS.ACTIVITY` | `IdDistributionOfsStatus_Activity` |  |  |  |
| 5 | `ID.DOS.STATUS` | `IdDistributionOfsStatus_Status` |  |  |  |
| 6 | `ID.DOS.OFS.RESPONSE` | `IdDistributionOfsStatus_OfsResponse` |  |  |  |
