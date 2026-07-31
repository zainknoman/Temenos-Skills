# FS.GA.CENTRAL.REGISTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.CENTRAL.REGISTER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CENTRAL.REGISTER.EXTERNAL.REFERENCE` | `FsGaCentralRegister_ExternalReference` | TField |  | External reference Multifonds DB Column is EXTERNAL_REF. |
| 2 | `CENTRAL.REGISTER.ACCOUNT.OFFICER.DESCRIPTION` | `FsGaCentralRegister_AccountOfficerDescription` | TField |  | Account officer Description Multifonds DB Column is XOFFI. |
| 3 | `CENTRAL.REGISTER.ACCOUNT` | `FsGaCentralRegister_Account` | TField |  | Account Multifonds DB Column is NRUBR. |
| 4 | `CENTRAL.REGISTER.INTRODUCER.DESCRIPTION` | `FsGaCentralRegister_IntroducerDescription` | TField |  | Introducer Description Multifonds DB Column is XINTRO. |
| 5 | `CENTRAL.REGISTER.RESIDENCE` | `FsGaCentralRegister_Residence` | TField |  | Residence Multifonds DB Column is DOMI. |
| 6 | `CENTRAL.REGISTER.COUNTRY` | `FsGaCentralRegister_Country` | TField |  | Country Multifonds DB Column is NAT. |
| 7 | `CENTRAL.REGISTER.TYPE.DESCRIPTION` | `FsGaCentralRegister_TypeDescription` | TField |  | Type Description Multifonds DB Column is XCTCL. |
| 8 | `CENTRAL.REGISTER.NAME` | `FsGaCentralRegister_Name` | TField |  | Name Multifonds DB Column is XLIBELLE. |
| 9 | `CENTRAL.REGISTER.NUMBER` | `FsGaCentralRegister_Number` | TField |  | Number Multifonds DB Column is NCORRESP. |
| 10 | `CENTRAL.REGISTER.SWIFT.CODE` | `FsGaCentralRegister_SwiftCode` | TField |  | SWIFT code Multifonds DB Column is COD_SWIFT. |
| 11 | `CENTRAL.REGISTER.INTRODUCER` | `FsGaCentralRegister_Introducer` | TField |  | Introducer Multifonds DB Column is INTRO. |
| 12 | `CENTRAL.REGISTER.TRUST` | `FsGaCentralRegister_Trust` | TField |  | Trust Multifonds DB Column is NCORRESP_TRUST. |
| 13 | `CENTRAL.REGISTER.ACCOUNT.OFFICER` | `FsGaCentralRegister_AccountOfficer` | TField |  | Account officer Multifonds DB Column is OFFI. |
| 14 | `CENTRAL.REGISTER.COUNTRY.DESCRIPTION` | `FsGaCentralRegister_CountryDescription` | TField |  | Country Description Multifonds DB Column is XNAT. |
| 15 | `CENTRAL.REGISTER.RESIDENCE.DESCRIPTION` | `FsGaCentralRegister_ResidenceDescription` | TField |  | Residence Description Multifonds DB Column is XDOMI. |
| 16 | `CENTRAL.REGISTER.TYPE` | `FsGaCentralRegister_Type` | TField |  | Type Multifonds DB Column is CTCL. |
| 17 | `CENTRAL.REGISTER.BLZ` | `FsGaCentralRegister_Blz` | TField |  | Blz Multifonds DB Column is BLZ. |
| 18 | `CENTRAL.REGISTER.NSUF` | `FsGaCentralRegister_Nsuf` | TField |  | Nsuf Multifonds DB Column is NSUF. |
| 19 | `CENTRAL.REGISTER.RECORD.STATUS` | `FsGaCentralRegister_RecordStatus` | String |  |  |
| 20 | `CENTRAL.REGISTER.CURR.NO` | `FsGaCentralRegister_CurrNo` | String |  |  |
| 21 | `CENTRAL.REGISTER.INPUTTER` | `FsGaCentralRegister_Inputter` |  |  |  |
| 22 | `CENTRAL.REGISTER.DATE.TIME` | `FsGaCentralRegister_DateTime` |  |  |  |
| 23 | `CENTRAL.REGISTER.AUTHORISER` | `FsGaCentralRegister_Authoriser` | String |  |  |
| 24 | `CENTRAL.REGISTER.CO.CODE` | `FsGaCentralRegister_CoCode` | String |  |  |
| 25 | `CENTRAL.REGISTER.DEPT.CODE` | `FsGaCentralRegister_DeptCode` | String |  |  |
| 26 | `CENTRAL.REGISTER.AUDITOR.CODE` | `FsGaCentralRegister_AuditorCode` | String |  |  |
| 27 | `CENTRAL.REGISTER.AUDIT.DATE.TIME` | `FsGaCentralRegister_AuditDateTime` | String |  |  |
