# ESCROW.ANALYSIS.TYPE — Table Schema

> Source: `INSERTS/I_F.ESCROW.ANALYSIS.TYPE` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.AT.DESCRIPTION` | `EscrowAnalysisType_Description` |  |  |  |
| 2 | `ESCROW.AT.TYPE` | `EscrowAnalysisType_Type` |  |  |  |
| 3 | `ESCROW.AT.PERIOD.END` | `EscrowAnalysisType_PeriodEnd` | TField | Yes | Mandatory input when ANALYSIS.TYPE is TPA or ANNUAL. Possible values: LAST.DISBURSEMENT ANNUAL.PERIOD For annual period, the dates are referred from ESCROW.PARAMETER>ANNUAL.PERIOD |
| 4 | `ESCROW.AT.ANALYSIS.PERIOD` | `EscrowAnalysisType_AnalysisPeriod` | TField |  | This field is used to defined period end for calculating analysis projection. Max length 4 chars Entered value would be validated if it is not upto the standard. Analysis Period can be defined as ex - MMDD where MM is for month and DD is to define Date |
| 5 | `ESCROW.AT.RESERVED.10` | `EscrowAnalysisType_Reserved10` | TField |  |  |
| 6 | `ESCROW.AT.RESERVED.9` | `EscrowAnalysisType_Reserved9` | TField |  |  |
| 7 | `ESCROW.AT.RESERVED.8` | `EscrowAnalysisType_Reserved8` | TField |  |  |
| 8 | `ESCROW.AT.RESERVED.7` | `EscrowAnalysisType_Reserved7` | TField |  |  |
| 9 | `ESCROW.AT.RESERVED.6` | `EscrowAnalysisType_Reserved6` | TField |  |  |
| 10 | `ESCROW.AT.RESERVED.5` | `EscrowAnalysisType_Reserved5` | TField |  |  |
| 11 | `ESCROW.AT.RESERVED.4` | `EscrowAnalysisType_Reserved4` | TField |  |  |
| 12 | `ESCROW.AT.RESERVED.3` | `EscrowAnalysisType_Reserved3` | TField |  |  |
| 13 | `ESCROW.AT.RESERVED.2` | `EscrowAnalysisType_Reserved2` | TField |  |  |
| 14 | `ESCROW.AT.RESERVED.1` | `EscrowAnalysisType_Reserved1` | TField |  |  |
| 15 | `ESCROW.AT.RECORD.STATUS` | `EscrowAnalysisType_RecordStatus` | String |  |  |
| 16 | `ESCROW.AT.CURR.NO` | `EscrowAnalysisType_CurrNo` | String |  |  |
| 17 | `ESCROW.AT.INPUTTER` | `EscrowAnalysisType_Inputter` |  |  |  |
| 18 | `ESCROW.AT.DATE.TIME` | `EscrowAnalysisType_DateTime` |  |  |  |
| 19 | `ESCROW.AT.AUTHORISER` | `EscrowAnalysisType_Authoriser` | String |  |  |
| 20 | `ESCROW.AT.CO.CODE` | `EscrowAnalysisType_CoCode` | String |  |  |
| 21 | `ESCROW.AT.DEPT.CODE` | `EscrowAnalysisType_DeptCode` | String |  |  |
| 22 | `ESCROW.AT.AUDITOR.CODE` | `EscrowAnalysisType_AuditorCode` | String |  |  |
| 23 | `ESCROW.AT.AUDIT.DATE.TIME` | `EscrowAnalysisType_AuditDateTime` | String |  |  |
