# SEPA.REFUSAL — Table Schema

> Source: `INSERTS/I_F.SEPA.REFUSAL` in `EP_Refusal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEPA.REF.REFUSAL.STATUS` | `SepaRefusal_RefusalStatus` | TField | Yes | This Field holds the Status of refusal transaction Possible values are �ACTIVE� or �INACTIVE� Validation Rules Value upto 8 and Mandatory field User can input only &apos;ACTIVE&apos; and &apos;INACTIVE&apos; User can modify the values using EB.LOOKUP with key REFUSAL.STATUS |
| 2 | `SEPA.REF.REFUSAL.TXN` | `SepaRefusal_RefusalTxn` |  |  |  |
| 3 | `SEPA.REF.DESCRIPTION` | `SepaRefusal_Description` |  |  |  |
| 4 | `SEPA.REF.FIELD` | `SepaRefusal_Field` |  |  |  |
| 5 | `SEPA.REF.T24.POSITION` | `SepaRefusal_T24Position` |  |  |  |
| 6 | `SEPA.REF.OPERAND` | `SepaRefusal_Operand` |  |  |  |
| 7 | `SEPA.REF.VALUE` | `SepaRefusal_Value` |  |  |  |
| 8 | `SEPA.REF.FTTC` | `SepaRefusal_Fttc` | A (Alphanumeric) | No | This field is an Optional field and the possible values are stored in FT.TXN.TYPE.CONDITION file Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in FT.TXN.TYPE.CONDITION application |
| 9 | `SEPA.REF.PROCESS.TYPE` | `SepaRefusal_ProcessType` | TField | No | This field is an Optional field and the possible values are �MAN� and �RET� Validation Rules Value upto 3 and user can input only &apos;MAN&apos; or &apos;RET&apos; User can modify the values using EB.LOOKUP with key PROCESS.TYPE |
| 10 | `SEPA.REF.REASON.CODE` | `SepaRefusal_ReasonCode` | A (Alphanumeric) |  | This Field specifies the Reason code for refusal Can only be filled, if the field �PROCESS.TYPE� contains �RET� Validation Rules Value upto 4 type A(Alphanumeric) and Value should exist SEPA.REASONS Application |
| 11 | `SEPA.REF.RECURRENT` | `SepaRefusal_Recurrent` | A (Alphanumeric) |  | If this field is set to YES, REFUSAL.STATUS field should remain as ACTIVE even after the transaction is processed If it is set to NO, then the status will change to INACTIVE Validation Rules Value upto 3 type A(Alphanumeric) and values allowed are YES or NO |
| 12 | `SEPA.REF.VALID.UNTIL.DATE` | `SepaRefusal_ValidUntilDate` | D (Date) |  | This field indicates the date after which SEPA refusal record becomes inactive Validation Rules Value upto 8 type D(Date) |
| 13 | `SEPA.REF.RESERVED.10` | `SepaRefusal_Reserved10` | TField |  |  |
| 14 | `SEPA.REF.RESERVED.9` | `SepaRefusal_Reserved9` | TField |  |  |
| 15 | `SEPA.REF.RESERVED.8` | `SepaRefusal_Reserved8` | TField |  |  |
| 16 | `SEPA.REF.RESERVED.7` | `SepaRefusal_Reserved7` | TField |  |  |
| 17 | `SEPA.REF.RESERVED.6` | `SepaRefusal_Reserved6` | TField |  |  |
| 18 | `SEPA.REF.RESERVED.5` | `SepaRefusal_Reserved5` | TField |  |  |
| 19 | `SEPA.REF.RESERVED.4` | `SepaRefusal_Reserved4` | TField |  |  |
| 20 | `SEPA.REF.RESERVED.3` | `SepaRefusal_Reserved3` | TField |  |  |
| 21 | `SEPA.REF.RESERVED.2` | `SepaRefusal_Reserved2` | TField |  |  |
| 22 | `SEPA.REF.RESERVED.1` | `SepaRefusal_Reserved1` | TField |  |  |
| 23 | `SEPA.REF.LOCAL.REF` | `SepaRefusal_LocalRef` |  |  |  |
| 24 | `SEPA.REF.OVERRIDE` | `SepaRefusal_Override` |  |  |  |
| 25 | `SEPA.REF.RECORD.STATUS` | `SepaRefusal_RecordStatus` | String |  |  |
| 26 | `SEPA.REF.CURR.NO` | `SepaRefusal_CurrNo` | String |  |  |
| 27 | `SEPA.REF.INPUTTER` | `SepaRefusal_Inputter` |  |  |  |
| 28 | `SEPA.REF.DATE.TIME` | `SepaRefusal_DateTime` |  |  |  |
| 29 | `SEPA.REF.AUTHORISER` | `SepaRefusal_Authoriser` | String |  |  |
| 30 | `SEPA.REF.CO.CODE` | `SepaRefusal_CoCode` | String |  |  |
| 31 | `SEPA.REF.DEPT.CODE` | `SepaRefusal_DeptCode` | String |  |  |
| 32 | `SEPA.REF.AUDITOR.CODE` | `SepaRefusal_AuditorCode` | String |  |  |
| 33 | `SEPA.REF.AUDIT.DATE.TIME` | `SepaRefusal_AuditDateTime` | String |  |  |
