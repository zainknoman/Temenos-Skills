# Accounts & Core Banking — Reference

> Generated 2026-06-20T03:39:43.046735+00:00 from 129 JARs. Re-run `aggregate.py` to refresh.

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
| `Account` | `AC_AccountApi.jar` | `getVersion` | `java.lang.String` |  |
| `Account` | `AC_AccountApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Account` | `AC_AccountApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Account` | `AC_AccountApi.jar` | `setAccountId` | `void` |  |
| `Account` | `AC_AccountApi.jar` | `getAccountId` | `java.lang.String` |  |
| `Account` | `AC_AccountApi.jar` | `getAvailableAmount` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `isValidAccountClassForSector` | `com.temenos.api.TBoolean` |  |
| `Account` | `AC_AccountApi.jar` | `getOpenAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getOpenActualBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getOpenClearedBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getAccountOverdueDate` | `java.util.List<com.temenos.t24.api.complex.ac.accountapi.Overdue>` |  |
| `Account` | `AC_AccountApi.jar` | `getCapitalisationDate` | `com.temenos.api.TDate` |  |
| `Account` | `AC_AccountApi.jar` | `getStatementNarrative` | `java.lang.String` |  |
| `Account` | `AC_AccountApi.jar` | `isValidAccountId` | `com.temenos.api.TBoolean` |  |
| `Account` | `AC_AccountApi.jar` | `isValidInternalAccount` | `com.temenos.api.TBoolean` |  |
| `Account` | `AC_AccountApi.jar` | `getTurnoverCredit` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getTurnoverDebit` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getBalance` | `com.temenos.t24.api.complex.ac.accountapi.Amount` |  |
| `Account` | `AC_AccountApi.jar` | `getEntries` | `java.util.List<java.lang.String>` |  |
| `Account` | `AC_AccountApi.jar` | `isValidNostroAccount` | `com.temenos.api.TBoolean` |  |
| `Account` | `AC_AccountApi.jar` | `isValidNostroAccount` | `com.temenos.api.TBoolean` |  |
| `Account` | `AC_AccountApi.jar` | `getNostroAccount` | `com.temenos.t24.api.complex.ac.accountapi.NostroAccount` |  |
| `Account` | `AC_AccountApi.jar` | `getNostroAccountForTransactionType` | `com.temenos.t24.api.complex.ac.accountapi.NostroAccount` |  |
| `Account` | `AC_AccountApi.jar` | `lockContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` |  |
| `Account` | `AC_AccountApi.jar` | `getContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` |  |
| `Account` | `AC_AccountApi.jar` | `getContractBalancesRecord` | `com.temenos.t24.api.records.ebcontractbalances.EbContractBalancesRecord` |  |
| `Account` | `AC_AccountApi.jar` | `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` |  |
| `Account` | `AC_AccountApi.jar` | `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` |  |
| `Account` | `AC_AccountApi.jar` | `getAvailableBalance` | `com.temenos.t24.api.complex.ac.accountapi.Balance` |  |
| `AccountingEntry` | `AC_AccountHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `raiseOverrides` | `java.util.List<java.lang.String>` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `exportEntries` | `void` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `setAccountId` | `void` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `setAlternateAccountId` | `java.lang.String` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `getAlternateAccountId` | `java.lang.String` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `postUpdateRequest` | `void` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `generateStatementEntryEvent` | `void` | This Interface enables the implementer for export accounting entries to local developement. |
| `AccountingEntry` | `AC_AccountHook.jar` | `getAccountingEntryLocalFieldValues` | `void` | This Interface enables the implementer for export accounting entries to local developement. |
| `Account` | `AC_AccountServiceHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to get the payment currency for the account. |
| `Account` | `AC_AccountServiceHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to get the payment currency for the account. |
| `Account` | `AC_AccountServiceHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to get the payment currency for the account. |
| `Account` | `AC_AccountServiceHook.jar` | `getPaymentCurrency` | `java.lang.String` | This interface enables the implementer to get the payment currency for the account. |
| `Category` | `AC_CategoryApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Category` | `AC_CategoryApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Category` | `AC_CategoryApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Category` | `AC_CategoryApi.jar` | `setCategoryId` | `void` | Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Category` | `AC_CategoryApi.jar` | `getProfitAndLossEntryIds` | `java.util.List<java.lang.String>` | Default constructor. Create an empty Category.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `AC_ChargeApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `AC_ChargeApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `AC_ChargeApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `AC_ChargeApi.jar` | `setAccrualEndDate` | `void` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `AC_ChargeApi.jar` | `setAccrualAmount` | `void` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `ClearingService` | `AC_ClearingServiceHook.jar` | `getVersion` | `java.lang.String` | This interface is invoked from a service and enables the implementer to provide clearing entries which will be raised by the system. |
| `ClearingService` | `AC_ClearingServiceHook.jar` | `getBuildDate` | `java.lang.String` | This interface is invoked from a service and enables the implementer to provide clearing entries which will be raised by the system. |
| `ClearingService` | `AC_ClearingServiceHook.jar` | `getComponentVersion` | `java.lang.String` | This interface is invoked from a service and enables the implementer to provide clearing entries which will be raised by the system. |
| `ClearingService` | `AC_ClearingServiceHook.jar` | `bookEntries` | `void` | This interface is invoked from a service and enables the implementer to provide clearing entries which will be raised by the system. |
| `StandingOrder` | `AC_ContractHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to check the status of a Funds Transfer generated by a standing order during batch processing. |
| `StandingOrder` | `AC_ContractHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to check the status of a Funds Transfer generated by a standing order during batch processing. |
| `StandingOrder` | `AC_ContractHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to check the status of a Funds Transfer generated by a standing order during batch processing. |
| `StandingOrder` | `AC_ContractHook.jar` | `checkStandingOrderFundsTransfer` | `void` | This Interface enables the implementer to check the status of a Funds Transfer generated by a standing order during batch processing. |
| `StandingOrder` | `AC_ContractHook.jar` | `modifyPaymentOrderRecord` | `com.temenos.t24.api.records.paymentorder.PaymentOrderRecord` | This Interface enables the implementer to check the status of a Funds Transfer generated by a standing order during batch processing. |
| `Statement` | `AC_StatementHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `printStatement` | `void` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `printAccountStatement` | `void` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `formatStatement` | `void` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `modifyDataRecord` | `java.util.List<com.temenos.t24.api.complex.ac.statementhook.ModifiedData>` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `modifyHandOffRecord` | `java.util.List<com.temenos.t24.api.complex.ac.statementhook.ModifiedHandoffData>` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `getExternalSepaId` | `java.lang.String` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Statement` | `AC_StatementHook.jar` | `getNarrativeText` | `java.util.List<java.lang.String>` | This interface enables the implementer to do special format on statements, e.g. for NOSTRO statements might containg less transaction details than customer account, or HVT accounts with less details etc. |
| `Archive` | `EB_ArchiveHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getDateComparator` | `java.lang.String` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getSkipDecision` | `java.lang.String` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getArchiveFilter` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveFilter` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `archiveRelatedRecords` | `com.temenos.api.TNumber` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `loadArchiveFiles` | `void` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `selectArchiveRecords` | `void` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `processArchiveRecords` | `void` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getSelectedRecords` | `com.temenos.t24.api.complex.eb.archivehook.ArchiveSelect` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `Archive` | `EB_ArchiveHook.jar` | `getRelatedFiles` | `void` | This interface enables the implementer to archive records from local applications related to the supplied contract returning the number of records that have been archived. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getRecord` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getRecord` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getRecord` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getHistoryRecord` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getConcatValues` | `java.util.List<java.lang.String>` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `selectRecords` | `java.util.List<java.lang.String>` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `selectRecords` | `java.util.List<java.lang.String>` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `updateLocalfields` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getRequestResponse` | `com.temenos.t24.api.records.ofsrequestdetail.OfsRequestDetailRecord` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getFieldValue` | `com.temenos.t24.api.complex.eb.dataaccessapi.FieldValue` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `setFieldValue` | `com.temenos.api.TStructure` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataAccess` | `EB_DataAccessApi.jar` | `getCurrentDirectory` | `java.lang.String` | Default constructor. Create an empty DataAccess.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getVersion` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getSourceFileName` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getCompanyCode` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `validateFile` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `validateSourceData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getHeader` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getHeaderData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getTrailerData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getTrailer` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `convertFieldData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `updateFieldData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `processOutwardTransactionData` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `processInwardTransactionResponse` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `performCustomOperations` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `modifyOutboundRecord` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `modifyInboundMessage` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `updateOutboundData` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getIds` | `java.util.List<java.lang.String>` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `modifyData` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getTransactionId` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `getTargetFileName` | `java.lang.String` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `publishMessage` | `void` |  |
| `DataFormattingEngine` | `EB_DataFormattingEngineHook.jar` | `updateRecord` | `void` |  |
| `DataMapper` | `EB_DataMappingHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to convert the given value and return the converted value while mapping data from one record to another. |
| `DataMapper` | `EB_DataMappingHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to convert the given value and return the converted value while mapping data from one record to another. |
| `DataMapper` | `EB_DataMappingHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to convert the given value and return the converted value while mapping data from one record to another. |
| `DataMapper` | `EB_DataMappingHook.jar` | `convertFieldValue` | `java.lang.String` | This interface enables the implementer to convert the given value and return the converted value while mapping data from one record to another. |
| `Date` | `EB_DateApi.jar` | `getVersion` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getDayType` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getDayType` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `addWorkingDays` | `com.temenos.api.TDate` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `addWorkingDays` | `com.temenos.api.TDate` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getDates` | `com.temenos.t24.api.records.dates.DatesRecord` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `addFrequency` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `addFrequency` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `minusFrequency` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getWorkingDayDifference` | `com.temenos.api.TNumber` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getWorkingDayDifference` | `com.temenos.api.TNumber` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `gregorianToJulian` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `julianToGregorian` | `com.temenos.api.TDate` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getRecurrenceText` | `java.lang.String` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getMonthDifference` | `com.temenos.api.TNumber` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getHolidaySchedules` | `java.util.List<com.temenos.t24.api.complex.eb.dateapi.HolidaySchedule>` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getBranchHolidaySchedules` | `java.util.List<com.temenos.t24.api.complex.eb.dateapi.HolidaySchedule>` | Create a new Date using a specific context.. |
| `Date` | `EB_DateApi.jar` | `getSystemDate` | `com.temenos.api.TDate` | Create a new Date using a specific context.. |
| `Date` | `EB_DateHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the next frequency in the cycle for the given T24 frequency. |
| `Date` | `EB_DateHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the next frequency in the cycle for the given T24 frequency. |
| `Date` | `EB_DateHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the next frequency in the cycle for the given T24 frequency. |
| `Date` | `EB_DateHook.jar` | `getNextFrequency` | `java.lang.String` | This interface enables the implementer to return the next frequency in the cycle for the given T24 frequency. |
| `Encryption` | `EB_EncryptionHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `encryptFieldData` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `decryptFieldData` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `maskFieldData` | `com.temenos.api.TBoolean` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `decryptEnquiryFieldData` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Encryption` | `EB_EncryptionHook.jar` | `decryptEnrichmentFieldData` | `java.lang.String` | This interface enables the implementer to decrypt or modify sensitive data for display in an enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setFilterCriteria` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setValue` | `java.lang.String` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setValues` | `java.util.List<java.lang.String>` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setRecord` | `void` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setIds` | `java.util.List<java.lang.String>` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `setDropdownFilterCriteria` | `java.util.List<com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria>` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `Enquiry` | `EB_EnquiryHook.jar` | `getAttributeClass` | `java.lang.String` | This interface enables the implementer to return the attribute class while processing enquiry. |
| `MessageLifecycle` | `EB_MessageHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to perform their own processing after processing the incoming message. |
| `MessageLifecycle` | `EB_MessageHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to perform their own processing after processing the incoming message. |
| `MessageLifecycle` | `EB_MessageHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to perform their own processing after processing the incoming message. |
| `MessageLifecycle` | `EB_MessageHook.jar` | `preProcess` | `void` | This interface enables the implementer to perform their own processing after processing the incoming message. |
| `MessageLifecycle` | `EB_MessageHook.jar` | `postProcess` | `void` | This interface enables the implementer to perform their own processing after processing the incoming message. |
| `Record` | `EB_RecordApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Record.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Record` | `EB_RecordApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Record.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Record` | `EB_RecordApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Record.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Record` | `EB_RecordApi.jar` | `getGroupName` | `java.lang.String` | Default constructor. Create an empty Record.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Security` | `EB_SecurityHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `getAttributeValue` | `java.lang.String` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `getAttributeValuePair` | `java.util.List<com.temenos.t24.api.complex.eb.securityhook.AttributeValuePair>` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `isDataAccessRestricted` | `com.temenos.api.TBoolean` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `Security` | `EB_SecurityHook.jar` | `validateSignOn` | `com.temenos.t24.api.complex.eb.securityhook.SignOnResponse` | This interface enables the implementer to return a specified attribute value to be used for external security processing. |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getVersion` | `java.lang.String` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `initialise` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getTableName` | `java.lang.String` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getTableCriteria` | `com.temenos.t24.api.complex.eb.servicehook.TableCriteria` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getIds` | `java.util.List<java.lang.String>` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `process` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `inputRecord` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `processSingleThreaded` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `postUpdateRequest` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `updateRecord` | `void` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getServiceControlDetail` | `com.temenos.t24.api.complex.eb.servicehook.ServiceControl` |  |
| `ServiceLifecycle` | `EB_ServiceHook.jar` | `getSwiftRequests` | `java.util.List<com.temenos.t24.api.complex.eb.servicehook.SwiftRequest>` |  |
| `Session` | `EB_SessionApi.jar` | `getVersion` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getBuildDate` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getComponentVersion` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `listCurrentVariables` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.NameValuePair>` |  |
| `Session` | `EB_SessionApi.jar` | `getCurrentVariable` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `setCurrentVariable` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `deleteCurrentVariable` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `getCompanyId` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getCompanyRecord` | `com.temenos.t24.api.records.company.CompanyRecord` |  |
| `Session` | `EB_SessionApi.jar` | `getLocalCountry` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getLocalCurrency` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getUserId` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getUserRecord` | `com.temenos.t24.api.records.user.UserRecord` |  |
| `Session` | `EB_SessionApi.jar` | `getUserLanguage` | `com.temenos.api.TNumber` |  |
| `Session` | `EB_SessionApi.jar` | `getMainMenu` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getOnlineStatus` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `isService` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `isProductInstalled` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `getUserDispoOfficer` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getUserDispoRights` | `java.util.List<java.lang.String>` |  |
| `Session` | `EB_SessionApi.jar` | `getUserOverrideClass` | `java.util.List<java.lang.String>` |  |
| `Session` | `EB_SessionApi.jar` | `getUserRoles` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.UserRole>` |  |
| `Session` | `EB_SessionApi.jar` | `publishMessage` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `publishMessage` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `getSessionNumber` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getSourceId` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `printLine` | `void` |  |
| `Session` | `EB_SessionApi.jar` | `setNextVersion` | `void` |  |
| `Session` | `EB_SessionApi.jar` | `setNextVersion` | `void` |  |
| `Session` | `EB_SessionApi.jar` | `getCachedRecord` | `com.temenos.api.TStructure` |  |
| `Session` | `EB_SessionApi.jar` | `getCachedLookupValues` | `java.util.List<com.temenos.t24.api.complex.eb.sessionapi.LookupValue>` |  |
| `Session` | `EB_SessionApi.jar` | `clearLookupCache` | `void` |  |
| `Session` | `EB_SessionApi.jar` | `getExternalUserId` | `java.lang.String` |  |
| `Session` | `EB_SessionApi.jar` | `getClientConnection` | `com.temenos.t24.api.complex.eb.sessionapi.Connection` |  |
| `Session` | `EB_SessionApi.jar` | `addMessageToQueue` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `addMessageToQueue` | `com.temenos.api.TBoolean` |  |
| `Session` | `EB_SessionApi.jar` | `getUnauthorisedRecord` | `com.temenos.api.TStructure` |  |
| `Session` | `EB_SessionHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `Session` | `EB_SessionHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `Session` | `EB_SessionHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `Session` | `EB_SessionHook.jar` | `initialise` | `void` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `Session` | `EB_SessionHook.jar` | `loadRecord` | `void` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `Session` | `EB_SessionHook.jar` | `deriveLabelValue` | `java.lang.String` | This interface enables the implementer to return the derived data for the field label based on the data arguments defined in the EB.CONTEXT table. |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getVersion` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `checkId` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `validateRecord` | `com.temenos.api.TValidationResponse` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `updateLookupTable` | `com.temenos.api.TBoolean` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `defaultFieldValues` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `defaultFieldValuesOnHotField` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `formatDealSlip` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `validateField` | `com.temenos.api.TValidationResponse` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `updateCoreRecord` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `setOverrideComparisonValue` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `postUpdateRequest` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `isOverrideAutoApprove` | `com.temenos.api.TBoolean` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getTransactionMessage` | `java.lang.String` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `updateRecord` | `void` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getServiceControlDetail` | `com.temenos.t24.api.complex.eb.servicehook.ServiceControl` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `enableAutomaticAuthorisation` | `com.temenos.api.TBoolean` |  |
| `RecordLifecycle` | `EB_TemplateHook.jar` | `getLookupRecordAmendments` | `java.util.List<com.temenos.t24.api.complex.eb.templatehook.LookupRecordAmendment>` |  |

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
| `AC_AccountApi.jar` | 20 | public-api, unknown |
| `AC_AccountClosure.jar` | 91 | unknown |
| `AC_AccountHook.jar` | 10 | public-api, unknown |
| `AC_AccountingEventsService.jar` | 18 | unknown |
| `AC_AccountOpening.jar` | 298 | unknown |
| `AC_AccountServiceHook.jar` | 3 | public-api, unknown |
| `AC_AccountStatement.jar` | 149 | unknown |
| `AC_Alerts.jar` | 11 | unknown |
| `AC_API.jar` | 119 | unknown |
| `AC_Archiving.jar` | 37 | unknown |
| `AC_BalanceUpdates.jar` | 114 | unknown |
| `AC_CashFlow.jar` | 142 | unknown |
| `AC_CategoryApi.jar` | 3 | public-api, unknown |
| `AC_Channels.jar` | 10 | unknown |
| `AC_ChargeApi.jar` | 3 | public-api, unknown |
| `AC_ClearingServiceHook.jar` | 3 | public-api, unknown |
| `AC_Config.jar` | 129 | unknown |
| `AC_Contract.jar` | 11 | unknown |
| `AC_ContractHook.jar` | 4 | public-api, unknown |
| `AC_CurrencyPosition.jar` | 148 | unknown |
| `AC_DDAService.jar` | 48 | unknown |
| `AC_EntryBalancing.jar` | 9 | unknown |
| `AC_EntryCreation.jar` | 163 | unknown |
| `AC_Fees.jar` | 49 | unknown |
| `AC_HighVolume.jar` | 60 | unknown |
| `AC_IFConfig.jar` | 74 | unknown |
| `AC_IFRS.jar` | 26 | unknown |
| `AC_IntegrityCheck.jar` | 18 | unknown |
| `AC_MiBase.jar` | 15 | unknown |
| `AC_ModelBank.jar` | 209 | unknown |
| `AC_NSF.jar` | 33 | unknown |
| `AC_PaymentNetting.jar` | 63 | unknown |
| `AC_SoftAccounting.jar` | 57 | unknown |
| `AC_StandingOrderProcessing.jar` | 13 | unknown |
| `AC_StandingOrders.jar` | 127 | unknown |
| `AC_StatementHook.jar` | 9 | public-api, unknown |
| `AC_StmtMappingService.jar` | 6 | unknown |
| `AC_StmtPrinting.jar` | 135 | unknown |
| `AC_TransactionData.jar` | 17 | unknown |
| `AC_ValueDatedProcess.jar` | 28 | unknown |
| `EB_AgentFramework.jar` | 23 | unknown |
| `EB_AlertProcessing.jar` | 21 | unknown |
| `EB_API.jar` | 191 | unknown |
| `EB_ARC.jar` | 78 | unknown |
| `EB_ArchiveHook.jar` | 11 | public-api, unknown |
| `EB_Archiving.jar` | 44 | unknown |
| `EB_ArcSecurity.jar` | 9 | unknown |
| `EB_AuthenticationService.jar` | 24 | unknown |
| `EB_AuthorizationService.jar` | 10 | unknown |
| `EB_AutomationService.jar` | 6 | unknown |
| `EB_Browser.jar` | 101 | unknown |
| `EB_BrowserEnquiry.jar` | 26 | unknown |
| `EB_BrowserTags.jar` | 1 | unknown |
| `EB_BrowserVersion.jar` | 23 | unknown |
| `EB_CatalogService.jar` | 168 | unknown |
| `EB_Channels.jar` | 28 | unknown |
| `EB_CMM.jar` | 5 | unknown |
| `EB_Constraints.jar` | 45 | unknown |
| `EB_Conversion.jar` | 31 | unknown |
| `EB_DataAccess.jar` | 43 | unknown |
| `EB_DataAccessApi.jar` | 13 | public-api, unknown |
| `EB_Database.jar` | 4 | unknown |
| `EB_DataFormattingEngineHook.jar` | 25 | public-api, unknown |
| `EB_DataMappingHook.jar` | 3 | public-api, unknown |
| `EB_DateApi.jar` | 18 | public-api, unknown |
| `EB_DateHook.jar` | 3 | public-api, unknown |
| `EB_DatInterface.jar` | 38 | unknown |
| `EB_Dealslip.jar` | 9 | unknown |
| `EB_Delivery.jar` | 50 | unknown |
| `EB_Desktop.jar` | 147 | unknown |
| `EB_Dim.jar` | 20 | unknown |
| `EB_Display.jar` | 63 | unknown |
| `EB_EncryptionHook.jar` | 13 | public-api, unknown |
| `EB_EnquiryHook.jar` | 10 | public-api, unknown |
| `EB_EntitlementService.jar` | 9 | unknown |
| `EB_ErrorProcessing.jar` | 34 | unknown |
| `EB_EventDeliveryService.jar` | 12 | unknown |
| `EB_FileUpload.jar` | 28 | unknown |
| `EB_Foundation.jar` | 123 | unknown |
| `EB_IFConfig.jar` | 1 | unknown |
| `EB_Interface.jar` | 110 | unknown |
| `EB_InternalUtility.jar` | 47 | unknown |
| `EB_Iris.jar` | 27 | unknown |
| `EB_LocalContent.jar` | 14 | unknown |
| `EB_LocalReferences.jar` | 17 | unknown |
| `EB_Logging.jar` | 82 | unknown |
| `EB_Mandate.jar` | 47 | unknown |
| `EB_MdalFramework.jar` | 39 | unknown |
| `EB_MessageHook.jar` | 4 | public-api, unknown |
| `EB_MicroService.jar` | 39 | event, unknown |
| `EB_ModelBank.jar` | 92 | unknown |
| `EB_Monitoring.jar` | 24 | unknown |
| `EB_NonStop.jar` | 3 | unknown |
| `EB_OFSConnectorService.jar` | 8 | unknown |
| `EB_OverrideProcessing.jar` | 65 | unknown |
| `EB_PresentationServices.jar` | 33 | unknown |
| `EB_ProductConfig.jar` | 44 | unknown |
| `EB_RecordApi.jar` | 3 | public-api, unknown |
| `EB_Repgens.jar` | 32 | unknown |
| `EB_Reports.jar` | 185 | unknown |
| `EB_ResourceProviderService.jar` | 190 | unknown |
| `EB_RulesEngine.jar` | 36 | unknown |
| `EB_Seat.jar` | 21 | unknown |
| `EB_Security.jar` | 114 | unknown |
| `EB_SecurityHook.jar` | 6 | public-api, unknown |
| `EB_Service.jar` | 234 | unknown |
| `EB_ServiceHook.jar` | 16 | public-api, unknown |
| `EB_SessionApi.jar` | 34 | public-api, unknown |
| `EB_SessionHook.jar` | 5 | public-api, unknown |
| `EB_Sms.jar` | 18 | unknown |
| `EB_SOAframework.jar` | 23 | unknown |
| `EB_StateEngine.jar` | 18 | unknown |
| `EB_StateMachineService.jar` | 32 | unknown |
| `EB_Streaming.jar` | 51 | unknown |
| `EB_SupportUtilities.jar` | 7 | unknown |
| `EB_SystemTables.jar` | 490 | unknown |
| `EB_SystemTesting.jar` | 11 | unknown |
| `EB_Template.jar` | 149 | unknown |
| `EB_TemplateHook.jar` | 25 | public-api, unknown |
| `EB_TimeService.jar` | 10 | unknown |
| `EB_Toolbox.jar` | 9 | unknown |
| `EB_TransactionControl.jar` | 76 | unknown |
| `EB_TSDK.jar` | 29 | unknown |
| `EB_Updates.jar` | 130 | unknown |
| `EB_UpdatesRun.jar` | 9 | unknown |
| `EB_Upgrade.jar` | 120 | unknown |
| `EB_Utility.jar` | 258 | unknown |
| `EB_Versions.jar` | 34 | unknown |
| `EB_XML.jar` | 11 | unknown |
