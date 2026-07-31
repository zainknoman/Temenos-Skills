# MIFDII.CLIENT.QUESTION — Table Schema

> Source: `INSERTS/I_F.MIFDII.CLIENT.QUESTION` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFDII.CL.QUE.QUESTION.HEADER` | `MifdiiClientQuestion_QuestionHeader` |  |  |  |
| 2 | `MIFDII.CL.QUE.MANDATORY` | `MifdiiClientQuestion_Mandatory` | TField | Yes | This field indicates if the answer to the question is mandatory. |
| 3 | `MIFDII.CL.QUE.IRP.MANDATORY` | `MifdiiClientQuestion_IrpMandatory` | TField |  | This field indicates if this question is considered for Individual risk profile calculation. |
| 4 | `MIFDII.CL.QUE.WGT.OR.TXT` | `MifdiiClientQuestion_WgtOrTxt` | TField | Yes | This field indicated if the response from the customer is to be a free Text or a Pre-defined answer. Validation Rule: If TXT is chosen, then the ANSWER/ ANSWER.WGT/ IRP.MANDATORY should be made No-Input. |
| 5 | `MIFDII.CL.QUE.ANSWER` | `MifdiiClientQuestion_Answer` |  |  |  |
| 6 | `MIFDII.CL.QUE.ANSWER.WGT` | `MifdiiClientQuestion_AnswerWgt` |  |  |  |
| 7 | `MIFDII.CL.QUE.LOCAL.REF` | `MifdiiClientQuestion_LocalRef` |  |  |  |
| 8 | `MIFDII.CL.QUE.RESERVED.10` | `MifdiiClientQuestion_Reserved10` | TField |  |  |
| 9 | `MIFDII.CL.QUE.RESERVED.9` | `MifdiiClientQuestion_Reserved9` | TField |  |  |
| 10 | `MIFDII.CL.QUE.RESERVED.8` | `MifdiiClientQuestion_Reserved8` | TField |  |  |
| 11 | `MIFDII.CL.QUE.RESERVED.7` | `MifdiiClientQuestion_Reserved7` | TField |  |  |
| 12 | `MIFDII.CL.QUE.RESERVED.6` | `MifdiiClientQuestion_Reserved6` | TField |  |  |
| 13 | `MIFDII.CL.QUE.RESERVED.5` | `MifdiiClientQuestion_Reserved5` | TField |  |  |
| 14 | `MIFDII.CL.QUE.RESERVED.4` | `MifdiiClientQuestion_Reserved4` | TField |  |  |
| 15 | `MIFDII.CL.QUE.RESERVED.3` | `MifdiiClientQuestion_Reserved3` | TField |  |  |
| 16 | `MIFDII.CL.QUE.RESERVED.2` | `MifdiiClientQuestion_Reserved2` | TField |  |  |
| 17 | `MIFDII.CL.QUE.RESERVED.1` | `MifdiiClientQuestion_Reserved1` | TField |  |  |
| 18 | `MIFDII.CL.QUE.OVERRIDE` | `MifdiiClientQuestion_Override` |  |  |  |
| 19 | `MIFDII.CL.QUE.RECORD.STATUS` | `MifdiiClientQuestion_RecordStatus` | String |  |  |
| 20 | `MIFDII.CL.QUE.CURR.NO` | `MifdiiClientQuestion_CurrNo` | String |  |  |
| 21 | `MIFDII.CL.QUE.INPUTTER` | `MifdiiClientQuestion_Inputter` |  |  |  |
| 22 | `MIFDII.CL.QUE.DATE.TIME` | `MifdiiClientQuestion_DateTime` |  |  |  |
| 23 | `MIFDII.CL.QUE.AUTHORISER` | `MifdiiClientQuestion_Authoriser` | String |  |  |
| 24 | `MIFDII.CL.QUE.CO.CODE` | `MifdiiClientQuestion_CoCode` | String |  |  |
| 25 | `MIFDII.CL.QUE.DEPT.CODE` | `MifdiiClientQuestion_DeptCode` | String |  |  |
| 26 | `MIFDII.CL.QUE.AUDITOR.CODE` | `MifdiiClientQuestion_AuditorCode` | String |  |  |
| 27 | `MIFDII.CL.QUE.AUDIT.DATE.TIME` | `MifdiiClientQuestion_AuditDateTime` | String |  |  |
