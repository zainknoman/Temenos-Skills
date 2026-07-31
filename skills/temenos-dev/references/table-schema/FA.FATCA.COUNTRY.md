# FA.FATCA.COUNTRY — Table Schema

> Source: `INSERTS/I_F.FA.FATCA.COUNTRY` in `FA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.COU.DESCRIPTION` | `FaFatcaCountry_Description` |  |  |  |
| 2 | `FA.COU.IGA.INDICATOR` | `FaFatcaCountry_IgaIndicator` | TField |  | IGA indicator ( FATCA Inter Governmental Agreement) for every country that enters into an IGA with US.The possible values are 1 or 2 if there exists a IGA between the ID country and the US. Else, it will be null |
| 3 | `FA.COU.RESERVED.20` | `FaFatcaCountry_Reserved20` | TField |  | Reserved for future use |
| 4 | `FA.COU.RESERVED.19` | `FaFatcaCountry_Reserved19` | TField |  | Reserved for future use |
| 5 | `FA.COU.RESERVED.18` | `FaFatcaCountry_Reserved18` | TField |  | Reserved for future use |
| 6 | `FA.COU.RESERVED.17` | `FaFatcaCountry_Reserved17` | TField |  | Reserved for future use |
| 7 | `FA.COU.RESERVED.16` | `FaFatcaCountry_Reserved16` | TField |  | Reserved for future use |
| 8 | `FA.COU.RESERVED.15` | `FaFatcaCountry_Reserved15` | TField |  | Reserved for future use |
| 9 | `FA.COU.RESERVED.14` | `FaFatcaCountry_Reserved14` | TField |  | Reserved for future use |
| 10 | `FA.COU.RESERVED.13` | `FaFatcaCountry_Reserved13` | TField |  | Reserved for future use |
| 11 | `FA.COU.RESERVED.12` | `FaFatcaCountry_Reserved12` | TField |  | Reserved for future use |
| 12 | `FA.COU.RESERVED.11` | `FaFatcaCountry_Reserved11` | TField |  | Reserved for future use |
| 13 | `FA.COU.RESERVED.10` | `FaFatcaCountry_Reserved10` | TField |  | Reserved for future use |
| 14 | `FA.COU.RESERVED.09` | `FaFatcaCountry_Reserved09` | TField |  | Reserved for future use |
| 15 | `FA.COU.RESERVED.08` | `FaFatcaCountry_Reserved08` | TField |  | Reserved for future use |
| 16 | `FA.COU.RESERVED.07` | `FaFatcaCountry_Reserved07` | TField |  | Reserved for future use |
| 17 | `FA.COU.RESERVED.06` | `FaFatcaCountry_Reserved06` | TField |  | Reserved for future use |
| 18 | `FA.COU.RESERVED.05` | `FaFatcaCountry_Reserved05` | TField |  | Reserved for future use |
| 19 | `FA.COU.RESERVED.04` | `FaFatcaCountry_Reserved04` | TField |  | Reserved for future use |
| 20 | `FA.COU.RESERVED.03` | `FaFatcaCountry_Reserved03` | TField |  | Reserved for future use |
| 21 | `FA.COU.RESERVED.02` | `FaFatcaCountry_Reserved02` | TField |  | Reserved for future use |
| 22 | `FA.COU.RESERVED.01` | `FaFatcaCountry_Reserved01` | TField |  | Reserved for future use |
| 23 | `FA.COU.LOCAL.REF` | `FaFatcaCountry_LocalRef` |  |  |  |
| 24 | `FA.COU.OVERRIDE` | `FaFatcaCountry_Override` |  |  |  |
| 25 | `FA.COU.RECORD.STATUS` | `FaFatcaCountry_RecordStatus` | String |  | Status of the record |
| 26 | `FA.COU.CURR.NO` | `FaFatcaCountry_CurrNo` | String |  | Curr No |
| 27 | `FA.COU.INPUTTER` | `FaFatcaCountry_Inputter` |  |  |  |
| 28 | `FA.COU.DATE.TIME` | `FaFatcaCountry_DateTime` |  |  |  |
| 29 | `FA.COU.AUTHORISER` | `FaFatcaCountry_Authoriser` | String |  | Authoriser |
| 30 | `FA.COU.CO.CODE` | `FaFatcaCountry_CoCode` | String |  | Company code |
| 31 | `FA.COU.DEPT.CODE` | `FaFatcaCountry_DeptCode` | String |  | Department code |
| 32 | `FA.COU.AUDITOR.CODE` | `FaFatcaCountry_AuditorCode` | String |  | Auditor Code |
| 33 | `FA.COU.AUDIT.DATE.TIME` | `FaFatcaCountry_AuditDateTime` | String |  | Audit Date and time |
