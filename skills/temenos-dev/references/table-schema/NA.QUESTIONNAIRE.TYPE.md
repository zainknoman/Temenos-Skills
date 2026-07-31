# NA.QUESTIONNAIRE.TYPE — Table Schema

> Source: `INSERTS/I_F.NA.QUESTIONNAIRE.TYPE` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.NQT.DESCRIPTION` | `NaQuestionnaireType_Description` |  |  |  |
| 2 | `NA.NQT.CLASS.NAME` | `NaQuestionnaireType_ClassName` | TField |  | Name of the class as given in AA.DEFINITION.MANAGER. Should belong to NA.NEEDS.CLASS |
| 3 | `NA.NQT.STATUS` | `NaQuestionnaireType_Status` | TField |  | The current STATUS of the Needs Questionnaire Type. The only allowed Status PUBLISHED will get update after publishing the definition. |
| 4 | `NA.NQT.AVAILABLE.DATE` | `NaQuestionnaireType_AvailableDate` | TField |  | The Date from which the Evidence Type is Valid. Standard T24 Date, format is YYYYMMDD |
| 5 | `NA.NQT.EXPIRY.DATE` | `NaQuestionnaireType_ExpiryDate` | TField |  | The Date beyond which the Questionnaire Type is no longer Valid.Standard T24 Date, format is YYYYMMDD |
| 6 | `NA.NQT.LAST.PUBLISHED` | `NaQuestionnaireType_LastPublished` | TField |  | The Date at which the Evidence Type is published. It will be TODAY&apos;s date.Standard T24 Date, format is YYYYMMDD |
