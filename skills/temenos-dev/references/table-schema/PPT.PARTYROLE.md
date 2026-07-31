# PPT.PARTYROLE — Table Schema

> Source: `INSERTS/I_F.PPT.PARTYROLE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPTR.PartyRole` | `PptPartyrole_Partyrole` |  |  |  |
| 2 | `PPPTR.PartyRoleTag` | `PptPartyrole_Partyroletag` |  |  |  |
| 3 | `PPPTR.PartyRoleDescription` | `PptPartyrole_Partyroledescription` |  |  |  |
| 4 | `PPPTR.RACPartyRole` | `PptPartyrole_Racpartyrole` |  |  |  |
| 5 | `PPPTR.RSCPartyRole` | `PptPartyrole_Rscpartyrole` |  |  |  |
| 6 | `PPPTR.EntryUserID` | `PptPartyrole_Entryuserid` |  |  |  |
| 7 | `PPPTR.EntryDateTime` | `PptPartyrole_Entrydatetime` |  |  |  |
| 8 | `PPPTR.ApproverUserID` | `PptPartyrole_Approveruserid` |  |  |  |
| 9 | `PPPTR.ApprovedDateTime` | `PptPartyrole_Approveddatetime` |  |  |  |
