# POR.OUTBOUNDINFO — Table Schema

> Source: `INSERTS/I_F.POR.OUTBOUNDINFO` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPOI.CompanyID` | `PorOutboundinfo_Companyid` |  |  |  |
| 2 | `PPPOI.FTNumber` | `PorOutboundinfo_Ftnumber` |  |  |  |
| 3 | `PPPOI.InstructionCode` | `PorOutboundinfo_Instructioncode` |  |  |  |
| 4 | `PPPOI.InformationTypeLineSequence` | `PorOutboundinfo_Informationtypelinesequence` |  |  |  |
| 5 | `PPPOI.CountryCode` | `PorOutboundinfo_Countrycode` |  |  |  |
| 6 | `PPPOI.InformationLine` | `PorOutboundinfo_Informationline` |  |  |  |
| 7 | `PPPOI.InformationCode` | `PorOutboundinfo_Informationcode` |  |  |  |
