# PP.FILTER.REJECT.RESPONSE — Table Schema

> Source: `INSERTS/I_F.PP.FILTER.REJECT.RESPONSE` in `PP_FilteringService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FRR.CompanyID` | `PpFilterRejectResponse_Companyid` |  |  |  |
| 2 | `PP.FRR.Ranking` | `PpFilterRejectResponse_Ranking` |  |  |  |
| 3 | `PP.FRR.Direction` | `PpFilterRejectResponse_Direction` |  |  |  |
| 4 | `PP.FRR.Currency` | `PpFilterRejectResponse_Currency` |  |  |  |
| 5 | `PP.FRR.TransAmtLowerLimit` | `PpFilterRejectResponse_Transamtlowerlimit` |  |  |  |
| 6 | `PP.FRR.TransAmtUpperLimit` | `PpFilterRejectResponse_Transamtupperlimit` |  |  |  |
| 7 | `PP.FRR.RejectAction` | `PpFilterRejectResponse_Rejectaction` |  |  |  |
| 8 | `PP.FRR.StartDateFilterRejectResponse` | `PpFilterRejectResponse_Startdatefilterrejectresponse` |  |  |  |
| 9 | `PP.FRR.EndDateFilterRejectResponse` | `PpFilterRejectResponse_Enddatefilterrejectresponse` |  |  |  |
| 10 | `PP.FRR.RAC` | `PpFilterRejectResponse_Rac` |  |  |  |
| 11 | `PP.FRR.RSC` | `PpFilterRejectResponse_Rsc` |  |  |  |
| 12 | `PP.FRR.OldID` | `PpFilterRejectResponse_Oldid` |  |  |  |
| 13 | `PP.FRR.CurrentID` | `PpFilterRejectResponse_Currentid` |  |  |  |
| 14 | `PP.FRR.Action` | `PpFilterRejectResponse_Action` |  |  |  |
| 15 | `PP.FRR.OVERRIDE` | `PpFilterRejectResponse_Override` |  |  |  |
| 16 | `PP.FRR.RECORD.STATUS` | `PpFilterRejectResponse_RecordStatus` |  |  |  |
| 17 | `PP.FRR.CURR.NO` | `PpFilterRejectResponse_CurrNo` |  |  |  |
| 18 | `PP.FRR.INPUTTER` | `PpFilterRejectResponse_Inputter` |  |  |  |
| 19 | `PP.FRR.DATE.TIME` | `PpFilterRejectResponse_DateTime` |  |  |  |
| 20 | `PP.FRR.AUTHORISER` | `PpFilterRejectResponse_Authoriser` |  |  |  |
| 21 | `PP.FRR.CO.CODE` | `PpFilterRejectResponse_CoCode` |  |  |  |
| 22 | `PP.FRR.DEPT.CODE` | `PpFilterRejectResponse_DeptCode` |  |  |  |
| 23 | `PP.FRR.AUDITOR.CODE` | `PpFilterRejectResponse_AuditorCode` |  |  |  |
| 24 | `PP.FRR.AUDIT.DATE.TIME` | `PpFilterRejectResponse_AuditDateTime` |  |  |  |
