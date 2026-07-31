# PPT.CLEARINGNATURECODE — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGNATURECODE` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCGN.CompanyID` | `PptClearingnaturecode_Companyid` |  |  |  |
| 2 | `PPCGN.ClearingID` | `PptClearingnaturecode_Clearingid` |  |  |  |
| 3 | `PPCGN.ClearingNatureCode` | `PptClearingnaturecode_Clearingnaturecode` |  |  |  |
| 4 | `PPCGN.StartDateClearingNatureCode` | `PptClearingnaturecode_Startdateclearingnaturecode` |  |  |  |
| 5 | `PPCGN.ClearingNatureCodeDescription` | `PptClearingnaturecode_Clearingnaturecodedescription` |  |  |  |
| 6 | `PPCGN.ChequeType` | `PptClearingnaturecode_Chequetype` |  |  |  |
| 7 | `PPCGN.EndDateClearingNatureCode` | `PptClearingnaturecode_Enddateclearingnaturecode` |  |  |  |
| 8 | `PPCGN.RACClearingNatureCode` | `PptClearingnaturecode_Racclearingnaturecode` |  |  |  |
| 9 | `PPCGN.RSCClearingNatureCode` | `PptClearingnaturecode_Rscclearingnaturecode` |  |  |  |
| 10 | `PPCGN.EntryUserID` | `PptClearingnaturecode_Entryuserid` |  |  |  |
| 11 | `PPCGN.EntryDateTime` | `PptClearingnaturecode_Entrydatetime` |  |  |  |
| 12 | `PPCGN.ApproverUserID` | `PptClearingnaturecode_Approveruserid` |  |  |  |
| 13 | `PPCGN.ApprovedDateTime` | `PptClearingnaturecode_Approveddatetime` |  |  |  |
