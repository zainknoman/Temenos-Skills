# VER.TXN.TYPE.MAP — Table Schema

> Source: `INSERTS/I_F.VER.TXN.TYPE.MAP` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VER.TXN.FT.TXN.TYPE` | `VerTxnTypeMap_FtTxnType` | TField |  |  |
| 2 | `VER.TXN.TELLER.TRANSACTION` | `VerTxnTypeMap_TellerTransaction` | TField |  |  |
| 3 | `VER.TXN.RESERVED.1` | `VerTxnTypeMap_Reserved1` | TField |  |  |
| 4 | `VER.TXN.RESERVED.2` | `VerTxnTypeMap_Reserved2` | TField |  |  |
| 5 | `VER.TXN.RESERVED.3` | `VerTxnTypeMap_Reserved3` | TField |  |  |
| 6 | `VER.TXN.RESERVED.4` | `VerTxnTypeMap_Reserved4` | TField |  |  |
| 7 | `VER.TXN.RECORD.STATUS` | `VerTxnTypeMap_RecordStatus` | String |  |  |
| 8 | `VER.TXN.CURR.NO` | `VerTxnTypeMap_CurrNo` | String |  |  |
| 9 | `VER.TXN.INPUTTER` | `VerTxnTypeMap_Inputter` |  |  |  |
| 10 | `VER.TXN.DATE.TIME` | `VerTxnTypeMap_DateTime` |  |  |  |
| 11 | `VER.TXN.AUTHORISER` | `VerTxnTypeMap_Authoriser` | String |  |  |
| 12 | `VER.TXN.CO.CODE` | `VerTxnTypeMap_CoCode` | String |  |  |
| 13 | `VER.TXN.DEPT.CODE` | `VerTxnTypeMap_DeptCode` | String |  |  |
| 14 | `VER.TXN.AUDITOR.CODE` | `VerTxnTypeMap_AuditorCode` | String |  |  |
| 15 | `VER.TXN.AUDIT.DATE.TIME` | `VerTxnTypeMap_AuditDateTime` | String |  |  |
