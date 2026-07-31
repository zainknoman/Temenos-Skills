# PP.ALLOWED.IPSYBIC — Table Schema

> Source: `INSERTS/I_F.PP.ALLOWED.IPSYBIC` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.AIB.CompanyID` | `PpAllowedIpsybic_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PP.AIB.AllowedIPSYBIC` | `PpAllowedIpsybic_Allowedipsybic` | TField | Yes | Indicates the BIC code that is allowed for IPSY payment processing. Validation Rules: Mandatory field. 35 alphanumeric characters. |
| 3 | `PP.AIB.StartDateAllowedIpsyBIC` | `PpAllowedIpsybic_Startdateallowedipsybic` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 4 | `PP.AIB.EndDateAllowedIpsyBIC` | `PpAllowedIpsybic_Enddateallowedipsybic` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 5 | `PP.AIB.RAC` | `PpAllowedIpsybic_Rac` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 6 | `PP.AIB.RSC` | `PpAllowedIpsybic_Rsc` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 7 | `PP.AIB.OldID` | `PpAllowedIpsybic_Oldid` | TField |  | Used for internal purpose. Holds the ID of the previous live record of store table. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 8 | `PP.AIB.CurrentID` | `PpAllowedIpsybic_Currentid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 9 | `PP.AIB.Action` | `PpAllowedIpsybic_Action` | TField |  | Used for internal purpose. Value of this field determines values of fields, 'RAC' and 'RSC' Possible values: N - New M - Modified R - Reverse This field can hold upto 1 alphanumeric character and the value is not editable by the user. |
| 10 | `PP.AIB.OVERRIDE` | `PpAllowedIpsybic_Override` |  |  |  |
| 11 | `PP.AIB.RECORD.STATUS` | `PpAllowedIpsybic_RecordStatus` | String |  |  |
| 12 | `PP.AIB.CURR.NO` | `PpAllowedIpsybic_CurrNo` | String |  |  |
| 13 | `PP.AIB.INPUTTER` | `PpAllowedIpsybic_Inputter` |  |  |  |
| 14 | `PP.AIB.DATE.TIME` | `PpAllowedIpsybic_DateTime` |  |  |  |
| 15 | `PP.AIB.AUTHORISER` | `PpAllowedIpsybic_Authoriser` | String |  |  |
| 16 | `PP.AIB.CO.CODE` | `PpAllowedIpsybic_CoCode` | String |  |  |
| 17 | `PP.AIB.DEPT.CODE` | `PpAllowedIpsybic_DeptCode` | String |  |  |
| 18 | `PP.AIB.AUDITOR.CODE` | `PpAllowedIpsybic_AuditorCode` | String |  |  |
| 19 | `PP.AIB.AUDIT.DATE.TIME` | `PpAllowedIpsybic_AuditDateTime` | String |  |  |
