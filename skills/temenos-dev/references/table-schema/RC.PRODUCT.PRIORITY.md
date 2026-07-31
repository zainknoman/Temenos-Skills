# RC.PRODUCT.PRIORITY — Table Schema

> Source: `INSERTS/I_F.RC.PRODUCT.PRIORITY` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.PROD.DESCRIPTION` | `RcProductPriority_Description` |  |  |  |
| 2 | `RC.PROD.SYSTEM.ID` | `RcProductPriority_SystemId` | TField | Yes | System Id for which the Priority is defined Validation Rules: Field Input allowed only when the @ID is FreeText. Must be a valid EB.SYSTEM.ID record id. Cannot be entered along with AA.PRODUCT.GROUP Mandatory field when TRANSACTION.SUB.TYPE or TRANSACTION.CODE is entered. |
| 3 | `RC.PROD.TRANSACTION.SUB.TYPE` | `RcProductPriority_TransactionSubType` | TField | No | Subtype of the Transaction for which this product priority is applicable Validation Rules: Optional Field. Field Input allowed only when the @ID is FreeText. When entered only the Transaction with this sub type will follow this priority definition. When left blank all subtype with corresponding SYSTEM.ID takes the same priority. |
| 4 | `RC.PROD.TRANSACTION.CODE` | `RcProductPriority_TransactionCode` | TField | No | Transaction Code for which the product priority is defined Validation Rules: Optional Field. Field Input allowed only when the @ID is FreeText. When entered only the Transaction with this Code will follow this priority definition. When left blank all transactions under the SYSTEM.ID takes the same priority. |
| 5 | `RC.PROD.AA.PRODUCT` | `RcProductPriority_AaProduct` |  |  |  |
| 6 | `RC.PROD.RESERVED.07` | `RcProductPriority_Reserved07` |  |  |  |
| 7 | `RC.PROD.RESERVED.06` | `RcProductPriority_Reserved06` |  |  |  |
| 8 | `RC.PROD.RESERVED.05` | `RcProductPriority_Reserved05` |  |  |  |
| 9 | `RC.PROD.AA.CONTRACT.PRTY` | `RcProductPriority_AaContractPrty` |  |  |  |
| 10 | `RC.PROD.PROD.CAT.START` | `RcProductPriority_ProdCatStart` |  |  |  |
| 11 | `RC.PROD.PROD.CAT.END` | `RcProductPriority_ProdCatEnd` |  |  |  |
| 12 | `RC.PROD.RESERVED.04` | `RcProductPriority_Reserved04` |  |  |  |
| 13 | `RC.PROD.RESERVED.03` | `RcProductPriority_Reserved03` |  |  |  |
| 14 | `RC.PROD.RESERVED.02` | `RcProductPriority_Reserved02` |  |  |  |
| 15 | `RC.PROD.CONTRACT.PRTY` | `RcProductPriority_ContractPrty` |  |  |  |
| 16 | `RC.PROD.LOCAL.REF` | `RcProductPriority_LocalRef` |  |  |  |
| 17 | `RC.PROD.RESERVED.11` | `RcProductPriority_Reserved11` | TField |  |  |
| 18 | `RC.PROD.OVERRIDE` | `RcProductPriority_Override` |  |  |  |
| 19 | `RC.PROD.RECORD.STATUS` | `RcProductPriority_RecordStatus` | String |  |  |
| 20 | `RC.PROD.CURR.NO` | `RcProductPriority_CurrNo` | String |  |  |
| 21 | `RC.PROD.INPUTTER` | `RcProductPriority_Inputter` |  |  |  |
| 22 | `RC.PROD.DATE.TIME` | `RcProductPriority_DateTime` |  |  |  |
| 23 | `RC.PROD.AUTHORISER` | `RcProductPriority_Authoriser` | String |  |  |
| 24 | `RC.PROD.CO.CODE` | `RcProductPriority_CoCode` | String |  |  |
| 25 | `RC.PROD.DEPT.CODE` | `RcProductPriority_DeptCode` | String |  |  |
| 26 | `RC.PROD.AUDITOR.CODE` | `RcProductPriority_AuditorCode` | String |  |  |
| 27 | `RC.PROD.AUDIT.DATE.TIME` | `RcProductPriority_AuditDateTime` | String |  |  |
| 28 | `RC.PROD.AA.PRODUCT.GROUP` | `RcProductPriority_AaProductGroup` | TField | Yes | AA Product Group for which the Priority is defined Validation Rules: Field Input allowed only when the @ID is FreeText. Must be a valid AA.PRODUCT.GROUP record id. Cannot be entered along SYSTEM.ID AA.PRODUCT and AA.CONTRACT.PRTY fields are Mandatory when AA.PRODUCT.GROUP is defined |
| 29 | `RC.PROD.CUSTOM.PRD.GROUP` | `RcProductPriority_CustomPrdGroup` |  |  |  |
| 30 | `RC.PROD.CUSTOM.PRD.SUB.GROUP` | `RcProductPriority_CustomPrdSubGroup` |  |  |  |
| 31 | `RC.PROD.PRIORITY.EXECUTION` | `RcProductPriority_PriorityExecution` | TField | Yes | Field to indicate the Order of Priority Execution Options: PRODUCT.THEN.RANK - The RC Detail records are sorted based on the PRODUCT first and then based on the RANK RANK.THEN.PRODUCT - The RC Detail records are sorted based on the RANK first and then based on the PRODUCT Validation Rules: Field will be made inputtable only for the records with @ID as Free Text and becomes mandatory when CUSTOM.PRD.GROUP is entered Field input not allowed along with the existing SYSTEM.ID/AA.PRODUCT.GROUP definitions |
