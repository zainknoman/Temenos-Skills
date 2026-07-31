# POR.ERRORFLAGS — Table Schema

> Source: `INSERTS/I_F.POR.ERRORFLAGS` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPER.CompanyID` | `PorErrorflags_Companyid` |  |  |  |
| 2 | `PPPER.FTNumber` | `PorErrorflags_Ftnumber` |  |  |  |
| 3 | `PPPER.ErrorTimestamp` | `PorErrorflags_Errortimestamp` |  |  |  |
| 4 | `PPPER.ErrorCode` | `PorErrorflags_Errorcode` |  |  |  |
| 5 | `PPPER.ErrorType` | `PorErrorflags_Errortype` |  |  |  |
| 6 | `PPPER.AdditionalInformation` | `PorErrorflags_Additionalinformation` |  |  |  |
| 7 | `PPPER.ActiveFlag` | `PorErrorflags_Activeflag` |  |  |  |
| 8 | `PPPER.OriginatedBy` | `PorErrorflags_Originatedby` |  |  |  |
