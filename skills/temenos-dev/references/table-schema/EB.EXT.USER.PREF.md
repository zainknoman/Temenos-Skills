# EB.EXT.USER.PREF — Table Schema

> Source: `INSERTS/I_F.EB.EXT.USER.PREF` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.USR.PREF.USER.GRP.NAME` | `EbExtUserPref_UserGrpName` | TField |  |  |
| 2 | `EXT.USR.PREF.USER.GRP.DESC` | `EbExtUserPref_UserGrpDesc` | TField |  |  |
| 3 | `EXT.USR.PREF.USER.ACCOUNTS` | `EbExtUserPref_UserAccounts` |  |  |  |
| 4 | `EXT.USR.PREF.USER.GROUP.POS` | `EbExtUserPref_UserGroupPos` | TField |  |  |
| 5 | `EXT.USR.PREF.USER.GRP.FAV` | `EbExtUserPref_UserGrpFav` | TField |  |  |
| 6 | `EXT.USR.PREF.PFM.ACTIVATE` | `EbExtUserPref_PfmActivate` | TField |  |  |
| 7 | `EXT.USR.PREF.RESERVED.07` | `EbExtUserPref_Reserved07` | TField |  |  |
| 8 | `EXT.USR.PREF.RESERVED.06` | `EbExtUserPref_Reserved06` | TField |  |  |
| 9 | `EXT.USR.PREF.RESERVED.05` | `EbExtUserPref_Reserved05` | TField |  |  |
| 10 | `EXT.USR.PREF.RESERVED.04` | `EbExtUserPref_Reserved04` | TField |  |  |
| 11 | `EXT.USR.PREF.RESERVED.03` | `EbExtUserPref_Reserved03` | TField |  |  |
| 12 | `EXT.USR.PREF.RESERVED.02` | `EbExtUserPref_Reserved02` | TField |  |  |
| 13 | `EXT.USR.PREF.RESERVED.01` | `EbExtUserPref_Reserved01` | TField |  |  |
| 14 | `EXT.USR.PREF.RECORD.STATUS` | `EbExtUserPref_RecordStatus` | String |  |  |
| 15 | `EXT.USR.PREF.CURR.NO` | `EbExtUserPref_CurrNo` | String |  |  |
| 16 | `EXT.USR.PREF.INPUTTER` | `EbExtUserPref_Inputter` |  |  |  |
| 17 | `EXT.USR.PREF.DATE.TIME` | `EbExtUserPref_DateTime` |  |  |  |
| 18 | `EXT.USR.PREF.AUTHORISER` | `EbExtUserPref_Authoriser` | String |  |  |
| 19 | `EXT.USR.PREF.CO.CODE` | `EbExtUserPref_CoCode` | String |  |  |
| 20 | `EXT.USR.PREF.DEPT.CODE` | `EbExtUserPref_DeptCode` | String |  |  |
| 21 | `EXT.USR.PREF.AUDITOR.CODE` | `EbExtUserPref_AuditorCode` | String |  |  |
| 22 | `EXT.USR.PREF.AUDIT.DATE.TIME` | `EbExtUserPref_AuditDateTime` | String |  |  |
