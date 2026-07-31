# PP.FEETYPE — Table Schema

> Source: `INSERTS/I_F.PP.FEETYPE` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FET.ConditionalIndicator` | `PpFeetype_Conditionalindicator` | TField |  | Differentiates if the fee type is conditional or unconditional. Possible values: U - Unconditional C - Conditional |
| 2 | `PP.FET.BeneficiaryChargeAllowed` | `PpFeetype_Beneficiarychargeallowed` | TField |  | Indicates if a beneficiary party can be charged in case of OUR payment. Possible values: "Y" � Yes "N" � No. |
| 3 | `PP.FET.FeeDescription` | `PpFeetype_Feedescription` |  |  |  |
| 4 | `PP.FET.PercentageVATOnCharge` | `PpFeetype_Percentagevatoncharge` |  |  |  |
| 5 | `PP.FET.TaxId` | `PpFeetype_Taxid` |  |  |  |
| 6 | `PP.FET.TaxTypeId` | `PpFeetype_Taxtypeid` |  |  |  |
| 7 | `PP.FET.FeeAPI` | `PpFeetype_Feeapi` | TField | Yes | Holds the API to be used to calculate the fee. Fee returned by the API will be applied as is and system will not check for min charge/max charge/charge rise/charge discount etc. Validation Rules:Valid EB.API record of type 'Basic',if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record FEE.TYPE.FEE.API.HOOK. It is not mandatory to have an API to calculate the fee. If API is not defined, then, system will calculate the fee based on configuration in PP.CLIENTCHARGES/PP.BANKCHARGES. Override to be raised if existing PP.FEETYPE is modified to add a FEE.API. Routine configured should have an entry in EB.API. Specify either A jBC subroutine name The routine has two passed parameters and is expected to get a charge response for the transaction, this can be either calculated charge amount or a boolean value indicating that the system default calculation is to be used. For java implementations: An EB.API record of type METHOD which implements an interface defined in the EB.API record PP.FEETYPE.FeeAPI.HOOK. This field supports the PaymentLifecycle.getChargeResponse() method. The PaymentLifecycle class is in the com.temenos.t24.api.hook.payments package which is in PP_PaymentLifecycleHook.jar shipped with T24. |
| 8 | `PP.FET.DebitChargeBookCode` | `PpFeetype_Debitchargebookcode` | TField |  | Holds the booking code to be used in the debit leg of the accounting entry for the Charge component. This will be used by the posting scheme while posting charge entries when the charges are configured to be collected separately and in detail. The system derives charge transaction codes for payment posting using the below priority: 1. Charge Book Codes from PP.FEETYPE 2. When (1) is blank, the output of the API in Posting Set Configuration 3. When (1) and (2) are blank, the book codes configured for the Posting Set 4. When (1), (2) and (3) are blank, the charge book codes configured for the Product |
| 9 | `PP.FET.CreditChargeBookCode` | `PpFeetype_Creditchargebookcode` | TField |  | Holds the booking code to be used in the credit leg of the accounting entry for the Charge component. This will be used by the posting scheme while posting charge entries when the charges are configured to be collected separately and in detail. The system derives charge transaction codes for payment posting using the below priority: 1. Charge Book Codes from PP.FEETYPE 2. When (1) is blank, the output of the API in Posting Set Configuration 3. When (1) and (2) are blank, the book codes configured for the Posting Set 4. When (1), (2) and (3) are blank, the charge book codes configured for the Product |
| 10 | `PP.FET.LOCAL.REF` | `PpFeetype_LocalRef` |  |  |  |
| 11 | `PP.FET.LinkID` | `PpFeetype_Linkid` | TField |  |  |
| 12 | `PP.FET.OVERRIDE` | `PpFeetype_Override` |  |  |  |
| 13 | `PP.FET.RECORD.STATUS` | `PpFeetype_RecordStatus` | String |  |  |
| 14 | `PP.FET.CURR.NO` | `PpFeetype_CurrNo` | String |  |  |
| 15 | `PP.FET.INPUTTER` | `PpFeetype_Inputter` |  |  |  |
| 16 | `PP.FET.DATE.TIME` | `PpFeetype_DateTime` |  |  |  |
| 17 | `PP.FET.AUTHORISER` | `PpFeetype_Authoriser` | String |  |  |
| 18 | `PP.FET.CO.CODE` | `PpFeetype_CoCode` | String |  |  |
| 19 | `PP.FET.DEPT.CODE` | `PpFeetype_DeptCode` | String |  |  |
| 20 | `PP.FET.AUDITOR.CODE` | `PpFeetype_AuditorCode` | String |  |  |
| 21 | `PP.FET.AUDIT.DATE.TIME` | `PpFeetype_AuditDateTime` | String |  |  |
| 22 | `PP.FET.CompanyID` | `PpFeetype_Companyid` |  |  |  |
| 23 | `PP.FET.DebitVATBookCode` | `PpFeetype_Debitvatbookcode` | TField |  | Holds the booking code to be used in the debit leg of the VAT accounting entry for the applied charge. This will be used by the posting scheme while posting VAT entries for the charge component. The system derives VAT transaction codes for payment posting using the below priority: 1. VAT Book Codes from PP.FEETYPE 2. When (1) is blank, the book codes configured for the Posting Set 3. When (1) and (2) are blank, the VAT book codes configured for the Product |
| 24 | `PP.FET.CreditVATBookCode` | `PpFeetype_Creditvatbookcode` | TField |  | Holds the booking code to be used in the credit leg of the VAT accounting entry for the applied charge. This will be used by the posting scheme while posting VAT entries for the charge component. The system derives VAT transaction codes for payment posting using the below priority: 1. VAT Book Codes from PP.FEETYPE 2. When (1) is blank, the book codes configured for the Posting Set 3. When (1) and (2) are blank, the VAT book codes configured for the Product. |
