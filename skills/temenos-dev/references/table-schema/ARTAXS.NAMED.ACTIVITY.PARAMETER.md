# ARTAXS.NAMED.ACTIVITY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ARTAXS.NAMED.ACTIVITY.PARAMETER` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACTIVITY.PARAM.BANK.NAMED.ACTIVITY` | `ArtaxsNamedActivityParameter_BankNamedActivity` |  |  |  |
| 2 | `ACTIVITY.PARAM.STANDARD.ACTIVITY` | `ArtaxsNamedActivityParameter_StandardActivity` |  |  |  |
| 3 | `ACTIVITY.PARAM.RESERVED.15` | `ArtaxsNamedActivityParameter_Reserved15` | TField |  | Field reserved for future use. |
| 4 | `ACTIVITY.PARAM.RESERVED.14` | `ArtaxsNamedActivityParameter_Reserved14` | TField |  | Field reserved for future use. |
| 5 | `ACTIVITY.PARAM.RESERVED.13` | `ArtaxsNamedActivityParameter_Reserved13` | TField |  | Field reserved for future use. |
| 6 | `ACTIVITY.PARAM.RESERVED.12` | `ArtaxsNamedActivityParameter_Reserved12` | TField |  | Field reserved for future use. |
| 7 | `ACTIVITY.PARAM.RESERVED.11` | `ArtaxsNamedActivityParameter_Reserved11` | TField |  | Field reserved for future use. |
| 8 | `ACTIVITY.PARAM.RESERVED.10` | `ArtaxsNamedActivityParameter_Reserved10` | TField |  | Field reserved for future use. |
| 9 | `ACTIVITY.PARAM.RESERVED.9` | `ArtaxsNamedActivityParameter_Reserved9` | TField |  | Field reserved for future use. |
| 10 | `ACTIVITY.PARAM.RESERVED.8` | `ArtaxsNamedActivityParameter_Reserved8` | TField |  | Field reserved for future use. |
| 11 | `ACTIVITY.PARAM.RESERVED.7` | `ArtaxsNamedActivityParameter_Reserved7` | TField |  | Field reserved for future use. |
| 12 | `ACTIVITY.PARAM.RESERVED.6` | `ArtaxsNamedActivityParameter_Reserved6` | TField |  | Field reserved for future use. |
| 13 | `ACTIVITY.PARAM.RESERVED.5` | `ArtaxsNamedActivityParameter_Reserved5` | TField |  | Field reserved for future use. |
| 14 | `ACTIVITY.PARAM.RESERVED.4` | `ArtaxsNamedActivityParameter_Reserved4` | TField |  | Field reserved for future use. |
| 15 | `ACTIVITY.PARAM.RESERVED.3` | `ArtaxsNamedActivityParameter_Reserved3` | TField |  | Field reserved for future use. |
| 16 | `ACTIVITY.PARAM.RESERVED.2` | `ArtaxsNamedActivityParameter_Reserved2` | TField |  | Field reserved for future use. |
| 17 | `ACTIVITY.PARAM.RESERVED.1` | `ArtaxsNamedActivityParameter_Reserved1` | TField |  | Field reserved for future use. |
| 18 | `ACTIVITY.PARAM.LOCAL.REF` | `ArtaxsNamedActivityParameter_LocalRef` |  |  |  |
| 19 | `ACTIVITY.PARAM.OVERRIDE` | `ArtaxsNamedActivityParameter_Override` |  |  |  |
| 20 | `ACTIVITY.PARAM.RECORD.STATUS` | `ArtaxsNamedActivityParameter_RecordStatus` | String |  |  |
| 21 | `ACTIVITY.PARAM.CURR.NO` | `ArtaxsNamedActivityParameter_CurrNo` | String |  |  |
| 22 | `ACTIVITY.PARAM.INPUTTER` | `ArtaxsNamedActivityParameter_Inputter` |  |  |  |
| 23 | `ACTIVITY.PARAM.DATE.TIME` | `ArtaxsNamedActivityParameter_DateTime` |  |  |  |
| 24 | `ACTIVITY.PARAM.AUTHORISER` | `ArtaxsNamedActivityParameter_Authoriser` | String |  |  |
| 25 | `ACTIVITY.PARAM.CO.CODE` | `ArtaxsNamedActivityParameter_CoCode` | String |  |  |
| 26 | `ACTIVITY.PARAM.DEPT.CODE` | `ArtaxsNamedActivityParameter_DeptCode` | String |  |  |
| 27 | `ACTIVITY.PARAM.AUDITOR.CODE` | `ArtaxsNamedActivityParameter_AuditorCode` | String |  |  |
| 28 | `ACTIVITY.PARAM.AUDIT.DATE.TIME` | `ArtaxsNamedActivityParameter_AuditDateTime` | String |  |  |
