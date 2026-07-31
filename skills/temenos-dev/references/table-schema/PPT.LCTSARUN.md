# PPT.LCTSARUN — Table Schema

> Source: `INSERTS/I_F.PPT.LCTSARUN` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTSA.CompanyID` | `PptLctsarun_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PPTSA.ClearingID` | `PptLctsarun_Clearingid` | TField | Yes | Holds ID which refers to the clearing in the payments hub. Validation Rules: Mandatory field. 10 alphanumeric characters. The value links to field 'ClearingID' in PPT.CLEARING |
| 3 | `PPTSA.TSAServiceID` | `PptLctsarun_Tsaserviceid` | TField | Yes | TSAService ID. Validation Rules: Mandatory field. 50 alphanumeric characters. This is the ID of the TSA service from TSA.SERVICE table. |
| 4 | `PPTSA.StartTimestamp` | `PptLctsarun_Starttimestamp` | TField | Yes | Holds the timestamp when TSA was started. Validation Rules: Mandatory field. 17 characters TIME. |
| 5 | `PPTSA.EndTimestamp` | `PptLctsarun_Endtimestamp` | TField |  | Holds the timestamp when TSA was finished. Validation Rules: 17 characters TIME. |
| 6 | `PPTSA.TSAFinished` | `PptLctsarun_Tsafinished` | TField |  | TSA Finished. It can take the values: Y or N. |
