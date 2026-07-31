# USREGS.CTR.EXCEED — Table Schema

> Source: `INSERTS/I_F.USREGS.CTR.EXCEED` in `USREGS_CTR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CTR.FILING.TYPE` | `UsregsCtrExceed_FilingType` | TField |  | This field shows the type of filing. Required values: a.Initial report b.Correct/Amend Prior Report c.FinCEN Directed Backfile |
| 2 | `CTR.MULT.TXN` | `UsregsCtrExceed_MultTxn` | TField |  | Multiple transactions (indicator).This element declares that multiple cash in or cash out transactions of any amount were conducted in a single business day by or for party. It will allow 'Y' - Yes or Null values |
| 3 | `CTR.PERSON.TYPE` | `UsregsCtrExceed_PersonType` |  |  |  |
| 4 | `CTR.ENTITY` | `UsregsCtrExceed_Entity` |  |  |  |
| 5 | `CTR.INT.LAST.ENT.LEGAL.NAME` | `UsregsCtrExceed_IntLastEntLegalName` |  |  |  |
| 6 | `CTR.INT.LAST.UNKNOWN` | `UsregsCtrExceed_IntLastUnknown` |  |  |  |
| 7 | `CTR.FIRST.NAME` | `UsregsCtrExceed_FirstName` |  |  |  |
| 8 | `CTR.FN.UNKNOWN` | `UsregsCtrExceed_FnUnknown` |  |  |  |
| 9 | `CTR.ALTERNATE.NAME` | `UsregsCtrExceed_AlternateName` |  |  |  |
| 10 | `CTR.ADDRESS.LINES` | `UsregsCtrExceed_AddressLines` |  |  |  |
| 11 | `CTR.ADDR.UNKNOWN` | `UsregsCtrExceed_AddrUnknown` |  |  |  |
| 12 | `CTR.CITY` | `UsregsCtrExceed_City` |  |  |  |
| 13 | `CTR.CITY.UNKNOWN` | `UsregsCtrExceed_CityUnknown` |  |  |  |
| 14 | `CTR.STATE` | `UsregsCtrExceed_State` |  |  |  |
| 15 | `CTR.STATE.UNKNOWN` | `UsregsCtrExceed_StateUnknown` |  |  |  |
| 16 | `CTR.ZIP.CODE` | `UsregsCtrExceed_ZipCode` |  |  |  |
| 17 | `CTR.ZIP.UNKNOWN` | `UsregsCtrExceed_ZipUnknown` |  |  |  |
| 18 | `CTR.COUNTRY` | `UsregsCtrExceed_Country` |  |  |  |
| 19 | `CTR.COUNTRY.UNKNOWN` | `UsregsCtrExceed_CountryUnknown` |  |  |  |
| 20 | `CTR.TIN` | `UsregsCtrExceed_Tin` |  |  |  |
| 21 | `CTR.TIN.UNKNOWN` | `UsregsCtrExceed_TinUnknown` |  |  |  |
| 22 | `CTR.TIN.TYPE` | `UsregsCtrExceed_TinType` |  |  |  |
| 23 | `CTR.DATE.OF.BIRTH` | `UsregsCtrExceed_DateOfBirth` |  |  |  |
| 24 | `CTR.DOB.UNKNOWN` | `UsregsCtrExceed_DobUnknown` |  |  |  |
| 25 | `CTR.FORM.ID` | `UsregsCtrExceed_FormId` |  |  |  |
| 26 | `CTR.FORM.UNKNOWN` | `UsregsCtrExceed_FormUnknown` |  |  |  |
| 27 | `CTR.OTHER.PARTY.ID` | `UsregsCtrExceed_OtherPartyId` |  |  |  |
| 28 | `CTR.ID.NUMBER` | `UsregsCtrExceed_IdNumber` |  |  |  |
| 29 | `CTR.ID.ISS.COUNTRY` | `UsregsCtrExceed_IdIssCountry` |  |  |  |
| 30 | `CTR.ID.ISS.STATE` | `UsregsCtrExceed_IdIssState` |  |  |  |
| 31 | `CTR.ACCOUNT.NUMBER` | `UsregsCtrExceed_AccountNumber` |  |  |  |
| 32 | `CTR.ACCOUNT.ASSOCIATE` | `UsregsCtrExceed_AccountAssociate` |  |  |  |
| 33 | `CTR.DATE.OF.TXN` | `UsregsCtrExceed_DateOfTxn` | TField |  | For institutions which use T24 Teller it will be defaulted with the the same date as the date in the ID of USREGS.CTR.EXCEED record for the customer. |
| 34 | `CTR.TRANS.TYPE` | `UsregsCtrExceed_TransType` | TField |  | Field not in use |
| 35 | `CTR.TOT.CASH.IN.USD` | `UsregsCtrExceed_TotCashInUsd` | TField |  | Required field. It must be recorded. Numeric amount field, allowing 1-15 numeric characters. It has to be an amount higher that $10,000.00. It will be defaulted from USREGS.CTR.DETAILS>IN.TOTAL.AMT field. If user manually amends this value, upon commitment of the record, system will generate override message: Total Cash In different than recorded sum of Teller transactions New amount will need to be updated manually in USREGS.CTR.DETAILS>IN.TOTAL.AMT field. |
| 36 | `CTR.TOT.CASH.OUT.USD` | `UsregsCtrExceed_TotCashOutUsd` | TField |  | Required field. It must be recorded. Numeric amount field, allowing 1-15 numeric characters. It has to be an amount higher that $10,000.00. It will be defaulted from USREGS.CTR.DETAILS>OUT.TOTAL.AMT field. If user manually amends this value, upon commitment of the record, system will generate override message: Total Cash Out different than recorded sum of Teller transactions New amount will need to be updated manually in USREGS.CTR.DETAILS>OUT.TOTAL.AMT field. |
| 37 | `CTR.FOREIGN.CASH.IN` | `UsregsCtrExceed_ForeignCashIn` |  |  |  |
| 38 | `CTR.FORGN.COUNTRY.CASH.IN` | `UsregsCtrExceed_ForgnCountryCashIn` |  |  |  |
| 39 | `CTR.FOREIGN.CASH.OUT` | `UsregsCtrExceed_ForeignCashOut` |  |  |  |
| 40 | `CTR.FORGN.COUNTRY.CASH.OUT` | `UsregsCtrExceed_ForgnCountryCashOut` |  |  |  |
| 41 | `CTR.TYPE.OF.FIN.INSTITUTE` | `UsregsCtrExceed_TypeOfFinInstitute` | TField |  | Conditionally Required field. Type of financial institution field will have a dropdown list with one element: 2 - Depository Institution |
| 42 | `CTR.PRIMARY.FED.REG` | `UsregsCtrExceed_PrimaryFedReg` | TField |  | Required field. Primary Federal regulator will have a dropdown list with the following values: 1 � Federal Reserve Board (FRB) 2 � Federal Deposit Insurance Corporation (FDIC) 3 � National Credit Union Administration (NCUA) 4 � Office of the Comptroller of the Currency (OCC) |
| 43 | `CTR.LEGAL.NAME.FIN.INST` | `UsregsCtrExceed_LegalNameFinInst` | TField |  | Text field allowing 1-150 characters. Legal Name of Financial Institution will be defaulted with the value from main company COMPANY>COMPANY.NAME. If user changes this value, upon commitment of the record system will generate override message: Legal Name of Financial Institution is different than main company name |
| 44 | `CTR.INST.ALTERNATE.NAME` | `UsregsCtrExceed_InstAlternateName` | TField |  | Conditionally Required field. Text field allowing 1-150 characters. It cannot have the same value as Legal Name of Financial Institution. |
| 45 | `CTR.INST.EIN` | `UsregsCtrExceed_InstEin` | TField |  | Required field Numeric field 1-9 characters. EIN field will be defaulted with the value stored in USCORE.COMPANY>TAX.ID for the main company. If amended by the user system will generate override message: EIN different than stored for the main company |
| 46 | `CTR.INST.ADDRESS` | `UsregsCtrExceed_InstAddress` |  |  |  |
| 47 | `CTR.INST.CITY` | `UsregsCtrExceed_InstCity` | TField |  | Required field Text field allowing 1-50 characters City field will be defaulted with the value stored in USCORE.COMPANY>INCORP.CITY for the main company. |
| 48 | `CTR.INST.STATE` | `UsregsCtrExceed_InstState` | TField |  | Required field Text field with the attached dropdown listing all the states as defined in US.STATE table. State field will be defaulted with the value stored in USCORE.COMPANY>INCORP.STATE for the main company. |
| 49 | `CTR.INST.ZIP.CODE` | `UsregsCtrExceed_InstZipCode` | TField |  | Required field Numeric field allowing 1-9 characters. Zip code field will be defaulted with the value stored in USCORE.COMPANY>ZIP and USCORE.COMPANY>ZIP4 for the main company. |
| 50 | `CTR.INST.COUNTRY` | `UsregsCtrExceed_InstCountry` | TField |  | Required field. Text field, with the dropdown of all country codes as defined in COUNTRY table. |
| 51 | `CTR.INST.CASH.IN.AMOUNT` | `UsregsCtrExceed_InstCashInAmount` | TField |  | Required field. Numeric amount field, allowing 1-15 numeric characters. It will be defaulted from USREGS.CTR.DETAILS>IN.TOTAL.AMT field. If user manually amends this value, upon commitment of the record, system will generate override message: Total Cash In different than recorded sum of Teller transactions New amount need to be updated manually in USREGS.CTR.DETAILS>IN.TOTAL.AMT field. |
| 52 | `CTR.INST.CASH.OUT.AMOUNT` | `UsregsCtrExceed_InstCashOutAmount` | TField |  | Required field. Numeric amount field, allowing 1-15 numeric characters. It has to be an amount higher that $10,000.00. It will be defaulted from USREGS.CTR.DETAILS>IN.TOTAL.AMT field. |
| 53 | `CTR.INST.CONTACT.OFFICE` | `UsregsCtrExceed_InstContactOffice` | TField |  | Required field. Text field allowing 1-150 characters. Contact office will be defaulted with the value from new table CTR.INSTITUTIO.PARAM field Contact office for main company. If user manually amends this value then on commitment of the record system will generate override message: Contact office details do not match details recorded for main company. |
| 54 | `CTR.INST.PHONE` | `UsregsCtrExceed_InstPhone` | TField |  | Required field. 10 numeric characters; not all same digit, such as all 0 or all 9. The field will be defaulted with the value recorded in new table CTR.INSTITUTION.PARAM Phone field for the main company. |
| 55 | `CTR.INST.DATE.FIELD` | `UsregsCtrExceed_InstDateField` | TField |  | Required field. |
| 56 | `CTR.INST.EXTENSION` | `UsregsCtrExceed_InstExtension` | TField |  | Conditionally Required field. 1-6 numeric characters The field will be defaulted with the value recorded in new table CTR.INSTITUTION.PARAM in field � Ext. for the main company. If user manually amends this value then on commitment of the record system will generate override message: Ext. details do not match details recorded for main company. |
| 57 | `CTR.RESERVED.10` | `UsregsCtrExceed_Reserved10` | TField |  |  |
| 58 | `CTR.RESERVED.9` | `UsregsCtrExceed_Reserved9` | TField |  |  |
| 59 | `CTR.RESERVED.8` | `UsregsCtrExceed_Reserved8` | TField |  |  |
| 60 | `CTR.RESERVED.7` | `UsregsCtrExceed_Reserved7` | TField |  |  |
| 61 | `CTR.RESERVED.6` | `UsregsCtrExceed_Reserved6` | TField |  |  |
| 62 | `CTR.RESERVED.5` | `UsregsCtrExceed_Reserved5` | TField |  |  |
| 63 | `CTR.RESERVED.4` | `UsregsCtrExceed_Reserved4` | TField |  |  |
| 64 | `CTR.RESERVED.3` | `UsregsCtrExceed_Reserved3` | TField |  |  |
| 65 | `CTR.RESERVED.2` | `UsregsCtrExceed_Reserved2` | TField |  |  |
| 66 | `CTR.RESERVED.1` | `UsregsCtrExceed_Reserved1` | TField |  |  |
| 67 | `CTR.LOCAL.REF` | `UsregsCtrExceed_LocalRef` |  |  |  |
| 68 | `CTR.OVERRIDE` | `UsregsCtrExceed_Override` |  |  |  |
| 69 | `CTR.RECORD.STATUS` | `UsregsCtrExceed_RecordStatus` | String |  |  |
| 70 | `CTR.CURR.NO` | `UsregsCtrExceed_CurrNo` | String |  |  |
| 71 | `CTR.INPUTTER` | `UsregsCtrExceed_Inputter` |  |  |  |
| 72 | `CTR.DATE.TIME` | `UsregsCtrExceed_DateTime` |  |  |  |
| 73 | `CTR.AUTHORISER` | `UsregsCtrExceed_Authoriser` | String |  |  |
| 74 | `CTR.CO.CODE` | `UsregsCtrExceed_CoCode` | String |  |  |
| 75 | `CTR.DEPT.CODE` | `UsregsCtrExceed_DeptCode` | String |  |  |
| 76 | `CTR.AUDITOR.CODE` | `UsregsCtrExceed_AuditorCode` | String |  |  |
| 77 | `CTR.AUDIT.DATE.TIME` | `UsregsCtrExceed_AuditDateTime` | String |  |  |
