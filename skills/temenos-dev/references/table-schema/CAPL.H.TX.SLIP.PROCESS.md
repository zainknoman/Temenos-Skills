# CAPL.H.TX.SLIP.PROCESS — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.SLIP.PROCESS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TSP.TAX.FORM` | `CaplHTxSlipProcess_TaxForm` | TField |  | This field is used to define the type of tax form applicable for slip generation.Valid record from CAPL.TX.FORM.TYPE table.E.g |
| 2 | `CAPL.TSP.TAX.YEAR` | `CaplHTxSlipProcess_TaxYear` | TField |  | The purpose of this field is used to define the Tax year. For while year the tax slip needs to be generated.E.g 2015, 2016 |
| 3 | `CAPL.TSP.CUSTOMER.NO` | `CaplHTxSlipProcess_CustomerNo` | TField |  | This field is used to define the customer id for which the tax slip to be generated. In case if the slip needs to be generated as per customer.Valid record from CUSTOMER Table |
| 4 | `CAPL.TSP.SEL.CRITERIA` | `CaplHTxSlipProcess_SelCriteria` |  |  |  |
| 5 | `CAPL.TSP.TAX.ACTION` | `CaplHTxSlipProcess_TaxAction` | TField |  | This field is used to choose the tax action for slip generation.Allowed values are.GENERATE/PRINT/DUPLICATE/MODIFY/XML.Valid record fromEB.LOOKUP&gt;TAX.ACTION |
| 6 | `CAPL.TSP.SLIP.ID` | `CaplHTxSlipProcess_SlipId` |  |  |  |
| 7 | `CAPL.TSP.SLIP.PROCESS` | `CaplHTxSlipProcess_SlipProcess` |  |  |  |
| 8 | `CAPL.TSP.TOTAL.SELECTED` | `CaplHTxSlipProcess_TotalSelected` | TField |  | Total slip ids selected. NOINPUT Field |
| 9 | `CAPL.TSP.LOCAL.REF` | `CaplHTxSlipProcess_LocalRef` |  |  |  |
| 10 | `CAPL.TSP.REASON.REPRINT` | `CaplHTxSlipProcess_ReasonReprint` | TField |  | This field is used to define the reason for reprint. When the tax action is reprint, then user have to input the reason for the reprint.Freetext field 50 alphanumeric character. |
| 11 | `CAPL.TSP.RESERVED.9` | `CaplHTxSlipProcess_Reserved9` |  |  |  |
| 12 | `CAPL.TSP.RESERVED.8` | `CaplHTxSlipProcess_Reserved8` |  |  |  |
| 13 | `CAPL.TSP.RESERVED.7` | `CaplHTxSlipProcess_Reserved7` |  |  |  |
| 14 | `CAPL.TSP.RESERVED.6` | `CaplHTxSlipProcess_Reserved6` |  |  |  |
| 15 | `CAPL.TSP.RESERVED.5` | `CaplHTxSlipProcess_Reserved5` |  |  |  |
| 16 | `CAPL.TSP.RESERVED.4` | `CaplHTxSlipProcess_Reserved4` |  |  |  |
| 17 | `CAPL.TSP.RESERVED.3` | `CaplHTxSlipProcess_Reserved3` |  |  |  |
| 18 | `CAPL.TSP.RESERVED.2` | `CaplHTxSlipProcess_Reserved2` |  |  |  |
| 19 | `CAPL.TSP.RESERVED.1` | `CaplHTxSlipProcess_Reserved1` |  |  |  |
| 20 | `CAPL.TSP.OVERRIDE` | `CaplHTxSlipProcess_Override` |  |  |  |
| 21 | `CAPL.TSP.RECORD.STATUS` | `CaplHTxSlipProcess_RecordStatus` | String |  |  |
| 22 | `CAPL.TSP.CURR.NO` | `CaplHTxSlipProcess_CurrNo` | String |  |  |
| 23 | `CAPL.TSP.INPUTTER` | `CaplHTxSlipProcess_Inputter` |  |  |  |
| 24 | `CAPL.TSP.DATE.TIME` | `CaplHTxSlipProcess_DateTime` |  |  |  |
| 25 | `CAPL.TSP.AUTHORISER` | `CaplHTxSlipProcess_Authoriser` | String |  |  |
| 26 | `CAPL.TSP.CO.CODE` | `CaplHTxSlipProcess_CoCode` | String |  |  |
| 27 | `CAPL.TSP.DEPT.CODE` | `CaplHTxSlipProcess_DeptCode` | String |  |  |
| 28 | `CAPL.TSP.AUDITOR.CODE` | `CaplHTxSlipProcess_AuditorCode` | String |  |  |
| 29 | `CAPL.TSP.AUDIT.DATE.TIME` | `CaplHTxSlipProcess_AuditDateTime` | String |  |  |
