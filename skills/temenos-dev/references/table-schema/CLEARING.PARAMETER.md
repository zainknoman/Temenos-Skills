# CLEARING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CLEARING.PARAMETER` in `ACCCSM_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.PAR.DESCRIPTION` | `ClearingParameter_Description` | TField |  | Description of the record. |
| 2 | `CL.PAR.BEST.MATCH` | `ClearingParameter_BestMatch` | TField |  | This field indicates whether best match (closest match) functionality of generic accounting system is opted or not. If it is set to Yes, on each creation, updation and cancellation of AC.LOCKED.EVENTS, the reservation (locked) balance will be merged to use for best match during BOOK transactions via generic accounting interface. |
| 3 | `CL.PAR.RESERVED.20` | `ClearingParameter_Reserved20` | TField |  |  |
| 4 | `CL.PAR.RESERVED.19` | `ClearingParameter_Reserved19` | TField |  |  |
| 5 | `CL.PAR.RESERVED.18` | `ClearingParameter_Reserved18` | TField |  |  |
| 6 | `CL.PAR.RESERVED.17` | `ClearingParameter_Reserved17` | TField |  |  |
| 7 | `CL.PAR.RESERVED.16` | `ClearingParameter_Reserved16` | TField |  |  |
| 8 | `CL.PAR.RESERVED.15` | `ClearingParameter_Reserved15` | TField |  |  |
| 9 | `CL.PAR.RESERVED.14` | `ClearingParameter_Reserved14` | TField |  |  |
| 10 | `CL.PAR.RESERVED.13` | `ClearingParameter_Reserved13` | TField |  |  |
| 11 | `CL.PAR.RESERVED.12` | `ClearingParameter_Reserved12` | TField |  |  |
| 12 | `CL.PAR.RESERVED.11` | `ClearingParameter_Reserved11` | TField |  |  |
| 13 | `CL.PAR.RESERVED.10` | `ClearingParameter_Reserved10` | TField |  |  |
| 14 | `CL.PAR.RESERVED.09` | `ClearingParameter_Reserved09` | TField |  |  |
| 15 | `CL.PAR.RESERVED.08` | `ClearingParameter_Reserved08` | TField |  |  |
| 16 | `CL.PAR.RESERVED.07` | `ClearingParameter_Reserved07` | TField |  |  |
| 17 | `CL.PAR.RESERVED.06` | `ClearingParameter_Reserved06` | TField |  |  |
| 18 | `CL.PAR.RESERVED.05` | `ClearingParameter_Reserved05` | TField |  |  |
| 19 | `CL.PAR.RESERVED.04` | `ClearingParameter_Reserved04` | TField |  |  |
| 20 | `CL.PAR.RESERVED.03` | `ClearingParameter_Reserved03` | TField |  |  |
| 21 | `CL.PAR.RESERVED.02` | `ClearingParameter_Reserved02` | TField |  |  |
| 22 | `CL.PAR.RESERVED.01` | `ClearingParameter_Reserved01` | TField |  |  |
| 23 | `CL.PAR.LOCAL.REF` | `ClearingParameter_LocalRef` |  |  |  |
| 24 | `CL.PAR.OVERRIDE` | `ClearingParameter_Override` |  |  |  |
| 25 | `CL.PAR.RECORD.STATUS` | `ClearingParameter_RecordStatus` | String |  |  |
| 26 | `CL.PAR.CURR.NO` | `ClearingParameter_CurrNo` | String |  |  |
| 27 | `CL.PAR.INPUTTER` | `ClearingParameter_Inputter` |  |  |  |
| 28 | `CL.PAR.DATE.TIME` | `ClearingParameter_DateTime` |  |  |  |
| 29 | `CL.PAR.AUTHORISER` | `ClearingParameter_Authoriser` | String |  |  |
| 30 | `CL.PAR.CO.CODE` | `ClearingParameter_CoCode` | String |  |  |
| 31 | `CL.PAR.DEPT.CODE` | `ClearingParameter_DeptCode` | String |  |  |
| 32 | `CL.PAR.AUDITOR.CODE` | `ClearingParameter_AuditorCode` | String |  |  |
| 33 | `CL.PAR.AUDIT.DATE.TIME` | `ClearingParameter_AuditDateTime` | String |  |  |
