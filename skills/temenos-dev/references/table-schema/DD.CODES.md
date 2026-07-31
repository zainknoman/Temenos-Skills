# DD.CODES — Table Schema

> Source: `INSERTS/I_F.DD.CODES` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.CODE.DD.EVENT` | `DdCodes_DdEvent` |  |  |  |
| 2 | `DD.CODE.REASON.CODES` | `DdCodes_ReasonCodes` |  |  |  |
| 3 | `DD.CODE.HOLD.REASON.CODE` | `DdCodes_HoldReasonCode` |  |  |  |
| 4 | `DD.CODE.RESUBMIT.EXCL.CODE` | `DdCodes_ResubmitExclCode` |  |  |  |
| 5 | `DD.CODE.RESERVED08` | `DdCodes_Reserved08` |  |  |  |
| 6 | `DD.CODE.RESERVED07` | `DdCodes_Reserved07` |  |  |  |
| 7 | `DD.CODE.RESERVED06` | `DdCodes_Reserved06` |  |  |  |
| 8 | `DD.CODE.RESERVED05` | `DdCodes_Reserved05` | TField |  |  |
| 9 | `DD.CODE.RESERVED04` | `DdCodes_Reserved04` | TField |  |  |
| 10 | `DD.CODE.RESERVED03` | `DdCodes_Reserved03` | TField |  |  |
| 11 | `DD.CODE.RESERVED02` | `DdCodes_Reserved02` | TField |  |  |
| 12 | `DD.CODE.RESERVED01` | `DdCodes_Reserved01` | TField |  |  |
| 13 | `DD.CODE.LOCAL.REF` | `DdCodes_LocalRef` |  |  |  |
| 14 | `DD.CODE.OVERRIDE` | `DdCodes_Override` |  |  |  |
| 15 | `DD.CODE.RECORD.STATUS` | `DdCodes_RecordStatus` | String |  |  |
| 16 | `DD.CODE.CURR.NO` | `DdCodes_CurrNo` | String |  |  |
| 17 | `DD.CODE.INPUTTER` | `DdCodes_Inputter` |  |  |  |
| 18 | `DD.CODE.DATE.TIME` | `DdCodes_DateTime` |  |  |  |
| 19 | `DD.CODE.AUTHORISER` | `DdCodes_Authoriser` | String |  |  |
| 20 | `DD.CODE.CO.CODE` | `DdCodes_CoCode` | String |  |  |
| 21 | `DD.CODE.DEPT.CODE` | `DdCodes_DeptCode` | String |  |  |
| 22 | `DD.CODE.AUDITOR.CODE` | `DdCodes_AuditorCode` | String |  |  |
| 23 | `DD.CODE.AUDIT.DATE.TIME` | `DdCodes_AuditDateTime` | String |  |  |
