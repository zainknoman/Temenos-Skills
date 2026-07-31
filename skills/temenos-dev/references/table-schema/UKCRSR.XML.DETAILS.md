# UKCRSR.XML.DETAILS — Table Schema

> Source: `INSERTS/I_F.UKCRSR.XML.DETAILS` in `UKCRSR_CRSReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKCRSR.XML.MESSAGE.CATEGORY` | `UkcrsrXmlDetails_MessageCategory` | TField |  |  |
| 2 | `UKCRSR.XML.FI.RETURN.ID` | `UkcrsrXmlDetails_FiReturnId` | TField |  |  |
| 3 | `UKCRSR.XML.MESSAGE.REF.ID` | `UkcrsrXmlDetails_MessageRefId` | TField |  |  |
| 4 | `UKCRSR.XML.STATUS` | `UkcrsrXmlDetails_Status` | TField |  | The status of the report can be New/Referred. whenever a file reference is selected in the drop down of UKCRSR.REPORT.GENERATION, the field should be updated as 'Referred'. |
| 5 | `UKCRSR.XML.REFERRED.AGAINST` | `UkcrsrXmlDetails_ReferredAgainst` | TField |  |  |
