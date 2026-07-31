# FS.GA.COUNTRY.CODES.EQUIVALENCES — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUNTRY.CODES.EQUIVALENCES` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.PARENT.REF.ID` | `FsGaCountryCodesEquivalences_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.ORA.ROWID` | `FsGaCountryCodesEquivalences_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.MULTIFONDS.COUNTRY.CODE` | `FsGaCountryCodesEquivalences_MultifondsCountryCode` | TField |  | Multifonds Country Code Multifonds DB Column is CPAYS_MULTIFONDS. |
| 4 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.COUNTRY.ISO.CODE` | `FsGaCountryCodesEquivalences_CountryIsoCode` | TField |  | Country ISO Identification Code Multifonds DB Column is CPAYS_ISO. |
| 5 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.CUSTOMER.COUNTRY.CODE` | `FsGaCountryCodesEquivalences_CustomerCountryCode` | TField |  | Customer Country Code for Non-ISO code Cases Multifonds DB Column is CPAYS_REPRISE. |
| 6 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.CCLUX.COUNTRY.CODE` | `FsGaCountryCodesEquivalences_CcluxCountryCode` | TField |  | CCLUX Country Code Multifonds DB Column is CPAYS_CCLUX. |
| 7 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED10` | `FsGaCountryCodesEquivalences_Reserved10` | TField |  |  |
| 8 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED9` | `FsGaCountryCodesEquivalences_Reserved9` | TField |  |  |
| 9 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED8` | `FsGaCountryCodesEquivalences_Reserved8` | TField |  |  |
| 10 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED7` | `FsGaCountryCodesEquivalences_Reserved7` | TField |  |  |
| 11 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED6` | `FsGaCountryCodesEquivalences_Reserved6` | TField |  |  |
| 12 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED5` | `FsGaCountryCodesEquivalences_Reserved5` | TField |  |  |
| 13 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED4` | `FsGaCountryCodesEquivalences_Reserved4` | TField |  |  |
| 14 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED3` | `FsGaCountryCodesEquivalences_Reserved3` | TField |  |  |
| 15 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED2` | `FsGaCountryCodesEquivalences_Reserved2` | TField |  |  |
| 16 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RESERVED1` | `FsGaCountryCodesEquivalences_Reserved1` | TField |  |  |
| 17 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.LOCAL.REF` | `FsGaCountryCodesEquivalences_LocalRef` |  |  |  |
| 18 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.OVERRIDE` | `FsGaCountryCodesEquivalences_Override` |  |  |  |
| 19 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.RECORD.STATUS` | `FsGaCountryCodesEquivalences_RecordStatus` | String |  |  |
| 20 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.CURR.NO` | `FsGaCountryCodesEquivalences_CurrNo` | String |  |  |
| 21 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.INPUTTER` | `FsGaCountryCodesEquivalences_Inputter` |  |  |  |
| 22 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.DATE.TIME` | `FsGaCountryCodesEquivalences_DateTime` |  |  |  |
| 23 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.AUTHORISER` | `FsGaCountryCodesEquivalences_Authoriser` | String |  |  |
| 24 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.CO.CODE` | `FsGaCountryCodesEquivalences_CoCode` | String |  |  |
| 25 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.DEPT.CODE` | `FsGaCountryCodesEquivalences_DeptCode` | String |  |  |
| 26 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.AUDITOR.CODE` | `FsGaCountryCodesEquivalences_AuditorCode` | String |  |  |
| 27 | `FS.GA.COUNTRY.CODES.EQUIVALENCES.AUDIT.DATE.TIME` | `FsGaCountryCodesEquivalences_AuditDateTime` | String |  |  |
