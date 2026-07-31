# INLEND.SHIPPING.BILL.SEQ — Table Schema

> Source: `INSERTS/I_F.INLEND.SHIPPING.BILL.SEQ` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.SEQ.CUR.SB.SEQUENCE` | `InlendShippingBillSeq_CurSbSequence` | TField |  | This field will contain the current shipping bill sequence. Based on this the next Sb sequence will be generated. |
| 2 | `INLEND.SEQ.LOCAL.REF` | `InlendShippingBillSeq_LocalRef` |  |  |  |
| 3 | `INLEND.SEQ.OVERRIDE` | `InlendShippingBillSeq_Override` |  |  |  |
