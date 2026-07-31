# SC.PEND.BUY.ORDER — Table Schema

> Source: `INSERTS/I_F.SC.PEND.BUY.ORDER` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PBO.ORDER.REF` | `ScPendBuyOrder_OrderRef` |  |  |  |
| 2 | `SC.PBO.NOMINAL` | `ScPendBuyOrder_Nominal` |  |  |  |
| 3 | `SC.PBO.CASH` | `ScPendBuyOrder_Cash` |  |  |  |
| 4 | `SC.PBO.RESERVED.5` | `ScPendBuyOrder_Reserved5` | TField |  |  |
| 5 | `SC.PBO.RESERVED.4` | `ScPendBuyOrder_Reserved4` | TField |  |  |
| 6 | `SC.PBO.RESERVED.3` | `ScPendBuyOrder_Reserved3` | TField |  |  |
| 7 | `SC.PBO.RESERVED.2` | `ScPendBuyOrder_Reserved2` | TField |  |  |
| 8 | `SC.PBO.RESERVED.1` | `ScPendBuyOrder_Reserved1` | TField |  |  |
