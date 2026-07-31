# CAPL.W.NEW.CONTR.PRINT — Table Schema

> Source: `INSERTS/I_F.CAPL.W.NEW.CONTR.PRINT` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.NCP.TAX.YEAR` | `CaplWNewContrPrint_TaxYear` | TField |  |  |
| 2 | `CAPL.NCP.PLAN.GROUP` | `CaplWNewContrPrint_PlanGroup` |  |  |  |
| 3 | `CAPL.NCP.FORM.TYPE.GROUP` | `CaplWNewContrPrint_FormTypeGroup` |  |  |  |
| 4 | `CAPL.NCP.RESERVED.8` | `CaplWNewContrPrint_Reserved8` | TField |  |  |
| 5 | `CAPL.NCP.RESERVED.7` | `CaplWNewContrPrint_Reserved7` | TField |  |  |
| 6 | `CAPL.NCP.RESERVED.6` | `CaplWNewContrPrint_Reserved6` | TField |  |  |
| 7 | `CAPL.NCP.RESERVED.5` | `CaplWNewContrPrint_Reserved5` | TField |  |  |
| 8 | `CAPL.NCP.RESERVED.4` | `CaplWNewContrPrint_Reserved4` | TField |  |  |
| 9 | `CAPL.NCP.RESERVED.3` | `CaplWNewContrPrint_Reserved3` | TField |  |  |
| 10 | `CAPL.NCP.RESERVED.2` | `CaplWNewContrPrint_Reserved2` | TField |  |  |
| 11 | `CAPL.NCP.RESERVED.1` | `CaplWNewContrPrint_Reserved1` | TField |  |  |
| 12 | `CAPL.NCP.LOCAL.REF` | `CaplWNewContrPrint_LocalRef` |  |  |  |
| 13 | `CAPL.NCP.OVERRIDE` | `CaplWNewContrPrint_Override` |  |  |  |
| 14 | `CAPL.NCP.RECORD.STATUS` | `CaplWNewContrPrint_RecordStatus` | String |  |  |
| 15 | `CAPL.NCP.CURR.NO` | `CaplWNewContrPrint_CurrNo` | String |  |  |
| 16 | `CAPL.NCP.INPUTTER` | `CaplWNewContrPrint_Inputter` |  |  |  |
| 17 | `CAPL.NCP.DATE.TIME` | `CaplWNewContrPrint_DateTime` |  |  |  |
| 18 | `CAPL.NCP.AUTHORISER` | `CaplWNewContrPrint_Authoriser` | String |  |  |
| 19 | `CAPL.NCP.CO.CODE` | `CaplWNewContrPrint_CoCode` | String |  |  |
| 20 | `CAPL.NCP.DEPT.CODE` | `CaplWNewContrPrint_DeptCode` | String |  |  |
| 21 | `CAPL.NCP.AUDITOR.CODE` | `CaplWNewContrPrint_AuditorCode` | String |  |  |
| 22 | `CAPL.NCP.AUDIT.DATE.TIME` | `CaplWNewContrPrint_AuditDateTime` | String |  |  |
