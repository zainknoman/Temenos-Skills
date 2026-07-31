# BFW.EVENT.DATA.GROUP.DISP.DETS — Table Schema

> Source: `INSERTS/I_F.BFW.EVENT.DATA.GROUP.DISP.DETS` in `AC_IFConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BFW.DGD.EVENT.DATA.GROUP.ID` | `BfwEventDataGroupDispDets_EventDataGroupId` |  |  |  |
| 2 | `BFW.DGD.EVENT.TYPE` | `BfwEventDataGroupDispDets_EventType` |  |  |  |
| 3 | `BFW.DGD.DISPLAY.DECISION` | `BfwEventDataGroupDispDets_DisplayDecision` |  |  |  |
| 4 | `BFW.DGD.OVERALL.DISPLAY.DECISION` | `BfwEventDataGroupDispDets_OverallDisplayDecision` | TField | Conditional | Specifies whether a Display name is Mandatory or Optional. Even if one of the Data Grouping records associated with the Display name is defined as "Mandatory" then the Display Name becomes "Mandatory" (i.e. this field will be updated as Mandatory). If the Display Decision for all the Data grouping records associated with the Display name are "Optional", then the Display Name becomes "Optional" (i.e. this field will be updated as Optional). |
| 5 | `BFW.DGD.DATA.TYPE` | `BfwEventDataGroupDispDets_DataType` | TField |  | Data type associated with the display name. This is updated based on the data type field in the BFW.EVENT.DATA.GROUPING record. Once this field is updated with a value then all the subsequent BFW.EVENT.DATA.GROUPING record being created with same display name must have the same data type as updated in this field. |
