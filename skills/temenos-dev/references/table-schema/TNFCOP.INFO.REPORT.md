# TNFCOP.INFO.REPORT — Table Schema

> Source: `INSERTS/I_F.TNFCOP.INFO.REPORT` in `TNFCOP_InformationSheet.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INFO.RPT.FROM.DATE` | `TnfcopInfoReport_FromDate` | TField |  | This field stores the date from when the report has to be generated. |
| 2 | `INFO.RPT.TO.DATE` | `TnfcopInfoReport_ToDate` | TField |  | This field stores the date until which the report has to be generated.. |
| 3 | `INFO.RPT.SERVICE.ID` | `TnfcopInfoReport_ServiceId` | TField |  | This field stores the name of the service which has to be run. |
| 4 | `INFO.RPT.STATUS` | `TnfcopInfoReport_Status` | TField |  | This field stores the status of the record. |
| 5 | `INFO.RPT.RESERVED.1` | `TnfcopInfoReport_Reserved1` | TField |  |  |
| 6 | `INFO.RPT.LOCAL.REF` | `TnfcopInfoReport_LocalRef` |  |  |  |
| 7 | `INFO.RPT.OVERRIDE` | `TnfcopInfoReport_Override` |  |  |  |
| 8 | `INFO.RPT.RECORD.STATUS` | `TnfcopInfoReport_RecordStatus` | String |  |  |
| 9 | `INFO.RPT.CURR.NO` | `TnfcopInfoReport_CurrNo` | String |  |  |
| 10 | `INFO.RPT.INPUTTER` | `TnfcopInfoReport_Inputter` |  |  |  |
| 11 | `INFO.RPT.DATE.TIME` | `TnfcopInfoReport_DateTime` |  |  |  |
| 12 | `INFO.RPT.AUTHORISER` | `TnfcopInfoReport_Authoriser` | String |  |  |
| 13 | `INFO.RPT.CO.CODE` | `TnfcopInfoReport_CoCode` | String |  |  |
| 14 | `INFO.RPT.DEPT.CODE` | `TnfcopInfoReport_DeptCode` | String |  |  |
| 15 | `INFO.RPT.AUDITOR.CODE` | `TnfcopInfoReport_AuditorCode` | String |  |  |
| 16 | `INFO.RPT.AUDIT.DATE.TIME` | `TnfcopInfoReport_AuditDateTime` | String |  |  |
