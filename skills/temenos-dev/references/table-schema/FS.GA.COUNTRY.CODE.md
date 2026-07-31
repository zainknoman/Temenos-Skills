# FS.GA.COUNTRY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUNTRY.CODE` in `FS_SystemConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUNTRY.CODE.PARENT.REF.ID` | `FsGaCountryCode_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COUNTRY.CODE.ORA.ROWID` | `FsGaCountryCode_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COUNTRY.CODE.COUNTRY.ID.CODE` | `FsGaCountryCode_CountryIdCode` | TField |  | Defines the country short code Multifonds DB Column is CPAYS. |
| 4 | `FS.GA.COUNTRY.CODE.CONTINENT.CODE` | `FsGaCountryCode_ContinentCode` | TField |  | Continent code like EMEA, US etc user definable Multifonds DB Column is CCONTINENT. |
| 5 | `FS.GA.COUNTRY.CODE.CEE.COUNTRY` | `FsGaCountryCode_CeeCountry` | TField |  | It indicates if the country is part of CEE countries (Central &amp; East Europe) Multifonds DB Column is C_CEE. |
| 6 | `FS.GA.COUNTRY.CODE.OECD.COUNTRY` | `FsGaCountryCode_OecdCountry` | TField |  | It indicates if the country is part of OECD group (Organization of Economic Cooperation &amp; Development) Multifonds DB Column is C_OCDE. |
| 7 | `FS.GA.COUNTRY.CODE.COUNTRY.GROUPS.MASTER.GROUP` | `FsGaCountryCode_CountryGroupsMasterGroup` | TField |  | Swiss Bank country groups are not used anymore Multifonds DB Column is GRP_PAYS. |
| 8 | `FS.GA.COUNTRY.CODE.STARTING.DATE.OF.LAW` | `FsGaCountryCode_StartingDateOfLaw` | TField |  | It provides the starting date of law to which country is part of Multifonds DB Column is DSTART_LAW. |
| 9 | `FS.GA.COUNTRY.CODE.END.TRANSIT.PERIOD` | `FsGaCountryCode_EndTransitPeriod` | TField |  | End of transit period of law to which country is part of Multifonds DB Column is DEND_LAW. |
| 10 | `FS.GA.COUNTRY.CODE.CE.COUNTRY` | `FsGaCountryCode_CeCountry` | TField |  | It indicates if the country is a CE country Multifonds DB Column is C_CE. |
| 11 | `FS.GA.COUNTRY.CODE.QI.COUNTRY` | `FsGaCountryCode_QiCountry` | TField |  | QI Multifonds DB Column is QI. |
| 12 | `FS.GA.COUNTRY.CODE.RESERVED10` | `FsGaCountryCode_Reserved10` | TField |  |  |
| 13 | `FS.GA.COUNTRY.CODE.RESERVED9` | `FsGaCountryCode_Reserved9` | TField |  |  |
| 14 | `FS.GA.COUNTRY.CODE.RESERVED8` | `FsGaCountryCode_Reserved8` | TField |  |  |
| 15 | `FS.GA.COUNTRY.CODE.RESERVED7` | `FsGaCountryCode_Reserved7` | TField |  |  |
| 16 | `FS.GA.COUNTRY.CODE.RESERVED6` | `FsGaCountryCode_Reserved6` | TField |  |  |
| 17 | `FS.GA.COUNTRY.CODE.RESERVED5` | `FsGaCountryCode_Reserved5` | TField |  |  |
| 18 | `FS.GA.COUNTRY.CODE.RESERVED4` | `FsGaCountryCode_Reserved4` | TField |  |  |
| 19 | `FS.GA.COUNTRY.CODE.RESERVED3` | `FsGaCountryCode_Reserved3` | TField |  |  |
| 20 | `FS.GA.COUNTRY.CODE.RESERVED2` | `FsGaCountryCode_Reserved2` | TField |  |  |
| 21 | `FS.GA.COUNTRY.CODE.RESERVED1` | `FsGaCountryCode_Reserved1` | TField |  |  |
| 22 | `FS.GA.COUNTRY.CODE.LOCAL.REF` | `FsGaCountryCode_LocalRef` |  |  |  |
| 23 | `FS.GA.COUNTRY.CODE.OVERRIDE` | `FsGaCountryCode_Override` |  |  |  |
| 24 | `FS.GA.COUNTRY.CODE.RECORD.STATUS` | `FsGaCountryCode_RecordStatus` | String |  |  |
| 25 | `FS.GA.COUNTRY.CODE.CURR.NO` | `FsGaCountryCode_CurrNo` | String |  |  |
| 26 | `FS.GA.COUNTRY.CODE.INPUTTER` | `FsGaCountryCode_Inputter` |  |  |  |
| 27 | `FS.GA.COUNTRY.CODE.DATE.TIME` | `FsGaCountryCode_DateTime` |  |  |  |
| 28 | `FS.GA.COUNTRY.CODE.AUTHORISER` | `FsGaCountryCode_Authoriser` | String |  |  |
| 29 | `FS.GA.COUNTRY.CODE.CO.CODE` | `FsGaCountryCode_CoCode` | String |  |  |
| 30 | `FS.GA.COUNTRY.CODE.DEPT.CODE` | `FsGaCountryCode_DeptCode` | String |  |  |
| 31 | `FS.GA.COUNTRY.CODE.AUDITOR.CODE` | `FsGaCountryCode_AuditorCode` | String |  |  |
| 32 | `FS.GA.COUNTRY.CODE.AUDIT.DATE.TIME` | `FsGaCountryCode_AuditDateTime` | String |  |  |
