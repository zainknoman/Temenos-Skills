# PP.MULTIPLE.MSG.SWIFT — Table Schema

> Source: `INSERTS/I_F.PP.MULTIPLE.MSG.SWIFT` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMMT.TotalTxn` | `PpMultipleMsgSwift_Totaltxn` | TField |  |  |
| 2 | `PPMMT.ReceivedTxn` | `PpMultipleMsgSwift_Receivedtxn` | TField |  |  |
| 3 | `PPMMT.ChildTxn` | `PpMultipleMsgSwift_Childtxn` | TField |  |  |
| 4 | `PPMMT.TotalAmount` | `PpMultipleMsgSwift_Totalamount` | TField |  |  |
| 5 | `PPMMT.ReceivedFileDetailsID` | `PpMultipleMsgSwift_Receivedfiledetailsid` |  |  |  |
| 6 | `PPMMT.ParentProcessed` | `PpMultipleMsgSwift_Parentprocessed` | TField |  |  |
| 7 | `PPMMT.ParentFTNumber` | `PpMultipleMsgSwift_Parentftnumber` | TField |  |  |
| 8 | `PPMMT.RESERVED.5` | `PpMultipleMsgSwift_Reserved5` | TField |  |  |
| 9 | `PPMMT.RESERVED.4` | `PpMultipleMsgSwift_Reserved4` | TField |  |  |
| 10 | `PPMMT.RESERVED.3` | `PpMultipleMsgSwift_Reserved3` | TField |  |  |
| 11 | `PPMMT.RESERVED.2` | `PpMultipleMsgSwift_Reserved2` | TField |  |  |
| 12 | `PPMMT.RESERVED.1` | `PpMultipleMsgSwift_Reserved1` | TField |  |  |
