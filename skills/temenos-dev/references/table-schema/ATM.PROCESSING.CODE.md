# ATM.PROCESSING.CODE — Table Schema

> Source: `INSERTS/I_F.ATM.PROCESSING.CODE` in `ATMFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.PCODE.DESCRIPTION` | `AtmProcessingCode_Description` |  |  |  |
| 2 | `ATM.PCODE.ATM.MSG.FORMAT` | `AtmProcessingCode_AtmMsgFormat` | TField |  | It provides which type of atm is used based on the record id provided. |
| 3 | `ATM.PCODE.PROC.CODE` | `AtmProcessingCode_ProcCode` | TField |  | Provides the processing code of the transaction. |
| 4 | `ATM.PCODE.PROC.TYPE` | `AtmProcessingCode_ProcType` | TField |  | EB.LOOKUP file, where type of transaction will be provided. Purchase_cashwithdrawal_fundstransfer_ministatement transaction has to be selected based on the processing code. |
| 5 | `ATM.PCODE.ACCT.TYPE` | `AtmProcessingCode_AcctType` |  |  |  |
| 6 | `ATM.PCODE.LOCAL.REF` | `AtmProcessingCode_LocalRef` |  |  |  |
| 7 | `ATM.PCODE.RESERVED.5` | `AtmProcessingCode_Reserved5` | TField |  |  |
| 8 | `ATM.PCODE.RESERVED.4` | `AtmProcessingCode_Reserved4` | TField |  |  |
| 9 | `ATM.PCODE.RESERVED.3` | `AtmProcessingCode_Reserved3` | TField |  |  |
| 10 | `ATM.PCODE.RESERVED.2` | `AtmProcessingCode_Reserved2` | TField |  |  |
| 11 | `ATM.PCODE.RESERVED.1` | `AtmProcessingCode_Reserved1` | TField |  |  |
| 12 | `ATM.PCODE.RECORD.STATUS` | `AtmProcessingCode_RecordStatus` | String |  |  |
| 13 | `ATM.PCODE.CURR.NO` | `AtmProcessingCode_CurrNo` | String |  |  |
| 14 | `ATM.PCODE.INPUTTER` | `AtmProcessingCode_Inputter` |  |  |  |
| 15 | `ATM.PCODE.DATE.TIME` | `AtmProcessingCode_DateTime` |  |  |  |
| 16 | `ATM.PCODE.AUTHORISER` | `AtmProcessingCode_Authoriser` | String |  |  |
| 17 | `ATM.PCODE.CO.CODE` | `AtmProcessingCode_CoCode` | String |  |  |
| 18 | `ATM.PCODE.DEPT.CODE` | `AtmProcessingCode_DeptCode` | String |  |  |
| 19 | `ATM.PCODE.AUDITOR.CODE` | `AtmProcessingCode_AuditorCode` | String |  |  |
| 20 | `ATM.PCODE.AUDIT.DATE.TIME` | `AtmProcessingCode_AuditDateTime` | String |  |  |
