# TAXREG.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TAXREG.PARAMETER` in `TAXGST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAXREG.PARAM.INPUT.TAX.CODE` | `TaxregParameter_InputTaxCode` |  |  |  |
| 2 | `TAXREG.PARAM.RECOV.IRRECOV` | `TaxregParameter_RecovIrrecov` |  |  |  |
| 3 | `TAXREG.PARAM.RECOV.IRRECOV.TAX.CODE` | `TaxregParameter_RecovIrrecovTaxCode` |  |  |  |
| 4 | `TAXREG.PARAM.OUTPUT.TAX.CODE` | `TaxregParameter_OutputTaxCode` |  |  |  |
| 5 | `TAXREG.PARAM.GST.CCY` | `TaxregParameter_GstCcy` | TField |  | Used to capture currency in which GST is to be reported to the regulators. Though most of the time this could be local currency of T24 installation, in some cases it is possible that bank can choose a different currency different from local currency. For example, a bank is Singapore may choose USD as local currency instead of SGD. In this scenario, the below field will hold the currency in which reports will be generated for local regulators. |
| 6 | `TAXREG.PARAM.LOCAL.REF` | `TaxregParameter_LocalRef` |  |  |  |
| 7 | `TAXREG.PARAM.INVOICE.FREQUENCY` | `TaxregParameter_InvoiceFrequency` | TField |  |  |
| 8 | `TAXREG.PARAM.CHARGE.VERSION` | `TaxregParameter_ChargeVersion` | TField |  | Holds the value of FT version used for raising VAT entries |
| 9 | `TAXREG.PARAM.REFUND.VERSION` | `TaxregParameter_RefundVersion` | TField |  | Holds the value of FT version used for refunding VAT |
| 10 | `TAXREG.PARAM.PBOC.RATE` | `TaxregParameter_PbocRate` | TField |  | Indicates current multiplicand rate used in tax threshold rate calculation.� System calculates threshold rate when deciding the lending amount subjected to tax. For example, when multiplicand rate is 6% and multiplier is 150, threshold rate calculated is 9%. Only the interest portion exceeding 9% is subjected to tax. |
| 11 | `TAXREG.PARAM.MULTIPLIER.PERCENTAGE` | `TaxregParameter_MultiplierPercentage` |  |  |  |
| 12 | `TAXREG.PARAM.STD.RITC` | `TaxregParameter_StdRitc` | TField |  | The standard RITC rate which is applied when there is no variation at the Investment category level. When this rate is set, the relevant routines are to be attached in the tax tables in order to make this functionality work. |
| 13 | `TAXREG.PARAM.DEBULK.SWEEP` | `TaxregParameter_DebulkSweep` | TField |  | If the De-bulk is set to Yes, for each transaction, separate entries will be raised, else the existing practice of bulking the entries will continue |
| 14 | `TAXREG.PARAM.BRANCH.GSTIN` | `TaxregParameter_BranchGstin` | TField |  | GSTIN of Bank / Branch |
| 15 | `TAXREG.PARAM.SAC.CODE` | `TaxregParameter_SacCode` | TField |  | HSN code for Banking Services as provided by GST authorities |
| 16 | `TAXREG.PARAM.REFUND.PO.VERSION` | `TaxregParameter_RefundPoVersion` | TField |  | Version of PAYMENT.ORDER used for refund transactions |
| 17 | `TAXREG.PARAM.RESERVED.10` | `TaxregParameter_Reserved10` |  |  |  |
| 18 | `TAXREG.PARAM.OVERRIDE` | `TaxregParameter_Override` |  |  |  |
| 19 | `TAXREG.PARAM.RECORD.STATUS` | `TaxregParameter_RecordStatus` | String |  |  |
| 20 | `TAXREG.PARAM.CURR.NO` | `TaxregParameter_CurrNo` | String |  |  |
| 21 | `TAXREG.PARAM.INPUTTER` | `TaxregParameter_Inputter` |  |  |  |
| 22 | `TAXREG.PARAM.DATE.TIME` | `TaxregParameter_DateTime` |  |  |  |
| 23 | `TAXREG.PARAM.AUTHORISER` | `TaxregParameter_Authoriser` | String |  |  |
| 24 | `TAXREG.PARAM.CO.CODE` | `TaxregParameter_CoCode` | String |  |  |
| 25 | `TAXREG.PARAM.DEPT.CODE` | `TaxregParameter_DeptCode` | String |  |  |
| 26 | `TAXREG.PARAM.AUDITOR.CODE` | `TaxregParameter_AuditorCode` | String |  |  |
| 27 | `TAXREG.PARAM.AUDIT.DATE.TIME` | `TaxregParameter_AuditDateTime` | String |  |  |
