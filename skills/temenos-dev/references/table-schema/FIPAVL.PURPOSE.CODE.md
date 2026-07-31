# FIPAVL.PURPOSE.CODE — Table Schema

> Source: `INSERTS/I_F.FIPAVL.PURPOSE.CODE` in `FIPAVL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIPAVL.DESCRIPTION` | `FipavlPurposeCode_Description` |  |  |  |
| 2 | `FIPAVL.RESERVED.5` | `FipavlPurposeCode_Reserved5` | TField |  |  |
| 3 | `FIPAVL.RESERVED.4` | `FipavlPurposeCode_Reserved4` | TField |  |  |
| 4 | `FIPAVL.RESERVED.3` | `FipavlPurposeCode_Reserved3` | TField |  |  |
| 5 | `FIPAVL.RESERVED.2` | `FipavlPurposeCode_Reserved2` | TField |  |  |
| 6 | `FIPAVL.RESERVED.1` | `FipavlPurposeCode_Reserved1` | TField |  |  |
| 7 | `FIPAVL.OVERRIDE` | `FipavlPurposeCode_Override` |  |  |  |
| 8 | `FIPAVL.RECORD.STATUS` | `FipavlPurposeCode_RecordStatus` | String |  |  |
| 9 | `FIPAVL.CURR.NO` | `FipavlPurposeCode_CurrNo` | String |  |  |
| 10 | `FIPAVL.INPUTTER` | `FipavlPurposeCode_Inputter` |  |  |  |
| 11 | `FIPAVL.DATE.TIME` | `FipavlPurposeCode_DateTime` |  |  |  |
| 12 | `FIPAVL.AUTHORISER` | `FipavlPurposeCode_Authoriser` | String |  |  |
| 13 | `FIPAVL.CO.CODE` | `FipavlPurposeCode_CoCode` | String |  |  |
| 14 | `FIPAVL.DEPT.CODE` | `FipavlPurposeCode_DeptCode` | String |  |  |
| 15 | `FIPAVL.AUDITOR.CODE` | `FipavlPurposeCode_AuditorCode` | String |  |  |
| 16 | `FIPAVL.AUDIT.DATE.TIME` | `FipavlPurposeCode_AuditDateTime` | String |  |  |
