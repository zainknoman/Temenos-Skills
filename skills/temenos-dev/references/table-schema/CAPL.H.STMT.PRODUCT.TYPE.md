# CAPL.H.STMT.PRODUCT.TYPE — Table Schema

> Source: `INSERTS/I_F.CAPL.H.STMT.PRODUCT.TYPE` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.STMT.PROD.EXISTING.PRODUCT` | `CaplHStmtProductType_ExistingProduct` | TField |  | The field is used to define the existing product. The value entered must be a valid product parameter id.Valid id of CAPL.H.STMT.PRODUCT.TYPE.This is to reuse the product definition already defined. If this field is entered then no inputs are allowed to the below fields. |
| 2 | `CAPL.STMT.PROD.STATEMENT.SECTION` | `CaplHStmtProductType_StatementSection` | TField |  | Field is used to define the statement section used to define the Banking, Borrowing or Investment. Linked to CAPL.STMT.PROD.STATEMENT.SECTIONValid record from CAPL.ACCT.STMT.SELECTION |
| 3 | `CAPL.STMT.PROD.PRD.DESCRIPTION` | `CaplHStmtProductType_PrdDescription` | TField |  | Field denotes brief description of the product type. This must be parameterized fore.g. "PRODUCT FILE NAME&gt;PRODUCT DESCRIPTION". The T24 account record contains fields like CONDITION.GROUP, and ARRANGEMENT.ID that will be used as the ID to get the product description as defined in this field.E.g. AA.PRODUCT.GROUP&gt;DESCRIPTION |
| 4 | `CAPL.STMT.PROD.PRD.DETAIL.FILE` | `CaplHStmtProductType_PrdDetailFile` | TField |  | This field is used to define the product details file. Each account belonging to a product will be part of the T24 product file from where more detailed information about the product can be acquired. This field must allow the product detail file name to be entered. For e.g. for Term Deposits the product and for Loans the product detail file will be AA.ARRANGEMENT.Valid record from PGM.FILE table.E.g. AA.ARRANGEMENT Modified |
| 5 | `CAPL.STMT.PROD.PRD.DETAIL.FILE.ID` | `CaplHStmtProductType_PrdDetailFileId` | TField |  | This field is to define the product detail file ID.The value entered here must be a valid T24 ACCOUNT field name or @ID.Valid field name or the @id to be defined.For e.g. for Term Deposits the product detail and the product detail file ID is the account number. In this case "@ID" must be entered in this field. For Loans using AA, the field ARRANGEMENT.ID must be used. Modified |
| 6 | `CAPL.STMT.PROD.PRODUCT.DETAILS` | `CaplHStmtProductType_ProductDetails` |  |  |  |
| 7 | `CAPL.STMT.PROD.SOURCE.FIELD` | `CaplHStmtProductType_SourceField` |  |  |  |
| 8 | `CAPL.STMT.PROD.SOURCE.ROUTINE` | `CaplHStmtProductType_SourceRoutine` |  |  |  |
| 9 | `CAPL.STMT.PROD.LOCAL.REF` | `CaplHStmtProductType_LocalRef` |  |  |  |
| 10 | `CAPL.STMT.PROD.STMT.SUM.OR.DET` | `CaplHStmtProductType_StmtSumOrDet` | TField |  | This field is used to define whether the statement should is displayed as summary or detailed statement.Allowed options are Detail/Summary |
| 11 | `CAPL.STMT.PROD.INT.RATE.CHANGE` | `CaplHStmtProductType_IntRateChange` | TField |  | This field indicates whether the interest rate change to be reported in statement or not.Valid inputs are Y/ N/ NoneIf Y the details of interest rate change will be reported.If N the details of interest rate change will not be reported.None implies as N |
| 12 | `CAPL.STMT.PROD.AGENCY.PROD` | `CaplHStmtProductType_AgencyProd` | TField |  | This field is used to define whether the agent prod to be included to statement or not.Allowed options are Y/N |
| 13 | `CAPL.STMT.PROD.STMT.PREF.ADDRESS` | `CaplHStmtProductType_StmtPrefAddress` | TField |  | This field denotes the option to choose the preferred address for sending the statement for respective product.Validation:The drop down based on DE.PRODCUT field CARRIER.ADDR.NOAllowed inputs are None/ Print.1/ Print.2 |
| 14 | `CAPL.STMT.PROD.RESERVED.7` | `CaplHStmtProductType_Reserved7` | TField |  |  |
| 15 | `CAPL.STMT.PROD.RESERVED.6` | `CaplHStmtProductType_Reserved6` | TField |  |  |
| 16 | `CAPL.STMT.PROD.RESERVED.5` | `CaplHStmtProductType_Reserved5` | TField |  |  |
| 17 | `CAPL.STMT.PROD.RESERVED.4` | `CaplHStmtProductType_Reserved4` | TField |  |  |
| 18 | `CAPL.STMT.PROD.RESERVED.3` | `CaplHStmtProductType_Reserved3` | TField |  |  |
| 19 | `CAPL.STMT.PROD.RESERVED.2` | `CaplHStmtProductType_Reserved2` | TField |  |  |
| 20 | `CAPL.STMT.PROD.RESERVED.1` | `CaplHStmtProductType_Reserved1` | TField |  |  |
| 21 | `CAPL.STMT.PROD.OVERRIDE` | `CaplHStmtProductType_Override` |  |  |  |
| 22 | `CAPL.STMT.PROD.RECORD.STATUS` | `CaplHStmtProductType_RecordStatus` | String |  |  |
| 23 | `CAPL.STMT.PROD.CURR.NO` | `CaplHStmtProductType_CurrNo` | String |  |  |
| 24 | `CAPL.STMT.PROD.INPUTTER` | `CaplHStmtProductType_Inputter` |  |  |  |
| 25 | `CAPL.STMT.PROD.DATE.TIME` | `CaplHStmtProductType_DateTime` |  |  |  |
| 26 | `CAPL.STMT.PROD.AUTHORISER` | `CaplHStmtProductType_Authoriser` | String |  |  |
| 27 | `CAPL.STMT.PROD.CO.CODE` | `CaplHStmtProductType_CoCode` | String |  |  |
| 28 | `CAPL.STMT.PROD.DEPT.CODE` | `CaplHStmtProductType_DeptCode` | String |  |  |
| 29 | `CAPL.STMT.PROD.AUDITOR.CODE` | `CaplHStmtProductType_AuditorCode` | String |  |  |
| 30 | `CAPL.STMT.PROD.AUDIT.DATE.TIME` | `CaplHStmtProductType_AuditDateTime` | String |  |  |
