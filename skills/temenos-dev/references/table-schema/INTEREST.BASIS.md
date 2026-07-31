# INTEREST.BASIS — Table Schema

> Source: `INSERTS/I_F.INTEREST.BASIS` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IB.DESCRIPTION` | `InterestBasis_Description` |  |  |  |
| 2 | `IB.INT.BASIS` | `InterestBasis_IntBasis` | TField |  | Interest Basis calculation method. Validation Rules: 7 Alphanumeric characters. This field cannot be amended. |
| 3 | `IB.OLD.CALC.METHOD` | `InterestBasis_OldCalcMethod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `IB.RESERVED.4` | `InterestBasis_Reserved4` | TField |  |  |
| 5 | `IB.RESERVED.3` | `InterestBasis_Reserved3` | TField |  |  |
| 6 | `IB.LOCAL.REF` | `InterestBasis_LocalRef` |  |  |  |
| 7 | `IB.RESERVED.1` | `InterestBasis_Reserved1` | TField |  |  |
| 8 | `IB.RECORD.STATUS` | `InterestBasis_RecordStatus` | String |  |  |
| 9 | `IB.CURR.NO` | `InterestBasis_CurrNo` | String |  |  |
| 10 | `IB.INPUTTER` | `InterestBasis_Inputter` |  |  |  |
| 11 | `IB.DATE.TIME` | `InterestBasis_DateTime` |  |  |  |
| 12 | `IB.AUTHORISER` | `InterestBasis_Authoriser` | String |  |  |
| 13 | `IB.CO.CODE` | `InterestBasis_CoCode` | String |  |  |
| 14 | `IB.DEPT.CODE` | `InterestBasis_DeptCode` | String |  |  |
| 15 | `IB.AUDITOR.CODE` | `InterestBasis_AuditorCode` | String |  |  |
| 16 | `IB.AUDIT.DATE.TIME` | `InterestBasis_AuditDateTime` | String |  |  |
