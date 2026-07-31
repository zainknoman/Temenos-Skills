# TX.CONDITION — Table Schema

> Source: `INSERTS/I_F.TX.CONDITION` in `TX_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TE.COND.DECISION.FLD` | `TxCondition_DecisionFld` |  |  |  |
| 2 | `TE.COND.DECIS.CONV` | `TxCondition_DecisConv` |  |  |  |
| 3 | `TE.COND.DECISION` | `TxCondition_Decision` |  |  |  |
| 4 | `TE.COND.DECISION.FRM` | `TxCondition_DecisionFrm` |  |  |  |
| 5 | `TE.COND.DECISION.TO` | `TxCondition_DecisionTo` |  |  |  |
| 6 | `TE.COND.LEVEL` | `TxCondition_Level` |  |  |  |
| 7 | `TE.COND.OPERAND` | `TxCondition_Operand` |  |  |  |
| 8 | `TE.COND.TXN.BASE.ID` | `TxCondition_TxnBaseId` |  |  |  |
| 9 | `TE.COND.TE.MAPPING.ID` | `TxCondition_TeMappingId` |  |  |  |
| 10 | `TE.COND.EVENT.ID` | `TxCondition_EventId` |  |  |  |
| 11 | `TE.COND.MSG.NUMBER` | `TxCondition_MsgNumber` |  |  |  |
| 12 | `TE.COND.DE.PROCESS` | `TxCondition_DeProcess` |  |  |  |
| 13 | `TE.COND.RESERVED15` | `TxCondition_Reserved15` | TField |  |  |
| 14 | `TE.COND.RESERVED14` | `TxCondition_Reserved14` | TField |  |  |
| 15 | `TE.COND.RESERVED13` | `TxCondition_Reserved13` | TField |  |  |
| 16 | `TE.COND.SEARCH.TYPE` | `TxCondition_SearchType` | TField | No | Specifies the method of evaluating the events. When Search.Type is 'Best Fit', then the Events having maximum number of conditions in them are evaluated first, and then in that order. When the Search.Type is 'First Fit', then the events are evaluated in the order provided. In both the cases, which ever event is satisfied first, the TXN.BASE.ID / MAPPING.ID of that event is used. Validations a. Input to this field is optional. b. The valid input to this field are 'B' for Best Fit / 'F' for First fit. c. When no input is provided, then the default value of 'F' - First fit is used. |
| 17 | `TE.COND.AUTH.WRITE.FILE` | `TxCondition_AuthWriteFile` | TField |  | Indicates the Local Tax Key File. The corresponding file will get updates with the Transaction authorised message at the time of authorisation of the contract. Validation Rules: The field should have a valid File Control. |
| 18 | `TE.COND.AUTH.FILE.ID` | `TxCondition_AuthFileId` |  |  |  |
| 19 | `TE.COND.RESERVED8` | `TxCondition_Reserved8` | TField |  |  |
| 20 | `TE.COND.RESERVED7` | `TxCondition_Reserved7` | TField |  |  |
| 21 | `TE.COND.RESERVED6` | `TxCondition_Reserved6` | TField |  |  |
| 22 | `TE.COND.RESERVED5` | `TxCondition_Reserved5` | TField |  |  |
| 23 | `TE.COND.RESERVED4` | `TxCondition_Reserved4` | TField |  |  |
| 24 | `TE.COND.RESERVED3` | `TxCondition_Reserved3` | TField |  |  |
| 25 | `TE.COND.RESERVED2` | `TxCondition_Reserved2` | TField |  |  |
| 26 | `TE.COND.LOCAL.REF` | `TxCondition_LocalRef` |  |  |  |
| 27 | `TE.COND.OVERRIDE` | `TxCondition_Override` |  |  |  |
| 28 | `TE.COND.RECORD.STATUS` | `TxCondition_RecordStatus` | String |  |  |
| 29 | `TE.COND.CURR.NO` | `TxCondition_CurrNo` | String |  |  |
| 30 | `TE.COND.INPUTTER` | `TxCondition_Inputter` |  |  |  |
| 31 | `TE.COND.DATE.TIME` | `TxCondition_DateTime` |  |  |  |
| 32 | `TE.COND.AUTHORISER` | `TxCondition_Authoriser` | String |  |  |
| 33 | `TE.COND.CO.CODE` | `TxCondition_CoCode` | String |  |  |
| 34 | `TE.COND.DEPT.CODE` | `TxCondition_DeptCode` | String |  |  |
| 35 | `TE.COND.AUDITOR.CODE` | `TxCondition_AuditorCode` | String |  |  |
| 36 | `TE.COND.AUDIT.DATE.TIME` | `TxCondition_AuditDateTime` | String |  |  |
