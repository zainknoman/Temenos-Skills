# PV.LOAN.CLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.PV.LOAN.CLASSIFICATION` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVLC.RANK` | `PvLoanClassification_Rank` | TField |  | A unique numeric ranking. Maximum 3 numeric allowed. |
| 2 | `PVLC.RESERVED.5` | `PvLoanClassification_Reserved5` |  |  |  |
| 3 | `PVLC.RESERVED.4` | `PvLoanClassification_Reserved4` |  |  |  |
| 4 | `PVLC.RESERVED.3` | `PvLoanClassification_Reserved3` |  |  |  |
| 5 | `PVLC.LOCAL.REF` | `PvLoanClassification_LocalRef` |  |  |  |
| 6 | `PVLC.OVERRIDE` | `PvLoanClassification_Override` |  |  |  |
| 7 | `PVLC.RECORD.STATUS` | `PvLoanClassification_RecordStatus` | String |  |  |
| 8 | `PVLC.CURR.NO` | `PvLoanClassification_CurrNo` | String |  |  |
| 9 | `PVLC.INPUTTER` | `PvLoanClassification_Inputter` |  |  |  |
| 10 | `PVLC.DATE.TIME` | `PvLoanClassification_DateTime` |  |  |  |
| 11 | `PVLC.AUTHORISER` | `PvLoanClassification_Authoriser` | String |  |  |
| 12 | `PVLC.CO.CODE` | `PvLoanClassification_CoCode` | String |  |  |
| 13 | `PVLC.DEPT.CODE` | `PvLoanClassification_DeptCode` | String |  |  |
| 14 | `PVLC.AUDITOR.CODE` | `PvLoanClassification_AuditorCode` | String |  |  |
| 15 | `PVLC.AUDIT.DATE.TIME` | `PvLoanClassification_AuditDateTime` | String |  |  |
