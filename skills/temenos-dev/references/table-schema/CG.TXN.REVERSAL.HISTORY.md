# CG.TXN.REVERSAL.HISTORY — Table Schema

> Source: `INSERTS/I_F.CG.TXN.REVERSAL.HISTORY` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.REV.CG.TXN.BASE.ID` | `CgTxnReversalHistory_CgTxnBaseId` |  |  |  |
| 2 | `CG.REV.SEC.TRANS.ID` | `CgTxnReversalHistory_SecTransId` |  |  |  |
