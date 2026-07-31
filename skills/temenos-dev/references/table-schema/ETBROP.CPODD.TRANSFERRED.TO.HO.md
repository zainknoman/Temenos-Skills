# ETBROP.CPODD.TRANSFERRED.TO.HO — Table Schema

> Source: `INSERTS/I_F.ETBROP.CPODD.TRANSFERRED.TO.HO` in `ETBROP_CashiersPaymentOrderDD.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETBROP.TRANSFER.TRAN.ID` | `EtbropCpoddTransferredToHo_TranId` | TField |  | This field holds the transaction ID of the Payment transferred to HO. |
| 2 | `ETBROP.TRANSFER.TRAN.DATE` | `EtbropCpoddTransferredToHo_TranDate` | TField |  | This field holds the transaction date of the Payment transferred to HO. |
