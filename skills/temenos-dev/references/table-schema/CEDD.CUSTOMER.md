# CEDD.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.CEDD.CUSTOMER` in `USREGS_CEDD.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.KYC.POLITIC.EXPOSED` | `CeddCustomer_PoliticExposed` | TField | No | This field is used to indicate whether the customer is a politically Exposed person or not. Validation Rule: It is a Standard T24 Dropdown Button field, Optional Field and Text Field. |
| 2 | `US.KYC.POLITIC.POSITION` | `CeddCustomer_PoliticPosition` | TField | Yes | This field shows political position of politically exposed person. Validation Rule: Text Field, This field is mandatory if the field POLITIC.EXPOSED Person is Yes. Maximum 35 Alphanumeric Character. |
| 3 | `US.KYC.POLITICAL` | `CeddCustomer_Political` | TField |  |  |
| 4 | `US.KYC.POLITIC.TITLE` | `CeddCustomer_PoliticTitle` | TField | Yes | Shows the political position of the customer. This is mandatory if the field POLITICAL = 'Yes' or else no input field. Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 5 | `US.KYC.POLITIC.CNTY` | `CeddCustomer_PoliticCnty` | TField | Yes | Shows the political country of the customer. This field is mandatory field if the field is POLITICAL = 'Yes' or else no input field. Validation Rule: Dropdown Field. Dropdown will show values COUNTRY table. |
| 6 | `US.KYC.SR.POLITICAL` | `CeddCustomer_SrPolitical` | TField | No | This field is used to indicate whether the customer is a senior political official or not Validation Rule: It is a Standard T24 Dropdown Button field with values �Yes� and �No�, Optional Field. |
| 7 | `US.KYC.PARTY.NAME` | `CeddCustomer_PartyName` | TField | Yes | Shows the Name of the political party which customer is a senior official at. This is mandatory if the field SR.POLITICAL = 'Yes' or else no input field. Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 8 | `US.KYC.PARTY.CNTY` | `CeddCustomer_PartyCnty` | TField | Yes | Shows the country name of the political party. This field is mandatory field if the field SR.POLITICAL = 'Yes' or else no input field. Validation Rule: Dropdown Field: Dropdown will show values COUNTRY table. |
| 9 | `US.KYC.SR.EXECUTIVE` | `CeddCustomer_SrExecutive` | TField | No | This field is used to indicate whether the customer is a senior executive of the government owned corporation or not Validation Rule: It is a Standard T24 Dropdown Button field with values �Yes� and �No�, Optional Field. |
| 10 | `US.KYC.CORP.NAME` | `CeddCustomer_CorpName` | TField | Yes | It shows the name of the government owned corporation, where the customer is a senior executive. This field is mandatory if the field SR.EXECUTIVE = 'Yes' or else this is no input field Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 11 | `US.KYC.CORP.CNTY` | `CeddCustomer_CorpCnty` | TField | Yes | Shows the country name of the government owned corporation. This field is mandatory field if the field SR.EXECUTIVE = 'Yes' or else this is no input field. Validation Rule: Dropdown Field. Dropdown will show values from COUNTRY table. |
| 12 | `US.KYC.POLITIC.RELATIVE` | `CeddCustomer_PoliticRelative` | TField | No | This field is used to indicate whether the senior politically exposed person whom customer is related to or not Validation Rule: It is a Standard T24 Dropdown Button field with values �Yes� and �No�, Optional Field. |
| 13 | `US.KYC.POLITIC.REL.NAME` | `CeddCustomer_PoliticRelName` | TField | Yes | Shows name of the senior politically exposed person whom customer is related to. This is mandatory if the field POLITIC.RELATIVE = 'Yes' or else no input field. Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 14 | `US.KYC.POLITIC.REL.CNTY` | `CeddCustomer_PoliticRelCnty` | TField | Yes | Shows the country name of the senior political person to whom the customer is related. This is mandatory if the field POLITIC.RELATIVE = 'Yes' or else no input field Validation Rule: Dropdown Field Dropdown will show values COUNTRY table. |
| 15 | `US.KYC.POLITIC.ASSOCIATE` | `CeddCustomer_PoliticAssociate` | TField |  |  |
| 16 | `US.KYC.POLITIC.ASSOC.NAME` | `CeddCustomer_PoliticAssocName` | TField | Yes | Shows the name of the senior political Person with whom the customer has a close association. This is mandatory if the field POLITIC.ASSOCIATE = 'Yes' or else no input field. Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 17 | `US.KYC.POLITIC.ASSOC.CNTY` | `CeddCustomer_PoliticAssocCnty` | TField | Yes | Shows the country to which the senior political person is associated with. This is mandatory if the field POLITIC.ASSOCIATE = 'Yes' or else no input field. Validation Rule: Dropdown Field. Dropdown will show values COUNTRY table. |
| 18 | `US.KYC.POLITIC.ASSOC.REL` | `CeddCustomer_PoliticAssocRel` | TField | Yes | Describes the relationship of the customer with the senior political person. This is mandatory if the field POLITIC.ASSOCIATE = Yes or else no input. Validation Rule: Text Field. Maximum 15 Alphanumeric Character. |
| 19 | `US.KYC.POLITIC.CORP` | `CeddCustomer_PoliticCorp` | TField |  |  |
| 20 | `US.KYC.POLITIC.PERSN.NAME` | `CeddCustomer_PoliticPersnName` | TField | Yes | Name of politically exposed person who is associated with business/ corporation, This is mandatory if the field POLITIC.CORP = 'Yes' or else No input field. Validation Rule: Text Field, Maximum 35 Alphanumeric Character. |
| 21 | `US.KYC.POLITIC.PERSN.CNTY` | `CeddCustomer_PoliticPersnCnty` | TField | Yes | Country of politically exposed person who is associated with business/corporation. This is mandatory if the field POLITIC.CORP = 'Yes' or else no input field. Validation Rule: Dropdown Field. Dropdown will show values COUNTRY table. |
| 22 | `US.KYC.OWNERSHIP.PERCENT` | `CeddCustomer_OwnershipPercent` | TField | Yes | Shows the political person�s percentage of ownership in the associated corporation or business. This is mandatory if the field POLITIC.CORP = 'Yes' or else no input field. Validation Rule:Text Field, Max 3 numeric characters, should be equal to or less than 100. |
| 23 | `US.KYC.FCY.CORP` | `CeddCustomer_FcyCorp` | TField |  |  |
| 24 | `US.KYC.FCY.CNTY` | `CeddCustomer_FcyCnty` | TField | Yes | Shows the foreign country where the politically exposed person owns a corporation (fully or partially). This field is mandatory if field FCY.CORP= �Yes�, otherwise it is no input field. Validation Rule: Dropdown Field. Dropdown will show values from COUNTRY table |
| 25 | `US.KYC.FCY.MINISTRY` | `CeddCustomer_FcyMinistry` | TField | Yes | Shows the name of the particular ministry. This field is mandatory field if the field FCY.CORP = 'Yes' or else no input field. Validation Rule: Text Field, Maximum 20 Alphanumeric Character |
| 26 | `US.KYC.FCY.DEPT` | `CeddCustomer_FcyDept` | TField | Yes | Shows the name of department of the foreign ministry. This field is mandatory field if the field FCY.CORP = 'Yes' or else no input field. Validation Rule: Text Field. |
| 27 | `US.KYC.ACCOUNT.TYPES` | `CeddCustomer_AccountTypes` |  |  |  |
| 28 | `US.KYC.ACCOUNT.OTHER` | `CeddCustomer_AccountOther` |  |  |  |
| 29 | `US.KYC.ACCOUNT.SIZE` | `CeddCustomer_AccountSize` |  |  |  |
| 30 | `US.KYC.TRANS.PER.MTH` | `CeddCustomer_TransPerMth` |  |  |  |
| 31 | `US.KYC.COMMENTS` | `CeddCustomer_Comments` | TField | No | It shows any additional comments to be added. Optional Field. Validation Rule: Text Field. Maximum 35 Alphanumeric Character |
| 32 | `US.KYC.IN.CRS.BRD.WIRE` | `CeddCustomer_InCrsBrdWire` | TField | No | Shows whether the customer expects to be involved in any cross border transfers. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 33 | `US.KYC.IN.CRS.BRDR.NO` | `CeddCustomer_InCrsBrdrNo` |  |  |  |
| 34 | `US.KYC.IN.CRS.BRDR.AMT` | `CeddCustomer_InCrsBrdrAmt` |  |  |  |
| 35 | `US.KYC.IN.CRS.BRDR.CNTY` | `CeddCustomer_InCrsBrdrCnty` |  |  |  |
| 36 | `US.KYC.OUT.CRS.BRD.WIRE` | `CeddCustomer_OutCrsBrdWire` | TField | No | It shows whether the customer expects to do Outgoing cross border activities. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 37 | `US.KYC.OUT.CRS.BRD.NO` | `CeddCustomer_OutCrsBrdNo` |  |  |  |
| 38 | `US.KYC.OUT.CRS.BRD.AMT` | `CeddCustomer_OutCrsBrdAmt` |  |  |  |
| 39 | `US.KYC.OUT.CRS.BRD.CNTY` | `CeddCustomer_OutCrsBrdCnty` |  |  |  |
| 40 | `US.KYC.CASH.TRANS` | `CeddCustomer_CashTrans` | TField | No | It shows whether the customer expects to perform cash transactions. Validation Rule: Optional Field. Dropdown Field Dropdown Button values are 'Yes' and 'No' |
| 41 | `US.KYC.CASH.TRANS.PER.MTH` | `CeddCustomer_CashTransPerMth` | TField | Yes | Anticipated number of cash transactions per month Validation Rule: Text Field. Max 4 numeric characters Mandatory field if the field CASH.TRANS = 'Yes'. No input field if the field CASH.TRANS = 'No'. |
| 42 | `US.KYC.CASH.TRANS.AMT` | `CeddCustomer_CashTransAmt` | TField | Yes | Anticipated amount per cash transaction Validation Rule: Text Field Standard T24 AMOUNT field. Mandatory field if the field CASH.TRANS = 'Yes'. No input field if the field CASH.TRANS = 'No'. |
| 43 | `US.KYC.INT.ACH.TRANS` | `CeddCustomer_IntAchTrans` | TField | No | It shows whether customer anticipates conducting international ACH transactions. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 44 | `US.KYC.INT.ACH.TRANS.NO` | `CeddCustomer_IntAchTransNo` | TField | Yes | Number of transactions per month for International ACH transactions. Validation Rule: Text Field. Max 4 numeric characters Mandatory if the field INT.ACH.TRANS = 'Yes' or else no input field. |
| 45 | `US.KYC.INT.ACH.TRANS.AMT` | `CeddCustomer_IntAchTransAmt` | TField | Yes | Amount of transactions per month for International ACH transactions. Validation Rule: Text Field. Standard T24 AMOUNT field. Mandatory if the field INT.ACH.TRANS = 'Yes' or else no input field. |
| 46 | `US.KYC.INSTRUMENTS` | `CeddCustomer_Instruments` | TField | No | Shows whether the customer expects to conduct transactions in monetary instruments. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 47 | `US.KYC.INSTRUMENTS.NO` | `CeddCustomer_InstrumentsNo` | TField | Yes | Number of transactions per month for Monetary Instruments. Validation Rule: Text Field. Max 4 numeric characters. Mandatory if the field INSTRUMENTS = 'Yes' or else no input field. |
| 48 | `US.KYC.INSTRUMENTS.AMT` | `CeddCustomer_InstrumentsAmt` | TField | Yes | Transaction amount on monetary instrument Validation Rule: Standard T24 AMOUNT field. Mandatory if the field INSTRUMENTS = 'Yes' or else no input field. |
| 49 | `US.KYC.TRADE.FINANCE` | `CeddCustomer_TradeFinance` | TField | No | It shows whether customer expects any trade finance activity. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 50 | `US.KYC.CASH.COLL.LOANS` | `CeddCustomer_CashCollLoans` | TField | No | It shows whether the customer expects to do cash or marketable securities collateralized loans. Validation Rule: Optional Field. Dropdown Field. Dropdown Button values are 'Yes' and 'No'. |
| 51 | `US.KYC.KYC.EXEMPT` | `CeddCustomer_KycExempt` | TField | Yes | This field is used to indicate whether the customer is exempt from KYC process or not. Mandatory Field. Validation Rule: Dropdown Field. Dropdown values are 'Yes' and 'No'. |
| 52 | `US.KYC.KYC.EXEMPT.REASON` | `CeddCustomer_KycExemptReason` | TField | Yes | This field is used to indicate the reason for customer being exempt from KYC process. Validation Rule: Mandatory if the field KYC.EXEMPT = 'Yes'. Dropdown Field. The dropdown values are from EB.LOOKUP 1 customer was acquired through a business combination (merger or acquisition). 2 customer's only account with the institution was opened for the purpose of participating in an employee benefit plan established under ERISA. 3 customer is a financial institution. 4 customer is a government agency. 5 customer is a publicly-held company. |
| 53 | `US.KYC.EXMPT.REV.DATE` | `CeddCustomer_ExmptRevDate` | TField | Yes | This field is used to indicate the date when customer exemption was reviewed last time. Validation Rule: Mandatory field if the field KYC.EXEMPT = 'Yes'. Date Field. Standard T24 Date Field. |
| 54 | `US.KYC.RESERVED.10` | `CeddCustomer_Reserved10` | TField |  |  |
| 55 | `US.KYC.RESERVED.9` | `CeddCustomer_Reserved9` | TField |  |  |
| 56 | `US.KYC.RESERVED.8` | `CeddCustomer_Reserved8` | TField |  |  |
| 57 | `US.KYC.RESERVED.7` | `CeddCustomer_Reserved7` | TField |  |  |
| 58 | `US.KYC.RESERVED.6` | `CeddCustomer_Reserved6` | TField |  |  |
| 59 | `US.KYC.RESERVED.5` | `CeddCustomer_Reserved5` | TField |  |  |
| 60 | `US.KYC.RESERVED.4` | `CeddCustomer_Reserved4` | TField |  |  |
| 61 | `US.KYC.RESERVED.3` | `CeddCustomer_Reserved3` | TField |  |  |
| 62 | `US.KYC.RESERVED.2` | `CeddCustomer_Reserved2` | TField |  |  |
| 63 | `US.KYC.RESERVED.1` | `CeddCustomer_Reserved1` | TField |  |  |
| 64 | `US.KYC.OVERRIDE` | `CeddCustomer_Override` |  |  |  |
| 65 | `US.KYC.RECORD.STATUS` | `CeddCustomer_RecordStatus` | String |  |  |
| 66 | `US.KYC.CURR.NO` | `CeddCustomer_CurrNo` | String |  |  |
| 67 | `US.KYC.INPUTTER` | `CeddCustomer_Inputter` |  |  |  |
| 68 | `US.KYC.DATE.TIME` | `CeddCustomer_DateTime` |  |  |  |
| 69 | `US.KYC.AUTHORISER` | `CeddCustomer_Authoriser` | String |  |  |
| 70 | `US.KYC.CO.CODE` | `CeddCustomer_CoCode` | String |  |  |
| 71 | `US.KYC.DEPT.CODE` | `CeddCustomer_DeptCode` | String |  |  |
| 72 | `US.KYC.AUDITOR.CODE` | `CeddCustomer_AuditorCode` | String |  |  |
| 73 | `US.KYC.AUDIT.DATE.TIME` | `CeddCustomer_AuditDateTime` | String |  |  |
