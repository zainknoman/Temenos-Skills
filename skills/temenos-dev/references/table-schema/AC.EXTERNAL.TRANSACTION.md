# AC.EXTERNAL.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.AC.EXTERNAL.TRANSACTION` in `AC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.XT.EVENT.REFERENCE` | `AcExternalTransaction_EventReference` | TField |  |  |
| 2 | `AC.XT.EX.TYPE` | `AcExternalTransaction_ExType` | TField |  |  |
| 3 | `AC.XT.TRANSACTION.ID` | `AcExternalTransaction_TransactionId` |  |  |  |
| 4 | `AC.XT.TRANSACTION.SYS.ID` | `AcExternalTransaction_TransactionSysId` |  |  |  |
| 5 | `AC.XT.CONTRACT.ID` | `AcExternalTransaction_ContractId` |  |  |  |
| 6 | `AC.XT.CONTRACT.SYS.ID` | `AcExternalTransaction_ContractSysId` |  |  |  |
| 7 | `AC.XT.RULE.ID` | `AcExternalTransaction_RuleId` |  |  |  |
| 8 | `AC.XT.EVENT.TYPE` | `AcExternalTransaction_EventType` |  |  |  |
| 9 | `AC.XT.EVENT.CCY` | `AcExternalTransaction_EventCcy` |  |  |  |
| 10 | `AC.XT.SIGN` | `AcExternalTransaction_Sign` |  |  |  |
| 11 | `AC.XT.AMOUNT` | `AcExternalTransaction_Amount` |  |  |  |
| 12 | `AC.XT.AMOUNT.LCY` | `AcExternalTransaction_AmountLcy` |  |  |  |
| 13 | `AC.XT.EXCHRATE` | `AcExternalTransaction_Exchrate` |  |  |  |
| 14 | `AC.XT.VALUE.DATE` | `AcExternalTransaction_ValueDate` |  |  |  |
| 15 | `AC.XT.EXPOSURE.DATE` | `AcExternalTransaction_ExposureDate` |  |  |  |
| 16 | `AC.XT.BAL.SUB.TYPE` | `AcExternalTransaction_BalSubType` |  |  |  |
| 17 | `AC.XT.REVERSAL.IND` | `AcExternalTransaction_ReversalInd` |  |  |  |
| 18 | `AC.XT.BALANCE.TYPE` | `AcExternalTransaction_BalanceType` |  |  |  |
| 19 | `AC.XT.CONTRA.TARGET` | `AcExternalTransaction_ContraTarget` |  |  |  |
| 20 | `AC.XT.DIRECT.ACCT` | `AcExternalTransaction_DirectAcct` |  |  |  |
| 21 | `AC.XT.ORIG.TXN.ID` | `AcExternalTransaction_OrigTxnId` |  |  |  |
| 22 | `AC.XT.ORIG.TXN.SYS.ID` | `AcExternalTransaction_OrigTxnSysId` |  |  |  |
| 23 | `AC.XT.VARIABLE.NAME` | `AcExternalTransaction_VariableName` |  |  |  |
| 24 | `AC.XT.VARIABLE.VALUE` | `AcExternalTransaction_VariableValue` |  |  |  |
| 25 | `AC.XT.BOOKING.DATE` | `AcExternalTransaction_BookingDate` |  |  |  |
| 26 | `AC.XT.TAX.DATA` | `AcExternalTransaction_TaxData` |  |  |  |
| 27 | `AC.XT.BOOKING.COMPANY` | `AcExternalTransaction_BookingCompany` |  |  |  |
| 28 | `AC.XT.DEPARTMENT.CODE` | `AcExternalTransaction_DepartmentCode` |  |  |  |
| 29 | `AC.XT.PARENT.TXN.ID` | `AcExternalTransaction_ParentTxnId` |  |  |  |
| 30 | `AC.XT.PARENT.TXN.SYS.ID` | `AcExternalTransaction_ParentTxnSysId` |  |  |  |
| 31 | `AC.XT.PROCESSING.DATE` | `AcExternalTransaction_ProcessingDate` |  |  |  |
| 32 | `AC.XT.CONTRACT.BAL.ID` | `AcExternalTransaction_ContractBalId` |  |  |  |
| 33 | `AC.XT.CUSTOMER` | `AcExternalTransaction_Customer` |  |  |  |
| 34 | `AC.XT.REPORTING.CUSTOMER` | `AcExternalTransaction_ReportingCustomer` |  |  |  |
| 35 | `AC.XT.CURRENCY.MARKET` | `AcExternalTransaction_CurrencyMarket` |  |  |  |
| 36 | `AC.XT.POSITION.TYPE` | `AcExternalTransaction_PositionType` |  |  |  |
| 37 | `AC.XT.CATEGORY` | `AcExternalTransaction_Category` |  |  |  |
| 38 | `AC.XT.ACCOUNT.OFFICER` | `AcExternalTransaction_AccountOfficer` |  |  |  |
| 39 | `AC.XT.START.DATE` | `AcExternalTransaction_StartDate` |  |  |  |
| 40 | `AC.XT.MATURITY.DATE` | `AcExternalTransaction_MaturityDate` |  |  |  |
| 41 | `AC.XT.RESERVED.1` | `AcExternalTransaction_Reserved1` |  |  |  |
| 42 | `AC.XT.RESERVED.2` | `AcExternalTransaction_Reserved2` |  |  |  |
| 43 | `AC.XT.RESERVED.3` | `AcExternalTransaction_Reserved3` |  |  |  |
| 44 | `AC.XT.RESERVED.4` | `AcExternalTransaction_Reserved4` |  |  |  |
| 45 | `AC.XT.RESERVED.5` | `AcExternalTransaction_Reserved5` |  |  |  |
| 46 | `AC.XT.SYSTEM.IDENTIFIER` | `AcExternalTransaction_SystemIdentifier` | TField |  |  |
| 47 | `AC.XT.ACCOUNTING.ACTION` | `AcExternalTransaction_AccountingAction` | TField |  |  |
| 48 | `AC.XT.RESERVED.6` | `AcExternalTransaction_Reserved6` | TField |  |  |
| 49 | `AC.XT.RESERVED.7` | `AcExternalTransaction_Reserved7` | TField |  |  |
| 50 | `AC.XT.RESERVED.8` | `AcExternalTransaction_Reserved8` | TField |  |  |
| 51 | `AC.XT.RESERVED.9` | `AcExternalTransaction_Reserved9` | TField |  |  |
| 52 | `AC.XT.RESERVED.10` | `AcExternalTransaction_Reserved10` | TField |  |  |
| 53 | `AC.XT.LOCAL.REF` | `AcExternalTransaction_LocalRef` |  |  |  |
| 54 | `AC.XT.STMT.NOS` | `AcExternalTransaction_StmtNos` |  |  |  |
| 55 | `AC.XT.OVERRIDE` | `AcExternalTransaction_Override` |  |  |  |
| 56 | `AC.XT.RECORD.STATUS` | `AcExternalTransaction_RecordStatus` | String |  |  |
| 57 | `AC.XT.CURR.NO` | `AcExternalTransaction_CurrNo` | String |  |  |
| 58 | `AC.XT.INPUTTER` | `AcExternalTransaction_Inputter` |  |  |  |
| 59 | `AC.XT.DATE.TIME` | `AcExternalTransaction_DateTime` |  |  |  |
| 60 | `AC.XT.AUTHORISER` | `AcExternalTransaction_Authoriser` | String |  |  |
| 61 | `AC.XT.CO.CODE` | `AcExternalTransaction_CoCode` | String |  |  |
| 62 | `AC.XT.DEPT.CODE` | `AcExternalTransaction_DeptCode` | String |  |  |
| 63 | `AC.XT.AUDITOR.CODE` | `AcExternalTransaction_AuditorCode` | String |  |  |
| 64 | `AC.XT.AUDIT.DATE.TIME` | `AcExternalTransaction_AuditDateTime` | String |  |  |
