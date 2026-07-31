# ESSCIN.INSURANCE.DATA.FORM — Table Schema

> Source: `INSERTS/I_F.ESSCIN.INSURANCE.DATA.FORM` in `ESSPIN_SocialInsurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.INS.ACTION` | `EsscinInsuranceDataForm_Action` | TField |  | Refers to the action |
| 2 | `ES.INS.MODEL.TYPE` | `EsscinInsuranceDataForm_ModelType` | TField |  | Refers to the insurance type |
| 3 | `ES.INS.CUSTOMER.TYPE` | `EsscinInsuranceDataForm_CustomerType` | TField |  | Refers to customer type (customer or non customer) |
| 4 | `ES.INS.TC.CODE` | `EsscinInsuranceDataForm_TcCode` | TField |  | User Input (Dropdown values)Values stored in ESSSPY.INSURANCE.MODEL.DETAILS table |
| 5 | `ES.INS.MODEL.CODE` | `EsscinInsuranceDataForm_ModelCode` | TField |  | Value retrieved from MODEL.CODE field stored in ESSSPY.INSURANCE.MODEL.DETAILS table based on TC.CODE field input by the user |
| 6 | `ES.INS.MODEL.CODE.DESCRIPTION` | `EsscinInsuranceDataForm_ModelCodeDescription` |  |  |  |
| 7 | `ES.INS.DOCUMENT.TYPE` | `EsscinInsuranceDataForm_DocumentType` | TField |  | This field is to store the Document type |
| 8 | `ES.INS.TYPE` | `EsscinInsuranceDataForm_Type` | TField |  | This field is to store the Insurance Transaction type |
| 9 | `ES.INS.AMOUNT` | `EsscinInsuranceDataForm_Amount` | TField |  | Auto-populated with value from AMOUNT.LOCAL.1 field from TELLER table (for Social Insurance Cash payment) or PAYMENT.AMOUNT field from PAYMENT.ORDER table (for Social Insurance payment via Account Transfer) |
| 10 | `ES.INS.CURRENCY` | `EsscinInsuranceDataForm_Currency` | TField |  | Auto-populated with value from CURRENCY.1 field from TELLER table (for Social Insurance Cash payment) or PAYMENT.CURRENCY field from PAYMENT.ORDER table (for Social Insurance payment via Account Transfer) |
| 11 | `ES.INS.LANGUAGE` | `EsscinInsuranceDataForm_Language` | TField |  | This field is to store the language |
| 12 | `ES.INS.OPERATION.DATE` | `EsscinInsuranceDataForm_OperationDate` | TField |  | This field stores the date of the insurance transaction |
| 13 | `ES.INS.PRESENTATION.DATE` | `EsscinInsuranceDataForm_PresentationDate` | TField |  | This field stores the date of the insurance presentation |
| 14 | `ES.INS.COLLECTION.TYPE` | `EsscinInsuranceDataForm_CollectionType` | TField |  | This field stores type of the insurance collected |
| 15 | `ES.INS.ACCOUNT.NUMBER` | `EsscinInsuranceDataForm_AccountNumber` | TField |  | Auto-populated with value from DEBIT.ACCOUNT field from PAYMENT.ORDER table (for Social Insurance payment via Account Transfer) |
| 16 | `ES.INS.CONTROL.DIGIT` | `EsscinInsuranceDataForm_ControlDigit` | TField |  | This field stores the control digit of the entity number, branch code and Account Number |
| 17 | `ES.INS.REGION.DIGIT` | `EsscinInsuranceDataForm_RegionDigit` | TField |  | This field stores the code of direction provincial |
| 18 | `ES.INS.ISSUER.SUFFIX` | `EsscinInsuranceDataForm_IssuerSuffix` | TField |  | User Input (Dropdown values)Stored in SUFFIX field in ESSSPY.INSURANCE.MODEL.DETAILS table |
| 19 | `ES.INS.ISSUER.NAME` | `EsscinInsuranceDataForm_IssuerName` |  |  |  |
| 20 | `ES.INS.NIB` | `EsscinInsuranceDataForm_Nib` | TField |  | This field is to store the NIB Value |
| 21 | `ES.INS.REFERENCE.NUMBER` | `EsscinInsuranceDataForm_ReferenceNumber` | TField |  | This field is to store the Reference Number |
| 22 | `ES.INS.IDENTIFICATION` | `EsscinInsuranceDataForm_Identification` | TField |  | This field is to store the Identification code |
| 23 | `ES.INS.COMPENSATION` | `EsscinInsuranceDataForm_Compensation` | TField |  | Compensation/Reduction User Input, Amount field |
| 24 | `ES.INS.CONTINGENCIES` | `EsscinInsuranceDataForm_Contingencies` | TField |  | This field is to store any contingencies. User Input, Amount field which can take a negative sign |
| 25 | `ES.INS.AT.EP` | `EsscinInsuranceDataForm_AtEp` | TField |  | This field is to store any At/Ep. User Input, Amount field which can take a negative sign |
| 26 | `ES.INS.OTHER.QUOTATION` | `EsscinInsuranceDataForm_OtherQuotation` | TField |  | This field is to store any other quatation. User Input, Amount field which can take a negative sign |
| 27 | `ES.INS.SURCHARGE` | `EsscinInsuranceDataForm_Surcharge` | TField |  | This field is to store any other Surcharge |
| 28 | `ES.INS.LIQUIDATION.PERIOD.FROM` | `EsscinInsuranceDataForm_LiquidationPeriodFrom` | TField |  | This field is to store start date of liquidation period |
| 29 | `ES.INS.LIQUIDATION.PERIOD.TO` | `EsscinInsuranceDataForm_LiquidationPeriodTo` | TField |  | This field is to store end date of liquidation period |
| 30 | `ES.INS.COMMENTS` | `EsscinInsuranceDataForm_Comments` | TField |  | This field is to stores Comments |
| 31 | `ES.INS.FILE.NUMBER` | `EsscinInsuranceDataForm_FileNumber` | TField |  | This field is to store File Number |
| 32 | `ES.INS.TRANSACTION.REF` | `EsscinInsuranceDataForm_TransactionRef` | TField |  | This field is to store transaction ref |
| 33 | `ES.INS.INTERNAL.ACCOUNT` | `EsscinInsuranceDataForm_InternalAccount` | TField |  | This field is to store internal Account |
| 34 | `ES.INS.SOCIAL.SECURITY.IDENTIFIER` | `EsscinInsuranceDataForm_SocialSecurityIdentifier` | TField |  | This field is to store social security identifier |
| 35 | `ES.INS.LOCAL.REF` | `EsscinInsuranceDataForm_LocalRef` |  |  |  |
| 36 | `ES.INS.CUSTOMER` | `EsscinInsuranceDataForm_Customer` | TField |  |  |
| 37 | `ES.INS.PAYMENT.ID` | `EsscinInsuranceDataForm_PaymentId` | TField |  |  |
| 38 | `ES.INS.PAYMENT.STATUS` | `EsscinInsuranceDataForm_PaymentStatus` |  |  |  |
| 39 | `ES.INS.RESERVED.4` | `EsscinInsuranceDataForm_Reserved4` | TField |  |  |
| 40 | `ES.INS.RESERVED.5` | `EsscinInsuranceDataForm_Reserved5` | TField |  |  |
| 41 | `ES.INS.RESERVED.6` | `EsscinInsuranceDataForm_Reserved6` | TField |  |  |
| 42 | `ES.INS.RESERVED.7` | `EsscinInsuranceDataForm_Reserved7` | TField |  |  |
| 43 | `ES.INS.RESERVED.8` | `EsscinInsuranceDataForm_Reserved8` | TField |  |  |
| 44 | `ES.INS.RESERVED.9` | `EsscinInsuranceDataForm_Reserved9` | TField |  |  |
| 45 | `ES.INS.RESERVED.10` | `EsscinInsuranceDataForm_Reserved10` | TField |  |  |
| 46 | `ES.INS.RESERVED.11` | `EsscinInsuranceDataForm_Reserved11` | TField |  |  |
| 47 | `ES.INS.RESERVED.12` | `EsscinInsuranceDataForm_Reserved12` | TField |  |  |
| 48 | `ES.INS.RESERVED.13` | `EsscinInsuranceDataForm_Reserved13` | TField |  |  |
| 49 | `ES.INS.RESERVED.14` | `EsscinInsuranceDataForm_Reserved14` | TField |  |  |
| 50 | `ES.INS.RESERVED.15` | `EsscinInsuranceDataForm_Reserved15` | TField |  |  |
| 51 | `ES.INS.OVERRIDE` | `EsscinInsuranceDataForm_Override` |  |  |  |
| 52 | `ES.INS.RECORD.STATUS` | `EsscinInsuranceDataForm_RecordStatus` | String |  |  |
| 53 | `ES.INS.CURR.NO` | `EsscinInsuranceDataForm_CurrNo` | String |  |  |
| 54 | `ES.INS.INPUTTER` | `EsscinInsuranceDataForm_Inputter` |  |  |  |
| 55 | `ES.INS.DATE.TIME` | `EsscinInsuranceDataForm_DateTime` |  |  |  |
| 56 | `ES.INS.AUTHORISER` | `EsscinInsuranceDataForm_Authoriser` | String |  |  |
| 57 | `ES.INS.CO.CODE` | `EsscinInsuranceDataForm_CoCode` | String |  |  |
| 58 | `ES.INS.DEPT.CODE` | `EsscinInsuranceDataForm_DeptCode` | String |  |  |
| 59 | `ES.INS.AUDITOR.CODE` | `EsscinInsuranceDataForm_AuditorCode` | String |  |  |
| 60 | `ES.INS.AUDIT.DATE.TIME` | `EsscinInsuranceDataForm_AuditDateTime` | String |  |  |
