# CAPL.W.CB.RPT.REQUEST — Table Schema

> Source: `INSERTS/I_F.CAPL.W.CB.RPT.REQUEST` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CB.BRANCH.ID` | `CaplWCbRptRequest_BranchId` |  |  |  |
| 2 | `CAPL.CB.NEW.REPORT` | `CaplWCbRptRequest_NewReport` |  |  |  |
| 3 | `CAPL.CB.IDECISION` | `CaplWCbRptRequest_Idecision` | TField |  |  |
| 4 | `CAPL.CB.JOINT.REQUEST` | `CaplWCbRptRequest_JointRequest` | TField |  | This field is used to define the request as joint request or not.Validation:Values are YES or NO.Default Value set as No. Allow to input YES when iDESC.FLAG is set to YES |
| 5 | `CAPL.CB.JOINT.CUSTOMER` | `CaplWCbRptRequest_JointCustomer` |  |  |  |
| 6 | `CAPL.CB.RESERVED.3` | `CaplWCbRptRequest_Reserved3` | TField |  |  |
| 7 | `CAPL.CB.RESERVED.4` | `CaplWCbRptRequest_Reserved4` | TField |  |  |
| 8 | `CAPL.CB.RESERVED.5` | `CaplWCbRptRequest_Reserved5` | TField |  |  |
| 9 | `CAPL.CB.LOCAL.REF` | `CaplWCbRptRequest_LocalRef` |  |  |  |
| 10 | `CAPL.CB.OVERRIDES` | `CaplWCbRptRequest_Overrides` |  |  |  |
| 11 | `CAPL.CB.RECORD.STATUS` | `CaplWCbRptRequest_RecordStatus` | String |  |  |
| 12 | `CAPL.CB.CURR.NO` | `CaplWCbRptRequest_CurrNo` | String |  |  |
| 13 | `CAPL.CB.INPUTTER` | `CaplWCbRptRequest_Inputter` |  |  |  |
| 14 | `CAPL.CB.DATE.TIME` | `CaplWCbRptRequest_DateTime` |  |  |  |
| 15 | `CAPL.CB.AUTHORISER` | `CaplWCbRptRequest_Authoriser` | String |  |  |
| 16 | `CAPL.CB.CO.CODE` | `CaplWCbRptRequest_CoCode` | String |  |  |
| 17 | `CAPL.CB.DEPT.CODE` | `CaplWCbRptRequest_DeptCode` | String |  |  |
| 18 | `CAPL.CB.AUDITOR.CODE` | `CaplWCbRptRequest_AuditorCode` | String |  |  |
| 19 | `CAPL.CB.AUDIT.DATE.TIME` | `CaplWCbRptRequest_AuditDateTime` | String |  |  |
