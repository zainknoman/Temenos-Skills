# WR.CONFIGURATION.ITEMS — Table Schema

> Source: `INSERTS/I_F.WR.CONFIGURATION.ITEMS` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.CI.LABEL` | `WrConfigurationItems_Label` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `WR.CI.TYPE` | `WrConfigurationItems_Type` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `WR.CI.LENGTH` | `WrConfigurationItems_Length` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `WR.CI.MANDATORY` | `WrConfigurationItems_Mandatory` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `WR.CI.COMMENT` | `WrConfigurationItems_Comment` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `WR.CI.VISIBLE` | `WrConfigurationItems_Visible` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `WR.CI.ROUTINE` | `WrConfigurationItems_Routine` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `WR.CI.ITEM.VALUE.ID` | `WrConfigurationItems_ItemValueId` |  |  |  |
| 9 | `WR.CI.ITEM.VALUE.NAME` | `WrConfigurationItems_ItemValueName` |  |  |  |
| 10 | `WR.CI.ITEM.VALUE.DEFAULT` | `WrConfigurationItems_ItemValueDefault` |  |  |  |
| 11 | `WR.CI.ITEM.VALUE.COMMENT` | `WrConfigurationItems_ItemValueComment` |  |  |  |
| 12 | `WR.CI.RESERVED.05` | `WrConfigurationItems_Reserved05` | TField |  |  |
| 13 | `WR.CI.RESERVED.04` | `WrConfigurationItems_Reserved04` | TField |  |  |
| 14 | `WR.CI.RESERVED.03` | `WrConfigurationItems_Reserved03` | TField |  |  |
| 15 | `WR.CI.RESERVED.02` | `WrConfigurationItems_Reserved02` | TField |  |  |
| 16 | `WR.CI.RESERVED.01` | `WrConfigurationItems_Reserved01` | TField |  |  |
| 17 | `WR.CI.RECORD.STATUS` | `WrConfigurationItems_RecordStatus` | String |  |  |
| 18 | `WR.CI.CURR.NO` | `WrConfigurationItems_CurrNo` | String |  |  |
| 19 | `WR.CI.INPUTTER` | `WrConfigurationItems_Inputter` |  |  |  |
| 20 | `WR.CI.DATE.TIME` | `WrConfigurationItems_DateTime` |  |  |  |
| 21 | `WR.CI.AUTHORISER` | `WrConfigurationItems_Authoriser` | String |  |  |
| 22 | `WR.CI.CO.CODE` | `WrConfigurationItems_CoCode` | String |  |  |
| 23 | `WR.CI.DEPT.CODE` | `WrConfigurationItems_DeptCode` | String |  |  |
| 24 | `WR.CI.AUDITOR.CODE` | `WrConfigurationItems_AuditorCode` | String |  |  |
| 25 | `WR.CI.AUDIT.DATE.TIME` | `WrConfigurationItems_AuditDateTime` | String |  |  |
