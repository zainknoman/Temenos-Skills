# CUSTOMER — Table Schema

> Source: `INSERTS/I_F.CUSTOMER` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CUS.MNEMONIC` | `Customer_Mnemonic` | TField | Yes | Specifies an alternative easy means of referencing the Customer. For countries where the Customer name should not be recorded (e.g. numbered Customers/accounts) any value can be entered in this field with the exception that the first character must be alpha. Like the ID, the Mnemonic must be unique across T24. Care should be taken when assigning Mnemonics to Customers and some rules should ideally be defined across the bank to allow easy identification of the Customers by their Mnemonics. Note : For each Customer, the System will automatically update the internal file "MNEMONIC.CUSTOMER" which allows the User to display the Customers in Mnemonic sequence instead of Customer number. Validation Rules: 3-10 type MNE (Uppercase alpha or numeric, first character alpha, or ".") characters. (Mandatory input) |
| 2 | `EB.CUS.SHORT.NAME` | `Customer_ShortName` |  |  |  |
| 3 | `EB.CUS.NAME.1` | `Customer_Name1` |  |  |  |
| 4 | `EB.CUS.NAME.2` | `Customer_Name2` |  |  |  |
| 5 | `EB.CUS.STREET` | `Customer_Street` |  |  |  |
| 6 | `EB.CUS.ADDRESS` | `Customer_Address` |  |  |  |
| 7 | `EB.CUS.TOWN.COUNTRY` | `Customer_TownCountry` |  |  |  |
| 8 | `EB.CUS.POST.CODE` | `Customer_PostCode` |  |  |  |
| 9 | `EB.CUS.COUNTRY` | `Customer_Country` |  |  |  |
| 10 | `EB.CUS.RELATION.CODE` | `Customer_RelationCode` |  |  |  |
| 11 | `EB.CUS.REL.CUSTOMER` | `Customer_RelCustomer` |  |  |  |
| 12 | `EB.CUS.REVERS.REL.CODE` | `Customer_ReversRelCode` |  |  |  |
| 13 | `EB.CUS.REL.DELIV.OPT` | `Customer_RelDelivOpt` |  |  |  |
| 14 | `EB.CUS.ROLE` | `Customer_Role` |  |  |  |
| 15 | `EB.CUS.ROLE.MORE.INFO` | `Customer_RoleMoreInfo` |  |  |  |
| 16 | `EB.CUS.ROLE.NOTES` | `Customer_RoleNotes` |  |  |  |
| 17 | `EB.CUS.REL.RESERV6` | `Customer_RelReserv6` |  |  |  |
| 18 | `EB.CUS.REL.RESERV5` | `Customer_RelReserv5` |  |  |  |
| 19 | `EB.CUS.REL.RESERV4` | `Customer_RelReserv4` |  |  |  |
| 20 | `EB.CUS.REL.RESERV3` | `Customer_RelReserv3` |  |  |  |
| 21 | `EB.CUS.REL.RESERV2` | `Customer_RelReserv2` |  |  |  |
| 22 | `EB.CUS.REL.RESERV1` | `Customer_RelReserv1` |  |  |  |
| 23 | `EB.CUS.SECTOR` | `Customer_Sector` | TField | Yes | Identifies the Sector code relating to the Customer. If the Sector code is defined on the Customer DEFAULT table the associated default values will be retrieved and added to a new Customer record during the Validation process except if some specific values have been input by the User. Validation Rules: 1-4 numeric character Sector code. (Mandatory input) It must be a valid code on the SECTOR table. The field must not be blank. |
| 24 | `EB.CUS.ACCOUNT.OFFICER` | `Customer_AccountOfficer` | TField | Conditional | Identifies the main Account Officer responsible for the Customer. his code will be defaulted on all Customer transactions within T24 except if it is overriden by another Account Officer code at the transaction or product level. The existence of the Account Officer code on every Customer transaction will allow generation of M.I.S. information at the Account Officer level. Validation Rules: 1-4 numeric character Account Officer code. (Mandatory input if no default value has been specified on the Customer DEFAULT Table for the corresponding sector code or the VERSION File [Ref: UTILITIES]. Otherwise Input is optional and will override default value.) It must be a valid code on the DEPT.ACCT.OFFICER table (Ref: GENERAL TABLES). |
| 25 | `EB.CUS.OTHER.OFFICER` | `Customer_OtherOfficer` |  |  |  |
| 26 | `EB.CUS.INDUSTRY` | `Customer_Industry` | TField | Conditional | Identifies the Industry in which the Customer is trading. Each User can define their own industry codes according to the use they want to make of them. Production of central bank reports classified by Industry codes or the monitoring of the overall credit exposure by Industry type are typical examples of uses of this code. Validation Rules: 1-10 numeric character Industry code. (Mandatory input if no default value has been specified on the Customer DEFAULT table for the corresponding Sector code or the VERSION File [Ref: UTILITIES]. Otherwise input is optional and will override default value.) It must be a valid code on the INDUSTRY code table. |
| 27 | `EB.CUS.TARGET` | `Customer_Target` | TField | Conditional | Specifies how the Customer is considered by the bank and how he fits in with the Account Officer's overall marketing strategy. Examples of this field are: "Prime Customer", "No Potential", etc. but it must be a valid code on the TARGET code table. The values of the field should be defined according to the bank's overall marketing strategy. Validation Rules: 1-4 numeric characters. (Mandatory input if no default value has been specified on the Customer DEFAULT table for the corresponding Sector code, or the VERSION File [Ref: UTILITIES]. Otherwise input is optional and will override default value.) |
| 28 | `EB.CUS.NATIONALITY` | `Customer_Nationality` | TField | Conditional | Identifies the Nationality of the Customer. Validation Rules: 2 type SSS (uppercase alpha) Country code characters. (Mandatory input if no default value has been specified on the Customer DEFAULT table for the corresponding Sector Code or the VERSION file [Ref: UTILITIES]. Otherwise input is optional and will override default value.) It must be a valid code on the COUNTRY table (Ref: GENERAL TABLES). |
| 29 | `EB.CUS.CUSTOMER.STATUS` | `Customer_CustomerStatus` | TField | Conditional | Identifies the Status of the Customer. The values applicable to this field can be defined by each bank/branch according to the their own practice. Validation Rules: 1-4 numeric characters. (Mandatory input if no default value has been specified on the Customer DEFAULT table for the corresponding Sector code or the VERSION file [Ref: UTILITIES]. Otherwise input is optional and will override default value.) It must be a valid code on the Customer STATUS table. |
| 30 | `EB.CUS.RESIDENCE` | `Customer_Residence` | TField | Conditional | Identifies the Country of Residence of the Customer. Any change in the value of this field will prompt a message reminding the User that the Town Country defined in line 4 of the SWIFT address should also be changed. If the User, for any reason, does not want to change the content of line 4 of the SWIFT address, he will be forced to confirm it by entering an Override. Validation Rules: 2 type SSS (uppercase alpha) Country code characters. (Mandatory input if no default value has been specified on the Customer DEFAULT table for the corresponding Sector code or the VERSION file [Ref: UTILITIES]. Otherwise input is optional and will override default value.) It must be a valid code on the COUNTRY table (Ref: GENERAL TABLES). |
| 31 | `EB.CUS.CONTACT.DATE` | `Customer_ContactDate` | TField | No | Specifies the date that first contact was made with the Customer. Validation Rules: 1-9 type D (Date format in range 1950 - 2049) numeric characters. (Optional Input. No default value.) This field is for information only. It must be a valid date which is less than or equal to today. |
| 32 | `EB.CUS.INTRODUCER` | `Customer_Introducer` | A (alphanumeric) | No | Identifies the name of the person who introduced the Customer to the bank. This field is for information only and must not contain more than 35 characters. Validation Rules: 1-35 type A (alphanumeric) characters. (Optional input. No default value.) |
| 33 | `EB.CUS.TEXT` | `Customer_Text` |  |  |  |
| 34 | `EB.CUS.LEGAL.ID` | `Customer_LegalId` |  |  |  |
| 35 | `EB.CUS.LEGAL.DOC.NAME` | `Customer_LegalDocName` |  |  |  |
| 36 | `EB.CUS.LEGAL.HOLDER.NAME` | `Customer_LegalHolderName` |  |  |  |
| 37 | `EB.CUS.LEGAL.ISS.AUTH` | `Customer_LegalIssAuth` |  |  |  |
| 38 | `EB.CUS.LEGAL.ISS.DATE` | `Customer_LegalIssDate` |  |  |  |
| 39 | `EB.CUS.LEGAL.EXP.DATE` | `Customer_LegalExpDate` |  |  |  |
| 40 | `EB.CUS.OFF.PHONE` | `Customer_OffPhone` |  |  |  |
| 41 | `EB.CUS.REVIEW.FREQUENCY` | `Customer_ReviewFrequency` | TField | No | This field allows the user to specify a frequency for any Customer indicating when any type of review should take place. If a valid Frequency only is input the next Review date will be calculated from the present system date. The first Review date and the Review Frequency will then be displayed. A different start date for the Reviews can, if required, be specified and input before the Frequency. Standard Frequency Format is as follows: Wn Where n = number of weeks in the cycle, n can have values 4-9. or Mnndd Where nn = number of months, nn can have values 01-99, dd = day of month. Note : (a) A Review Frequency can be input without a date but a date cannot be input without a Review Frequency. (b) The first date calculated by the System (if not input under 1) above) will then be the date resulting from the frequency applied to the Processing date. If a date was input first, the frequency will then be applied on this date and not on the Processing date. Validation Rules: This field is sub-divided in 2 elements: 1) Date 1-9 type D (standard date format in range 1950-2049) characters. The date input or generated in this field will correspond to the first review date. 2) Frequency 2-5 characters type FQU (standard frequency format) as shown in Details below. (Optional input. No default value.) Review Frequency cannot be less than 4 weeks. The start date for the Reviews must be greater than today's date. The system updates an internal file "CUSTOMER.FQU" which allows the user to check all the Customers for whom review dates and frequencies have been defined. |
| 42 | `EB.CUS.BIRTH.INCORP.DATE` | `Customer_BirthIncorpDate` | TField | No | Specifies the Customer's date of birth or the date on which the Company was registered. Any birth or incorporation date which is before 1950 should be entered yyyymmdd. Validation Rules: Standard date format - type DD (Date format in range 1000-2049). (Optional input. No default value.) It must be a valid date which is less than or equal to today. |
| 43 | `EB.CUS.GLOBAL.CUSTOMER` | `Customer_GlobalCustomer` | TField | No | Specifies a unique identification number for a multi-national Customer which is valid across all branches of the bank worldwide. The use of this Global Customer number will allow any bank to uniquely identify, on a worldwide basis, those Customers who are dealing with various branches across the world. The consolidation of the "Global" Customer exposure or profitability on a worldwide basis will then be made referencing this unique Customer identification. Validation Rules: 1-10 numeric characters. (Optional input. No default value.) It must be a valid number on the GLOBAL Table. |
| 44 | `EB.CUS.CUSTOMER.LIABILITY` | `Customer_CustomerLiability` | TField | No | Indicates the Customer consolidation number for credit grouping purposes, within the same branch/country. This field allows Customer exposure to be consolidated at the branch or country level when analysing the risk by the LIMIT Application. If entered it must be a valid Customer code or Mnemonic. Note : This is a no change field. Any change must be done using the LIMIT.CHANGE application. Validation Rules: 1-10 numeric character Customer Number or 3-10 type MNE (uppercase alpha or numeric, or ".") character Customer Mnemonic. (Optional input. Default Value is = None.) The customer number entered here must not be linked to another liability. |
| 45 | `EB.CUS.LANGUAGE` | `Customer_Language` | TField | Yes | Identifies the Customer's Language to be used for correspondence. Validation Rules: 1-2 numeric characters. (Mandatory input) Input must be a valid Language code defined on the LANGUAGE table (Ref: GENERAL TABLES). Multilanguage field. Where SWIFT is used the first language must only allow standard SWIFT character validation. If SWIFT is not used the first language can be configured via ASCII.VALUES and ASCII.VAL.TABLES to allow the required range of characters, and multiple language definitions will not be required. |
| 46 | `EB.CUS.POSTING.RESTRICT` | `Customer_PostingRestrict` |  |  |  |
| 47 | `EB.CUS.DISPO.OFFICER` | `Customer_DispoOfficer` | TField | No | The DISPO.OFFICER who is responsible overall for the CUSTOMER Validation Rules: Optional field - up to 4 numeric digits. Valid Dispo Officer as set up in the DISPO.OFFICER file. |
| 48 | `EB.CUS.COMPANY.BOOK` | `Customer_CompanyBook` | TField |  | This field holds the branch of the customer. Accepts the id of the COMPANY which shares customer with currently signed in company. This field when left blank will be updated with the value of the COMPANY under which the user is signed in. |
| 49 | `EB.CUS.CONFID.TXT` | `Customer_ConfidTxt` | TField |  | There are occasions where for the sake of client confidentiality that the client name is not used in advices or payment instructions generated by the bank. Typically a phrase such as 'One of our Clients' would be used instead of the client name. This field controls the generation of the standard text in the &amp;#145;Ordering Customer&amp;#146; fields of the SWIFT messages, allowing the text to be in the language of the receiving bank. The standard text is defined in the ORD record in DE.TRANSLATION. To utilise this the conversion should be set to &amp;#145;CUS*TEXT*ORD&amp;#146; in the relevant DE.FORMAT.SWIFT record. Validation Rules: Input is either YES or NO Yes - will try to insert the standard text in the ordering customer field of the SWIFT message provided the system has been set correctly. If unsuccessful then the customer text will be used. |
| 50 | `EB.CUS.DISPO.EXEMPT` | `Customer_DispoExempt` | TField |  | This field specifies whether a particular Transaction Type will be subject to Dispo processing. Validation Rules: |
| 51 | `EB.CUS.ISSUE.CHEQUES` | `Customer_IssueCheques` | TField |  | This field denotes whether the customer is eligible for cheque issue facility and to know first cheque book issued or not. System automatically changes the value to "YES" once first cheque book is issued to an account for the customer. Input "No" if the customer is not eligible for the cheque issue facility. To make cheque facility available to the customer change "NO" to Null. Validation Rules: User can only input "NO" or Null. Value "YES" is updated by the system. |
| 52 | `EB.CUS.CLS.CPARTY` | `Customer_ClsCparty` | TField |  | This field is used to cross check which counterparty can deal with CONTINUOUS LINKED SETTLEMENT (CLS). If this field is set to 'YES' then only FX.CLS.CPARTY accepts the CUSTOMER no. or mnemonic as ID otherwise throws error saying 'CUSTOMER NOT BE DEFINED CLS FLAG IN CUSTOMER TABLE' Validation Rules: A maximum of 3 characters may be entered. The following values are permitted: YES (or) NO |
| 53 | `EB.CUS.FX.COMM.GROUP.ID` | `Customer_FxCommGroupId` | TField |  | Validation Rules: Standard T24 numeric field. A maximum of 3 characters may be entered. Must be the key to a valid entry on the FX.COMM.GROUP file. |
| 54 | `EB.CUS.RESIDENCE.REGION` | `Customer_ResidenceRegion` | TField | No | This field is used for captial gains tax purposes and allows linking of regional captial gain indexation values as specified in the REGION application. Validation Rules: Must be a valid REGION code Optional Input |
| 55 | `EB.CUS.ASSET.CLASS` | `Customer_AssetClass` | TField |  | When asset classification is set in the system(through ASSET.CLASS.PARAMETER table) , this field would be automatically updated reflecting the overall classification of the customer. It would be updated with an asset classification that reflects the worst status among all the contracts for the customer in LD, MG and PD. For e.g. if customer has 2 contracts in the system each classified as "SPECIAL MENTION" and "DOUBTFUL" customer record would be updated with worst status which is "DOUBTFUL". Would be a valid record in LN.ASSET.CLASS table. Validation Rules: : No input - System maintained field |
| 56 | `EB.CUS.CUSTOMER.RATING` | `Customer_CustomerRating` |  |  |  |
| 57 | `EB.CUS.CR.PROFILE.TYPE` | `Customer_CrProfileType` |  |  |  |
| 58 | `EB.CUS.CR.PROFILE` | `Customer_CrProfile` |  |  |  |
| 59 | `EB.CUS.NO.UPDATE.CRM` | `Customer_NoUpdateCrm` | TField |  | Specifies whether the customer is intrested in CRM or not. If this field is set to YES then no CRM updates will happen for this customer . Otherwise this customer will be processed by CRM. Allowed values are YES or NO. Optinal input. By default it is NO. |
| 60 | `EB.CUS.TITLE` | `Customer_Title` | TField |  | Holds the title for the customer name as the part of improved client information required by CRM Validation Rules: : A maximum of 6 characters may be entered. The following values are permitted: MR MRS MS MISS DR REV |
| 61 | `EB.CUS.GIVEN.NAMES` | `Customer_GivenNames` | TField |  | Specifies customer's given name. This additional client detail is required by CRM. Validation Rules: : Maximum of 50 character is allowed Characters must support swift format |
| 62 | `EB.CUS.FAMILY.NAME` | `Customer_FamilyName` | TField |  | Specifies customer's family name. This additional client information is required by CRM. Validation Rules: : Maximum of 50 character is allowed Characters must support swift format |
| 63 | `EB.CUS.GENDER` | `Customer_Gender` | TField |  | Contains customer's gender. This additional client information is required by CRM. Validation Rules: : Maximum of 10 characters is allowed Allowed values are based on EB.LOOKUP details. Sample values MALE FEMALE Non-Binary. |
| 64 | `EB.CUS.DATE.OF.BIRTH` | `Customer_DateOfBirth` | TField | No | Specifies customer's date of birth. This additional client information is required by CRM. Validation Rules: : Standard date format (YYYYMMDD). Optional input. No default value. |
| 65 | `EB.CUS.MARITAL.STATUS` | `Customer_MaritalStatus` | TField |  | Identifies the marital status of the customer. This customer profile information is required by CRM. Validation Rules: : Linked to the virtual table EB.LOOKUP. All values must have an entry on EB.LOOKUP table. |
| 66 | `EB.CUS.NO.OF.DEPENDENTS` | `Customer_NoOfDependents` | TField |  | Specifies the number of dependents to the customer. This customer profile information is required by CRM. Validation Rules: : Input must be numeric |
| 67 | `EB.CUS.PHONE.1` | `Customer_Phone1` |  |  |  |
| 68 | `EB.CUS.SMS.1` | `Customer_Sms1` |  |  |  |
| 69 | `EB.CUS.EMAIL.1` | `Customer_Email1` |  |  |  |
| 70 | `EB.CUS.ADDR.LOCATION` | `Customer_AddrLocation` |  |  |  |
| 71 | `EB.CUS.EMPLOYMENT.STATUS` | `Customer_EmploymentStatus` |  |  |  |
| 72 | `EB.CUS.OCCUPATION` | `Customer_Occupation` |  |  |  |
| 73 | `EB.CUS.JOB.TITLE` | `Customer_JobTitle` |  |  |  |
| 74 | `EB.CUS.EMPLOYERS.NAME` | `Customer_EmployersName` |  |  |  |
| 75 | `EB.CUS.EMPLOYERS.ADD` | `Customer_EmployersAdd` |  |  |  |
| 76 | `EB.CUS.EMPLOYERS.BUSS` | `Customer_EmployersBuss` |  |  |  |
| 77 | `EB.CUS.EMPLOYMENT.START` | `Customer_EmploymentStart` |  |  |  |
| 78 | `EB.CUS.CUSTOMER.CURRENCY` | `Customer_CustomerCurrency` |  |  |  |
| 79 | `EB.CUS.SALARY` | `Customer_Salary` |  |  |  |
| 80 | `EB.CUS.ANNUAL.BONUS` | `Customer_AnnualBonus` |  |  |  |
| 81 | `EB.CUS.SALARY.DATE.FREQ` | `Customer_SalaryDateFreq` |  |  |  |
| 82 | `EB.CUS.NET.MONTHLY.IN` | `Customer_NetMonthlyIn` | TField |  | Net income earned by customer each month. Validation Rules: : Format of the amount fields based on the currency specified in LCCY 1-14 characters plus a decimal point (Standard Amount format) - type AMT. |
| 83 | `EB.CUS.NET.MONTHLY.OUT` | `Customer_NetMonthlyOut` | TField |  | Net expenses of customer each month. Validation Rules: : Format of the amount fields based on the currency specified in LCCY. 1-14 characters plus a decimal point (Standard Amount format) - type AMT. |
| 84 | `EB.CUS.RESIDENCE.STATUS` | `Customer_ResidenceStatus` |  |  |  |
| 85 | `EB.CUS.RESIDENCE.TYPE` | `Customer_ResidenceType` |  |  |  |
| 86 | `EB.CUS.RESIDENCE.SINCE` | `Customer_ResidenceSince` |  |  |  |
| 87 | `EB.CUS.RESIDENCE.VALUE` | `Customer_ResidenceValue` |  |  |  |
| 88 | `EB.CUS.MORTGAGE.AMT` | `Customer_MortgageAmt` |  |  |  |
| 89 | `EB.CUS.OTHER.FIN.REL` | `Customer_OtherFinRel` |  |  |  |
| 90 | `EB.CUS.OTHER.FIN.INST` | `Customer_OtherFinInst` |  |  |  |
| 91 | `EB.CUS.COMM.TYPE` | `Customer_CommType` |  |  |  |
| 92 | `EB.CUS.PREF.CHANNEL` | `Customer_PrefChannel` |  |  |  |
| 93 | `EB.CUS.ALLOW.BULK.PROCESS` | `Customer_AllowBulkProcess` | TField |  | To indicate whether the CUSTOMER is allowed to do BULK process. |
| 94 | `EB.CUS.LEGAL.ID.DOC.NAME` | `Customer_LegalIdDocName` |  |  |  |
| 95 | `EB.CUS.INTERESTS` | `Customer_Interests` |  |  |  |
| 96 | `EB.CUS.FAX.1` | `Customer_Fax1` |  |  |  |
| 97 | `EB.CUS.PREVIOUS.NAME` | `Customer_PreviousName` |  |  |  |
| 98 | `EB.CUS.CHANGE.DATE` | `Customer_ChangeDate` |  |  |  |
| 99 | `EB.CUS.CHANGE.REASON` | `Customer_ChangeReason` |  |  |  |
| 100 | `EB.CUS.CUSTOMER.SINCE` | `Customer_CustomerSince` | TField | No | Contains the date on which individual/corporate becomes the customer of the bank Validation Rules: : Standard date format (YYYYMMDD). (Optional input. No default value.) |
| 101 | `EB.CUS.CUSTOMER.TYPE` | `Customer_CustomerType` | TField |  | Indicates the type of customer, and is dependant on the CR (Customer Relationship Management) module being installed. The values of PROSPECT, EXTERNAL.USER, ACTIVE or null (the equivalent of ACTIVE) are allowed. If PROSPECT is entered then if the customer does not form a business relationship with the bank, such as opening an account, limit or contract then after a period of time defined on the CUST.RETENTION field on COMPANY the customer record and all associated data will be removed from the system. If the customer forms a business relationship with the bank then they (the prospect) will have a Customer Type of 'ACTIVE' and after this point the customer record cannot be physically deleted. However the data could be anonymized at a later stage as a part of the Customer Data Protection erasure process (CZ) If opted for External.user then the customer can only be used as a signatory in applications EB.SIGNATORY.GROUP, EB.EXTERNAL.USER, Owning Customer in Beneficiary, To Customer in EB.SECURE.MESSAGE, EXTERNAL.USER.PREFERENCES, EB.ALERT.REQUEST and then in field named SIGNATORY if used in any other applications, and restricted for use in any other fields in all remaining applications. |
| 102 | `EB.CUS.RESERVED.51` | `Customer_Reserved51` | TField |  |  |
| 103 | `EB.CUS.DATE.LAST.VERIFIED` | `Customer_DateLastVerified` | TField |  | Allows the date and time that the record was last input to be recorded, even though changes have not been made to the live record. This field will only be populated when input takes place via a VERSION that has the routine ADD.DATE.TIME applied to the VALIDATION.RTN field and DATE.LAST.VERIFIED in the VALIDATION.FLD field. Of particular use when used in conjunction with PROCESS.WORKFLOW. |
| 104 | `EB.CUS.SPOKEN.LANGUAGE` | `Customer_SpokenLanguage` |  |  |  |
| 105 | `EB.CUS.PASTIMES` | `Customer_Pastimes` |  |  |  |
| 106 | `EB.CUS.FURTHER.DETAILS` | `Customer_FurtherDetails` |  |  |  |
| 107 | `EB.CUS.DOMICILE` | `Customer_Domicile` | TField |  | Indicates country of domicile. If input, must exist on COUNTRY table. |
| 108 | `EB.CUS.OTHER.NATIONALITY` | `Customer_OtherNationality` |  |  |  |
| 109 | `EB.CUS.CALC.RISK.CLASS` | `Customer_CalcRiskClass` | TField |  | Personal Risk Class (calculated). If input, must exist on RISK.CLASS table. |
| 110 | `EB.CUS.MANUAL.RISK.CLASS` | `Customer_ManualRiskClass` | TField |  | Personal Risk Class (manual override). If input, must exist on RISK.CLASS table. |
| 111 | `EB.CUS.OVERRIDE.REASON` | `Customer_OverrideReason` |  |  |  |
| 112 | `EB.CUS.TAX.ID` | `Customer_TaxId` |  |  |  |
| 113 | `EB.CUS.VIS.TYPE` | `Customer_VisType` |  |  |  |
| 114 | `EB.CUS.VIS.COMMENT` | `Customer_VisComment` |  |  |  |
| 115 | `EB.CUS.VIS.INTERNAL.REVIEW` | `Customer_VisInternalReview` |  |  |  |
| 116 | `EB.CUS.FORMER.VIS.TYPE` | `Customer_FormerVisType` |  |  |  |
| 117 | `EB.CUS.FORMER.VIS.COMMENT` | `Customer_FormerVisComment` |  |  |  |
| 118 | `EB.CUS.RISK.ASSET.TYPE` | `Customer_RiskAssetType` |  |  |  |
| 119 | `EB.CUS.RISK.LEVEL` | `Customer_RiskLevel` |  |  |  |
| 120 | `EB.CUS.RISK.TOLERANCE` | `Customer_RiskTolerance` |  |  |  |
| 121 | `EB.CUS.RISK.FROM.DATE` | `Customer_RiskFromDate` |  |  |  |
| 122 | `EB.CUS.LAST.KYC.REVIEW.DATE` | `Customer_LastKycReviewDate` | TField |  | Date customer KYC information was last reviewed. |
| 123 | `EB.CUS.AUTO.NEXT.KYC.REVIEW.DATE` | `Customer_AutoNextKycReviewDate` | TField |  | Date system has calculated customer should next be reviewed. |
| 124 | `EB.CUS.MANUAL.NEXT.KYC.REVIEW.DATE` | `Customer_ManualNextKycReviewDate` | TField |  | Manual specification of next review date. |
| 125 | `EB.CUS.LAST.SUIT.REVIEW.DATE` | `Customer_LastSuitReviewDate` | TField |  | Date customer Suitability information was last reviewed. |
| 126 | `EB.CUS.AUTO.NEXT.SUIT.REVIEW.DATE` | `Customer_AutoNextSuitReviewDate` | TField |  | Date system has calculated customer suitability should next be reviewed. |
| 127 | `EB.CUS.MANUAL.NEXT.SUIT.REVIEW.DATE` | `Customer_ManualNextSuitReviewDate` | TField |  | Manual specification of next suitability review date. |
| 128 | `EB.CUS.KYC.RELATIONSHIP` | `Customer_KycRelationship` | TField |  | Indicates the relationship this customer is being held in. If input, must exist on CR.RELATIONSHIP table. |
| 129 | `EB.CUS.MANDATE.APPL` | `Customer_MandateAppl` |  |  |  |
| 130 | `EB.CUS.MANDATE.REG` | `Customer_MandateReg` |  |  |  |
| 131 | `EB.CUS.MANDATE.RECORD` | `Customer_MandateRecord` |  |  |  |
| 132 | `EB.CUS.SECURE.MESSAGE` | `Customer_SecureMessage` | TField |  | If this field is set to YES, then the customer will receive a SECURE message.DE.ADDRESS record will be created newly for SECUREMSG carrier. |
| 133 | `EB.CUS.AML.CHECK` | `Customer_AmlCheck` | TField |  | Field is used to describe the legal controls that is required by institutions to prevent or report Anti Money Laundering activities.It can have YES, SENT or NULL values. Depending on these values the AML.RESULT field will get updated. |
| 134 | `EB.CUS.AML.RESULT` | `Customer_AmlResult` | TField |  | If the value in AML.CHECK is NULL, then this field will be NULL. If the value in AML.CHECK is SENT, then the value in this field will be RESULT.AWAITED. And if the value in AML.CHECK is YES, then the value in this field will be either POSITIVE or NEGATIVE. |
| 135 | `EB.CUS.LAST.AML.RESULT.DATE` | `Customer_LastAmlResultDate` | TField |  | This field is the date field, when the last Anti Money Laundering result is performed. |
| 136 | `EB.CUS.KYC.COMPLETE` | `Customer_KycComplete` | TField |  | Know Your Customer is the due diligence and bank regulation that institutions must perform to identify their clients and ascertain relevant information pertinent to doing financial business with them. This field is for information only and contains YES or NULL. If set to YES then the information related to the customer has been collected and verified. |
| 137 | `EB.CUS.INTERNET.BANKING.SERVICE` | `Customer_InternetBankingService` | TField |  | If field is set to YES, then Internet Banking service will be enabled for the customer. |
| 138 | `EB.CUS.MOBILE.BANKING.SERVICE` | `Customer_MobileBankingService` | TField |  | Indicates whether is Customer is subscribed to the mobile banking service or not. |
| 139 | `EB.CUS.REPORT.TEMPLATE` | `Customer_ReportTemplate` | TField |  | Identifies the "Orchestrate Report Style" to be used for the Customer. The report style allow you customise a report - the look and feel as well as specific pages and elements that are displayed. This is the lookup field CUS.REPORT.TEMPLATE. This field is only inputtable if both the Asset Management (AM) and Wealth Management Reporting (WR) products are installed. |
| 140 | `EB.CUS.HOLDINGS.PIVOT` | `Customer_HoldingsPivot` |  |  |  |
| 141 | `EB.CUS.MERGED.TO` | `Customer_MergedTo` | TField |  | If duplicate customer record is merged with main customer then in duplicate customer record, main customer id is updated in this field. Accept valid customer id. |
| 142 | `EB.CUS.MERGED.STATUS` | `Customer_MergedStatus` | TField |  | This field denotes whether the customer is merged with main customer or not. It accepts only two values MERGE and UNMERGE. |
| 143 | `EB.CUS.ALT.CUS.ID` | `Customer_AltCusId` |  |  |  |
| 144 | `EB.CUS.EXTERN.SYS.ID` | `Customer_ExternSysId` |  |  |  |
| 145 | `EB.CUS.EXTERN.CUS.ID` | `Customer_ExternCusId` |  |  |  |
| 146 | `EB.CUS.SOCIAL.NTW.IDS` | `Customer_SocialNtwIds` |  |  |  |
| 147 | `EB.CUS.PERSON.ENTITY.ID` | `Customer_PersonEntityId` | TField |  | When a customer record has been created from an underlying PERSON.ENTITY record this field will contain the ID to the PERSON.ENTITY record. Creating a link between the two records. The id must be in the range of 1-9999999999 Validation rules No Input field 1- 10 numerical characters &#160; &#160; |
| 148 | `EB.CUS.REG.COUNTRY` | `Customer_RegCountry` | TField | No | This field is used to identify which country an entity has been registered, this field may be populated when a Customer record has been created from an underlying PERSON.ENTITY Validation rules Optional input 2 type SSS uppercase country code characters Must be a valid record on the COUNTRY table No input if the field PERSON.ENTITY is person |
| 149 | `EB.CUS.CR.USER.PROFILE.TYPE` | `Customer_CrUserProfileType` |  |  |  |
| 150 | `EB.CUS.CR.CALC.PROFILE` | `Customer_CrCalcProfile` |  |  |  |
| 151 | `EB.CUS.CR.USER.PROFILE` | `Customer_CrUserProfile` |  |  |  |
| 152 | `EB.CUS.CR.CALC.RESET.DATE` | `Customer_CrCalcResetDate` |  |  |  |
| 153 | `EB.CUS.REF.DATA.ITEM` | `Customer_RefDataItem` |  |  |  |
| 154 | `EB.CUS.REF.DATA.VALUE` | `Customer_RefDataValue` |  |  |  |
| 155 | `EB.CUS.PROB.OF.DEFT` | `Customer_ProbOfDeft` |  |  |  |
| 156 | `EB.CUS.DEATH.DATE` | `Customer_DeathDate` | TField |  | This holds the date of death of the customer |
| 157 | `EB.CUS.NOTIFICATION.OF.DEATH` | `Customer_NotificationOfDeath` | TField |  | This is the date on which the bank gets the notification that the customer is dead |
| 158 | `EB.CUS.PROBATE.DATE` | `Customer_ProbateDate` | TField |  | This is the date on which the funds belonged to the deceased customer will be handed over to the beneficiary |
| 159 | `EB.CUS.VULNERABILITY` | `Customer_Vulnerability` |  |  |  |
| 160 | `EB.CUS.UPDATE.PREV.ADDRESS` | `Customer_UpdatePrevAddress` | TField |  | This indicates whether to maintain the address history in the table PREV.CUST.ADDRESS. If No specified then address details will not be updated in the table. If nothing specified the details will be maintained Validation Rules: The values will be null or NO |
| 161 | `EB.CUS.NAME.ALIAS` | `Customer_NameAlias` |  |  |  |
| 162 | `EB.CUS.ADDRESS.COUNTRY` | `Customer_AddressCountry` | TField |  | This field defines which country is the country of the address being captured. Validation Rule: Valid record from country to be mentioned. |
| 163 | `EB.CUS.ADDRESS.ITEM1` | `Customer_AddressItem1` |  |  |  |
| 164 | `EB.CUS.ADDRESS.ITEM2` | `Customer_AddressItem2` |  |  |  |
| 165 | `EB.CUS.ADDRESS.TYPE` | `Customer_AddressType` | TField |  | Will identify the nature of the postal address. To be linked to an EB.LOOKUP. |
| 166 | `EB.CUS.ADDRESS.PURPOSE` | `Customer_AddressPurpose` | TField |  | Represents the special purpose of the address. To be linked to a new EB.LOOKUP table. |
| 167 | `EB.CUS.BUILDING.NUMBER` | `Customer_BuildingNumber` | TField |  | Represents the number that identifies the position of a building on a street |
| 168 | `EB.CUS.BUILDING.NAME` | `Customer_BuildingName` | TField |  | Represents the name of the building, entrance |
| 169 | `EB.CUS.FLAT.NUMBER` | `Customer_FlatNumber` | TField |  | The number that identifies apartment and unit that have other dwellings above or below, often with shared access and common areas. |
| 170 | `EB.CUS.PO.BOX.NUMBER` | `Customer_PoBoxNumber` | TField |  | Identifies the postal office (PO) box number. |
| 171 | `EB.CUS.COUNTRY.SUBDIVISION` | `Customer_CountrySubdivision` | TField |  | Represents a subdivision of a country such as state, region, county. This field will be linked to a vetting table or to a virtual table as per the address rules setup. |
| 172 | `EB.CUS.SALUTATION` | `Customer_Salutation` | TField |  | Represents the greeting used for communication with the client. |
| 173 | `EB.CUS.CONTACT.TYPE` | `Customer_ContactType` |  |  |  |
| 174 | `EB.CUS.IDD.PREFIX.PHONE` | `Customer_IddPrefixPhone` |  |  |  |
| 175 | `EB.CUS.CONTACT.DATA` | `Customer_ContactData` |  |  |  |
| 176 | `EB.CUS.AUTO.UPD.DEL.ADD` | `Customer_AutoUpdDelAdd` |  |  |  |
| 177 | `EB.CUS.ADDRESS.VALIDATED.BY` | `Customer_AddressValidatedBy` | TField |  | Represents the party/service which was used to confirm that it is a real address. Core will not provide any automation. Can be used by country/implementation layer to store the name/identifier of local party/service used to confirm the address; Free text. |
| 178 | `EB.CUS.LOCAL.CONTENT` | `Customer_LocalContent` |  |  |  |
| 179 | `EB.CUS.LOCAL.REF` | `Customer_LocalRef` |  |  |  |
| 180 | `EB.CUS.OVERRIDE` | `Customer_Override` |  |  |  |
| 181 | `EB.CUS.RECORD.STATUS` | `Customer_RecordStatus` | String |  |  |
| 182 | `EB.CUS.CURR.NO` | `Customer_CurrNo` | String |  |  |
| 183 | `EB.CUS.INPUTTER` | `Customer_Inputter` |  |  |  |
| 184 | `EB.CUS.DATE.TIME` | `Customer_DateTime` |  |  |  |
| 185 | `EB.CUS.AUTHORISER` | `Customer_Authoriser` | String |  |  |
| 186 | `EB.CUS.CO.CODE` | `Customer_CoCode` | String |  |  |
| 187 | `EB.CUS.DEPT.CODE` | `Customer_DeptCode` | String |  |  |
| 188 | `EB.CUS.AUDITOR.CODE` | `Customer_AuditorCode` | String |  |  |
| 189 | `EB.CUS.AUDIT.DATE.TIME` | `Customer_AuditDateTime` | String |  |  |
| 190 | `EB.CUS.EXIT.STATUS` | `Customer_ExitStatus` | TField | No | Indicates the Customer/Prospect has closed the relationship with the bank. Must be a valid record in Customer Exit Status This field is optional. |
| 191 | `EB.CUS.EXIT.REASON` | `Customer_ExitReason` | TField | No | Indicates the reason for exiting a relation with a prospect or customer. This field is optional. |
| 192 | `EB.CUS.EXIT.DATE` | `Customer_ExitDate` | TField | No | The date when the Exit Status has been updated last time. This will be automatically populated by the system with the current business date when the Exit Status is captured and the changes are authorised This field is optional. |
| 193 | `EB.CUS.DEPARTMENT` | `Customer_Department` | TField |  | Identifies a division of a large organisation or building |
| 194 | `EB.CUS.SUB.DEPARTMENT` | `Customer_SubDepartment` | TField |  | Identifies a sub-division of a large organisation or building |
| 195 | `EB.CUS.FLOOR` | `Customer_Floor` | TField |  | Floor or storey within a building |
| 196 | `EB.CUS.TOWN.LOCATION.NAME` | `Customer_TownLocationName` | TField |  | Specific location name within the town. |
| 197 | `EB.CUS.DISTRICT.NAME` | `Customer_DistrictName` | TField |  | Identifies a subdivision within a country sub-division. |
| 198 | `EB.CUS.BIRTH.PROVINCE` | `Customer_BirthProvince` |  |  |  |
| 199 | `EB.CUS.BIRTH.CITY` | `Customer_BirthCity` |  |  |  |
| 200 | `EB.CUS.BIRTH.COUNTRY` | `Customer_BirthCountry` |  |  |  |
| 201 | `EB.CUS.LEGAL.ISS.CTRY` | `Customer_LegalIssCtry` |  |  |  |
