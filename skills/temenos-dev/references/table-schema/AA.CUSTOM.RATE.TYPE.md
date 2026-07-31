# AA.CUSTOM.RATE.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOM.RATE.TYPE` in `AA_Interest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUSTOM.RATE.DESCRIPTION` | `AaCustomRateType_Description` |  |  |  |
| 2 | `AA.CUSTOM.RATE.ROUTINE.NAME` | `AaCustomRateType_RoutineName` | TField |  | Id of a EB.API record which is suitable for calculating Custom interest rate |
| 3 | `AA.CUSTOM.RATE.RESERVERD.5` | `AaCustomRateType_Reserverd5` | TField |  |  |
| 4 | `AA.CUSTOM.RATE.RESERVERD.4` | `AaCustomRateType_Reserverd4` | TField |  |  |
| 5 | `AA.CUSTOM.RATE.RESERVERD.3` | `AaCustomRateType_Reserverd3` | TField |  |  |
| 6 | `AA.CUSTOM.RATE.RESERVERD.2` | `AaCustomRateType_Reserverd2` | TField |  |  |
| 7 | `AA.CUSTOM.RATE.RESERVERD.1` | `AaCustomRateType_Reserverd1` | TField |  |  |
| 8 | `AA.CUSTOM.RATE.LOCAL.REF` | `AaCustomRateType_LocalRef` |  |  |  |
| 9 | `AA.CUSTOM.RATE.OVERRIDE` | `AaCustomRateType_Override` |  |  |  |
| 10 | `AA.CUSTOM.RATE.RECORD.STATUS` | `AaCustomRateType_RecordStatus` | String |  |  |
| 11 | `AA.CUSTOM.RATE.CURR.NO` | `AaCustomRateType_CurrNo` | String |  |  |
| 12 | `AA.CUSTOM.RATE.INPUTTER` | `AaCustomRateType_Inputter` |  |  |  |
| 13 | `AA.CUSTOM.RATE.DATE.TIME` | `AaCustomRateType_DateTime` |  |  |  |
| 14 | `AA.CUSTOM.RATE.AUTHORISER` | `AaCustomRateType_Authoriser` | String |  |  |
| 15 | `AA.CUSTOM.RATE.CO.CODE` | `AaCustomRateType_CoCode` | String |  |  |
| 16 | `AA.CUSTOM.RATE.DEPT.CODE` | `AaCustomRateType_DeptCode` | String |  |  |
| 17 | `AA.CUSTOM.RATE.AUDITOR.CODE` | `AaCustomRateType_AuditorCode` | String |  |  |
| 18 | `AA.CUSTOM.RATE.AUDIT.DATE.TIME` | `AaCustomRateType_AuditDateTime` | String |  |  |
