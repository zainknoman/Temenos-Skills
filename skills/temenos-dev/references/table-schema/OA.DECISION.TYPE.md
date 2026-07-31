# OA.DECISION.TYPE — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.TYPE` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DT.DESCRIPTION` | `OaDecisionType_Description` |  |  |  |
| 2 | `OA.DT.CLASS.NAME` | `OaDecisionType_ClassName` | TField |  | Name of the class as given in AA.DEFINITION.MANAGER. Should belong to OA.DECISION.CLASS |
| 3 | `OA.DT.STATUS` | `OaDecisionType_Status` | TField |  | It specifies the STATUS of the current decision type. The only allowed value is PUBLISHED. |
| 4 | `OA.DT.AVAILABLE.DATE` | `OaDecisionType_AvailableDate` | TField |  | The Date from which the Decision Type is Valid. Standard T24 Date, format is YYYYMMDD. |
| 5 | `OA.DT.EXPIRY.DATE` | `OaDecisionType_ExpiryDate` | TField |  | The Date beyond which the Decision Type is no longer Valid.Standard T24 Date, format is YYYYMMDD. |
| 6 | `OA.DT.LAST.PUBLISHED` | `OaDecisionType_LastPublished` | TField |  | The Date at which the Decision Type is published. It will be TODAY&apos;s date.Standard T24 Date, format is YYYYMMDD. |
