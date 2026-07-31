# AA.PURPOSE.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.PURPOSE.TYPE` in `AF_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PT.DESCRIPTION` | `AaPurposeType_Description` |  |  |  |
| 2 | `AA.PT.STATUS` | `AaPurposeType_Status` | TField |  | The current STATUS of the PURPOSE.TYPE. Two statuses are allowed for a purpose type , once a PURPOSE record is authorised the status of this purpose in the purpose type table will be set to DESIGN. Later when the purpose is further defined in the OA.APPLICATION.DEFINIETION table and if such definition is succesfully pubished the status of the purpose type will be set to CATALOG .This mean that the purpose can be used for an application in OA.APPLICATION This field will be blank when AA.PURPOSE.TYPE is created 1)Maximum of 25 alphanumeric characters 2)At the moment values can only be DESIGN, or CATALOG |
| 3 | `AA.PT.EXPIRY.DATE` | `AaPurposeType_ExpiryDate` | TField |  | The Date beyond which the Purpose Type is no longer Valid and can not be used for an Application 1)Standard T24 Date , format is YYYYMMDD |
