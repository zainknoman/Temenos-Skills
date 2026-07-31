# ESTXPY.TAX.DATA.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESTXPY.TAX.DATA.DETAILS` in `ESTXPY_SocialSecurityTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.TAX.ADMIN.CODE` | `EstxpyTaxDataDetails_AdminCode` | TField |  | Refers to the administration code |
| 2 | `ES.TAX.DOC.CODE` | `EstxpyTaxDataDetails_DocCode` | TField |  | Refers to the tax model code associated with autoliquidation tax |
| 3 | `ES.TAX.EXERCISE` | `EstxpyTaxDataDetails_Exercise` | TField |  | Refers to the fiscal year denoting YY |
| 4 | `ES.TAX.PERIOD` | `EstxpyTaxDataDetails_Period` | TField |  | Identifies the period of the tax payment |
| 5 | `ES.TAX.IDEN.TYPE` | `EstxpyTaxDataDetails_IdenType` | TField |  | Refers to the customer legal document |
| 6 | `ES.TAX.IDEN.CODE` | `EstxpyTaxDataDetails_IdenCode` | TField |  |  |
| 7 | `ES.TAX.AMOUNT` | `EstxpyTaxDataDetails_Amount` | TField |  | Tax liability or tax refund amount |
| 8 | `ES.TAX.CCY` | `EstxpyTaxDataDetails_Ccy` | TField |  | Currency of the tax amount |
| 9 | `ES.TAX.TELLER.OPS` | `EstxpyTaxDataDetails_TellerOps` | TField |  | indicator if this is a teller operation or not |
| 10 | `ES.TAX.ACCOUNT` | `EstxpyTaxDataDetails_Account` | TField |  | Customer account associated for the tax payment or tax refund |
| 11 | `ES.TAX.INTERNAL.ACCOUNT` | `EstxpyTaxDataDetails_InternalAccount` | TField |  |  |
| 12 | `ES.TAX.DECLARATION` | `EstxpyTaxDataDetails_Declaration` | TField |  | indicates if this is a tax liability or a tax refund. A value of "0" indicates tax payment and a value of "1" indicates tax refund |
| 13 | `ES.TAX.FRACTION.ADD` | `EstxpyTaxDataDetails_FractionAdd` | TField |  | indicates if this is a fraction or domiciliation |
| 14 | `ES.TAX.DUE.DATE` | `EstxpyTaxDataDetails_DueDate` | TField |  | Due date for the tax payment |
| 15 | `ES.TAX.PRESENT.DATE` | `EstxpyTaxDataDetails_PresentDate` | TField |  | Presentation date for the tax payment |
| 16 | `ES.TAX.TOT.AMT.DEP` | `EstxpyTaxDataDetails_TotAmtDep` | TField |  | Refers to the total amount deposited |
| 17 | `ES.TAX.SPEC.DATA` | `EstxpyTaxDataDetails_SpecData` | TField |  | Refers to specific details associated with the tax |
| 18 | `ES.TAX.ENT.BRANCH` | `EstxpyTaxDataDetails_EntBranch` | TField |  | Refers to the entity and the branch code |
| 19 | `ES.TAX.AEAT.DEPT` | `EstxpyTaxDataDetails_AeatDept` | TField |  | Indicates the specific department in AEAT |
| 20 | `ES.TAX.MODEL` | `EstxpyTaxDataDetails_Model` | TField |  | Refers to the tax model code associated with liquidation tax |
| 21 | `ES.TAX.REF.NUM` | `EstxpyTaxDataDetails_RefNum` | TField |  | Identifies the voucher number received for liquidation tax |
| 22 | `ES.TAX.NRC` | `EstxpyTaxDataDetails_Nrc` | TField |  | Refers to the NRC or Challan for the tax payment |
| 23 | `ES.TAX.CUS.TYPE` | `EstxpyTaxDataDetails_CusType` | TField |  |  |
| 24 | `ES.TAX.TAX.MODEL.TYPE` | `EstxpyTaxDataDetails_TaxModelType` | TField |  |  |
| 25 | `ES.TAX.NAME` | `EstxpyTaxDataDetails_Name` | TField |  | First name of the customer |
| 26 | `ES.TAX.SURNAME` | `EstxpyTaxDataDetails_Surname` | TField |  | Surname of the customer |
| 27 | `ES.TAX.CUSTOMER` | `EstxpyTaxDataDetails_Customer` | TField |  |  |
| 28 | `ES.TAX.TRANSACTION.REF` | `EstxpyTaxDataDetails_TransactionRef` | TField |  |  |
| 29 | `ES.TAX.STATUS` | `EstxpyTaxDataDetails_Status` | TField |  | Refers to the Status of the transaction whether it is posted or not |
| 30 | `ES.TAX.LOCAL.REF` | `EstxpyTaxDataDetails_LocalRef` |  |  |  |
| 31 | `ES.TAX.DISCHARGE` | `EstxpyTaxDataDetails_Discharge` | TField |  | Refers to the Discharge value |
| 32 | `ES.TAX.IDENT.FORM` | `EstxpyTaxDataDetails_IdentForm` | TField |  | Refers to the Identification Form |
| 33 | `ES.TAX.AMT.INSTALMENT` | `EstxpyTaxDataDetails_AmtInstalment` | TField |  | Refers to the Installemnt Amount |
| 34 | `ES.TAX.NIF.FIRST` | `EstxpyTaxDataDetails_NifFirst` | TField |  | Refers to the NIF First value |
| 35 | `ES.TAX.NIF.SECOND` | `EstxpyTaxDataDetails_NifSecond` | TField |  | Refers to the NIF Second value |
| 36 | `ES.TAX.OWNERSHIP` | `EstxpyTaxDataDetails_Ownership` | TField |  | Refers to the Ownership value |
| 37 | `ES.TAX.ANAGRAM` | `EstxpyTaxDataDetails_Anagram` | TField |  | Refers to Anagram |
| 38 | `ES.TAX.AEAT.RESPONSE.CODE` | `EstxpyTaxDataDetails_AeatResponseCode` | TField |  | Refers to AEAT Response Code |
| 39 | `ES.TAX.AEAT.RETURN.REASON` | `EstxpyTaxDataDetails_AeatReturnReason` | TField |  | Refers to Aeat Return Reason |
| 40 | `ES.TAX.TRX.STATUS` | `EstxpyTaxDataDetails_TrxStatus` | TField |  | Refers to Transaction Status |
| 41 | `ES.TAX.NIF.PRESENTOR` | `EstxpyTaxDataDetails_NifPresentor` | TField |  | Refers to Nif Presentor |
| 42 | `ES.TAX.OTHER.AMOUNT` | `EstxpyTaxDataDetails_OtherAmount` | TField |  | Refers to Other amount |
| 43 | `ES.TAX.COLLECTION.TYPE` | `EstxpyTaxDataDetails_CollectionType` | TField |  | Refers to collection type |
| 44 | `ES.TAX.AEAT.ONLINE` | `EstxpyTaxDataDetails_AeatOnline` | TField |  | Refers to Aeat Online |
| 45 | `ES.TAX.NIF.FORCED` | `EstxpyTaxDataDetails_NifForced` | TField |  | Identifies the NIF FORCED |
| 46 | `ES.TAX.OVERRIDE` | `EstxpyTaxDataDetails_Override` |  |  |  |
| 47 | `ES.TAX.RECORD.STATUS` | `EstxpyTaxDataDetails_RecordStatus` | String |  |  |
| 48 | `ES.TAX.CURR.NO` | `EstxpyTaxDataDetails_CurrNo` | String |  |  |
| 49 | `ES.TAX.INPUTTER` | `EstxpyTaxDataDetails_Inputter` |  |  |  |
| 50 | `ES.TAX.DATE.TIME` | `EstxpyTaxDataDetails_DateTime` |  |  |  |
| 51 | `ES.TAX.AUTHORISER` | `EstxpyTaxDataDetails_Authoriser` | String |  |  |
| 52 | `ES.TAX.CO.CODE` | `EstxpyTaxDataDetails_CoCode` | String |  |  |
| 53 | `ES.TAX.DEPT.CODE` | `EstxpyTaxDataDetails_DeptCode` | String |  |  |
| 54 | `ES.TAX.AUDITOR.CODE` | `EstxpyTaxDataDetails_AuditorCode` | String |  |  |
| 55 | `ES.TAX.AUDIT.DATE.TIME` | `EstxpyTaxDataDetails_AuditDateTime` | String |  |  |
| 56 | `ES.TAX.FORTNIGHT.NUMBER` | `EstxpyTaxDataDetails_FortnightNumber` | TField |  | Refers to which fortnight tax is present |
| 57 | `ES.TAX.LIQUIDATION.KEY` | `EstxpyTaxDataDetails_LiquidationKey` | TField |  | Refers to Liquidation Key |
| 58 | `ES.TAX.NRC.DATA` | `EstxpyTaxDataDetails_NrcData` | TField |  | Refers to NRC Data |
