# PZ.NATIONAL.COMP.AUTHORITY — Table Schema

> Source: `INSERTS/I_F.PZ.NATIONAL.COMP.AUTHORITY` in `RT_OpenBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PZN.NCA.NAME` | `PzNationalCompAuthority_NcaName` | TField |  | The NCA Name must be static and agreed. The value will be inside the QSEAL Certificate. E.g. Financial ConductAuthority.This NAME should be unique per NCA record i.e. no other PZ.NATIONAL.COMP.AUTHORITY record should have thesame NAME as in the current record. |
| 2 | `PZN.NCA.COUNTRY` | `PzNationalCompAuthority_NcaCountry` | TField |  | The 2 Digit NCA Country Code will use the ISO country code for that country e.g. GB |
| 3 | `PZN.NCA.CODE` | `PzNationalCompAuthority_NcaCode` | TField |  | Unique reference for National Competent Authority; e.g. FCA |
| 4 | `PZN.RESERVED.10` | `PzNationalCompAuthority_Reserved10` | TField |  |  |
| 5 | `PZN.RESERVED.09` | `PzNationalCompAuthority_Reserved09` | TField |  |  |
| 6 | `PZN.RESERVED.08` | `PzNationalCompAuthority_Reserved08` | TField |  |  |
| 7 | `PZN.RESERVED.07` | `PzNationalCompAuthority_Reserved07` | TField |  |  |
| 8 | `PZN.RESERVED.06` | `PzNationalCompAuthority_Reserved06` | TField |  |  |
| 9 | `PZN.RESERVED.05` | `PzNationalCompAuthority_Reserved05` | TField |  |  |
| 10 | `PZN.RESERVED.04` | `PzNationalCompAuthority_Reserved04` | TField |  |  |
| 11 | `PZN.RESERVED.03` | `PzNationalCompAuthority_Reserved03` | TField |  |  |
| 12 | `PZN.RESERVED.02` | `PzNationalCompAuthority_Reserved02` | TField |  |  |
| 13 | `PZN.RESERVED.01` | `PzNationalCompAuthority_Reserved01` | TField |  |  |
| 14 | `PZN.LOCAL.REF` | `PzNationalCompAuthority_LocalRef` |  |  |  |
| 15 | `PZN.RECORD.STATUS` | `PzNationalCompAuthority_RecordStatus` | String |  |  |
| 16 | `PZN.CURR.NO` | `PzNationalCompAuthority_CurrNo` | String |  |  |
| 17 | `PZN.INPUTTER` | `PzNationalCompAuthority_Inputter` |  |  |  |
| 18 | `PZN.DATE.TIME` | `PzNationalCompAuthority_DateTime` |  |  |  |
| 19 | `PZN.AUTHORISER` | `PzNationalCompAuthority_Authoriser` | String |  |  |
| 20 | `PZN.CO.CODE` | `PzNationalCompAuthority_CoCode` | String |  |  |
| 21 | `PZN.DEPT.CODE` | `PzNationalCompAuthority_DeptCode` | String |  |  |
| 22 | `PZN.AUDITOR.CODE` | `PzNationalCompAuthority_AuditorCode` | String |  |  |
| 23 | `PZN.AUDIT.DATE.TIME` | `PzNationalCompAuthority_AuditDateTime` | String |  |  |
