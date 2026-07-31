# AA.PURPOSE — Table Schema

> Source: `INSERTS/I_F.AA.PURPOSE` in `AF_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PPSE.DESCRIPTION` | `AaPurpose_Description` |  |  |  |
| 2 | `AA.PPSE.FULL.DESC` | `AaPurpose_FullDesc` | TField |  | The Full Description of the Domain Type 1)1 to 60 alphanumeric characters Multivalue field Multilanguage |
| 3 | `AA.PPSE.RESERVED.10` | `AaPurpose_Reserved10` | TField |  |  |
| 4 | `AA.PPSE.RESERVED.9` | `AaPurpose_Reserved9` | TField |  |  |
| 5 | `AA.PPSE.RESERVED.8` | `AaPurpose_Reserved8` | TField |  |  |
| 6 | `AA.PPSE.RESERVED.7` | `AaPurpose_Reserved7` | TField |  |  |
| 7 | `AA.PPSE.RESERVED.6` | `AaPurpose_Reserved6` | TField |  |  |
| 8 | `AA.PPSE.RESERVED.5` | `AaPurpose_Reserved5` | TField |  |  |
| 9 | `AA.PPSE.RESERVED.4` | `AaPurpose_Reserved4` | TField |  |  |
| 10 | `AA.PPSE.RESERVED.3` | `AaPurpose_Reserved3` | TField |  |  |
| 11 | `AA.PPSE.RESERVED.2` | `AaPurpose_Reserved2` | TField |  |  |
| 12 | `AA.PPSE.RESERVED.1` | `AaPurpose_Reserved1` | TField |  |  |
| 13 | `AA.PPSE.LOCAL.REF` | `AaPurpose_LocalRef` |  |  |  |
| 14 | `AA.PPSE.OVERRIDE` | `AaPurpose_Override` |  |  |  |
| 15 | `AA.PPSE.RECORD.STATUS` | `AaPurpose_RecordStatus` | String |  |  |
| 16 | `AA.PPSE.CURR.NO` | `AaPurpose_CurrNo` | String |  |  |
| 17 | `AA.PPSE.INPUTTER` | `AaPurpose_Inputter` |  |  |  |
| 18 | `AA.PPSE.DATE.TIME` | `AaPurpose_DateTime` |  |  |  |
| 19 | `AA.PPSE.AUTHORISER` | `AaPurpose_Authoriser` | String |  |  |
| 20 | `AA.PPSE.CO.CODE` | `AaPurpose_CoCode` | String |  |  |
| 21 | `AA.PPSE.DEPT.CODE` | `AaPurpose_DeptCode` | String |  |  |
| 22 | `AA.PPSE.AUDITOR.CODE` | `AaPurpose_AuditorCode` | String |  |  |
| 23 | `AA.PPSE.AUDIT.DATE.TIME` | `AaPurpose_AuditDateTime` | String |  |  |
