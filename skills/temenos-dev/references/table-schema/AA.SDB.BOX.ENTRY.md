# AA.SDB.BOX.ENTRY — Table Schema

> Source: `INSERTS/I_F.AA.SDB.BOX.ENTRY` in `BX_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BX.ENT.DESCRIPTION` | `AaSdbBoxEntry_Description` |  |  |  |
| 2 | `AA.BX.ENT.BOX.TYPE` | `AaSdbBoxEntry_BoxType` |  |  |  |
| 3 | `AA.BX.ENT.BOX.START.NO` | `AaSdbBoxEntry_BoxStartNo` |  |  |  |
| 4 | `AA.BX.ENT.BOX.TOTAL` | `AaSdbBoxEntry_BoxTotal` |  |  |  |
| 5 | `AA.BX.ENT.OVERRIDE` | `AaSdbBoxEntry_Override` |  |  |  |
| 6 | `AA.BX.ENT.RECORD.STATUS` | `AaSdbBoxEntry_RecordStatus` | String |  |  |
| 7 | `AA.BX.ENT.CURR.NO` | `AaSdbBoxEntry_CurrNo` | String |  |  |
| 8 | `AA.BX.ENT.INPUTTER` | `AaSdbBoxEntry_Inputter` |  |  |  |
| 9 | `AA.BX.ENT.DATE.TIME` | `AaSdbBoxEntry_DateTime` |  |  |  |
| 10 | `AA.BX.ENT.AUTHORISER` | `AaSdbBoxEntry_Authoriser` | String |  |  |
| 11 | `AA.BX.ENT.CO.CODE` | `AaSdbBoxEntry_CoCode` | String |  |  |
| 12 | `AA.BX.ENT.DEPT.CODE` | `AaSdbBoxEntry_DeptCode` | String |  |  |
| 13 | `AA.BX.ENT.AUDITOR.CODE` | `AaSdbBoxEntry_AuditorCode` | String |  |  |
| 14 | `AA.BX.ENT.AUDIT.DATE.TIME` | `AaSdbBoxEntry_AuditDateTime` | String |  |  |
