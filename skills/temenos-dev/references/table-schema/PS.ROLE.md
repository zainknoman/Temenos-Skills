# PS.ROLE — Table Schema

> Source: `INSERTS/I_F.PS.ROLE` in `EI_PresentationServices.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PS.ROLE.DESCRIPTION` | `PsRole_Description` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `PS.ROLE.DISPLAY.NAME` | `PsRole_DisplayName` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `PS.ROLE.HOMEPAGE.ID` | `PsRole_HomepageId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `PS.ROLE.CONTEXT.ID` | `PsRole_ContextId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `PS.ROLE.RESERVED.16` | `PsRole_Reserved16` | TField |  |  |
| 6 | `PS.ROLE.SYSTEM.MENU` | `PsRole_SystemMenu` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `PS.ROLE.TOP.MENU` | `PsRole_TopMenu` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `PS.ROLE.SIDE.MENU` | `PsRole_SideMenu` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `PS.ROLE.HIDDEN.MENU` | `PsRole_HiddenMenu` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `PS.ROLE.RESERVED.15` | `PsRole_Reserved15` | TField |  |  |
| 11 | `PS.ROLE.ATTRIBUTES` | `PsRole_Attributes` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `PS.ROLE.RESERVED.14` | `PsRole_Reserved14` | TField |  |  |
| 13 | `PS.ROLE.RESERVED.13` | `PsRole_Reserved13` | TField |  |  |
| 14 | `PS.ROLE.RESERVED.12` | `PsRole_Reserved12` | TField |  |  |
| 15 | `PS.ROLE.RESERVED.11` | `PsRole_Reserved11` | TField |  |  |
| 16 | `PS.ROLE.RESERVED.10` | `PsRole_Reserved10` | TField |  |  |
| 17 | `PS.ROLE.RESERVED.9` | `PsRole_Reserved9` | TField |  |  |
| 18 | `PS.ROLE.RESERVED.8` | `PsRole_Reserved8` | TField |  |  |
| 19 | `PS.ROLE.RESERVED.7` | `PsRole_Reserved7` | TField |  |  |
| 20 | `PS.ROLE.RESERVED.6` | `PsRole_Reserved6` | TField |  |  |
| 21 | `PS.ROLE.RESERVED.5` | `PsRole_Reserved5` | TField |  |  |
| 22 | `PS.ROLE.RESERVED.4` | `PsRole_Reserved4` | TField |  |  |
| 23 | `PS.ROLE.RESERVED.3` | `PsRole_Reserved3` | TField |  |  |
| 24 | `PS.ROLE.RESERVED.2` | `PsRole_Reserved2` | TField |  |  |
| 25 | `PS.ROLE.RESERVED.1` | `PsRole_Reserved1` | TField |  |  |
| 26 | `PS.ROLE.LOCAL.REF` | `PsRole_LocalRef` |  |  |  |
| 27 | `PS.ROLE.OVERRIDE` | `PsRole_Override` |  |  |  |
| 28 | `PS.ROLE.RECORD.STATUS` | `PsRole_RecordStatus` | String |  |  |
| 29 | `PS.ROLE.CURR.NO` | `PsRole_CurrNo` | String |  |  |
| 30 | `PS.ROLE.INPUTTER` | `PsRole_Inputter` |  |  |  |
| 31 | `PS.ROLE.DATE.TIME` | `PsRole_DateTime` |  |  |  |
| 32 | `PS.ROLE.AUTHORISER` | `PsRole_Authoriser` | String |  |  |
| 33 | `PS.ROLE.CO.CODE` | `PsRole_CoCode` | String |  |  |
| 34 | `PS.ROLE.DEPT.CODE` | `PsRole_DeptCode` | String |  |  |
| 35 | `PS.ROLE.AUDITOR.CODE` | `PsRole_AuditorCode` | String |  |  |
| 36 | `PS.ROLE.AUDIT.DATE.TIME` | `PsRole_AuditDateTime` | String |  |  |
