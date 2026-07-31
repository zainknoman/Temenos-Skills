# AA.QUOTATION.OUTPUT — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.OUTPUT` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.QO.QUOTATION.TYPE` | `AaQuotationOutput_QuotationType` | TField |  | Quotation Type that needs to be processed for the arrangement specified in Quotation Class |
| 2 | `AA.QO.VERSION` | `AaQuotationOutput_Version` | TField |  | Version of AA.QUOTATION.TYPE that needs to be used for processing the quotation |
| 3 | `AA.QO.EFFECTIVE.DATE` | `AaQuotationOutput_EffectiveDate` | TField |  | Effective date when the quotation was requested |
| 4 | `AA.QO.NOTES` | `AaQuotationOutput_Notes` |  |  |  |
| 5 | `AA.QO.XML.DATA` | `AaQuotationOutput_XmlData` |  |  |  |
| 6 | `AA.QO.OUTPUT.NAME` | `AaQuotationOutput_OutputName` |  |  |  |
| 7 | `AA.QO.OUTPUT.VALUE` | `AaQuotationOutput_OutputValue` |  |  |  |
| 8 | `AA.QO.ARRANGEMENT` | `AaQuotationOutput_Arrangement` | TField |  |  |
| 9 | `AA.QO.SIM.RUN.REF` | `AaQuotationOutput_SimRunRef` |  |  |  |
| 10 | `AA.QO.SIM.CAP.REF` | `AaQuotationOutput_SimCapRef` |  |  |  |
| 11 | `AA.QO.SIM.STATUS` | `AaQuotationOutput_SimStatus` |  |  |  |
| 12 | `AA.QO.QUOTATION.STATUS` | `AaQuotationOutput_QuotationStatus` | TField |  |  |
