# PPT.LCTSAFREQUENCIES — Table Schema

> Source: `INSERTS/I_F.PPT.LCTSAFREQUENCIES` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPFRQ.CompanyID` | `PptLctsafrequencies_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PPFRQ.LCTSAFrequenciesID` | `PptLctsafrequencies_Lctsafrequenciesid` | TField |  | Holds unique ID which refers to the LCTSA Frequencies in the payments hub. Validation Rules: 65 alphanumeric characters. |
| 3 | `PPFRQ.ClearingID` | `PptLctsafrequencies_Clearingid` | TField | Yes | Holds ID which refers to the clearing in the payments hub. Validation Rules: Mandatory field. 10 alphanumeric characters. The value links to field 'ClearingID' in PPT.CLEARING |
| 4 | `PPFRQ.TSAServiceID` | `PptLctsafrequencies_Tsaserviceid` | TField | Yes | This is the ID of the TSA service from T24 TSA.SERVICE table. Validation Rules: Mandatory field. 50 alphanumeric characters. |
| 5 | `PPFRQ.Frequency1` | `PptLctsafrequencies_Frequency1` | TField |  | Frequency 1. Validation Rules: 5 characters. |
| 6 | `PPFRQ.Frequency2` | `PptLctsafrequencies_Frequency2` | TField |  | Frequency 2. Validation Rules: 30 characters. |
| 7 | `PPFRQ.Frequency3` | `PptLctsafrequencies_Frequency3` | TField |  | Frequency 3. Validation Rules: 30 characters. |
| 8 | `PPFRQ.Frequency4` | `PptLctsafrequencies_Frequency4` | TField |  | Frequency 4. Validation Rules: 30 characters. |
| 9 | `PPFRQ.Frequency5` | `PptLctsafrequencies_Frequency5` | TField |  | Frequency 5. Validation Rules: 30 characters. |
| 10 | `PPFRQ.RACLCTsaFrequencies` | `PptLctsafrequencies_Raclctsafrequencies` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 11 | `PPFRQ.RSCLCTsaFrequencies` | `PptLctsafrequencies_Rsclctsafrequencies` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 12 | `PPFRQ.EntryUserID` | `PptLctsafrequencies_Entryuserid` | TField |  | Indicates the user that created or modified the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 13 | `PPFRQ.EntryDateTime` | `PptLctsafrequencies_Entrydatetime` | TField |  | Indicates the system date and time when the entry was created or modified. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
| 14 | `PPFRQ.ApproverUserID` | `PptLctsafrequencies_Approveruserid` | TField |  | Indicates the name of the user who approved the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 15 | `PPFRQ.ApprovedDateTime` | `PptLctsafrequencies_Approveddatetime` | TField |  | Indicates the system date and time when the entry was approved. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
