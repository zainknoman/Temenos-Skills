# CBR.CONSUMER.DETAILS — Table Schema

> Source: `INSERTS/I_F.CBR.CONSUMER.DETAILS` in `FINEXT_CBR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBR.CUS.PRIMARY.CUSTOMER` | `CbrConsumerDetails_PrimaryCustomer` | TField |  | This field updated with the AA customer ID which is called base customer reference number for selected arrangement records. |
| 2 | `CBR.CUS.CON.TRAN.TYPE` | `CbrConsumerDetails_ConTranType` | TField |  |  |
| 3 | `CBR.CUS.SURNAME` | `CbrConsumerDetails_Surname` | TField |  | This field updated with base or primary customer's family from the field FAMILY.NAME. |
| 4 | `CBR.CUS.FIRST.NAME` | `CbrConsumerDetails_FirstName` | TField |  | This field updated with base or primary customer's first name from the field GIVEN.NAME. |
| 5 | `CBR.CUS.MIDDLE.NAME` | `CbrConsumerDetails_MiddleName` | TField |  | This field updated with base or primary customer's middle name from the field MIDDLE.NAME. |
| 6 | `CBR.CUS.SUFFIX.CODE` | `CbrConsumerDetails_SuffixCode` | TField |  | This field updated with base or primary customer's suffix title from the field SUFFIX. |
| 7 | `CBR.CUS.SSN` | `CbrConsumerDetails_Ssn` | TField |  | This field updated with base or primary customer's social security number from the field TAX.ID |
| 8 | `CBR.CUS.DATE.OF.BIRTH` | `CbrConsumerDetails_DateOfBirth` | TField |  | This field updated with base or primary customer's Date.of.Birth |
| 9 | `CBR.CUS.TELEPHONE.NO` | `CbrConsumerDetails_TelephoneNo` | TField |  |  |
| 10 | `CBR.CUS.ECOA.CODE` | `CbrConsumerDetails_EcoaCode` | TField |  | This field updated with base or primary customer's relation code. |
| 11 | `CBR.CUS.CI.INDICATOR` | `CbrConsumerDetails_CiIndicator` | TField |  | Contains a value that indicates a special condition of the account that applies to the primary consumer. |
| 12 | `CBR.CUS.COUNTRY.CODE` | `CbrConsumerDetails_CountryCode` | TField |  | This field updated with base or primary customer's country code from the field COUNTRY. |
| 13 | `CBR.CUS.FIRST.ADDRESS` | `CbrConsumerDetails_FirstAddress` | TField |  | This field updated with base or primary customer's first line address from the field NAME.2. |
| 14 | `CBR.CUS.SECOND.ADDRESS` | `CbrConsumerDetails_SecondAddress` | TField |  | This field updated with base or primary customer's second line address from the field STREET. |
| 15 | `CBR.CUS.BASE.CITY` | `CbrConsumerDetails_BaseCity` | TField |  | This field updated with base or primary customer's city from the field TOWN.COUNTRY |
| 16 | `CBR.CUS.BASE.STATE` | `CbrConsumerDetails_BaseState` | TField |  | This field updated with base or primary customer's state from the field state. |
| 17 | `CBR.CUS.BASE.ZIP.CODE` | `CbrConsumerDetails_BaseZipCode` | TField |  | This field updated with base or primary customer's postal / zip code from the field This field updated with base or primary customer's . |
| 18 | `CBR.CUS.ADDR.IND` | `CbrConsumerDetails_AddrInd` | TField |  | This will be the blank field. |
| 19 | `CBR.CUS.RESERVED.1` | `CbrConsumerDetails_Reserved1` | TField |  |  |
| 20 | `CBR.CUS.RESERVED.2` | `CbrConsumerDetails_Reserved2` | TField |  |  |
| 21 | `CBR.CUS.RESERVED.3` | `CbrConsumerDetails_Reserved3` | TField |  |  |
| 22 | `CBR.CUS.RESERVED.4` | `CbrConsumerDetails_Reserved4` | TField |  |  |
| 23 | `CBR.CUS.RESERVED.5` | `CbrConsumerDetails_Reserved5` | TField |  |  |
| 24 | `CBR.CUS.RESERVED.6` | `CbrConsumerDetails_Reserved6` | TField |  |  |
| 25 | `CBR.CUS.RESERVED.7` | `CbrConsumerDetails_Reserved7` | TField |  |  |
| 26 | `CBR.CUS.RESERVED.8` | `CbrConsumerDetails_Reserved8` | TField |  |  |
| 27 | `CBR.CUS.RESERVED.9` | `CbrConsumerDetails_Reserved9` | TField |  |  |
| 28 | `CBR.CUS.RESERVED.10` | `CbrConsumerDetails_Reserved10` | TField |  |  |
| 29 | `CBR.CUS.J1.CUSTOMER` | `CbrConsumerDetails_J1Customer` |  |  |  |
| 30 | `CBR.CUS.J1.TRAN.TYPE` | `CbrConsumerDetails_J1TranType` |  |  |  |
| 31 | `CBR.CUS.J1.CUS.SURNAME` | `CbrConsumerDetails_J1CusSurname` |  |  |  |
| 32 | `CBR.CUS.J1.FIRST.NAME` | `CbrConsumerDetails_J1FirstName` |  |  |  |
| 33 | `CBR.CUS.J1.CUS.MID.NAME` | `CbrConsumerDetails_J1CusMidName` |  |  |  |
| 34 | `CBR.CUS.J1.SUFFIX.CODE` | `CbrConsumerDetails_J1SuffixCode` |  |  |  |
| 35 | `CBR.CUS.J1.CUS.SSN` | `CbrConsumerDetails_J1CusSsn` |  |  |  |
| 36 | `CBR.CUS.J1.CUS.DOB` | `CbrConsumerDetails_J1CusDob` |  |  |  |
| 37 | `CBR.CUS.J1.TELE.NUMBER` | `CbrConsumerDetails_J1TeleNumber` |  |  |  |
| 38 | `CBR.CUS.J1.ECOA` | `CbrConsumerDetails_J1Ecoa` |  |  |  |
| 39 | `CBR.CUS.J1.CONS.IND` | `CbrConsumerDetails_J1ConsInd` |  |  |  |
| 40 | `CBR.CUS.RESERVED.11` | `CbrConsumerDetails_Reserved11` | TField |  |  |
| 41 | `CBR.CUS.RESERVED.12` | `CbrConsumerDetails_Reserved12` | TField |  |  |
| 42 | `CBR.CUS.RESERVED.13` | `CbrConsumerDetails_Reserved13` | TField |  |  |
| 43 | `CBR.CUS.RESERVED.14` | `CbrConsumerDetails_Reserved14` | TField |  |  |
| 44 | `CBR.CUS.RESERVED.15` | `CbrConsumerDetails_Reserved15` | TField |  |  |
| 45 | `CBR.CUS.RESERVED.16` | `CbrConsumerDetails_Reserved16` | TField |  |  |
| 46 | `CBR.CUS.RESERVED.17` | `CbrConsumerDetails_Reserved17` | TField |  |  |
| 47 | `CBR.CUS.RESERVED.18` | `CbrConsumerDetails_Reserved18` | TField |  |  |
| 48 | `CBR.CUS.RESERVED.19` | `CbrConsumerDetails_Reserved19` | TField |  |  |
| 49 | `CBR.CUS.RESERVED.20` | `CbrConsumerDetails_Reserved20` | TField |  |  |
| 50 | `CBR.CUS.J2.CUSTOMER` | `CbrConsumerDetails_J2Customer` |  |  |  |
| 51 | `CBR.CUS.J2.TRAN.TYPE` | `CbrConsumerDetails_J2TranType` |  |  |  |
| 52 | `CBR.CUS.J2.CUS.SURNAME` | `CbrConsumerDetails_J2CusSurname` |  |  |  |
| 53 | `CBR.CUS.J2.FIRST.NAME` | `CbrConsumerDetails_J2FirstName` |  |  |  |
| 54 | `CBR.CUS.J2.CUS.MID.NAME` | `CbrConsumerDetails_J2CusMidName` |  |  |  |
| 55 | `CBR.CUS.J2.SUFFIX.CODE` | `CbrConsumerDetails_J2SuffixCode` |  |  |  |
| 56 | `CBR.CUS.J2.CUS.SSN` | `CbrConsumerDetails_J2CusSsn` |  |  |  |
| 57 | `CBR.CUS.J2.CUS.DOB` | `CbrConsumerDetails_J2CusDob` |  |  |  |
| 58 | `CBR.CUS.J2.TELE.NUMBER` | `CbrConsumerDetails_J2TeleNumber` |  |  |  |
| 59 | `CBR.CUS.J2.ECOA` | `CbrConsumerDetails_J2Ecoa` |  |  |  |
| 60 | `CBR.CUS.J2.CONS.IND` | `CbrConsumerDetails_J2ConsInd` |  |  |  |
| 61 | `CBR.CUS.J2.COUNTRY` | `CbrConsumerDetails_J2Country` |  |  |  |
| 62 | `CBR.CUS.J2.FIRST.ADDRESS` | `CbrConsumerDetails_J2FirstAddress` |  |  |  |
| 63 | `CBR.CUS.J2.SECOND.ADDRESS` | `CbrConsumerDetails_J2SecondAddress` |  |  |  |
| 64 | `CBR.CUS.J2.CUS.CITY` | `CbrConsumerDetails_J2CusCity` |  |  |  |
| 65 | `CBR.CUS.J2.CUS.STATE` | `CbrConsumerDetails_J2CusState` |  |  |  |
| 66 | `CBR.CUS.J2.CUS.ZIP.CODE` | `CbrConsumerDetails_J2CusZipCode` |  |  |  |
| 67 | `CBR.CUS.J2.ADDR.IND` | `CbrConsumerDetails_J2AddrInd` |  |  |  |
| 68 | `CBR.CUS.J2.RESIDENCE` | `CbrConsumerDetails_J2Residence` |  |  |  |
| 69 | `CBR.CUS.RESERVED.21` | `CbrConsumerDetails_Reserved21` | TField |  |  |
| 70 | `CBR.CUS.RESERVED.22` | `CbrConsumerDetails_Reserved22` | TField |  |  |
| 71 | `CBR.CUS.RESERVED.23` | `CbrConsumerDetails_Reserved23` | TField |  |  |
| 72 | `CBR.CUS.RESERVED.24` | `CbrConsumerDetails_Reserved24` | TField |  |  |
| 73 | `CBR.CUS.RESERVED.25` | `CbrConsumerDetails_Reserved25` | TField |  |  |
| 74 | `CBR.CUS.RESERVED.26` | `CbrConsumerDetails_Reserved26` | TField |  |  |
| 75 | `CBR.CUS.RESERVED.27` | `CbrConsumerDetails_Reserved27` | TField |  |  |
| 76 | `CBR.CUS.RESERVED.28` | `CbrConsumerDetails_Reserved28` | TField |  |  |
| 77 | `CBR.CUS.RESERVED.29` | `CbrConsumerDetails_Reserved29` | TField |  |  |
| 78 | `CBR.CUS.RESERVED.30` | `CbrConsumerDetails_Reserved30` | TField |  |  |
