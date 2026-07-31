# SC.CA.PRE.ADVICE — Table Schema

> Source: `INSERTS/I_F.SC.CA.PRE.ADVICE` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PA.INIT.MSG.FUNC` | `ScCaPreAdvice_InitMsgFunc` | TField | Yes | The function of the message (MT564 - Corporate Action Notification) based on which the firstpre-advice/notification has to be generated. The function must contain any of the codes like NEWM, REPL, etc. The valid functions will be defined by EB.LOOKUP table - MSG.FUNC*(ADDB,CANC,NEWM,REPE,REPL,RMDR,WITH) Validation Rules Mandatory Field |
| 2 | `SC.PA.INIT.MSG.STATUS` | `ScCaPreAdvice_InitMsgStatus` | TField |  | The processing status from the incoming MT564 - PREU, PREC, COMP, etc. If specified, the initial notification will be generated only if the processing status in the message/of theevent matches with the status defined here. If the field is left blank, notification will be generated on receiptof MT 564 (provided there is a match with the INIT.MSG.FUNC) The valid statuses will be defined by EB.LOOKUP table - MSG.STATUS*(COMP,COMU,ENTL,PREU,PREC) |
| 3 | `SC.PA.AMND.MSG.FUNC` | `ScCaPreAdvice_AmndMsgFunc` |  |  |  |
| 4 | `SC.PA.AMND.MSG.STATUS` | `ScCaPreAdvice_AmndMsgStatus` |  |  |  |
| 5 | `SC.PA.RESERVED.15` | `ScCaPreAdvice_Reserved15` | TField |  |  |
| 6 | `SC.PA.RESERVED.14` | `ScCaPreAdvice_Reserved14` | TField |  |  |
| 7 | `SC.PA.RESERVED.13` | `ScCaPreAdvice_Reserved13` | TField |  |  |
| 8 | `SC.PA.RESERVED.12` | `ScCaPreAdvice_Reserved12` | TField |  |  |
| 9 | `SC.PA.RESERVED.11` | `ScCaPreAdvice_Reserved11` | TField |  |  |
| 10 | `SC.PA.RESERVED.10` | `ScCaPreAdvice_Reserved10` | TField |  |  |
| 11 | `SC.PA.RESERVED.09` | `ScCaPreAdvice_Reserved09` | TField |  |  |
| 12 | `SC.PA.RESERVED.08` | `ScCaPreAdvice_Reserved08` | TField |  |  |
| 13 | `SC.PA.RESERVED.07` | `ScCaPreAdvice_Reserved07` | TField |  |  |
| 14 | `SC.PA.RESERVED.06` | `ScCaPreAdvice_Reserved06` | TField |  |  |
| 15 | `SC.PA.RESERVED.05` | `ScCaPreAdvice_Reserved05` | TField |  |  |
| 16 | `SC.PA.RESERVED.04` | `ScCaPreAdvice_Reserved04` | TField |  |  |
| 17 | `SC.PA.RESERVED.03` | `ScCaPreAdvice_Reserved03` | TField |  |  |
| 18 | `SC.PA.RESERVED.02` | `ScCaPreAdvice_Reserved02` | TField |  |  |
| 19 | `SC.PA.RESERVED.01` | `ScCaPreAdvice_Reserved01` | TField |  |  |
| 20 | `SC.PA.LOCAL.REF` | `ScCaPreAdvice_LocalRef` |  |  |  |
| 21 | `SC.PA.OVERRIDE` | `ScCaPreAdvice_Override` |  |  |  |
| 22 | `SC.PA.RECORD.STATUS` | `ScCaPreAdvice_RecordStatus` | String |  |  |
| 23 | `SC.PA.CURR.NO` | `ScCaPreAdvice_CurrNo` | String |  |  |
| 24 | `SC.PA.INPUTTER` | `ScCaPreAdvice_Inputter` |  |  |  |
| 25 | `SC.PA.DATE.TIME` | `ScCaPreAdvice_DateTime` |  |  |  |
| 26 | `SC.PA.AUTHORISER` | `ScCaPreAdvice_Authoriser` | String |  |  |
| 27 | `SC.PA.CO.CODE` | `ScCaPreAdvice_CoCode` | String |  |  |
| 28 | `SC.PA.DEPT.CODE` | `ScCaPreAdvice_DeptCode` | String |  |  |
| 29 | `SC.PA.AUDITOR.CODE` | `ScCaPreAdvice_AuditorCode` | String |  |  |
| 30 | `SC.PA.AUDIT.DATE.TIME` | `ScCaPreAdvice_AuditDateTime` | String |  |  |
