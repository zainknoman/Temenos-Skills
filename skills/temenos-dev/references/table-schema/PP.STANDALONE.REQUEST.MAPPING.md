# PP.STANDALONE.REQUEST.MAPPING — Table Schema

> Source: `INSERTS/I_F.PP.STANDALONE.REQUEST.MAPPING` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSRM.Description` | `PpStandaloneRequestMapping_Description` | TField |  | Holds description of the mapping record |
| 2 | `PPSRM.RequestType` | `PpStandaloneRequestMapping_Requesttype` | TField |  |  |
| 3 | `PPSRM.ApplicationName` | `PpStandaloneRequestMapping_Applicationname` |  |  |  |
| 4 | `PPSRM.FieldName` | `PpStandaloneRequestMapping_Fieldname` |  |  |  |
| 5 | `PPSRM.FieldPosition` | `PpStandaloneRequestMapping_Fieldposition` |  |  |  |
| 6 | `PPSRM.Mandatory` | `PpStandaloneRequestMapping_Mandatory` |  |  |  |
| 7 | `PPSRM.Routine` | `PpStandaloneRequestMapping_Routine` |  |  |  |
| 8 | `PPSRM.ConstantValue` | `PpStandaloneRequestMapping_Constantvalue` |  |  |  |
| 9 | `PPSRM.PaymentDetailsToEmit` | `PpStandaloneRequestMapping_Paymentdetailstoemit` | TField |  | This field indicates whether all the details from POR tables or set of fields must be emitted out to the external system for the request type Possible values are: Complete or blank If �Complete� is selected, then all the details from POR tables will be emitted for that request type If it is blank, then details defined in PP.STANDALONE.REQUEST.MAPPING will only be emitted out |
| 10 | `PPSRM.RESERVED.9` | `PpStandaloneRequestMapping_Reserved9` | TField |  |  |
| 11 | `PPSRM.RESERVED.8` | `PpStandaloneRequestMapping_Reserved8` | TField |  |  |
| 12 | `PPSRM.RESERVED.7` | `PpStandaloneRequestMapping_Reserved7` | TField |  |  |
| 13 | `PPSRM.RESERVED.6` | `PpStandaloneRequestMapping_Reserved6` | TField |  |  |
| 14 | `PPSRM.RESERVED.5` | `PpStandaloneRequestMapping_Reserved5` | TField |  |  |
| 15 | `PPSRM.RESERVED.4` | `PpStandaloneRequestMapping_Reserved4` | TField |  |  |
| 16 | `PPSRM.RESERVED.3` | `PpStandaloneRequestMapping_Reserved3` | TField |  |  |
| 17 | `PPSRM.RESERVED.2` | `PpStandaloneRequestMapping_Reserved2` | TField |  |  |
| 18 | `PPSRM.RESERVED.1` | `PpStandaloneRequestMapping_Reserved1` | TField |  |  |
| 19 | `PPSRM.OVERRIDE` | `PpStandaloneRequestMapping_Override` |  |  |  |
| 20 | `PPSRM.RECORD.STATUS` | `PpStandaloneRequestMapping_RecordStatus` | String |  |  |
| 21 | `PPSRM.CURR.NO` | `PpStandaloneRequestMapping_CurrNo` | String |  |  |
| 22 | `PPSRM.INPUTTER` | `PpStandaloneRequestMapping_Inputter` |  |  |  |
| 23 | `PPSRM.DATE.TIME` | `PpStandaloneRequestMapping_DateTime` |  |  |  |
| 24 | `PPSRM.AUTHORISER` | `PpStandaloneRequestMapping_Authoriser` | String |  |  |
| 25 | `PPSRM.CO.CODE` | `PpStandaloneRequestMapping_CoCode` | String |  |  |
| 26 | `PPSRM.DEPT.CODE` | `PpStandaloneRequestMapping_DeptCode` | String |  |  |
| 27 | `PPSRM.AUDITOR.CODE` | `PpStandaloneRequestMapping_AuditorCode` | String |  |  |
| 28 | `PPSRM.AUDIT.DATE.TIME` | `PpStandaloneRequestMapping_AuditDateTime` | String |  |  |
