# NORSIC.INTEREST.CODE.MAPPING — Table Schema

> Source: `INSERTS/I_F.NORSIC.INTEREST.CODE.MAPPING` in `NORSIC_SubsidyInterestCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORPER.DESCRIPTION` | `NorsicInterestCodeMapping_Description` |  |  |  |
| 2 | `NORPER.INTEREST.REFERENCE.RATE.CODE` | `NorsicInterestCodeMapping_InterestReferenceRateCode` | TField |  | This field denotes the State Treasury Interest Reference Rate Codes |
| 3 | `NORPER.LOCAL.REF` | `NorsicInterestCodeMapping_LocalRef` |  |  |  |
| 4 | `NORPER.OVERRIDE` | `NorsicInterestCodeMapping_Override` |  |  |  |
| 5 | `NORPER.RECORD.STATUS` | `NorsicInterestCodeMapping_RecordStatus` | String |  |  |
| 6 | `NORPER.CURR.NO` | `NorsicInterestCodeMapping_CurrNo` | String |  |  |
| 7 | `NORPER.INPUTTER` | `NorsicInterestCodeMapping_Inputter` |  |  |  |
| 8 | `NORPER.DATE.TIME` | `NorsicInterestCodeMapping_DateTime` |  |  |  |
| 9 | `NORPER.AUTHORISER` | `NorsicInterestCodeMapping_Authoriser` | String |  |  |
| 10 | `NORPER.CO.CODE` | `NorsicInterestCodeMapping_CoCode` | String |  |  |
| 11 | `NORPER.DEPT.CODE` | `NorsicInterestCodeMapping_DeptCode` | String |  |  |
| 12 | `NORPER.AUDITOR.CODE` | `NorsicInterestCodeMapping_AuditorCode` | String |  |  |
| 13 | `NORPER.AUDIT.DATE.TIME` | `NorsicInterestCodeMapping_AuditDateTime` | String |  |  |
