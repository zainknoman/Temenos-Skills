# PP.TRANSACTION.TYPES — Table Schema

> Source: `INSERTS/I_F.PP.TRANSACTION.TYPES` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.TRN.TransactionTypeDescription` | `PpTransactionTypes_Transactiontypedescription` | TField | Yes | Contains a description of the transaction type. It's a mandatory field. |
| 2 | `PP.TRN.RESERVED.5` | `PpTransactionTypes_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 3 | `PP.TRN.RESERVED.4` | `PpTransactionTypes_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 4 | `PP.TRN.RESERVED.3` | `PpTransactionTypes_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 5 | `PP.TRN.RESERVED.2` | `PpTransactionTypes_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 6 | `PP.TRN.RESERVED.1` | `PpTransactionTypes_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 7 | `PP.TRN.LOCAL.REF` | `PpTransactionTypes_LocalRef` |  |  |  |
| 8 | `PP.TRN.OVERRIDE` | `PpTransactionTypes_Override` |  |  |  |
| 9 | `PP.TRN.RECORD.STATUS` | `PpTransactionTypes_RecordStatus` | String |  |  |
| 10 | `PP.TRN.CURR.NO` | `PpTransactionTypes_CurrNo` | String |  |  |
| 11 | `PP.TRN.INPUTTER` | `PpTransactionTypes_Inputter` |  |  |  |
| 12 | `PP.TRN.DATE.TIME` | `PpTransactionTypes_DateTime` |  |  |  |
| 13 | `PP.TRN.AUTHORISER` | `PpTransactionTypes_Authoriser` | String |  |  |
| 14 | `PP.TRN.CO.CODE` | `PpTransactionTypes_CoCode` | String |  |  |
| 15 | `PP.TRN.DEPT.CODE` | `PpTransactionTypes_DeptCode` | String |  |  |
| 16 | `PP.TRN.AUDITOR.CODE` | `PpTransactionTypes_AuditorCode` | String |  |  |
| 17 | `PP.TRN.AUDIT.DATE.TIME` | `PpTransactionTypes_AuditDateTime` | String |  |  |
