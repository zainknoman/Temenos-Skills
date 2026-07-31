# FS.GA.CENTRAL.REGISTER.ADDRESS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CENTRAL.REGISTER.ADDRESS` in `FS_ThirdParties.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CENTRAL.REGISTER.ADDRESS.PARENT.REF.ID` | `FsGaCentralRegisterAddress_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ORA.ROWID` | `FsGaCentralRegisterAddress_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CENTRAL.REGISTER.ADDRESS.CORRESPONDENT` | `FsGaCentralRegisterAddress_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CENTRAL.REGISTER.ADDRESS.TYPE.OF.ADDRESS` | `FsGaCentralRegisterAddress_TypeOfAddress` | TField |  | Refer to type of correspondent or central register address Multifonds DB Column is TYP_ADRESS. |
| 5 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ADDRESS.NUMBER` | `FsGaCentralRegisterAddress_AddressNumber` | TField |  | Correspondent Address number Multifonds DB Column is NADRESS. |
| 6 | `FS.GA.CENTRAL.REGISTER.ADDRESS.CORRESPONDENT.ADDRESS` | `FsGaCentralRegisterAddress_CorrespondentAddress` | TField |  | Correspondent Address Multifonds DB Column is ADRESSE. |
| 7 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ADDRESS.LINE2` | `FsGaCentralRegisterAddress_AddressLine2` | TField |  | Correspondent Address Line2 Multifonds DB Column is ADRESSE_LINE2. |
| 8 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ADDRESS.LINE3` | `FsGaCentralRegisterAddress_AddressLine3` | TField |  | Correspondent Address Line3 Multifonds DB Column is ADRESSE_LINE3. |
| 9 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ADDRESS.LINE4` | `FsGaCentralRegisterAddress_AddressLine4` | TField |  | Correspondent Address Line4 Multifonds DB Column is ADRESSE_LINE4. |
| 10 | `FS.GA.CENTRAL.REGISTER.ADDRESS.ZIP.CODE` | `FsGaCentralRegisterAddress_ZipCode` | TField |  | City zip code Multifonds DB Column is CODE. |
| 11 | `FS.GA.CENTRAL.REGISTER.ADDRESS.CITY` | `FsGaCentralRegisterAddress_City` | TField |  | Refers to the City of Correspondent address. Multifonds DB Column is VILLE. |
| 12 | `FS.GA.CENTRAL.REGISTER.ADDRESS.COUNTRIES.CODES` | `FsGaCentralRegisterAddress_CountriesCodes` | TField |  | Refers to the Country Code of Correspondent address. Multifonds DB Column is PAYS. |
| 13 | `FS.GA.CENTRAL.REGISTER.ADDRESS.FREQUENCY` | `FsGaCentralRegisterAddress_Frequency` | TField |  | Frequency code for processing Multifonds DB Column is CFREQ. |
| 14 | `FS.GA.CENTRAL.REGISTER.ADDRESS.NUMBER.OF.COPIES` | `FsGaCentralRegisterAddress_NumberOfCopies` | TField |  | This can be entered up to 4 digit Multifonds DB Column is NBCOPIES. |
| 15 | `FS.GA.CENTRAL.REGISTER.ADDRESS.MAIL.CODE.3` | `FsGaCentralRegisterAddress_MailCode3` | TField |  | Mail Code 3 Multifonds DB Column is CODE_MAIL. |
| 16 | `FS.GA.CENTRAL.REGISTER.ADDRESS.SIREN.ID` | `FsGaCentralRegisterAddress_SirenId` | TField |  | Refers to the official identifier code for the French central Bank Multifonds DB Column is SIREN_ID. |
| 17 | `FS.GA.CENTRAL.REGISTER.ADDRESS.TRANS.CODE` | `FsGaCentralRegisterAddress_TransCode` | TField |  | Refers to an element which will be used for the file transmission to the French central Bank. Multifonds DB Column is TRANS. |
| 18 | `FS.GA.CENTRAL.REGISTER.ADDRESS.DESCRIPTION` | `FsGaCentralRegisterAddress_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 19 | `FS.GA.CENTRAL.REGISTER.ADDRESS.TELEPHONE` | `FsGaCentralRegisterAddress_Telephone` | TField |  | Corresponds to the phone number of the BDF correspondent Multifonds DB Column is TELE. |
| 20 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED10` | `FsGaCentralRegisterAddress_Reserved10` | TField |  |  |
| 21 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED9` | `FsGaCentralRegisterAddress_Reserved9` | TField |  |  |
| 22 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED8` | `FsGaCentralRegisterAddress_Reserved8` | TField |  |  |
| 23 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED7` | `FsGaCentralRegisterAddress_Reserved7` | TField |  |  |
| 24 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED6` | `FsGaCentralRegisterAddress_Reserved6` | TField |  |  |
| 25 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED5` | `FsGaCentralRegisterAddress_Reserved5` | TField |  |  |
| 26 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED4` | `FsGaCentralRegisterAddress_Reserved4` | TField |  |  |
| 27 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED3` | `FsGaCentralRegisterAddress_Reserved3` | TField |  |  |
| 28 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED2` | `FsGaCentralRegisterAddress_Reserved2` | TField |  |  |
| 29 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RESERVED1` | `FsGaCentralRegisterAddress_Reserved1` | TField |  |  |
| 30 | `FS.GA.CENTRAL.REGISTER.ADDRESS.LOCAL.REF` | `FsGaCentralRegisterAddress_LocalRef` |  |  |  |
| 31 | `FS.GA.CENTRAL.REGISTER.ADDRESS.OVERRIDE` | `FsGaCentralRegisterAddress_Override` |  |  |  |
| 32 | `FS.GA.CENTRAL.REGISTER.ADDRESS.RECORD.STATUS` | `FsGaCentralRegisterAddress_RecordStatus` | String |  |  |
| 33 | `FS.GA.CENTRAL.REGISTER.ADDRESS.CURR.NO` | `FsGaCentralRegisterAddress_CurrNo` | String |  |  |
| 34 | `FS.GA.CENTRAL.REGISTER.ADDRESS.INPUTTER` | `FsGaCentralRegisterAddress_Inputter` |  |  |  |
| 35 | `FS.GA.CENTRAL.REGISTER.ADDRESS.DATE.TIME` | `FsGaCentralRegisterAddress_DateTime` |  |  |  |
| 36 | `FS.GA.CENTRAL.REGISTER.ADDRESS.AUTHORISER` | `FsGaCentralRegisterAddress_Authoriser` | String |  |  |
| 37 | `FS.GA.CENTRAL.REGISTER.ADDRESS.CO.CODE` | `FsGaCentralRegisterAddress_CoCode` | String |  |  |
| 38 | `FS.GA.CENTRAL.REGISTER.ADDRESS.DEPT.CODE` | `FsGaCentralRegisterAddress_DeptCode` | String |  |  |
| 39 | `FS.GA.CENTRAL.REGISTER.ADDRESS.AUDITOR.CODE` | `FsGaCentralRegisterAddress_AuditorCode` | String |  |  |
| 40 | `FS.GA.CENTRAL.REGISTER.ADDRESS.AUDIT.DATE.TIME` | `FsGaCentralRegisterAddress_AuditDateTime` | String |  |  |
