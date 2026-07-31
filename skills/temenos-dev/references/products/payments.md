# Payments & Funds Transfer — Reference

> Generated 2026-06-20T03:39:43.046735+00:00 from 256 JARs. Re-run `aggregate.py` to refresh.

---

## Lifecycle Hooks

*No lifecycle hooks detected in this domain.*

---

## Validation & Authorization Hooks

*No validation or authorization hooks detected in this domain.*

---

## Public APIs

| Class | JAR | Method | Returns | Description |
|-------|-----|--------|---------|-------------|
| `InwardEntry` | `FT_ClearingHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to modify the local reference fields in the clearingRecord parameter. |
| `InwardEntry` | `FT_ClearingHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to modify the local reference fields in the clearingRecord parameter. |
| `InwardEntry` | `FT_ClearingHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to modify the local reference fields in the clearingRecord parameter. |
| `InwardEntry` | `FT_ClearingHook.jar` | `modifyLocalReferenceValues` | `void` | This interface enables the implementer to modify the local reference fields in the clearingRecord parameter. |
| `InwardEntry` | `FT_ClearingHook.jar` | `validateEntry` | `com.temenos.t24.api.complex.ft.clearinghook.ValidationResponse` | This interface enables the implementer to modify the local reference fields in the clearingRecord parameter. |
| `FundsTransfer` | `FT_ContractHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the values which will be used to update the FT.TAPE.REFERENCE record by the FT.TAPES.RUN. |
| `FundsTransfer` | `FT_ContractHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the values which will be used to update the FT.TAPE.REFERENCE record by the FT.TAPES.RUN. |
| `FundsTransfer` | `FT_ContractHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the values which will be used to update the FT.TAPE.REFERENCE record by the FT.TAPES.RUN. |
| `FundsTransfer` | `FT_ContractHook.jar` | `updateFundsTransferTapeReference` | `com.temenos.t24.api.complex.ft.contracthook.FtTapeReferenceFields` | This interface enables the implementer to return the values which will be used to update the FT.TAPE.REFERENCE record by the FT.TAPES.RUN. |
| `BalanceCheckApiHook` | `PP_BalanceCheckApiHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getRequestType instead |
| `BalanceCheckApiHook` | `PP_BalanceCheckApiHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getRequestType instead |
| `BalanceCheckApiHook` | `PP_BalanceCheckApiHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getRequestType instead |
| `BalanceCheckApiHook` | `PP_BalanceCheckApiHook.jar` | `recyclerLookup` | `void` | Deprecated.  use PaymentLifecycle.getRequestType instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getCreditAccount` | `com.temenos.t24.api.complex.pp.componentapihook.Account` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getDebitAccount` | `com.temenos.t24.api.complex.pp.componentapihook.DebitAccount` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `validateCreditParty` | `com.temenos.t24.api.complex.pp.componentapihook.Response` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `validateDebitParty` | `com.temenos.t24.api.complex.pp.componentapihook.Response` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `getCodewordFlag` | `com.temenos.api.TBoolean` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `ComponentApiHook` | `PP_ComponentApiHook.jar` | `setCalculatedDate` | `com.temenos.t24.api.complex.pp.componentapihook.CalculatedDates` | Deprecated.  use PaymentLifecycle.updateProcessSequence instead |
| `DataAccess` | `PP_DataAccessApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `PP_DataAccessApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `PP_DataAccessApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `PP_DataAccessApi.jar` | `getPaymentRecord` | `com.temenos.t24.api.records.portransaction.PorTransactionRecord` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `PP_DataAccessApi.jar` | `getActiveId` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `FeeDeterminationHook` | `PP_FeeDeterminationHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getChargeResponse instead |
| `FeeDeterminationHook` | `PP_FeeDeterminationHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getChargeResponse instead |
| `FeeDeterminationHook` | `PP_FeeDeterminationHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getChargeResponse instead |
| `FeeDeterminationHook` | `PP_FeeDeterminationHook.jar` | `getChargeAmount` | `com.temenos.api.TNumber` | Deprecated.  use PaymentLifecycle.getChargeResponse instead |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `validateSwiftMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `ackNackMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `messageForward` | `void` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `debulkMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.FileInformation` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `validateBacsMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `validateAchMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `validateChequeClearingMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `validateClearingMessage` | `com.temenos.t24.api.complex.pp.messageacceptanceparamhook.MessageResponse` | This interface enables the implementer to validate the ACH messages. |
| `MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | `ackClearingMessage` | `void` | This interface enables the implementer to validate the ACH messages. |
| `Message` | `PP_MessageHook.jar` | `getVersion` | `java.lang.String` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `updateInformationLine` | `void` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `updateFieldValue` | `void` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `updatePaymentObject` | `void` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `Message` | `PP_MessageHook.jar` | `updateMessageStatus` | `com.temenos.t24.api.complex.pp.messagehook.ValidationResponse` | This interface enables the developer to update a field value for non-xml message to be mapped to a payment. |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getVersion` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `updateRequestToExternalCoreSystem` | `void` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getTransactionCode` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.TransactionCode` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `validatePaymentForClearing` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.ValidationResponse` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getAccountLocation` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountLocation` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getRoutingProductId` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getExternalRequestFieldValue` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `updateProduct` | `void` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `postRequestToExternalSystem` | `com.temenos.api.TBoolean` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `postUpdateRequest` | `void` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getChargeResponse` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.ChargeResponse` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getFileName` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getCreditAccount` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Account` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getDebitAccount` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.DebitAccount` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `validateCreditParty` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `validateDebitParty` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getPaymentDate` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.PaymentDate` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `updateProcessSequence` | `void` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `skipMessage` | `com.temenos.api.TBoolean` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `validatePayment` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Response` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getSource` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getSwiftSource` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getStatementNarrative` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getRequestType` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getExternalRequestField` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.Field` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getGroupingCriteria` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.GroupingCriteria` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getCustomGroupingValues` | `java.util.List<java.lang.String>` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getBulkPaymentReference` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `updateOutgoingPaymentRecords` | `void` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getSwiftOriginatingSource` | `java.lang.String` |  |
| `PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | `getPostingRestriction` | `com.temenos.t24.api.complex.pp.paymentlifecyclehook.AccountRestrictions` |  |
| `PostingSchemeAPIHook` | `PP_PostingSchemeAPIHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getStatementNarrative instead |
| `PostingSchemeAPIHook` | `PP_PostingSchemeAPIHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getStatementNarrative instead |
| `PostingSchemeAPIHook` | `PP_PostingSchemeAPIHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getStatementNarrative instead |
| `PostingSchemeAPIHook` | `PP_PostingSchemeAPIHook.jar` | `getTextTokenValue` | `java.lang.String` | Deprecated.  use PaymentLifecycle.getStatementNarrative instead |
| `Swap` | `SW_SwapHook.jar` | `getVersion` | `java.lang.String` | This interface allows the implementer to calculate the forward rate used to calculate the cash flow amount for the swap Net Present Value details enquiry. |
| `Swap` | `SW_SwapHook.jar` | `getBuildDate` | `java.lang.String` | This interface allows the implementer to calculate the forward rate used to calculate the cash flow amount for the swap Net Present Value details enquiry. |
| `Swap` | `SW_SwapHook.jar` | `getComponentVersion` | `java.lang.String` | This interface allows the implementer to calculate the forward rate used to calculate the cash flow amount for the swap Net Present Value details enquiry. |
| `Swap` | `SW_SwapHook.jar` | `getForwardRate` | `com.temenos.api.TNumber` | This interface allows the implementer to calculate the forward rate used to calculate the cash flow amount for the swap Net Present Value details enquiry. |

