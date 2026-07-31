# BENEFICIARY — Table Schema

> Source: `INSERTS/I_F.BENEFICIARY` in `BY_Payments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARC.BEN.NICKNAME` | `Beneficiary_Nickname` |  |  |  |
| 2 | `ARC.BEN.OWNING.CUSTOMER` | `Beneficiary_OwningCustomer` | TField | Yes | It is a mandatory field and used only in customer defined beneficiaries, it contains valid customer id of the customer who creates his own beneficiaries. Value shoule be valid Customer id. |
| 3 | `ARC.BEN.LINK.TO.BENEFICIARY` | `Beneficiary_LinkToBeneficiary` | TField |  | Used in Customer defined beneficiaries , it contains the ID of the bank defined beneficiaries and customer can link it in these field. Value should be valid BENEFICIARY id. |
| 4 | `ARC.BEN.CATEGORY` | `Beneficiary_Category` | TField | Yes | It is mandatory field and used only in bank defined beneficiaries and it is a free Text field. 35 Size - Type Alpha numerical character. |
| 5 | `ARC.BEN.HINT.TEXT` | `Beneficiary_HintText` | TField |  | Used in Bank Defined beneficiary only and it is a free text field will accept upto 255 characters. 255 Size. Type - Alpha numerical character. |
| 6 | `ARC.BEN.CUSTOMER.REF` | `Beneficiary_CustomerRef` | TField | Yes | It is used in Customer beneficiary only. Mapped to Credit their ref field in FT and Ben.Reference in STO. For detail description about this field, refer credit.their.ref in FT or BEN.REFERENCE in STO. Must be swift characters. 35 type Swift characters. (not mandatory) |
| 7 | `ARC.BEN.DEFAULT.NARRATIVE` | `Beneficiary_DefaultNarrative` | TField | Yes | Used in Customer beneficiary only and it contains free text. it is linked to Debit their ref filed in FT and STO. It also mapped to Credit Their Ref if Cust ref field in Beneficiary is null. 35 type Swift characters. (not mandatory) |
| 8 | `ARC.BEN.BENEFICIARY.RISK` | `Beneficiary_BeneficiaryRisk` | TField |  | Contains a single numeric character 1-9 used by the Protection Limits application. Can be used in customer or bank-defined beneficiaries. Bank-defined value takes precedence. Size - 1. Numerical character |
| 9 | `ARC.BEN.BEN.ACCT.NO` | `Beneficiary_BenAcctNo` | TField | Conditional | It is a mandatory field for AC and BC type transaction and it is linked to BEN.ACCT.NO field in FT and CPTY ACCT No. field in STO for AC type transaction. And it is an optional field in case of OT, OD transaction type and it is linked to Ben Acct no. field in FT and STO for OT, OD and BC types of transactions. Mandatory field for AC and BC transaction type. |
| 10 | `ARC.BEN.ACCOUNT.NAME` | `Beneficiary_AccountName` | TField |  | Reserved for future use |
| 11 | `ARC.BEN.BEN.CUSTOMER` | `Beneficiary_BenCustomer` | TField | Yes | It is a mandatory field for OT, BC and OD transaction types in beneficiary table and it is linked to BEN.CUSTOMER field in FT and STO. For detail description about this field, refer the help text of BEN.CUSTOMER in FT or STO. Value can be either free text value or valid customer id. Maximum value of sizw 35 will be allowed. |
| 12 | `ARC.BEN.ACCT.WITH.BANK` | `Beneficiary_AcctWithBank` | TField |  | This field is widely used for OT transactions and it accepts valid swift code and it is linked to the ACCT WITH BANK field in FT and STO. For the detail description about this field, refer the help text of same field in FT or STO. Value can be free text, Valid customer id, Valid swift code. Maximum value of sizw 35 will be allowed. |
| 13 | `ARC.BEN.AC.WITH.BK.SHORT.NAME` | `Beneficiary_AcWithBkShortName` |  |  |  |
| 14 | `ARC.BEN.BK.NAME.1` | `Beneficiary_BkName1` |  |  |  |
| 15 | `ARC.BEN.BK.NAME.2` | `Beneficiary_BkName2` |  |  |  |
| 16 | `ARC.BEN.BK.STREET.ADDR` | `Beneficiary_BkStreetAddr` |  |  |  |
| 17 | `ARC.BEN.BK.TOWN.COUNTRY` | `Beneficiary_BkTownCountry` |  |  |  |
| 18 | `ARC.BEN.BK.POST.CODE` | `Beneficiary_BkPostCode` |  |  |  |
| 19 | `ARC.BEN.BK.COUNTRY` | `Beneficiary_BkCountry` |  |  |  |
| 20 | `ARC.BEN.BANK.SORT.CODE` | `Beneficiary_BankSortCode` | TField | Yes | It is a mandatory field for BC type of transaction and it accepts valid Sort code defined in SIC Sort Code and it is linked to BC.BANK.SORT.CODE.field in FT and STO. For detail desciption about this field, refer the help text of same field in FT or STO. Value should have the valid BC.SORT.CODE id |
| 21 | `ARC.BEN.TRANSACTION.TYPE` | `Beneficiary_TransactionType` | TField | Yes | it is mandatory field and Maps to same field in FT and Pay Method in STO. For detail description, refer the help text of same field in FT and helptext of Pay menthod in STO. Value must be valid FT.TXN.TYPE.CONDITION id. |
| 22 | `ARC.BEN.BIC` | `Beneficiary_Bic` | TField |  | Input in this field will be allowed only for Transaction type OT and it maps to receiver bank of FT. Value should have the valid DE.BIC id. |
| 23 | `ARC.BEN.BEN.SHORT.NAME` | `Beneficiary_BenShortName` |  |  |  |
| 24 | `ARC.BEN.NAME.1` | `Beneficiary_Name1` |  |  |  |
| 25 | `ARC.BEN.NAME.2` | `Beneficiary_Name2` |  |  |  |
| 26 | `ARC.BEN.STREET.ADDR` | `Beneficiary_StreetAddr` |  |  |  |
| 27 | `ARC.BEN.TOWN.COUNTRY` | `Beneficiary_TownCountry` |  |  |  |
| 28 | `ARC.BEN.POST.CODE` | `Beneficiary_PostCode` |  |  |  |
| 29 | `ARC.BEN.COUNTRY` | `Beneficiary_Country` |  |  |  |
| 30 | `ARC.BEN.PAYMENT.DETAILS` | `Beneficiary_PaymentDetails` |  |  |  |
| 31 | `ARC.BEN.IBAN.BEN` | `Beneficiary_IbanBen` | TField |  | Holds IBAN of the BEN.ACCT.NO If value is entered, it will be validated against IN.IBAN.STRUCTURE file, else an equivalent IBAN will be retrieved from a beneficiary account record with alternate account type set as "T24.IBAN" |
| 32 | `ARC.BEN.BIC.IBAN.BEN` | `Beneficiary_BicIbanBen` | TField |  | When a valid IBAN number is input in the field IBAN.BEN, BIC code of the IBAN number will be derived based on IN.IBAN.PLUS table and updated in this field, when system does not find the BIC code then this field will be open for user input. System updated BIC code or any valid DE.BIC record id. |
| 33 | `ARC.BEN.BIC.IBAN.BEN.NAME` | `Beneficiary_BicIbanBenName` |  |  |  |
| 34 | `ARC.BEN.BIC.IBAN.BEN.CITY` | `Beneficiary_BicIbanBenCity` | TField |  | Stores the city of the bank (BIC code). This is derived from field CITY of DE.BIC record when a valid BIC.IBAN.BEN is given; otherwise it is allowed for user input. If the BIC id is valid but a record is not found in DE.BIC table, COUNTRY value from the IN.IBAN.PLUS table corresponding to the BIC code will be populated System updated BIC bank city or any valid city name. |
| 35 | `ARC.BEN.BEN.PYMT.COUNTRY` | `Beneficiary_BenPymtCountry` | TField |  | The payment country to be populated when the Beneficiary will be used |
| 36 | `ARC.BEN.PAYMENT.CCY` | `Beneficiary_PaymentCcy` | TField |  | The payment currency to be populated when the Beneficiary will be used |
| 37 | `ARC.BEN.PREF.PYMT.AMOUNT` | `Beneficiary_PrefPymtAmount` | TField |  | The payment amount to be populated in the FT or Payment Order when the Beneficiary will be used |
| 38 | `ARC.BEN.CLEARING.TYPE` | `Beneficiary_ClearingType` | TField |  | The clearing type to be populated in FT or Payment Order when the Beneficiary will be used |
| 39 | `ARC.BEN.BC.SORT.CODE` | `Beneficiary_BcSortCode` | TField |  | The sort code to be populated when the Beneficiary will be used |
| 40 | `ARC.BEN.BEN.OUR.CHARGES` | `Beneficiary_BenOurCharges` | TField |  | The charges bearer option to be populated when the Beneficiary will be used |
| 41 | `ARC.BEN.ACCT.WITH.BK.SORT.CODE` | `Beneficiary_AcctWithBkSortCode` | TField |  | Sort code of Account with Bank. Field introduced to facilitate the Payment Order for Beneficiary trasfers. The value maintained in this field will be defaulted to the "Account with Bank clearing code" in the Payment Order application. |
| 42 | `ARC.BEN.ACCT.WITH.BANK.IBAN` | `Beneficiary_AcctWithBankIban` | TField |  | IBAN of Account with Bank. Field introduced to facilitate the Payment Order for Beneficiary trasfers. The value maintained in this field will be defaulted to the "Account with Bank IBAN" in the Payment Order application. |
| 43 | `ARC.BEN.PREF.PYMT.PRODUCT` | `Beneficiary_PrefPymtProduct` | TField |  | Valid record in PAYMENT.ORDER.PRODUCT which allows Payment through Beneficiary i.e. PAY.THROUGH.BENEFICIARY set as YES.Product for which the Beneficiary will be preferably used in Payment order.Will get defaulted in PAYMENT.ORDER.PRODUCT field of Payment order if not defined |
| 44 | `ARC.BEN.ULTIMATE.CRED.NAME` | `Beneficiary_UltimateCredName` | TField |  | Name of the Ultimate creditor of payment. |
| 45 | `ARC.BEN.ULTIMATE.CRED.ADDR.TYPE` | `Beneficiary_UltimateCredAddrType` | TField |  | Address type to be used for the Ultimate creditor of payment. |
| 46 | `ARC.BEN.ULTIMATE.CRED.ADDR.LINE` | `Beneficiary_UltimateCredAddrLine` |  |  |  |
| 47 | `ARC.BEN.ULTIMATE.CRED.BIC` | `Beneficiary_UltimateCredBic` | TField |  | BIC code of Ultimate creditor of payment. |
| 48 | `ARC.BEN.ULTIMATE.CRED.COUNTRY` | `Beneficiary_UltimateCredCountry` | TField |  | Country of Ultimate creditor of payment. |
| 49 | `ARC.BEN.REQUESTED.CCY` | `Beneficiary_RequestedCcy` | TField |  | This would indicate the currency in which funds should be deducted from the account stored as part of the beneficiary record. This will be defaulted to payment currency in payment order record when ordering customer SSI holds a valid record from beneficiary application. Value must be a valid record from CURRENCY table |
| 50 | `ARC.BEN.BEN.ACCT.LOCATION` | `Beneficiary_BenAcctLocation` | TField | Yes | Location of the Beneficiary account/Beneficiary IBAN based on which core will trigger or not a validation at theaccount closure identified in the Beneficiary . Non mandatory option field Options are 'OWN' or Blank OWN will indicate the Beneficiary Account/IBAN is within T24; this will determine Core to update the AC.BLOCK.CLOSURE file Blank or any other value from Core perspective the location is not determined and the AC.BLOCK.CLOSURE will not be updated |
| 51 | `ARC.BEN.PAYMENT.CATEGORY` | `Beneficiary_PaymentCategory` | TField |  |  |
| 52 | `ARC.BEN.PAYMENT.PURPOSE` | `Beneficiary_PaymentPurpose` | TField |  | Underlying reason for the payment transaction. Purpose is used to provide information concerning the nature of the payment These details are for the end customer and in general they are not used for processing by any of the agents involved in the payment chain Should be a valid record in the table PAYMENT.PURPOSE.CODE |
| 53 | `ARC.BEN.ULTIMATE.CRED.OT.ID.TYPE` | `Beneficiary_UltimateCredOtIdType` |  |  |  |
| 54 | `ARC.BEN.ULTIMATE.CRED.OT.ID` | `Beneficiary_UltimateCredOtId` |  |  |  |
| 55 | `ARC.BEN.ULTIMATE.CRED.DOB` | `Beneficiary_UltimateCredDob` |  |  |  |
| 56 | `ARC.BEN.ULTIMATE.CRED.BR.PRVNC` | `Beneficiary_UltimateCredBrPrvnc` |  |  |  |
| 57 | `ARC.BEN.ULTIMATE.CRED.BR.CITY` | `Beneficiary_UltimateCredBrCity` |  |  |  |
| 58 | `ARC.BEN.ULTIMATE.CRED.BR.COUNTRY` | `Beneficiary_UltimateCredBrCountry` |  |  |  |
| 59 | `ARC.BEN.ULTIMATE.CRED.SCHME.CDE` | `Beneficiary_UltimateCredSchmeCde` |  |  |  |
| 60 | `ARC.BEN.ULTIMATE.CRED.SCH.PRTY` | `Beneficiary_UltimateCredSchPrty` |  |  |  |
| 61 | `ARC.BEN.ULTIMATE.CRED.SCH.ISSUR` | `Beneficiary_UltimateCredSchIssur` |  |  |  |
| 62 | `ARC.BEN.BENEFICIARY.OT.ID.TYPE` | `Beneficiary_BeneficiaryOtIdType` |  |  |  |
| 63 | `ARC.BEN.BENEFICIARY.OT.ID` | `Beneficiary_BeneficiaryOtId` |  |  |  |
| 64 | `ARC.BEN.LOCAL.REF` | `Beneficiary_LocalRef` |  |  |  |
| 65 | `ARC.BEN.OVERRIDE` | `Beneficiary_Override` |  |  |  |
| 66 | `ARC.BEN.RECORD.STATUS` | `Beneficiary_RecordStatus` | String |  |  |
| 67 | `ARC.BEN.CURR.NO` | `Beneficiary_CurrNo` | String |  |  |
| 68 | `ARC.BEN.INPUTTER` | `Beneficiary_Inputter` |  |  |  |
| 69 | `ARC.BEN.DATE.TIME` | `Beneficiary_DateTime` |  |  |  |
| 70 | `ARC.BEN.AUTHORISER` | `Beneficiary_Authoriser` | String |  |  |
| 71 | `ARC.BEN.CO.CODE` | `Beneficiary_CoCode` | String |  |  |
| 72 | `ARC.BEN.DEPT.CODE` | `Beneficiary_DeptCode` | String |  |  |
| 73 | `ARC.BEN.AUDITOR.CODE` | `Beneficiary_AuditorCode` | String |  |  |
| 74 | `ARC.BEN.AUDIT.DATE.TIME` | `Beneficiary_AuditDateTime` | String |  |  |
| 75 | `ARC.BEN.BENEFICIARY.DOB` | `Beneficiary_BeneficiaryDob` |  |  |  |
| 76 | `ARC.BEN.BENEFICIARY.BR.PRVNC` | `Beneficiary_BeneficiaryBrPrvnc` |  |  |  |
| 77 | `ARC.BEN.BENEFICIARY.BR.CITY` | `Beneficiary_BeneficiaryBrCity` |  |  |  |
| 78 | `ARC.BEN.BENEFICIARY.BR.COUNTRY` | `Beneficiary_BeneficiaryBrCountry` |  |  |  |
| 79 | `ARC.BEN.BENEFICIARY.SCHME.CDE` | `Beneficiary_BeneficiarySchmeCde` |  |  |  |
| 80 | `ARC.BEN.BENEFICIARY.SCH.PRTY` | `Beneficiary_BeneficiarySchPrty` |  |  |  |
| 81 | `ARC.BEN.BENEFICIARY.SCH.ISSUR` | `Beneficiary_BeneficiarySchIssur` |  |  |  |
| 82 | `ARC.BEN.BACC.PRP.SCH.NAME` | `Beneficiary_BaccPrpSchName` | TField |  | This field captures the account type of the beneficiary, when a beneficiary record(BEN.ACCT.NO.) is captured. EXAMPLE: CLABE , MOBILE , ACCOUNT NO. etc., |
| 83 | `ARC.BEN.BEN.CUSTOMER.NAME` | `Beneficiary_BenCustomerName` | TField |  | Identifies the Customer name who is the ultimate receiver of the funds transferred by the sending bank. |
| 84 | `ARC.BEN.BEN.CUSTOMER.ID` | `Beneficiary_BenCustomerId` | TField |  | Identifies the Customer number who is the ultimate receiver of the funds transferred by the sending bank. |
| 85 | `ARC.BEN.BEN.CUSTOMER.BIC` | `Beneficiary_BenCustomerBic` | TField |  | Identifies the Customer BIC of the ultimate receiver of the funds transferred by the sending bank. |
| 86 | `ARC.BEN.TRUSTED` | `Beneficiary_Trusted` | TField |  | This field identifies if a Beneficiary is considered as a "trusted" beneficiary. If the flag is set to "Yes" it can indicate to other applications that this Beneficiary is trusted and could hence impact decisioning on whether additional authentication is required or not. How this flag is set or consumed is up to the banks implementation requirements. Allowed values are "YES" or "NO" |
| 87 | `ARC.BEN.DEPARTMENT` | `Beneficiary_Department` | TField |  | Stores the department of the Beneficiary Customer. |
| 88 | `ARC.BEN.SUB.DEPARTMENT` | `Beneficiary_SubDepartment` | TField |  | Stores define the sub department of the Beneficiary Customer. |
| 89 | `ARC.BEN.BUILDING.NUMBER` | `Beneficiary_BuildingNumber` | TField |  | Stores the Building Number of the Beneficiary Customer. |
| 90 | `ARC.BEN.BUILDING.NAME` | `Beneficiary_BuildingName` | TField |  | Stores the Building Name of the Beneficiary Customer. |
| 91 | `ARC.BEN.FLOOR` | `Beneficiary_Floor` | TField |  | Stores the Building Floor of the Beneficiary Customer. |
| 92 | `ARC.BEN.PO.BOX.NUMBER` | `Beneficiary_PoBoxNumber` | TField |  | Stores the Post Box Number of the Beneficiary Customer. |
| 93 | `ARC.BEN.FLAT.NUMBER` | `Beneficiary_FlatNumber` | TField |  | Stores the Building Flat Number of the Beneficiary Customer. |
| 94 | `ARC.BEN.TOWN.LOCATION` | `Beneficiary_TownLocation` | TField |  | Stores the Town location of the Beneficiary Customer. |
| 95 | `ARC.BEN.DISTRICT.NAME` | `Beneficiary_DistrictName` | TField |  | Stores the district name of the Beneficiary Customer. |
| 96 | `ARC.BEN.COUNTRY.SUBDIVISION` | `Beneficiary_CountrySubdivision` | TField |  | Stores the country subdivision of the Beneficiary Customer. |
| 97 | `ARC.BEN.ULTIMATE.CRED.DEPARTMENT` | `Beneficiary_UltimateCredDepartment` | TField |  | Stores the department of the Ultimate Creditor. |
| 98 | `ARC.BEN.ULTIMATE.CRED.SUB.DEPARTMENT` | `Beneficiary_UltimateCredSubDepartment` | TField |  | Stores the sub department of the Ultimate Creditor. |
| 99 | `ARC.BEN.ULTIMATE.CRED.STREET.ADDR` | `Beneficiary_UltimateCredStreetAddr` | TField |  | Stores the Street of the Ultimate Creditor. |
| 100 | `ARC.BEN.ULTIMATE.CRED.BUILDING.NUMBER` | `Beneficiary_UltimateCredBuildingNumber` | TField |  | Stores the Building Number of the Ultimate Creditor. |
| 101 | `ARC.BEN.ULTIMATE.CRED.BUILDING.NAME` | `Beneficiary_UltimateCredBuildingName` | TField |  | Stores the Building Name of the Ultimate Creditor. |
| 102 | `ARC.BEN.ULTIMATE.CRED.FLOOR` | `Beneficiary_UltimateCredFloor` | TField |  | Stores the Building Floor of the Ultimate Creditor. |
| 103 | `ARC.BEN.ULTIMATE.CRED.PO.BOX.NUMBER` | `Beneficiary_UltimateCredPoBoxNumber` | TField |  | Stores the Post Box Number of the Ultimate Creditor. |
| 104 | `ARC.BEN.ULTIMATE.CRED.FLAT.NUMBER` | `Beneficiary_UltimateCredFlatNumber` | TField |  | Stores the Building Flat Number of the Ultimate Creditor. |
| 105 | `ARC.BEN.ULTIMATE.CRED.TOWN.LOCATION` | `Beneficiary_UltimateCredTownLocation` | TField |  | Stores the Town location of the Ultimate Creditor. |
| 106 | `ARC.BEN.ULTIMATE.CRED.DISTRICT.NAME` | `Beneficiary_UltimateCredDistrictName` | TField |  | Stores the district name of the Ultimate Creditor. |
| 107 | `ARC.BEN.ULTIMATE.CRED.TOWN.NAME` | `Beneficiary_UltimateCredTownName` | TField |  | Stores the town name of the Ultimate Creditor. |
| 108 | `ARC.BEN.ULTIMATE.CRED.POST.CODE` | `Beneficiary_UltimateCredPostCode` | TField |  | Stores the postal code of the Ultimate Creditor. |
| 109 | `ARC.BEN.ULTIMATE.CRED.COUNTRY.SUBDIVISION` | `Beneficiary_UltimateCredCountrySubdivision` | TField |  | Stores the country subdivision of the Ultimate Creditor. |
| 110 | `ARC.BEN.INTERNAL.FLAG` | `Beneficiary_InternalFlag` | TField |  | Flag to indicate if beneficiary is internal type used for contract purposes and not by customer When it is updated with YES the beneficiary record is eligible for purging, provided its not linked to any contracts or accounts based on beneficiary parameter setup |
