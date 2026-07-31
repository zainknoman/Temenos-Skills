# FS.GI.PAYMENT.CASH.FLOW.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.PAYMENT.CASH.FLOW.DEFINITION` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PAYMENT.CASH.FLOW.DEF.CASH.FLOW.ID` | `FsGiPaymentCashFlowDefinition_CashFlowId` |  |  |  |
| 2 | `GI.PAYMENT.CASH.FLOW.DEF.PAYMENT.TYPE` | `FsGiPaymentCashFlowDefinition_PaymentType` |  |  |  |
| 3 | `GI.PAYMENT.CASH.FLOW.DEF.OPERATION.CODE` | `FsGiPaymentCashFlowDefinition_OperationCode` |  |  |  |
| 4 | `GI.PAYMENT.CASH.FLOW.DEF.STATUS` | `FsGiPaymentCashFlowDefinition_Status` |  |  |  |
| 5 | `GI.PAYMENT.CASH.FLOW.DEF.DEAL.TYPE` | `FsGiPaymentCashFlowDefinition_DealType` |  |  |  |
| 6 | `GI.PAYMENT.CASH.FLOW.DEF.EVENT` | `FsGiPaymentCashFlowDefinition_Event` |  |  |  |
| 7 | `GI.PAYMENT.CASH.FLOW.DEF.CORRECTION.FLAG` | `FsGiPaymentCashFlowDefinition_CorrectionFlag` |  |  |  |
| 8 | `METHOD` | `method` |  |  |  |
| 9 | `GI.PAYMENT.CASH.FLOW.DEF.PL.BEARING.CODE` | `FsGiPaymentCashFlowDefinition_PlBearingCode` |  |  |  |
| 10 | `GI.PAYMENT.CASH.FLOW.DEF.SETTLEMENT.TYPE` | `FsGiPaymentCashFlowDefinition_SettlementType` |  |  |  |
| 11 | `GI.PAYMENT.CASH.FLOW.DEF.SETTLEMENT.MONEY` | `FsGiPaymentCashFlowDefinition_SettlementMoney` |  |  |  |
| 12 | `GI.PAYMENT.CASH.FLOW.DEF.CUSTODY.SETTLEMENT` | `FsGiPaymentCashFlowDefinition_CustodySettlement` |  |  |  |
| 13 | `GI.PAYMENT.CASH.FLOW.DEF.AGENT.GROUP` | `FsGiPaymentCashFlowDefinition_AgentGroup` |  |  |  |
| 14 | `GI.PAYMENT.CASH.FLOW.DEF.CASHFLOW.PAYMENT.CURRENCY` | `FsGiPaymentCashFlowDefinition_CashflowPaymentCurrency` |  |  |  |
| 15 | `GI.PAYMENT.CASH.FLOW.DEF.CASHFLOW.QUOTATION.CURRENCY` | `FsGiPaymentCashFlowDefinition_CashflowQuotationCurrency` |  |  |  |
| 16 | `GI.PAYMENT.CASH.FLOW.DEF.EURO.PAY.COUNTRY` | `FsGiPaymentCashFlowDefinition_EuroPayCountry` |  |  |  |
| 17 | `GI.PAYMENT.CASH.FLOW.DEF.FLAG.FX` | `FsGiPaymentCashFlowDefinition_FlagFx` |  |  |  |
| 18 | `GI.PAYMENT.CASH.FLOW.DEF.FUND.TYPE` | `FsGiPaymentCashFlowDefinition_FundType` |  |  |  |
| 19 | `GI.PAYMENT.CASH.FLOW.DEF.TYPE.OF.PAYMENT` | `FsGiPaymentCashFlowDefinition_TypeOfPayment` |  |  |  |
| 20 | `GI.PAYMENT.CASH.FLOW.DEF.CUSTODIAN` | `FsGiPaymentCashFlowDefinition_Custodian` |  |  |  |
| 21 | `GI.PAYMENT.CASH.FLOW.DEF.INTERNAL.SEQUENCE.NUMBER` | `FsGiPaymentCashFlowDefinition_InternalSequenceNumber` |  |  |  |
| 22 | `GI.PAYMENT.CASH.FLOW.DEF.TAX.ID.COMMENT` | `FsGiPaymentCashFlowDefinition_TaxIdComment` |  |  |  |
| 23 | `GI.PAYMENT.CASH.FLOW.DEF.DEBIT.ENTITY` | `FsGiPaymentCashFlowDefinition_DebitEntity` |  |  |  |
| 24 | `GI.PAYMENT.CASH.FLOW.DEF.DEBIT.ACCOUNT.TYPE` | `FsGiPaymentCashFlowDefinition_DebitAccountType` |  |  |  |
| 25 | `GI.PAYMENT.CASH.FLOW.DEF.CREDIT.ENTITY` | `FsGiPaymentCashFlowDefinition_CreditEntity` |  |  |  |
| 26 | `GI.PAYMENT.CASH.FLOW.DEF.CREDIT.ACCOUNT.TYPE` | `FsGiPaymentCashFlowDefinition_CreditAccountType` |  |  |  |
| 27 | `GI.PAYMENT.CASH.FLOW.DEF.HOLD.ACCOUNT.ENTITY` | `FsGiPaymentCashFlowDefinition_HoldAccountEntity` |  |  |  |
| 28 | `GI.PAYMENT.CASH.FLOW.DEF.HOLD.ACCOUNT.TYPE` | `FsGiPaymentCashFlowDefinition_HoldAccountType` |  |  |  |
| 29 | `GI.PAYMENT.CASH.FLOW.DEF.HOLD.MOVEMENT.TYPE` | `FsGiPaymentCashFlowDefinition_HoldMovementType` |  |  |  |
| 30 | `GI.PAYMENT.CASH.FLOW.DEF.SINGLE.COMPONENT` | `FsGiPaymentCashFlowDefinition_SingleComponent` |  |  |  |
| 31 | `GI.PAYMENT.CASH.FLOW.DEF.GROUP.COMPONENT` | `FsGiPaymentCashFlowDefinition_GroupComponent` |  |  |  |
| 32 | `GI.PAYMENT.CASH.FLOW.DEF.PERCENTAGE` | `FsGiPaymentCashFlowDefinition_Percentage` |  |  |  |
| 33 | `GI.PAYMENT.CASH.FLOW.DEF.MOVEMENT.TYPE` | `FsGiPaymentCashFlowDefinition_MovementType` |  |  |  |
| 34 | `GI.PAYMENT.CASH.FLOW.DEF.MT210.FLAG` | `FsGiPaymentCashFlowDefinition_Mt210Flag` |  |  |  |
| 35 | `GI.PAYMENT.CASH.FLOW.DEF.INSTRUCTION.TYPE` | `FsGiPaymentCashFlowDefinition_InstructionType` |  |  |  |
| 36 | `GI.PAYMENT.CASH.FLOW.DEF.DEFAULT.COMMISSION.TYPE` | `FsGiPaymentCashFlowDefinition_DefaultCommissionType` |  |  |  |
| 37 | `GI.PAYMENT.CASH.FLOW.DEF.PAYMENT.DESTINATION` | `FsGiPaymentCashFlowDefinition_PaymentDestination` |  |  |  |
| 38 | `GI.PAYMENT.CASH.FLOW.DEF.CHARGES.CODE` | `FsGiPaymentCashFlowDefinition_ChargesCode` |  |  |  |
| 39 | `GI.PAYMENT.CASH.FLOW.DEF.NETTING.GROUP` | `FsGiPaymentCashFlowDefinition_NettingGroup` |  |  |  |
| 40 | `GI.PAYMENT.CASH.FLOW.DEF.NETTING.GROUP.TYPE` | `FsGiPaymentCashFlowDefinition_NettingGroupType` |  |  |  |
| 41 | `GI.PAYMENT.CASH.FLOW.DEF.PAYMENT.REFERENCE.ID` | `FsGiPaymentCashFlowDefinition_PaymentReferenceId` |  |  |  |
| 42 | `GI.PAYMENT.CASH.FLOW.DEF.EXCLUDE.PAYMENT` | `FsGiPaymentCashFlowDefinition_ExcludePayment` |  |  |  |
| 43 | `GI.PAYMENT.CASH.FLOW.DEF.NO.PAYMENT` | `FsGiPaymentCashFlowDefinition_NoPayment` |  |  |  |
| 44 | `GI.PAYMENT.CASH.FLOW.DEF.RECONCILIATION.FLAG` | `FsGiPaymentCashFlowDefinition_ReconciliationFlag` |  |  |  |
| 45 | `GI.PAYMENT.CASH.FLOW.DEF.PAYMENT.AMOUNT.HANDLING` | `FsGiPaymentCashFlowDefinition_PaymentAmountHandling` |  |  |  |
| 46 | `GI.PAYMENT.CASH.FLOW.DEF.SEQUENCE.NUMBER` | `FsGiPaymentCashFlowDefinition_SequenceNumber` |  |  |  |
| 47 | `GI.PAYMENT.CASH.FLOW.DEF.CURRENCY.CODE` | `FsGiPaymentCashFlowDefinition_CurrencyCode` |  |  |  |
| 48 | `GI.PAYMENT.CASH.FLOW.DEF.LINKED.SEQUENCE.NUMBER` | `FsGiPaymentCashFlowDefinition_LinkedSequenceNumber` |  |  |  |
| 49 | `GI.PAYMENT.CASH.FLOW.DEF.ORIGINAL.UPDATED.SEQUENCE` | `FsGiPaymentCashFlowDefinition_OriginalUpdatedSequence` |  |  |  |
| 50 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED10` | `FsGiPaymentCashFlowDefinition_Reserved10` |  |  |  |
| 51 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED9` | `FsGiPaymentCashFlowDefinition_Reserved9` |  |  |  |
| 52 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED8` | `FsGiPaymentCashFlowDefinition_Reserved8` |  |  |  |
| 53 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED7` | `FsGiPaymentCashFlowDefinition_Reserved7` |  |  |  |
| 54 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED6` | `FsGiPaymentCashFlowDefinition_Reserved6` |  |  |  |
| 55 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED5` | `FsGiPaymentCashFlowDefinition_Reserved5` |  |  |  |
| 56 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED4` | `FsGiPaymentCashFlowDefinition_Reserved4` |  |  |  |
| 57 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED3` | `FsGiPaymentCashFlowDefinition_Reserved3` |  |  |  |
| 58 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED2` | `FsGiPaymentCashFlowDefinition_Reserved2` |  |  |  |
| 59 | `GI.PAYMENT.CASH.FLOW.DEF.RESERVED1` | `FsGiPaymentCashFlowDefinition_Reserved1` |  |  |  |
| 60 | `GI.PAYMENT.CASH.FLOW.DEF.LOCAL.REF` | `FsGiPaymentCashFlowDefinition_LocalRef` |  |  |  |
| 61 | `GI.PAYMENT.CASH.FLOW.DEF.OVERRIDE` | `FsGiPaymentCashFlowDefinition_Override` |  |  |  |
| 62 | `GI.PAYMENT.CASH.FLOW.DEF.RECORD.STATUS` | `FsGiPaymentCashFlowDefinition_RecordStatus` |  |  |  |
| 63 | `GI.PAYMENT.CASH.FLOW.DEF.CURR.NO` | `FsGiPaymentCashFlowDefinition_CurrNo` |  |  |  |
| 64 | `GI.PAYMENT.CASH.FLOW.DEF.INPUTTER` | `FsGiPaymentCashFlowDefinition_Inputter` |  |  |  |
| 65 | `GI.PAYMENT.CASH.FLOW.DEF.DATE.TIME` | `FsGiPaymentCashFlowDefinition_DateTime` |  |  |  |
| 66 | `GI.PAYMENT.CASH.FLOW.DEF.AUTHORISER` | `FsGiPaymentCashFlowDefinition_Authoriser` |  |  |  |
| 67 | `GI.PAYMENT.CASH.FLOW.DEF.CO.CODE` | `FsGiPaymentCashFlowDefinition_CoCode` |  |  |  |
| 68 | `GI.PAYMENT.CASH.FLOW.DEF.DEPT.CODE` | `FsGiPaymentCashFlowDefinition_DeptCode` |  |  |  |
| 69 | `GI.PAYMENT.CASH.FLOW.DEF.AUDITOR.CODE` | `FsGiPaymentCashFlowDefinition_AuditorCode` |  |  |  |
| 70 | `GI.PAYMENT.CASH.FLOW.DEF.AUDIT.DATE.TIME` | `FsGiPaymentCashFlowDefinition_AuditDateTime` |  |  |  |
