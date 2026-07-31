# CAMB.H.ADJUST.BILL — Table Schema

> Source: `INSERTS/I_F.CAMB.H.ADJUST.BILL` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.H.ADJUST.ARR.ID` | `CambHAdjustBill_ArrId` | TField |  |  |
| 2 | `CAMB.H.ADJUST.RESERVED.1` | `CambHAdjustBill_Reserved1` | TField |  |  |
| 3 | `CAMB.H.ADJUST.RESERVED.2` | `CambHAdjustBill_Reserved2` | TField |  |  |
| 4 | `CAMB.H.ADJUST.RESERVED.3` | `CambHAdjustBill_Reserved3` | TField |  |  |
| 5 | `CAMB.H.ADJUST.OVERRIDE` | `CambHAdjustBill_Override` |  |  |  |
| 6 | `CAMB.H.ADJUST.RECORD.STATUS` | `CambHAdjustBill_RecordStatus` | String |  |  |
| 7 | `CAMB.H.ADJUST.CURR.NO` | `CambHAdjustBill_CurrNo` | String |  |  |
| 8 | `CAMB.H.ADJUST.INPUTTER` | `CambHAdjustBill_Inputter` |  |  |  |
| 9 | `CAMB.H.ADJUST.DATE.TIME` | `CambHAdjustBill_DateTime` |  |  |  |
| 10 | `CAMB.H.ADJUST.AUTHORISER` | `CambHAdjustBill_Authoriser` | String |  |  |
| 11 | `CAMB.H.ADJUST.CO.CODE` | `CambHAdjustBill_CoCode` | String |  |  |
| 12 | `CAMB.H.ADJUST.DEPT.CODE` | `CambHAdjustBill_DeptCode` | String |  |  |
| 13 | `CAMB.H.ADJUST.AUDITOR.CODE` | `CambHAdjustBill_AuditorCode` | String |  |  |
| 14 | `CAMB.H.ADJUST.AUDIT.DATE.TIME` | `CambHAdjustBill_AuditDateTime` | String |  |  |
