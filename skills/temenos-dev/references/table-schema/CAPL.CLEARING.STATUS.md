# CAPL.CLEARING.STATUS — Table Schema

> Source: `INSERTS/I_F.CAPL.CLEARING.STATUS` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLR.STATUS.DESCRIPTION` | `CaplClearingStatus_Description` |  |  |  |
| 2 | `CLR.STATUS.LOC.REF` | `CaplClearingStatus_LocRef` |  |  |  |
| 3 | `CLR.STATUS.RESERVED.10` | `CaplClearingStatus_Reserved10` |  |  |  |
| 4 | `CLR.STATUS.RESERVED.9` | `CaplClearingStatus_Reserved9` |  |  |  |
| 5 | `CLR.STATUS.RESERVED.8` | `CaplClearingStatus_Reserved8` |  |  |  |
| 6 | `CLR.STATUS.RESERVED.7` | `CaplClearingStatus_Reserved7` |  |  |  |
| 7 | `CLR.STATUS.RESERVED.6` | `CaplClearingStatus_Reserved6` |  |  |  |
| 8 | `CLR.STATUS.RESERVED.5` | `CaplClearingStatus_Reserved5` |  |  |  |
| 9 | `CLR.STATUS.RESERVED.4` | `CaplClearingStatus_Reserved4` |  |  |  |
| 10 | `CLR.STATUS.RESERVED.3` | `CaplClearingStatus_Reserved3` |  |  |  |
| 11 | `CLR.STATUS.RESERVED.2` | `CaplClearingStatus_Reserved2` |  |  |  |
| 12 | `CLR.STATUS.RESERVED.1` | `CaplClearingStatus_Reserved1` |  |  |  |
| 13 | `CLR.STATUS.OVERRIDE` | `CaplClearingStatus_Override` |  |  |  |
| 14 | `CLR.STATUS.RECORD.STATUS` | `CaplClearingStatus_RecordStatus` |  |  |  |
| 15 | `CLR.STATUS.CURR.NO` | `CaplClearingStatus_CurrNo` |  |  |  |
| 16 | `CLR.STATUS.INPUTTER` | `CaplClearingStatus_Inputter` |  |  |  |
| 17 | `CLR.STATUS.DATE.TIME` | `CaplClearingStatus_DateTime` |  |  |  |
| 18 | `CLR.STATUS.AUTHORISER` | `CaplClearingStatus_Authoriser` |  |  |  |
| 19 | `CLR.STATUS.CO.CODE` | `CaplClearingStatus_CoCode` |  |  |  |
| 20 | `CLR.STATUS.DEPT.CODE` | `CaplClearingStatus_DeptCode` |  |  |  |
| 21 | `CLR.STATUS.AUDITOR.CODE` | `CaplClearingStatus_AuditorCode` |  |  |  |
| 22 | `CLR.STATUS.AUDIT.DATE.TIME` | `CaplClearingStatus_AuditDateTime` |  |  |  |
