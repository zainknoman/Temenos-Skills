# POR.INFORMATION — Table Schema

> Source: `INSERTS/I_F.POR.INFORMATION` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPI.CompanyID` | `PorInformation_Companyid` |  |  |  |
| 2 | `PPPI.FTNumber` | `PorInformation_Ftnumber` |  |  |  |
| 3 | `PPPI.InformationCode` | `PorInformation_Informationcode` |  |  |  |
| 4 | `PPPI.InformationTypeLineSequence` | `PorInformation_Informationtypelinesequence` |  |  |  |
| 5 | `PPPI.InformationTag` | `PorInformation_Informationtag` |  |  |  |
| 6 | `PPPI.InstructionCode` | `PorInformation_Instructioncode` |  |  |  |
| 7 | `PPPI.CountryCode` | `PorInformation_Countrycode` |  |  |  |
| 8 | `PPPI.InformationLine` | `PorInformation_Informationline` |  |  |  |
| 9 | `PPPI.OutboundCwApplicableFlag` | `PorInformation_Outboundcwapplicableflag` |  |  |  |
