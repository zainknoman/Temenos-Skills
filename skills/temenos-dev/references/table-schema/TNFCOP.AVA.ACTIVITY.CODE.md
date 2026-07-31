# TNFCOP.AVA.ACTIVITY.CODE — Table Schema

> Source: `INSERTS/I_F.TNFCOP.AVA.ACTIVITY.CODE` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.ACTIVITY.DESCRIPTION` | `TnfcopAvaActivityCode_Description` |  |  |  |
| 2 | `TNFCOP.ACTIVITY.LOCAL.REF` | `TnfcopAvaActivityCode_LocalRef` |  |  |  |
| 3 | `TNFCOP.ACTIVITY.RESERVED.10` | `TnfcopAvaActivityCode_Reserved10` | TField |  | Reserved field for future use |
| 4 | `TNFCOP.ACTIVITY.RESERVED.9` | `TnfcopAvaActivityCode_Reserved9` | TField |  | Reserved field for future use |
| 5 | `TNFCOP.ACTIVITY.RESERVED.8` | `TnfcopAvaActivityCode_Reserved8` | TField |  | Reserved field for future use |
| 6 | `TNFCOP.ACTIVITY.RESERVED.7` | `TnfcopAvaActivityCode_Reserved7` | TField |  | Reserved field for future use |
| 7 | `TNFCOP.ACTIVITY.RESERVED.6` | `TnfcopAvaActivityCode_Reserved6` | TField |  | Reserved field for future use |
| 8 | `TNFCOP.ACTIVITY.RESERVED.5` | `TnfcopAvaActivityCode_Reserved5` | TField |  | Reserved field for future use |
| 9 | `TNFCOP.ACTIVITY.RESERVED.4` | `TnfcopAvaActivityCode_Reserved4` | TField |  | Reserved field for future use |
| 10 | `TNFCOP.ACTIVITY.RESERVED.3` | `TnfcopAvaActivityCode_Reserved3` | TField |  | Reserved field for future use |
| 11 | `TNFCOP.ACTIVITY.RESERVED.2` | `TnfcopAvaActivityCode_Reserved2` | TField |  | Reserved field for future use |
| 12 | `TNFCOP.ACTIVITY.RESERVED.1` | `TnfcopAvaActivityCode_Reserved1` | TField |  | Reserved field for future use |
| 13 | `TNFCOP.ACTIVITY.OVERRIDE` | `TnfcopAvaActivityCode_Override` |  |  |  |
| 14 | `TNFCOP.ACTIVITY.RECORD.STATUS` | `TnfcopAvaActivityCode_RecordStatus` | String |  |  |
| 15 | `TNFCOP.ACTIVITY.CURR.NO` | `TnfcopAvaActivityCode_CurrNo` | String |  |  |
| 16 | `TNFCOP.ACTIVITY.INPUTTER` | `TnfcopAvaActivityCode_Inputter` |  |  |  |
| 17 | `TNFCOP.ACTIVITY.DATE.TIME` | `TnfcopAvaActivityCode_DateTime` |  |  |  |
| 18 | `TNFCOP.ACTIVITY.AUTHORISER` | `TnfcopAvaActivityCode_Authoriser` | String |  |  |
| 19 | `TNFCOP.ACTIVITY.CO.CODE` | `TnfcopAvaActivityCode_CoCode` | String |  |  |
| 20 | `TNFCOP.ACTIVITY.DEPT.CODE` | `TnfcopAvaActivityCode_DeptCode` | String |  |  |
| 21 | `TNFCOP.ACTIVITY.AUDITOR.CODE` | `TnfcopAvaActivityCode_AuditorCode` | String |  |  |
| 22 | `TNFCOP.ACTIVITY.AUDIT.DATE.TIME` | `TnfcopAvaActivityCode_AuditDateTime` | String |  |  |
