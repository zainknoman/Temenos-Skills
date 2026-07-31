# FATCA.CUSTOMER.SUPPLEMENTARY.INFO — Table Schema

> Source: `INSERTS/I_F.FATCA.CUSTOMER.SUPPLEMENTARY.INFO` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FI.CLIENT.TYPE` | `FatcaCustomerSupplementaryInfo_ClientType` | TField | Yes | The field is used to define the type of customer in terms of FATCA - individual or Legal entity. The due diligence requirements vary based on nature of customer(for e.g. individual/NFFE). The entity accounts can be classified as Legal Entity but if a further granular classification is required, they can be classified as FFI or NFFE. The FFI can have further classifications as NON.REG.LOCAL.BANK,RETIREMENT.FUND,NON.PROFIT.ORG,LOW.VALUE.FFI and OWNER.DOC.FFI. Similarly, the NFFEs can be classified as ACTIVE or PASSIVE NFFEs. Validation rules: This is a mandatory field. Allows any valid record from the table FATCA.CUSTOMER.TYPE. ACTIVE.NFFE FFI INDIVIDUAL LEGAL.ENTITY LOW.VALUE.FFI NFFE NON.PROFIT.ORG NON.REG.LOCAL.BANK OWNER.DOC.FFI PASSIVE.NFFE PRIVATE RETAIL RETIREMENT.FUND TRADED.NFFE US.CORP USFI |
| 2 | `FA.FI.US.PLACE.OF.BIRTH` | `FatcaCustomerSupplementaryInfo_UsPlaceOfBirth` | TField |  | The field is used to record the birth place of the client. Validation rules: Allowed values are Yes, No or any valid country code. Yes - if birth place/incorporation place is US No - if birth place/incorporation place is not US Valid country code - if the birth place is any country other than US |
| 3 | `FA.FI.TAX.DOMICILE` | `FatcaCustomerSupplementaryInfo_TaxDomicile` | TField |  | The field is used to record the tax domicile of the client. Defaulted from the field CUSTOMER>DOMICILE. When DOMICILE is changed in CUSTOMER then this field will be updated with new domicile value during COB. Validation rules: Accepts Valid country code. |
| 4 | `FA.FI.CITIZENSHIP` | `FatcaCustomerSupplementaryInfo_Citizenship` |  |  |  |
| 5 | `FA.FI.GREENCARD` | `FatcaCustomerSupplementaryInfo_Greencard` | TField |  | The field is for recording the Greencard details (ID) of the client and has to be entered if the customer holds a US Greencard. Validation rules Alpha-numeric |
| 6 | `FA.FI.TAX.RESIDENCE` | `FatcaCustomerSupplementaryInfo_TaxResidence` | TField |  | The field is used to record the tax residence of the client (generally based on substantial presence test). Validation rules: 2 type SSS (uppercase alpha) characters The code will be the ID of an existing record in the COUNTRY table. |
| 7 | `FA.FI.ADDR.TYPE` | `FatcaCustomerSupplementaryInfo_AddrType` |  |  |  |
| 8 | `FA.FI.ADDR.COUNTRY` | `FatcaCustomerSupplementaryInfo_AddrCountry` |  |  |  |
| 9 | `FA.FI.POA.HOLDER.COUNTRY` | `FatcaCustomerSupplementaryInfo_PoaHolderCountry` | TField | No | The field is used to specify whether there is any POA (Power of Attorney) to a person with US address Validation rules: Allowed values are Yes or No Optional input |
| 10 | `FA.FI.STND.INSTRUCTION` | `FatcaCustomerSupplementaryInfo_StndInstruction` | TField | No | The field denotes whether there is any standing instruction "to" an account in US. If FCSI is set to create automatically , this field will be updated based on the active standing instructions in the application STANDING.ORDER and Recurring payments in AA. i.e. If the country of beneficiary who receives payment is US , then the payee will be considered to have Standing Instruction Indicia. Validation rules: Allowed values Yes or No. Yes - if the customer has standing instruction "to" an account in US. No/Blank - if the customer has no standing instruction "to" an account in US. Optional input |
| 11 | `FA.FI.ACCT.INSTN.FROM` | `FatcaCustomerSupplementaryInfo_AcctInstnFrom` | TField | No | Field to indicate whether or not the customer's account is likely to receive payments from an account holder with US address. Validation Rules: Allowed values are Yes or No. No system default, to be updated by user if needed. Optional input This field is for information purpose only. |
| 12 | `FA.FI.FORM.OWNER` | `FatcaCustomerSupplementaryInfo_FormOwner` |  |  |  |
| 13 | `FA.FI.FORM.TYPE` | `FatcaCustomerSupplementaryInfo_FormType` |  |  |  |
| 14 | `FA.FI.FORM.ID` | `FatcaCustomerSupplementaryInfo_FormId` |  |  |  |
| 15 | `FA.FI.REQ.DATE` | `FatcaCustomerSupplementaryInfo_ReqDate` |  |  |  |
| 16 | `FA.FI.RECV.DATE` | `FatcaCustomerSupplementaryInfo_RecvDate` |  |  |  |
| 17 | `FA.FI.CUT.OFF.DATE` | `FatcaCustomerSupplementaryInfo_CutOffDate` |  |  |  |
| 18 | `FA.FI.EXP.DATE` | `FatcaCustomerSupplementaryInfo_ExpDate` |  |  |  |
| 19 | `FA.FI.TIN.COUNTRY` | `FatcaCustomerSupplementaryInfo_TinCountry` |  |  |  |
| 20 | `FA.FI.TIN.CODE` | `FatcaCustomerSupplementaryInfo_TinCode` |  |  |  |
| 21 | `FA.FI.SOCIAL.SEC.NO` | `FatcaCustomerSupplementaryInfo_SocialSecNo` | TField |  | The field is used to record the customer's Social Security Number. Validation rules: 1- 35 alphanumeric characters &#160; &#160; |
| 22 | `FA.FI.TELEPHONE.NUMBER` | `FatcaCustomerSupplementaryInfo_TelephoneNumber` | TField | No | The field is used to specify whether the client has any US telephone number. When ST.REGULATORY.PARAMETER>AUTO.CREATE.RECS is set and RT.GET.TELEPHONE.INDICIA API is configured in mapping rule, the fields IDD.PREFIX.PHONE and CONTACT.DATA in CUSTOMER will be referred for US telephone number (provided the CONTACT.TYPE is parameterized in FATCA.PARAMETER>TELE.CONT.TYPE) and if found this field will be set to YES. Validation rules: Allowed values Yes or No. Yes - if the customer has US telephone number. No/Blank - if the customer has no US telephone number. Optional input |
| 23 | `FA.FI.DORMANT.NO.CONTACT` | `FatcaCustomerSupplementaryInfo_DormantNoContact` | TField |  | The field can be set to YES in case no contact could be established with the client. The automatic classification (FATCA STATUS update) of the account as dormant can be specified based on the settings in FATCA PARAMETER for dormant account identification with this value. Validation rules: Allowed values are Yes or No. |
| 24 | `FA.FI.KYC.CHECK` | `FatcaCustomerSupplementaryInfo_KycCheck` | TField |  | Records whether the KYC check has been completed. Validation rules: Allowed values Yes or No |
| 25 | `FA.FI.ENTITY.STATUS` | `FatcaCustomerSupplementaryInfo_EntityStatus` | TField |  | Records the self-classification received from entities. The self-classification will be one of the factors (besides documentation) determining the Account classification (FATCA Status). Validation rules: A valid FATCA TAX STATUS ID can be input in this field. |
| 26 | `FA.FI.EIN` | `FatcaCustomerSupplementaryInfo_Ein` | TField |  | The EIN (Employer identification Number) is a unique nine-digit number assigned by the Internal Revenue Service (IRS). Participating and deemed compliant FFI's will have to register with IRS and obtain an EIN.The EIN can be entered here or in the FORM ID field if EIN is defined as one of the Form Types (document). Validation rules: 1- 35 alphanumeric characters |
| 27 | `FA.FI.STATUS.EXPIRY.DATE` | `FatcaCustomerSupplementaryInfo_StatusExpiryDate` | TField |  | The field denotes the expiry date of the current status in the case of deemed compliant entities. If EIN is included as a document in FORM TYPE field, the expiry date can be specified in the EXP DATE field (part of the FORM OWNER multi-value set) instead of in this field. Validation rules: 1-9 Type D Standard date format -(YYYYMMDD) |
| 28 | `FA.FI.BEN.SUBS.OWNER` | `FatcaCustomerSupplementaryInfo_BenSubsOwner` | TField |  | Records whether the client (entity) has any substantial (for NFFEs) or beneficial owners (for FFI). This field is one of the parameters in calculating POTENTIAL.US field. When this field is not set as NO the entity will be considered as potential US person. Validation rules: Input is allowed only for entity accounts. No auto update. When the field is set as YES and no Beneficial/substantial owner details is updated then error will be raised. When the field is set to NO and Beneficial/substantial owner details is updated then override will be raised. The allowed values are: Yes/Blank - The account has US beneficial or substantial owners. No - The account has no US beneficial or substantial owners. |
| 29 | `FA.FI.ROLE.TYPE` | `FatcaCustomerSupplementaryInfo_RoleType` |  |  |  |
| 30 | `FA.FI.ENT.TAX.CLASS` | `FatcaCustomerSupplementaryInfo_EntTaxClass` |  |  |  |
| 31 | `FA.FI.CUSTOMER.ID` | `FatcaCustomerSupplementaryInfo_CustomerId` |  |  |  |
| 32 | `FA.FI.HOLDER.REF` | `FatcaCustomerSupplementaryInfo_HolderRef` |  |  |  |
| 33 | `FA.FI.HOLDER.NAME` | `FatcaCustomerSupplementaryInfo_HolderName` |  |  |  |
| 34 | `FA.FI.SUR.NAME` | `FatcaCustomerSupplementaryInfo_SurName` |  |  |  |
| 35 | `FA.FI.FIRST.NAME` | `FatcaCustomerSupplementaryInfo_FirstName` |  |  |  |
| 36 | `FA.FI.ALIAS` | `FatcaCustomerSupplementaryInfo_Alias` |  |  |  |
| 37 | `FA.FI.NATIONALITY` | `FatcaCustomerSupplementaryInfo_Nationality` |  |  |  |
| 38 | `FA.FI.RESIDENCE` | `FatcaCustomerSupplementaryInfo_Residence` |  |  |  |
| 39 | `FA.FI.DOMICILE` | `FatcaCustomerSupplementaryInfo_Domicile` |  |  |  |
| 40 | `FA.FI.ADDRESS` | `FatcaCustomerSupplementaryInfo_Address` |  |  |  |
| 41 | `FA.FI.BIRTH.INCO.DATE` | `FatcaCustomerSupplementaryInfo_BirthIncoDate` |  |  |  |
| 42 | `FA.FI.PRCNT.OWNERSHIP` | `FatcaCustomerSupplementaryInfo_PrcntOwnership` |  |  |  |
| 43 | `FA.FI.HOLDER.TIN` | `FatcaCustomerSupplementaryInfo_HolderTin` |  |  |  |
| 44 | `FA.FI.JO.BO.STATUS` | `FatcaCustomerSupplementaryInfo_JoBoStatus` |  |  |  |
| 45 | `FA.FI.HOLD.ADDR.COUNTRY` | `FatcaCustomerSupplementaryInfo_HoldAddrCountry` |  |  |  |
| 46 | `FA.FI.HOLD.TIN.COUNTRY` | `FatcaCustomerSupplementaryInfo_HoldTinCountry` |  |  |  |
| 47 | `FA.FI.LEGAL.ENTITY.TYPE` | `FatcaCustomerSupplementaryInfo_LegalEntityType` |  |  |  |
| 48 | `FA.FI.INDICIA.STRENGTH` | `FatcaCustomerSupplementaryInfo_IndiciaStrength` | TField |  | The system will update the field as STRONG, MEDIUM or WEAK based on the indicia details updated. Validation rules: No input field. System generated values: STRONG MEDIUM WEAK |
| 49 | `FA.FI.POTENTIAL.US` | `FatcaCustomerSupplementaryInfo_PotentialUs` | TField |  | This is a system generated field. The value of this field will be calculated by the system based on the indicia details that have been provided. A value of Yes means that the client is potentially US. Any updates to this field will be cleared once the FATCA STATUS is updated. Validation rules: Allowed value is Yes. |
| 50 | `FA.FI.PROVEN.US` | `FatcaCustomerSupplementaryInfo_ProvenUs` | TField |  | This is a system generated field. The value of this field will be calculated based on the documentation provided. If a client has provided any US document, then this field will be updated as YES. Any updates to this field will be cleared once the FATCA STATUS is updated. Validation rules: Allowed value is Yes. |
| 51 | `FA.FI.PROVEN.NONUS` | `FatcaCustomerSupplementaryInfo_ProvenNonus` | TField |  | This is a system generated field. The value of this field will be calculated based on the documentation provided. If a client has provided any non-US document, then this field will be updated as YES. Any updates to this field will be cleared once the FATCA STATUS is updated. Validation rules Allowed value is Yes. |
| 52 | `FA.FI.FATCA.STATUS` | `FatcaCustomerSupplementaryInfo_FatcaStatus` | TField |  | The field used to specify the FATCA STATUS or Account Classification of the client/entity based on documentation. The FATCA STATUS can be updated either manually or automatically. Even if the status is automatically updated, the same can be changed and the reasons for the change recorded in CHANGE REASON field. Validation rules: A valid FATCA TAX STATUS ID can be input in this field |
| 53 | `FA.FI.STATUS.NARRATIVE` | `FatcaCustomerSupplementaryInfo_StatusNarrative` | TField |  | The field is used to record any free-format narrative relating to the FATCA STATUS (Account classification) updated. If the FATCA STATUS is automatically updated, the Narrative will also be automatically updated. Validation rules: 1-35 ANY characters |
| 54 | `FA.FI.EXCEPTION.LOG` | `FatcaCustomerSupplementaryInfo_ExceptionLog` | TField |  | If FATCA status is set for auto update, this field will be updated with the error conditions if there are situations where FATCA status could not be updated for whatsoever reason. Validation rules: System updated field. No input |
| 55 | `FA.FI.OLD.FATCA.STATUS` | `FatcaCustomerSupplementaryInfo_OldFatcaStatus` | TField |  | This field is updated by system with the old FATCA status value that is being modified. Validation rules: System updated field. NOINPUT |
| 56 | `FA.FI.STATUS.CHANGE.DATE` | `FatcaCustomerSupplementaryInfo_StatusChangeDate` | TField |  | This field holds the date on which the FATCA.STATUS of the customer has been changed by the user manually after providing the status change reason. FATCA.STATUS can be changed to INACTIVE effective from a back date, in which case the system will refer the Aggregate balances record of the inactive customer based on back effective date for reporting purpose. Validation rules: 1-9 Type D Standard date format - (YYYYMMDD). Updated by user If no date is mentioned in this field, the date on which status was changed by the user will be considered for aggregation which will be equal to FA.STATUS.CHG.DATE |
| 57 | `FA.FI.CHANGE.REASON` | `FatcaCustomerSupplementaryInfo_ChangeReason` | TField |  | This field is used to record the reason for any status change. Automatic Status update can be manually overridden by specifying a value in this field. FATCA.STATUS will not be updated by the system until this field is cleared. Validation Rules: 1-35 ANY characters |
| 58 | `FA.FI.CHANGE.PENDING.DOC` | `FatcaCustomerSupplementaryInfo_ChangePendingDoc` | TField |  | The field is updated to indicate that there are pending documents from the Primary customer or Joint customers. It is updated as YES when the documents are pending. The field will be cleared when the documents are received or when the FATCA.STATUS becomes recalcitrant. The pending documents are identified based on the Form REQ.DATE, CUT.OFF.DATE and RECV.DATE fields Field for information purpose. |
| 59 | `FA.FI.GIIN` | `FatcaCustomerSupplementaryInfo_Giin` |  |  |  |
| 60 | `FA.FI.SPONSOR.GIIN` | `FatcaCustomerSupplementaryInfo_SponsorGiin` |  |  |  |
| 61 | `FA.FI.W9.EXEMPT.CODE` | `FatcaCustomerSupplementaryInfo_W9ExemptCode` | TField |  | This field will be input when the primary customer has to be exempted from FATCA reporting. Validation rules: Valid ID from FATCA.W9.EXEMPTION.CODES table |
| 62 | `FA.FI.CR.CUSTOMER.ID` | `FatcaCustomerSupplementaryInfo_CrCustomerId` |  |  |  |
| 63 | `FA.FI.CR.CUST.STATUS` | `FatcaCustomerSupplementaryInfo_CrCustStatus` |  |  |  |
| 64 | `FA.FI.PORTFOLIO.ID` | `FatcaCustomerSupplementaryInfo_PortfolioId` |  |  |  |
| 65 | `FA.FI.PORTFOLIO.STATUS` | `FatcaCustomerSupplementaryInfo_PortfolioStatus` | TField |  | This is the final FATCA.STATUS for the portfolio, the status is arrived based on the TAX.STATUS.NO value from the FATCA.TAX.STATUS record. Portfolio status will be highest level classification among the status of the joint customers. Validation rules: Valid ID from FATCA.TAX.STATUS table System updated field. No input |
| 66 | `FA.FI.FA.STATUS.CHG.DATE` | `FatcaCustomerSupplementaryInfo_FaStatusChgDate` | TField |  | This field holds the date on which the FATCA.STATUS of the customer has been changed by the system. Validation rules: Any valid Date. Standard date format -(YYYYMMDD). System updated field. No input |
| 67 | `FA.FI.INDICIA.SUMMARY` | `FatcaCustomerSupplementaryInfo_IndiciaSummary` |  |  |  |
| 68 | `FA.FI.INDICIA.COUNTRY` | `FatcaCustomerSupplementaryInfo_IndiciaCountry` |  |  |  |
| 69 | `FA.FI.RESERVED.8` | `FatcaCustomerSupplementaryInfo_Reserved8` | TField |  | This field is reserved for future use. |
| 70 | `FA.FI.RESERVED.7` | `FatcaCustomerSupplementaryInfo_Reserved7` | TField |  | This field is reserved for future use. |
| 71 | `FA.FI.RESERVED.6` | `FatcaCustomerSupplementaryInfo_Reserved6` | TField |  | This field is reserved for future use. |
| 72 | `FA.FI.RESERVED.5` | `FatcaCustomerSupplementaryInfo_Reserved5` | TField |  | This field is reserved for future use. |
| 73 | `FA.FI.RESERVED.4` | `FatcaCustomerSupplementaryInfo_Reserved4` | TField |  | This field is reserved for future use. |
| 74 | `FA.FI.RESERVED.3` | `FatcaCustomerSupplementaryInfo_Reserved3` | TField |  | This field is reserved for future use. |
| 75 | `FA.FI.RESERVED.2` | `FatcaCustomerSupplementaryInfo_Reserved2` | TField |  | This field is reserved for future use. |
| 76 | `FA.FI.RESERVED.1` | `FatcaCustomerSupplementaryInfo_Reserved1` | TField |  | This field is reserved for future use. |
| 77 | `FA.FI.LOCAL.REF` | `FatcaCustomerSupplementaryInfo_LocalRef` |  |  |  |
| 78 | `FA.FI.OVERRIDE` | `FatcaCustomerSupplementaryInfo_Override` |  |  |  |
| 79 | `FA.FI.RECORD.STATUS` | `FatcaCustomerSupplementaryInfo_RecordStatus` | String |  |  |
| 80 | `FA.FI.CURR.NO` | `FatcaCustomerSupplementaryInfo_CurrNo` | String |  |  |
| 81 | `FA.FI.INPUTTER` | `FatcaCustomerSupplementaryInfo_Inputter` |  |  |  |
| 82 | `FA.FI.DATE.TIME` | `FatcaCustomerSupplementaryInfo_DateTime` |  |  |  |
| 83 | `FA.FI.AUTHORISER` | `FatcaCustomerSupplementaryInfo_Authoriser` | String |  |  |
| 84 | `FA.FI.CO.CODE` | `FatcaCustomerSupplementaryInfo_CoCode` | String |  |  |
| 85 | `FA.FI.DEPT.CODE` | `FatcaCustomerSupplementaryInfo_DeptCode` | String |  |  |
| 86 | `FA.FI.AUDITOR.CODE` | `FatcaCustomerSupplementaryInfo_AuditorCode` | String |  |  |
| 87 | `FA.FI.AUDIT.DATE.TIME` | `FatcaCustomerSupplementaryInfo_AuditDateTime` | String |  |  |
| 88 | `FA.FI.TIN.NOT.PROVIDED.CODE` | `FatcaCustomerSupplementaryInfo_TinNotProvidedCode` |  |  |  |
| 89 | `FA.FI.TIN.NOT.PROVIDED.REASON` | `FatcaCustomerSupplementaryInfo_TinNotProvidedReason` |  |  |  |
| 90 | `FA.FI.INDICIA.START.DATE` | `FatcaCustomerSupplementaryInfo_IndiciaStartDate` |  |  |  |
| 91 | `FA.FI.INDICIA.DATA.RULE` | `FatcaCustomerSupplementaryInfo_IndiciaDataRule` |  |  |  |
| 92 | `FA.FI.INDICIA.DATA.VALUE` | `FatcaCustomerSupplementaryInfo_IndiciaDataValue` |  |  |  |
