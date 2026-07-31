# AA.QUOTATION.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.TYPE` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.QT.DESCRIPTION` | `AaQuotationType_Description` |  |  |  |
| 2 | `AA.QT.CLASS.NAME` | `AaQuotationType_ClassName` | TField |  | Class name as given in AA.DEFINITION.MANAGER. Should belong to AA.QUOTATION.CLASS |
| 3 | `AA.QT.STATUS` | `AaQuotationType_Status` | TField |  | It specifies the STATUS of the current quotation type. The only status PUBLISHED is updated after publishing the quotation type. |
| 4 | `AA.QT.AVAILABLE.DATE` | `AaQuotationType_AvailableDate` | TField |  | The Date from which the Evidence Type is Valid. Standard T24 Date, format is YYYYMMDD. |
| 5 | `AA.QT.EXPIRY.DATE` | `AaQuotationType_ExpiryDate` | TField |  | The Date beyond which the Quotation Type is no longer Valid.Standard T24 Date, format is YYYYMMDD. |
| 6 | `AA.QT.LAST.PUBLISHED` | `AaQuotationType_LastPublished` | TField |  | The Date at which the Quotation Type is published. It will be TODAY&apos;s date.Standard T24 Date, format is YYYYMMDD. |
