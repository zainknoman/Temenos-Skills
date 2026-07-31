# ETFXOP.FXPN.PO.SEQ.NUMBER — Table Schema

> Source: `INSERTS/I_F.ETFXOP.FXPN.PO.SEQ.NUMBER` in `ETFXOP_ForexPermit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.FXPN.ID.CURRENT.SEQ.NO` | `EtfxopFxpnPoSeqNumber_CurrentSeqNo` | TField |  | Currently locked Forex Permit ID |
| 2 | `ETFXOP.FXPN.ID.PO.CURRENT.SEQ.NO` | `EtfxopFxpnPoSeqNumber_PoCurrentSeqNo` | TField |  | Currently Locked Purchase Order ID |
