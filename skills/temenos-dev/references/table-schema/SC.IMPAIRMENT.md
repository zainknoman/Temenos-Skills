# SC.IMPAIRMENT — Table Schema

> Source: `INSERTS/I_F.SC.IMPAIRMENT` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.IMP.DESCRIPTION` | `ScImpairment_Description` |  |  |  |
| 2 | `SC.IMP.PORTFOLIO` | `ScImpairment_Portfolio` |  |  |  |
| 3 | `SC.IMP.IMPAIRMENT.REASON` | `ScImpairment_ImpairmentReason` | TField |  | This field specifies the reason for impairment classification |
| 4 | `SC.IMP.IMPAIRMENT.DATE` | `ScImpairment_ImpairmentDate` | TField |  | This field specifies the date of impairment classification |
| 5 | `SC.IMP.CANCEL` | `ScImpairment_Cancel` | TField |  | This field takes the value "YES" to cancel the impairment |
| 6 | `SC.IMP.CANCEL.DATE` | `ScImpairment_CancelDate` | TField |  | This field specifies the date of impairment cancellation. |
| 7 | `SC.IMP.RECORD.STATUS` | `ScImpairment_RecordStatus` | String |  |  |
| 8 | `SC.IMP.CURR.NO` | `ScImpairment_CurrNo` | String |  |  |
| 9 | `SC.IMP.INPUTTER` | `ScImpairment_Inputter` |  |  |  |
| 10 | `SC.IMP.DATE.TIME` | `ScImpairment_DateTime` |  |  |  |
| 11 | `SC.IMP.AUTHORISER` | `ScImpairment_Authoriser` | String |  |  |
| 12 | `SC.IMP.CO.CODE` | `ScImpairment_CoCode` | String |  |  |
| 13 | `SC.IMP.DEPT.CODE` | `ScImpairment_DeptCode` | String |  |  |
| 14 | `SC.IMP.AUDITOR.CODE` | `ScImpairment_AuditorCode` | String |  |  |
| 15 | `SC.IMP.AUDIT.DATE.TIME` | `ScImpairment_AuditDateTime` | String |  |  |
