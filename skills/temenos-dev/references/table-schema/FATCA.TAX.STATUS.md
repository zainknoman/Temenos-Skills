# FATCA.TAX.STATUS — Table Schema

> Source: `INSERTS/I_F.FATCA.TAX.STATUS` in `FA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FS.DESCRIPTION` | `FatcaTaxStatus_Description` |  |  |  |
| 2 | `FA.FS.VALID.FOR` | `FatcaTaxStatus_ValidFor` |  |  |  |
| 3 | `FA.FS.TAX.STATUS.NO` | `FatcaTaxStatus_TaxStatusNo` | TField |  | This field is to record the status number for the classification, this is used in determining the FATCA.STATUS of the joint portfolio. When a TAX type of CUSTOMER.RELATIONSHIP record is linked to the portfolio (SEC.ACC.MASTER), then a FATCA.CUSTOMER.SUPPLEMENTARY.INFO will be updated for the customer relationship id. PORTFOLIO.STATUS will be the highest level classification of FATCA.STATUS among the joint customers in the customer relationship record. |
| 4 | `FA.FS.PRIORITY.LIST` | `FatcaTaxStatus_PriorityList` |  |  |  |
| 5 | `FA.FS.RESERVED.4` | `FatcaTaxStatus_Reserved4` | TField |  | This field is reserved for future use. |
| 6 | `FA.FS.RESERVED.3` | `FatcaTaxStatus_Reserved3` | TField |  | This field is reserved for future use. |
| 7 | `FA.FS.RESERVED.2` | `FatcaTaxStatus_Reserved2` | TField |  | This field is reserved for future use. |
| 8 | `FA.FS.RESERVED.1` | `FatcaTaxStatus_Reserved1` | TField |  | This field is reserved for future use. |
| 9 | `FA.FS.LOCAL.REF` | `FatcaTaxStatus_LocalRef` |  |  |  |
| 10 | `FA.FS.RECORD.STATUS` | `FatcaTaxStatus_RecordStatus` | String |  |  |
| 11 | `FA.FS.CURR.NO` | `FatcaTaxStatus_CurrNo` | String |  |  |
| 12 | `FA.FS.INPUTTER` | `FatcaTaxStatus_Inputter` |  |  |  |
| 13 | `FA.FS.DATE.TIME` | `FatcaTaxStatus_DateTime` |  |  |  |
| 14 | `FA.FS.AUTHORISER` | `FatcaTaxStatus_Authoriser` | String |  |  |
| 15 | `FA.FS.CO.CODE` | `FatcaTaxStatus_CoCode` | String |  |  |
| 16 | `FA.FS.DEPT.CODE` | `FatcaTaxStatus_DeptCode` | String |  |  |
| 17 | `FA.FS.AUDITOR.CODE` | `FatcaTaxStatus_AuditorCode` | String |  |  |
| 18 | `FA.FS.AUDIT.DATE.TIME` | `FatcaTaxStatus_AuditDateTime` | String |  |  |
| 19 | `FA.FS.WHT.APPLICABLE` | `FatcaTaxStatus_WhtApplicable` | TField |  | Fields denotes the taxability of the fatca status. Allowed values are Yes or No |
| 20 | `FA.FS.CUS.ASSET.THRES.VALUE` | `FatcaTaxStatus_CusAssetThresValue` | TField |  | Value in this field is considered in deciding the taxability of the Fatca status. Allowed values are Above or Below |
| 21 | `FA.FS.IGA.INDICATOR` | `FatcaTaxStatus_IgaIndicator` | TField |  | Value in this field is considered in deciding the taxability of the Fatca status. Allowed values are Available or NotAvailable |
| 22 | `FA.FS.PRE.EXIST.CUSTOMER` | `FatcaTaxStatus_PreExistCustomer` | TField |  | Value in this field is considered in deciding the taxability of the Fatca status. Allowed values are True or False |
