# CR.PROFILE.TYPE — Table Schema

> Source: `INSERTS/I_F.CR.PROFILE.TYPE` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.PFL.TYP.DESC` | `CrProfileType_Desc` |  |  |  |
| 2 | `CR.PFL.TYP.EXTERNAL.SOURCE` | `CrProfileType_ExternalSource` | TField |  | Specifies external routine for profiling the client. This routine takes care of assigning profile information to the customer if it is specified. Validation Rules :Input must have an entry on EB.API table |
| 3 | `CR.PFL.TYP.CLASSIFICATION` | `CrProfileType_Classification` | TField | Yes | Identifies the Profile type is Internal(using PW.TRANSITION) or External(using Insight data). Validation Rules :2 values allowed INTERNAL or EXTERNALSingle Value field and Mandatory Input |
| 4 | `CR.PFL.TYP.FROM.FILE` | `CrProfileType_FromFile` | TField |  | It holds the Valid Table/Application name. This table must have an @ID of the CUSTOMER id. Validation Rules :35 Alphanumeric Character allowed.Input allowed only if CLASSIFICATION field has value as EXTERNAL. |
| 5 | `CR.PFL.TYP.FROM.FIELD` | `CrProfileType_FromField` | TField |  | Valid Field Name on the table mentioned in FROM.TABLE should be specified. Validation Rules :35 Alphanumeric Character allowed.Single value field.Input allowed only if CLASSIFICATION field has value as EXTERNAL. |
| 6 | `CR.PFL.TYP.LAST.CHNGD.FLD` | `CrProfileType_LastChngdFld` | TField |  | Valid Field Name on the table mentioned in FROM.TABLE should be specified. Validation Rules :35 Alphanumeric Character allowed.Single value field.Input allowed only if CLASSIFICATION field has value as EXTERNAL. |
| 7 | `CR.PFL.TYP.RECORD.STATUS` | `CrProfileType_RecordStatus` | String |  |  |
| 8 | `CR.PFL.TYP.CURR.NO` | `CrProfileType_CurrNo` | String |  |  |
| 9 | `CR.PFL.TYP.INPUTTER` | `CrProfileType_Inputter` |  |  |  |
| 10 | `CR.PFL.TYP.DATE.TIME` | `CrProfileType_DateTime` |  |  |  |
| 11 | `CR.PFL.TYP.AUTHORISER` | `CrProfileType_Authoriser` | String |  |  |
| 12 | `CR.PFL.TYP.CO.CODE` | `CrProfileType_CoCode` | String |  |  |
| 13 | `CR.PFL.TYP.DEPT.CODE` | `CrProfileType_DeptCode` | String |  |  |
| 14 | `CR.PFL.TYP.AUDITOR.CODE` | `CrProfileType_AuditorCode` | String |  |  |
| 15 | `CR.PFL.TYP.AUDIT.DATE.TIME` | `CrProfileType_AuditDateTime` | String |  |  |
