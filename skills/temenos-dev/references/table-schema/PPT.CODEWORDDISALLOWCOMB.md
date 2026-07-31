# PPT.CODEWORDDISALLOWCOMB — Table Schema

> Source: `INSERTS/I_F.PPT.CODEWORDDISALLOWCOMB` in `PP_SwiftOutService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCWD.CodeWord1` | `PptCodeworddisallowcomb_Codeword1` | TField | Yes | The codeword received in the payment instruction Validation Rules: Mandatory field. 8 alphanumeric character. |
| 2 | `PPCWD.CodeWord2` | `PptCodeworddisallowcomb_Codeword2` | TField | Yes | The codeword received in the payment instruction Validation Rules: Mandatory field. 8 alphanumeric character. |
| 3 | `PPCWD.StartDateCodewDisallowedCombi` | `PptCodeworddisallowcomb_Startdatecodewdisallowedcombi` | TField |  | ??? |
| 4 | `PPCWD.EndDateCodewDisallowedCombi` | `PptCodeworddisallowcomb_Enddatecodewdisallowedcombi` | TField |  | ??? |
| 5 | `PPCWD.RACCodeWordDisallowedCombi` | `PptCodeworddisallowcomb_Raccodeworddisallowedcombi` | TField |  |  |
| 6 | `PPCWD.RSCCodeWordDisallowedCombi` | `PptCodeworddisallowcomb_Rsccodeworddisallowedcombi` | TField |  |  |
| 7 | `PPCWD.EntryUserID` | `PptCodeworddisallowcomb_Entryuserid` | TField |  |  |
| 8 | `PPCWD.EntryDateTime` | `PptCodeworddisallowcomb_Entrydatetime` | TField |  |  |
| 9 | `PPCWD.ApproverUserID` | `PptCodeworddisallowcomb_Approveruserid` | TField |  |  |
| 10 | `PPCWD.ApprovedDateTime` | `PptCodeworddisallowcomb_Approveddatetime` | TField |  |  |
