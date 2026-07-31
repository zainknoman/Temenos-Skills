# LBNCDR.SHAREHOLDER.TYPE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.SHAREHOLDER.TYPE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.SHT.DESCRIPTION` | `LbncdrShareholderType_Description` | TField |  | Any text related . Description field |
| 2 | `LBNCDR.SHT.BDL.CODE` | `LbncdrShareholderType_BdlCode` | TField |  | Hold BDL Code Value |
| 3 | `LBNCDR.SHT.RESERVED.1` | `LbncdrShareholderType_Reserved1` | TField |  |  |
| 4 | `LBNCDR.SHT.RESERVED.2` | `LbncdrShareholderType_Reserved2` | TField |  |  |
| 5 | `LBNCDR.SHT.RESERVED.3` | `LbncdrShareholderType_Reserved3` | TField |  |  |
| 6 | `LBNCDR.SHT.RESERVED.4` | `LbncdrShareholderType_Reserved4` | TField |  |  |
| 7 | `LBNCDR.SHT.RESERVED.5` | `LbncdrShareholderType_Reserved5` | TField |  |  |
| 8 | `LBNCDR.SHT.RESERVED.6` | `LbncdrShareholderType_Reserved6` | TField |  |  |
| 9 | `LBNCDR.SHT.RESERVED.7` | `LbncdrShareholderType_Reserved7` | TField |  |  |
| 10 | `LBNCDR.SHT.RESERVED.8` | `LbncdrShareholderType_Reserved8` | TField |  |  |
| 11 | `LBNCDR.SHT.LOCAL.REF` | `LbncdrShareholderType_LocalRef` |  |  |  |
| 12 | `LBNCDR.SHT.OVERRIDE` | `LbncdrShareholderType_Override` |  |  |  |
| 13 | `LBNCDR.SHT.RECORD.STATUS` | `LbncdrShareholderType_RecordStatus` | String |  |  |
| 14 | `LBNCDR.SHT.CURR.NO` | `LbncdrShareholderType_CurrNo` | String |  |  |
| 15 | `LBNCDR.SHT.INPUTTER` | `LbncdrShareholderType_Inputter` |  |  |  |
| 16 | `LBNCDR.SHT.DATE.TIME` | `LbncdrShareholderType_DateTime` |  |  |  |
| 17 | `LBNCDR.SHT.AUTHORISER` | `LbncdrShareholderType_Authoriser` | String |  |  |
| 18 | `LBNCDR.SHT.CO.CODE` | `LbncdrShareholderType_CoCode` | String |  |  |
| 19 | `LBNCDR.SHT.DEPT.CODE` | `LbncdrShareholderType_DeptCode` | String |  |  |
| 20 | `LBNCDR.SHT.AUDITOR.CODE` | `LbncdrShareholderType_AuditorCode` | String |  |  |
| 21 | `LBNCDR.SHT.AUDIT.DATE.TIME` | `LbncdrShareholderType_AuditDateTime` | String |  |  |
