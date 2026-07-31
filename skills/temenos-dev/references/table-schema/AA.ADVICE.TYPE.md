# AA.ADVICE.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.ADVICE.TYPE` in `AF_Advice.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ADV.DESCRIPTION` | `AaAdviceType_Description` |  |  |  |
| 2 | `AA.ADV.CLASS.NAME` | `AaAdviceType_ClassName` | TField |  |  |
| 3 | `AA.ADV.STATUS` | `AaAdviceType_Status` | TField |  | It specifies the current status of the advice definition. The STATUS will update as PUBLISHED while publishing the AA.DEFINITION.MANAGER of ADVICE.CLASS definition. |
| 4 | `AA.ADV.AVAILABLE.DATE` | `AaAdviceType_AvailableDate` | TField |  | The Date from which the Advice Type is Valid. 1)Standard T24 Date , format is YYYYMMDD |
| 5 | `AA.ADV.EXPIRY.DATE` | `AaAdviceType_ExpiryDate` | TField |  | The Date beyond which the Advice Type is no longer Valid and can not be used as an Advice 1)Standard T24 Date , format is YYYYMMDD |
| 6 | `AA.ADV.LAST.PUBLISHED` | `AaAdviceType_LastPublished` | TField |  | The Date at which the Advice Type is published. It will be TODAY's date. 1)Standard T24 Date , format is YYYYMMDD |
| 7 | `AA.ADV.ADVICE.APPLICATION.NAMES` | `AaAdviceType_AdviceApplicationNames` |  |  |  |
| 8 | `AA.ADV.ADVICE.APPLICATION.IDS` | `AaAdviceType_AdviceApplicationIds` |  |  |  |
