# EP.XML.VALIDATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EP.XML.VALIDATION.PARAMETER` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EP.XML.VAL.DESCRIPTION` | `EpXmlValidationParameter_Description` |  |  |  |
| 2 | `EP.XML.VAL.VAL.DESCRIPTION` | `EpXmlValidationParameter_ValDescription` |  |  |  |
| 3 | `EP.XML.VAL.STP.STATUS` | `EpXmlValidationParameter_StpStatus` |  |  |  |
| 4 | `EP.XML.VAL.STP.VAL.RNT` | `EpXmlValidationParameter_StpValRnt` |  |  |  |
| 5 | `EP.XML.VAL.ALLOWED.MESSAGE` | `EpXmlValidationParameter_AllowedMessage` |  |  |  |
| 6 | `EP.XML.VAL.EXCEPTION.MESSAGE` | `EpXmlValidationParameter_ExceptionMessage` |  |  |  |
| 7 | `EP.XML.VAL.NEXT.ACTION.RNT` | `EpXmlValidationParameter_NextActionRnt` |  |  |  |
| 8 | `EP.XML.VAL.RESERVED15` | `EpXmlValidationParameter_Reserved15` |  |  |  |
| 9 | `EP.XML.VAL.RESERVED14` | `EpXmlValidationParameter_Reserved14` |  |  |  |
| 10 | `EP.XML.VAL.RESERVED13` | `EpXmlValidationParameter_Reserved13` |  |  |  |
| 11 | `EP.XML.VAL.RESERVED12` | `EpXmlValidationParameter_Reserved12` |  |  |  |
| 12 | `EP.XML.VAL.RESERVED11` | `EpXmlValidationParameter_Reserved11` |  |  |  |
| 13 | `EP.XML.VAL.ERROR.VAL.TYPE` | `EpXmlValidationParameter_ErrorValType` | TField |  | This field controls the exit process in case of validation failure. Allowed Values FRST - Will stop the process and exit the flow soon after the first occurrence of the error is returned by the routine attached to the field STP.VAL.RTN NACT - Will stop the process and exit the flow soon after the first occurrence of the error is returned by the routine attached to the field NEXT.ACTION.RNT |
| 14 | `EP.XML.VAL.RESERVED.09` | `EpXmlValidationParameter_Reserved09` | TField |  |  |
| 15 | `EP.XML.VAL.RESERVED.08` | `EpXmlValidationParameter_Reserved08` | TField |  |  |
| 16 | `EP.XML.VAL.RESERVED.07` | `EpXmlValidationParameter_Reserved07` | TField |  |  |
| 17 | `EP.XML.VAL.RESERVED.06` | `EpXmlValidationParameter_Reserved06` | TField |  |  |
| 18 | `EP.XML.VAL.RESERVED.05` | `EpXmlValidationParameter_Reserved05` | TField |  |  |
| 19 | `EP.XML.VAL.RESERVED.04` | `EpXmlValidationParameter_Reserved04` | TField |  |  |
| 20 | `EP.XML.VAL.RESERVED.03` | `EpXmlValidationParameter_Reserved03` | TField |  |  |
| 21 | `EP.XML.VAL.RESERVED.02` | `EpXmlValidationParameter_Reserved02` | TField |  |  |
| 22 | `EP.XML.VAL.RESERVED.01` | `EpXmlValidationParameter_Reserved01` | TField |  |  |
| 23 | `EP.XML.VAL.LOCAL.REF` | `EpXmlValidationParameter_LocalRef` |  |  |  |
| 24 | `EP.XML.VAL.OVERRIDE` | `EpXmlValidationParameter_Override` |  |  |  |
| 25 | `EP.XML.VAL.RECORD.STATUS` | `EpXmlValidationParameter_RecordStatus` | String |  |  |
| 26 | `EP.XML.VAL.CURR.NO` | `EpXmlValidationParameter_CurrNo` | String |  |  |
| 27 | `EP.XML.VAL.INPUTTER` | `EpXmlValidationParameter_Inputter` |  |  |  |
| 28 | `EP.XML.VAL.DATE.TIME` | `EpXmlValidationParameter_DateTime` |  |  |  |
| 29 | `EP.XML.VAL.AUTHORISER` | `EpXmlValidationParameter_Authoriser` | String |  |  |
| 30 | `EP.XML.VAL.CO.CODE` | `EpXmlValidationParameter_CoCode` | String |  |  |
| 31 | `EP.XML.VAL.DEPT.CODE` | `EpXmlValidationParameter_DeptCode` | String |  |  |
| 32 | `EP.XML.VAL.AUDITOR.CODE` | `EpXmlValidationParameter_AuditorCode` | String |  |  |
| 33 | `EP.XML.VAL.AUDIT.DATE.TIME` | `EpXmlValidationParameter_AuditDateTime` | String |  |  |
