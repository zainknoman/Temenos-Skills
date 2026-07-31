# AA.FULFILMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.FULFILMENT.TYPE` in `AF_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.FLT.DESCRIPTION` | `AaFulfilmentType_Description` |  |  |  |
| 2 | `AA.FLT.FULFILMENT.TYPE` | `AaFulfilmentType_FulfilmentType` | TField |  |  |
| 3 | `AA.FLT.FULFILMENT.TARGET` | `AaFulfilmentType_FulfilmentTarget` | TField |  |  |
| 4 | `AA.FLT.INTERFACE.TYPE` | `AaFulfilmentType_InterfaceType` | TField |  |  |
| 5 | `AA.FLT.CLASS.NAME` | `AaFulfilmentType_ClassName` | TField |  |  |
| 6 | `AA.FLT.STATUS` | `AaFulfilmentType_Status` | TField |  |  |
| 7 | `AA.FLT.AVAILABLE.DATE` | `AaFulfilmentType_AvailableDate` | TField |  |  |
| 8 | `AA.FLT.EXPIRY.DATE` | `AaFulfilmentType_ExpiryDate` | TField |  |  |
| 9 | `AA.FLT.LAST.PUBLISHED` | `AaFulfilmentType_LastPublished` | TField |  |  |
