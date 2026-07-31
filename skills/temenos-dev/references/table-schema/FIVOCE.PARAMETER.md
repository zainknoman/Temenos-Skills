# FIVOCE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FIVOCE.PARAMETER` in `FIVOCE_InvoicingCreditNote.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIVOCE.PAR.PREVIOUS.INVOICE.STATUS` | `FivoceParameter_PreviousInvoiceStatus` | TField |  | Previous invoice status. |
| 2 | `FIVOCE.PAR.CURRENT.INVOICE.STATUS` | `FivoceParameter_CurrentInvoiceStatus` | TField |  | Current invoice status |
| 3 | `FIVOCE.PAR.PREVIOUS.INVOICE.TYPE` | `FivoceParameter_PreviousInvoiceType` | TField |  | Previous invoice type |
| 4 | `FIVOCE.PAR.CURRENT.INVOICE.TYPE` | `FivoceParameter_CurrentInvoiceType` | TField |  | Current invoice type |
| 5 | `FIVOCE.PAR.CURRENT.INVOICE.NO` | `FivoceParameter_CurrentInvoiceNo` |  |  |  |
| 6 | `FIVOCE.PAR.STAGING.APPL.ID` | `FivoceParameter_StagingApplId` |  |  |  |
| 7 | `FIVOCE.PAR.BATCH.NO` | `FivoceParameter_BatchNo` | TField |  | Batch Number |
| 8 | `FIVOCE.PAR.CURRENT.INVOICE.DATE` | `FivoceParameter_CurrentInvoiceDate` | TField |  | Current Invoice Date |
| 9 | `FIVOCE.PAR.ALREADY.MODIFIED` | `FivoceParameter_AlreadyModified` | TField |  | Flag for Already Modified |
| 10 | `FIVOCE.PAR.LOCAL.REF` | `FivoceParameter_LocalRef` |  |  |  |
| 11 | `FIVOCE.PAR.RESERVED.10` | `FivoceParameter_Reserved10` | TField |  |  |
| 12 | `FIVOCE.PAR.RESERVED.9` | `FivoceParameter_Reserved9` | TField |  |  |
| 13 | `FIVOCE.PAR.RESERVED.8` | `FivoceParameter_Reserved8` | TField |  |  |
| 14 | `FIVOCE.PAR.RESERVED.7` | `FivoceParameter_Reserved7` | TField |  |  |
| 15 | `FIVOCE.PAR.RESERVED.6` | `FivoceParameter_Reserved6` | TField |  |  |
| 16 | `FIVOCE.PAR.RESERVED.5` | `FivoceParameter_Reserved5` | TField |  |  |
| 17 | `FIVOCE.PAR.RESERVED.4` | `FivoceParameter_Reserved4` | TField |  |  |
| 18 | `FIVOCE.PAR.RESERVED.3` | `FivoceParameter_Reserved3` | TField |  |  |
| 19 | `FIVOCE.PAR.RESERVED.2` | `FivoceParameter_Reserved2` | TField |  |  |
| 20 | `FIVOCE.PAR.RESERVED.1` | `FivoceParameter_Reserved1` | TField |  |  |
| 21 | `FIVOCE.PAR.OVERRIDE` | `FivoceParameter_Override` |  |  |  |
| 22 | `FIVOCE.PAR.RECORD.STATUS` | `FivoceParameter_RecordStatus` | String |  |  |
| 23 | `FIVOCE.PAR.CURR.NO` | `FivoceParameter_CurrNo` | String |  |  |
| 24 | `FIVOCE.PAR.INPUTTER` | `FivoceParameter_Inputter` |  |  |  |
| 25 | `FIVOCE.PAR.DATE.TIME` | `FivoceParameter_DateTime` |  |  |  |
| 26 | `FIVOCE.PAR.AUTHORISER` | `FivoceParameter_Authoriser` | String |  |  |
| 27 | `FIVOCE.PAR.CO.CODE` | `FivoceParameter_CoCode` | String |  |  |
| 28 | `FIVOCE.PAR.DEPT.CODE` | `FivoceParameter_DeptCode` | String |  |  |
| 29 | `FIVOCE.PAR.AUDITOR.CODE` | `FivoceParameter_AuditorCode` | String |  |  |
| 30 | `FIVOCE.PAR.AUDIT.DATE.TIME` | `FivoceParameter_AuditDateTime` | String |  |  |
