# NORSIC.INVOICE.PURPOSE.CODE — Table Schema

> Source: `INSERTS/I_F.NORSIC.INVOICE.PURPOSE.CODE` in `NORSIC_SubsidyInterestCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORLOAN.DESCRIPTION` | `NorsicInvoicePurposeCode_Description` |  |  |  |
| 2 | `NORLOAN.PURPOSE.CODE` | `NorsicInvoicePurposeCode_PurposeCode` | TField |  | It defines the Loan purpose codes for State Treasury. |
| 3 | `NORLOAN.LOCAL.REF` | `NorsicInvoicePurposeCode_LocalRef` |  |  |  |
| 4 | `NORLOAN.OVERRIDE` | `NorsicInvoicePurposeCode_Override` |  |  |  |
| 5 | `NORLOAN.RECORD.STATUS` | `NorsicInvoicePurposeCode_RecordStatus` | String |  |  |
| 6 | `NORLOAN.CURR.NO` | `NorsicInvoicePurposeCode_CurrNo` | String |  |  |
| 7 | `NORLOAN.INPUTTER` | `NorsicInvoicePurposeCode_Inputter` |  |  |  |
| 8 | `NORLOAN.DATE.TIME` | `NorsicInvoicePurposeCode_DateTime` |  |  |  |
| 9 | `NORLOAN.AUTHORISER` | `NorsicInvoicePurposeCode_Authoriser` | String |  |  |
| 10 | `NORLOAN.CO.CODE` | `NorsicInvoicePurposeCode_CoCode` | String |  |  |
| 11 | `NORLOAN.DEPT.CODE` | `NorsicInvoicePurposeCode_DeptCode` | String |  |  |
| 12 | `NORLOAN.AUDITOR.CODE` | `NorsicInvoicePurposeCode_AuditorCode` | String |  |  |
| 13 | `NORLOAN.AUDIT.DATE.TIME` | `NorsicInvoicePurposeCode_AuditDateTime` | String |  |  |
