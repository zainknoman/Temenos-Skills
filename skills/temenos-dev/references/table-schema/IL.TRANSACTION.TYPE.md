# IL.TRANSACTION.TYPE — Table Schema

> Source: `INSERTS/I_F.IL.TRANSACTION.TYPE` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.TRANSTYPE.CLASSIFICATION` | `IlTransactionType_Classification` | TField | Yes | This field holds the classification for the Transaction Type based on which a direction is assigned. Validation Rules: Allowed values are Receipts and Payments. Mandatory field and NOCHANGE field ID Suffix should match the classification value opted. For Example: AP is the first record created with classification as Payments and Id suffix is 'P' then for all the subsequent records created, the system should allow only with the suffix as 'P' for Payments classification. |
| 2 | `IL.TRANSTYPE.DESCRIPTION` | `IlTransactionType_Description` |  |  |  |
| 3 | `IL.TRANSTYPE.DIRECTION` | `IlTransactionType_Direction` | TField | Yes | This field specifies the general sign of the transaction type associated to the classification defined. It is used to prefix the amounts in downstream tables. Validation Rules: Allowed Values are +1 and -1. Mandatory field and NOCHANGE field. Direction assigned to a Classification for the first record will be saved by system. Different direction cannot be assigned to same classification for preceding records. For Example: AP is the first record created with classification as Payments and Direction as -1, then for all the subsequent records created, the system will allow only Direction as -1 for Payments classification and Direction as +1 for Receipts classification. |
| 4 | `IL.TRANSTYPE.RESERVED.10` | `IlTransactionType_Reserved10` | TField |  |  |
| 5 | `IL.TRANSTYPE.RESERVED.9` | `IlTransactionType_Reserved9` | TField |  |  |
| 6 | `IL.TRANSTYPE.RESERVED.8` | `IlTransactionType_Reserved8` | TField |  |  |
| 7 | `IL.TRANSTYPE.RESERVED.7` | `IlTransactionType_Reserved7` | TField |  |  |
| 8 | `IL.TRANSTYPE.RESERVED.6` | `IlTransactionType_Reserved6` | TField |  |  |
| 9 | `IL.TRANSTYPE.RESERVED.5` | `IlTransactionType_Reserved5` | TField |  |  |
| 10 | `IL.TRANSTYPE.RESERVED.4` | `IlTransactionType_Reserved4` | TField |  |  |
| 11 | `IL.TRANSTYPE.RESERVED.3` | `IlTransactionType_Reserved3` | TField |  |  |
| 12 | `IL.TRANSTYPE.RESERVED.2` | `IlTransactionType_Reserved2` | TField |  |  |
| 13 | `IL.TRANSTYPE.RESERVED.1` | `IlTransactionType_Reserved1` | TField |  |  |
| 14 | `IL.TRANSTYPE.LOCAL.REF` | `IlTransactionType_LocalRef` |  |  |  |
| 15 | `IL.TRANSTYPE.OVERRIDE` | `IlTransactionType_Override` |  |  |  |
| 16 | `IL.TRANSTYPE.RECORD.STATUS` | `IlTransactionType_RecordStatus` | String |  |  |
| 17 | `IL.TRANSTYPE.CURR.NO` | `IlTransactionType_CurrNo` | String |  |  |
| 18 | `IL.TRANSTYPE.INPUTTER` | `IlTransactionType_Inputter` |  |  |  |
| 19 | `IL.TRANSTYPE.DATE.TIME` | `IlTransactionType_DateTime` |  |  |  |
| 20 | `IL.TRANSTYPE.AUTHORISER` | `IlTransactionType_Authoriser` | String |  |  |
| 21 | `IL.TRANSTYPE.CO.CODE` | `IlTransactionType_CoCode` | String |  |  |
| 22 | `IL.TRANSTYPE.DEPT.CODE` | `IlTransactionType_DeptCode` | String |  |  |
| 23 | `IL.TRANSTYPE.AUDITOR.CODE` | `IlTransactionType_AuditorCode` | String |  |  |
| 24 | `IL.TRANSTYPE.AUDIT.DATE.TIME` | `IlTransactionType_AuditDateTime` | String |  |  |
