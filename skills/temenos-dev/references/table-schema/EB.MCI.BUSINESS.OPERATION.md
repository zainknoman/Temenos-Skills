# EB.MCI.BUSINESS.OPERATION — Table Schema

> Source: `INSERTS/I_F.EB.MCI.BUSINESS.OPERATION` in `EI_MCI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MCI.BO.DESCRIPTION` | `EbMciBusinessOperation_Description` |  |  |  |
| 2 | `EB.MCI.BO.PRODUCT.LINE` | `EbMciBusinessOperation_ProductLine` |  |  |  |
| 3 | `EB.MCI.BO.PRODUCT.GROUP` | `EbMciBusinessOperation_ProductGroup` |  |  |  |
| 4 | `EB.MCI.BO.PRODUCT` | `EbMciBusinessOperation_Product` |  |  |  |
| 5 | `EB.MCI.BO.ACTIVITY` | `EbMciBusinessOperation_Activity` |  |  |  |
| 6 | `EB.MCI.BO.T24.APPLICATION` | `EbMciBusinessOperation_T24Application` | TField |  | Where the intended Business Operation is a Non-AA T24 Application, is used to specify T24 application which can be used instead of ACTIVITY to perform the business operation for mass change instructions. Input is allowed only either in this field or in the Activity field. |
| 7 | `EB.MCI.BO.REQUIRES.APPROVAL` | `EbMciBusinessOperation_RequiresApproval` | TField |  | This field defines if approval is required or not for the mass change instruction to be executed. A special Override will be raised with details of the Business Operation being performed so as to be able to use special |
| 8 | `EB.MCI.BO.EXECUTION.SIZE` | `EbMciBusinessOperation_ExecutionSize` | TField |  | This field defines the maximum number of Target records that can be performed by a single Mass Change Instruction, for this Business Operation. If in any instance, the number of records happen to be more than this, then the system will force the user to narrow down their Selection criteria further to bring the number of records below this threshold. Value in this field cannot be greater than the value specified in the same field in EB.MCI.PARAMETER. |
| 9 | `EB.MCI.BO.BACK.DATED` | `EbMciBusinessOperation_BackDated` | TField |  | This field defines if the Effective Date of Mass Change instruction can be back valued or not. This is only applicable for an AA Activity. |
| 10 | `EB.MCI.BO.FORWARD.DATED` | `EbMciBusinessOperation_ForwardDated` | TField |  | This field defines if the Effective Date of the Mass Change Instruction can be forward valued or not. This is only applicable for an AA Activity. |
| 11 | `EB.MCI.BO.REVERSAL.ALLOWED` | `EbMciBusinessOperation_ReversalAllowed` | TField |  |  |
| 12 | `EB.MCI.BO.PROPERTY.CLASS` | `EbMciBusinessOperation_PropertyClass` | TField |  |  |
| 13 | `EB.MCI.BO.RESERVED.1` | `EbMciBusinessOperation_Reserved1` | TField |  | This field is reserved for future use. |
| 14 | `EB.MCI.BO.RESERVED.2` | `EbMciBusinessOperation_Reserved2` | TField |  | This field is reserved for future use. |
| 15 | `EB.MCI.BO.RESERVED.3` | `EbMciBusinessOperation_Reserved3` | TField |  | This field is reserved for future use. |
| 16 | `EB.MCI.BO.RESERVED.4` | `EbMciBusinessOperation_Reserved4` | TField |  | This field is reserved for future use. |
| 17 | `EB.MCI.BO.RESERVED.5` | `EbMciBusinessOperation_Reserved5` | TField |  | This field is reserved for future use. |
| 18 | `EB.MCI.BO.LOCAL.REF` | `EbMciBusinessOperation_LocalRef` |  |  |  |
| 19 | `EB.MCI.BO.OVERRIDE` | `EbMciBusinessOperation_Override` |  |  |  |
| 20 | `EB.MCI.BO.RECORD.STATUS` | `EbMciBusinessOperation_RecordStatus` | String |  |  |
| 21 | `EB.MCI.BO.CURR.NO` | `EbMciBusinessOperation_CurrNo` | String |  |  |
| 22 | `EB.MCI.BO.INPUTTER` | `EbMciBusinessOperation_Inputter` |  |  |  |
| 23 | `EB.MCI.BO.DATE.TIME` | `EbMciBusinessOperation_DateTime` |  |  |  |
| 24 | `EB.MCI.BO.AUTHORISER` | `EbMciBusinessOperation_Authoriser` | String |  |  |
| 25 | `EB.MCI.BO.CO.CODE` | `EbMciBusinessOperation_CoCode` | String |  |  |
| 26 | `EB.MCI.BO.DEPT.CODE` | `EbMciBusinessOperation_DeptCode` | String |  |  |
| 27 | `EB.MCI.BO.AUDITOR.CODE` | `EbMciBusinessOperation_AuditorCode` | String |  |  |
| 28 | `EB.MCI.BO.AUDIT.DATE.TIME` | `EbMciBusinessOperation_AuditDateTime` | String |  |  |
