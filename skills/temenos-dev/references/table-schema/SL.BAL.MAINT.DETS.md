# SL.BAL.MAINT.DETS — Table Schema

> Source: `INSERTS/I_F.SL.BAL.MAINT.DETS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.BAL.MAINT.DETS.ARR.ID` | `SlBalMaintDets_ArrId` | TField |  | This field stores the arrangement ID when a balance maintenance activity/write off activity is performed.Valid Arrangemnet Id record to be updated here. |
| 2 | `SL.BAL.MAINT.DETS.ACT.PRIN.AMT` | `SlBalMaintDets_ActPrinAmt` | TField |  | The purpose of this field is to store the principal portion adjusted usingthe of the balance adjustment/write-off activity.Valid amount is stored here. |
| 3 | `SL.BAL.MAINT.DETS.ACT.INT.AMT` | `SlBalMaintDets_ActIntAmt` | TField |  | This purpose of this field is to store the interest portion adjusted usingthe of the balance adjustment/write-off activity.Valid amount is stored here. |
| 4 | `SL.BAL.MAINT.DETS.ENTRY.POSTED` | `SlBalMaintDets_EntryPosted` | TField |  | The purpose of this field is used to store, whether the accounting entryis posted or not.Allowed values are Yes_NoYes - Entry posted.No - Entry not posted.Validation - This field will be updated, once the balance maintenanceactivities are performed. |
| 5 | `SL.BAL.MAINT.DETS.ACCOUNTING` | `SlBalMaintDets_Accounting` | TField |  | The purpose of this field is used to store whether accounting is requiredor not.Allowed values are Yes_NoYes - Accounting required.No - Accounting not required.Validation - This field will be updated based on theCAMB.H.SL.PARAMETER > ACCOUNTING field. |
