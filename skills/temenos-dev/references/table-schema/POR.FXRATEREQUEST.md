# POR.FXRATEREQUEST — Table Schema

> Source: `INSERTS/I_F.POR.FXRATEREQUEST` in `PP_FXService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POFXR.CompanyID` | `PorFxraterequest_Companyid` |  |  |  |
| 2 | `POFXR.FTNumber` | `PorFxraterequest_Ftnumber` |  |  |  |
| 3 | `POFXR.ProcessingDate` | `PorFxraterequest_Processingdate` |  |  |  |
| 4 | `POFXR.Status` | `PorFxraterequest_Status` |  |  |  |
| 5 | `POFXR.StatusDateTime` | `PorFxraterequest_Statusdatetime` |  |  |  |
| 6 | `POFXR.DebitCreditIndicator` | `PorFxraterequest_Debitcreditindicator` |  |  |  |
| 7 | `POFXR.LimOrderReference` | `PorFxraterequest_Limorderreference` |  |  |  |
