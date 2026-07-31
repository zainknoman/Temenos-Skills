# EB.EXTERNAL.REST.API.JWT — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.REST.API.JWT` in `BE_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `JWT.GEN.DESCRIPTION` | `EbExternalRestApiJwt_Description` |  |  |  |
| 2 | `JWT.GEN.CLAIM.NAME` | `EbExternalRestApiJwt_ClaimName` |  |  |  |
| 3 | `JWT.GEN.CLAIM.VALUE` | `EbExternalRestApiJwt_ClaimValue` |  |  |  |
| 4 | `JWT.GEN.RESFIELD.4` | `EbExternalRestApiJwt_Resfield4` |  |  |  |
| 5 | `JWT.GEN.RESFIELD.3` | `EbExternalRestApiJwt_Resfield3` |  |  |  |
| 6 | `JWT.GEN.RESFIELD.2` | `EbExternalRestApiJwt_Resfield2` |  |  |  |
| 7 | `JWT.GEN.RESFIELD.1` | `EbExternalRestApiJwt_Resfield1` |  |  |  |
| 8 | `JWT.GEN.RESFIELD.0` | `EbExternalRestApiJwt_Resfield0` |  |  |  |
| 9 | `JWT.GEN.JWT.METHOD` | `EbExternalRestApiJwt_JwtMethod` | TField |  | Name of the local java API to generate the JWT based on the defined claims and its a valid EB.API record. |
| 10 | `JWT.GEN.RESERVEDFLD.6` | `EbExternalRestApiJwt_Reservedfld6` |  |  |  |
| 11 | `JWT.GEN.RESERVEDFLD.5` | `EbExternalRestApiJwt_Reservedfld5` |  |  |  |
| 12 | `JWT.GEN.RESERVEDFLD.4` | `EbExternalRestApiJwt_Reservedfld4` |  |  |  |
| 13 | `JWT.GEN.RESERVEDFLD.3` | `EbExternalRestApiJwt_Reservedfld3` |  |  |  |
| 14 | `JWT.GEN.RESERVEDFLD.2` | `EbExternalRestApiJwt_Reservedfld2` |  |  |  |
| 15 | `JWT.GEN.RESERVEDFLD.1` | `EbExternalRestApiJwt_Reservedfld1` |  |  |  |
| 16 | `JWT.GEN.RESERVED.10` | `EbExternalRestApiJwt_Reserved10` |  |  |  |
| 17 | `JWT.GEN.RESERVED.9` | `EbExternalRestApiJwt_Reserved9` |  |  |  |
| 18 | `JWT.GEN.RESERVED.8` | `EbExternalRestApiJwt_Reserved8` |  |  |  |
| 19 | `JWT.GEN.RESERVED.7` | `EbExternalRestApiJwt_Reserved7` |  |  |  |
| 20 | `JWT.GEN.RESERVED.6` | `EbExternalRestApiJwt_Reserved6` |  |  |  |
| 21 | `JWT.GEN.RESERVED.5` | `EbExternalRestApiJwt_Reserved5` |  |  |  |
| 22 | `JWT.GEN.RESERVED.4` | `EbExternalRestApiJwt_Reserved4` |  |  |  |
| 23 | `JWT.GEN.RESERVED.3` | `EbExternalRestApiJwt_Reserved3` | TField |  |  |
| 24 | `JWT.GEN.RESERVED.2` | `EbExternalRestApiJwt_Reserved2` | TField |  |  |
| 25 | `JWT.GEN.RESERVED.1` | `EbExternalRestApiJwt_Reserved1` | TField |  |  |
| 26 | `JWT.GEN.LOCAL.REF` | `EbExternalRestApiJwt_LocalRef` |  |  |  |
| 27 | `JWT.GEN.OVERRIDE` | `EbExternalRestApiJwt_Override` |  |  |  |
| 28 | `JWT.GEN.RECORD.STATUS` | `EbExternalRestApiJwt_RecordStatus` | String |  |  |
| 29 | `JWT.GEN.CURR.NO` | `EbExternalRestApiJwt_CurrNo` | String |  |  |
| 30 | `JWT.GEN.INPUTTER` | `EbExternalRestApiJwt_Inputter` |  |  |  |
| 31 | `JWT.GEN.DATE.TIME` | `EbExternalRestApiJwt_DateTime` |  |  |  |
| 32 | `JWT.GEN.AUTHORISER` | `EbExternalRestApiJwt_Authoriser` | String |  |  |
| 33 | `JWT.GEN.CO.CODE` | `EbExternalRestApiJwt_CoCode` | String |  |  |
| 34 | `JWT.GEN.DEPT.CODE` | `EbExternalRestApiJwt_DeptCode` | String |  |  |
| 35 | `JWT.GEN.AUDITOR.CODE` | `EbExternalRestApiJwt_AuditorCode` | String |  |  |
| 36 | `JWT.GEN.AUDIT.DATE.TIME` | `EbExternalRestApiJwt_AuditDateTime` | String |  |  |
