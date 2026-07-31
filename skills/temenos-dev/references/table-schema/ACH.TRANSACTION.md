# ACH.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.ACH.TRANSACTION` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHCODE.TRANSACTION.CODE` | `AchTransaction_TransactionCode` | TField |  | The field identifies the transaction code to be displayed in the entries for the incoming transaction. Validation Rules Should have a valid entry in TRANSACTION table. 1-10(Max Value) numeric characters Transaction Code. The Maximum value is specified in EB.OBJECT for TRANSACTION. |
| 2 | `ACHCODE.CR.DR.INDICATOR` | `AchTransaction_CrDrIndicator` | TField |  | Indicates whether the transaction code denotes a credit or debit. This is no input populated based on the TRANSACTION table. When more than one addenda record is available, this can be multi valued. Validation Rules No validation |
| 3 | `ACHCODE.NON.CASH.FLAG` | `AchTransaction_NonCashFlag` | TField | Yes | Yes or No field. Indicates if the the transaction linked to this code requires accounting updates. When this field is input as "Yes" then the Transaction Code will not be mandatory Validation Rules No validation |
| 4 | `ACHCODE.ACH.RETURN.CODE` | `AchTransaction_AchReturnCode` | TField |  | Denotes the code for returned entries. This will be the transaction code used while return is generated Validation Rules Any numeric value, upto 2 digits |
| 5 | `ACHCODE.ACH.TXN.NARR` | `AchTransaction_AchTxnNarr` |  |  |  |
| 6 | `ACHCODE.CHECK.TXN.CODE` | `AchTransaction_CheckTxnCode` | TField |  | If the check serial number is present in the entry record, then the check transaction code which is setup here will be used for transaction. |
| 7 | `ACHCODE.RESERVED.13` | `AchTransaction_Reserved13` |  |  |  |
| 8 | `ACHCODE.RESERVED.12` | `AchTransaction_Reserved12` | TField |  |  |
| 9 | `ACHCODE.RESERVED.11` | `AchTransaction_Reserved11` | TField |  |  |
| 10 | `ACHCODE.RESERVED.10` | `AchTransaction_Reserved10` | TField |  |  |
| 11 | `ACHCODE.RESERVED.9` | `AchTransaction_Reserved9` | TField |  |  |
| 12 | `ACHCODE.RESERVED.8` | `AchTransaction_Reserved8` | TField |  |  |
| 13 | `ACHCODE.RESERVED.7` | `AchTransaction_Reserved7` | TField |  |  |
| 14 | `ACHCODE.RESERVED.6` | `AchTransaction_Reserved6` | TField |  |  |
| 15 | `ACHCODE.RESERVED.5` | `AchTransaction_Reserved5` | TField |  |  |
| 16 | `ACHCODE.RESERVED.4` | `AchTransaction_Reserved4` | TField |  |  |
| 17 | `ACHCODE.RESERVED.3` | `AchTransaction_Reserved3` | TField |  |  |
| 18 | `ACHCODE.RESERVED.2` | `AchTransaction_Reserved2` | TField |  |  |
| 19 | `ACHCODE.RESERVED.1` | `AchTransaction_Reserved1` | TField |  |  |
| 20 | `ACHCODE.LOCAL.REF` | `AchTransaction_LocalRef` |  |  |  |
| 21 | `ACHCODE.RECORD.STATUS` | `AchTransaction_RecordStatus` | String |  |  |
| 22 | `ACHCODE.CURR.NO` | `AchTransaction_CurrNo` | String |  |  |
| 23 | `ACHCODE.INPUTTER` | `AchTransaction_Inputter` |  |  |  |
| 24 | `ACHCODE.DATE.TIME` | `AchTransaction_DateTime` |  |  |  |
| 25 | `ACHCODE.AUTHORISER` | `AchTransaction_Authoriser` | String |  |  |
| 26 | `ACHCODE.CO.CODE` | `AchTransaction_CoCode` | String |  |  |
| 27 | `ACHCODE.DEPT.CODE` | `AchTransaction_DeptCode` | String |  |  |
| 28 | `ACHCODE.AUDITOR.CODE` | `AchTransaction_AuditorCode` | String |  |  |
| 29 | `ACHCODE.AUDIT.DATE.TIME` | `AchTransaction_AuditDateTime` | String |  |  |
