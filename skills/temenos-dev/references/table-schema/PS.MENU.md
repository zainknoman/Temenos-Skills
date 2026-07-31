# PS.MENU — Table Schema

> Source: `INSERTS/I_F.PS.MENU` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.MENU.DESCRIPTION` | `PsMenu_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `PS.MENU.ITEM.TYPE` | `PsMenu_ItemType` |  |  |  |
| 3 | `PS.MENU.ITEM.ID` | `PsMenu_ItemId` |  |  |  |
| 4 | `PS.MENU.ITEM.LABEL` | `PsMenu_ItemLabel` |  |  |  |
| 5 | `PS.MENU.RESERVE.1` | `PsMenu_Reserve1` |  |  |  |
| 6 | `PS.MENU.RESERVE.2` | `PsMenu_Reserve2` |  |  |  |
| 7 | `PS.MENU.MENU.TYPE` | `PsMenu_MenuType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `PS.MENU.RESERVED.18` | `PsMenu_Reserved18` | TField |  |  |
| 9 | `PS.MENU.RESERVED.17` | `PsMenu_Reserved17` | TField |  |  |
| 10 | `PS.MENU.RESERVED.16` | `PsMenu_Reserved16` | TField |  |  |
| 11 | `PS.MENU.RESERVED.15` | `PsMenu_Reserved15` | TField |  |  |
| 12 | `PS.MENU.RESERVED.14` | `PsMenu_Reserved14` | TField |  |  |
| 13 | `PS.MENU.RESERVED.13` | `PsMenu_Reserved13` | TField |  |  |
| 14 | `PS.MENU.RESERVED.12` | `PsMenu_Reserved12` | TField |  |  |
| 15 | `PS.MENU.RESERVED.11` | `PsMenu_Reserved11` | TField |  |  |
| 16 | `PS.MENU.RESERVED.10` | `PsMenu_Reserved10` | TField |  |  |
| 17 | `PS.MENU.RESERVED.9` | `PsMenu_Reserved9` | TField |  |  |
| 18 | `PS.MENU.RESERVED.8` | `PsMenu_Reserved8` | TField |  |  |
| 19 | `PS.MENU.RESERVED.7` | `PsMenu_Reserved7` | TField |  |  |
| 20 | `PS.MENU.RESERVED.6` | `PsMenu_Reserved6` | TField |  |  |
| 21 | `PS.MENU.RESERVED.5` | `PsMenu_Reserved5` | TField |  |  |
| 22 | `PS.MENU.RESERVED.4` | `PsMenu_Reserved4` | TField |  |  |
| 23 | `PS.MENU.RESERVED.3` | `PsMenu_Reserved3` | TField |  |  |
| 24 | `PS.MENU.RESERVED.2` | `PsMenu_Reserved2` | TField |  |  |
| 25 | `PS.MENU.RESERVED.1` | `PsMenu_Reserved1` | TField |  |  |
| 26 | `PS.MENU.LOCAL.REF` | `PsMenu_LocalRef` |  |  |  |
| 27 | `PS.MENU.OVERRIDE` | `PsMenu_Override` |  |  |  |
| 28 | `PS.MENU.RECORD.STATUS` | `PsMenu_RecordStatus` | String |  |  |
| 29 | `PS.MENU.CURR.NO` | `PsMenu_CurrNo` | String |  |  |
| 30 | `PS.MENU.INPUTTER` | `PsMenu_Inputter` |  |  |  |
| 31 | `PS.MENU.DATE.TIME` | `PsMenu_DateTime` |  |  |  |
| 32 | `PS.MENU.AUTHORISER` | `PsMenu_Authoriser` | String |  |  |
| 33 | `PS.MENU.CO.CODE` | `PsMenu_CoCode` | String |  |  |
| 34 | `PS.MENU.DEPT.CODE` | `PsMenu_DeptCode` | String |  |  |
| 35 | `PS.MENU.AUDITOR.CODE` | `PsMenu_AuditorCode` | String |  |  |
| 36 | `PS.MENU.AUDIT.DATE.TIME` | `PsMenu_AuditDateTime` | String |  |  |
