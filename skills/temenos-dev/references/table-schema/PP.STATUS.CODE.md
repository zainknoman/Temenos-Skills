# PP.STATUS.CODE — Table Schema

> Source: `INSERTS/I_F.PP.STATUS.CODE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SCD.StatusDescription` | `PpStatusCode_Statusdescription` | TField |  | Holds the description of a specific status code that is entered in the field StatusCode. Possible Values: Alpha Numeric Text - 128 Length |
| 2 | `PP.SCD.GPIStatus` | `PpStatusCode_Gpistatus` | TField |  | Holds the GPIStatus for the StatusCode. |
| 3 | `PP.SCD.ReasonCode` | `PpStatusCode_Reasoncode` | TField |  | Holds the ReasonCode. |
| 4 | `PP.SCD.CSRStatus` | `PpStatusCode_Csrstatus` | TField | No | Optional field. This field indicates that the Customer status report is enabled for Individual transactions parked in Interim status. |
| 5 | `PP.SCD.CSRStatusDescription` | `PpStatusCode_Csrstatusdescription` | TField |  | Conditional field. This field indicates the description of the Interim status. If value in CSRStatus is present , then CSRStatusDescription must not be left blank. |
| 6 | `PP.SCD.ShortDescription` | `PpStatusCode_Shortdescription` | TField |  | Holds the short description of a specific status code that is entered in the field StatusCode. Possible Values: Alpha Numeric Text - 128 Length |
| 7 | `PP.SCD.LOCAL.REF` | `PpStatusCode_LocalRef` |  |  |  |
| 8 | `PP.SCD.OVERRIDE` | `PpStatusCode_Override` |  |  |  |
| 9 | `PP.SCD.RECORD.STATUS` | `PpStatusCode_RecordStatus` | String |  |  |
| 10 | `PP.SCD.CURR.NO` | `PpStatusCode_CurrNo` | String |  |  |
| 11 | `PP.SCD.INPUTTER` | `PpStatusCode_Inputter` |  |  |  |
| 12 | `PP.SCD.DATE.TIME` | `PpStatusCode_DateTime` |  |  |  |
| 13 | `PP.SCD.AUTHORISER` | `PpStatusCode_Authoriser` | String |  |  |
| 14 | `PP.SCD.CO.CODE` | `PpStatusCode_CoCode` | String |  |  |
| 15 | `PP.SCD.DEPT.CODE` | `PpStatusCode_DeptCode` | String |  |  |
| 16 | `PP.SCD.AUDITOR.CODE` | `PpStatusCode_AuditorCode` | String |  |  |
| 17 | `PP.SCD.AUDIT.DATE.TIME` | `PpStatusCode_AuditDateTime` | String |  |  |
