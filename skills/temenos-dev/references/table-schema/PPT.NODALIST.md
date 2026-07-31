# PPT.NODALIST — Table Schema

> Source: `INSERTS/I_F.PPT.NODALIST` in `PP_DebitAuthorityService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPNOD.CompanyID` | `PptNodalist_Companyid` |  |  |  |
| 2 | `PPNOD.IncomingMessageType` | `PptNodalist_Incomingmessagetype` |  |  |  |
| 3 | `PPNOD.StartDateDebitAuthorityFilter` | `PptNodalist_Startdatedebitauthorityfilter` |  |  |  |
| 4 | `PPNOD.EndDateDebitAuthorityFilter` | `PptNodalist_Enddatedebitauthorityfilter` |  |  |  |
| 5 | `PPNOD.RACNoDAList` | `PptNodalist_Racnodalist` |  |  |  |
| 6 | `PPNOD.RSCNoDAList` | `PptNodalist_Rscnodalist` |  |  |  |
| 7 | `PPNOD.EntryUserID` | `PptNodalist_Entryuserid` |  |  |  |
| 8 | `PPNOD.EntryDateTime` | `PptNodalist_Entrydatetime` |  |  |  |
| 9 | `PPNOD.ApproverUserID` | `PptNodalist_Approveruserid` |  |  |  |
| 10 | `PPNOD.ApprovedDateTime` | `PptNodalist_Approveddatetime` |  |  |  |
