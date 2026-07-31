# CAPL.DRAFT.NUMBERS — Table Schema

> Source: `INSERTS/I_F.CAPL.DRAFT.NUMBERS` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.DN.DESCRIPTION` | `CaplDraftNumbers_Description` | TField |  | Description for this draft typeallowed up to 35 char |
| 2 | `CAPL.DN.DRAFT.NUMBER` | `CaplDraftNumbers_DraftNumber` | TField |  |  |
| 3 | `CAPL.DN.RESERVED.10` | `CaplDraftNumbers_Reserved10` | TField |  |  |
| 4 | `CAPL.DN.RESERVED.9` | `CaplDraftNumbers_Reserved9` | TField |  |  |
| 5 | `CAPL.DN.RESERVED.8` | `CaplDraftNumbers_Reserved8` | TField |  |  |
| 6 | `CAPL.DN.RESERVED.7` | `CaplDraftNumbers_Reserved7` | TField |  |  |
| 7 | `CAPL.DN.RESERVED.6` | `CaplDraftNumbers_Reserved6` | TField |  |  |
| 8 | `CAPL.DN.RESERVED.5` | `CaplDraftNumbers_Reserved5` | TField |  |  |
| 9 | `CAPL.DN.RESERVED.4` | `CaplDraftNumbers_Reserved4` | TField |  |  |
| 10 | `CAPL.DN.RESERVED.3` | `CaplDraftNumbers_Reserved3` | TField |  |  |
| 11 | `CAPL.DN.RESERVED.2` | `CaplDraftNumbers_Reserved2` | TField |  |  |
| 12 | `CAPL.DN.RESERVED.1` | `CaplDraftNumbers_Reserved1` | TField |  |  |
| 13 | `CAPL.DN.LOCAL.REF` | `CaplDraftNumbers_LocalRef` |  |  |  |
| 14 | `CAPL.DN.OVERRIDE` | `CaplDraftNumbers_Override` |  |  |  |
| 15 | `CAPL.DN.RECORD.STATUS` | `CaplDraftNumbers_RecordStatus` | String |  |  |
| 16 | `CAPL.DN.CURR.NO` | `CaplDraftNumbers_CurrNo` | String |  |  |
| 17 | `CAPL.DN.INPUTTER` | `CaplDraftNumbers_Inputter` |  |  |  |
| 18 | `CAPL.DN.DATE.TIME` | `CaplDraftNumbers_DateTime` |  |  |  |
| 19 | `CAPL.DN.AUTHORISER` | `CaplDraftNumbers_Authoriser` | String |  |  |
| 20 | `CAPL.DN.CO.CODE` | `CaplDraftNumbers_CoCode` | String |  |  |
| 21 | `CAPL.DN.DEPT.CODE` | `CaplDraftNumbers_DeptCode` | String |  |  |
| 22 | `CAPL.DN.AUDITOR.CODE` | `CaplDraftNumbers_AuditorCode` | String |  |  |
| 23 | `CAPL.DN.AUDIT.DATE.TIME` | `CaplDraftNumbers_AuditDateTime` | String |  |  |
