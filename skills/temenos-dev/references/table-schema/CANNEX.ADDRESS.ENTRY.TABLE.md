# CANNEX.ADDRESS.ENTRY.TABLE — Table Schema

> Source: `INSERTS/I_F.CANNEX.ADDRESS.ENTRY.TABLE` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.ADDR.RECORD.TYPE` | `CannexAddressEntryTable_RecordType` |  |  |  |
| 2 | `CANNEX.ADDR.ADDRESS1` | `CannexAddressEntryTable_Address1` |  |  |  |
| 3 | `CANNEX.ADDR.ADDRESS2` | `CannexAddressEntryTable_Address2` |  |  |  |
| 4 | `CANNEX.ADDR.ADDRESS3` | `CannexAddressEntryTable_Address3` |  |  |  |
| 5 | `CANNEX.ADDR.ADDRESS4` | `CannexAddressEntryTable_Address4` |  |  |  |
| 6 | `CANNEX.ADDR.AGENT.REG.INFO` | `CannexAddressEntryTable_AgentRegInfo` |  |  |  |
| 7 | `CANNEX.ADDR.BIRTH.DATE` | `CannexAddressEntryTable_BirthDate` |  |  |  |
| 8 | `CANNEX.ADDR.CITY` | `CannexAddressEntryTable_City` |  |  |  |
| 9 | `CANNEX.ADDR.COUNTRY.NAME` | `CannexAddressEntryTable_CountryName` |  |  |  |
| 10 | `CANNEX.ADDR.DOCUMENT.NUMBER` | `CannexAddressEntryTable_DocumentNumber` |  |  |  |
| 11 | `CANNEX.ADDR.DOCUMENT.TYPE` | `CannexAddressEntryTable_DocumentType` |  |  |  |
| 12 | `CANNEX.ADDR.LANGUAGE` | `CannexAddressEntryTable_Language` |  |  |  |
| 13 | `CANNEX.ADDR.NAME.1` | `CannexAddressEntryTable_Name1` |  |  |  |
| 14 | `CANNEX.ADDR.NAME.2` | `CannexAddressEntryTable_Name2` |  |  |  |
| 15 | `CANNEX.ADDR.NAME.3` | `CannexAddressEntryTable_Name3` |  |  |  |
| 16 | `CANNEX.ADDR.NAME.TYPE` | `CannexAddressEntryTable_NameType` |  |  |  |
| 17 | `CANNEX.ADDR.OCCUPATION` | `CannexAddressEntryTable_Occupation` |  |  |  |
| 18 | `CANNEX.ADDR.PHONE.RES` | `CannexAddressEntryTable_PhoneRes` |  |  |  |
| 19 | `CANNEX.ADDR.PHONE.BUS` | `CannexAddressEntryTable_PhoneBus` |  |  |  |
| 20 | `CANNEX.ADDR.POSTAL.ZIP.CODE` | `CannexAddressEntryTable_PostalZipCode` |  |  |  |
| 21 | `CANNEX.ADDR.PROV.STATE.NAME` | `CannexAddressEntryTable_ProvStateName` |  |  |  |
| 22 | `CANNEX.ADDR.RECORD.CODE` | `CannexAddressEntryTable_RecordCode` |  |  |  |
| 23 | `CANNEX.ADDR.REFERENCE` | `CannexAddressEntryTable_Reference` |  |  |  |
| 24 | `CANNEX.ADDR.REVOCABLE` | `CannexAddressEntryTable_Revocable` |  |  |  |
| 25 | `CANNEX.ADDR.SHARE.PERCENT` | `CannexAddressEntryTable_SharePercent` |  |  |  |
| 26 | `CANNEX.ADDR.SIN.NUMBER` | `CannexAddressEntryTable_SinNumber` |  |  |  |
| 27 | `CANNEX.ADDR.SOURCE.REF.ID` | `CannexAddressEntryTable_SourceRefId` |  |  |  |
| 28 | `CANNEX.ADDR.TITLE` | `CannexAddressEntryTable_Title` |  |  |  |
| 29 | `CANNEX.ADDR.BUSINESS.TYPE` | `CannexAddressEntryTable_BusinessType` |  |  |  |
| 30 | `CANNEX.ADDR.CITIZENSHIP` | `CannexAddressEntryTable_Citizenship` |  |  |  |
| 31 | `CANNEX.ADDR.COUNTRY.INC` | `CannexAddressEntryTable_CountryInc` |  |  |  |
| 32 | `CANNEX.ADDR.DOCUMENT.COUNTRY` | `CannexAddressEntryTable_DocumentCountry` |  |  |  |
| 33 | `CANNEX.ADDR.DOCUMENT.CNTY2` | `CannexAddressEntryTable_DocumentCnty2` |  |  |  |
| 34 | `CANNEX.ADDR.DOCUMENT.DESC` | `CannexAddressEntryTable_DocumentDesc` |  |  |  |
| 35 | `CANNEX.ADDR.DOCUMENT.DESC2` | `CannexAddressEntryTable_DocumentDesc2` |  |  |  |
| 36 | `CANNEX.ADDR.DOCUMENT.EXPIRY` | `CannexAddressEntryTable_DocumentExpiry` |  |  |  |
| 37 | `CANNEX.ADDR.DOCUMENT.EXPIRY2` | `CannexAddressEntryTable_DocumentExpiry2` |  |  |  |
| 38 | `CANNEX.ADDR.DOCUMENT.NUMBER2` | `CannexAddressEntryTable_DocumentNumber2` |  |  |  |
| 39 | `CANNEX.ADDR.DOCUMENT.PROV.ST` | `CannexAddressEntryTable_DocumentProvSt` |  |  |  |
| 40 | `CANNEX.ADDR.DOCUMENT.PRV.ST2` | `CannexAddressEntryTable_DocumentPrvSt2` |  |  |  |
| 41 | `CANNEX.ADDR.DOCUMENT.TYPE2` | `CannexAddressEntryTable_DocumentType2` |  |  |  |
| 42 | `CANNEX.ADDR.EXPIRY.DATE` | `CannexAddressEntryTable_ExpiryDate` |  |  |  |
| 43 | `CANNEX.ADDR.MONTHS.AT.ADDR` | `CannexAddressEntryTable_MonthsAtAddr` |  |  |  |
| 44 | `CANNEX.ADDR.PHONE.FAX` | `CannexAddressEntryTable_PhoneFax` |  |  |  |
| 45 | `CANNEX.ADDR.PROV.STATE.INC` | `CannexAddressEntryTable_ProvStateInc` |  |  |  |
| 46 | `CANNEX.ADDR.YEARS.AT.ADDR` | `CannexAddressEntryTable_YearsAtAddr` |  |  |  |
| 47 | `CANNEX.ADDR.SHARE.AMOUNT` | `CannexAddressEntryTable_ShareAmount` |  |  |  |
| 48 | `CANNEX.ADDR.CFN.EVENT.NO` | `CannexAddressEntryTable_CfnEventNo` |  |  |  |
| 49 | `CANNEX.ADDR.LEI` | `CannexAddressEntryTable_Lei` | TField |  | This field is used to capture the Legal Entity Identifier (LEI) value |
| 50 | `CANNEX.ADDR.RESERVED.4` | `CannexAddressEntryTable_Reserved4` | TField |  |  |
| 51 | `CANNEX.ADDR.RESERVED.5` | `CannexAddressEntryTable_Reserved5` | TField |  |  |
| 52 | `CANNEX.ADDR.RESERVED.6` | `CannexAddressEntryTable_Reserved6` | TField |  |  |
| 53 | `CANNEX.ADDR.RESERVED.7` | `CannexAddressEntryTable_Reserved7` | TField |  |  |
| 54 | `CANNEX.ADDR.RESERVED.8` | `CannexAddressEntryTable_Reserved8` | TField |  |  |
| 55 | `CANNEX.ADDR.RESERVED.9` | `CannexAddressEntryTable_Reserved9` | TField |  |  |
| 56 | `CANNEX.ADDR.RESERVED.10` | `CannexAddressEntryTable_Reserved10` | TField |  |  |
| 57 | `CANNEX.ADDR.LOCAL.REF` | `CannexAddressEntryTable_LocalRef` |  |  |  |
| 58 | `CANNEX.ADDR.OVERRIDE` | `CannexAddressEntryTable_Override` |  |  |  |
| 59 | `CANNEX.ADDR.RECORD.STATUS` | `CannexAddressEntryTable_RecordStatus` | String |  |  |
| 60 | `CANNEX.ADDR.CURR.NO` | `CannexAddressEntryTable_CurrNo` | String |  |  |
| 61 | `CANNEX.ADDR.INPUTTER` | `CannexAddressEntryTable_Inputter` |  |  |  |
| 62 | `CANNEX.ADDR.DATE.TIME` | `CannexAddressEntryTable_DateTime` |  |  |  |
| 63 | `CANNEX.ADDR.AUTHORISER` | `CannexAddressEntryTable_Authoriser` | String |  |  |
| 64 | `CANNEX.ADDR.CO.CODE` | `CannexAddressEntryTable_CoCode` | String |  |  |
| 65 | `CANNEX.ADDR.DEPT.CODE` | `CannexAddressEntryTable_DeptCode` | String |  |  |
| 66 | `CANNEX.ADDR.AUDITOR.CODE` | `CannexAddressEntryTable_AuditorCode` | String |  |  |
| 67 | `CANNEX.ADDR.AUDIT.DATE.TIME` | `CannexAddressEntryTable_AuditDateTime` | String |  |  |
