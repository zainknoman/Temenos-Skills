# FS.GA.OPERATION.CODES.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPERATION.CODES.ACCOUNTS` in `FS_AccountingEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPERATION.CODES.ACCOUNTS.PARENT.REF.ID` | `FsGaOperationCodesAccounts_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPERATION.CODES.ACCOUNTS.ORA.ROWID` | `FsGaOperationCodesAccounts_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPERATION.CODES.ACCOUNTS.OP.CODE` | `FsGaOperationCodesAccounts_OpCode` | TField |  | Enter the operation code Multifonds DB Column is COPER_REPRISE. |
| 4 | `FS.GA.OPERATION.CODES.ACCOUNTS.REPRISE.INT.ACCOUNT.NUMBER` | `FsGaOperationCodesAccounts_RepriseIntAccountNumber` | TField |  | Enter account number as per the source system Multifonds DB Column is NRUBR_REP_INT. |
| 5 | `FS.GA.OPERATION.CODES.ACCOUNTS.SOURCE.SUFFIX.NUMBER` | `FsGaOperationCodesAccounts_SourceSuffixNumber` | TField |  | Enter the suffix number, if any, as used in the source system. Multifonds DB Column is NSUFF_REP_INT. |
| 6 | `FS.GA.OPERATION.CODES.ACCOUNTS.GL.ACCOUNT` | `FsGaOperationCodesAccounts_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 7 | `FS.GA.OPERATION.CODES.ACCOUNTS.GL.ACCOUNT.SUFFIX` | `FsGaOperationCodesAccounts_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 8 | `FS.GA.OPERATION.CODES.ACCOUNTS.CURRENCY` | `FsGaOperationCodesAccounts_Currency` | TField |  | Allows defining if the account should accept a movement in the currency of the transaction or only in the currency of the fund. Multifonds DB Column is FLAG_MON. |
| 9 | `FS.GA.OPERATION.CODES.ACCOUNTS.HISTORY` | `FsGaOperationCodesAccounts_History` | TField |  | Indicates for conversions&quot; if the exchange rates in system should be used or if the exchange rates are deduced from the amounts in the currency of the fund and in the currency of the transaction.&quot; Multifonds DB Column is FLAG_COURS_HIST. |
| 10 | `FS.GA.OPERATION.CODES.ACCOUNTS.AMOUNT.IDENTIFIER` | `FsGaOperationCodesAccounts_AmountIdentifier` | TField |  | Amount Identifier Multifonds DB Column is FLAG_MNT_PROV. |
| 11 | `FS.GA.OPERATION.CODES.ACCOUNTS.FUND.ID` | `FsGaOperationCodesAccounts_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 12 | `FS.GA.OPERATION.CODES.ACCOUNTS.USE.ACCOUNT` | `FsGaOperationCodesAccounts_UseAccount` | TField |  | Allows defining if the account can be used or not for a fund conversion/migration. If No, then all the entries for defined account during a conversion will be ignored Multifonds DB Column is FLAG_REPRISE. |
| 13 | `FS.GA.OPERATION.CODES.ACCOUNTS.CHARGE.CODE` | `FsGaOperationCodesAccounts_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 14 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS2` | `FsGaOperationCodesAccounts_Nofrais2` | TField |  | NOFRAIS2 Multifonds DB Column is NOFRAIS2. |
| 15 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS3` | `FsGaOperationCodesAccounts_Nofrais3` | TField |  | NOFRAIS3 Multifonds DB Column is NOFRAIS3. |
| 16 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS4` | `FsGaOperationCodesAccounts_Nofrais4` | TField |  | NOFRAIS4 Multifonds DB Column is NOFRAIS4. |
| 17 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS5` | `FsGaOperationCodesAccounts_Nofrais5` | TField |  | NOFRAIS5 Multifonds DB Column is NOFRAIS5. |
| 18 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS6` | `FsGaOperationCodesAccounts_Nofrais6` | TField |  | NOFRAIS6 Multifonds DB Column is NOFRAIS6. |
| 19 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS7` | `FsGaOperationCodesAccounts_Nofrais7` | TField |  | NOFRAIS7 Multifonds DB Column is NOFRAIS7. |
| 20 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS8` | `FsGaOperationCodesAccounts_Nofrais8` | TField |  | NOFRAIS8 Multifonds DB Column is NOFRAIS8. |
| 21 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS9` | `FsGaOperationCodesAccounts_Nofrais9` | TField |  | NOFRAIS9 Multifonds DB Column is NOFRAIS9. |
| 22 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS10` | `FsGaOperationCodesAccounts_Nofrais10` | TField |  | NOFRAIS10 Multifonds DB Column is NOFRAIS10. |
| 23 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS11` | `FsGaOperationCodesAccounts_Nofrais11` | TField |  | NOFRAIS11 Multifonds DB Column is NOFRAIS11. |
| 24 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS12` | `FsGaOperationCodesAccounts_Nofrais12` | TField |  | NOFRAIS12 Multifonds DB Column is NOFRAIS12. |
| 25 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS13` | `FsGaOperationCodesAccounts_Nofrais13` | TField |  | NOFRAIS13 Multifonds DB Column is NOFRAIS13. |
| 26 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS14` | `FsGaOperationCodesAccounts_Nofrais14` | TField |  | NOFRAIS14 Multifonds DB Column is NOFRAIS14. |
| 27 | `FS.GA.OPERATION.CODES.ACCOUNTS.NOFRAIS15` | `FsGaOperationCodesAccounts_Nofrais15` | TField |  | NOFRAIS15 Multifonds DB Column is NOFRAIS15. |
| 28 | `FS.GA.OPERATION.CODES.ACCOUNTS.DESCRIPTION` | `FsGaOperationCodesAccounts_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 29 | `FS.GA.OPERATION.CODES.ACCOUNTS.DEBIT.ACCOUNT` | `FsGaOperationCodesAccounts_DebitAccount` | TField |  | Define the account number to be debited. Used for the specific journal functionality. Multifonds DB Column is NRUBR_DB. |
| 30 | `FS.GA.OPERATION.CODES.ACCOUNTS.CREDIT.ACCOUNT` | `FsGaOperationCodesAccounts_CreditAccount` | TField |  | Define the account number to be credited. Used for the specific journal functionality. Multifonds DB Column is NRUBR_CR. |
| 31 | `FS.GA.OPERATION.CODES.ACCOUNTS.DEBIT.ACCOUNT.SUFFIX` | `FsGaOperationCodesAccounts_DebitAccountSuffix` | TField |  | Define the account number suffix to be debited. Used for the specific journal functionality. Multifonds DB Column is NSUFF_DB. |
| 32 | `FS.GA.OPERATION.CODES.ACCOUNTS.CREDIT.ACCOUNT.SUFFIX` | `FsGaOperationCodesAccounts_CreditAccountSuffix` | TField |  | Define the account number suffix to be credited. Used for the specific journal functionality. Multifonds DB Column is NSUFF_CR. |
| 33 | `FS.GA.OPERATION.CODES.ACCOUNTS.DEBIT.MANAGER` | `FsGaOperationCodesAccounts_DebitManager` | TField |  | Define the debit manager. Used for the specific journal functionality. Multifonds DB Column is NS_PORTFOLIO_DB. |
| 34 | `FS.GA.OPERATION.CODES.ACCOUNTS.CREDIT.MANAGER` | `FsGaOperationCodesAccounts_CreditManager` | TField |  | Define the credit manager. Used for the specific journal functionality. Multifonds DB Column is NS_PORTFOLIO_CR. |
| 35 | `FS.GA.OPERATION.CODES.ACCOUNTS.DEPOSITORY.BANK.CODE` | `FsGaOperationCodesAccounts_DepositoryBankCode` | TField |  | Position for check status is used: if its Y&quot; then the load INSERTS a new line in the operation code equivalence. If its &quot;N&quot; then the load amends an already existing line in the op code equiv screen.&quot; Multifonds DB Column is CODE_DEP_BANK. |
| 36 | `FS.GA.OPERATION.CODES.ACCOUNTS.CHECKED.BY` | `FsGaOperationCodesAccounts_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 37 | `FS.GA.OPERATION.CODES.ACCOUNTS.CHECK.DATE` | `FsGaOperationCodesAccounts_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 38 | `FS.GA.OPERATION.CODES.ACCOUNTS.OPERATION.CODE` | `FsGaOperationCodesAccounts_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 39 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED10` | `FsGaOperationCodesAccounts_Reserved10` | TField |  |  |
| 40 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED9` | `FsGaOperationCodesAccounts_Reserved9` | TField |  |  |
| 41 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED8` | `FsGaOperationCodesAccounts_Reserved8` | TField |  |  |
| 42 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED7` | `FsGaOperationCodesAccounts_Reserved7` | TField |  |  |
| 43 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED6` | `FsGaOperationCodesAccounts_Reserved6` | TField |  |  |
| 44 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED5` | `FsGaOperationCodesAccounts_Reserved5` | TField |  |  |
| 45 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED4` | `FsGaOperationCodesAccounts_Reserved4` | TField |  |  |
| 46 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED3` | `FsGaOperationCodesAccounts_Reserved3` | TField |  |  |
| 47 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED2` | `FsGaOperationCodesAccounts_Reserved2` | TField |  |  |
| 48 | `FS.GA.OPERATION.CODES.ACCOUNTS.RESERVED1` | `FsGaOperationCodesAccounts_Reserved1` | TField |  |  |
| 49 | `FS.GA.OPERATION.CODES.ACCOUNTS.LOCAL.REF` | `FsGaOperationCodesAccounts_LocalRef` |  |  |  |
| 50 | `FS.GA.OPERATION.CODES.ACCOUNTS.OVERRIDE` | `FsGaOperationCodesAccounts_Override` |  |  |  |
| 51 | `FS.GA.OPERATION.CODES.ACCOUNTS.RECORD.STATUS` | `FsGaOperationCodesAccounts_RecordStatus` | String |  |  |
| 52 | `FS.GA.OPERATION.CODES.ACCOUNTS.CURR.NO` | `FsGaOperationCodesAccounts_CurrNo` | String |  |  |
| 53 | `FS.GA.OPERATION.CODES.ACCOUNTS.INPUTTER` | `FsGaOperationCodesAccounts_Inputter` |  |  |  |
| 54 | `FS.GA.OPERATION.CODES.ACCOUNTS.DATE.TIME` | `FsGaOperationCodesAccounts_DateTime` |  |  |  |
| 55 | `FS.GA.OPERATION.CODES.ACCOUNTS.AUTHORISER` | `FsGaOperationCodesAccounts_Authoriser` | String |  |  |
| 56 | `FS.GA.OPERATION.CODES.ACCOUNTS.CO.CODE` | `FsGaOperationCodesAccounts_CoCode` | String |  |  |
| 57 | `FS.GA.OPERATION.CODES.ACCOUNTS.DEPT.CODE` | `FsGaOperationCodesAccounts_DeptCode` | String |  |  |
| 58 | `FS.GA.OPERATION.CODES.ACCOUNTS.AUDITOR.CODE` | `FsGaOperationCodesAccounts_AuditorCode` | String |  |  |
| 59 | `FS.GA.OPERATION.CODES.ACCOUNTS.AUDIT.DATE.TIME` | `FsGaOperationCodesAccounts_AuditDateTime` | String |  |  |
