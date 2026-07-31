# USREGS.IRS.FORM.DATA — Table Schema

> Source: `INSERTS/I_F.USREGS.IRS.FORM.DATA` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FORM.DATA.T.TRANSMIT.TIN` | `UsregsIrsFormData_TTransmitTin` | TField |  |  |
| 2 | `FORM.DATA.T.TRANSMIT.CODE` | `UsregsIrsFormData_TTransmitCode` | TField | Yes | Shows the five-character alphanumeric Transmitter Control Code (TCC) assigned by IRS. Mandatory field. Max 5 alphanumeric character |
| 3 | `FORM.DATA.T.TEST.FILE.IND` | `UsregsIrsFormData_TTestFileInd` | TField |  | This field is required for test files only. Enter a �T� if this is a test file; otherwise leave it blank. Radio button with values T and None. Default value is None. Max 1 Numeric character |
| 4 | `FORM.DATA.T.FGN.ENTITY.IND` | `UsregsIrsFormData_TFgnEntityInd` | TField |  | Shows whether the transmitter is a foreign entity or not. Enter a �1� if the transmitter is a foreign entity. If not leave it blank. Radio button with values 1 and None. Default value is none. |
| 5 | `FORM.DATA.T.TRANSMIT.NAME.1` | `UsregsIrsFormData_TTransmitName1` | TField |  |  |
| 6 | `FORM.DATA.T.TRANSMIT.NAME.2` | `UsregsIrsFormData_TTransmitName2` | TField |  |  |
| 7 | `FORM.DATA.T.COMPANY.NAME.1` | `UsregsIrsFormData_TCompanyName1` | TField | Yes | The name of the company associated with the address where correspondence should be sent. Mandatory field. 40 Alpha numeric characters |
| 8 | `FORM.DATA.T.COMPANY.NAME.2` | `UsregsIrsFormData_TCompanyName2` | TField |  | Shows any additional information that may be part of the name of the company where correspondence should be sent. 40 Alpha numeric characters |
| 9 | `FORM.DATA.T.COMPANY.ADDR` | `UsregsIrsFormData_TCompanyAddr` | TField | Yes | Displays the mailing address where the correspondence should be sent. Mandatory field. 40 Alpha numeric characters |
| 10 | `FORM.DATA.T.COMPANY.CITY` | `UsregsIrsFormData_TCompanyCity` | TField | Yes | City name of the company address Mandatory field 40 Alpha numeric characters |
| 11 | `FORM.DATA.T.COMPANY.STATE` | `UsregsIrsFormData_TCompanyState` | TField | Yes | Shows the state name of the company�s correspondence Drop down US.STATE>@ID Mandatory field if T.COUNTRY.CODE is blank If not entered, throw the error message 'State code is mandatory if there is no country code' |
| 12 | `FORM.DATA.T.COMP.ZIP.CODE` | `UsregsIrsFormData_TCompZipCode` | TField | Yes | The postal code of the company�s correspondence address Enter the valid nine digit zip assigned by the U.S. postal service. Mandatory field. Max 9 Numeric character |
| 13 | `FORM.DATA.T.PROVINCE.CODE` | `UsregsIrsFormData_TProvinceCode` | TField |  | Shows the province code Max 2 alphanumeric character |
| 14 | `FORM.DATA.T.COUNTRY.CODE` | `UsregsIrsFormData_TCountryCode` | TField |  | Shows the country code for foreign transmitter Max 2 alphanumeric character |
| 15 | `FORM.DATA.T.CONTACT.NAME` | `UsregsIrsFormData_TContactName` | TField | Yes | Enter the name of the person to be contacted if IRS encounters problems with the file or transmission. Mandatory field. Max 40 alphanumeric character |
| 16 | `FORM.DATA.T.CONTACT.PH.NO` | `UsregsIrsFormData_TContactPhNo` | TField | Yes | Shows the telephone number of the person to contact. Mandatory field. Max 15 alphanumeric character |
| 17 | `FORM.DATA.T.CONTACT.EMAIL` | `UsregsIrsFormData_TContactEmail` | TField | Yes | Shows the email address of the person to contact regarding the electronic or magnetic files. Mandatory field. Max 50 alphanumeric characters. |
| 18 | `FORM.DATA.T.VENDOR.IND` | `UsregsIrsFormData_TVendorInd` | TField |  | Indicates if the software used to produce this file was provided by a vendor or produced in house Radio button with options �V� and �I�. V � Your software was purchased from a vendor or other source. I � Your software was produced by in house programmers. Default option is I |
| 19 | `FORM.DATA.T.VENDOR.NAME` | `UsregsIrsFormData_TVendorName` | TField | No | The name of the company from whom the software was purchase. Optional field, Max 40 alphanumeric characters. If the software is produced in-house, leave blank. |
| 20 | `FORM.DATA.T.VENDOR.ADDR` | `UsregsIrsFormData_TVendorAddr` | TField | No | Shows the mailing address of vendor Optional field, Max 40 alphanumeric characters If the software is produced in-house, leave blank. |
| 21 | `FORM.DATA.T.VENDOR.CITY` | `UsregsIrsFormData_TVendorCity` | TField |  | Shows the city, town, or post office of vendor Max 40 alphanumeric characters. |
| 22 | `FORM.DATA.T.VENDOR.STATE` | `UsregsIrsFormData_TVendorState` | TField |  | Shows the valid U.S. Postal Service state abbreviation for vendor address. Max 2 alpha characters |
| 23 | `FORM.DATA.T.VENDOR.ZIP.CODE` | `UsregsIrsFormData_TVendorZipCode` | TField |  | Shows the valid nine digit ZIP code assigned by the U.S Postal service for the vendor address Max 9 numeric characters |
| 24 | `FORM.DATA.T.VEN.CONT.NAME` | `UsregsIrsFormData_TVenContName` | TField |  | The name of the person who can be contacted concerning any software questions. Max 40 alphanumeric characters. |
| 25 | `FORM.DATA.T.VENDOR.PH.NO` | `UsregsIrsFormData_TVendorPhNo` | TField |  | The telephone number of the person to contact concerning software questions. Max 15 numeric characters. |
| 26 | `FORM.DATA.T.VEN.FGN.ENT.IND` | `UsregsIrsFormData_TVenFgnEntInd` | TField |  | Indicates whether the vendor is a foreign entity or not Radio button with values 1 and None. Default value is 1.Enter a �1� if the vendor is a foreign entity. Otherwise leave it blank. |
| 27 | `FORM.DATA.A.STATE.FILER` | `UsregsIrsFormData_AStateFiler` | TField |  | Shows whether the filing Combined Federal/State Filer. Required for the combined federal / state filing program. Enter �1� if approved or submitting a test to participate in the combined federal / state filing program; otherwise leave it blank. Max 1 numeric character. |
| 28 | `FORM.DATA.A.TAXPAYER.ID` | `UsregsIrsFormData_ATaxpayerId` | TField | Yes | Shows the valid nine digit Tax payer Identification. Mandatory field., max 9 numeric characters. |
| 29 | `FORM.DATA.A.PAY.NAME.CTRL` | `UsregsIrsFormData_APayNameCtrl` | TField | No | Shows the four characters of the name control Optional field, Max 4 alphanumeric characters |
| 30 | `FORM.DATA.A.LAST.FILING.IND` | `UsregsIrsFormData_ALastFilingInd` | TField |  | Indicates whether the payer is filing information returns electronically last year or not Enter a �1� if this is the last year this payer name and TIN will file information returns, else leave it blank. Max 1 numeric character. |
| 31 | `FORM.DATA.A.FGN.ENTITY.IND` | `UsregsIrsFormData_AFgnEntityInd` | TField |  | Indicates whether the payer is a foreign entity or not Enter a �1� if the payer is a foreign entity and income is paid by foreign entity to a U.S. resident. Otherwise, leave it blank. Max 1 numeric character |
| 32 | `FORM.DATA.A.FIRST.PAYER.NAME` | `UsregsIrsFormData_AFirstPayerName` | TField | Yes | Displays the name of the payer whose TIN appears in the A record. Mandatory field. Max 40 alphanumeric characters. |
| 33 | `FORM.DATA.A.SEC.PAYER.NAME` | `UsregsIrsFormData_ASecPayerName` | TField | No | Indicates the name of the transfer or paying agent for the agent indicator contains a �1�. If the transfer agent indicator (field 52) contains a �1� then this field must contain the name of the transfer (or paying) agent. Optional field Max 40 alphanumeric characters |
| 34 | `FORM.DATA.A.TRF.AGENT.IND` | `UsregsIrsFormData_ATrfAgentInd` | TField | Yes | Indicates the whether the entity is the transfer agent or not Mandatory field. Can be either 1 or 0. 1 � The entity in the second payer name field is the transfer agent. 0 � The entity shown is not the transfer agent. Radio button with values 1 and 0. Default value is 1. |
| 35 | `FORM.DATA.A.PAY.SHIP.ADDR` | `UsregsIrsFormData_APayShipAddr` | TField | Yes | Shows the email address of the person to contact regarding the electronic or magnetic files. Mandatory field. If the transfer agent indicator is �1� then enter the shipping address of the transfer agent. Otherwise enter the actual shipping address of the payer. Max 40 alphanumeric characters |
| 36 | `FORM.DATA.A.PAYER.CITY` | `UsregsIrsFormData_APayerCity` | TField |  |  |
| 37 | `FORM.DATA.A.PAYER.STATE` | `UsregsIrsFormData_APayerState` | TField | Yes | Shows the state name of the transfer agent Mandatory field. Enter the valid U.S. Postal Service state abbreviations. Max 2 alpha characters |
| 38 | `FORM.DATA.A.PAY.ZIP.CODE` | `UsregsIrsFormData_APayZipCode` | TField | Yes | The valid nine digit ZIP code assigned by the U.S. Postal service. Mandatory field. Max 9 numeric characters |
| 39 | `FORM.DATA.A.PAYER.PH.NO` | `UsregsIrsFormData_APayerPhNo` | TField |  | Shows the payers phone number and extension Max 15 numeric characters. |
| 40 | `FORM.DATA.K.WITHELD.STAT.TAX` | `UsregsIrsFormData_KWitheldStatTax` | TField | No | Aggregate totals of the state income tax withheld field in the payee �B� records. Optional field AMOUNT field. Max 18 numeric characters |
| 41 | `FORM.DATA.K.WITHHELD.LOC.TAX` | `UsregsIrsFormData_KWithheldLocTax` | TField | No | Aggregate totals of the local income tax withheld field in the payee �B� records. Optional field AMOUNT field. Max 18 numeric characters |
| 42 | `FORM.DATA.W.WHLD.A.EIN` | `UsregsIrsFormData_WWhldAEin` | TField |  | Shows the Withholding Agent�s EIN Max 9 numeric characters |
| 43 | `FORM.DATA.W.WHLD.A.EIN.IND` | `UsregsIrsFormData_WWhldAEinInd` | TField |  | Shows withholding agents. EIN type Withholding Agent�s EIN Indicator Radio button 0 or 1 or 2 0 = EIN 1 = QI-EIN, WP-EIN, WT-EIN 2 = NQI-EIN Default value is �1�. |
| 44 | `FORM.DATA.W.WHLD.A.NAME1` | `UsregsIrsFormData_WWhldAName1` | TField |  | Displays Withholding Agent�s Name Line-1 Max 40 alphanumeric characters |
| 45 | `FORM.DATA.W.WHLD.A.NAME2` | `UsregsIrsFormData_WWhldAName2` | TField |  | Displays Withholding Agent�s Name Line-2 Max 40 alphanumeric characters |
| 46 | `FORM.DATA.W.WHLD.A.NAME3` | `UsregsIrsFormData_WWhldAName3` | TField |  | Displays Withholding Agent�s Name Line-3 Max 40 alphanumeric characters |
| 47 | `FORM.DATA.W.WHLD.A.STREET1` | `UsregsIrsFormData_WWhldAStreet1` | TField |  | Displays Withholding Agent�s Street Line-1 Max 40 alphanumeric characters |
| 48 | `FORM.DATA.W.WHLD.A.STREET2` | `UsregsIrsFormData_WWhldAStreet2` | TField |  | Displays Withholding Agent�s Street Line-2 Max 40 alphanumeric characters |
| 49 | `FORM.DATA.W.WHLD.A.CITY` | `UsregsIrsFormData_WWhldACity` | TField |  | Displays Withholding Agent�s City Max 40 alphanumeric characters |
| 50 | `FORM.DATA.W.WHLD.A.STATE` | `UsregsIrsFormData_WWhldAState` | TField |  | Shows Withholding Agent�s State Code Max 2 alpha characters |
| 51 | `FORM.DATA.W.WHLD.A.PROV` | `UsregsIrsFormData_WWhldAProv` | TField |  | Shows Withholding Agent�s Province Code Max 2 alpha characters |
| 52 | `FORM.DATA.W.WHLD.A.COUNTRY` | `UsregsIrsFormData_WWhldACountry` | TField |  | Shows Withholding Agent�s Country Code Max 2 alpha characters |
| 53 | `FORM.DATA.W.WHLD.A.POSTAL` | `UsregsIrsFormData_WWhldAPostal` | TField |  | Displays Postal or ZIP Code for withholding agent�s address Max 9 numeric characters |
| 54 | `FORM.DATA.W.WHLD.A.CONT.NAME` | `UsregsIrsFormData_WWhldAContName` | TField |  | Withholding Agent Contact Name Max 45 alphanumeric characters |
| 55 | `FORM.DATA.W.WHLD.A.CONT.DEPT` | `UsregsIrsFormData_WWhldAContDept` | TField |  | Withholding Agent�s Department Title Max 45 alphanumeric characters |
| 56 | `FORM.DATA.W.CONTACT.NO.EXT` | `UsregsIrsFormData_WContactNoExt` | TField |  | Contact Telephone Number and Extension Max 20 alphanumeric characters |
| 57 | `FORM.DATA.W.RETURN.TYPE.IND` | `UsregsIrsFormData_WReturnTypeInd` | TField |  | Return Type Indicator Radio button 0 or 1 Default value is 0 Max 1 numeric character |
| 58 | `FORM.DATA.W.PRORATA.BASIS` | `UsregsIrsFormData_WProrataBasis` | TField |  | Pro Rata Basis Reporting Radio button 0 or 1 Default value is 0 Max 1 numeric character |
| 59 | `FORM.DATA.W.WHLD.A.FTIN` | `UsregsIrsFormData_WWhldAFtin` | TField | No | Withholding Agent�s Foreign Tax Identification Number. Optional field Max 22 Alphanumeric field |
| 60 | `FORM.DATA.W.WHLD.CH.INDICATOR` | `UsregsIrsFormData_WWhldChIndicator` | TField |  |  |
| 61 | `FORM.DATA.W.WHLD.AGENT.GIIN` | `UsregsIrsFormData_WWhldAgentGiin` | TField |  | Withholding Agent�s GIIN. |
| 62 | `FORM.DATA.W.WHLD.AGENT.CH3.STATUS.CODE` | `UsregsIrsFormData_WWhldAgentCh3StatusCode` | TField | Yes | Withholding Agent�s Chapter 3 Status Code It will be a dropdown field including the entity type codes (same as in CUSTOMER application). Drop down will be from EB.LOOKUP TX.ENT.TYPE.CODE*. This field should be Mandatory. |
| 63 | `FORM.DATA.W.WHLD.AGENT.CH4.STATUS.CODE` | `UsregsIrsFormData_WWhldAgentCh4StatusCode` | TField | Yes | Withholding Agent�s Chapter 4 Status Code It will be a dropdown field including the FATCA status codes (same as in CUSTOMER application). Drop down will be from EB.LOOKUP FATCA.STATUS.CODE*. This field should be Mandatory. |
| 64 | `FORM.DATA.US.STATE` | `UsregsIrsFormData_UsState` |  |  |  |
| 65 | `FORM.DATA.WHLD.ACCT.NUMBER` | `UsregsIrsFormData_WhldAcctNumber` |  |  |  |
| 66 | `FORM.DATA.IRS.FILE.PATH` | `UsregsIrsFormData_IrsFilePath` | TField |  | The path where the IRS files have to be generated. It must be a valid path otherwise system will raise error message. |
| 67 | `FORM.DATA.RESERVED.9` | `UsregsIrsFormData_Reserved9` | TField |  |  |
| 68 | `FORM.DATA.RESERVED.10` | `UsregsIrsFormData_Reserved10` | TField |  |  |
| 69 | `FORM.DATA.RESERVED.11` | `UsregsIrsFormData_Reserved11` | TField |  |  |
| 70 | `FORM.DATA.RESERVED.12` | `UsregsIrsFormData_Reserved12` | TField |  |  |
| 71 | `FORM.DATA.RESERVED.13` | `UsregsIrsFormData_Reserved13` | TField |  |  |
| 72 | `FORM.DATA.RESERVED.14` | `UsregsIrsFormData_Reserved14` | TField |  |  |
| 73 | `FORM.DATA.RESERVED.15` | `UsregsIrsFormData_Reserved15` | TField |  |  |
| 74 | `FORM.DATA.RESERVED.16` | `UsregsIrsFormData_Reserved16` | TField |  |  |
| 75 | `FORM.DATA.RESERVED.17` | `UsregsIrsFormData_Reserved17` | TField |  |  |
| 76 | `FORM.DATA.RESERVED.18` | `UsregsIrsFormData_Reserved18` | TField |  |  |
| 77 | `FORM.DATA.RESERVED.19` | `UsregsIrsFormData_Reserved19` | TField |  |  |
| 78 | `FORM.DATA.RESERVED.20` | `UsregsIrsFormData_Reserved20` | TField |  |  |
| 79 | `FORM.DATA.LOCAL.REF` | `UsregsIrsFormData_LocalRef` |  |  |  |
| 80 | `FORM.DATA.OVERRIDE` | `UsregsIrsFormData_Override` |  |  |  |
| 81 | `FORM.DATA.RECORD.STATUS` | `UsregsIrsFormData_RecordStatus` | String |  |  |
| 82 | `FORM.DATA.CURR.NO` | `UsregsIrsFormData_CurrNo` | String |  |  |
| 83 | `FORM.DATA.INPUTTER` | `UsregsIrsFormData_Inputter` |  |  |  |
| 84 | `FORM.DATA.DATE.TIME` | `UsregsIrsFormData_DateTime` |  |  |  |
| 85 | `FORM.DATA.AUTHORISER` | `UsregsIrsFormData_Authoriser` | String |  |  |
| 86 | `FORM.DATA.CO.CODE` | `UsregsIrsFormData_CoCode` | String |  |  |
| 87 | `FORM.DATA.DEPT.CODE` | `UsregsIrsFormData_DeptCode` | String |  |  |
| 88 | `FORM.DATA.AUDITOR.CODE` | `UsregsIrsFormData_AuditorCode` | String |  |  |
| 89 | `FORM.DATA.AUDIT.DATE.TIME` | `UsregsIrsFormData_AuditDateTime` | String |  |  |
