# CR.INTRODUCTION.SOURCE — Table Schema

> Source: `INSERTS/I_F.CR.INTRODUCTION.SOURCE` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.IS.DESCRIPTION` | `CrIntroductionSource_Description` |  |  |  |
| 2 | `CR.IS.COMPANY.AVAILABLE` | `CrIntroductionSource_CompanyAvailable` |  |  |  |
| 3 | `CR.IS.RESERVED.5` | `CrIntroductionSource_Reserved5` |  |  |  |
| 4 | `CR.IS.RESERVED.4` | `CrIntroductionSource_Reserved4` |  |  |  |
| 5 | `CR.IS.RESERVED.3` | `CrIntroductionSource_Reserved3` |  |  |  |
| 6 | `CR.IS.RESERVED.2` | `CrIntroductionSource_Reserved2` |  |  |  |
| 7 | `CR.IS.RESERVED.1` | `CrIntroductionSource_Reserved1` |  |  |  |
| 8 | `CR.IS.LOCAL.REF` | `CrIntroductionSource_LocalRef` |  |  |  |
| 9 | `CR.IS.OVERRIDE` | `CrIntroductionSource_Override` |  |  |  |
| 10 | `CR.IS.RECORD.STATUS` | `CrIntroductionSource_RecordStatus` |  |  |  |
| 11 | `CR.IS.CURR.NO` | `CrIntroductionSource_CurrNo` |  |  |  |
| 12 | `CR.IS.INPUTTER` | `CrIntroductionSource_Inputter` |  |  |  |
| 13 | `CR.IS.DATE.TIME` | `CrIntroductionSource_DateTime` |  |  |  |
| 14 | `CR.IS.AUTHORISER` | `CrIntroductionSource_Authoriser` |  |  |  |
| 15 | `CR.IS.CO.CODE` | `CrIntroductionSource_CoCode` |  |  |  |
| 16 | `CR.IS.DEPT.CODE` | `CrIntroductionSource_DeptCode` |  |  |  |
| 17 | `CR.IS.AUDITOR.CODE` | `CrIntroductionSource_AuditorCode` |  |  |  |
| 18 | `CR.IS.AUDIT.DATE.TIME` | `CrIntroductionSource_AuditDateTime` |  |  |  |
