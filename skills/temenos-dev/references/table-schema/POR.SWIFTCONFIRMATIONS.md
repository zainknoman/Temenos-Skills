# POR.SWIFTCONFIRMATIONS — Table Schema

> Source: `INSERTS/I_F.POR.SWIFTCONFIRMATIONS` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPSW.CompanyID` | `PorSwiftconfirmations_Companyid` |  |  |  |
| 2 | `PPPSW.FTNumber` | `PorSwiftconfirmations_Ftnumber` |  |  |  |
| 3 | `PPPSW.AdviceNumber` | `PorSwiftconfirmations_Advicenumber` |  |  |  |
| 4 | `PPPSW.SequenceNumber` | `PorSwiftconfirmations_Sequencenumber` |  |  |  |
| 5 | `PPPSW.MTType` | `PorSwiftconfirmations_Mttype` |  |  |  |
| 6 | `PPPSW.BICCode` | `PorSwiftconfirmations_Biccode` |  |  |  |
| 7 | `PPPSW.ConfirmationSent` | `PorSwiftconfirmations_Confirmationsent` |  |  |  |
