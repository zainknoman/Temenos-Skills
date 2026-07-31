# EV.EVIDENCE.TYPE — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.TYPE` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVT.DESCRIPTION` | `EvEvidenceType_Description` |  |  |  |
| 2 | `EV.EVT.CLASS.NAME` | `EvEvidenceType_ClassName` | TField |  | Name of the class as given in AA.DEFINITION.MANAGER. Should belong to EV.EVIDENCE.CLASS |
| 3 | `EV.EVT.STATUS` | `EvEvidenceType_Status` | TField |  | The current STATUS of the EVIDENCE.TYPE. The only allowed Status PUBLISHED will get update after publishing the definition. |
| 4 | `EV.EVT.AVAILABLE.DATE` | `EvEvidenceType_AvailableDate` | TField |  | The Date from which the Evidence Type is Valid. 1)Standard T24 Date , format is YYYYMMDD |
| 5 | `EV.EVT.EXPIRY.DATE` | `EvEvidenceType_ExpiryDate` | TField |  | The Date beyond which the Evidence Type is no longer Valid and can not be used as an Evidence 1)Standard T24 Date , format is YYYYMMDD |
| 6 | `EV.EVT.LAST.PUBLISHED` | `EvEvidenceType_LastPublished` | TField |  | The Date at which the Evidence Type is published. It will be TODAY&apos;s date. 1)Standard T24 Date , format is YYYYMMDD |
