# HKLEND.INSURANCE.CODE — Table Schema

> Source: `INSERTS/I_F.HKLEND.INSURANCE.CODE` in `HKLEND_MortgageInsuranceProgram.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKLEND.INSURANCE.CODE.DESCRIPTION` | `HklendInsuranceCode_Description` | TField |  | This field holds the description of the Insurance Code. |
| 2 | `HKLEND.INSURANCE.CODE.LOCAL.REF` | `HklendInsuranceCode_LocalRef` |  |  |  |
| 3 | `HKLEND.INSURANCE.CODE.OVERRIDE` | `HklendInsuranceCode_Override` |  |  |  |
| 4 | `HKLEND.INSURANCE.CODE.RECORD.STATUS` | `HklendInsuranceCode_RecordStatus` | String |  |  |
| 5 | `HKLEND.INSURANCE.CODE.CURR.NO` | `HklendInsuranceCode_CurrNo` | String |  |  |
| 6 | `HKLEND.INSURANCE.CODE.INPUTTER` | `HklendInsuranceCode_Inputter` |  |  |  |
| 7 | `HKLEND.INSURANCE.CODE.DATE.TIME` | `HklendInsuranceCode_DateTime` |  |  |  |
| 8 | `HKLEND.INSURANCE.CODE.AUTHORISER` | `HklendInsuranceCode_Authoriser` | String |  |  |
| 9 | `HKLEND.INSURANCE.CODE.CO.CODE` | `HklendInsuranceCode_CoCode` | String |  |  |
| 10 | `HKLEND.INSURANCE.CODE.DEPT.CODE` | `HklendInsuranceCode_DeptCode` | String |  |  |
| 11 | `HKLEND.INSURANCE.CODE.AUDITOR.CODE` | `HklendInsuranceCode_AuditorCode` | String |  |  |
| 12 | `HKLEND.INSURANCE.CODE.AUDIT.DATE.TIME` | `HklendInsuranceCode_AuditDateTime` | String |  |  |
