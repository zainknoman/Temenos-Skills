# SL.BAL.MAINT.DETS.HIS — Table Schema

> Source: `INSERTS/I_F.SL.BAL.MAINT.DETS.HIS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.BAL.MAINT.DETS.HIS.ARR.ID` | `SlBalMaintDetsHis_ArrId` | TField |  |  |
| 2 | `SL.BAL.MAINT.DETS.HIS.ACT.PRIN.AMT` | `SlBalMaintDetsHis_ActPrinAmt` | TField |  |  |
| 3 | `SL.BAL.MAINT.DETS.HIS.ACT.INT.AMT` | `SlBalMaintDetsHis_ActIntAmt` | TField |  |  |
| 4 | `SL.BAL.MAINT.DETS.HIS.ENTRY.POSTED` | `SlBalMaintDetsHis_EntryPosted` | TField |  |  |
| 5 | `SL.BAL.MAINT.DETS.HIS.ACCOUNTING` | `SlBalMaintDetsHis_Accounting` | TField |  |  |
