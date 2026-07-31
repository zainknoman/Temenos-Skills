# HUWRNT.QUEUE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.PARAMETER` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.QPARAM.CCY.MKT.COLLECTION` | `HuwrntQueueParameter_CcyMktCollection` | TField |  | Specifies the currency market for collection purpose. |
| 2 | `HUWRNT.QPARAM.MIN.PENSION.AMOUNT` | `HuwrntQueueParameter_MinPensionAmount` | TField |  | Specifies the Minimum Retirement Pension amount as declared by Hungarian Govt. Exempt amount calculation depends on this MIN.PENSION value. |
| 3 | `HUWRNT.QPARAM.EXEMPT.PRCNT.REM.BAL` | `HuwrntQueueParameter_ExemptPrcntRemBal` | TField |  | Indicates the percentage of remaining balance that should be added with Minimum Pension Amount to arrive at Exempt Amount. |
| 4 | `HUWRNT.QPARAM.UPPER.LIMIT.AMOUNT` | `HuwrntQueueParameter_UpperLimitAmount` | TField |  | Indicates the upper limit of pension that is used for Exempt amount calculation. Currently it is 4 times minimum pension amount. |
| 5 | `HUWRNT.QPARAM.MIN.PAYMENT.AMOUNT` | `HuwrntQueueParameter_MinPaymentAmount` | TField |  | Specifies the minimum amount for partial collection for collection instruments. |
| 6 | `HUWRNT.QPARAM.CCY.PRIORITY` | `HuwrntQueueParameter_CcyPriority` |  |  |  |
| 7 | `HUWRNT.QPARAM.DATE.CONVENTION` | `HuwrntQueueParameter_DateConvention` | TField |  | This field is no longer in use. |
| 8 | `HUWRNT.QPARAM.CCY.TOLERANCE` | `HuwrntQueueParameter_CcyTolerance` | TField |  | Specifies the mark up which is allowed during currency conversion. It accepts both positive and negative values. |
| 9 | `HUWRNT.QPARAM.CONVERSION.RATE` | `HuwrntQueueParameter_ConversionRate` | TField |  | Specifies the type of rate to be applied during currency conversion. |
| 10 | `HUWRNT.QPARAM.LOCK.APPLICABLE` | `HuwrntQueueParameter_LockApplicable` | TField |  | Specifies whether we should lock the amount during balance request of loans. |
| 11 | `HUWRNT.QPARAM.NAME.NUMBER.CHECK.ROUTINE` | `HuwrntQueueParameter_NameNumberCheckRoutine` | TField | No | The Field contains the routine which checks the name number mismatch. It should be a valid record in EB.API table. Arguments: 1. Payer Account Number(In) 2. Queue Reference(In) 3. Response(Out) - Yes/No If the response is "Yes", it means there is a mismatch and user intervention is needed else do the customer liquidation check. Validation Rules Optional Input |
| 12 | `HUWRNT.QPARAM.CUSTOMER.LIQUIDATION.CHECK.RTN` | `HuwrntQueueParameter_CustomerLiquidationCheckRtn` | TField | No | The Field contains the routine which checks the Customer liquidation status. It should be a valid record in EB.API table. Arguments: 1. Customer Id(In) 2. Response(Out) - Yes/No If the response is "Yes", it means there is a mismatch and user intervention is needed else do the currency mismatch check. Validation Rules Optional Input |
| 13 | `HUWRNT.QPARAM.COT.SETTLEMENT` | `HuwrntQueueParameter_CotSettlement` | TField |  | Specifies the Cut off time for settlement service in case of partial settlement |
| 14 | `HUWRNT.QPARAM.DEBIT.TXN.CODE` | `HuwrntQueueParameter_DebitTxnCode` | TField |  | Specifies the debit transaction code |
| 15 | `HUWRNT.QPARAM.CREDIT.TXN.CODE` | `HuwrntQueueParameter_CreditTxnCode` | TField |  | Specifies the credit transaction code |
| 16 | `HUWRNT.QPARAM.PENALTY.INT.PROPERTY` | `HuwrntQueueParameter_PenaltyIntProperty` | TField |  | Contains the Penalty Interest property name. |
| 17 | `HUWRNT.QPARAM.LOCK.PRIORITY` | `HuwrntQueueParameter_LockPriority` |  |  |  |
| 18 | `HUWRNT.QPARAM.LOCK.TYPE.ID` | `HuwrntQueueParameter_LockTypeId` |  |  |  |
| 19 | `HUWRNT.QPARAM.LOAN.COMPONENT` | `HuwrntQueueParameter_LoanComponent` |  |  |  |
| 20 | `HUWRNT.QPARAM.LOAN.DEBIT.TXN.CODE` | `HuwrntQueueParameter_LoanDebitTxnCode` |  |  |  |
| 21 | `HUWRNT.QPARAM.LOAN.CREDIT.TXN.CODE` | `HuwrntQueueParameter_LoanCreditTxnCode` |  |  |  |
| 22 | `HUWRNT.QPARAM.LOCAL.REF` | `HuwrntQueueParameter_LocalRef` |  |  |  |
| 23 | `HUWRNT.QPARAM.OVERRIDE` | `HuwrntQueueParameter_Override` |  |  |  |
| 24 | `HUWRNT.QPARAM.RECORD.STATUS` | `HuwrntQueueParameter_RecordStatus` | String |  |  |
| 25 | `HUWRNT.QPARAM.CURR.NO` | `HuwrntQueueParameter_CurrNo` | String |  |  |
| 26 | `HUWRNT.QPARAM.INPUTTER` | `HuwrntQueueParameter_Inputter` |  |  |  |
| 27 | `HUWRNT.QPARAM.DATE.TIME` | `HuwrntQueueParameter_DateTime` |  |  |  |
| 28 | `HUWRNT.QPARAM.AUTHORISER` | `HuwrntQueueParameter_Authoriser` | String |  |  |
| 29 | `HUWRNT.QPARAM.CO.CODE` | `HuwrntQueueParameter_CoCode` | String |  |  |
| 30 | `HUWRNT.QPARAM.DEPT.CODE` | `HuwrntQueueParameter_DeptCode` | String |  |  |
| 31 | `HUWRNT.QPARAM.AUDITOR.CODE` | `HuwrntQueueParameter_AuditorCode` | String |  |  |
| 32 | `HUWRNT.QPARAM.AUDIT.DATE.TIME` | `HuwrntQueueParameter_AuditDateTime` | String |  |  |
| 33 | `HUWRNT.QPARAM.SWEEP.DR.TXN` | `HuwrntQueueParameter_SweepDrTxn` | TField |  | Specifies the Debit transaction code for sweep transactions related to Warrants, Loans and UOD.. |
| 34 | `HUWRNT.QPARAM.SWEEP.CR.TXN` | `HuwrntQueueParameter_SweepCrTxn` | TField |  | Specifies the Credit transaction code for sweep transactions related to Warrants, Loans and UOD. |
| 35 | `HUWRNT.QPARAM.AUTO.SETTLE.DR.TXN` | `HuwrntQueueParameter_AutoSettleDrTxn` | TField |  | Specifies the Debit transaction code for automatic settlement of Warrants. |
| 36 | `HUWRNT.QPARAM.AUTO.SETTLE.CR.TXN` | `HuwrntQueueParameter_AutoSettleCrTxn` | TField |  | Specifies the Credit transaction code for automatic settlement of Warrants. |
| 37 | `HUWRNT.QPARAM.MANUAL.SETTLE.DR.TXN` | `HuwrntQueueParameter_ManualSettleDrTxn` | TField |  | Specifies the Debit transaction code for manual settlement of Warrants. |
| 38 | `HUWRNT.QPARAM.MANUAL.SETTLE.CR.TXN` | `HuwrntQueueParameter_ManualSettleCrTxn` | TField |  | Specifies the Credit transaction code for manual settlement of Warrants. |
