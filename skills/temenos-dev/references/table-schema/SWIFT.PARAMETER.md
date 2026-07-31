# SWIFT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SWIFT.PARAMETER` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SF.PAR.CURR.SWIFT.REL` | `SwiftParameter_CurrSwiftRel` | TField |  | This field will be used to hold the current SWIFT release. Validation Rules: Should hold a value within range 1950 - 2049. |
| 2 | `SF.PAR.PREV.SWIFT.REL` | `SwiftParameter_PrevSwiftRel` |  |  |  |
| 3 | `SF.PAR.RESTRICTED.CCY` | `SwiftParameter_RestrictedCcy` |  |  |  |
| 4 | `SF.PAR.MESSAGE.TYPE` | `SwiftParameter_MessageType` |  |  |  |
| 5 | `SF.PAR.INVALID.MSG.TYPE` | `SwiftParameter_InvalidMsgType` |  |  |  |
| 6 | `SF.PAR.UETR.MSG.TYPE` | `SwiftParameter_UetrMsgType` |  |  |  |
| 7 | `SF.PAR.FWD.MSG.TYPE` | `SwiftParameter_FwdMsgType` |  |  |  |
| 8 | `SF.PAR.ENABLE.MX` | `SwiftParameter_EnableMx` | TField |  |  |
| 9 | `SF.PAR.RESERVED.5` | `SwiftParameter_Reserved5` | TField |  |  |
| 10 | `SF.PAR.RESERVED.6` | `SwiftParameter_Reserved6` | TField |  |  |
| 11 | `SF.PAR.RESERVED.7` | `SwiftParameter_Reserved7` | TField |  |  |
| 12 | `SF.PAR.RESERVED.8` | `SwiftParameter_Reserved8` | TField |  |  |
| 13 | `SF.PAR.RESERVED.9` | `SwiftParameter_Reserved9` | TField |  |  |
| 14 | `SF.PAR.RESERVED.10` | `SwiftParameter_Reserved10` | TField |  |  |
| 15 | `SF.PAR.RESERVED.11` | `SwiftParameter_Reserved11` | TField |  |  |
| 16 | `SF.PAR.RESERVED.12` | `SwiftParameter_Reserved12` | TField |  |  |
| 17 | `SF.PAR.RESERVED.13` | `SwiftParameter_Reserved13` | TField |  |  |
| 18 | `SF.PAR.RESERVED.14` | `SwiftParameter_Reserved14` | TField |  |  |
| 19 | `SF.PAR.RESERVED.15` | `SwiftParameter_Reserved15` | TField |  |  |
| 20 | `SF.PAR.RESERVED.16` | `SwiftParameter_Reserved16` | TField |  |  |
| 21 | `SF.PAR.RESERVED.17` | `SwiftParameter_Reserved17` | TField |  |  |
| 22 | `SF.PAR.RESERVED.18` | `SwiftParameter_Reserved18` | TField |  |  |
| 23 | `SF.PAR.RESERVED.19` | `SwiftParameter_Reserved19` | TField |  |  |
| 24 | `SF.PAR.RESERVED.20` | `SwiftParameter_Reserved20` | TField |  |  |
| 25 | `SF.PAR.LOCAL.REF` | `SwiftParameter_LocalRef` |  |  |  |
| 26 | `SF.PAR.OVERRIDE` | `SwiftParameter_Override` |  |  |  |
| 27 | `SF.PAR.RECORD.STATUS` | `SwiftParameter_RecordStatus` | String |  |  |
| 28 | `SF.PAR.CURR.NO` | `SwiftParameter_CurrNo` | String |  |  |
| 29 | `SF.PAR.INPUTTER` | `SwiftParameter_Inputter` |  |  |  |
| 30 | `SF.PAR.DATE.TIME` | `SwiftParameter_DateTime` |  |  |  |
| 31 | `SF.PAR.AUTHORISER` | `SwiftParameter_Authoriser` | String |  |  |
| 32 | `SF.PAR.CO.CODE` | `SwiftParameter_CoCode` | String |  |  |
| 33 | `SF.PAR.DEPT.CODE` | `SwiftParameter_DeptCode` | String |  |  |
| 34 | `SF.PAR.AUDITOR.CODE` | `SwiftParameter_AuditorCode` | String |  |  |
| 35 | `SF.PAR.AUDIT.DATE.TIME` | `SwiftParameter_AuditDateTime` | String |  |  |
| 36 | `SF.PAR.MANUAL.PREV.SWIFT.REL` | `SwiftParameter_ManPrevSwiftRel` |  |  |  |
