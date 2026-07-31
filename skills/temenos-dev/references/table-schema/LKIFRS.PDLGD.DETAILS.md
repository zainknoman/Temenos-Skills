# LKIFRS.PDLGD.DETAILS — Table Schema

> Source: `INSERTS/I_F.LKIFRS.PDLGD.DETAILS` in `LKIFRS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKIFRS.PDLGD.CLASS` | `LkifrsPdlgdDetails_Class` |  |  |  |
| 2 | `LKIFRS.PDLGD.PD.CONTRACT` | `LkifrsPdlgdDetails_PdContract` |  |  |  |
| 3 | `LKIFRS.PDLGD.LGD.CONTRACT` | `LkifrsPdlgdDetails_LgdContract` |  |  |  |
| 4 | `LKIFRS.PDLGD.CCF.CONTRACT` | `LkifrsPdlgdDetails_CcfContract` |  |  |  |
| 5 | `LKIFRS.PDLGD.RESERVED.1` | `LkifrsPdlgdDetails_Reserved1` | TField |  | Reserved for future use. |
| 6 | `LKIFRS.PDLGD.RESERVED.2` | `LkifrsPdlgdDetails_Reserved2` | TField |  | Reserved for future use. |
| 7 | `LKIFRS.PDLGD.RESERVED.3` | `LkifrsPdlgdDetails_Reserved3` | TField |  | Reserved for future use. |
| 8 | `LKIFRS.PDLGD.RESERVED.4` | `LkifrsPdlgdDetails_Reserved4` | TField |  | Reserved for future use. |
| 9 | `LKIFRS.PDLGD.RESERVED.5` | `LkifrsPdlgdDetails_Reserved5` | TField |  | Reserved for future use. |
| 10 | `LKIFRS.PDLGD.RESERVED.6` | `LkifrsPdlgdDetails_Reserved6` | TField |  | Reserved for future use. |
| 11 | `LKIFRS.PDLGD.RESERVED.7` | `LkifrsPdlgdDetails_Reserved7` | TField |  | Reserved for future use. |
| 12 | `LKIFRS.PDLGD.RESERVED.8` | `LkifrsPdlgdDetails_Reserved8` | TField |  | Reserved for future use. |
| 13 | `LKIFRS.PDLGD.RESERVED.9` | `LkifrsPdlgdDetails_Reserved9` | TField |  | Reserved for future use. |
| 14 | `LKIFRS.PDLGD.RESERVED.10` | `LkifrsPdlgdDetails_Reserved10` | TField |  | Reserved for future use. |
| 15 | `LKIFRS.PDLGD.LOCAL.REF` | `LkifrsPdlgdDetails_LocalRef` |  |  |  |
| 16 | `LKIFRS.PDLGD.OVERRIDE` | `LkifrsPdlgdDetails_Override` |  |  |  |
| 17 | `LKIFRS.PDLGD.RECORD.STATUS` | `LkifrsPdlgdDetails_RecordStatus` | String |  |  |
| 18 | `LKIFRS.PDLGD.CURR.NO` | `LkifrsPdlgdDetails_CurrNo` | String |  |  |
| 19 | `LKIFRS.PDLGD.INPUTTER` | `LkifrsPdlgdDetails_Inputter` |  |  |  |
| 20 | `LKIFRS.PDLGD.DATE.TIME` | `LkifrsPdlgdDetails_DateTime` |  |  |  |
| 21 | `LKIFRS.PDLGD.AUTHORISER` | `LkifrsPdlgdDetails_Authoriser` | String |  |  |
| 22 | `LKIFRS.PDLGD.CO.CODE` | `LkifrsPdlgdDetails_CoCode` | String |  |  |
| 23 | `LKIFRS.PDLGD.DEPT.CODE` | `LkifrsPdlgdDetails_DeptCode` | String |  |  |
| 24 | `LKIFRS.PDLGD.AUDITOR.CODE` | `LkifrsPdlgdDetails_AuditorCode` | String |  |  |
| 25 | `LKIFRS.PDLGD.AUDIT.DATE.TIME` | `LkifrsPdlgdDetails_AuditDateTime` | String |  |  |
