# EV.EVIDENCE.CLASS — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.CLASS` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVC.DESCRIPTION` | `EvEvidenceClass_Description` |  |  |  |
| 2 | `EV.EVC.FULL.DESC` | `EvEvidenceClass_FullDesc` |  |  |  |
| 3 | `EV.EVC.TYPE` | `EvEvidenceClass_Type` |  |  |  |
| 4 | `EV.EVC.CLASSIFICATION` | `EvEvidenceClass_Classification` |  |  |  |
| 5 | `EV.EVC.RESERVED.10` | `EvEvidenceClass_Reserved10` | TField |  |  |
| 6 | `EV.EVC.RESERVED.9` | `EvEvidenceClass_Reserved9` | TField |  |  |
| 7 | `EV.EVC.RESERVED.8` | `EvEvidenceClass_Reserved8` | TField |  |  |
| 8 | `EV.EVC.RESERVED.7` | `EvEvidenceClass_Reserved7` | TField |  |  |
| 9 | `EV.EVC.RESERVED.6` | `EvEvidenceClass_Reserved6` | TField |  |  |
| 10 | `EV.EVC.RESERVED.5` | `EvEvidenceClass_Reserved5` | TField |  |  |
| 11 | `EV.EVC.RESERVED.4` | `EvEvidenceClass_Reserved4` | TField |  |  |
| 12 | `EV.EVC.RESERVED.3` | `EvEvidenceClass_Reserved3` | TField |  |  |
| 13 | `EV.EVC.RESERVED.2` | `EvEvidenceClass_Reserved2` | TField |  |  |
| 14 | `EV.EVC.RESERVED.1` | `EvEvidenceClass_Reserved1` | TField |  |  |
| 15 | `EV.EVC.LOCAL.REF` | `EvEvidenceClass_LocalRef` |  |  |  |
| 16 | `EV.EVC.OVERRIDE` | `EvEvidenceClass_Override` |  |  |  |
| 17 | `EV.EVC.RECORD.STATUS` | `EvEvidenceClass_RecordStatus` | String |  |  |
| 18 | `EV.EVC.CURR.NO` | `EvEvidenceClass_CurrNo` | String |  |  |
| 19 | `EV.EVC.INPUTTER` | `EvEvidenceClass_Inputter` |  |  |  |
| 20 | `EV.EVC.DATE.TIME` | `EvEvidenceClass_DateTime` |  |  |  |
| 21 | `EV.EVC.AUTHORISER` | `EvEvidenceClass_Authoriser` | String |  |  |
| 22 | `EV.EVC.CO.CODE` | `EvEvidenceClass_CoCode` | String |  |  |
| 23 | `EV.EVC.DEPT.CODE` | `EvEvidenceClass_DeptCode` | String |  |  |
| 24 | `EV.EVC.AUDITOR.CODE` | `EvEvidenceClass_AuditorCode` | String |  |  |
| 25 | `EV.EVC.AUDIT.DATE.TIME` | `EvEvidenceClass_AuditDateTime` | String |  |  |
