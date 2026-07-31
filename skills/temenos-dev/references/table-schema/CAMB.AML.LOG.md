# CAMB.AML.LOG — Table Schema

> Source: `INSERTS/I_F.CAMB.AML.LOG` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.AML.FIRST.NAME` | `CambAmlLog_FirstName` | TField | Yes | First name of customer.Mandatory field. Defaults from primary Customer record, if any. |
| 2 | `CAMB.AML.FNAME.FIELD` | `CambAmlLog_FnameField` | TField |  |  |
| 3 | `CAMB.AML.LAST.NAME` | `CambAmlLog_LastName` | TField | Yes | Last name of customer.Mandatory field.Defaults from primary Customer record, if any. |
| 4 | `CAMB.AML.LNAME.FIELD` | `CambAmlLog_LnameField` | TField |  |  |
| 5 | `CAMB.AML.EMPLOYEE` | `CambAmlLog_Employee` | TField |  | Is the customer an employee? |
| 6 | `CAMB.AML.POSTCODE` | `CambAmlLog_Postcode` | TField |  | Post code of primary customer address. (Mailing address) |
| 7 | `CAMB.AML.DOB` | `CambAmlLog_Dob` | TField | Yes | Date of birth of customer.Mandatory field.Defaults from primary Customer record, if any. |
| 8 | `CAMB.AML.ADDRESS` | `CambAmlLog_Address` | TField |  |  |
| 9 | `CAMB.AML.CITY` | `CambAmlLog_City` | TField | Yes | City of the Customer.Mandatory field.Defaults from primary Customer record from city of Mailing Address |
| 10 | `CAMB.AML.COUNTRY` | `CambAmlLog_Country` | TField | Yes | Valid country code (Address of customer)Mandatory field.Country of the Customer does LCTR.Defaults the country information from primary Customer record of Mailing Address |
| 11 | `CAMB.AML.PROVINCE` | `CambAmlLog_Province` | TField | Yes | Province (Address of customer)Mandatory field.Province of the Customer does LCTR.Defaults the province information from primary Customer record of Mailing Address |
| 12 | `CAMB.AML.OCCUPATION` | `CambAmlLog_Occupation` | TField | Yes | Occupation of customer does LCTR.Mandatory field. |
| 13 | `CAMB.AML.PRIN.BSNSS` | `CambAmlLog_PrinBsnss` | TField |  |  |
| 14 | `CAMB.AML.POS.TITLE` | `CambAmlLog_PosTitle` | TField |  | Title for the customer does LCTR. |
| 15 | `CAMB.AML.ID.TYPE` | `CambAmlLog_IdType` | TField | Yes | Valid ID type of customer does LCTR.Mandatory field,Defaults the first ID type of the customer from Customer record. |
| 16 | `CAMB.AML.ID.NO` | `CambAmlLog_IdNo` | TField | Yes | ID number does LCTR.Mandatory field,Defaults the first ID type No of the customer from Customer record. |
| 17 | `CAMB.AML.CNTRY.ISSUE` | `CambAmlLog_CntryIssue` | TField | Yes | Country which the document is issued.Mandatory field,Defaults the first ID type's country issue information from Customer record. |
| 18 | `CAMB.AML.PLACE.ISSUE` | `CambAmlLog_PlaceIssue` | TField |  | Place of issue of IDDefaults the first ID type's place of issue information from Customer record. |
| 19 | `CAMB.AML.SRC.OF.FUND` | `CambAmlLog_SrcOfFund` |  |  |  |
| 20 | `CAMB.AML.FLAG.PERS` | `CambAmlLog_FlagPers` | TField |  | Is the transaction been performed by 3rd party.Inputs allowed - YES/NO |
| 21 | `CAMB.AML.BELIEVE.3P` | `CambAmlLog_Believe3p` | TField |  |  |
| 22 | `CAMB.AML.RATIONALE.3P` | `CambAmlLog_Rationale3p` | TField |  |  |
| 23 | `CAMB.AML.FNAME.3P` | `CambAmlLog_Fname3p` | TField |  | If the transaction is performed by 3rd party, this field holds the 3rd party given name |
| 24 | `CAMB.AML.FNAME.FLD.3P` | `CambAmlLog_FnameFld3p` | TField |  |  |
| 25 | `CAMB.AML.LNAME.3P` | `CambAmlLog_Lname3p` | TField |  | If the transaction is performed by 3rd party, this field holds the 3rd party last name |
| 26 | `CAMB.AML.LNAME.FLD.3P` | `CambAmlLog_LnameFld3p` | TField |  |  |
| 27 | `CAMB.AML.ENT.3P` | `CambAmlLog_Ent3p` | TField |  | 3rd Party Entity Name for the transaction made on behalf of personal customer. |
| 28 | `CAMB.AML.DOB.3P` | `CambAmlLog_Dob3p` | TField |  | If the transaction is performed by 3rd party, this field holds the Date of birth incase the 3rd party is an individual |
| 29 | `CAMB.AML.ADDR.3P` | `CambAmlLog_Addr3p` | TField |  | If the transaction is performed by 3rd party, this field holds the Address of 3rd party |
| 30 | `CAMB.AML.CITY.3P` | `CambAmlLog_City3p` | TField |  | If the transaction is performed by 3rd party, this field holds the City information of the third pary. |
| 31 | `CAMB.AML.CTRY.3P` | `CambAmlLog_Ctry3p` | TField |  | If the transaction is performed by 3rd party, this field holds the Country information of the third party. |
| 32 | `CAMB.AML.PCDE.3P` | `CambAmlLog_Pcde3p` | TField |  | If the transaction is performed by 3rd party, this field holds the Pincode information of the third party. |
| 33 | `CAMB.AML.PROV.3P` | `CambAmlLog_Prov3p` | TField |  |  |
| 34 | `CAMB.AML.OCCP.3P` | `CambAmlLog_Occp3p` | TField |  |  |
| 35 | `CAMB.AML.PRIN.BUS.3P` | `CambAmlLog_PrinBus3p` | TField |  |  |
| 36 | `CAMB.AML.POS.3P` | `CambAmlLog_Pos3p` | TField |  |  |
| 37 | `CAMB.AML.CORP.3P` | `CambAmlLog_Corp3p` | TField |  | Is the transaction been performed by 3rd party is a Corporation.Inputs allowed - YES/NO |
| 38 | `CAMB.AML.CORPNO.3P` | `CambAmlLog_Corpno3p` | TField |  | If the 3rd party is a corporate, incorporation number to be stored. |
| 39 | `CAMB.AML.PLACE.IS.3P` | `CambAmlLog_PlaceIs3p` | TField |  | Place of issuance of the corporation. |
| 40 | `CAMB.AML.REL.3P` | `CambAmlLog_Rel3p` | TField |  | Relation of 3rd party with personal customer. |
| 41 | `CAMB.AML.ENT.NAME.3P` | `CambAmlLog_EntName3p` | TField |  | Name of the Entity if the customer acts as third party and performs the transaction. |
| 42 | `CAMB.AML.NOB.3P` | `CambAmlLog_Nob3p` | TField |  | If the transaction is performed by 3rd party, this field holds the Date of incorporation, if the 3rd party is a corporation. |
| 43 | `CAMB.AML.FNAME.NP` | `CambAmlLog_FnameNp` | TField |  |  |
| 44 | `CAMB.AML.FN.FLD.NP` | `CambAmlLog_FnFldNp` | TField |  |  |
| 45 | `CAMB.AML.LNAME.NP` | `CambAmlLog_LnameNp` | TField |  |  |
| 46 | `CAMB.AML.NOB.NP` | `CambAmlLog_NobNp` | TField |  |  |
| 47 | `CAMB.AML.EMP.FLG.NP` | `CambAmlLog_EmpFlgNp` | TField |  |  |
| 48 | `CAMB.AML.SRC.FUND.NP` | `CambAmlLog_SrcFundNp` | TField |  |  |
| 49 | `CAMB.AML.FLAG.NONPERS` | `CambAmlLog_FlagNonpers` | TField |  |  |
| 50 | `CAMB.AML.FNAME.3P.NP` | `CambAmlLog_Fname3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the 3rd party given name |
| 51 | `CAMB.AML.LNAME.3P.NP` | `CambAmlLog_Lname3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the 3rd party last name |
| 52 | `CAMB.AML.EMPLOYEE.3P.NP` | `CambAmlLog_Employee3pNp` | TField |  |  |
| 53 | `CAMB.AML.ENT.FLG.3P.NP` | `CambAmlLog_EntFlg3pNp` | TField |  | If the transaction is performed by 3rd party on behalf of non personal customer, is the 3rd party is Entity or Individual.Inputs allowed - YES / NO |
| 54 | `CAMB.AML.ENT.CRP.3P.NP` | `CambAmlLog_EntCrp3pNp` | TField |  |  |
| 55 | `CAMB.AML.BELIEVE.3P.NP` | `CambAmlLog_Believe3pNp` | TField |  |  |
| 56 | `CAMB.AML.RATIONALE.3P.NP` | `CambAmlLog_Rationale3pNp` | TField |  |  |
| 57 | `CAMB.AML.ENT.3P.NP` | `CambAmlLog_Ent3pNp` | TField |  | 3rd Party Entity Name for the transaction made on behalf of non personal customer. |
| 58 | `CAMB.AML.NOB.3P.NP` | `CambAmlLog_Nob3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Date of incorporation details, if the 3rd party is a Corporation. |
| 59 | `CAMB.AML.CORPNO.3P.NP` | `CambAmlLog_Corpno3pNp` | TField |  | If the 3rd party is a corporate, incorporation number to be stored. |
| 60 | `CAMB.AML.PLACE.IS.3P.NP` | `CambAmlLog_PlaceIs3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Place of issuance of the corporation. ( (if 3rd party is a corporation) |
| 61 | `CAMB.AML.REL.3P.NP` | `CambAmlLog_Rel3pNp` | TField |  | Relation of 3rd party with non personal customer. |
| 62 | `CAMB.AML.ADDR.3P.NP` | `CambAmlLog_Addr3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Address of 3rd party |
| 63 | `CAMB.AML.CITY.3P.NP` | `CambAmlLog_City3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the City information of the 3rd party. |
| 64 | `CAMB.AML.CTRY.3P.NP` | `CambAmlLog_Ctry3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Country information of the third party. |
| 65 | `CAMB.AML.PROV.3P.NP` | `CambAmlLog_Prov3pNp` | TField |  |  |
| 66 | `CAMB.AML.PCDE.3P.NP` | `CambAmlLog_Pcde3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Pincode information of the third party. |
| 67 | `CAMB.AML.PRIMARY.CUSTOMER` | `CambAmlLog_PrimaryCustomer` | TField |  | This field holds the customer No, initiating the transactionHot Value field. Based on the input, other field value gets defaulted. |
| 68 | `CAMB.AML.DOB.3P.NP` | `CambAmlLog_Dob3pNp` | TField |  | If the transaction is performed by 3rd party, this field holds the Date of birth incase the 3rd party is an individual |
| 69 | `CAMB.AML.OCCUPATION.3P.NP` | `CambAmlLog_Occupation3pNp` | TField |  |  |
| 70 | `CAMB.AML.PRIN.BSNSS.3P.NP` | `CambAmlLog_PrinBsnss3pNp` | TField |  |  |
| 71 | `CAMB.AML.POS.TITLE.3P.NP` | `CambAmlLog_PosTitle3pNp` | TField |  |  |
| 72 | `CAMB.AML.TXN.COMMITED` | `CambAmlLog_TxnCommited` | TField |  |  |
| 73 | `CAMB.AML.WAY.TXN.COND` | `CambAmlLog_WayTxnCond` |  |  |  |
| 74 | `CAMB.AML.TXN.COND.DESC` | `CambAmlLog_TxnCondDesc` |  |  |  |
| 75 | `CAMB.AML.FUND.DISPOSITION` | `CambAmlLog_FundDisposition` |  |  |  |
| 76 | `CAMB.AML.FUND.DISP.DESC` | `CambAmlLog_FundDispDesc` |  |  |  |
| 77 | `CAMB.AML.ACCOUNT.TYPE` | `CambAmlLog_AccountType` | TField |  | Field to store the type of accounts.Inputs allowed are Personal, Business, Trust and Others. |
| 78 | `CAMB.AML.ACCT.TYPE.DESC` | `CambAmlLog_AcctTypeDesc` | TField |  | Proper description based on the type of the account. |
| 79 | `CAMB.AML.ID.TYPE.DESC` | `CambAmlLog_IdTypeDesc` | TField |  |  |
| 80 | `CAMB.AML.IND.BUS.PH.EXT` | `CambAmlLog_IndBusPhExt` | TField |  |  |
| 81 | `CAMB.AML.HOME.PHONE.NO` | `CambAmlLog_HomePhoneNo` | TField |  | Contact number of the customer initiating the Large cash transaction. |
| 82 | `CAMB.AML.OFF.PHONE.NO` | `CambAmlLog_OffPhoneNo` | TField |  | Contact number of the customer initiating the Large cash transaction. |
| 83 | `CAMB.AML.OFF.PHONE.NO.EXT` | `CambAmlLog_OffPhoneNoExt` | TField |  |  |
| 84 | `CAMB.AML.PROV.STAT.ID.ISS` | `CambAmlLog_ProvStatIdIss` | TField |  |  |
| 85 | `CAMB.AML.NAME.1` | `CambAmlLog_Name1` | TField |  |  |
| 86 | `CAMB.AML.NAME.2` | `CambAmlLog_Name2` | TField |  |  |
| 87 | `CAMB.AML.NAME.3` | `CambAmlLog_Name3` | TField |  |  |
| 88 | `CAMB.AML.IND.NAME.1` | `CambAmlLog_IndName1` | TField |  | Name of the individual if the customer acts as third party and performs the transaction. |
| 89 | `CAMB.AML.IND.NAME.2` | `CambAmlLog_IndName2` | TField |  |  |
| 90 | `CAMB.AML.IND.NAME.3` | `CambAmlLog_IndName3` | TField |  |  |
| 91 | `CAMB.AML.MID.NAME.INIT` | `CambAmlLog_MidNameInit` | TField |  | Field to indicate the Middle name of the primary customer. Free text |
| 92 | `CAMB.AML.NIGHT.DEPO.IND` | `CambAmlLog_NightDepoInd` | TField |  |  |
| 93 | `CAMB.AML.TXN.ID` | `CambAmlLog_TxnId` |  |  |  |
| 94 | `CAMB.AML.ADDRESS.1` | `CambAmlLog_Address1` | TField | Yes | Address of customer.Mandatory field.Defaults from primary Customer record from Address line 1 of Mailing Address |
| 95 | `CAMB.AML.ADDRESS.2` | `CambAmlLog_Address2` | TField |  | Address of customer.Defaults from primary Customer record from Address line 2 of Mailing Address |
| 96 | `CAMB.AML.ADDRESS.3` | `CambAmlLog_Address3` | TField |  | Address of customer.Defaults from primary Customer record from Address line 3 of Mailing Address |
| 97 | `CAMB.AML.FUND.DISP.AMT` | `CambAmlLog_FundDispAmt` |  |  |  |
| 98 | `CAMB.AML.FUND.DISP.CCY` | `CambAmlLog_FundDispCcy` |  |  |  |
| 99 | `CAMB.AML.ENT.CNTRY.ISSUE` | `CambAmlLog_EntCntryIssue` | TField |  |  |
| 100 | `CAMB.AML.ENT.PROV.ST.ISS` | `CambAmlLog_EntProvStIss` | TField |  |  |
| 101 | `CAMB.AML.TXN.CURRENCY` | `CambAmlLog_TxnCurrency` | TField |  |  |
| 102 | `CAMB.AML.TXN.AMOUNT` | `CambAmlLog_TxnAmount` | TField |  |  |
| 103 | `CAMB.AML.EXTRACT.DATE` | `CambAmlLog_ExtractDate` | TField |  |  |
| 104 | `CAMB.AML.MIDDLE.NAME.INIT` | `CambAmlLog_MiddleNameInit` | TField |  | If the transaction is performed by 3rd party, this field holds the 3rd party middle name. |
| 105 | `CAMB.AML.ISSUE.AUTH` | `CambAmlLog_IssueAuth` | TField |  | Issuing Authority of the Legal ID document.Defaults the first ID type's issuing authority information from Customer record. |
| 106 | `CAMB.AML.DATE.OF.VERIF` | `CambAmlLog_DateOfVerif` | TField |  | "Verification Date" of the ID document.Defaults the first ID type's Verification Date information from Customer record. |
| 107 | `CAMB.AML.DOC.ISS.DATE` | `CambAmlLog_DocIssDate` | TField |  | "Issue Date" of the ID document.Defaults the first ID type's Issue Date information from Customer record. |
| 108 | `CAMB.AML.ID.EXPIRY` | `CambAmlLog_IdExpiry` | TField |  | Field with date format - YYYYMMDDDefault from the field DOC.EXP.DATE from Customer record. |
| 109 | `CAMB.AML.EMP.STATUS` | `CambAmlLog_EmpStatus` | TField |  | Field to store the employment status of the Personal customer.Default the value from CUSTOMER > EMPLOYMENT.STATUS, if value exist.Valid record from EB.LOOKUP table Ex. EMPLOYMENT.STATUS*EMPLOYED. |
| 110 | `CAMB.AML.EMP.DES` | `CambAmlLog_EmpDes` | TField |  | Field to store the description/title of the Personal customer's employment.Default the value from CUSTOMER > JOB.TITLE, if value exist. |
| 111 | `CAMB.AML.NOC.CODE` | `CambAmlLog_NocCode` | TField |  | Field to store the NOC code of the Personal Customer.Default the value from CUSTOMER > NAICS, if value exist.Should be a valid record of USCORE.NAICS |
| 112 | `CAMB.AML.EMP.STATUS.NP` | `CambAmlLog_EmpStatusNp` | TField |  | Field to store the employment status of the Non Personal customer.Default the value from CUSTOMER > EMPLOYMENT.STATUS, if value exist.Valid record from EB.LOOKUP table Ex. EMPLOYMENT.STATUS*EMPLOYED. |
| 113 | `CAMB.AML.EMP.DES.NP` | `CambAmlLog_EmpDesNp` | TField |  | Field to store the description/title of the Non Personal customer's employment.Default the value from CUSTOMER > JOB.TITLE, if value exist |
| 114 | `CAMB.AML.NOC.CODE.NP` | `CambAmlLog_NocCodeNp` | TField |  | Field to store the NOC code of the Non Personal Customer.Default the value from CUSTOMER > NAICS, if value exist.Should be a valid record of USCORE.NAICS |
| 115 | `CAMB.AML.EMP.STATUS.3P` | `CambAmlLog_EmpStatus3p` | TField |  | Field to store the employment status of the Third Party Individual. This field is a drop down field with EB.LOOKUP values.Valid record from EB.LOOKUP table Ex. EMPLOYMENT.STATUS*EMPLOYED |
| 116 | `CAMB.AML.EMP.DES.3P` | `CambAmlLog_EmpDes3p` | TField |  | Field to store the description/title of the Third Party Individual. |
| 117 | `CAMB.AML.NOC.CODE.3P` | `CambAmlLog_NocCode3p` | TField |  | Field to store the NOC code of the Third Party Individual.Should be a valid record of USCORE.NAICS |
| 118 | `CAMB.AML.EMP.STATUS.3P.NP` | `CambAmlLog_EmpStatus3pNp` | TField |  | Field to store the employment status of the Third Party Individual.Applicable, if a customer is a Non Personal. Valid record from EB.LOOKUP table Ex. EMPLOYMENT.STATUS*EMPLOYED. |
| 119 | `CAMB.AML.EMP.DES.3P.NP` | `CambAmlLog_EmpDes3pNp` | TField |  | Field to store the description/title of the Third Party Individual.Applicable, if a customer is a Non Personal. |
| 120 | `CAMB.AML.NOC.CODE.3P.NP` | `CambAmlLog_NocCode3pNp` | TField |  | Field to store the NOC code of the Third Party Individual.Should be a valid record of USCORE.NAICSApplicable, if a customer is a Non Personal. |
| 121 | `CAMB.AML.AML.JCUST` | `CambAmlLog_AmlJcust` | TField |  | Field to store the reason/ remarks, in case of joint customers.Free text field. |
| 122 | `CAMB.AML.AML.FORM` | `CambAmlLog_AmlForm` | TField |  | Purpose of this field to indicate on what basis the AML form is updated., either conductor form or LCTR form.Allowed inputs - LCTR / ConductorValues are from EB.LOOKUP > AML.FORMSSystem updates this field as "Auto new Content".Version - CAMB.AML.LOG,CAMB.PERSONAL, to be updated as LCTRVersion - CAMB.AML.LOG,CAMB.NON.PERSONAL to be updated as LCTRVersion - CAMB.AML.LOG,CONDUCTOR to be updated as Conductor |
| 123 | `CAMB.AML.CONDUCTOR.TYPE` | `CambAmlLog_ConductorType` | TField |  | Purpose of the field to indicate the type of the Conductor CIF.New EB.LOOKUP to be created for Individual, Business, Public Entity, Corporation with look up id as CUSTOMER.TYPE |
| 124 | `CAMB.AML.COND.BENE.RELATION` | `CambAmlLog_CondBeneRelation` |  |  |  |
| 125 | `CAMB.AML.IS.CUSTOMER` | `CambAmlLog_IsCustomer` | TField |  | Purpose of the field to indicate the Conductor is a FI Client or not.Allowed inputs : YES / NO |
| 126 | `CAMB.AML.NON.MEM.OC` | `CambAmlLog_NonMemOc` | TField |  | Purpose of the field to indicate the transaction is a Cheque Deposit transaction or official cheque /draft issuance.Allowed inputs : YES / NO |
| 127 | `CAMB.AML.EMAIL` | `CambAmlLog_Email` | TField |  | Field to indicate the Email id of the Primary Customer.To be auto populated based on PRIMARY.CUSTOMERMapping - CUSTOMER>EMAIL.1 |
| 128 | `CAMB.AML.EMPLOYER` | `CambAmlLog_Employer` | TField |  | Field to indicate the employer of the Primary Customer.To be auto populated based on PRIMARY.CUSTOMERMapping - CUSTOMER>EMPLOYER.NAME |
| 129 | `CAMB.AML.IS.CUSTOMER.3P` | `CambAmlLog_IsCustomer3p` | TField |  | Field to indicate if third party is a FI Client or not.Allowed inputs Yes / NO |
| 130 | `CAMB.AML.THIRD.PARTY.CIF` | `CambAmlLog_ThirdPartyCif` | TField |  | Field to indicate the Customer Id of the Third party.Hot validation field to pull in CUSTOMER dataValid records of Customer.Text enrichment to show NAME.1 on screen |
| 131 | `CAMB.AML.MID.NAME.INIT.3P` | `CambAmlLog_MidNameInit3p` | TField |  | Field to indicate the Middle name of the Third party.Free text |
| 132 | `CAMB.AML.PHONE.3P` | `CambAmlLog_Phone3p` | TField |  | Field to indicate the Phone number of the Third party.Based on the Customer in THIRD.PARTY.CIF field, value to be defaulted from CUSTOMER>CONTACT.DETAIL.1Free Form Alpha/Numeric Field |
| 133 | `CAMB.AML.EMAIL.3P` | `CambAmlLog_Email3p` | TField |  | Field to indicate the email address of the Third party.Based on the Customer in THIRD.PARTY.CIF field, value to be defaulted from CUSTOMER>EMAIL.1Free Form Alpha/Numeric Field |
| 134 | `CAMB.AML.EMPLOYER.3P` | `CambAmlLog_Employer3p` | TField |  | Field to indicate the Employer name of the Third party.Based on the Customer in THIRD.PARTY.CIF field, value to be defaulted from CUSTOMER>EMPLOYER.NAMEFree Form Alpha/Numeric Field |
| 135 | `CAMB.AML.SIGNER1.3P` | `CambAmlLog_Signer13p` | TField |  | Field to indicate the signer details in Conductor form. Free text field. |
| 136 | `CAMB.AML.SIGNER2.3P` | `CambAmlLog_Signer23p` | TField |  | Field to indicate the signer details in Conductor form. Free text field. |
| 137 | `CAMB.AML.SIGNER3.3P` | `CambAmlLog_Signer33p` | TField |  | Field to indicate the signer details in Conductor form. Free text field. |
| 138 | `CAMB.AML.RESERVED.10` | `CambAmlLog_Reserved10` | TField |  |  |
| 139 | `CAMB.AML.RESERVED.9` | `CambAmlLog_Reserved9` | TField |  |  |
| 140 | `CAMB.AML.RESERVED.8` | `CambAmlLog_Reserved8` | TField |  |  |
| 141 | `CAMB.AML.RESERVED.7` | `CambAmlLog_Reserved7` | TField |  |  |
| 142 | `CAMB.AML.RESERVED.6` | `CambAmlLog_Reserved6` | TField |  |  |
| 143 | `CAMB.AML.RESERVED.5` | `CambAmlLog_Reserved5` | TField |  |  |
| 144 | `CAMB.AML.RESERVED.4` | `CambAmlLog_Reserved4` | TField |  |  |
| 145 | `CAMB.AML.RESERVED.3` | `CambAmlLog_Reserved3` | TField |  |  |
| 146 | `CAMB.AML.RESERVED.2` | `CambAmlLog_Reserved2` | TField |  |  |
| 147 | `CAMB.AML.RESERVED.1` | `CambAmlLog_Reserved1` | TField |  |  |
| 148 | `CAMB.AML.LOCAL.REF` | `CambAmlLog_LocalRef` |  |  |  |
| 149 | `CAMB.AML.RECORD.STATUS` | `CambAmlLog_RecordStatus` | String |  |  |
| 150 | `CAMB.AML.CURR.NO` | `CambAmlLog_CurrNo` | String |  |  |
| 151 | `CAMB.AML.INPUTTER` | `CambAmlLog_Inputter` |  |  |  |
| 152 | `CAMB.AML.DATE.TIME` | `CambAmlLog_DateTime` |  |  |  |
| 153 | `CAMB.AML.AUTHORISER` | `CambAmlLog_Authoriser` | String |  |  |
| 154 | `CAMB.AML.CO.CODE` | `CambAmlLog_CoCode` | String |  |  |
| 155 | `CAMB.AML.DEPT.CODE` | `CambAmlLog_DeptCode` | String |  |  |
| 156 | `CAMB.AML.AUDITOR.CODE` | `CambAmlLog_AuditorCode` | String |  |  |
| 157 | `CAMB.AML.AUDIT.DATE.TIME` | `CambAmlLog_AuditDateTime` | String |  |  |
