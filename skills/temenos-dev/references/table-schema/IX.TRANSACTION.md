# IX.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.IX.TRANSACTION` in `AC_StmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IX.TRAN.DESCRIPTION` | `IxTransaction_Description` |  |  |  |
| 2 | `IX.TRAN.DOMAIN.CODE` | `IxTransaction_DomainCode` | TField | Yes | ISO standard bank transaction Domain code for this particular system id and its transaction code Validation Rules: Must be a valid record in IX.EXTERNAL.CODES with Usage.Code defined as "Domain.Code". Must also be a valid combination as defined in the IX.DOMAIN.CODES Mandatory Input |
| 3 | `IX.TRAN.FAMILY.CODE` | `IxTransaction_FamilyCode` | TField | Yes | ISO standard bank transaction Family code for this particular Domain Code under system id and transaction code. Validation Rules: Must be a valid record in IX.EXTERNAL.CODES with Usage.Code defined as "Family.Code". Must also be a valid combination as defined in the IX.DOMAIN.CODES Must be a valid Family code present under the Domain code. Domain code is mandatory before inputting this field Mandatory Input |
| 4 | `IX.TRAN.SUB.FAMILY.CODE` | `IxTransaction_SubFamilyCode` | TField | Yes | ISO standard bank transaction Sub Family code for this particular system id and its transaction code. Validation Rules: Must be a valid record in IX.EXTERNAL.CODES with Usage.Code defined as "Sub.Family.Code". Must also be a valid combination as defined in the IX.DOMAIN.CODES Must be a valid Sub Family code present under the Family code for that Domain code Domain code and Sub Family Code is mandatory before inputting this field Mandatory Input |
| 5 | `IX.TRAN.LOCAL.REF` | `IxTransaction_LocalRef` |  |  |  |
| 6 | `IX.TRAN.TXN.TYPE` | `IxTransaction_TxnType` | TField |  | Transaction type associated with this System id and its Transaction Code The logic for suppressing and defining values for the tags in XML.TAG.DEFINITION can be defined based on the Transaction type defined in this field For such a setup, the Application id in XML.TAG.DEFINITION should be defined as the System id (Id of this record)*Transaction type(Value defined in this field) |
| 7 | `IX.TRAN.TXN.TYPE.RTN` | `IxTransaction_TxnTypeRtn` | TField |  | API to retrieve the Transaction type for the System id and Transaction Code The System id along with the retrieved Transaction type can be used in XML.TAG.DEFINITION to suppress or define value for tags Validation Rules: i) Must be a valid EB.API ii) Input not allowed if TXN.TYPE is defined For jBC implementations : An EB.API record Id with a source type of BASIC This routine has 4 parameters. StatementEntryRecord - Statement entry record that is being processed. Reserved - Reserved for future use. TransactionType - Out parameter - The transaction type for the statement entry. TransactionTypeError - Out parameter - Error if any returned. For java implementations : An EB.API record Id with a source type of METHOD which implements an interface defined in the EB.API record HOOK.IX.TRANSACTION.TXN.TYPE.RTN. This field supports the Statement.getTransactionType() method. The Statement class is in the com.temenos.t24.api.hook.accounting.Statement package which is in AC_StatementHook.jar shipped with T24. |
| 8 | `IX.TRAN.CAT.APPLICATION` | `IxTransaction_CatApplication` |  |  |  |
| 9 | `IX.TRAN.CAT.LINK.FIELD` | `IxTransaction_CatLinkField` |  |  |  |
| 10 | `IX.TRAN.CAT.LINK.ROUTINE` | `IxTransaction_CatLinkRoutine` |  |  |  |
| 11 | `IX.TRAN.CAT.FIELD.NAME` | `IxTransaction_CatFieldName` |  |  |  |
| 12 | `IX.TRAN.CATEGORY.START` | `IxTransaction_CategoryStart` |  |  |  |
| 13 | `IX.TRAN.CATEGORY.END` | `IxTransaction_CategoryEnd` |  |  |  |
| 14 | `IX.TRAN.CAT.DOMAIN.CODE` | `IxTransaction_CatDomainCode` |  |  |  |
| 15 | `IX.TRAN.CAT.FAMILY.CODE` | `IxTransaction_CatFamilyCode` |  |  |  |
| 16 | `IX.TRAN.OVERRIDE` | `IxTransaction_Override` |  |  |  |
| 17 | `IX.TRAN.RECORD.STATUS` | `IxTransaction_RecordStatus` | String |  |  |
| 18 | `IX.TRAN.CURR.NO` | `IxTransaction_CurrNo` | String |  |  |
| 19 | `IX.TRAN.INPUTTER` | `IxTransaction_Inputter` |  |  |  |
| 20 | `IX.TRAN.DATE.TIME` | `IxTransaction_DateTime` |  |  |  |
| 21 | `IX.TRAN.AUTHORISER` | `IxTransaction_Authoriser` | String |  |  |
| 22 | `IX.TRAN.CO.CODE` | `IxTransaction_CoCode` | String |  |  |
| 23 | `IX.TRAN.DEPT.CODE` | `IxTransaction_DeptCode` | String |  |  |
| 24 | `IX.TRAN.AUDITOR.CODE` | `IxTransaction_AuditorCode` | String |  |  |
| 25 | `IX.TRAN.AUDIT.DATE.TIME` | `IxTransaction_AuditDateTime` | String |  |  |
| 26 | `IX.TRAN.CAT.SUB.FAMILY.CODE` | `IxTransaction_CatSubFamilyCode` |  |  |  |
| 27 | `IX.TRAN.TXN.TYPE.LINK.RTN` | `IxTransaction_TxnTypeLinkRtn` | TField |  | To link a User-defined API to return the ID of another valid IX.TRANSACTION record that contains the bank transaction code to be used in the statement for the accounting movement. The category specific or default bank transaction codes available in the linked IX.TRANSACTION record will be used if the API execution provides a valid IX.TRASNACTION Id. If there is no linked IX.TRANSACTION record available then either the category specific or default bank transaction codes available in the current IX.TRANSACTION record will be used. Validation Rules: i) Must be a valid record in EB.API ii) Input allowed only if the Id of the record is a valid EB.SYSTEM.ID or EB.SYSTEM.ID-RE.TXN.CODE For jBC implementations : An EB.API record Id with a source type of BASIC This routine has 3 parameters. StatementEntryRecord - Statement entry record that is being processed. IxTransactionRecord - IX.TRANSACTION record where TXN.TYPE.LINK.RTN is defined VariantIxTransactionId - Out parameter - The IX.TRANSACTION Id which better categorizes the type of transaction. For java implementations : An EB.API record Id with a source type of METHOD which implements an interface defined in the EB.API record IX.TRANSACTION.TYPE.LINK.RTN.HOOK. This field supports the Statement.getIxTransactionId() method. The Statement class is in the com.temenos.t24.api.hook.accounting.Statement package which is in AC_StatementHook.jar shipped with T24. |
