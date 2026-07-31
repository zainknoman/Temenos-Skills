# FIVOCE.INVOICE.COUNT — Table Schema

> Source: `INSERTS/I_F.FIVOCE.INVOICE.COUNT` in `FIVOCE_InvoicingCreditNote.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIVOCE.INVCOUNT.INVOICE.COUNT` | `FivoceInvoiceCount_InvoiceCount` | TField |  | This field holds the number of Invoices sent for the Bill Issue Date mentioned in the ID |
| 2 | `FIVOCE.INVCOUNT.CREDIT.NOTE.COUNT` | `FivoceInvoiceCount_CreditNoteCount` | TField |  | This field holds the number of Credit Notes sent for the Bill Issue Date mentioned in the ID |
| 3 | `FIVOCE.INVCOUNT.REMINDER.COUNT` | `FivoceInvoiceCount_ReminderCount` | TField |  | This field holds the number of Reminder Invoices sent for the Bill Issue Date mentioned in the ID |
