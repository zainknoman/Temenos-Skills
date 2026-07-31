# PAYMENT.ORDER.HIST — Table Schema

> Source: `INSERTS/I_F.PAYMENT.ORDER.HIST` in `PI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PI.POH.PO.HIST.CURR.NO` | `PaymentOrderHist_PoHistCurrNo` |  |  |  |
| 2 | `PI.POH.PO.NOTIFICATION.SEQ` | `PaymentOrderHist_PoNotificationSeq` | TField |  |  |
