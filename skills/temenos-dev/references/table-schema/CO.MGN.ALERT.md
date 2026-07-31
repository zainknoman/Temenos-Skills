# CO.MGN.ALERT — Table Schema

> Source: `INSERTS/I_F.CO.MGN.ALERT` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMA.OLD.MARGIN.LEVEL` | `CoMgnAlert_OldMarginLevel` | TField |  | Specifies the application from which the current low advance ratio has been considered. |
| 2 | `CMA.NEW.MARGIN.LEVEL` | `CoMgnAlert_NewMarginLevel` | TField |  | Specifies the application from which the current high advance ratio has to be considered. |
| 3 | `CMA.OLD.MARGIN.ID` | `CoMgnAlert_OldMarginId` | TField |  | ID of the application of old/previous High advance ratio. |
| 4 | `CMA.NEW.MARGIN.ID` | `CoMgnAlert_NewMarginId` | TField |  | ID of the application from which current High advance ratio has been considered. |
| 5 | `CMA.OLD.MARGIN.RATE` | `CoMgnAlert_OldMarginRate` | TField |  | Specifies the old/previous high advance rate value. Validation Rules: 1. Standard T24 rate field |
| 6 | `CMA.NEW.MARGIN.RATE` | `CoMgnAlert_NewMarginRate` | TField |  | Specifies the current high advance rate value. Validation Rules: 1. Standard T24 rate field |
| 7 | `CMA.OLD.ADJ.MARGIN.LEVEL` | `CoMgnAlert_OldAdjMarginLevel` | TField |  | Specifies the application from which the old/previous low advance ratio was considered. |
| 8 | `CMA.NEW.ADJ.MARGIN.LEVEL` | `CoMgnAlert_NewAdjMarginLevel` | TField |  | Specifies the application from which the current low advance ratio has to be considered. |
| 9 | `CMA.OLD.ADJ.MARGIN.ID` | `CoMgnAlert_OldAdjMarginId` | TField |  | ID of the application of old/previous Low advance ratio. |
| 10 | `CMA.NEW.ADJ.MARGIN.ID` | `CoMgnAlert_NewAdjMarginId` | TField |  | ID of the application from which current Low advance ratio has been considered. |
| 11 | `CMA.OLD.ADJ.MGN.RATE` | `CoMgnAlert_OldAdjMgnRate` | TField |  | Specifies the old/previous low advance rate value. Validation Rules: 1. Standard T24 rate field |
| 12 | `CMA.NEW.ADJ.MGN.RATE` | `CoMgnAlert_NewAdjMgnRate` | TField |  | Specifies the current low advance rate value. Validation Rules: 1. Standard T24 rate field |
| 13 | `CMA.OLD.COLL.VALUE` | `CoMgnAlert_OldCollValue` | TField |  | Specifies the old/previous value of the collateral Validation Rules: 1. Standard T24 AMT field |
| 14 | `CMA.NEW.COLL.VALUE` | `CoMgnAlert_NewCollValue` | TField |  | Specifies the current value of the collateral Validation Rules: 1. Standard T24 AMT field |
| 15 | `CMA.DATE.UPDATED` | `CoMgnAlert_DateUpdated` | TField |  | This field holds the date and time which specifies when the record was last modified. |
