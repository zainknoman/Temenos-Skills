# NORSIC.INVOICE.INTEREST.CODE — Table Schema

> Source: `INSERTS/I_F.NORSIC.INVOICE.INTEREST.CODE` in `NORSIC_SubsidyInterestCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORINT.DESCRIPTION` | `NorsicInvoiceInterestCode_Description` |  |  |  |
| 2 | `NORINT.LOCAL.REF` | `NorsicInvoiceInterestCode_LocalRef` |  |  |  |
| 3 | `NORINT.OVERRIDE` | `NorsicInvoiceInterestCode_Override` |  |  |  |
| 4 | `NORINT.RECORD.STATUS` | `NorsicInvoiceInterestCode_RecordStatus` | String |  |  |
| 5 | `NORINT.CURR.NO` | `NorsicInvoiceInterestCode_CurrNo` | String |  |  |
| 6 | `NORINT.INPUTTER` | `NorsicInvoiceInterestCode_Inputter` |  |  |  |
| 7 | `NORINT.DATE.TIME` | `NorsicInvoiceInterestCode_DateTime` |  |  |  |
| 8 | `NORINT.AUTHORISER` | `NorsicInvoiceInterestCode_Authoriser` | String |  |  |
| 9 | `NORINT.CO.CODE` | `NorsicInvoiceInterestCode_CoCode` | String |  |  |
| 10 | `NORINT.DEPT.CODE` | `NorsicInvoiceInterestCode_DeptCode` | String |  |  |
| 11 | `NORINT.AUDITOR.CODE` | `NorsicInvoiceInterestCode_AuditorCode` | String |  |  |
| 12 | `NORINT.AUDIT.DATE.TIME` | `NorsicInvoiceInterestCode_AuditDateTime` | String |  |  |