---

## Enquiry Routines

*No enquiry routines detected in this domain.*

---

## Record Models

*No record models detected in this domain.*

---

## JAR Inventory

| JAR | Class Count | Component Types Present |
|-----|-------------|------------------------|
| `FS_Accounting.jar` | 5 | unknown |
| `FS_AccountingEquivalence.jar` | 17 | unknown |
| `FS_AccountingSchema.jar` | 11 | unknown |
| `FS_Address.jar` | 13 | unknown |
| `FS_AgentPaymentStaticData.jar` | 2 | unknown |
| `FS_AgentStaticData.jar` | 17 | unknown |
| `FS_ApplicationFramework.jar` | 69 | unknown |
| `FS_ApplicationParameters.jar` | 5 | unknown |
| `FS_BankAccount.jar` | 5 | unknown |
| `FS_CallDeposit.jar` | 5 | unknown |
| `FS_Capstock.jar` | 8 | unknown |
| `FS_CashHandling.jar` | 2 | unknown |
| `FS_Charge.jar` | 5 | unknown |
| `FS_ChargeAndFeeConfiguration.jar` | 2 | unknown |
| `FS_ChargesFees.jar` | 79 | unknown |
| `FS_ChartOfAccount.jar` | 5 | unknown |
| `FS_CommissionManagement.jar` | 35 | unknown |
| `FS_Common.jar` | 211 | unknown |
| `FS_CommonCustom.jar` | 196 | unknown |
| `FS_Contacts.jar` | 2 | unknown |
| `FS_Contract.jar` | 2 | unknown |
| `FS_Controls.jar` | 28 | unknown |
| `FS_CorporateAction.jar` | 8 | unknown |
| `FS_CorporateActionEquivalence.jar` | 2 | unknown |
| `FS_Correspondent.jar` | 5 | unknown |
| `FS_DatabaseClientDetails.jar` | 2 | unknown |
| `FS_Dealing.jar` | 8 | unknown |
| `FS_DebitCredit.jar` | 11 | unknown |
| `FS_Deposit.jar` | 8 | unknown |
| `FS_Distribution.jar` | 4 | unknown |
| `FS_DistributorPortal.jar` | 2 | unknown |
| `FS_Dividend.jar` | 13 | unknown |
| `FS_EqualisationChartOfAccount.jar` | 2 | unknown |
| `FS_Equivalence.jar` | 52 | unknown |
| `FS_ExchangeConfiguration.jar` | 2 | unknown |
| `FS_ExchangeRates.jar` | 16 | unknown |
| `FS_Fee.jar` | 11 | unknown |
| `FS_Forex.jar` | 8 | unknown |
| `FS_Fund.jar` | 2 | unknown |
| `FS_FundCalendar.jar` | 5 | unknown |
| `FS_FundDealing.jar` | 11 | unknown |
| `FS_FundEquivalence.jar` | 2 | unknown |
| `FS_FundLegalEntity.jar` | 8 | unknown |
| `FS_FundMaster.jar` | 28 | unknown |
| `FS_FundMasterAccounting.jar` | 8 | unknown |
| `FS_FundMasterException.jar` | 5 | unknown |
| `FS_FundMasterValuation.jar` | 2 | unknown |
| `FS_FundPromoter.jar` | 5 | unknown |
| `FS_FundShareClassStaticData.jar` | 11 | unknown |
| `FS_FundStaticData.jar` | 23 | unknown |
| `FS_FutureMaster.jar` | 5 | unknown |
| `FS_FutureTransaction.jar` | 11 | unknown |
| `FS_GlobalAccounting.jar` | 498 | unknown |
| `FS_GlobalAccountingLookup.jar` | 2 | unknown |
| `FS_GlobalAccountingTransactions.jar` | 81 | unknown |
| `FS_GlobalInvestor.jar` | 421 | unknown |
| `FS_GlobalInvestorLookup.jar` | 2 | unknown |
| `FS_GlobalInvestorTransactions.jar` | 62 | unknown |
| `FS_Income.jar` | 11 | unknown |
| `FS_IncomeCorporateAction.jar` | 19 | unknown |
| `FS_InterestRate.jar` | 2 | unknown |
| `FS_InvestmentRestrictions.jar` | 11 | unknown |
| `FS_InvestorAccountStaticData.jar` | 14 | unknown |
| `FS_InvestorCompliance.jar` | 2 | unknown |
| `FS_InvestorComplianceDocument.jar` | 2 | unknown |
| `FS_InvestorStaticData.jar` | 5 | unknown |
| `FS_LimitedPartnership.jar` | 54 | unknown |
| `FS_LimitedPartnershipConfiguration.jar` | 38 | unknown |
| `FS_LimitedPartnershipLog.jar` | 2 | unknown |
| `FS_LimitedPartnershipProcess.jar` | 25 | unknown |
| `FS_LimitedPartnershipStaticData.jar` | 14 | unknown |
| `FS_Loan.jar` | 8 | unknown |
| `FS_ManagerParameters.jar` | 8 | unknown |
| `FS_MBS.jar` | 2 | unknown |
| `FS_Modules.jar` | 2 | unknown |
| `FS_OptionMaster.jar` | 5 | unknown |
| `FS_OptionTransaction.jar` | 8 | unknown |
| `FS_Payment.jar` | 4 | unknown |
| `FS_Position.jar` | 2 | unknown |
| `FS_Price.jar` | 2 | unknown |
| `FS_PricesRates.jar` | 19 | unknown |
| `FS_PrivateEquity.jar` | 4 | unknown |
| `FS_Processing.jar` | 14 | unknown |
| `FS_ProcessingValuation.jar` | 4 | unknown |
| `FS_Profile.jar` | 2 | unknown |
| `FS_Receipt.jar` | 7 | unknown |
| `FS_Regulatory.jar` | 5 | unknown |
| `FS_Reporting.jar` | 2 | unknown |
| `FS_Reports.jar` | 80 | unknown |
| `FS_Scheduler.jar` | 5 | unknown |
| `FS_Securities.jar` | 43 | unknown |
| `FS_SecurityEquivalence.jar` | 2 | unknown |
| `FS_SecurityMaster.jar` | 5 | unknown |
| `FS_SecurityMasterConfiguration.jar` | 8 | unknown |
| `FS_SecurityMasterMarketData.jar` | 5 | unknown |
| `FS_SecurityMasterRates.jar` | 2 | unknown |
| `FS_SecurityMasterSchedule.jar` | 2 | unknown |
| `FS_StaticData.jar` | 70 | unknown |
| `FS_StaticEquivalence.jar` | 8 | unknown |
| `FS_StaticMasterConfiguration.jar` | 5 | unknown |
| `FS_StockTransaction.jar` | 11 | unknown |
| `FS_SystemConfiguration.jar` | 11 | unknown |
| `FS_Tax.jar` | 8 | unknown |
| `FS_ThirdParties.jar` | 13 | unknown |
| `FS_ThirdPartiesConfiguration.jar` | 2 | unknown |
| `FS_ThirdPartiesException.jar` | 2 | unknown |
| `FS_ThirdPartiesIdentifiers.jar` | 2 | unknown |
| `FS_ThirdPartyEquivalence.jar` | 5 | unknown |
| `FS_Tools.jar` | 2 | unknown |
| `FS_TransactionConfiguration.jar` | 5 | unknown |
| `FS_TransactionEntry.jar` | 12 | unknown |
| `FS_TransactionEquivalence.jar` | 2 | unknown |
| `FS_TransactionProcess.jar` | 40 | unknown |
| `FS_UserAgent.jar` | 2 | unknown |
| `FS_UsersManagement.jar` | 4 | unknown |
| `FS_Valuation.jar` | 23 | unknown |
| `FS_WEM.jar` | 89 | unknown |
| `FS_WemChecklistConfiguration.jar` | 4 | unknown |
| `FS_WemChecklistProcessing.jar` | 2 | unknown |
| `FS_WemConfiguration.jar` | 3 | unknown |
| `FS_WEMEngine.jar` | 48 | unknown |
| `FS_WemExceptionConfiguration.jar` | 2 | unknown |
| `FS_WemProcess.jar` | 7 | unknown |
| `FS_WemSetupConfiguration.jar` | 3 | unknown |
| `FS_WemStatic.jar` | 2 | unknown |
| `FT_AdhocChargeRequests.jar` | 12 | unknown |
| `FT_BulkProcessing.jar` | 57 | unknown |
| `FT_Channels.jar` | 5 | unknown |
| `FT_Clearing.jar` | 101 | unknown |
| `FT_ClearingHook.jar` | 2 | public-api, unknown |
| `FT_Config.jar` | 14 | unknown |
| `FT_Contract.jar` | 116 | unknown |
| `FT_ContractHook.jar` | 3 | public-api, unknown |
| `FT_Delivery.jar` | 32 | unknown |
| `FT_FeeRequests.jar` | 9 | unknown |
| `FT_LocalClearing.jar` | 35 | unknown |
| `FT_ModelBank.jar` | 22 | unknown |
| `FT_PaymentEnhancementService.jar` | 6 | unknown |
| `PP_AccountandCustomerInterfaceService.jar` | 13 | unknown |
| `PP_AccountCashPositionService.jar` | 10 | unknown |
| `PP_ArchivingService.jar` | 55 | unknown |
| `PP_AutoformService.jar` | 18 | unknown |
| `PP_AutomatedRepairToolService.jar` | 53 | unknown |
| `PP_BACSMessageMappingService.jar` | 9 | unknown |
| `PP_BalanceCheckApiHook.jar` | 3 | public-api, unknown |
| `PP_BalanceCheckService.jar` | 60 | unknown |
| `PP_BalanceInterfaceService.jar` | 24 | unknown |
| `PP_BankCodeService.jar` | 52 | unknown |
| `PP_BankConditionsService.jar` | 40 | unknown |
| `PP_BatchServerService.jar` | 34 | unknown |
| `PP_BICUploadService.jar` | 54 | unknown |
| `PP_BillingService.jar` | 52 | unknown |
| `PP_CamtAcctStmt.jar` | 4 | unknown |
| `PP_ChequeService.jar` | 33 | unknown |
| `PP_ClaimsService.jar` | 38 | unknown |
| `PP_ClearingFrameworkService.jar` | 31 | unknown |
| `PP_ClearingStatusReport.jar` | 27 | unknown |
| `PP_ClientConditionsService.jar` | 48 | unknown |
| `PP_ComponentApiHook.jar` | 8 | public-api, unknown |
| `PP_ConfirmationsService.jar` | 65 | unknown |
| `PP_CountryIBANStructureService.jar` | 16 | unknown |
| `PP_CoverDeterminationService.jar` | 10 | unknown |
| `PP_CreditPartyDeterminationService.jar` | 48 | unknown |
| `PP_CustomerPaymentStatusReport.jar` | 37 | unknown |
| `PP_DataAccessApi.jar` | 4 | public-api, unknown |
| `PP_DateDeterminationService.jar` | 97 | unknown |
| `PP_DebitAuthorityService.jar` | 69 | unknown |
| `PP_DebitPartyDeterminationService.jar` | 64 | unknown |
| `PP_DirectDebitChequeService.jar` | 56 | unknown |
| `PP_DirectDebitGUI.jar` | 1 | unknown |
| `PP_DirectionDeterminationService.jar` | 14 | unknown |
| `PP_DuplicateCheckService.jar` | 36 | unknown |
| `PP_EmailSMSService.jar` | 11 | unknown |
| `PP_FeeDeterminationGUI.jar` | 1 | unknown |
| `PP_FeeDeterminationHook.jar` | 3 | public-api, unknown |
| `PP_FeeDeterminationService.jar` | 140 | unknown |
| `PP_FeeTypesService.jar` | 50 | unknown |
| `PP_FilteringService.jar` | 62 | unknown |
| `PP_FutureDueDateService.jar` | 6 | unknown |
| `PP_FXService.jar` | 39 | unknown |
| `PP_GUIFrameworkService.jar` | 19 | unknown |
| `PP_HKCLGMessageMappingService.jar` | 9 | unknown |
| `PP_InboundCodeWordService.jar` | 71 | unknown |
| `PP_InquiryGUI.jar` | 255 | unknown |
| `PP_InsightService.jar` | 68 | unknown |
| `PP_InwardCreditTransferInitiationService.jar` | 25 | unknown |
| `PP_InwardFramework.jar` | 17 | unknown |
| `PP_InwardMappingFramework.jar` | 224 | unknown |
| `PP_LocalClearingBACSService.jar` | 28 | unknown |
| `PP_LocalClearingDebulkingService.jar` | 7 | unknown |
| `PP_LocalClearingGUI.jar` | 1 | unknown |
| `PP_LocalClearingHKCLGService.jar` | 22 | unknown |
| `PP_LocalClearingMsgMapService.jar` | 14 | unknown |
| `PP_LocalClearingService.jar` | 219 | unknown |
| `PP_LocalClearingUSACH.jar` | 20 | unknown |
| `PP_LoroNostroAccountService.jar` | 16 | unknown |
| `PP_MessageAcceptanceDASService.jar` | 1 | unknown |
| `PP_MessageAcceptanceParamHook.jar` | 11 | public-api, unknown |
| `PP_MessageAcceptanceService.jar` | 142 | unknown |
| `PP_MessageHook.jar` | 6 | public-api, unknown |
| `PP_MessageMappingService.jar` | 43 | unknown |
| `PP_ModelBank.jar` | 2 | unknown |
| `PP_NorkomAMLService.jar` | 10 | unknown |
| `PP_OrderEntryGUI.jar` | 87 | unknown |
| `PP_OrderEntryRepairService.jar` | 87 | unknown |
| `PP_OutboundCodeWordService.jar` | 52 | unknown |
| `PP_OutwardInterfaceService.jar` | 76 | unknown |
| `PP_OutwardMappingFramework.jar` | 165 | unknown |
| `PP_OwnAccountDeterminationService.jar` | 10 | unknown |
| `PP_PaymentFinalisationService.jar` | 48 | unknown |
| `PP_PaymentFrameworkService.jar` | 337 | unknown |
| `PP_PaymentGenerationService.jar` | 16 | unknown |
| `PP_PaymentInitialisationService.jar` | 7 | unknown |
| `PP_PaymentLifecycleHook.jar` | 32 | public-api, unknown |
| `PP_PaymentReturn.jar` | 11 | unknown |
| `PP_PaymentRouterService.jar` | 39 | unknown |
| `PP_PaymentSTPFlowService.jar` | 49 | unknown |
| `PP_PaymentWorkflowDASService.jar` | 113 | unknown |
| `PP_PaymentWorkflowGUI.jar` | 65 | unknown |
| `PP_PaymentWorkflowService.jar` | 90 | unknown |
| `PP_PostingSchemeAPIHook.jar` | 3 | public-api, unknown |
| `PP_PostingSchemeService.jar` | 139 | unknown |
| `PP_PrintService.jar` | 3 | unknown |
| `PP_ProductDeterminationService.jar` | 83 | unknown |
| `PP_ReversePostingService.jar` | 22 | unknown |
| `PP_RiskFilterService.jar` | 52 | unknown |
| `PP_RoutingAndSettlementDASService.jar` | 2 | unknown |
| `PP_RoutingAndSettlementService.jar` | 231 | unknown |
| `PP_RPSSCLService.jar` | 7 | unknown |
| `PP_SLADeterminationService.jar` | 17 | unknown |
| `PP_SODEODService.jar` | 78 | unknown |
| `PP_StandingOrderService.jar` | 27 | unknown |
| `PP_StaticDataGUI.jar` | 95 | unknown |
| `PP_STEP2Service.jar` | 15 | unknown |
| `PP_STePService.jar` | 10 | unknown |
| `PP_SwiftOutService.jar` | 188 | unknown |
| `PP_SwiftService.jar` | 40 | unknown |
| `PP_TARGET2Service.jar` | 21 | unknown |
| `PP_TemenosAMLService.jar` | 10 | unknown |
| `PP_TPSGUIFramework.jar` | 8 | unknown |
| `PP_TraFixService.jar` | 10 | unknown |
| `PP_TransactionReferenceGenerationService.jar` | 14 | unknown |
| `PP_TRIPService.jar` | 45 | unknown |
| `PP_USACHMessageMapping.jar` | 3 | unknown |
| `PP_WarehouseService.jar` | 19 | unknown |
| `PP_WeightAssignmentService.jar` | 16 | unknown |
| `SW_Config.jar` | 17 | unknown |
| `SW_Contract.jar` | 79 | unknown |
| `SW_Delivery.jar` | 13 | unknown |
| `SW_Foundation.jar` | 34 | unknown |
| `SW_Interest.jar` | 17 | unknown |
| `SW_PositionAndReval.jar` | 18 | unknown |
| `SW_Reports.jar` | 18 | unknown |
| `SW_Schedules.jar` | 52 | unknown |
| `SW_SwapDetailsService.jar` | 7 | unknown |
| `SW_SwapHook.jar` | 3 | public-api, unknown |
