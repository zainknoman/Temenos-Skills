# PO.SWEEP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PO.SWEEP.PARAMETER` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PO.SW.SWEEP.CUTTOFF.TIME` | `PoSweepParameter_SweepCuttoffTime` | TField |  |  |
| 2 | `PO.SW.RESERVED11` | `PoSweepParameter_Reserved11` | TField |  |  |
| 3 | `PO.SW.RESERVED10` | `PoSweepParameter_Reserved10` | TField |  |  |
| 4 | `PO.SW.RESERVED09` | `PoSweepParameter_Reserved09` | TField |  |  |
| 5 | `PO.SW.RESERVED08` | `PoSweepParameter_Reserved08` | TField |  |  |
| 6 | `PO.SW.RESERVED07` | `PoSweepParameter_Reserved07` | TField |  |  |
| 7 | `PO.SW.RESERVED06` | `PoSweepParameter_Reserved06` | TField |  |  |
| 8 | `PO.SW.RESERVED05` | `PoSweepParameter_Reserved05` | TField |  |  |
| 9 | `PO.SW.RESERVED04` | `PoSweepParameter_Reserved04` | TField |  |  |
| 10 | `PO.SW.RESERVED03` | `PoSweepParameter_Reserved03` | TField |  |  |
| 11 | `PO.SW.RESERVED02` | `PoSweepParameter_Reserved02` | TField |  |  |
| 12 | `PO.SW.RESERVED01` | `PoSweepParameter_Reserved01` | TField |  |  |
| 13 | `PO.SW.OVERRIDE` | `PoSweepParameter_Override` |  |  |  |
| 14 | `PO.SW.RECORD.STATUS` | `PoSweepParameter_RecordStatus` | String |  |  |
| 15 | `PO.SW.CURR.NO` | `PoSweepParameter_CurrNo` | String |  |  |
| 16 | `PO.SW.INPUTTER` | `PoSweepParameter_Inputter` |  |  |  |
| 17 | `PO.SW.DATE.TIME` | `PoSweepParameter_DateTime` |  |  |  |
| 18 | `PO.SW.AUTHORISER` | `PoSweepParameter_Authoriser` | String |  |  |
| 19 | `PO.SW.CO.CODE` | `PoSweepParameter_CoCode` | String |  |  |
| 20 | `PO.SW.DEPT.CODE` | `PoSweepParameter_DeptCode` | String |  |  |
| 21 | `PO.SW.AUDITOR.CODE` | `PoSweepParameter_AuditorCode` | String |  |  |
| 22 | `PO.SW.AUDIT.DATE.TIME` | `PoSweepParameter_AuditDateTime` | String |  |  |
