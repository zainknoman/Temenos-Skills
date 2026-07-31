# PPT.NORMA — Table Schema

> Source: `INSERTS/I_F.PPT.NORMA` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPNOR.NoRMAID` | `PptNorma_Normaid` |  |  |  |
| 2 | `PPNOR.CompanyID` | `PptNorma_Companyid` |  |  |  |
| 3 | `PPNOR.MessageID` | `PptNorma_Messageid` |  |  |  |
| 4 | `PPNOR.StartDateNoRMA` | `PptNorma_Startdatenorma` |  |  |  |
| 5 | `PPNOR.EndDateNoRMA` | `PptNorma_Enddatenorma` |  |  |  |
| 6 | `PPNOR.RACNoRMA` | `PptNorma_Racnorma` |  |  |  |
| 7 | `PPNOR.RSCNoRMA` | `PptNorma_Rscnorma` |  |  |  |
| 8 | `PPNOR.EntryUserID` | `PptNorma_Entryuserid` |  |  |  |
| 9 | `PPNOR.EntryDateTime` | `PptNorma_Entrydatetime` |  |  |  |
| 10 | `PPNOR.ApproverUserID` | `PptNorma_Approveruserid` |  |  |  |
| 11 | `PPNOR.ApprovedDateTime` | `PptNorma_Approveddatetime` |  |  |  |
