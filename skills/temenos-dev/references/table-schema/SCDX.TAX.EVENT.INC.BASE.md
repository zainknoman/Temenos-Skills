# SCDX.TAX.EVENT.INC.BASE — Table Schema

> Source: `INSERTS/I_F.SCDX.TAX.EVENT.INC.BASE` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TEI.TRANS.ID` | `ScdxTaxEventIncBase_TransId` |  |  |  |
| 2 | `SC.TEI.SYNTHETIC.CONTRACT` | `ScdxTaxEventIncBase_SyntheticContract` |  |  |  |
| 3 | `SC.TEI.TRANS.DATE` | `ScdxTaxEventIncBase_TransDate` |  |  |  |
| 4 | `SC.TEI.TRANS.QTY` | `ScdxTaxEventIncBase_TrnsQty` |  |  |  |
| 5 | `SC.TEI.TRANS.DELTA` | `ScdxTaxEventIncBase_TransDelta` |  |  |  |
