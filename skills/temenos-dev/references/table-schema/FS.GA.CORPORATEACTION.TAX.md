# FS.GA.CORPORATEACTION.TAX — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORPORATEACTION.TAX` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORPORATEACTION.TAX.TRANSACTION.CODE` | `FsGaCorporateactionTax_OperationCode` |  |  |  |
| 2 | `CORPORATEACTION.TAX.SEC.ID` | `FsGaCorporateactionTax_SecId` | TField |  | Sec id Multifonds DB Column is NOVAL. |
| 3 | `CORPORATEACTION.TAX.SEQUENCE.NUMBER` | `FsGaCorporateactionTax_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NSEQ. |
| 4 | `CORPORATEACTION.TAX.SUB.SEQUENCE.NUMBER` | `FsGaCorporateactionTax_SubSequenceNumber` | TField |  | Sub Sequence Number Multifonds DB Column is NSUB_SEQ. |
| 5 | `CORPORATEACTION.TAX.TAXES.AND.FEES.CODE` | `FsGaCorporateactionTax_TaxesAndFeesCode` | TField |  | Taxes and fees Code Multifonds DB Column is CODE_COM. |
| 6 | `CORPORATEACTION.TAX.RATE.PERCENTAGE` | `FsGaCorporateactionTax_RatePercentage` | TField |  | Rate Percentage Multifonds DB Column is PC_MNT. |
| 7 | `CORPORATEACTION.TAX.LOCAL.CURRENCY` | `FsGaCorporateactionTax_Currency` |  |  |  |
| 8 | `CORPORATEACTION.TAX.EXTERNAL.REFERENCE` | `FsGaCorporateactionTax_ExternalReference` | TField |  | External Reference Multifonds DB Column is EXT_REF. |
| 9 | `CORPORATEACTION.TAX.RECORD.STATUS` | `FsGaCorporateactionTax_RecordStatus` | String |  |  |
| 10 | `CORPORATEACTION.TAX.CURR.NO` | `FsGaCorporateactionTax_CurrNo` | String |  |  |
| 11 | `CORPORATEACTION.TAX.INPUTTER` | `FsGaCorporateactionTax_Inputter` |  |  |  |
| 12 | `CORPORATEACTION.TAX.DATE.TIME` | `FsGaCorporateactionTax_DateTime` |  |  |  |
| 13 | `CORPORATEACTION.TAX.AUTHORISER` | `FsGaCorporateactionTax_Authoriser` | String |  |  |
| 14 | `CORPORATEACTION.TAX.CO.CODE` | `FsGaCorporateactionTax_CoCode` | String |  |  |
| 15 | `CORPORATEACTION.TAX.DEPT.CODE` | `FsGaCorporateactionTax_DeptCode` | String |  |  |
| 16 | `CORPORATEACTION.TAX.AUDITOR.CODE` | `FsGaCorporateactionTax_AuditorCode` | String |  |  |
| 17 | `CORPORATEACTION.TAX.AUDIT.DATE.TIME` | `FsGaCorporateactionTax_AuditDateTime` | String |  |  |
