# IL.TRANSSTATUS — Table Schema

> Source: `INSERTS/I_F.IL.TRANSSTATUS` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.TRANSSTATUS.TRANS.STATUS.NAME` | `IlTransstatus_TransStatusName` | TField | Yes | This field holds the transaction status name. Validation Rules: Standard T24 Alphanumeric field. Mandatory field and accepts upto 35 characters. |
| 2 | `IL.TRANSSTATUS.DESCRIPTION` | `IlTransstatus_Description` |  |  |  |
| 3 | `IL.TRANSSTATUS.RESERVED.10` | `IlTransstatus_Reserved10` | TField |  |  |
| 4 | `IL.TRANSSTATUS.RESERVED.9` | `IlTransstatus_Reserved9` | TField |  |  |
| 5 | `IL.TRANSSTATUS.RESERVED.8` | `IlTransstatus_Reserved8` | TField |  |  |
| 6 | `IL.TRANSSTATUS.RESERVED.7` | `IlTransstatus_Reserved7` | TField |  |  |
| 7 | `IL.TRANSSTATUS.RESERVED.6` | `IlTransstatus_Reserved6` | TField |  |  |
| 8 | `IL.TRANSSTATUS.RESERVED.5` | `IlTransstatus_Reserved5` | TField |  |  |
| 9 | `IL.TRANSSTATUS.RESERVED.4` | `IlTransstatus_Reserved4` | TField |  |  |
| 10 | `IL.TRANSSTATUS.RESERVED.3` | `IlTransstatus_Reserved3` | TField |  |  |
| 11 | `IL.TRANSSTATUS.RESERVED.2` | `IlTransstatus_Reserved2` | TField |  |  |
| 12 | `IL.TRANSSTATUS.RESERVED.1` | `IlTransstatus_Reserved1` | TField |  |  |
| 13 | `IL.TRANSSTATUS.LOCAL.REF` | `IlTransstatus_LocalRef` |  |  |  |
| 14 | `IL.TRANSSTATUS.OVERRIDE` | `IlTransstatus_Override` |  |  |  |
| 15 | `IL.TRANSSTATUS.RECORD.STATUS` | `IlTransstatus_RecordStatus` | String |  |  |
| 16 | `IL.TRANSSTATUS.CURR.NO` | `IlTransstatus_CurrNo` | String |  |  |
| 17 | `IL.TRANSSTATUS.INPUTTER` | `IlTransstatus_Inputter` |  |  |  |
| 18 | `IL.TRANSSTATUS.DATE.TIME` | `IlTransstatus_DateTime` |  |  |  |
| 19 | `IL.TRANSSTATUS.AUTHORISER` | `IlTransstatus_Authoriser` | String |  |  |
| 20 | `IL.TRANSSTATUS.CO.CODE` | `IlTransstatus_CoCode` | String |  |  |
| 21 | `IL.TRANSSTATUS.DEPT.CODE` | `IlTransstatus_DeptCode` | String |  |  |
| 22 | `IL.TRANSSTATUS.AUDITOR.CODE` | `IlTransstatus_AuditorCode` | String |  |  |
| 23 | `IL.TRANSSTATUS.AUDIT.DATE.TIME` | `IlTransstatus_AuditDateTime` | String |  |  |
