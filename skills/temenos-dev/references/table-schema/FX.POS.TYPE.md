# FX.POS.TYPE — Table Schema

> Source: `INSERTS/I_F.FX.POS.TYPE` in `RE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.PT.DESCRIPTION` | `FxPosType_Description` |  |  |  |
| 2 | `FX.PT.PL.PREFIX` | `FxPosType_PlPrefix` | TField |  | DETAIL- The first component of the CPL key for Non-contingent entries. RULE 4 type SSS (Alphanumeric SWIFT) characters |
| 3 | `FX.PT.PL.CONT.CODE` | `FxPosType_PlContCode` | TField |  | DETAIL The first component of the CPL key for Contingent entries. RULE 4 type SSS (Alphanumeric SWIFT) characters |
| 4 | `FX.PT.PL.SELF.BAL` | `FxPosType_PlSelfBal` | TField |  | DETAIL ? The first component of the CPL key for Self-balancing entries. RULE ? 4 type SSS (Alphanumeric SWIFT) characters |
| 5 | `FX.PT.RESERVED9` | `FxPosType_Reserved9` | TField |  |  |
| 6 | `FX.PT.RESERVED8` | `FxPosType_Reserved8` | TField |  |  |
| 7 | `FX.PT.RESERVED7` | `FxPosType_Reserved7` | TField |  |  |
| 8 | `FX.PT.RESERVED6` | `FxPosType_Reserved6` | TField |  |  |
| 9 | `FX.PT.RESERVED5` | `FxPosType_Reserved5` | TField |  |  |
| 10 | `FX.PT.RESERVED4` | `FxPosType_Reserved4` | TField |  |  |
| 11 | `FX.PT.RESERVED3` | `FxPosType_Reserved3` | TField |  |  |
| 12 | `FX.PT.RESERVED2` | `FxPosType_Reserved2` | TField |  |  |
| 13 | `FX.PT.RESERVED1` | `FxPosType_Reserved1` | TField |  |  |
| 14 | `FX.PT.LOCAL.REF` | `FxPosType_LocalRef` |  |  |  |
| 15 | `FX.PT.OVERRIDE` | `FxPosType_Override` |  |  |  |
| 16 | `FX.PT.RECORD.STATUS` | `FxPosType_RecordStatus` | String |  |  |
| 17 | `FX.PT.CURR.NO` | `FxPosType_CurrNo` | String |  |  |
| 18 | `FX.PT.INPUTTER` | `FxPosType_Inputter` |  |  |  |
| 19 | `FX.PT.DATE.TIME` | `FxPosType_DateTime` |  |  |  |
| 20 | `FX.PT.AUTHORISER` | `FxPosType_Authoriser` | String |  |  |
| 21 | `FX.PT.CO.CODE` | `FxPosType_CoCode` | String |  |  |
| 22 | `FX.PT.DEPT.CODE` | `FxPosType_DeptCode` | String |  |  |
| 23 | `FX.PT.AUDITOR.CODE` | `FxPosType_AuditorCode` | String |  |  |
| 24 | `FX.PT.AUDIT.DATE.TIME` | `FxPosType_AuditDateTime` | String |  |  |
