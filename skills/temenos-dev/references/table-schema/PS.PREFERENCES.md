# PS.PREFERENCES — Table Schema

> Source: `INSERTS/I_F.PS.PREFERENCES` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.PREF.DESCRIPTION` | `PsPreferences_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `PS.PREF.ROLE` | `PsPreferences_Role` |  |  |  |
| 3 | `PS.PREF.LINK.ID` | `PsPreferences_LinkId` |  |  |  |
| 4 | `PS.PREF.GROUP.LABEL` | `PsPreferences_GroupLabel` |  |  |  |
| 5 | `PS.PREF.RESERVE.1` | `PsPreferences_Reserve1` |  |  |  |
| 6 | `PS.PREF.RESERVE.2` | `PsPreferences_Reserve2` |  |  |  |
| 7 | `PS.PREF.ATTRIBUTES` | `PsPreferences_Attributes` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `PS.PREF.RESERVED.18` | `PsPreferences_Reserved18` | TField |  |  |
| 9 | `PS.PREF.RESERVED.17` | `PsPreferences_Reserved17` | TField |  |  |
| 10 | `PS.PREF.RESERVED.16` | `PsPreferences_Reserved16` | TField |  |  |
| 11 | `PS.PREF.RESERVED.15` | `PsPreferences_Reserved15` | TField |  |  |
| 12 | `PS.PREF.RESERVED.14` | `PsPreferences_Reserved14` | TField |  |  |
| 13 | `PS.PREF.RESERVED.13` | `PsPreferences_Reserved13` | TField |  |  |
| 14 | `PS.PREF.RESERVED.12` | `PsPreferences_Reserved12` | TField |  |  |
| 15 | `PS.PREF.RESERVED.11` | `PsPreferences_Reserved11` | TField |  |  |
| 16 | `PS.PREF.RESERVED.10` | `PsPreferences_Reserved10` | TField |  |  |
| 17 | `PS.PREF.RESERVED.9` | `PsPreferences_Reserved9` | TField |  |  |
| 18 | `PS.PREF.RESERVED.8` | `PsPreferences_Reserved8` | TField |  |  |
| 19 | `PS.PREF.RESERVED.7` | `PsPreferences_Reserved7` | TField |  |  |
| 20 | `PS.PREF.RESERVED.6` | `PsPreferences_Reserved6` | TField |  |  |
| 21 | `PS.PREF.RESERVED.5` | `PsPreferences_Reserved5` | TField |  |  |
| 22 | `PS.PREF.RESERVED.4` | `PsPreferences_Reserved4` | TField |  |  |
| 23 | `PS.PREF.RESERVED.3` | `PsPreferences_Reserved3` | TField |  |  |
| 24 | `PS.PREF.RESERVED.2` | `PsPreferences_Reserved2` | TField |  |  |
| 25 | `PS.PREF.RESERVED.1` | `PsPreferences_Reserved1` | TField |  |  |
| 26 | `PS.PREF.LOCAL.REF` | `PsPreferences_LocalRef` |  |  |  |
| 27 | `PS.PREF.OVERRIDE` | `PsPreferences_Override` |  |  |  |
| 28 | `PS.PREF.RECORD.STATUS` | `PsPreferences_RecordStatus` | String |  |  |
| 29 | `PS.PREF.CURR.NO` | `PsPreferences_CurrNo` | String |  |  |
| 30 | `PS.PREF.INPUTTER` | `PsPreferences_Inputter` |  |  |  |
| 31 | `PS.PREF.DATE.TIME` | `PsPreferences_DateTime` |  |  |  |
| 32 | `PS.PREF.AUTHORISER` | `PsPreferences_Authoriser` | String |  |  |
| 33 | `PS.PREF.CO.CODE` | `PsPreferences_CoCode` | String |  |  |
| 34 | `PS.PREF.DEPT.CODE` | `PsPreferences_DeptCode` | String |  |  |
| 35 | `PS.PREF.AUDITOR.CODE` | `PsPreferences_AuditorCode` | String |  |  |
| 36 | `PS.PREF.AUDIT.DATE.TIME` | `PsPreferences_AuditDateTime` | String |  |  |
