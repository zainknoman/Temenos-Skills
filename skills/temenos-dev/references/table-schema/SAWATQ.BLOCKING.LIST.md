# SAWATQ.BLOCKING.LIST — Table Schema

> Source: `INSERTS/I_F.SAWATQ.BLOCKING.LIST` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.BLOCK.LEGAL.ID` | `SawatqBlockingList_LegalId` | TField |  |  |
| 2 | `SA.BLOCK.LEGAL.DOC.NAME` | `SawatqBlockingList_LegalDocName` | TField |  | Legal doc Name is mapped from concat table in case of customer. In case of Non-customer , the legal id is updated from the request |
| 3 | `SA.BLOCK.INQUIRED.PARTY` | `SawatqBlockingList_InquiredParty` | TField |  | Type of involved party. Corporate C Government G Charity H Chamber M INdividual I |
| 4 | `SA.BLOCK.FIRST.NAME` | `SawatqBlockingList_FirstName` | TField |  | First Name of the individual |
| 5 | `SA.BLOCK.SECOND.NAME` | `SawatqBlockingList_SecondName` | TField |  | SecoNd Name of the individual |
| 6 | `SA.BLOCK.THIRD.NAME` | `SawatqBlockingList_ThirdName` | TField |  | Third Name of the individual |
| 7 | `SA.BLOCK.LAST.NAME` | `SawatqBlockingList_LastName` | TField |  | Last Name of the individual |
| 8 | `SA.BLOCK.NATIONALITY` | `SawatqBlockingList_Nationality` | TField |  | Nationality of the individual |
| 9 | `SA.BLOCK.NON.INDIVIDUAL.NAME` | `SawatqBlockingList_NonIndividualName` | TField |  | Non Individual Name is corporate name |
| 10 | `SA.BLOCK.DECISION.NUMBER` | `SawatqBlockingList_DecisionNumber` |  |  |  |
| 11 | `SA.BLOCK.DECISION.DATE` | `SawatqBlockingList_DecisionDate` |  |  |  |
| 12 | `SA.BLOCK.BLOCKING.TYPE` | `SawatqBlockingList_BlockingType` | TField |  | Type of block. It is also parameterised iN SAWATQ.BLOCKING.PARAMETER |
| 13 | `SA.BLOCK.POSTING.RESTRICT` | `SawatqBlockingList_PostingRestrict` | TField |  |  |
| 14 | `SA.BLOCK.IS.REVERSE` | `SawatqBlockingList_IsReverse` | TField |  | Y - Specifies that the request is the reversal of the block. N- Specifies that the request is Not a reversal of the block. The request for reversal will come iN the same SRN . |
| 15 | `SA.BLOCK.IS.OVERRIDE` | `SawatqBlockingList_IsOverride` | TField |  | Y - Specifies that the request is the Override of the block. N- Specifies that the request is Not a Override of the block. The request for Override will come iN the same SRN . |
| 16 | `SA.BLOCK.DEBIT.TYPE` | `SawatqBlockingList_DebitType` | TField |  | EB.LOOKUP records will be created for the below LOV. (Applicable for Block) 01 Normal 02 GoverNmeNt 03 Nafaqa |
| 17 | `SA.BLOCK.CASE.TYPE` | `SawatqBlockingList_CaseType` | TField |  | EB.LOOKUP records will be created for the below LOV.(Applicable for GarNishmeNt ) 01 Money laundering 02 Fraud and embezzlement 03 Commercial Fraud 04 Commercial concealment 05 Counterfeiting and Counterfeiting 06 Criminal |
| 18 | `SA.BLOCK.DURATION.TYPE` | `SawatqBlockingList_DurationType` | TField |  | EB.LOOKUP records will be created for the below LOV.(Applicable for GarNishmeNt ) 01 PermeaNt 02 Temporary |
| 19 | `SA.BLOCK.EXECUTION.START.DATE` | `SawatqBlockingList_ExecutionStartDate` | TField |  | Applicable for Garnishment only |
| 20 | `SA.BLOCK.EXECUTION.PERIOD` | `SawatqBlockingList_ExecutionPeriod` | TField |  | Applicable for Garnishment only |
| 21 | `SA.BLOCK.EXECUTION.END.DATE` | `SawatqBlockingList_ExecutionEndDate` | TField |  | Applicable for Garnishment only |
| 22 | `SA.BLOCK.CURRENCY` | `SawatqBlockingList_Currency` | TField |  | The currency in which the block is requested. |
| 23 | `SA.BLOCK.TARGET.AMOUNT` | `SawatqBlockingList_TargetAmount` | TField |  | Target amount to be blocked in case of block or garnishment |
| 24 | `SA.BLOCK.PENDING.AMOUNT` | `SawatqBlockingList_PendingAmount` | TField |  | Pending amount to be blocked . Will be updated in case of ovveride. |
| 25 | `SA.BLOCK.TARGET.ACCOUNT.NUMBER` | `SawatqBlockingList_TargetAccountNumber` |  |  |  |
| 26 | `SA.BLOCK.TARGET.IS.IBAN` | `SawatqBlockingList_TargetIsIban` |  |  |  |
| 27 | `SA.BLOCK.TARGET.BIC` | `SawatqBlockingList_TargetBic` |  |  |  |
| 28 | `SA.BLOCK.TARGET.ACCOUNT.STATUS` | `SawatqBlockingList_TargetAccountStatus` |  |  |  |
| 29 | `SA.BLOCK.TARGET.PRODUCTS` | `SawatqBlockingList_TargetProducts` |  |  |  |
| 30 | `SA.BLOCK.REQUIRED.TGT.PRD.STATUS` | `SawatqBlockingList_RequiredTgtPrdStatus` |  |  |  |
| 31 | `SA.BLOCK.REQUIRED.EXECUTION.INFO` | `SawatqBlockingList_RequiredExecutionInfo` |  |  |  |
| 32 | `SA.BLOCK.REQUIRED.EXECUTION.INFO.STATUS` | `SawatqBlockingList_RequiredExecutionInfoStatus` |  |  |  |
| 33 | `SA.BLOCK.PARTIAL.LIFT` | `SawatqBlockingList_PartialLift` | TField |  | Specifies if the lift is partial or a full lift. Applicable only in case of Block and Garnish Y - Specifies partial lift n- Specifies full lift |
| 34 | `SA.BLOCK.LIFT.ACCOUNT.NUMBER` | `SawatqBlockingList_LiftAccountNumber` |  |  |  |
| 35 | `SA.BLOCK.LIFT.IS.IBAN` | `SawatqBlockingList_LiftIsIban` |  |  |  |
| 36 | `SA.BLOCK.LIFT.BIC` | `SawatqBlockingList_LiftBic` |  |  |  |
| 37 | `SA.BLOCK.LIFT.DEPOSIT.NUMBER` | `SawatqBlockingList_LiftDepositNumber` |  |  |  |
| 38 | `SA.BLOCK.LIFT.DEPOSIT.BIC` | `SawatqBlockingList_LiftDepositBic` |  |  |  |
| 39 | `SA.BLOCK.LIFT.DECISION.NUMBER` | `SawatqBlockingList_LiftDecisionNumber` | TField |  | The decision number for blocking request. |
| 40 | `SA.BLOCK.LIFT.DECISION.DATE` | `SawatqBlockingList_LiftDecisionDate` | TField |  | The date on which the blocking decision was taken |
| 41 | `SA.BLOCK.LIFT.TRANSFER.TARGET.AMOUNT` | `SawatqBlockingList_LiftTransferTargetAmount` | TField |  | Specifies the amount to be transferred on lifting the block. |
| 42 | `SA.BLOCK.LIFT.TRANSFER.NAME` | `SawatqBlockingList_LiftTransferName` | TField |  | Specifies the name of the customer to whom the amount will be transferred on lifting the block. |
| 43 | `SA.BLOCK.LIFT.TRANSFER.ACCOUNT.IBAN` | `SawatqBlockingList_LiftTransferAccountIban` | TField |  | Specifies the account details of the customer to whom the amount will be transferred on lifting the block. |
| 44 | `SA.BLOCK.LIFT.TRANSFER.ACCOUNT.BIC` | `SawatqBlockingList_LiftTransferAccountBic` | TField |  | Specifies the BIC details of the account to whom the amount will be transferred on lifting the block. |
| 45 | `SA.BLOCK.CUSTOMER.NAME` | `SawatqBlockingList_CustomerName` |  |  |  |
| 46 | `SA.BLOCK.CUSTOMER.NUMBER` | `SawatqBlockingList_CustomerNumber` |  |  |  |
| 47 | `SA.BLOCK.BLOCK.EXECUTION.DATE.AND.TIME` | `SawatqBlockingList_BlockExecutionDateAndTime` | TField |  | Specifies the date and time at which the block is executed |
| 48 | `SA.BLOCK.TOTAL.BLOCKED.AMOUNT` | `SawatqBlockingList_TotalBlockedAmount` | TField |  | Specifies the total amount blocked from all accounts in the source currency. Example, if the requested block is for 9000 USD, this field specifies the total of the below: 9000=1000 USD + 33750 SAR ( 33750 SAR converted in USD ) |
| 49 | `SA.BLOCK.TOTAL.BLOCKED.AMOUNT.SAR` | `SawatqBlockingList_TotalBlockedAmountSar` | TField |  | Specifies the amount blocked in SAR currencyAs per the above example the value int his field will be 33750 |
| 50 | `SA.BLOCK.TOTAL.BLOCKED.AMOUNT.CURRENCY` | `SawatqBlockingList_TotalBlockedAmountCurrency` | TField |  | Specifies the amount blocked in source currency or currency other than SAR. As per the above example , the value in this field will be 1000 |
| 51 | `SA.BLOCK.BLOCKED` | `SawatqBlockingList_Blocked` |  |  |  |
| 52 | `SA.BLOCK.BLOCKED.ACCOUNT.NUMBER` | `SawatqBlockingList_BlockedAccountNumber` |  |  |  |
| 53 | `SA.BLOCK.BLOCKED.ACCOUNT.IBAN` | `SawatqBlockingList_BlockedAccountIban` |  |  |  |
| 54 | `SA.BLOCK.BLOCKED.INSTITUTION` | `SawatqBlockingList_BlockedInstitution` |  |  |  |
| 55 | `SA.BLOCK.BLOCKED.ACCOUNT.CURRENCY` | `SawatqBlockingList_BlockedAccountCurrency` |  |  |  |
| 56 | `SA.BLOCK.BLOCKED.IS.JOINT.ACCOUNT` | `SawatqBlockingList_BlockedIsJointAccount` |  |  |  |
| 57 | `SA.BLOCK.SOURCE.CURRENCY.AMOUNT` | `SawatqBlockingList_SourceCurrencyAmount` |  |  |  |
| 58 | `SA.BLOCK.BLOCKED.AMOUNT` | `SawatqBlockingList_BlockedAmount` |  |  |  |
| 59 | `SA.BLOCK.BLOCKED.ACCOUNT.EXCHANGE.RATE` | `SawatqBlockingList_BlockedAccountExchangeRate` |  |  |  |
| 60 | `SA.BLOCK.BLOCKED.ACCOUNT.DATE.AND.TIME` | `SawatqBlockingList_BlockedAccountDateAndTime` |  |  |  |
| 61 | `SA.BLOCK.BLOCKED.USER.TYPE` | `SawatqBlockingList_BlockedUserType` |  |  |  |
| 62 | `SA.BLOCK.BLOCKED.ACCOUNT.STATUS` | `SawatqBlockingList_BlockedAccountStatus` |  |  |  |
| 63 | `SA.BLOCK.BLOCKED.DEPOSIT.NUMBER` | `SawatqBlockingList_BlockedDepositNumber` |  |  |  |
| 64 | `SA.BLOCK.BLOCKED.DEPOSIT.CURRENCY` | `SawatqBlockingList_BlockedDepositCurrency` |  |  |  |
| 65 | `SA.BLOCK.BLOCKED.DEPOSIT.AMOUNT` | `SawatqBlockingList_BlockedDepositAmount` |  |  |  |
| 66 | `SA.BLOCK.BLOCKED.DEPOSIT.DATE.AND.TIME` | `SawatqBlockingList_BlockedDepositDateAndTime` |  |  |  |
| 67 | `SA.BLOCK.BLOCKED.DEPOSIT.STATUS` | `SawatqBlockingList_BlockedDepositStatus` |  |  |  |
| 68 | `SA.BLOCK.BLOCKED.NF.ACCOUNT.NUMBER` | `SawatqBlockingList_BlockedNfAccountNumber` |  |  |  |
| 69 | `SA.BLOCK.BLOCKED.NF.IBAN` | `SawatqBlockingList_BlockedNfIban` |  |  |  |
| 70 | `SA.BLOCK.BLOCKED.NF.INSTITUTION` | `SawatqBlockingList_BlockedNfInstitution` |  |  |  |
| 71 | `SA.BLOCK.BLOCKED.NF.IS.JOINT.ACCOUNT` | `SawatqBlockingList_BlockedNfIsJointAccount` |  |  |  |
| 72 | `SA.BLOCK.BLOCKED.NF.DATE.AND.TIME` | `SawatqBlockingList_BlockedNfDateAndTime` |  |  |  |
| 73 | `SA.BLOCK.BLOCKED.NF.USER.TYPE` | `SawatqBlockingList_BlockedNfUserType` |  |  |  |
| 74 | `SA.BLOCK.BLOCKED.NF.ACCOUNT.STATUS` | `SawatqBlockingList_BlockedNfAccountStatus` |  |  |  |
| 75 | `SA.BLOCK.BLOCKED.NF.DEPOSIT.NUMBER` | `SawatqBlockingList_BlockedNfDepositNumber` |  |  |  |
| 76 | `SA.BLOCK.NF.DEPOSIT.EXECUTION.DATE.TIME` | `SawatqBlockingList_NfDepositExecutionDateTime` |  |  |  |
| 77 | `SA.BLOCK.BLOCKED.NF.DEPOSIT.STATUS` | `SawatqBlockingList_BlockedNfDepositStatus` |  |  |  |
| 78 | `SA.BLOCK.LIFT.EXECUTION.DATE.AND.TIME` | `SawatqBlockingList_LiftExecutionDateAndTime` | TField |  |  |
| 79 | `SA.BLOCK.LIFT.BLOCK.TFR.TOT.AMT` | `SawatqBlockingList_LiftBlockTfrTotAmt` | TField |  |  |
| 80 | `SA.BLOCK.LIFT.BLOCK.TFR.TOT.BLOCK.AMT` | `SawatqBlockingList_LiftBlockTfrTotBlockAmt` | TField |  |  |
| 81 | `SA.BLOCK.TRANSFER.ACCOUNT.NUMBER` | `SawatqBlockingList_TransferAccountNumber` |  |  |  |
| 82 | `SA.BLOCK.TRANSFER.ACCOUNT.IBAN` | `SawatqBlockingList_TransferAccountIban` |  |  |  |
| 83 | `SA.BLOCK.TRANSFER.ACCOUNT.INSTITUTION` | `SawatqBlockingList_TransferAccountInstitution` |  |  |  |
| 84 | `SA.BLOCK.TRANSFER.SOURCE.AMOUNT` | `SawatqBlockingList_TransferSourceAmount` |  |  |  |
| 85 | `SA.BLOCK.TRANSFER.ACCOUNT.AMOUNT` | `SawatqBlockingList_TransferAccountAmount` |  |  |  |
| 86 | `SA.BLOCK.TFR.ACCT.IS.JOINT.ACCOUNT` | `SawatqBlockingList_TfrAcctIsJointAccount` |  |  |  |
| 87 | `SA.BLOCK.TRANSFERRED.AMOUNT` | `SawatqBlockingList_TransferredAmount` |  |  |  |
| 88 | `SA.BLOCK.TRANSFER.FX.RATE` | `SawatqBlockingList_TransferFxRate` |  |  |  |
| 89 | `SA.BLOCK.TRANSFER.TIME` | `SawatqBlockingList_TransferTime` |  |  |  |
| 90 | `SA.BLOCK.TRANSFER.REF.NUMBER` | `SawatqBlockingList_TransferRefNumber` |  |  |  |
| 91 | `SA.BLOCK.TRANSFER.STATUS` | `SawatqBlockingList_TransferStatus` |  |  |  |
| 92 | `SA.BLOCK.TRANSFER.ACCOUNT.USER.TYPE` | `SawatqBlockingList_TransferAccountUserType` |  |  |  |
| 93 | `SA.BLOCK.BLACKLISTED` | `SawatqBlockingList_Blacklisted` | TField |  | When value is Yes, the records are required to be picked up to be sent to FCM. |
| 94 | `SA.BLOCK.TRANSFER.INT.ACCT.REF` | `SawatqBlockingList_TransferIntAcctRef` | TField |  |  |
| 95 | `SA.BLOCK.TRANSFER.INT.ACCT.NO` | `SawatqBlockingList_TransferIntAcctNo` | TField |  |  |
| 96 | `SA.BLOCK.REPLY.CODE` | `SawatqBlockingList_ReplyCode` |  |  |  |
| 97 | `SA.BLOCK.REPLY.DESCRIPTION` | `SawatqBlockingList_ReplyDescription` |  |  |  |
| 98 | `SA.BLOCK.REVERSE.TARGET.AMOUNT` | `SawatqBlockingList_ReverseTargetAmount` | TField |  |  |
| 99 | `SA.BLOCK.EXCEPTION.HANDLED` | `SawatqBlockingList_ExceptionHandled` | TField |  | When the exception case is handled by the bank, this field will be marked as Yes |
| 100 | `SA.BLOCK.EXCEPTION.CODE` | `SawatqBlockingList_ExceptionCode` | TField |  | 01,02,03,04 EB.LOOKUP records are created. |
| 101 | `SA.BLOCK.EXCEPTION.DESCRIPTION` | `SawatqBlockingList_ExceptionDescription` | TField |  | The description of the error faced 01 - Deposit matured during the block period, the amount available in the internal account 02 - Lift with transfer - transferred to internal account 03- Lift - Refrerence number - no corresponding record found. 04- Account - closed /invalid - Unable to lift |
| 102 | `SA.BLOCK.EXCEPTION.DATE.AND.TIME` | `SawatqBlockingList_ExceptionDateAndTime` | TField |  | Date on which the exception is applied. |
| 103 | `SA.BLOCK.REQUEST.DATE.AND.TIME` | `SawatqBlockingList_RequestDateAndTime` |  |  |  |
| 104 | `SA.BLOCK.LOCAL.REF` | `SawatqBlockingList_LocalRef` |  |  |  |
| 105 | `SA.BLOCK.OVERRIDE` | `SawatqBlockingList_Override` |  |  |  |
| 106 | `SA.BLOCK.RESERVED.1` | `SawatqBlockingList_Reserved1` | TField |  | Reserved For Future Use |
| 107 | `SA.BLOCK.RESERVED.2` | `SawatqBlockingList_Reserved2` | TField |  | Reserved For Future Use |
| 108 | `SA.BLOCK.RESERVED.3` | `SawatqBlockingList_Reserved3` | TField |  | Reserved For Future Use |
| 109 | `SA.BLOCK.RESERVED.4` | `SawatqBlockingList_Reserved4` | TField |  | Reserved For Future Use |
| 110 | `SA.BLOCK.RESERVED.5` | `SawatqBlockingList_Reserved5` | TField |  | Reserved For Future Use |
| 111 | `SA.BLOCK.RESERVED.6` | `SawatqBlockingList_Reserved6` | TField |  | Reserved For Future Use |
| 112 | `SA.BLOCK.RESERVED.7` | `SawatqBlockingList_Reserved7` | TField |  | Reserved For Future Use |
| 113 | `SA.BLOCK.RESERVED.8` | `SawatqBlockingList_Reserved8` | TField |  | Reserved For Future Use |
| 114 | `SA.BLOCK.RESERVED.9` | `SawatqBlockingList_Reserved9` | TField |  | Reserved For Future Use |
| 115 | `SA.BLOCK.RESERVED.10` | `SawatqBlockingList_Reserved10` | TField |  | Reserved For Future Use |
| 116 | `SA.BLOCK.RECORD.STATUS` | `SawatqBlockingList_RecordStatus` | String |  |  |
| 117 | `SA.BLOCK.CURR.NO` | `SawatqBlockingList_CurrNo` | String |  |  |
| 118 | `SA.BLOCK.INPUTTER` | `SawatqBlockingList_Inputter` |  |  |  |
| 119 | `SA.BLOCK.DATE.TIME` | `SawatqBlockingList_DateTime` |  |  |  |
| 120 | `SA.BLOCK.AUTHORISER` | `SawatqBlockingList_Authoriser` | String |  |  |
| 121 | `SA.BLOCK.CO.CODE` | `SawatqBlockingList_CoCode` | String |  |  |
| 122 | `SA.BLOCK.DEPT.CODE` | `SawatqBlockingList_DeptCode` | String |  |  |
| 123 | `SA.BLOCK.AUDITOR.CODE` | `SawatqBlockingList_AuditorCode` | String |  |  |
| 124 | `SA.BLOCK.AUDIT.DATE.TIME` | `SawatqBlockingList_AuditDateTime` | String |  |  |
