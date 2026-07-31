# AM.COMP.BV.UPD — Table Schema

> Source: `INSERTS/I_F.AM.COMP.BV.UPD` in `AM_BackvalueComposite.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.BVC.COMPOSITE.ID` | `AmCompBvUpd_CompositeId` |  |  |  |
| 2 | `AM.BVC.YEAR.MONTH` | `AmCompBvUpd_YearMonth` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `AM.BVC.STATUS` | `AmCompBvUpd_Status` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `AM.BVC.RESERVED.05` | `AmCompBvUpd_Reserved05` | TField |  |  |
| 5 | `AM.BVC.RESERVED.04` | `AmCompBvUpd_Reserved04` | TField |  |  |
| 6 | `AM.BVC.RESERVED.03` | `AmCompBvUpd_Reserved03` | TField |  |  |
| 7 | `AM.BVC.RESERVED.02` | `AmCompBvUpd_Reserved02` | TField |  |  |
| 8 | `AM.BVC.RESERVED.01` | `AmCompBvUpd_Reserved01` | TField |  |  |
| 9 | `AM.BVC.OVERRIDE` | `AmCompBvUpd_Override` |  |  |  |
| 10 | `AM.BVC.RECORD.STATUS` | `AmCompBvUpd_RecordStatus` | String |  |  |
| 11 | `AM.BVC.CURR.NO` | `AmCompBvUpd_CurrNo` | String |  |  |
| 12 | `AM.BVC.INPUTTER` | `AmCompBvUpd_Inputter` |  |  |  |
| 13 | `AM.BVC.DATE.TIME` | `AmCompBvUpd_DateTime` |  |  |  |
| 14 | `AM.BVC.AUTHORISER` | `AmCompBvUpd_Authoriser` | String |  |  |
| 15 | `AM.BVC.CO.CODE` | `AmCompBvUpd_CoCode` | String |  |  |
| 16 | `AM.BVC.DEPT.CODE` | `AmCompBvUpd_DeptCode` | String |  |  |
| 17 | `AM.BVC.AUDITOR.CODE` | `AmCompBvUpd_AuditorCode` | String |  |  |
| 18 | `AM.BVC.AUDIT.DATE.TIME` | `AmCompBvUpd_AuditDateTime` | String |  |  |
