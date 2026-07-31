# FIVOCE.INVOICING.MAPPING — Table Schema

> Source: `INSERTS/I_F.FIVOCE.INVOICING.MAPPING` in `FIVOCE_InvoicingCreditNote.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIVOCE.INVMAP.APPLICATION` | `FivoceInvoicingMapping_Application` |  |  |  |
| 2 | `FIVOCE.INVMAP.FIELD` | `FivoceInvoicingMapping_Field` |  |  |  |
| 3 | `FIVOCE.INVMAP.RESERVED.5` | `FivoceInvoicingMapping_Reserved5` | TField |  |  |
| 4 | `FIVOCE.INVMAP.RESERVED.4` | `FivoceInvoicingMapping_Reserved4` | TField |  |  |
| 5 | `FIVOCE.INVMAP.RESERVED.3` | `FivoceInvoicingMapping_Reserved3` | TField |  |  |
| 6 | `FIVOCE.INVMAP.RESERVED.2` | `FivoceInvoicingMapping_Reserved2` | TField |  |  |
| 7 | `FIVOCE.INVMAP.RESERVED.1` | `FivoceInvoicingMapping_Reserved1` | TField |  |  |
| 8 | `FIVOCE.INVMAP.LOCAL.REF` | `FivoceInvoicingMapping_LocalRef` |  |  |  |
| 9 | `FIVOCE.INVMAP.OVERRIDE` | `FivoceInvoicingMapping_Override` |  |  |  |
| 10 | `FIVOCE.INVMAP.RECORD.STATUS` | `FivoceInvoicingMapping_RecordStatus` | String |  |  |
| 11 | `FIVOCE.INVMAP.CURR.NO` | `FivoceInvoicingMapping_CurrNo` | String |  |  |
| 12 | `FIVOCE.INVMAP.INPUTTER` | `FivoceInvoicingMapping_Inputter` |  |  |  |
| 13 | `FIVOCE.INVMAP.DATE.TIME` | `FivoceInvoicingMapping_DateTime` |  |  |  |
| 14 | `FIVOCE.INVMAP.AUTHORISER` | `FivoceInvoicingMapping_Authoriser` | String |  |  |
| 15 | `FIVOCE.INVMAP.CO.CODE` | `FivoceInvoicingMapping_CoCode` | String |  |  |
| 16 | `FIVOCE.INVMAP.DEPT.CODE` | `FivoceInvoicingMapping_DeptCode` | String |  |  |
| 17 | `FIVOCE.INVMAP.AUDITOR.CODE` | `FivoceInvoicingMapping_AuditorCode` | String |  |  |
| 18 | `FIVOCE.INVMAP.AUDIT.DATE.TIME` | `FivoceInvoicingMapping_AuditDateTime` | String |  |  |
