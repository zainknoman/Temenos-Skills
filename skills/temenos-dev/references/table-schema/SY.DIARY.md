# SY.DIARY — Table Schema

> Source: `INSERTS/I_F.SY.DIARY` in `SY_CorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.DIA.UNDRLYNG.SECURITY` | `SyDiary_UndrlyngSecurity` | TField |  |  |
| 2 | `SY.DIA.DESCRIPTION` | `SyDiary_Description` |  |  |  |
| 3 | `SY.DIA.PROD.DEFINITION` | `SyDiary_ProdDefinition` | TField |  |  |
| 4 | `SY.DIA.DIARY.TYPE` | `SyDiary_DiaryType` | TField |  |  |
| 5 | `SY.DIA.TRADE.DATE` | `SyDiary_TradeDate` | TField |  |  |
| 6 | `SY.DIA.EX.DATE` | `SyDiary_ExDate` | TField |  |  |
| 7 | `SY.DIA.BACK.TO.BACK.DEAL` | `SyDiary_BackToBackDeal` | TField |  |  |
| 8 | `SY.DIA.ELEMENT` | `SyDiary_Element` |  |  |  |
| 9 | `SY.DIA.ELEMENT.NEW.VALUE` | `SyDiary_ElementNewValue` |  |  |  |
| 10 | `SY.DIA.ELEMENT.OLD.RATIO` | `SyDiary_ElementOldRatio` |  |  |  |
| 11 | `SY.DIA.ELEMENT.NEW.RATIO` | `SyDiary_ElementNewRatio` |  |  |  |
| 12 | `SY.DIA.RESERVED.15` | `SyDiary_Reserved15` |  |  |  |
| 13 | `SY.DIA.RESERVED.14` | `SyDiary_Reserved14` |  |  |  |
| 14 | `SY.DIA.RESERVED.13` | `SyDiary_Reserved13` |  |  |  |
| 15 | `SY.DIA.RESERVED.12` | `SyDiary_Reserved12` |  |  |  |
| 16 | `SY.DIA.RESERVED.11` | `SyDiary_Reserved11` |  |  |  |
| 17 | `SY.DIA.NEW.SECURITY` | `SyDiary_NewSecurity` | TField |  |  |
| 18 | `SY.DIA.ENT.CREATION` | `SyDiary_EntCreation` | TField |  |  |
| 19 | `SY.DIA.ROUNDING` | `SyDiary_Rounding` | TField |  |  |
| 20 | `SY.DIA.RND.FACTOR` | `SyDiary_RndFactor` | TField |  |  |
| 21 | `SY.DIA.EXCLUDE.B2B` | `SyDiary_ExcludeB2b` |  |  |  |
| 22 | `SY.DIA.ENTL.AUTHORISED` | `SyDiary_EntlAuthorised` | TField |  |  |
| 23 | `SY.DIA.ACTIVITY.CODE` | `SyDiary_ActivityCode` | TField |  |  |
| 24 | `SY.DIA.RERUN` | `SyDiary_Rerun` | TField |  |  |
| 25 | `SY.DIA.RESERVED.7` | `SyDiary_Reserved7` | TField |  |  |
| 26 | `SY.DIA.RESERVED.6` | `SyDiary_Reserved6` | TField |  |  |
| 27 | `SY.DIA.RESERVED.5` | `SyDiary_Reserved5` | TField |  |  |
| 28 | `SY.DIA.RESERVED.4` | `SyDiary_Reserved4` | TField |  |  |
| 29 | `SY.DIA.RESERVED.3` | `SyDiary_Reserved3` | TField |  |  |
| 30 | `SY.DIA.RESERVED.2` | `SyDiary_Reserved2` | TField |  |  |
| 31 | `SY.DIA.RESERVED.1` | `SyDiary_Reserved1` | TField |  |  |
| 32 | `SY.DIA.LOCAL.REF` | `SyDiary_LocalRef` |  |  |  |
| 33 | `SY.DIA.OVERRIDE` | `SyDiary_Override` |  |  |  |
| 34 | `SY.DIA.RECORD.STATUS` | `SyDiary_RecordStatus` | String |  |  |
| 35 | `SY.DIA.CURR.NO` | `SyDiary_CurrNo` | String |  |  |
| 36 | `SY.DIA.INPUTTER` | `SyDiary_Inputter` |  |  |  |
| 37 | `SY.DIA.DATE.TIME` | `SyDiary_DateTime` |  |  |  |
| 38 | `SY.DIA.AUTHORISER` | `SyDiary_Authoriser` | String |  |  |
| 39 | `SY.DIA.CO.CODE` | `SyDiary_CoCode` | String |  |  |
| 40 | `SY.DIA.DEPT.CODE` | `SyDiary_DeptCode` | String |  |  |
| 41 | `SY.DIA.AUDITOR.CODE` | `SyDiary_AuditorCode` | String |  |  |
| 42 | `SY.DIA.AUDIT.DATE.TIME` | `SyDiary_AuditDateTime` | String |  |  |
