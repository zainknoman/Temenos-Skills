# INLEND.EDPMS.ROD.INVOICE.DETAILS — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.ROD.INVOICE.DETAILS` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.EDPMS.INVOICE.NUMBER` | `InlendEdpmsRodInvoiceDetails_InvoiceNumber` |  |  |  |
| 2 | `INLEND.EDPMS.PENDING.INVOICE.AMOUNT` | `InlendEdpmsRodInvoiceDetails_PendingInvoiceAmount` |  |  |  |
| 3 | `INLEND.EDPMS.RESERVED.5` | `InlendEdpmsRodInvoiceDetails_Reserved5` | TField |  |  |
| 4 | `INLEND.EDPMS.RESERVED.4` | `InlendEdpmsRodInvoiceDetails_Reserved4` | TField |  |  |
| 5 | `INLEND.EDPMS.RESERVED.3` | `InlendEdpmsRodInvoiceDetails_Reserved3` | TField |  |  |
| 6 | `INLEND.EDPMS.RESERVED.2` | `InlendEdpmsRodInvoiceDetails_Reserved2` | TField |  |  |
| 7 | `INLEND.EDPMS.RESERVED.1` | `InlendEdpmsRodInvoiceDetails_Reserved1` | TField |  |  |
