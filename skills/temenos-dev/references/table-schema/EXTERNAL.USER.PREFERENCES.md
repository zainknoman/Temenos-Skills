# EXTERNAL.USER.PREFERENCES — Table Schema

> Source: `INSERTS/I_F.EXTERNAL.USER.PREFERENCES` in `T2_Preferences.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.USER.PREF.GROUP.NAME` | `ExternalUserPreferences_GroupName` | TField |  |  |
| 2 | `EXT.USER.PREF.GROUP.DESCRIPTION` | `ExternalUserPreferences_GroupDescription` | TField |  |  |
| 3 | `EXT.USER.PREF.GROUP.POSITION` | `ExternalUserPreferences_GroupPosition` | TField |  |  |
| 4 | `EXT.USER.PREF.FAVOURITE.GROUP` | `ExternalUserPreferences_FavouriteGroup` | TField |  |  |
| 5 | `EXT.USER.PREF.CUSTOMER` | `ExternalUserPreferences_Customer` |  |  |  |
| 6 | `EXT.USER.PREF.PRODUCT.LINE` | `ExternalUserPreferences_ProductLine` |  |  |  |
| 7 | `EXT.USER.PREF.PRODUCT.GROUP` | `ExternalUserPreferences_ProductGroup` |  |  |  |
| 8 | `EXT.USER.PREF.PRODUCT` | `ExternalUserPreferences_Product` |  |  |  |
| 9 | `EXT.USER.PREF.PRODUCT.LABEL` | `ExternalUserPreferences_ProductLabel` |  |  |  |
| 10 | `EXT.USER.PREF.PRODUCT.POSITION` | `ExternalUserPreferences_ProductPosition` |  |  |  |
| 11 | `EXT.USER.PREF.PRD.FAV.RESERVED.2` | `ExternalUserPreferences_PrdFavReserved2` |  |  |  |
| 12 | `EXT.USER.PREF.PRD.FAV.RESERVED.1` | `ExternalUserPreferences_PrdFavReserved1` |  |  |  |
| 13 | `EXT.USER.PREF.FAV.RESERVED.2` | `ExternalUserPreferences_FavReserved2` |  |  |  |
| 14 | `EXT.USER.PREF.FAV.RESERVED.1` | `ExternalUserPreferences_FavReserved1` |  |  |  |
| 15 | `EXT.USER.PREF.BAL.CUSTOMER` | `ExternalUserPreferences_BalCustomer` |  |  |  |
| 16 | `EXT.USER.PREF.BAL.PRODUCT.LINE` | `ExternalUserPreferences_BalProductLine` |  |  |  |
| 17 | `EXT.USER.PREF.BAL.PRODUCT.GROUP` | `ExternalUserPreferences_BalProductGroup` |  |  |  |
| 18 | `EXT.USER.PREF.BAL.PRODUCT` | `ExternalUserPreferences_BalProduct` |  |  |  |
| 19 | `EXT.USER.PREF.PRD.BAL.RESERVED.2` | `ExternalUserPreferences_PrdBalReserved2` |  |  |  |
| 20 | `EXT.USER.PREF.PRD.BAL.RESERVED.1` | `ExternalUserPreferences_PrdBalReserved1` |  |  |  |
| 21 | `EXT.USER.PREF.BAL.RESERVED.2` | `ExternalUserPreferences_BalReserved2` |  |  |  |
| 22 | `EXT.USER.PREF.BAL.RESERVED.1` | `ExternalUserPreferences_BalReserved1` |  |  |  |
| 23 | `EXT.USER.PREF.SERVICE.NAME` | `ExternalUserPreferences_ServiceName` |  |  |  |
| 24 | `EXT.USER.PREF.SER.RESERVED.4` | `ExternalUserPreferences_SerReserved4` |  |  |  |
| 25 | `EXT.USER.PREF.SER.RESERVED.3` | `ExternalUserPreferences_SerReserved3` |  |  |  |
| 26 | `EXT.USER.PREF.SER.RESERVED.2` | `ExternalUserPreferences_SerReserved2` |  |  |  |
| 27 | `EXT.USER.PREF.SER.RESERVED.1` | `ExternalUserPreferences_SerReserved1` |  |  |  |
| 28 | `EXT.USER.PREF.RESERVED.24` | `ExternalUserPreferences_Reserved24` | TField |  |  |
| 29 | `EXT.USER.PREF.RESERVED.23` | `ExternalUserPreferences_Reserved23` | TField |  |  |
| 30 | `EXT.USER.PREF.RESERVED.22` | `ExternalUserPreferences_Reserved22` | TField |  |  |
| 31 | `EXT.USER.PREF.RESERVED.21` | `ExternalUserPreferences_Reserved21` | TField |  |  |
| 32 | `EXT.USER.PREF.RESERVED.20` | `ExternalUserPreferences_Reserved20` | TField |  |  |
| 33 | `EXT.USER.PREF.RESERVED.19` | `ExternalUserPreferences_Reserved19` | TField |  |  |
| 34 | `EXT.USER.PREF.RESERVED.18` | `ExternalUserPreferences_Reserved18` | TField |  |  |
| 35 | `EXT.USER.PREF.RESERVED.17` | `ExternalUserPreferences_Reserved17` | TField |  |  |
| 36 | `EXT.USER.PREF.RESERVED.16` | `ExternalUserPreferences_Reserved16` | TField |  |  |
| 37 | `EXT.USER.PREF.RESERVED.15` | `ExternalUserPreferences_Reserved15` | TField |  |  |
| 38 | `EXT.USER.PREF.RESERVED.14` | `ExternalUserPreferences_Reserved14` | TField |  |  |
| 39 | `EXT.USER.PREF.RESERVED.13` | `ExternalUserPreferences_Reserved13` | TField |  |  |
| 40 | `EXT.USER.PREF.RESERVED.12` | `ExternalUserPreferences_Reserved12` | TField |  |  |
| 41 | `EXT.USER.PREF.RESERVED.11` | `ExternalUserPreferences_Reserved11` | TField |  |  |
| 42 | `EXT.USER.PREF.RESERVED.10` | `ExternalUserPreferences_Reserved10` | TField |  |  |
| 43 | `EXT.USER.PREF.RESERVED.9` | `ExternalUserPreferences_Reserved9` | TField |  |  |
| 44 | `EXT.USER.PREF.RESERVED.8` | `ExternalUserPreferences_Reserved8` | TField |  |  |
| 45 | `EXT.USER.PREF.RESERVED.7` | `ExternalUserPreferences_Reserved7` | TField |  |  |
| 46 | `EXT.USER.PREF.RESERVED.6` | `ExternalUserPreferences_Reserved6` | TField |  |  |
| 47 | `EXT.USER.PREF.RESERVED.5` | `ExternalUserPreferences_Reserved5` | TField |  |  |
| 48 | `EXT.USER.PREF.RESERVED.4` | `ExternalUserPreferences_Reserved4` | TField |  |  |
| 49 | `EXT.USER.PREF.RESERVED.3` | `ExternalUserPreferences_Reserved3` | TField |  |  |
| 50 | `EXT.USER.PREF.RESERVED.2` | `ExternalUserPreferences_Reserved2` | TField |  |  |
| 51 | `EXT.USER.PREF.RESERVED.1` | `ExternalUserPreferences_Reserved1` | TField |  |  |
| 52 | `EXT.USER.PREF.LOCAL.REF` | `ExternalUserPreferences_LocalRef` |  |  |  |
| 53 | `EXT.USER.PREF.OVERRIDE` | `ExternalUserPreferences_Override` |  |  |  |
| 54 | `EXT.USER.PREF.RECORD.STATUS` | `ExternalUserPreferences_RecordStatus` | String |  |  |
| 55 | `EXT.USER.PREF.CURR.NO` | `ExternalUserPreferences_CurrNo` | String |  |  |
| 56 | `EXT.USER.PREF.INPUTTER` | `ExternalUserPreferences_Inputter` |  |  |  |
| 57 | `EXT.USER.PREF.DATE.TIME` | `ExternalUserPreferences_DateTime` |  |  |  |
| 58 | `EXT.USER.PREF.AUTHORISER` | `ExternalUserPreferences_Authoriser` | String |  |  |
| 59 | `EXT.USER.PREF.CO.CODE` | `ExternalUserPreferences_CoCode` | String |  |  |
| 60 | `EXT.USER.PREF.DEPT.CODE` | `ExternalUserPreferences_DeptCode` | String |  |  |
| 61 | `EXT.USER.PREF.AUDITOR.CODE` | `ExternalUserPreferences_AuditorCode` | String |  |  |
| 62 | `EXT.USER.PREF.AUDIT.DATE.TIME` | `ExternalUserPreferences_AuditDateTime` | String |  |  |
