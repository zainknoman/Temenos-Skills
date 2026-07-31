# CAMB.ISO.ERROR.CODES — Table Schema

> Source: `INSERTS/I_F.CAMB.ISO.ERROR.CODES` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ISO.T24.ERR.DESC` | `CambIsoErrorCodes_T24ErrDesc` |  |  |  |
| 2 | `ISO.ISO.ERR.CODE` | `CambIsoErrorCodes_IsoErrCode` |  |  |  |
| 3 | `ISO.RESERVED.10` | `CambIsoErrorCodes_Reserved10` | TField |  |  |
| 4 | `ISO.RESERVED.9` | `CambIsoErrorCodes_Reserved9` | TField |  |  |
| 5 | `ISO.RESERVED.8` | `CambIsoErrorCodes_Reserved8` | TField |  |  |
| 6 | `ISO.RESERVED.7` | `CambIsoErrorCodes_Reserved7` | TField |  |  |
| 7 | `ISO.RESERVED.6` | `CambIsoErrorCodes_Reserved6` | TField |  |  |
| 8 | `ISO.RESERVED.5` | `CambIsoErrorCodes_Reserved5` | TField |  |  |
| 9 | `ISO.RESERVED.4` | `CambIsoErrorCodes_Reserved4` | TField |  |  |
| 10 | `ISO.RESERVED.3` | `CambIsoErrorCodes_Reserved3` | TField |  |  |
| 11 | `ISO.RESERVED.2` | `CambIsoErrorCodes_Reserved2` | TField |  |  |
| 12 | `ISO.RESERVED.1` | `CambIsoErrorCodes_Reserved1` | TField |  |  |
| 13 | `ISO.RECORD.STATUS` | `CambIsoErrorCodes_RecordStatus` | String |  |  |
| 14 | `ISO.CURR.NO` | `CambIsoErrorCodes_CurrNo` | String |  |  |
| 15 | `ISO.INPUTTER` | `CambIsoErrorCodes_Inputter` |  |  |  |
| 16 | `ISO.DATE.TIME` | `CambIsoErrorCodes_DateTime` |  |  |  |
| 17 | `ISO.AUTHORISER` | `CambIsoErrorCodes_Authoriser` | String |  |  |
| 18 | `ISO.CO.CODE` | `CambIsoErrorCodes_CoCode` | String |  |  |
| 19 | `ISO.DEPT.CODE` | `CambIsoErrorCodes_DeptCode` | String |  |  |
| 20 | `ISO.AUDITOR.CODE` | `CambIsoErrorCodes_AuditorCode` | String |  |  |
| 21 | `ISO.AUDIT.DATE.TIME` | `CambIsoErrorCodes_AuditDateTime` | String |  |  |
