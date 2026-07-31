# PPT.CLEARINGCORRESPONDENTS — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGCORRESPONDENTS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCGC.ClearingCorrespondentID` | `PptClearingcorrespondents_Clearingcorrespondentid` |  |  |  |
| 2 | `PPCGC.CompanyID` | `PptClearingcorrespondents_Companyid` |  |  |  |
| 3 | `PPCGC.Clearing` | `PptClearingcorrespondents_Clearing` |  |  |  |
| 4 | `PPCGC.StartDateClearingCorrespond` | `PptClearingcorrespondents_Startdateclearingcorrespond` |  |  |  |
| 5 | `PPCGC.BICCodeCorrespondent` | `PptClearingcorrespondents_Biccodecorrespondent` |  |  |  |
| 6 | `PPCGC.EndDateClearingCorrespond` | `PptClearingcorrespondents_Enddateclearingcorrespond` |  |  |  |
| 7 | `PPCGC.RACClearingCorrespondents` | `PptClearingcorrespondents_Racclearingcorrespondents` |  |  |  |
| 8 | `PPCGC.RSCClearingCorrespondents` | `PptClearingcorrespondents_Rscclearingcorrespondents` |  |  |  |
| 9 | `PPCGC.EntryUserID` | `PptClearingcorrespondents_Entryuserid` |  |  |  |
| 10 | `PPCGC.EntryDateTime` | `PptClearingcorrespondents_Entrydatetime` |  |  |  |
| 11 | `PPCGC.ApproverUserID` | `PptClearingcorrespondents_Approveruserid` |  |  |  |
| 12 | `PPCGC.ApprovedDateTime` | `PptClearingcorrespondents_Approveddatetime` |  |  |  |
