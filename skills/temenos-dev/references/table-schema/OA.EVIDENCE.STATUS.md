# OA.EVIDENCE.STATUS — Table Schema

> Source: `INSERTS/I_F.OA.EVIDENCE.STATUS` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ES.DESCRIPTION` | `OaEvidenceStatus_Description` |  |  |  |
| 2 | `OA.ES.FULL.DESCRIPTION` | `OaEvidenceStatus_FullDescription` |  |  |  |
| 3 | `OA.ES.VERIFIED` | `OaEvidenceStatus_Verified` | TField |  | It is an options field and accepts YES, NO or WAIVE. 1. The option YES describes that the verification of evidence is accepted. 2. The option NO describes that the verification of the evidence is rejected. 3. The option WAIVE describes that the verification of the evidence is waived. |
| 4 | `OA.ES.RESERVED.5` | `OaEvidenceStatus_Reserved5` | TField |  |  |
| 5 | `OA.ES.RESERVED.4` | `OaEvidenceStatus_Reserved4` | TField |  |  |
| 6 | `OA.ES.RESERVED.3` | `OaEvidenceStatus_Reserved3` | TField |  |  |
| 7 | `OA.ES.RESERVED.2` | `OaEvidenceStatus_Reserved2` | TField |  |  |
| 8 | `OA.ES.RESERVED.1` | `OaEvidenceStatus_Reserved1` | TField |  |  |
| 9 | `OA.ES.LOCAL.REF` | `OaEvidenceStatus_LocalRef` |  |  |  |
| 10 | `OA.ES.OVERRIDE` | `OaEvidenceStatus_Override` |  |  |  |
| 11 | `OA.ES.RECORD.STATUS` | `OaEvidenceStatus_RecordStatus` | String |  |  |
| 12 | `OA.ES.CURR.NO` | `OaEvidenceStatus_CurrNo` | String |  |  |
| 13 | `OA.ES.INPUTTER` | `OaEvidenceStatus_Inputter` |  |  |  |
| 14 | `OA.ES.DATE.TIME` | `OaEvidenceStatus_DateTime` |  |  |  |
| 15 | `OA.ES.AUTHORISER` | `OaEvidenceStatus_Authoriser` | String |  |  |
| 16 | `OA.ES.CO.CODE` | `OaEvidenceStatus_CoCode` | String |  |  |
| 17 | `OA.ES.DEPT.CODE` | `OaEvidenceStatus_DeptCode` | String |  |  |
| 18 | `OA.ES.AUDITOR.CODE` | `OaEvidenceStatus_AuditorCode` | String |  |  |
| 19 | `OA.ES.AUDIT.DATE.TIME` | `OaEvidenceStatus_AuditDateTime` | String |  |  |
