# CL.OUTCOME — Table Schema

> Source: `INSERTS/I_F.CL.OUTCOME` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.OUT.DESCRIPTION` | `ClOutcome_Description` |  |  |  |
| 2 | `CL.OUT.PRODUCTIVITY.FLG` | `ClOutcome_ProductivityFlg` | TField |  |  |
| 3 | `CL.OUT.ACTION.CODE` | `ClOutcome_ActionCode` |  |  |  |
| 4 | `CL.OUT.QTYPE.QUEUE` | `ClOutcome_QtypeQueue` |  |  |  |
| 5 | `CL.OUT.OUTCOME.DUE.DATE` | `ClOutcome_OutcomeDueDate` | TField |  | (Y/N) flag to indicate whether a date is to be entered with the outcome code. |
| 6 | `CL.OUT.MAX.FUTURE.DATE` | `ClOutcome_MaxFutureDate` | TField |  | Maximum number of days that can be between today date and the outcome due date. |
| 7 | `CL.OUT.OUTCOME.DUE.AMT` | `ClOutcome_OutcomeDueAmt` | TField |  | (Y/N) flag to indicate whether an amount is to be entered with the outcome code. |
| 8 | `CL.OUT.SRC.QUEUE` | `ClOutcome_SrcQueue` |  |  |  |
| 9 | `CL.OUT.DEST.QUEUE` | `ClOutcome_DestQueue` |  |  |  |
| 10 | `CL.OUT.NOTES` | `ClOutcome_Notes` |  |  |  |
| 11 | `CL.OUT.OVERDUE.REASON` | `ClOutcome_OverdueReason` | TField |  |  |
| 12 | `CL.OUT.COST.FLAG` | `ClOutcome_CostFlag` | TField |  |  |
| 13 | `CL.OUT.COLLECTOR` | `ClOutcome_Collector` | TField |  | This is a FLAG used to enable the Reassigning of collector (Y/N). |
| 14 | `CL.OUT.NEW.QUEUE` | `ClOutcome_NewQueue` | TField |  | This is a FLAG used to enable the Reassigning of QUEUE (Y/N). |
| 15 | `CL.OUT.LOCAL.REF` | `ClOutcome_LocalRef` |  |  |  |
| 16 | `CL.OUT.RESERVED.3` | `ClOutcome_Reserved3` | TField |  |  |
| 17 | `CL.OUT.RESERVED.2` | `ClOutcome_Reserved2` | TField |  |  |
| 18 | `CL.OUT.RESERVED.1` | `ClOutcome_Reserved1` | TField |  |  |
| 19 | `CL.OUT.RECORD.STATUS` | `ClOutcome_RecordStatus` | String |  |  |
| 20 | `CL.OUT.CURR.NO` | `ClOutcome_CurrNo` | String |  |  |
| 21 | `CL.OUT.INPUTTER` | `ClOutcome_Inputter` |  |  |  |
| 22 | `CL.OUT.DATE.TIME` | `ClOutcome_DateTime` |  |  |  |
| 23 | `CL.OUT.AUTHORISER` | `ClOutcome_Authoriser` | String |  |  |
| 24 | `CL.OUT.CO.CODE` | `ClOutcome_CoCode` | String |  |  |
| 25 | `CL.OUT.DEPT.CODE` | `ClOutcome_DeptCode` | String |  |  |
| 26 | `CL.OUT.AUDITOR.CODE` | `ClOutcome_AuditorCode` | String |  |  |
| 27 | `CL.OUT.AUDIT.DATE.TIME` | `ClOutcome_AuditDateTime` | String |  |  |
