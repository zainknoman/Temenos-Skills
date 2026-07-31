# AM.GROUP.TYPE — Table Schema

> Source: `INSERTS/I_F.AM.GROUP.TYPE` in `AM_Group.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.GTY.DESCRIPTION` | `AmGroupType_Description` |  |  |  |
| 2 | `AM.GTY.SHORT.NAME` | `AmGroupType_ShortName` |  |  |  |
| 3 | `AM.GTY.BLOCKED.PORT.TYPE` | `AmGroupType_BlockedPortType` |  |  |  |
| 4 | `AM.GTY.BLOCKED.PORT.ERR` | `AmGroupType_BlockedPortErr` |  |  |  |
| 5 | `AM.GTY.PERFORMANCE` | `AmGroupType_Performance` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `AM.GTY.REBALANCING` | `AmGroupType_Rebalancing` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AM.GTY.UNIQUE.MBRSHIP` | `AmGroupType_UniqueMbrship` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `AM.GTY.GRP.VALID.RTN` | `AmGroupType_GrpValidRtn` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `AM.GTY.RESERVED.07` | `AmGroupType_Reserved07` | TField |  |  |
| 10 | `AM.GTY.RESERVED.06` | `AmGroupType_Reserved06` | TField |  |  |
| 11 | `AM.GTY.RESERVED.05` | `AmGroupType_Reserved05` | TField |  |  |
| 12 | `AM.GTY.RESERVED.04` | `AmGroupType_Reserved04` | TField |  |  |
| 13 | `AM.GTY.RESERVED.03` | `AmGroupType_Reserved03` | TField |  |  |
| 14 | `AM.GTY.RESERVED.02` | `AmGroupType_Reserved02` | TField |  |  |
| 15 | `AM.GTY.RESERVED.01` | `AmGroupType_Reserved01` | TField |  |  |
| 16 | `AM.GTY.LOCAL.REF` | `AmGroupType_LocalRef` |  |  |  |
| 17 | `AM.GTY.RECORD.STATUS` | `AmGroupType_RecordStatus` | String |  |  |
| 18 | `AM.GTY.CURR.NO` | `AmGroupType_CurrNo` | String |  |  |
| 19 | `AM.GTY.INPUTTER` | `AmGroupType_Inputter` |  |  |  |
| 20 | `AM.GTY.DATE.TIME` | `AmGroupType_DateTime` |  |  |  |
| 21 | `AM.GTY.AUTHORISER` | `AmGroupType_Authoriser` | String |  |  |
| 22 | `AM.GTY.CO.CODE` | `AmGroupType_CoCode` | String |  |  |
| 23 | `AM.GTY.DEPT.CODE` | `AmGroupType_DeptCode` | String |  |  |
| 24 | `AM.GTY.AUDITOR.CODE` | `AmGroupType_AuditorCode` | String |  |  |
| 25 | `AM.GTY.AUDIT.DATE.TIME` | `AmGroupType_AuditDateTime` | String |  |  |
