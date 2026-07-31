# USRETL.STMT.ENTRY — Table Schema

> Source: `INSERTS/I_F.USRETL.STMT.ENTRY` in `USRETL_HistoryMigration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USRETL.STE.POSTING.DATE` | `UsretlStmtEntry_PostingDate` | TField |  | This field holds the product line of a transaction Validation: Alphanumeric field, with a length of 35 characters |
| 2 | `USRETL.STE.EFFECTIVE.DATE` | `UsretlStmtEntry_EffectiveDate` | TField |  | It denotes the Effective date of the transaction that has been migrated. Validation: Standard T24 date Field with a length of 11 character |
| 3 | `USRETL.STE.PAYMENT.DUE.DATE` | `UsretlStmtEntry_PaymentDueDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `USRETL.STE.AMOUNT` | `UsretlStmtEntry_Amount` | TField |  | The amount of the transaction that has been migrated is captured in this field Validation: Standard T24 amount field with a length of 20 characters |
| 5 | `USRETL.STE.CHEQUE.NUMBER` | `UsretlStmtEntry_ChequeNumber` | TField |  | It captures the check number of the transaction. Validation: Alphanumeric field, with a length of 25 characters |
| 6 | `USRETL.STE.TRANSACTION.TYPE` | `UsretlStmtEntry_TransactionType` | TField |  | It denotes the type of the transaction that has taken place for the contract. Validation: Alphanumeric field, with a length of 50 characters |
| 7 | `USRETL.STE.DESCRIPTION` | `UsretlStmtEntry_Description` | TField |  | Description of the transaction Validation: Alphanumeric field, with a length of 35 characters |
| 8 | `USRETL.STE.NARRATIVE` | `UsretlStmtEntry_Narrative` |  |  |  |
| 9 | `USRETL.STE.USER.REFERENCE` | `UsretlStmtEntry_UserReference` | TField |  | The user who has executed the transaction is captured in this field. Validation: Alphanumeric field, with a length of 35 characters |
| 10 | `USRETL.STE.IMAGE.REFERENCE` | `UsretlStmtEntry_ImageReference` |  |  |  |
| 11 | `USRETL.STE.TXN.CCY` | `UsretlStmtEntry_TxnCcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `USRETL.STE.OPENING.BALANCE` | `UsretlStmtEntry_OpeningBalance` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `USRETL.STE.ENDING.BALANCE` | `UsretlStmtEntry_EndingBalance` | TField |  | Denotes the Ending/ closing balance of the migrated transaction Validation: Standard T24 amount field with a length of 20 characters |
| 14 | `USRETL.STE.PRINCIPAL` | `UsretlStmtEntry_Principal` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `USRETL.STE.INTEREST` | `UsretlStmtEntry_Interest` | TField |  | This field contains the Interest amount of the transaction that has been migrated Validation: Standard T24 amount field with a length of 20 characters |
| 16 | `USRETL.STE.ESCROW` | `UsretlStmtEntry_Escrow` | TField |  | This field contains the Escrow amount of the migrated contract. Validation: Standard T24 amount field with a length of 20 characters |
| 17 | `USRETL.STE.LATE.FEES` | `UsretlStmtEntry_LateFees` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 18 | `USRETL.STE.OTHER.CHARGES` | `UsretlStmtEntry_OtherCharges` | TField |  | The Charges of the migrated contract. Validation: Standard T24 amount field with a length of 20 characters |
| 19 | `USRETL.STE.OLD.RATE` | `UsretlStmtEntry_OldRate` | TField |  | Holds the old interest rate of the contract. Validation: Standard T24 rate field with a length of 3 characters |
| 20 | `USRETL.STE.NEW.RATE` | `UsretlStmtEntry_NewRate` | TField |  | Holds the new interest rate of the contract. Validation: Standard T24 rate field with a length of 3 characters |
| 21 | `USRETL.STE.ENTRY.ID` | `UsretlStmtEntry_EntryId` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 22 | `USRETL.STE.RESERVED.1` | `UsretlStmtEntry_Reserved1` | TField |  |  |
| 23 | `USRETL.STE.RESERVED.2` | `UsretlStmtEntry_Reserved2` | TField |  |  |
| 24 | `USRETL.STE.RESERVED.3` | `UsretlStmtEntry_Reserved3` | TField |  |  |
| 25 | `USRETL.STE.RESERVED.4` | `UsretlStmtEntry_Reserved4` | TField |  |  |
| 26 | `USRETL.STE.RESERVED.5` | `UsretlStmtEntry_Reserved5` | TField |  |  |
| 27 | `USRETL.STE.RESERVED.6` | `UsretlStmtEntry_Reserved6` | TField |  |  |
| 28 | `USRETL.STE.RESERVED.7` | `UsretlStmtEntry_Reserved7` | TField |  |  |
| 29 | `USRETL.STE.RESERVED.8` | `UsretlStmtEntry_Reserved8` | TField |  |  |
| 30 | `USRETL.STE.RESERVED.9` | `UsretlStmtEntry_Reserved9` | TField |  |  |
| 31 | `USRETL.STE.RESERVED.10` | `UsretlStmtEntry_Reserved10` | TField |  |  |
| 32 | `USRETL.STE.RESERVED.11` | `UsretlStmtEntry_Reserved11` | TField |  |  |
| 33 | `USRETL.STE.RESERVED.12` | `UsretlStmtEntry_Reserved12` | TField |  |  |
| 34 | `USRETL.STE.RESERVED.13` | `UsretlStmtEntry_Reserved13` | TField |  |  |
| 35 | `USRETL.STE.RESERVED.14` | `UsretlStmtEntry_Reserved14` | TField |  |  |
| 36 | `USRETL.STE.RESERVED.15` | `UsretlStmtEntry_Reserved15` | TField |  |  |
| 37 | `USRETL.STE.RESERVED.16` | `UsretlStmtEntry_Reserved16` | TField |  |  |
| 38 | `USRETL.STE.RESERVED.17` | `UsretlStmtEntry_Reserved17` | TField |  |  |
| 39 | `USRETL.STE.RESERVED.18` | `UsretlStmtEntry_Reserved18` | TField |  |  |
| 40 | `USRETL.STE.RESERVED.19` | `UsretlStmtEntry_Reserved19` | TField |  |  |
| 41 | `USRETL.STE.RESERVED.20` | `UsretlStmtEntry_Reserved20` | TField |  |  |
| 42 | `USRETL.STE.RESERVED.21` | `UsretlStmtEntry_Reserved21` | TField |  |  |
| 43 | `USRETL.STE.RESERVED.22` | `UsretlStmtEntry_Reserved22` | TField |  |  |
| 44 | `USRETL.STE.RESERVED.23` | `UsretlStmtEntry_Reserved23` | TField |  |  |
| 45 | `USRETL.STE.RESERVED.24` | `UsretlStmtEntry_Reserved24` | TField |  |  |
| 46 | `USRETL.STE.RESERVED.25` | `UsretlStmtEntry_Reserved25` | TField |  |  |
| 47 | `USRETL.STE.RECORD.STATUS` | `UsretlStmtEntry_RecordStatus` | String |  |  |
| 48 | `USRETL.STE.CURR.NO` | `UsretlStmtEntry_CurrNo` | String |  |  |
| 49 | `USRETL.STE.INPUTTER` | `UsretlStmtEntry_Inputter` |  |  |  |
| 50 | `USRETL.STE.DATE.TIME` | `UsretlStmtEntry_DateTime` |  |  |  |
| 51 | `USRETL.STE.AUTHORISER` | `UsretlStmtEntry_Authoriser` | String |  |  |
| 52 | `USRETL.STE.CO.CODE` | `UsretlStmtEntry_CoCode` | String |  |  |
| 53 | `USRETL.STE.DEPT.CODE` | `UsretlStmtEntry_DeptCode` | String |  |  |
| 54 | `USRETL.STE.AUDITOR.CODE` | `UsretlStmtEntry_AuditorCode` | String |  |  |
| 55 | `USRETL.STE.AUDIT.DATE.TIME` | `UsretlStmtEntry_AuditDateTime` | String |  |  |
