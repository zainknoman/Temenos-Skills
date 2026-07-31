# SE.TRANSACTION.MAPPING — Table Schema

> Source: `INSERTS/I_F.SE.TRANSACTION.MAPPING` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.TM.DESCRIPTION` | `SeTransactionMapping_Description` |  |  |  |
| 2 | `SE.TM.MAP.VALUE` | `SeTransactionMapping_MapValue` |  |  |  |
| 3 | `SE.TM.OPERATION` | `SeTransactionMapping_Operation` |  |  |  |
| 4 | `SE.TM.MAP.APPLICATION` | `SeTransactionMapping_MapApplication` |  |  |  |
| 5 | `SE.TM.DECIS.FIELD` | `SeTransactionMapping_DecisField` |  |  |  |
| 6 | `SE.TM.DECISION` | `SeTransactionMapping_Decision` |  |  |  |
| 7 | `SE.TM.DECISION.FROM` | `SeTransactionMapping_DecisionFrom` |  |  |  |
| 8 | `SE.TM.DECISION.TO` | `SeTransactionMapping_DecisionTo` |  |  |  |
| 9 | `SE.TM.LINK.FIELD.ID` | `SeTransactionMapping_LinkFieldId` |  |  |  |
| 10 | `SE.TM.RESERVED.14` | `SeTransactionMapping_Reserved14` |  |  |  |
| 11 | `SE.TM.RESERVED.13` | `SeTransactionMapping_Reserved13` |  |  |  |
| 12 | `SE.TM.RESERVED.12` | `SeTransactionMapping_Reserved12` |  |  |  |
| 13 | `SE.TM.RESERVED.11` | `SeTransactionMapping_Reserved11` |  |  |  |
| 14 | `SE.TM.RESERVED.10` | `SeTransactionMapping_Reserved10` | TField |  |  |
| 15 | `SE.TM.RESERVED.9` | `SeTransactionMapping_Reserved9` | TField |  |  |
| 16 | `SE.TM.RESERVED.8` | `SeTransactionMapping_Reserved8` | TField |  |  |
| 17 | `SE.TM.RESERVED.7` | `SeTransactionMapping_Reserved7` | TField |  |  |
| 18 | `SE.TM.RESERVED.6` | `SeTransactionMapping_Reserved6` | TField |  |  |
| 19 | `SE.TM.RESERVED.5` | `SeTransactionMapping_Reserved5` | TField |  |  |
| 20 | `SE.TM.RESERVED.4` | `SeTransactionMapping_Reserved4` | TField |  |  |
| 21 | `SE.TM.RESERVED.3` | `SeTransactionMapping_Reserved3` | TField |  |  |
| 22 | `SE.TM.RESERVED.2` | `SeTransactionMapping_Reserved2` | TField |  |  |
| 23 | `SE.TM.RESERVED.1` | `SeTransactionMapping_Reserved1` | TField |  |  |
| 24 | `SE.TM.RECORD.STATUS` | `SeTransactionMapping_RecordStatus` | String |  |  |
| 25 | `SE.TM.CURR.NO` | `SeTransactionMapping_CurrNo` | String |  |  |
| 26 | `SE.TM.INPUTTER` | `SeTransactionMapping_Inputter` |  |  |  |
| 27 | `SE.TM.DATE.TIME` | `SeTransactionMapping_DateTime` |  |  |  |
| 28 | `SE.TM.AUTHORISER` | `SeTransactionMapping_Authoriser` | String |  |  |
| 29 | `SE.TM.CO.CODE` | `SeTransactionMapping_CoCode` | String |  |  |
| 30 | `SE.TM.DEPT.CODE` | `SeTransactionMapping_DeptCode` | String |  |  |
| 31 | `SE.TM.AUDITOR.CODE` | `SeTransactionMapping_AuditorCode` | String |  |  |
| 32 | `SE.TM.AUDIT.DATE.TIME` | `SeTransactionMapping_AuditDateTime` | String |  |  |
