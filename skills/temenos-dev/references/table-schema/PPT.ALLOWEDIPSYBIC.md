# PPT.ALLOWEDIPSYBIC — Table Schema

> Source: `INSERTS/I_F.PPT.ALLOWEDIPSYBIC` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPAIB.CompanyID` | `PptAllowedipsybic_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PPAIB.AllowedIPSYBIC` | `PptAllowedipsybic_Allowedipsybic` | TField | Yes | Indicates the BIC code that is allowed for IPSY payment processing. Validation Rules: Mandatory field. 35 alphanumeric characters. |
| 3 | `PPAIB.StartDateAllowedIpsyBIC` | `PptAllowedipsybic_Startdateallowedipsybic` | TField | Yes | Specifies the date on which the record is to be considered active by the payments hub. Validation Rules: Mandatory field. 11 characters DATE format |
| 4 | `PPAIB.EndDateAllowedIpsyBIC` | `PptAllowedipsybic_Enddateallowedipsybic` | TField | Yes | Specifies the date on which the record is to be considered inactive by the payments hub. Validation Rules: Mandatory field. 11 characters DATE format |
| 5 | `PPAIB.RACAllowedIpsyBIC` | `PptAllowedipsybic_Racallowedipsybic` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 6 | `PPAIB.RSCAllowedIpsyBIC` | `PptAllowedipsybic_Rscallowedipsybic` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 7 | `PPAIB.EntryUserID` | `PptAllowedipsybic_Entryuserid` | TField |  | Indicates the user that created or modified the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 8 | `PPAIB.EntryDateTime` | `PptAllowedipsybic_Entrydatetime` | TField |  | Indicates the system date and time when the entry was created or modified. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
| 9 | `PPAIB.ApproverUserID` | `PptAllowedipsybic_Approveruserid` | TField |  | Indicates the name of the user who approved the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 10 | `PPAIB.ApprovedDateTime` | `PptAllowedipsybic_Approveddatetime` | TField |  | Indicates the system date and time when the entry was approved. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
