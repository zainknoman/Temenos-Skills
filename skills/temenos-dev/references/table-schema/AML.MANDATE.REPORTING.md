# AML.MANDATE.REPORTING — Table Schema

> Source: `INSERTS/I_F.AML.MANDATE.REPORTING` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AML.MAND.REPORT.DESCRIPTION` | `AmlMandateReporting_Description` | TField |  | Field to describe the purpose of the record. |
| 2 | `AML.MAND.REPORT.MANDATORY.FIELD` | `AmlMandateReporting_MandatoryField` |  |  |  |
| 3 | `AML.MAND.REPORT.RESTRICT.TXN` | `AmlMandateReporting_RestrictTxn` | TField |  |  |
| 4 | `AML.MAND.REPORT.RESTRICT.ERROR` | `AmlMandateReporting_RestrictError` | TField |  |  |
| 5 | `AML.MAND.REPORT.RESERVED.5` | `AmlMandateReporting_Reserved5` |  |  |  |
| 6 | `AML.MAND.REPORT.RESERVED.4` | `AmlMandateReporting_Reserved4` | TField |  |  |
| 7 | `AML.MAND.REPORT.RESERVED.3` | `AmlMandateReporting_Reserved3` | TField |  |  |
| 8 | `AML.MAND.REPORT.RESERVED.2` | `AmlMandateReporting_Reserved2` | TField |  |  |
| 9 | `AML.MAND.REPORT.RESERVED.1` | `AmlMandateReporting_Reserved1` | TField |  |  |
| 10 | `AML.MAND.REPORT.LOCAL.REF` | `AmlMandateReporting_LocalRef` |  |  |  |
| 11 | `AML.MAND.REPORT.RECORD.STATUS` | `AmlMandateReporting_RecordStatus` | String |  |  |
| 12 | `AML.MAND.REPORT.CURR.NO` | `AmlMandateReporting_CurrNo` | String |  |  |
| 13 | `AML.MAND.REPORT.INPUTTER` | `AmlMandateReporting_Inputter` |  |  |  |
| 14 | `AML.MAND.REPORT.DATE.TIME` | `AmlMandateReporting_DateTime` |  |  |  |
| 15 | `AML.MAND.REPORT.AUTHORISER` | `AmlMandateReporting_Authoriser` | String |  |  |
| 16 | `AML.MAND.REPORT.CO.CODE` | `AmlMandateReporting_CoCode` | String |  |  |
| 17 | `AML.MAND.REPORT.DEPT.CODE` | `AmlMandateReporting_DeptCode` | String |  |  |
| 18 | `AML.MAND.REPORT.AUDITOR.CODE` | `AmlMandateReporting_AuditorCode` | String |  |  |
| 19 | `AML.MAND.REPORT.AUDIT.DATE.TIME` | `AmlMandateReporting_AuditDateTime` | String |  |  |
