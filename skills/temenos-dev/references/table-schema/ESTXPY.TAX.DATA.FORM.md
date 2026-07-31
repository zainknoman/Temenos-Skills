# ESTXPY.TAX.DATA.FORM — Table Schema

> Source: `INSERTS/I_F.ESTXPY.TAX.DATA.FORM` in `ESTXPY_SocialSecurityTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.TAX.ADMIN.CODE` | `EstxpyTaxDataForm_AdminCode` | TField |  | Refers to the administration code |
| 2 | `ES.TAX.DOC.CODE` | `EstxpyTaxDataForm_DocCode` | TField |  | Refers to the tax model code associated with autoliquidation tax |
| 3 | `ES.TAX.EXERCISE` | `EstxpyTaxDataForm_Exercise` | TField |  | Refers to the fiscal year denoting YY |
| 4 | `ES.TAX.PERIOD` | `EstxpyTaxDataForm_Period` | TField |  | Identifies the period of the tax payment |
| 5 | `ES.TAX.IDEN.TYPE` | `EstxpyTaxDataForm_IdenType` | TField |  | Refers to the customer legal document |
| 6 | `ES.TAX.IDEN.CODE` | `EstxpyTaxDataForm_IdenCode` | TField |  |  |
| 7 | `ES.TAX.AMOUNT` | `EstxpyTaxDataForm_Amount` | TField |  | Tax liability or tax refund amount |
| 8 | `ES.TAX.CCY` | `EstxpyTaxDataForm_Ccy` | TField |  | Currency of the tax amount |
| 9 | `ES.TAX.TELLER.OPS` | `EstxpyTaxDataForm_TellerOps` | TField |  | indicator if this is a teller operation or not |
| 10 | `ES.TAX.ACCOUNT` | `EstxpyTaxDataForm_Account` | TField |  | Customer account associated for the tax payment or tax refund |
| 11 | `ES.TAX.INTERNAL.ACCOUNT` | `EstxpyTaxDataForm_InternalAccount` | TField |  |  |
| 12 | `ES.TAX.DECLARATION` | `EstxpyTaxDataForm_Declaration` | TField |  | indicates if this is a tax liability or a tax refund. A value of "0" indicates tax payment and a value of "1" indicates tax refund |
| 13 | `ES.TAX.FRACTION.ADD` | `EstxpyTaxDataForm_FractionAdd` | TField |  | indicates if this is a fraction or domiciliation |
| 14 | `ES.TAX.DUE.DATE` | `EstxpyTaxDataForm_DueDate` | TField |  | Due date for the tax payment |
| 15 | `ES.TAX.PRESENT.DATE` | `EstxpyTaxDataForm_PresentDate` | TField |  | Presentation date for the tax payment |
| 16 | `ES.TAX.TOT.AMT.DEP` | `EstxpyTaxDataForm_TotAmtDep` | TField |  | Refers to the total amount deposited |
| 17 | `ES.TAX.SPEC.DATA` | `EstxpyTaxDataForm_SpecData` | TField |  | Refers to specific details associated with the tax |
| 18 | `ES.TAX.ENT.BRANCH` | `EstxpyTaxDataForm_EntBranch` | TField |  | Refers to the entity and the branch code |
| 19 | `ES.TAX.AEAT.DEPT` | `EstxpyTaxDataForm_AeatDept` | TField |  | Indicates the specific department in AEAT |
| 20 | `ES.TAX.MODEL` | `EstxpyTaxDataForm_Model` | TField |  | Refers to the tax model code associated with liquidation tax |
| 21 | `ES.TAX.REF.NUM` | `EstxpyTaxDataForm_RefNum` | TField |  | Identifies the voucher number received for liquidation tax |
| 22 | `ES.TAX.NRC` | `EstxpyTaxDataForm_Nrc` | TField |  | Refers to the NRC or Challan for the tax payment |
| 23 | `ES.TAX.CUS.TYPE` | `EstxpyTaxDataForm_CusType` | TField |  |  |
| 24 | `ES.TAX.TAX.MODEL.TYPE` | `EstxpyTaxDataForm_TaxModelType` | TField |  |  |
| 25 | `ES.TAX.NAME` | `EstxpyTaxDataForm_Name` | TField |  | First name of the customer |
| 26 | `ES.TAX.SURNAME` | `EstxpyTaxDataForm_Surname` | TField |  | Surname of the customer |
| 27 | `ES.TAX.CUSTOMER` | `EstxpyTaxDataForm_Customer` | TField |  |  |
| 28 | `ES.TAX.TRANSACTION.REF` | `EstxpyTaxDataForm_TransactionRef` | TField |  |  |
| 29 | `ES.TAX.LOCAL.REF` | `EstxpyTaxDataForm_LocalRef` |  |  |  |
| 30 | `ES.TAX.DISCHARGE` | `EstxpyTaxDataForm_Discharge` | TField |  | Refers to the Discharge value |
| 31 | `ES.TAX.IDENT.FORM` | `EstxpyTaxDataForm_IdentForm` | TField |  | Refers to the Identification Form |
| 32 | `ES.TAX.AMT.INSTALMENT` | `EstxpyTaxDataForm_AmtInstalment` | TField |  | Refers to the Installemnt Amount |
| 33 | `ES.TAX.NIF.FIRST` | `EstxpyTaxDataForm_NifFirst` | TField |  | Refers to the NIF First value |
| 34 | `ES.TAX.NIF.SECOND` | `EstxpyTaxDataForm_NifSecond` | TField |  | Refers to the NIF Second value |
| 35 | `ES.TAX.OWNERSHIP` | `EstxpyTaxDataForm_Ownership` | TField |  | Refers to the Ownership value |
| 36 | `ES.TAX.ANAGRAM` | `EstxpyTaxDataForm_Anagram` | TField |  | Refers to Anagram |
| 37 | `ES.TAX.AEAT.RESPONSE.CODE` | `EstxpyTaxDataForm_AeatResponseCode` | TField |  | Refers to AEAT Response Code |
| 38 | `ES.TAX.AEAT.RETURN.REASON` | `EstxpyTaxDataForm_AeatReturnReason` | TField |  | Refers to Aeat Return Reason |
| 39 | `ES.TAX.TRX.STATUS` | `EstxpyTaxDataForm_TrxStatus` | TField |  | Refers to Transaction Status |
| 40 | `ES.TAX.NIF.PRESENTOR` | `EstxpyTaxDataForm_NifPresentor` | TField |  | Refers to Nif Presentor |
| 41 | `ES.TAX.OTHER.AMOUNT` | `EstxpyTaxDataForm_OtherAmount` | TField |  | Refers to Other amount |
| 42 | `ES.TAX.COLLECTION.TYPE` | `EstxpyTaxDataForm_CollectionType` | TField |  | Refers to collection type |
| 43 | `ES.TAX.AEAT.ONLINE` | `EstxpyTaxDataForm_AeatOnline` | TField |  | Refers to Aeat Online |
| 44 | `ES.TAX.NIF.FORCED` | `EstxpyTaxDataForm_NifForced` | TField |  | Identifies the NIF forced |
| 45 | `ES.TAX.OVERRIDE` | `EstxpyTaxDataForm_Override` |  |  |  |
| 46 | `ES.TAX.RECORD.STATUS` | `EstxpyTaxDataForm_RecordStatus` | String |  |  |
| 47 | `ES.TAX.CURR.NO` | `EstxpyTaxDataForm_CurrNo` | String |  |  |
| 48 | `ES.TAX.INPUTTER` | `EstxpyTaxDataForm_Inputter` |  |  |  |
| 49 | `ES.TAX.DATE.TIME` | `EstxpyTaxDataForm_DateTime` |  |  |  |
| 50 | `ES.TAX.AUTHORISER` | `EstxpyTaxDataForm_Authoriser` | String |  |  |
| 51 | `ES.TAX.CO.CODE` | `EstxpyTaxDataForm_CoCode` | String |  |  |
| 52 | `ES.TAX.DEPT.CODE` | `EstxpyTaxDataForm_DeptCode` | String |  |  |
| 53 | `ES.TAX.AUDITOR.CODE` | `EstxpyTaxDataForm_AuditorCode` | String |  |  |
| 54 | `ES.TAX.AUDIT.DATE.TIME` | `EstxpyTaxDataForm_AuditDateTime` | String |  |  |
| 55 | `ES.TAX.FORTNIGHT.NUMBER` | `EstxpyTaxDataForm_FortnightNumber` | TField |  | Refers to which fortnight tax is present |
| 56 | `ES.TAX.LIQUIDATION.KEY` | `EstxpyTaxDataForm_LiquidationKey` | TField |  | Refers to Liquidation Key |
| 57 | `ES.TAX.NRC.DATA` | `EstxpyTaxDataForm_NrcData` | TField |  | Refers to NRC Data |
| 58 | `ES.TAX.REVERSAL.REFERENCE` | `EstxpyTaxDataForm_ReversalReference` | TField |  | Refers to Reversal Reference |
| 59 | `ES.TAX.REVERSAL.DATE` | `EstxpyTaxDataForm_ReversalDate` | TField |  | Refers to Reversal Date |
| 60 | `ES.TAX.VALIDATION.SKIP` | `EstxpyTaxDataForm_ValidationSkip` | TField |  | Enabling this will skip template level validations |
