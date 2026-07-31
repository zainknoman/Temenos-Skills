# FSCS.ELIGIBILITY — Table Schema

> Source: `INSERTS/I_F.FSCS.ELIGIBILITY` in `UKFSCS_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSCS.ELIG.DESCRIPTION` | `FscsEligibility_Description` | TField |  | Reason, why a customer is or is not eligible for the FSCS. Example: Private individual resident |
| 2 | `FSCS.ELIG.ELIGIBILITY` | `FscsEligibility_Eligibility` | TField |  | Flag, if customer is eligible to FSCS or not. Validation Rule: 'Y' or 'N' |
| 3 | `FSCS.ELIG.LOCAL.REF` | `FscsEligibility_LocalRef` |  |  |  |
| 4 | `FSCS.ELIG.BRRD.FLAG` | `FscsEligibility_BrrdFlag` | TField |  | BRRD flag, default value as YES. Validation Rule: 'Y' or 'N' |
| 5 | `FSCS.ELIG.RESERVED.9` | `FscsEligibility_Reserved9` | TField |  |  |
| 6 | `FSCS.ELIG.RESERVED.8` | `FscsEligibility_Reserved8` | TField |  |  |
| 7 | `FSCS.ELIG.RESERVED.7` | `FscsEligibility_Reserved7` | TField |  |  |
| 8 | `FSCS.ELIG.RESERVED.6` | `FscsEligibility_Reserved6` | TField |  |  |
| 9 | `FSCS.ELIG.RESERVED.5` | `FscsEligibility_Reserved5` | TField |  |  |
| 10 | `FSCS.ELIG.RESERVED.4` | `FscsEligibility_Reserved4` | TField |  |  |
| 11 | `FSCS.ELIG.RESERVED.3` | `FscsEligibility_Reserved3` | TField |  |  |
| 12 | `FSCS.ELIG.RESERVED.2` | `FscsEligibility_Reserved2` | TField |  |  |
| 13 | `FSCS.ELIG.RESERVED.1` | `FscsEligibility_Reserved1` | TField |  |  |
| 14 | `FSCS.ELIG.OVERRIDE` | `FscsEligibility_Override` |  |  |  |
| 15 | `FSCS.ELIG.RECORD.STATUS` | `FscsEligibility_RecordStatus` | String |  |  |
| 16 | `FSCS.ELIG.CURR.NO` | `FscsEligibility_CurrNo` | String |  |  |
| 17 | `FSCS.ELIG.INPUTTER` | `FscsEligibility_Inputter` |  |  |  |
| 18 | `FSCS.ELIG.DATE.TIME` | `FscsEligibility_DateTime` |  |  |  |
| 19 | `FSCS.ELIG.AUTHORISER` | `FscsEligibility_Authoriser` | String |  |  |
| 20 | `FSCS.ELIG.CO.CODE` | `FscsEligibility_CoCode` | String |  |  |
| 21 | `FSCS.ELIG.DEPT.CODE` | `FscsEligibility_DeptCode` | String |  |  |
| 22 | `FSCS.ELIG.AUDITOR.CODE` | `FscsEligibility_AuditorCode` | String |  |  |
| 23 | `FSCS.ELIG.AUDIT.DATE.TIME` | `FscsEligibility_AuditDateTime` | String |  |  |
