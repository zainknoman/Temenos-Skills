# EB.EXTERNAL.LINK.REF — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.LINK.REF` in `BE_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.LINK.EXT.LINK.APPL` | `EbExternalLinkRef_ExtLinkAppl` |  |  |  |
| 2 | `EXT.LINK.EXT.REF` | `EbExternalLinkRef_ExtRef` |  |  |  |
| 3 | `EXT.LINK.RESERVEDFLD.6` | `EbExternalLinkRef_Reservedfld6` |  |  |  |
| 4 | `EXT.LINK.RESERVEDFLD.5` | `EbExternalLinkRef_Reservedfld5` |  |  |  |
| 5 | `EXT.LINK.RESERVEDFLD.4` | `EbExternalLinkRef_Reservedfld4` |  |  |  |
| 6 | `EXT.LINK.RESERVEDFLD.3` | `EbExternalLinkRef_Reservedfld3` |  |  |  |
| 7 | `EXT.LINK.RESERVEDFLD.2` | `EbExternalLinkRef_Reservedfld2` |  |  |  |
| 8 | `EXT.LINK.RESERVEDFLD.1` | `EbExternalLinkRef_Reservedfld1` |  |  |  |
| 9 | `EXT.LINK.RESERVED.10` | `EbExternalLinkRef_Reserved10` | TField |  |  |
| 10 | `EXT.LINK.RESERVED.9` | `EbExternalLinkRef_Reserved9` | TField |  |  |
| 11 | `EXT.LINK.RESERVED.8` | `EbExternalLinkRef_Reserved8` | TField |  |  |
| 12 | `EXT.LINK.RESERVED.7` | `EbExternalLinkRef_Reserved7` | TField |  |  |
| 13 | `EXT.LINK.RESERVED.6` | `EbExternalLinkRef_Reserved6` | TField |  |  |
| 14 | `EXT.LINK.RESERVED.5` | `EbExternalLinkRef_Reserved5` | TField |  |  |
| 15 | `EXT.LINK.RESERVED.4` | `EbExternalLinkRef_Reserved4` | TField |  |  |
| 16 | `EXT.LINK.RESERVED.3` | `EbExternalLinkRef_Reserved3` | TField |  |  |
| 17 | `EXT.LINK.RESERVED.2` | `EbExternalLinkRef_Reserved2` | TField |  |  |
| 18 | `EXT.LINK.RESERVED.1` | `EbExternalLinkRef_Reserved1` | TField |  |  |
| 19 | `EXT.LINK.LOCAL.REF` | `EbExternalLinkRef_LocalRef` |  |  |  |
| 20 | `EXT.LINK.OVERRIDE` | `EbExternalLinkRef_Override` |  |  |  |
| 21 | `EXT.LINK.RECORD.STATUS` | `EbExternalLinkRef_RecordStatus` | String |  |  |
| 22 | `EXT.LINK.CURR.NO` | `EbExternalLinkRef_CurrNo` | String |  |  |
| 23 | `EXT.LINK.INPUTTER` | `EbExternalLinkRef_Inputter` |  |  |  |
| 24 | `EXT.LINK.DATE.TIME` | `EbExternalLinkRef_DateTime` |  |  |  |
| 25 | `EXT.LINK.AUTHORISER` | `EbExternalLinkRef_Authoriser` | String |  |  |
| 26 | `EXT.LINK.CO.CODE` | `EbExternalLinkRef_CoCode` | String |  |  |
| 27 | `EXT.LINK.DEPT.CODE` | `EbExternalLinkRef_DeptCode` | String |  |  |
| 28 | `EXT.LINK.AUDITOR.CODE` | `EbExternalLinkRef_AuditorCode` | String |  |  |
| 29 | `EXT.LINK.AUDIT.DATE.TIME` | `EbExternalLinkRef_AuditDateTime` | String |  |  |
