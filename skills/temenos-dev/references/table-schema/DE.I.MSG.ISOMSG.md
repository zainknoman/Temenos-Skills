# DE.I.MSG.ISOMSG — Table Schema

> Source: `INSERTS/I_F.DE.I.MSG.ISOMSG` in `DE_Inward.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.IMI.MESSAGE.TEXT` | `DeIMsgIsomsg_MessageText` | TField |  | ISOMSG message text. Validation Rules&#58; A maximum of 132 characters may be entered. |
| 2 | `DE.IMI.RECORD.STATUS` | `DeIMsgIsomsg_RecordStatus` | String |  |  |
| 3 | `DE.IMI.CURR.NO` | `DeIMsgIsomsg_CurrNo` | String |  |  |
| 4 | `DE.IMI.INPUTTER` | `DeIMsgIsomsg_Inputter` |  |  |  |
| 5 | `DE.IMI.DATE.TIME` | `DeIMsgIsomsg_DateTime` |  |  |  |
| 6 | `DE.IMI.AUTHORISER` | `DeIMsgIsomsg_Authoriser` | String |  |  |
| 7 | `DE.IMI.CO.CODE` | `DeIMsgIsomsg_CoCode` | String |  |  |
| 8 | `DE.IMI.DEPT.CODE` | `DeIMsgIsomsg_DeptCode` | String |  |  |
| 9 | `DE.IMI.AUDITOR.CODE` | `DeIMsgIsomsg_AuditorCode` | String |  |  |
| 10 | `DE.IMI.AUDIT.DATE.TIME` | `DeIMsgIsomsg_AuditDateTime` | String |  |  |
