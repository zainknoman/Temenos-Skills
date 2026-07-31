# ESTELL.DEPOSIT.TRANSACTION.TYPE — Table Schema

> Source: `INSERTS/I_F.ESTELL.DEPOSIT.TRANSACTION.TYPE` in `ESTELL_NonCustomerCash.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESTELL.DEP.TRANS.DESCRIPTION` | `EstellDepositTransactionType_Description` | TField |  | This field is to store the description |
| 2 | `ESTELL.DEP.TRANS.RESERVED.1` | `EstellDepositTransactionType_Reserved1` | TField |  | Reserved for future use |
| 3 | `ESTELL.DEP.TRANS.RESERVED.2` | `EstellDepositTransactionType_Reserved2` | TField |  | Reserved for future use |
| 4 | `ESTELL.DEP.TRANS.RESERVED.3` | `EstellDepositTransactionType_Reserved3` | TField |  | Reserved for future use |
| 5 | `ESTELL.DEP.TRANS.RESERVED.4` | `EstellDepositTransactionType_Reserved4` | TField |  | Reserved for future use |
| 6 | `ESTELL.DEP.TRANS.RESERVED.5` | `EstellDepositTransactionType_Reserved5` | TField |  | Reserved for future use |
| 7 | `ESTELL.DEP.TRANS.RESERVED.6` | `EstellDepositTransactionType_Reserved6` | TField |  | Reserved for future use |
| 8 | `ESTELL.DEP.TRANS.RESERVED.7` | `EstellDepositTransactionType_Reserved7` | TField |  | Reserved for future use |
| 9 | `ESTELL.DEP.TRANS.RESERVED.8` | `EstellDepositTransactionType_Reserved8` | TField |  | Reserved for future use |
| 10 | `ESTELL.DEP.TRANS.RESERVED.9` | `EstellDepositTransactionType_Reserved9` | TField |  | Reserved for future use |
| 11 | `ESTELL.DEP.TRANS.RESERVED.10` | `EstellDepositTransactionType_Reserved10` | TField |  | Reserved for future use |
| 12 | `ESTELL.DEP.TRANS.LOCAL.REF` | `EstellDepositTransactionType_LocalRef` |  |  |  |
| 13 | `ESTELL.DEP.TRANS.RECORD.STATUS` | `EstellDepositTransactionType_RecordStatus` | String |  |  |
| 14 | `ESTELL.DEP.TRANS.CURR.NO` | `EstellDepositTransactionType_CurrNo` | String |  |  |
| 15 | `ESTELL.DEP.TRANS.INPUTTER` | `EstellDepositTransactionType_Inputter` |  |  |  |
| 16 | `ESTELL.DEP.TRANS.DATE.TIME` | `EstellDepositTransactionType_DateTime` |  |  |  |
| 17 | `ESTELL.DEP.TRANS.AUTHORISER` | `EstellDepositTransactionType_Authoriser` | String |  |  |
| 18 | `ESTELL.DEP.TRANS.CO.CODE` | `EstellDepositTransactionType_CoCode` | String |  |  |
| 19 | `ESTELL.DEP.TRANS.DEPT.CODE` | `EstellDepositTransactionType_DeptCode` | String |  |  |
| 20 | `ESTELL.DEP.TRANS.AUDITOR.CODE` | `EstellDepositTransactionType_AuditorCode` | String |  |  |
| 21 | `ESTELL.DEP.TRANS.AUDIT.DATE.TIME` | `EstellDepositTransactionType_AuditDateTime` | String |  |  |
