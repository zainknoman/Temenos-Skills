# BM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BM.PARAMETER` in `BM_Core.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BM.PAR.ENABLED` | `BmParameter_Enabled` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `BM.PAR.EVENTS` | `BmParameter_Events` |  |  |  |
| 3 | `BM.PAR.RESERVED.12` | `BmParameter_Reserved12` | TField |  |  |
| 4 | `BM.PAR.RESERVED.11` | `BmParameter_Reserved11` | TField |  |  |
| 5 | `BM.PAR.QUEUE.SIZE` | `BmParameter_QueueSize` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `BM.PAR.DISPATCH.INTERVAL` | `BmParameter_DispatchInterval` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `BM.PAR.RESERVED.10` | `BmParameter_Reserved10` | TField |  |  |
| 8 | `BM.PAR.RESERVED.09` | `BmParameter_Reserved09` | TField |  |  |
| 9 | `BM.PAR.RESERVED.08` | `BmParameter_Reserved08` | TField |  |  |
| 10 | `BM.PAR.RESERVED.07` | `BmParameter_Reserved07` | TField |  |  |
| 11 | `BM.PAR.RESERVED.06` | `BmParameter_Reserved06` | TField |  |  |
| 12 | `BM.PAR.RESERVED.05` | `BmParameter_Reserved05` | TField |  |  |
| 13 | `BM.PAR.RESERVED.04` | `BmParameter_Reserved04` | TField |  |  |
| 14 | `BM.PAR.RESERVED.03` | `BmParameter_Reserved03` | TField |  |  |
| 15 | `BM.PAR.RESERVED.02` | `BmParameter_Reserved02` | TField |  |  |
| 16 | `BM.PAR.RESERVED.01` | `BmParameter_Reserved01` | TField |  |  |
| 17 | `BM.PAR.RECORD.STATUS` | `BmParameter_RecordStatus` | String |  |  |
| 18 | `BM.PAR.CURR.NO` | `BmParameter_CurrNo` | String |  |  |
| 19 | `BM.PAR.INPUTTER` | `BmParameter_Inputter` |  |  |  |
| 20 | `BM.PAR.DATE.TIME` | `BmParameter_DateTime` |  |  |  |
| 21 | `BM.PAR.AUTHORISER` | `BmParameter_Authoriser` | String |  |  |
| 22 | `BM.PAR.CO.CODE` | `BmParameter_CoCode` | String |  |  |
| 23 | `BM.PAR.DEPT.CODE` | `BmParameter_DeptCode` | String |  |  |
| 24 | `BM.PAR.AUDITOR.CODE` | `BmParameter_AuditorCode` | String |  |  |
| 25 | `BM.PAR.AUDIT.DATE.TIME` | `BmParameter_AuditDateTime` | String |  |  |
