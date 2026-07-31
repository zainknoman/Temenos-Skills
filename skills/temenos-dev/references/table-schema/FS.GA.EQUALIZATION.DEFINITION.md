# FS.GA.EQUALIZATION.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUALIZATION.DEFINITION` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUALIZATION.DEFINITION.PARENT.REF.ID` | `FsGaEqualizationDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUALIZATION.DEFINITION.ORA.ROWID` | `FsGaEqualizationDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUALIZATION.DEFINITION.CHART.OF.ACCOUNTS.CODE` | `FsGaEqualizationDefinition_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.EQUALIZATION.DEFINITION.OPERATION.CODE` | `FsGaEqualizationDefinition_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.EQUALIZATION.DEFINITION.GTI.CODE` | `FsGaEqualizationDefinition_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.EQUALIZATION.DEFINITION.EQUALISATION.CHART` | `FsGaEqualizationDefinition_EqualisationChart` | TField |  | Enter equalization chart number. Multifonds DB Column is NRUBR_REGUL. |
| 7 | `FS.GA.EQUALIZATION.DEFINITION.DEBIT.ACCOUNT.NUMBER` | `FsGaEqualizationDefinition_DebitAccountNumber` | TField |  | Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB. |
| 8 | `FS.GA.EQUALIZATION.DEFINITION.CREDIT.ACCOUNT.NUMBER` | `FsGaEqualizationDefinition_CreditAccountNumber` | TField |  | Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR. |
| 9 | `FS.GA.EQUALIZATION.DEFINITION.CP.EQUALISATION.ACCOUNT.DEBIT` | `FsGaEqualizationDefinition_CpEqualisationAccountDebit` | TField |  | Counterparty account to be Debited Multifonds DB Column is NRUBRDB_CP. |
| 10 | `FS.GA.EQUALIZATION.DEFINITION.CP.EQUALISATION.ACCOUNT.CREDIT` | `FsGaEqualizationDefinition_CpEqualisationAccountCredit` | TField |  | Counterparty account to be Credited Multifonds DB Column is NRUBRCR_CP. |
| 11 | `FS.GA.EQUALIZATION.DEFINITION.YEAR.END.PNL.ACCOUNT.DEBIT` | `FsGaEqualizationDefinition_YearEndPnlAccountDebit` | TField |  | Profit and loss account to be debited at year end Multifonds DB Column is NRUBRDB_YE. |
| 12 | `FS.GA.EQUALIZATION.DEFINITION.YEAR.END.PNL.ACCOUNT.CREDIT` | `FsGaEqualizationDefinition_YearEndPnlAccountCredit` | TField |  | Profit and loss account to be credited at year end Multifonds DB Column is NRUBRCR_YE. |
| 13 | `FS.GA.EQUALIZATION.DEFINITION.CP.YEAR.END.PNL.ACCOUNT.DEBIT` | `FsGaEqualizationDefinition_CpYearEndPnlAccountDebit` | TField |  | Counterparty account to be debited at year end Multifonds DB Column is NRUBRDB_CP_YE. |
| 14 | `FS.GA.EQUALIZATION.DEFINITION.CP.YEAR.END.PNL.ACCOUNT.CREDIT` | `FsGaEqualizationDefinition_CpYearEndPnlAccountCredit` | TField |  | Counterparty account to be credited at year end Multifonds DB Column is NRUBRCR_CP_YE. |
| 15 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED10` | `FsGaEqualizationDefinition_Reserved10` | TField |  |  |
| 16 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED9` | `FsGaEqualizationDefinition_Reserved9` | TField |  |  |
| 17 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED8` | `FsGaEqualizationDefinition_Reserved8` | TField |  |  |
| 18 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED7` | `FsGaEqualizationDefinition_Reserved7` | TField |  |  |
| 19 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED6` | `FsGaEqualizationDefinition_Reserved6` | TField |  |  |
| 20 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED5` | `FsGaEqualizationDefinition_Reserved5` | TField |  |  |
| 21 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED4` | `FsGaEqualizationDefinition_Reserved4` | TField |  |  |
| 22 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED3` | `FsGaEqualizationDefinition_Reserved3` | TField |  |  |
| 23 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED2` | `FsGaEqualizationDefinition_Reserved2` | TField |  |  |
| 24 | `FS.GA.EQUALIZATION.DEFINITION.RESERVED1` | `FsGaEqualizationDefinition_Reserved1` | TField |  |  |
| 25 | `FS.GA.EQUALIZATION.DEFINITION.LOCAL.REF` | `FsGaEqualizationDefinition_LocalRef` |  |  |  |
| 26 | `FS.GA.EQUALIZATION.DEFINITION.OVERRIDE` | `FsGaEqualizationDefinition_Override` |  |  |  |
| 27 | `FS.GA.EQUALIZATION.DEFINITION.RECORD.STATUS` | `FsGaEqualizationDefinition_RecordStatus` | String |  |  |
| 28 | `FS.GA.EQUALIZATION.DEFINITION.CURR.NO` | `FsGaEqualizationDefinition_CurrNo` | String |  |  |
| 29 | `FS.GA.EQUALIZATION.DEFINITION.INPUTTER` | `FsGaEqualizationDefinition_Inputter` |  |  |  |
| 30 | `FS.GA.EQUALIZATION.DEFINITION.DATE.TIME` | `FsGaEqualizationDefinition_DateTime` |  |  |  |
| 31 | `FS.GA.EQUALIZATION.DEFINITION.AUTHORISER` | `FsGaEqualizationDefinition_Authoriser` | String |  |  |
| 32 | `FS.GA.EQUALIZATION.DEFINITION.CO.CODE` | `FsGaEqualizationDefinition_CoCode` | String |  |  |
| 33 | `FS.GA.EQUALIZATION.DEFINITION.DEPT.CODE` | `FsGaEqualizationDefinition_DeptCode` | String |  |  |
| 34 | `FS.GA.EQUALIZATION.DEFINITION.AUDITOR.CODE` | `FsGaEqualizationDefinition_AuditorCode` | String |  |  |
| 35 | `FS.GA.EQUALIZATION.DEFINITION.AUDIT.DATE.TIME` | `FsGaEqualizationDefinition_AuditDateTime` | String |  |  |
