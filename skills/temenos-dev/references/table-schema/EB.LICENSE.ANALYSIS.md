# EB.LICENSE.ANALYSIS — Table Schema

> Source: `INSERTS/I_F.EB.LICENSE.ANALYSIS` in `EB_Monitoring.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ELA.CURRENT.RELEASE` | `EbLicenseAnalysis_CurrentRelease` |  |  |  |
| 2 | `ELA.SERVER.NAME` | `EbLicenseAnalysis_ServerName` |  |  |  |
| 3 | `ELA.DATE.TIME` | `EbLicenseAnalysis_DateTime` |  |  |  |
| 4 | `ELA.NO.OF.USER` | `EbLicenseAnalysis_NoOfUser` |  |  |  |
| 5 | `ELA.PERSONAL.USER` | `EbLicenseAnalysis_PersonalUser` |  |  |  |
| 6 | `ELA.PROXY.USER` | `EbLicenseAnalysis_ProxyUser` |  |  |  |
