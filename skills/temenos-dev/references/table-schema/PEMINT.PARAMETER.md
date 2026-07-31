# PEMINT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PEMINT.PARAMETER` in `PEMINT_DDAService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEMINT.PAR.SEPERATE.NON.INSTANT.RESPONSE` | `PemintParameter_SeperateNonInstantResponse` | TField |  | Emit separate integration event for response of Non Instant payment request Validation Rules: Default value is blank. Could be set to Y. |
| 2 | `PEMINT.PAR.RESPONSE.ENRICH.API` | `PemintParameter_ResponseEnrichApi` | TField |  | Configure the API to enrich additional information on the response message Validation Rules: Must have an entry in EB.API application |
| 3 | `PEMINT.PAR.RESERVED.10` | `PemintParameter_Reserved10` |  |  |  |
| 4 | `PEMINT.PAR.RESERVED.9` | `PemintParameter_Reserved9` |  |  |  |
| 5 | `PEMINT.PAR.RESERVED.8` | `PemintParameter_Reserved8` | TField |  | Reserve field for future use. Validation Rules: |
| 6 | `PEMINT.PAR.RESERVED.7` | `PemintParameter_Reserved7` | TField |  | Reserve field for future use. Validation Rules: |
| 7 | `PEMINT.PAR.RESERVED.6` | `PemintParameter_Reserved6` | TField |  | Reserve field for future use. Validation Rules: |
| 8 | `PEMINT.PAR.RESERVED.5` | `PemintParameter_Reserved5` | TField |  | Reserve field for future use. Validation Rules: |
| 9 | `PEMINT.PAR.RESERVED.4` | `PemintParameter_Reserved4` | TField |  | Reserve field for future use. Validation Rules: |
| 10 | `PEMINT.PAR.RESERVED.3` | `PemintParameter_Reserved3` | TField |  | Reserve field for future use. Validation Rules: |
| 11 | `PEMINT.PAR.RESERVED.2` | `PemintParameter_Reserved2` | TField |  | Reserve field for future use. Validation Rules: |
| 12 | `PEMINT.PAR.RESERVED.1` | `PemintParameter_Reserved1` | TField |  | Reserve field for future use. Validation Rules: |
| 13 | `PEMINT.PAR.LOCAL.REF` | `PemintParameter_LocalRef` |  |  |  |
| 14 | `PEMINT.PAR.OVERRIDE` | `PemintParameter_Override` |  |  |  |
| 15 | `PEMINT.PAR.RECORD.STATUS` | `PemintParameter_RecordStatus` | String |  |  |
| 16 | `PEMINT.PAR.CURR.NO` | `PemintParameter_CurrNo` | String |  |  |
| 17 | `PEMINT.PAR.INPUTTER` | `PemintParameter_Inputter` |  |  |  |
| 18 | `PEMINT.PAR.DATE.TIME` | `PemintParameter_DateTime` |  |  |  |
| 19 | `PEMINT.PAR.AUTHORISER` | `PemintParameter_Authoriser` | String |  |  |
| 20 | `PEMINT.PAR.CO.CODE` | `PemintParameter_CoCode` | String |  |  |
| 21 | `PEMINT.PAR.DEPT.CODE` | `PemintParameter_DeptCode` | String |  |  |
| 22 | `PEMINT.PAR.AUDITOR.CODE` | `PemintParameter_AuditorCode` | String |  |  |
| 23 | `PEMINT.PAR.AUDIT.DATE.TIME` | `PemintParameter_AuditDateTime` | String |  |  |
