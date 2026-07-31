# EV.EVIDENCE.DATA.SOURCE — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.DATA.SOURCE` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EDS.DESCRIPTION` | `EvEvidenceDataSource_Description` |  |  |  |
| 2 | `EV.EDS.FULL.DESCRIPTION` | `EvEvidenceDataSource_FullDescription` |  |  |  |
| 3 | `EV.EDS.EVIDENCE.TYPE` | `EvEvidenceDataSource_EvidenceType` |  |  |  |
| 4 | `EV.EDS.VERIFICATION.FIELD` | `EvEvidenceDataSource_VerificationField` |  |  |  |
| 5 | `EV.EDS.COMPARISON` | `EvEvidenceDataSource_Comparison` |  |  |  |
| 6 | `EV.EDS.RESERVED.5` | `EvEvidenceDataSource_Reserved5` | TField |  |  |
| 7 | `EV.EDS.RESERVED.4` | `EvEvidenceDataSource_Reserved4` | TField |  |  |
| 8 | `EV.EDS.RESERVED.3` | `EvEvidenceDataSource_Reserved3` | TField |  |  |
| 9 | `EV.EDS.RESERVED.2` | `EvEvidenceDataSource_Reserved2` | TField |  |  |
| 10 | `EV.EDS.RESERVED.1` | `EvEvidenceDataSource_Reserved1` | TField |  |  |
| 11 | `EV.EDS.LOCAL.REF` | `EvEvidenceDataSource_LocalRef` |  |  |  |
| 12 | `EV.EDS.OVERRIDE` | `EvEvidenceDataSource_Override` |  |  |  |
| 13 | `EV.EDS.RECORD.STATUS` | `EvEvidenceDataSource_RecordStatus` | String |  |  |
| 14 | `EV.EDS.CURR.NO` | `EvEvidenceDataSource_CurrNo` | String |  |  |
| 15 | `EV.EDS.INPUTTER` | `EvEvidenceDataSource_Inputter` |  |  |  |
| 16 | `EV.EDS.DATE.TIME` | `EvEvidenceDataSource_DateTime` |  |  |  |
| 17 | `EV.EDS.AUTHORISER` | `EvEvidenceDataSource_Authoriser` | String |  |  |
| 18 | `EV.EDS.CO.CODE` | `EvEvidenceDataSource_CoCode` | String |  |  |
| 19 | `EV.EDS.DEPT.CODE` | `EvEvidenceDataSource_DeptCode` | String |  |  |
| 20 | `EV.EDS.AUDITOR.CODE` | `EvEvidenceDataSource_AuditorCode` | String |  |  |
| 21 | `EV.EDS.AUDIT.DATE.TIME` | `EvEvidenceDataSource_AuditDateTime` | String |  |  |
