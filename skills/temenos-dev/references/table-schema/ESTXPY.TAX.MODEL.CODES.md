# ESTXPY.TAX.MODEL.CODES — Table Schema

> Source: `INSERTS/I_F.ESTXPY.TAX.MODEL.CODES` in `ESTXPY_SocialSecurityTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.CODES.DESCRIPTION` | `EstxpyTaxModelCodes_Description` | TField |  | The nature of tax for the model code identified in the ID |
| 2 | `TAX.CODES.ISSUER` | `EstxpyTaxModelCodes_Issuer` | TField |  | Holds the Issuer |
| 3 | `TAX.CODES.CODE.TYPE` | `EstxpyTaxModelCodes_CodeType` | TField |  | "The specific tax type to which the model code is applicable. Allowed values are Autoliquidation,Special Autoliquidation,Liquidation,State,Public" |
| 4 | `TAX.CODES.LOCAL.REF` | `EstxpyTaxModelCodes_LocalRef` |  |  |  |
| 5 | `TAX.CODES.ACTIVITY.CODE` | `EstxpyTaxModelCodes_ActivityCode` | TField |  |  |
| 6 | `TAX.CODES.CUST.NAME` | `EstxpyTaxModelCodes_CustName` | TField | Yes | "Indicates if the customer name is mandatory input for this model code or not" |
| 7 | `TAX.CODES.NIF` | `EstxpyTaxModelCodes_Nif` | TField | Yes | "Indicates if the NIF is mandatory input for this model code or not" |
| 8 | `TAX.CODES.PAY.COLL` | `EstxpyTaxModelCodes_PayColl` | TField |  | "Indicates if this is towards payment or collection" |
| 9 | `TAX.CODES.ANAGRAM` | `EstxpyTaxModelCodes_Anagram` | TField |  | "Indicates if Anagram is required as an input for this model code" |
| 10 | `TAX.CODES.TELEMATIC.PAYMENT` | `EstxpyTaxModelCodes_TelematicPayment` | TField |  | "Indicates if this is a telematic payment or not" |
| 11 | `TAX.CODES.EXERCISE` | `EstxpyTaxModelCodes_Exercise` |  |  |  |
| 12 | `TAX.CODES.PERIOD` | `EstxpyTaxModelCodes_Period` |  |  |  |
| 13 | `TAX.CODES.BEGIN.DATE` | `EstxpyTaxModelCodes_BeginDate` |  |  |  |
| 14 | `TAX.CODES.END.DATE` | `EstxpyTaxModelCodes_EndDate` |  |  |  |
| 15 | `TAX.CODES.DOMICILIATION` | `EstxpyTaxModelCodes_Domiciliation` | TField |  | "Indicates if this payment is domiciled at branch. " |
| 16 | `TAX.CODES.LABEL` | `EstxpyTaxModelCodes_Label` | TField |  | "Refers to the label" |
| 17 | `TAX.CODES.PREPOND.VAT` | `EstxpyTaxModelCodes_PrepondVat` | TField |  | "Refers to the Prepond VAT" |
| 18 | `TAX.CODES.RESTRICTION.TYPE` | `EstxpyTaxModelCodes_RestrictionType` | TField |  | "Refers to the Restriction Type" |
| 19 | `TAX.CODES.CONTROLF` | `EstxpyTaxModelCodes_Controlf` | TField |  | "Refers to Controlf" |
| 20 | `TAX.CODES.OVERRIDE` | `EstxpyTaxModelCodes_Override` |  |  |  |
| 21 | `TAX.CODES.RECORD.STATUS` | `EstxpyTaxModelCodes_RecordStatus` | String |  |  |
| 22 | `TAX.CODES.CURR.NO` | `EstxpyTaxModelCodes_CurrNo` | String |  |  |
| 23 | `TAX.CODES.INPUTTER` | `EstxpyTaxModelCodes_Inputter` |  |  |  |
| 24 | `TAX.CODES.DATE.TIME` | `EstxpyTaxModelCodes_DateTime` |  |  |  |
| 25 | `TAX.CODES.AUTHORISER` | `EstxpyTaxModelCodes_Authoriser` | String |  |  |
| 26 | `TAX.CODES.CO.CODE` | `EstxpyTaxModelCodes_CoCode` | String |  |  |
| 27 | `TAX.CODES.DEPT.CODE` | `EstxpyTaxModelCodes_DeptCode` | String |  |  |
| 28 | `TAX.CODES.AUDITOR.CODE` | `EstxpyTaxModelCodes_AuditorCode` | String |  |  |
| 29 | `TAX.CODES.AUDIT.DATE.TIME` | `EstxpyTaxModelCodes_AuditDateTime` | String |  |  |
| 30 | `TAX.CODES.COMPANY.TYPE` | `EstxpyTaxModelCodes_CompanyType` |  |  |  |
| 31 | `TAX.CODES.VOUCHER.PATTERN` | `EstxpyTaxModelCodes_VoucherPattern` | TField |  | "Refers to the Voucher Pattern" |
