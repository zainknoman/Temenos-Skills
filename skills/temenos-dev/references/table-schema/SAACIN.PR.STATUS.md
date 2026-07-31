# SAACIN.PR.STATUS — Table Schema

> Source: `INSERTS/I_F.SAACIN.PR.STATUS` in `SAACIN_AccountFreezing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAACIN.PR.ACCOUNT.STATUS` | `SaacinPrStatus_AccountStatus` |  |  |  |
| 2 | `SAACIN.PR.POSTING.RESTRICT` | `SaacinPrStatus_PostingRestrict` |  |  |  |
| 3 | `SAACIN.PR.RESERVED.1` | `SaacinPrStatus_Reserved1` | TField |  | reserved for future use. |
| 4 | `SAACIN.PR.RESERVED.2` | `SaacinPrStatus_Reserved2` | TField |  | reserved for future use. |
| 5 | `SAACIN.PR.RESERVED.3` | `SaacinPrStatus_Reserved3` | TField |  | reserved for future use. |
| 6 | `SAACIN.PR.RESERVED.4` | `SaacinPrStatus_Reserved4` | TField |  | reserved for future use. |
| 7 | `SAACIN.PR.RESERVED.5` | `SaacinPrStatus_Reserved5` | TField |  | reserved for future use. |
| 8 | `SAACIN.PR.RESERVED.6` | `SaacinPrStatus_Reserved6` | TField |  | reserved for future use. |
| 9 | `SAACIN.PR.RESERVED.7` | `SaacinPrStatus_Reserved7` | TField |  | reserved for future use. |
| 10 | `SAACIN.PR.RESERVED.8` | `SaacinPrStatus_Reserved8` | TField |  | reserved for future use. |
| 11 | `SAACIN.PR.RESERVED.9` | `SaacinPrStatus_Reserved9` | TField |  | reserved for future use. |
| 12 | `SAACIN.PR.RESERVED.10` | `SaacinPrStatus_Reserved10` | TField |  | reserved for future use. |
| 13 | `SAACIN.PR.RECORD.STATUS` | `SaacinPrStatus_RecordStatus` | String |  | Indicates the record status |
| 14 | `SAACIN.PR.CURR.NO` | `SaacinPrStatus_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 15 | `SAACIN.PR.INPUTTER` | `SaacinPrStatus_Inputter` |  |  |  |
| 16 | `SAACIN.PR.DATE.TIME` | `SaacinPrStatus_DateTime` |  |  |  |
| 17 | `SAACIN.PR.AUTHORISER` | `SaacinPrStatus_Authoriser` | String |  |  |
| 18 | `SAACIN.PR.CO.CODE` | `SaacinPrStatus_CoCode` | String |  |  |
| 19 | `SAACIN.PR.DEPT.CODE` | `SaacinPrStatus_DeptCode` | String |  |  |
| 20 | `SAACIN.PR.AUDITOR.CODE` | `SaacinPrStatus_AuditorCode` | String |  |  |
| 21 | `SAACIN.PR.AUDIT.DATE.TIME` | `SaacinPrStatus_AuditDateTime` | String |  |  |
