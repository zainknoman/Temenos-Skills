# PPT.STATUSACTION — Table Schema

> Source: `INSERTS/I_F.PPT.STATUSACTION` in `PP_TRIPService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSAC.CompanyID` | `PptStatusaction_Companyid` |  |  |  |
| 2 | `PPSAC.StatusCode` | `PptStatusaction_Statuscode` |  |  |  |
| 3 | `PPSAC.StartDateStatusAction` | `PptStatusaction_Startdatestatusaction` |  |  |  |
| 4 | `PPSAC.ProgramName` | `PptStatusaction_Programname` |  |  |  |
| 5 | `PPSAC.StatusActionDescription` | `PptStatusaction_Statusactiondescription` |  |  |  |
| 6 | `PPSAC.StatusRouterExpectedErrorCode` | `PptStatusaction_Statusrouterexpectederrorcode` |  |  |  |
| 7 | `PPSAC.StatusRouterExpectedStatus` | `PptStatusaction_Statusrouterexpectedstatus` |  |  |  |
| 8 | `PPSAC.EndDateStatusAction` | `PptStatusaction_Enddatestatusaction` |  |  |  |
| 9 | `PPSAC.RACStatusAction` | `PptStatusaction_Racstatusaction` |  |  |  |
| 10 | `PPSAC.RSCStatusAction` | `PptStatusaction_Rscstatusaction` |  |  |  |
| 11 | `PPSAC.EntryUserID` | `PptStatusaction_Entryuserid` |  |  |  |
| 12 | `PPSAC.EntryDateTime` | `PptStatusaction_Entrydatetime` |  |  |  |
| 13 | `PPSAC.ApproverUserID` | `PptStatusaction_Approveruserid` |  |  |  |
| 14 | `PPSAC.ApprovedDateTime` | `PptStatusaction_Approveddatetime` |  |  |  |
| 15 | `PPSAC.OriginatingSource` | `PptStatusaction_Originatingsource` |  |  |  |
