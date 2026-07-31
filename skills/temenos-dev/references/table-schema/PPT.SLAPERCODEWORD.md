# PPT.SLAPERCODEWORD — Table Schema

> Source: `INSERTS/I_F.PPT.SLAPERCODEWORD` in `PP_SLADeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSLA.CompanyID` | `PptSlapercodeword_Companyid` |  |  |  |
| 2 | `PPSLA.MessagePriority` | `PptSlapercodeword_Messagepriority` |  |  |  |
| 3 | `PPSLA.CodeWord` | `PptSlapercodeword_Codeword` |  |  |  |
| 4 | `PPSLA.CodeWordTag` | `PptSlapercodeword_Codewordtag` |  |  |  |
| 5 | `PPSLA.CodeWordText` | `PptSlapercodeword_Codewordtext` |  |  |  |
| 6 | `PPSLA.Ranking` | `PptSlapercodeword_Ranking` |  |  |  |
| 7 | `PPSLA.StartDateSLAPerCodeWord` | `PptSlapercodeword_Startdateslapercodeword` |  |  |  |
| 8 | `PPSLA.SLAID` | `PptSlapercodeword_Slaid` |  |  |  |
| 9 | `PPSLA.EndDateSLAPerCodeWord` | `PptSlapercodeword_Enddateslapercodeword` |  |  |  |
| 10 | `PPSLA.RACSLAPerCodeWord` | `PptSlapercodeword_Racslapercodeword` |  |  |  |
| 11 | `PPSLA.RSCSLAPerCodeWord` | `PptSlapercodeword_Rscslapercodeword` |  |  |  |
| 12 | `PPSLA.EntryUserID` | `PptSlapercodeword_Entryuserid` |  |  |  |
| 13 | `PPSLA.EntryDateTime` | `PptSlapercodeword_Entrydatetime` |  |  |  |
| 14 | `PPSLA.ApproverUserID` | `PptSlapercodeword_Approveruserid` |  |  |  |
| 15 | `PPSLA.ApprovedDateTime` | `PptSlapercodeword_Approveddatetime` |  |  |  |
