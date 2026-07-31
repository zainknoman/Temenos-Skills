# WTXSAI.TAX.ACCR.INT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.WTXSAI.TAX.ACCR.INT.PARAMETER` in `WTXSAI_WithholdingTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WTXSAI.TAX.PAY.ORD.PROD.TYPE` | `WtxsaiTaxAccrIntParameter_PayOrdProdType` | TField |  | @ID of PAYMENT.ORDER.PRODUCT Define payment order product ID here to distinguish this payment is for tax on accrued interest functionality |
| 2 | `WTXSAI.TAX.SECURITY.DOMICILE` | `WtxsaiTaxAccrIntParameter_SecurityDomicile` |  |  |  |
| 3 | `WTXSAI.TAX.INTERNAL.TAX.ACCT.CATEG` | `WtxsaiTaxAccrIntParameter_InternalTaxAcctCateg` |  |  |  |
| 4 | `WTXSAI.TAX.NARRATIVE` | `WtxsaiTaxAccrIntParameter_Narrative` | TField |  | User defined free text field |
| 5 | `WTXSAI.TAX.RESERVED.5` | `WtxsaiTaxAccrIntParameter_Reserved5` | TField |  | Reserved field for future use |
| 6 | `WTXSAI.TAX.RESERVED.4` | `WtxsaiTaxAccrIntParameter_Reserved4` | TField |  | Reserved field for future use |
| 7 | `WTXSAI.TAX.RESERVED.3` | `WtxsaiTaxAccrIntParameter_Reserved3` | TField |  | Reserved field for future use |
| 8 | `WTXSAI.TAX.RESERVED.2` | `WtxsaiTaxAccrIntParameter_Reserved2` | TField |  | Reserved field for future use |
| 9 | `WTXSAI.TAX.RESERVED.1` | `WtxsaiTaxAccrIntParameter_Reserved1` | TField |  | Reserved field for future use |
| 10 | `WTXSAI.TAX.LOCAL.REF` | `WtxsaiTaxAccrIntParameter_LocalRef` |  |  |  |
| 11 | `WTXSAI.TAX.OVERRIDE` | `WtxsaiTaxAccrIntParameter_Override` |  |  |  |
| 12 | `WTXSAI.TAX.RECORD.STATUS` | `WtxsaiTaxAccrIntParameter_RecordStatus` | String |  |  |
| 13 | `WTXSAI.TAX.CURR.NO` | `WtxsaiTaxAccrIntParameter_CurrNo` | String |  |  |
| 14 | `WTXSAI.TAX.INPUTTER` | `WtxsaiTaxAccrIntParameter_Inputter` |  |  |  |
| 15 | `WTXSAI.TAX.DATE.TIME` | `WtxsaiTaxAccrIntParameter_DateTime` |  |  |  |
| 16 | `WTXSAI.TAX.AUTHORISER` | `WtxsaiTaxAccrIntParameter_Authoriser` | String |  |  |
| 17 | `WTXSAI.TAX.CO.CODE` | `WtxsaiTaxAccrIntParameter_CoCode` | String |  |  |
| 18 | `WTXSAI.TAX.DEPT.CODE` | `WtxsaiTaxAccrIntParameter_DeptCode` | String |  |  |
| 19 | `WTXSAI.TAX.AUDITOR.CODE` | `WtxsaiTaxAccrIntParameter_AuditorCode` | String |  |  |
| 20 | `WTXSAI.TAX.AUDIT.DATE.TIME` | `WtxsaiTaxAccrIntParameter_AuditDateTime` | String |  |  |
