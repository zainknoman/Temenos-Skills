# Miscellaneous & Frameworks — Reference

> Generated 2026-06-20T03:17:58.699072+00:00 from 1033 JARs. Re-run `aggregate.py` to refresh.

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
| `Clearing` | `ACHFRM_ClearingHouseHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementor to update information related to transactions in automated clearing house entries. |
| `Clearing` | `ACHFRM_ClearingHouseHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementor to update information related to transactions in automated clearing house entries. |
| `Clearing` | `ACHFRM_ClearingHouseHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementor to update information related to transactions in automated clearing house entries. |
| `Clearing` | `ACHFRM_ClearingHouseHook.jar` | `updateEntry` | `com.temenos.t24.api.complex.achfrm.clearinghousehook.EntryData` | This interface enables the implementor to update information related to transactions in automated clearing house entries. |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `getVersion` | `java.lang.String` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `defaultSoftClassFieldValues` | `void` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `validateSoftClassRecord` | `com.temenos.api.TValidationResponse` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `processSoftClass` | `void` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `processSoftClassActivity` | `void` |  |
| `SoftClassActivityLifecycle` | `AF_ApiClassHook.jar` | `postUpdateRequest` | `void` |  |
| `SoftClass` | `AF_SoftClassApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty SoftClass.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `SoftClass` | `AF_SoftClassApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty SoftClass.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `SoftClass` | `AF_SoftClassApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty SoftClass.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `SoftClass` | `AF_SoftClassApi.jar` | `getSoftClassInstance` | `com.temenos.api.TStructure` | Default constructor. Create an empty SoftClass.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `InterfaceProcessEngine` | `ALLFND_InterfaceProcessEngineHook.jar` | `getVersion` | `java.lang.String` |  |
| `InterfaceProcessEngine` | `ALLFND_InterfaceProcessEngineHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `InterfaceProcessEngine` | `ALLFND_InterfaceProcessEngineHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `InterfaceProcessEngine` | `ALLFND_InterfaceProcessEngineHook.jar` | `convertData` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getVersion` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `updateRequestMessage` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `modifyRequestMessage` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `updateResponseMessage` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getMappingId` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `updateAccountNumber` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `calculateCharge` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getBalance` | `com.temenos.api.TNumber` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getFieldValue` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `updateOfsResponseMessage` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getTransactionData` | `com.temenos.t24.api.complex.atmfrm.messagehook.TransactionData` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getDualTransactionId` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `updateRecord` | `void` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getCharge` | `com.temenos.t24.api.complex.atmfrm.messagehook.Charge` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getAtmTransactionId` | `java.lang.String` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getReservationAmount` | `com.temenos.api.TNumber` |  |
| `AtmMessageLifecycle` | `ATMFRM_MessageHook.jar` | `getCompanyCode` | `java.lang.String` |  |
| `Charge` | `CG_ChargeApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateCharges` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateCharges` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateCommission` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateCommission` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateTax` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `calculateTax` | `com.temenos.t24.api.complex.cg.chargeapi.TaxData` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `getCommissionCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `getFundsTransferCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Charge` | `CG_ChargeApi.jar` | `getChargeCondition` | `com.temenos.t24.api.complex.cg.chargeapi.Condition` | Default constructor. Create an empty Charge.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `LegalID` | `CMBASE_IdValidationHook.jar` | `getVersion` | `java.lang.String` | This interface component allows to attach a validation routine that validates the given LegalID |
| `LegalID` | `CMBASE_IdValidationHook.jar` | `getBuildDate` | `java.lang.String` | This interface component allows to attach a validation routine that validates the given LegalID |
| `LegalID` | `CMBASE_IdValidationHook.jar` | `getComponentVersion` | `java.lang.String` | This interface component allows to attach a validation routine that validates the given LegalID |
| `LegalID` | `CMBASE_IdValidationHook.jar` | `validateLegalID` | `void` | This interface component allows to attach a validation routine that validates the given LegalID |
| `XmlExtractService` | `CMBASE_InterfaceBatchExtractHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to decide whether to process the current Id. |
| `XmlExtractService` | `CMBASE_InterfaceBatchExtractHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to decide whether to process the current Id. |
| `XmlExtractService` | `CMBASE_InterfaceBatchExtractHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to decide whether to process the current Id. |
| `XmlExtractService` | `CMBASE_InterfaceBatchExtractHook.jar` | `processId` | `com.temenos.api.TBoolean` | This interface enables the implementer to decide whether to process the current Id. |
| `GeneralDataProtectionRegulation` | `CZ_FrameworkHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process. |
| `GeneralDataProtectionRegulation` | `CZ_FrameworkHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process. |
| `GeneralDataProtectionRegulation` | `CZ_FrameworkHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process. |
| `GeneralDataProtectionRegulation` | `CZ_FrameworkHook.jar` | `isEligible` | `com.temenos.api.TBoolean` | This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process. |
| `GeneralDataProtectionRegulation` | `CZ_FrameworkHook.jar` | `getObfuscatedFieldValue` | `java.lang.String` | This interface enables the implementer to return the obfuscated version of a party's personal information to replace the original field value in the record to fulfil the customer data protection erasure process. |
| `DebitCollectionOrderHook` | `DB_DebitCollectionOrderHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to validate debit collection Product record. |
| `DebitCollectionOrderHook` | `DB_DebitCollectionOrderHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to validate debit collection Product record. |
| `DebitCollectionOrderHook` | `DB_DebitCollectionOrderHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to validate debit collection Product record. |
| `DebitCollectionOrderHook` | `DB_DebitCollectionOrderHook.jar` | `validateRecord` | `void` | This interface enables the implementer to validate debit collection Product record. |
| `DirectDebit` | `DD_ContractHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DirectDebit` | `DD_ContractHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DirectDebit` | `DD_ContractHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DirectDebit` | `DD_ContractHook.jar` | `setCreditorReference` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DirectDebit` | `DD_ContractHook.jar` | `setClearingReference` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DirectDebit` | `DD_ContractHook.jar` | `setMandateId` | `java.lang.String` | This Interface enables the implementer to set the clearing reference for the direct debit. |
| `DataExporter` | `DW_DataExportHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getIds` | `java.util.List<java.lang.String>` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getRows` | `java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.Row>` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getCustomFields` | `java.util.List<com.temenos.t24.api.complex.dw.dataexporthook.Field>` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `excludeId` | `com.temenos.api.TBoolean` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `transferDataExtract` | `com.temenos.api.TBoolean` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `setCustomFields` | `void` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `DataExporter` | `DW_DataExportHook.jar` | `getFilterCriteria` | `java.lang.String` | This interface enables the implementer to filter records from the data extract by excluding them. |
| `Collateral` | `FICOLL_CollateralHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the calculated depreciation amount. |
| `Collateral` | `FICOLL_CollateralHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the calculated depreciation amount. |
| `Collateral` | `FICOLL_CollateralHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the calculated depreciation amount. |
| `Collateral` | `FICOLL_CollateralHook.jar` | `getDepreciationAmount` | `com.temenos.api.TNumber` | This interface enables the implementer to return the calculated depreciation amount. |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `getVersion` | `java.lang.String` |  |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `getBuildDate` | `java.lang.String` |  |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `getComponentVersion` | `java.lang.String` |  |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `calculateContractBalance` | `void` |  |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `getExpectedCreditLoss` | `com.temenos.t24.api.complex.ia.accountinghook.ExpectedCreditLoss` |  |
| `InternationalAccountingStandards` | `IA_AccountingHook.jar` | `getCollateralDetails` | `com.temenos.t24.api.complex.ia.accountinghook.CollateralDetails` |  |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getVersion` | `java.lang.String` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getBuildDate` | `java.lang.String` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getEffectiveInterestRate` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getEffectiveInterestRate` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getNetPresentValue` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getNetPresentValue` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getNetPresentValue` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IFRSValuation` | `IA_ValuationApi.jar` | `getNetPresentValue` | `com.temenos.api.TNumber` | Create a new IFRSValuation using a specific context.. |
| `IntegrationFramework` | `IF_IntegrationFrameworkHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return join Ids where the data from two related tables need to be fetched but does not have common key fields |
| `IntegrationFramework` | `IF_IntegrationFrameworkHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return join Ids where the data from two related tables need to be fetched but does not have common key fields |
| `IntegrationFramework` | `IF_IntegrationFrameworkHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return join Ids where the data from two related tables need to be fetched but does not have common key fields |
| `IntegrationFramework` | `IF_IntegrationFrameworkHook.jar` | `getJoinIds` | `java.util.List<java.lang.String>` | This interface enables the implementer to return join Ids where the data from two related tables need to be fetched but does not have common key fields |
| `XmlStatementGenerator` | `IX_XmlStatementHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to return the values for each child tag defined in the xmlTagDefintionRecord. |
| `XmlStatementGenerator` | `IX_XmlStatementHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to return the values for each child tag defined in the xmlTagDefintionRecord. |
| `XmlStatementGenerator` | `IX_XmlStatementHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to return the values for each child tag defined in the xmlTagDefintionRecord. |
| `XmlStatementGenerator` | `IX_XmlStatementHook.jar` | `getGroupTagValues` | `java.util.List<com.temenos.t24.api.complex.ix.xmlstatementhook.Tags>` | This Interface enables the implementer to return the values for each child tag defined in the xmlTagDefintionRecord. |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `getDiscountRate` | `com.temenos.api.TNumber` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `calculateChargeAmount` | `com.temenos.t24.api.complex.lc.letterofcredithook.ChargeAmount` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `getDiscrepancyText` | `java.lang.String` | Deprecated.  No further information |
| `LetterOfCredit` | `LC_LetterOfCreditHook.jar` | `updateDocumentaryCreditRecords` | `void` | Deprecated.  No further information |
| `Insurance` | `LENINS_InsuranceHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to Calculate and return the lending insurance charge amount. |
| `Insurance` | `LENINS_InsuranceHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to Calculate and return the lending insurance charge amount. |
| `Insurance` | `LENINS_InsuranceHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to Calculate and return the lending insurance charge amount. |
| `Insurance` | `LENINS_InsuranceHook.jar` | `getCharge` | `com.temenos.api.TNumber` | This interface enables the implementer to Calculate and return the lending insurance charge amount. |
| `LoanRenewal` | `LENREN_LoanRenewalHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to determine whether automatic loan renewal is to be rejected. |
| `LoanRenewal` | `LENREN_LoanRenewalHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to determine whether automatic loan renewal is to be rejected. |
| `LoanRenewal` | `LENREN_LoanRenewalHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to determine whether automatic loan renewal is to be rejected. |
| `LoanRenewal` | `LENREN_LoanRenewalHook.jar` | `rejectRenewal` | `com.temenos.api.TBoolean` | This interface enables the implementer to determine whether automatic loan renewal is to be rejected. |
| `Limit` | `LI_LimitApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `setLimitId` | `void` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `getCurrencyAmount` | `com.temenos.t24.api.complex.li.limitapi.LimitCurrencyAmount` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `getLiabilityReferences` | `java.util.List<com.temenos.t24.api.complex.li.limitapi.LiabilityReferences>` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Limit` | `LI_LimitApi.jar` | `getLiabilities` | `java.util.List<com.temenos.t24.api.complex.li.limitapi.Liability>` | Default constructor. Create an empty Limit.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Guarantee` | `MD_MdDealHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified records and transaction data. |
| `Guarantee` | `MD_MdDealHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified records and transaction data. |
| `Guarantee` | `MD_MdDealHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to define one or more records to be input using the specified records and transaction data. |
| `Guarantee` | `MD_MdDealHook.jar` | `updateGuaranteeRecords` | `void` | This interface enables the implementer to define one or more records to be input using the specified records and transaction data. |
| `Integrator` | `OC_IntegrationHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementor to generate and return a unique id. |
| `Integrator` | `OC_IntegrationHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementor to generate and return a unique id. |
| `Integrator` | `OC_IntegrationHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementor to generate and return a unique id. |
| `Integrator` | `OC_IntegrationHook.jar` | `getUniqueTransactionId` | `com.temenos.t24.api.complex.oc.integrationhook.UniqueId` | This interface enables the implementor to generate and return a unique id. |
| `Obligor` | `OX_ObligorHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `Obligor` | `OX_ObligorHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `Obligor` | `OX_ObligorHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `Obligor` | `OX_ObligorHook.jar` | `getObligors` | `java.util.List<java.lang.String>` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `Obligor` | `OX_ObligorHook.jar` | `getReferenceObligor` | `java.lang.String` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `Obligor` | `OX_ObligorHook.jar` | `getObligorRiskClass` | `java.lang.String` | This Interface enables the implementer to classify the obligor risk level for example STANDARD, DOUBTFUL or BAD. |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `getVersion` | `java.lang.String` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `getBuildDate` | `java.lang.String` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `getComponentVersion` | `java.lang.String` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `isChargeApplied` | `com.temenos.api.TBoolean` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `setPaymentOrderProduct` | `void` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `getPaymentOrderProductId` | `java.lang.String` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `validateRecord` | `void` | Deprecated.  use PaymentOrderLifecycle.setProductId instead |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `getVersion` | `java.lang.String` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `getBuildDate` | `java.lang.String` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `getComponentVersion` | `java.lang.String` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `handleValidationEvent` | `void` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `applyChargeType` | `com.temenos.api.TBoolean` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `setProductId` | `void` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `validatePaymentOrderRecord` | `com.temenos.api.TValidationResponse` | Create a new PaymentOrderLifecycle using a specific context.. |
| `PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `getPaymentSystemType` | `com.temenos.t24.api.hook.payments.PaymentOrderLifecycle$PaymentSystemType` | Create a new PaymentOrderLifecycle using a specific context.. |
| `Position` | `PM_PositionHook.jar` | `getVersion` | `java.lang.String` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `Position` | `PM_PositionHook.jar` | `getBuildDate` | `java.lang.String` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `Position` | `PM_PositionHook.jar` | `getComponentVersion` | `java.lang.String` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `Position` | `PM_PositionHook.jar` | `getSecurityPosition` | `com.temenos.t24.api.complex.pm.positionhook.SecurityPosition` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `Position` | `PM_PositionHook.jar` | `getForexPosition` | `com.temenos.t24.api.complex.pm.positionhook.ForexPosition` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `Position` | `PM_PositionHook.jar` | `getForwardRateAgreementPosition` | `com.temenos.t24.api.complex.pm.positionhook.ForwardRateAgreementPosition` | This interface is used to obtain the position class values and calculates interest rate and obtains notional currency. |
| `AccountPool` | `PO_AccountPoolHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implemnter to provide a value for the CURRENT.BALANCE field in the AC.CASH.POOL table in T24. |
| `AccountPool` | `PO_AccountPoolHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implemnter to provide a value for the CURRENT.BALANCE field in the AC.CASH.POOL table in T24. |
| `AccountPool` | `PO_AccountPoolHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implemnter to provide a value for the CURRENT.BALANCE field in the AC.CASH.POOL table in T24. |
| `AccountPool` | `PO_AccountPoolHook.jar` | `calculateCurrentBalance` | `com.temenos.api.TNumber` | This interface enables the implemnter to provide a value for the CURRENT.BALANCE field in the AC.CASH.POOL table in T24. |
| `DebitOrderHook` | `PPADEB_DebitOrderHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to validate payment order Product record. |
| `DebitOrderHook` | `PPADEB_DebitOrderHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to validate payment order Product record. |
| `DebitOrderHook` | `PPADEB_DebitOrderHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to validate payment order Product record. |
| `DebitOrderHook` | `PPADEB_DebitOrderHook.jar` | `validateDebitOrder` | `void` | This interface enables the implementer to validate payment order Product record. |
| `DebitOrderHook` | `PPADEB_DebitOrderHook.jar` | `autoAcceptanceAPI` | `void` | This interface enables the implementer to validate payment order Product record. |
| `Assessment` | `PV_ContractAssessmentHook.jar` | `getVersion` | `java.lang.String` | This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system. |
| `Assessment` | `PV_ContractAssessmentHook.jar` | `getBuildDate` | `java.lang.String` | This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system. |
| `Assessment` | `PV_ContractAssessmentHook.jar` | `getComponentVersion` | `java.lang.String` | This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system. |
| `Assessment` | `PV_ContractAssessmentHook.jar` | `getContractStatus` | `void` | This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system. |
| `Assessment` | `PV_ContractAssessmentHook.jar` | `getObligorStatus` | `void` | This Interface enables the implementer to return Days Past Due(DPD) related details of the contract from external system. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getRiskClass` | `java.lang.String` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getRiskSegment` | `java.lang.String` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getRiskCollateralValue` | `com.temenos.api.TNumber` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getSegmentationProvision` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.SegmentationProvision` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `ProvisionManagement` | `PV_ProvisionManagementHook.jar` | `getProvision` | `com.temenos.t24.api.complex.pv.provisionmanagementhook.Provision` | This interface enables the implementer to calculate and return the provision information for a contract. |
| `Process` | `PW_ProcessHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return the evaluated condition for processing activity. |
| `Process` | `PW_ProcessHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return the evaluated condition for processing activity. |
| `Process` | `PW_ProcessHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return the evaluated condition for processing activity. |
| `Process` | `PW_ProcessHook.jar` | `getActivity` | `java.lang.String` | This interface enables the implementer to return the evaluated condition for processing activity. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `setTransactionCapture` | `void` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `modifyRecyclingCaptureData` | `void` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `evaluateSettlement` | `com.temenos.t24.api.complex.rc.contracthook.SettlementResponse` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `processSettlement` | `com.temenos.t24.api.complex.rc.contracthook.SettlementResponse` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `updateRecord` | `void` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `TransactionRecycler` | `RC_ContractHook.jar` | `sortRetryRequests` | `void` | This interface enables the implementer to evaluate a settlement for processing by updating the settlement details, setting an error status or handing off settlement for processing against other accounts. |
| `Report` | `RE_AccountingReportApi.jar` | `getVersion` | `java.lang.String` | Create a new Report using a specific context.. |
| `Report` | `RE_AccountingReportApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Report using a specific context.. |
| `Report` | `RE_AccountingReportApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Report using a specific context.. |
| `Report` | `RE_AccountingReportApi.jar` | `getAssetLiabilityReportLines` | `java.util.List<com.temenos.t24.api.complex.re.accountingreportapi.ReportLine>` | Create a new Report using a specific context.. |
| `Report` | `RE_AccountingReportApi.jar` | `getProfitLossReportLines` | `java.util.List<com.temenos.t24.api.complex.re.accountingreportapi.ReportLine>` | Create a new Report using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `getVersion` | `java.lang.String` | Create a new Balance using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Balance using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Balance using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | Create a new Balance using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | Create a new Balance using a specific context.. |
| `Balance` | `RE_ContractBalanceApi.jar` | `get` | `com.temenos.t24.api.complex.re.contractbalanceapi.Balance` | Create a new Balance using a specific context.. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `validateRecord` | `void` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `getResultOption` | `void` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `RfRtpOrderHook` | `RF_RTPOrderHook.jar` | `mapPOAToRtp` | `void` | This interface enables the implementer to determine the result option which in turn will be used for mapping back to the source system. |
| `Message` | `SWFTAL_FoundationApi.jar` | `getVersion` | `java.lang.String` | Create a new Message using a specific context.. |
| `Message` | `SWFTAL_FoundationApi.jar` | `getBuildDate` | `java.lang.String` | Create a new Message using a specific context.. |
| `Message` | `SWFTAL_FoundationApi.jar` | `getComponentVersion` | `java.lang.String` | Create a new Message using a specific context.. |
| `Message` | `SWFTAL_FoundationApi.jar` | `formatHeader` | `void` | Create a new Message using a specific context.. |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `setServiceHandler` | `void` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `tidyUp` | `void` |  |
| `DDAServiceAPI` | `t24-AC_DDAService-t24service.jar` | `cleanup` | `void` |  |
| `DDAServiceProxyAPI` | `t24-AC_DDAService-t24service.jar` | `setSecurityContext` | `void` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `setServiceHandler` | `void` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `tidyUp` | `void` |  |
| `DfMappingServiceAPI` | `t24-DF_DfMappingService-t24service.jar` | `cleanup` | `void` |  |
| `DfMappingServiceProxyAPI` | `t24-DF_DfMappingService-t24service.jar` | `setSecurityContext` | `void` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `setServiceHandler` | `void` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `tidyUp` | `void` |  |
| `DesignStudioInstallerServiceAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `cleanup` | `void` |  |
| `DesignStudioInstallerServiceProxyAPI` | `t24-DS_DesignStudioInstallerService-t24service.jar` | `setSecurityContext` | `void` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `setServiceHandler` | `void` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `tidyUp` | `void` |  |
| `AuthenticationServiceAPI` | `t24-EB_AuthenticationService-t24service.jar` | `cleanup` | `void` |  |
| `AuthenticationServiceProxyAPI` | `t24-EB_AuthenticationService-t24service.jar` | `setSecurityContext` | `void` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `setServiceHandler` | `void` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `tidyUp` | `void` |  |
| `AuthorizationServiceAPI` | `t24-EB_AuthorizationService-t24service.jar` | `cleanup` | `void` |  |
| `AuthorizationServiceProxyAPI` | `t24-EB_AuthorizationService-t24service.jar` | `setSecurityContext` | `void` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `setServiceHandler` | `void` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `tidyUp` | `void` |  |
| `AutomationServiceAPI` | `t24-EB_AutomationService-t24service.jar` | `cleanup` | `void` |  |
| `AutomationServiceProxyAPI` | `t24-EB_AutomationService-t24service.jar` | `setSecurityContext` | `void` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `setServiceHandler` | `void` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `tidyUp` | `void` |  |
| `CatalogServiceAPI` | `t24-EB_CatalogService-t24service.jar` | `cleanup` | `void` |  |
| `CatalogServiceProxyAPI` | `t24-EB_CatalogService-t24service.jar` | `setSecurityContext` | `void` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `setServiceHandler` | `void` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `tidyUp` | `void` |  |
| `EntitlementServiceAPI` | `t24-EB_EntitlementService-t24service.jar` | `cleanup` | `void` |  |
| `EntitlementServiceProxyAPI` | `t24-EB_EntitlementService-t24service.jar` | `setSecurityContext` | `void` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `setServiceHandler` | `void` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `tidyUp` | `void` |  |
| `OFSConnectorServiceAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `cleanup` | `void` |  |
| `OFSConnectorServiceProxyAPI` | `t24-EB_OFSConnectorService-t24service.jar` | `setSecurityContext` | `void` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `setServiceHandler` | `void` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `tidyUp` | `void` |  |
| `ResourceProviderServiceAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `cleanup` | `void` |  |
| `ResourceProviderServiceProxyAPI` | `t24-EB_ResourceProviderService-t24service.jar` | `setSecurityContext` | `void` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `setServiceHandler` | `void` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `tidyUp` | `void` |  |
| `SmsAPI` | `t24-EB_Sms-t24service.jar` | `cleanup` | `void` |  |
| `SmsProxyAPI` | `t24-EB_Sms-t24service.jar` | `setSecurityContext` | `void` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `setServiceHandler` | `void` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `tidyUp` | `void` |  |
| `InboundSecurityServiceAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `cleanup` | `void` |  |
| `InboundSecurityServiceProxyAPI` | `t24-IF_InboundSecurityService-t24service.jar` | `setSecurityContext` | `void` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `setServiceHandler` | `void` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `tidyUp` | `void` |  |
| `InflowServiceAPI` | `t24-IF_InflowService-t24service.jar` | `cleanup` | `void` |  |
| `InflowServiceProxyAPI` | `t24-IF_InflowService-t24service.jar` | `setSecurityContext` | `void` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `setServiceHandler` | `void` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `tidyUp` | `void` |  |
| `IntegrationFlowServiceAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `cleanup` | `void` |  |
| `IntegrationFlowServiceProxyAPI` | `t24-IF_IntegrationFlowService-t24service.jar` | `setSecurityContext` | `void` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `setServiceHandler` | `void` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `tidyUp` | `void` |  |
| `IntegrationFrameworkServiceAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `cleanup` | `void` |  |
| `IntegrationFrameworkServiceProxyAPI` | `t24-IF_IntegrationFrameworkService-t24service.jar` | `setSecurityContext` | `void` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `setServiceHandler` | `void` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `tidyUp` | `void` |  |
| `IntegrationLandscapeServiceAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `cleanup` | `void` |  |
| `IntegrationLandscapeServiceProxyAPI` | `t24-IF_IntegrationLandscapeService-t24service.jar` | `setSecurityContext` | `void` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `setServiceHandler` | `void` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `tidyUp` | `void` |  |
| `TraFixServiceAPI` | `t24-PP_TraFixService-t24service.jar` | `cleanup` | `void` |  |
| `TraFixServiceProxyAPI` | `t24-PP_TraFixService-t24service.jar` | `setSecurityContext` | `void` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `setServiceHandler` | `void` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `tidyUp` | `void` |  |
| `HumanTaskServiceAPI` | `t24-PW_HumanTaskService-t24service.jar` | `cleanup` | `void` |  |
| `HumanTaskServiceProxyAPI` | `t24-PW_HumanTaskService-t24service.jar` | `setSecurityContext` | `void` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `setServiceHandler` | `void` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `tidyUp` | `void` |  |
| `ProcessEngineServiceAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `cleanup` | `void` |  |
| `ProcessEngineServiceProxyAPI` | `t24-PW_ProcessEngineService-t24service.jar` | `setSecurityContext` | `void` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `setServiceHandler` | `void` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `tidyUp` | `void` |  |
| `ReplicationServiceAPI` | `t24-RR_ReplicationService-t24service.jar` | `cleanup` | `void` |  |
| `ReplicationServiceProxyAPI` | `t24-RR_ReplicationService-t24service.jar` | `setSecurityContext` | `void` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `getMetaData` | `java.lang.String` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `healthCheck` | `com.temenos.tafj.common.healthcheck.HealthCheckResponse` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `setServiceHandler` | `void` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `getServiceHandler` | `com.temenos.soa.services.tafj.TAFJServiceHandler` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `setUserContextCallBack` | `void` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `getUserContextCallBack` | `com.temenos.soa.services.UserContextCallBack` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `tidyUp` | `void` |  |
| `CustomerServiceAPI` | `t24-ST_CustomerService-t24service.jar` | `cleanup` | `void` |  |
| `CustomerServiceProxyAPI` | `t24-ST_CustomerService-t24service.jar` | `setSecurityContext` | `void` |  |
| `Table_IF_FLOW_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_IF_FLOW_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Table_EB_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_EB_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Table_DW_EXPORT_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_DW_EXPORT_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Table_CMBASE_TAX_EXEMPTION_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_CMBASE_TAX_EXEMPTION_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Table_ARACCT_FX_PAYMENT_CANCEL_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_ARACCT_FX_PAYMENT_CANCEL_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Table_AA_PRD_DES_ACTIVITY_API` | `Tables.jar` | `getFields` | `java.lang.String` |  |
| `Table_AA_PRD_DES_ACTIVITY_API` | `Tables.jar` | `getTableName` | `java.lang.String` |  |
| `Tax` | `TAXGST_TaxRegulatoryApi.jar` | `getVersion` | `java.lang.String` | Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Tax` | `TAXGST_TaxRegulatoryApi.jar` | `getBuildDate` | `java.lang.String` | Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Tax` | `TAXGST_TaxRegulatoryApi.jar` | `getComponentVersion` | `java.lang.String` | Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Tax` | `TAXGST_TaxRegulatoryApi.jar` | `updateTaxRefund` | `com.temenos.t24.api.complex.taxgst.taxregulatoryapi.UpdateResponse` | Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `Tax` | `TAXGST_TaxRegulatoryApi.jar` | `updateGoodsAndServicesTaxRecord` | `com.temenos.t24.api.complex.taxgst.taxregulatoryapi.UpdateResponse` | Default constructor. Create an empty Tax.  Warning  : The class should be constructed with an existing T24Context. This will ensure that the contextual values relating to the user are set up. Many API methods will not work correctly if they do not have an initialised context.. |
| `TaxEngine` | `TX_TaxEngineHook.jar` | `getVersion` | `java.lang.String` | This interface enables the implementer to return a converted field value for the transaction report. |
| `TaxEngine` | `TX_TaxEngineHook.jar` | `getBuildDate` | `java.lang.String` | This interface enables the implementer to return a converted field value for the transaction report. |
| `TaxEngine` | `TX_TaxEngineHook.jar` | `getComponentVersion` | `java.lang.String` | This interface enables the implementer to return a converted field value for the transaction report. |
| `TaxEngine` | `TX_TaxEngineHook.jar` | `convertReportFieldValue` | `java.lang.String` | This interface enables the implementer to return a converted field value for the transaction report. |

---

## Enquiry Routines

*No enquiry routines detected in this domain.*

---

## Record Models

| Class | JAR | Public Fields |
|-------|-----|--------------|
| `EventRecord` | `t24-IF_IntegrationFrameworkService-Data.jar` |  |
| `AggregateBalancesRecord` | `t24-ST_CustomerService-Data.jar` |  |
| `CustomerRecord` | `t24-ST_CustomerService-Data.jar` |  |

---

## JAR Inventory

| JAR | Class Count | Component Types Present |
|-----|-------------|------------------------|
| `AB_Framework.jar` | 57 | unknown |
| `AB_ModelBank.jar` | 10 | unknown |
| `ACCCSM_ClearingService.jar` | 6 | unknown |
| `ACCCSM_Config.jar` | 13 | unknown |
| `ACCCSM_Contract.jar` | 73 | unknown |
| `ACCDOM_Foundation.jar` | 27 | unknown |
| `ACCLAS_ProductConfiguration.jar` | 1 | unknown |
| `ACCPTY_Foundation.jar` | 6 | unknown |
| `ACCPTY_NomineeDetails.jar` | 3 | unknown |
| `ACFAMS_API.jar` | 3 | unknown |
| `ACFAMS_Config.jar` | 20 | unknown |
| `ACFAMS_Contract.jar` | 12 | unknown |
| `ACFAMS_ModelBank.jar` | 2 | unknown |
| `ACFAMS_Service.jar` | 17 | unknown |
| `ACHFRM_ClearingHouseHook.jar` | 3 | public-api, unknown |
| `ACHFRM_Foundation.jar` | 293 | unknown |
| `ACSWIT_Config.jar` | 9 | unknown |
| `ACSWIT_Contract.jar` | 19 | unknown |
| `AD_ModelBank.jar` | 12 | unknown |
| `AF_ActivityProcessing.jar` | 9 | unknown |
| `AF_Advice.jar` | 53 | unknown |
| `AF_ApiClassHook.jar` | 8 | public-api, unknown |
| `AF_ClassFramework.jar` | 159 | unknown |
| `AF_ClassInterfaces.jar` | 25 | unknown |
| `AF_Framework.jar` | 91 | unknown |
| `AF_Mapping.jar` | 87 | unknown |
| `AF_Rules.jar` | 40 | unknown |
| `AF_SoftClassApi.jar` | 3 | public-api, unknown |
| `AFB120_AccountStatement.jar` | 17 | unknown |
| `AFRACP_AssetClassification.jar` | 12 | unknown |
| `AFRACP_ProvisionCalculation.jar` | 8 | unknown |
| `AFRBAS_CustomerDataMapping.jar` | 6 | unknown |
| `AFRBOP_BalanceOfPayment.jar` | 21 | unknown |
| `AFRCIP_CentralisedPaymentIncidents.jar` | 45 | unknown |
| `AFRTRD_Foundation.jar` | 19 | unknown |
| `AG_Framework.jar` | 10 | unknown |
| `AG_ModelBank.jar` | 3 | unknown |
| `AI_ARC.jar` | 4 | unknown |
| `AI_ModelBank.jar` | 54 | unknown |
| `AL_ModelBank.jar` | 12 | unknown |
| `ALLFND_AlternatePortfolioId.jar` | 2 | unknown |
| `ALLFND_AssetTransfer.jar` | 2 | unknown |
| `ALLFND_CustomerOnboarding.jar` | 9 | unknown |
| `ALLFND_FundsCatalogue.jar` | 9 | unknown |
| `ALLFND_InterfaceProcessEngine.jar` | 13 | unknown |
| `ALLFND_InterfaceProcessEngineHook.jar` | 3 | public-api, unknown |
| `ALLFND_MarketingReports.jar` | 3 | unknown |
| `ALLFND_OrderSettlement.jar` | 4 | unknown |
| `ALLFND_RebalancingOrder.jar` | 24 | unknown |
| `AN_Config.jar` | 9 | unknown |
| `AN_ReportExtract.jar` | 5 | unknown |
| `AO_Framework.jar` | 47 | unknown |
| `AO_ModelBank.jar` | 2 | unknown |
| `AP_ARC.jar` | 10 | unknown |
| `AP_ModelBank.jar` | 2 | unknown |
| `AR_ModelBank.jar` | 14 | unknown |
| `ARACCT_AccountAlias.jar` | 47 | unknown |
| `ARACCT_AccountClabe.jar` | 2 | unknown |
| `ARACCT_AliasValidation.jar` | 5 | unknown |
| `ARACCT_AtmFxTransactions.jar` | 16 | unknown |
| `ARACCT_BalanceCheck.jar` | 6 | unknown |
| `ARACCT_BeneficiaryAdditionalFields.jar` | 4 | unknown |
| `ARACCT_CalculationOfRates.jar` | 9 | unknown |
| `ARACCT_CbuCode.jar` | 24 | unknown |
| `ARACCT_DormancyProcess.jar` | 11 | unknown |
| `ARACCT_EarlyRedeemDepositUVA.jar` | 28 | unknown |
| `ARACCT_FXBlacklistLimitValidation.jar` | 39 | unknown |
| `ARACCT_MaturityDateOnHoliday.jar` | 7 | unknown |
| `ARACCT_PaymentTaxPais.jar` | 6 | unknown |
| `ARACCT_PreClosureFee.jar` | 4 | unknown |
| `ARBASE_CustomerAdditionalFields.jar` | 6 | unknown |
| `ARGNPV_CustomerReclassification.jar` | 8 | unknown |
| `ARPYMT_ConceptBook.jar` | 1 | unknown |
| `ARPYMT_DebinRegistration.jar` | 2 | unknown |
| `ARPYMT_DebinUtilities.jar` | 7 | unknown |
| `ARPYMT_DebitOrder.jar` | 4 | unknown |
| `ARPYMT_MandateRegistration.jar` | 32 | unknown |
| `ARPYMT_ReconcilPayments.jar` | 37 | unknown |
| `ARTAXS_ProcessPadrons.jar` | 23 | unknown |
| `ARTAXS_TaxCalculation.jar` | 81 | unknown |
| `ARTAXS_TaxReturns.jar` | 26 | unknown |
| `ARTELL_ChequeControlDigitValidation.jar` | 2 | unknown |
| `AS_Framework.jar` | 3 | unknown |
| `AS_ModelBank.jar` | 3 | unknown |
| `AT_Foundation.jar` | 16 | unknown |
| `ATMFRM_Archive.jar` | 4 | unknown |
| `ATMFRM_Charges.jar` | 11 | unknown |
| `ATMFRM_Clearing.jar` | 19 | unknown |
| `ATMFRM_Foundation.jar` | 16 | unknown |
| `ATMFRM_Mapping.jar` | 87 | unknown |
| `ATMFRM_MessageHook.jar` | 20 | public-api, unknown |
| `ATMFRM_Statement.jar` | 3 | unknown |
| `ATMFRM_TransactionReference.jar` | 15 | unknown |
| `ATMFRM_Utility.jar` | 3 | unknown |
| `AX_Framework.jar` | 2 | unknown |
| `AZ_Accounting.jar` | 21 | unknown |
| `AZ_Config.jar` | 28 | unknown |
| `AZ_Contract.jar` | 38 | unknown |
| `AZ_Delivery.jar` | 5 | unknown |
| `AZ_Foundation.jar` | 45 | unknown |
| `AZ_Interest.jar` | 19 | unknown |
| `AZ_LatePayment.jar` | 12 | unknown |
| `AZ_Maturity.jar` | 10 | unknown |
| `AZ_ModelBank.jar` | 18 | unknown |
| `AZ_Overdue.jar` | 7 | unknown |
| `AZ_Payment.jar` | 12 | unknown |
| `AZ_PaymentSchedule.jar` | 10 | unknown |
| `AZ_Reports.jar` | 2 | unknown |
| `AZ_Schedules.jar` | 33 | unknown |
| `BE_AlertProcessing.jar` | 21 | unknown |
| `BE_ModelBank.jar` | 7 | unknown |
| `BENINT_Foundation.jar` | 10 | unknown |
| `BETOBT_WithholdingTax.jar` | 14 | unknown |
| `BF_ConBalanceUpdates.jar` | 18 | unknown |
| `BF_Framework.jar` | 6 | unknown |
| `BF_LimitExtTxn.jar` | 10 | unknown |
| `BL_Foundation.jar` | 248 | unknown |
| `BL_ModelBank.jar` | 11 | unknown |
| `BLMBPR_Foundation.jar` | 36 | unknown |
| `BLMBRT_Foundation.jar` | 19 | unknown |
| `BLNCNF_Foundation.jar` | 10 | unknown |
| `BM_Core.jar` | 6 | unknown |
| `BU_Config.jar` | 4 | unknown |
| `BU_Contract.jar` | 24 | unknown |
| `BU_Services.jar` | 5 | unknown |
| `BX_Framework.jar` | 21 | unknown |
| `BX_ModelBank.jar` | 6 | unknown |
| `BY_Payments.jar` | 39 | unknown |
| `CA_ClearingReachability.jar` | 19 | unknown |
| `CA_Config.jar` | 7 | unknown |
| `CA_Contract.jar` | 17 | unknown |
| `CAADRT_AddressRight.jar` | 22 | unknown |
| `CAAKCL_AkcelerantInterface.jar` | 87 | unknown |
| `CAATMD_CardtronicsFHM.jar` | 10 | unknown |
| `CAATMD_DCPInterface.jar` | 79 | unknown |
| `CAATMI_EverlinkATMInterface.jar` | 110 | unknown |
| `CAATMI_EverlinkFHM.jar` | 10 | unknown |
| `CAATMI_HexaToAscii.jar` | 2 | unknown |
| `CAATMI_ISOListener.jar` | 8 | unknown |
| `CAAUST_Foundation.jar` | 2 | unknown |
| `CABASE_AccountClosure.jar` | 10 | unknown |
| `CABASE_AccountNumbering.jar` | 2 | unknown |
| `CABASE_AMLInterface.jar` | 56 | unknown |
| `CABASE_ATMFoundation.jar` | 60 | unknown |
| `CABASE_CustomerRelation.jar` | 192 | unknown |
| `CABASE_CustomerStatement.jar` | 157 | unknown |
| `CABASE_Foundation.jar` | 171 | unknown |
| `CABASE_FutureXConnect.jar` | 2 | unknown |
| `CABASE_LegacyFinancial.jar` | 16 | unknown |
| `CABASE_SingleView.jar` | 28 | unknown |
| `CABASE_UserSecurity.jar` | 21 | unknown |
| `CABRCM_BrokerCommission.jar` | 44 | unknown |
| `CACANN_AnsiToUTF.jar` | 2 | unknown |
| `CACANN_CannexDeposits.jar` | 168 | unknown |
| `CACARD_CardManagement.jar` | 363 | unknown |
| `CACBRT_CreditBureau.jar` | 104 | unknown |
| `CACBRT_Eqlistener.jar` | 2 | unknown |
| `CACCPA_ClearingCPA.jar` | 121 | unknown |
| `CACLRC_ClearingCentralOne.jar` | 200 | unknown |
| `CACLRC_XmltoDelim.jar` | 2 | unknown |
| `CACQMG_ChequeManagement.jar` | 73 | unknown |
| `CACQOR_ChequeOrdering.jar` | 48 | unknown |
| `CACSIT_CoverdraftSweep.jar` | 74 | unknown |
| `CACUMI_CumisInterface.jar` | 33 | unknown |
| `CADEPO_CDIC.jar` | 106 | unknown |
| `CADEPO_CRAReporting.jar` | 299 | unknown |
| `CADEPO_Dormancy.jar` | 28 | unknown |
| `CADEPO_GICGurantees.jar` | 3 | unknown |
| `CADEPO_ValueAddedDeposits.jar` | 31 | unknown |
| `CAEBPS_EbillsInterface.jar` | 173 | unknown |
| `CAEBPS_EBillWSMDB.jar` | 4 | unknown |
| `CAEFPA_EFTPap.jar` | 208 | unknown |
| `CAEWDR_Foundation.jar` | 3 | unknown |
| `CAFATC_FataCrs.jar` | 3 | unknown |
| `CAGPGD_Deliquency.jar` | 27 | unknown |
| `CAGPGR_Reconciliation.jar` | 53 | unknown |
| `CAINDR_Foundation.jar` | 19 | unknown |
| `CAINTR_InteracInstant.jar` | 39 | unknown |
| `CAISIC_Foundation.jar` | 3 | unknown |
| `CAITIP_Foundation.jar` | 2 | unknown |
| `CAIVRB_Telpay.jar` | 69 | unknown |
| `CAIVRB_TelpayIVRListener.jar` | 3 | unknown |
| `CALEAS_Leasing.jar` | 17 | unknown |
| `CALEND_CostBorrowing.jar` | 9 | unknown |
| `CALEND_DischargeFee.jar` | 9 | unknown |
| `CALEND_Foundation.jar` | 9 | unknown |
| `CALEND_NonPerformingLoan.jar` | 9 | unknown |
| `CALEND_ReserveAccounts.jar` | 11 | unknown |
| `CALEND_Taxes.jar` | 15 | unknown |
| `CALENR_LendingReports.jar` | 39 | unknown |
| `CALKCL_Foundation.jar` | 2 | unknown |
| `CALOCI_LOCInsurance.jar` | 94 | unknown |
| `CALOCR_LineOfCredit.jar` | 51 | unknown |
| `CANVSN_Navision.jar` | 38 | unknown |
| `CAONBK_OnlineBanking.jar` | 419 | unknown |
| `CAPLND_ProlenderInterface.jar` | 162 | unknown |
| `CARCHQ_Foundation.jar` | 2 | unknown |
| `CARGPL_RegisteredPlans.jar` | 406 | unknown |
| `CARPSS_Foundation.jar` | 3 | unknown |
| `CASSON_SingleSignon.jar` | 4 | unknown |
| `CASYLN_SyndicatedLending.jar` | 88 | unknown |
| `CASYTC_Foundation.jar` | 2 | unknown |
| `CATCIB_TCIBOnlineBanking.jar` | 33 | unknown |
| `CATELS_TelephoneBanking.jar` | 70 | unknown |
| `CATNCL_Foundation.jar` | 3 | unknown |
| `CAUSFI_Foundation.jar` | 3 | unknown |
| `CAVLTT_ValueAddedTeller.jar` | 105 | unknown |
| `CAVNFR_Verafin.jar` | 172 | unknown |
| `CBCRRT_Foundation.jar` | 19 | unknown |
| `CBTMGT_Foundation.jar` | 28 | unknown |
| `CBVTMS_Foundation.jar` | 70 | unknown |
| `CD_Config.jar` | 13 | unknown |
| `CD_CustomerIdentification.jar` | 52 | unknown |
| `CD_ModelBank.jar` | 2 | unknown |
| `CE_CrsReporting.jar` | 59 | unknown |
| `CE_CrsReportingService.jar` | 6 | unknown |
| `CE_ModelBank.jar` | 2 | unknown |
| `CERTCQ_Foundation.jar` | 31 | unknown |
| `CG_ChargeApi.jar` | 5 | public-api, unknown |
| `CG_ChargeConfig.jar` | 93 | unknown |
| `CG_ChargeService.jar` | 6 | unknown |
| `CHSCRP_SecuritiesJournal.jar` | 25 | unknown |
| `CHSCRP_SixReporting.jar` | 97 | unknown |
| `CHSTMP_SwissStampDuty.jar` | 15 | unknown |
| `CHSTMP_SwissTaxStatement.jar` | 33 | unknown |
| `CK_Channels.jar` | 2 | unknown |
| `CK_Consent.jar` | 32 | unknown |
| `CK_ModelBank.jar` | 3 | unknown |
| `CL_Config.jar` | 8 | unknown |
| `CL_Contract.jar` | 70 | unknown |
| `CL_ModelReport.jar` | 14 | unknown |
| `CM_Contract.jar` | 51 | unknown |
| `CM_ModelBank.jar` | 9 | unknown |
| `CMBASE_AccountClabe.jar` | 6 | unknown |
| `CMBASE_CustomerAdditionalFields.jar` | 4 | unknown |
| `CMBASE_FinancialPosting.jar` | 7 | unknown |
| `CMBASE_Foundation.jar` | 28 | unknown |
| `CMBASE_IdValidation.jar` | 16 | unknown |
| `CMBASE_IdValidationHook.jar` | 3 | public-api, unknown |
| `CMBASE_InterfaceBatchExtract.jar` | 23 | unknown |
| `CMBASE_InterfaceBatchExtractHook.jar` | 3 | public-api, unknown |
| `CMBASE_MinorSavingAccount.jar` | 2 | unknown |
| `CMBASE_NonStandardMessages.jar` | 8 | unknown |
| `CMBASE_TaxCalculation.jar` | 50 | unknown |
| `COACCT_CalculationOfRates.jar` | 1 | unknown |
| `COACCT_GmfTax.jar` | 7 | unknown |
| `COACCT_ServiceCertificates.jar` | 4 | unknown |
| `CONLIB_Framework.jar` | 4 | unknown |
| `CP_Campaign.jar` | 198 | unknown |
| `CQ_Cards.jar` | 49 | unknown |
| `CQ_Channels.jar` | 4 | unknown |
| `CQ_ChequeInterfaceService.jar` | 6 | unknown |
| `CQ_ChqCollateral.jar` | 5 | unknown |
| `CQ_ChqConfig.jar` | 27 | unknown |
| `CQ_ChqEnquiry.jar` | 10 | unknown |
| `CQ_ChqFees.jar` | 22 | unknown |
| `CQ_ChqIssue.jar` | 31 | unknown |
| `CQ_ChqPaymentStop.jar` | 45 | unknown |
| `CQ_ChqStockControl.jar` | 22 | unknown |
| `CQ_ChqSubmit.jar` | 97 | unknown |
| `CQ_ModelBank.jar` | 3 | unknown |
| `CR_Analytical.jar` | 66 | unknown |
| `CR_Channels.jar` | 2 | unknown |
| `CR_ModelBank.jar` | 38 | unknown |
| `CR_Operational.jar` | 56 | unknown |
| `CS_SocialMedia.jar` | 4 | unknown |
| `CW_CashFlow.jar` | 46 | unknown |
| `CZ_AccessAndPortable.jar` | 36 | unknown |
| `CZ_CustomerActivity.jar` | 26 | unknown |
| `CZ_ErasureProcess.jar` | 64 | unknown |
| `CZ_EventStructures.jar` | 3 | unknown |
| `CZ_Framework.jar` | 98 | unknown |
| `CZ_FrameworkHook.jar` | 4 | public-api, unknown |
| `CZ_ModelBank.jar` | 4 | unknown |
| `DA_CustomerReportingService.jar` | 23 | unknown |
| `DB_DebitCollectionOrderHook.jar` | 3 | public-api, unknown |
| `DB_Foundation.jar` | 41 | unknown |
| `DC_Config.jar` | 4 | unknown |
| `DC_Contract.jar` | 45 | unknown |
| `DC_ModelBank.jar` | 3 | unknown |
| `DD_API.jar` | 7 | unknown |
| `DD_Channels.jar` | 2 | unknown |
| `DD_Config.jar` | 14 | unknown |
| `DD_Contract.jar` | 222 | unknown |
| `DD_ContractHook.jar` | 6 | public-api, unknown |
| `DD_Delivery.jar` | 4 | unknown |
| `DD_MandateMapping.jar` | 34 | unknown |
| `DD_MandateService.jar` | 8 | unknown |
| `DD_ModelBank.jar` | 4 | unknown |
| `DD_Services.jar` | 16 | unknown |
| `DF_DfMappingService.jar` | 16 | unknown |
| `DF_Foundation.jar` | 10 | unknown |
| `DI_Contract.jar` | 38 | unknown |
| `DI_ModelBank.jar` | 2 | unknown |
| `DI_Unit.jar` | 23 | unknown |
| `DL_Foundation.jar` | 50 | unknown |
| `DL_ModelBank.jar` | 5 | unknown |
| `DL_Separation.jar` | 15 | unknown |
| `DM_Foundation.jar` | 87 | unknown |
| `DM_ModelBank.jar` | 6 | unknown |
| `DP_Contract.jar` | 17 | unknown |
| `DP_Unit.jar` | 20 | unknown |
| `DS_DesignStudioInstallerService.jar` | 34 | unknown |
| `DS_Installer.jar` | 10 | unknown |
| `DS_PackageStaging.jar` | 8 | unknown |
| `DW_BiExport.jar` | 98 | unknown |
| `DW_BiExportFramework.jar` | 111 | unknown |
| `DW_BiExportLite.jar` | 9 | unknown |
| `DW_DataExportHook.jar` | 9 | public-api, unknown |
| `DW_ETL.jar` | 17 | unknown |
| `DW_Foundation.jar` | 21 | unknown |
| `EF_Config.jar` | 6 | unknown |
| `EI_ExternalSecurity.jar` | 7 | unknown |
| `EI_Foundation.jar` | 7 | unknown |
| `EI_MCI.jar` | 104 | unknown |
| `EI_ModelBank.jar` | 1 | unknown |
| `EI_PresentationServices.jar` | 30 | unknown |
| `EI_SupportUtilities.jar` | 42 | unknown |
| `ENTFEE_Framework.jar` | 1 | unknown |
| `ENTPRI_Feature.jar` | 1 | unknown |
| `ENTPRI_Framework.jar` | 4 | unknown |
| `ENTPRI_ModelBank.jar` | 16 | unknown |
| `EP_Accounting.jar` | 3 | unknown |
| `EP_Archiving.jar` | 5 | unknown |
| `EP_CamtAcctStmt.jar` | 8 | unknown |
| `EP_Config.jar` | 28 | unknown |
| `EP_Fields.jar` | 4 | unknown |
| `EP_Framework.jar` | 109 | unknown |
| `EP_IBANProcessing.jar` | 8 | unknown |
| `EP_InwardMapping.jar` | 257 | unknown |
| `EP_InwardProcess.jar` | 144 | unknown |
| `EP_Layout.jar` | 57 | unknown |
| `EP_ModelBank.jar` | 103 | unknown |
| `EP_OutwardMapping.jar` | 122 | unknown |
| `EP_OutwardProcess.jar` | 86 | unknown |
| `EP_Refusal.jar` | 21 | unknown |
| `ER_Api.jar` | 10 | unknown |
| `ER_Config.jar` | 23 | unknown |
| `ER_Contract.jar` | 61 | unknown |
| `ESBASE_ClosedDormantAccounts.jar` | 7 | unknown |
| `ESBASE_CustomerAdditionalFields.jar` | 6 | unknown |
| `ESBASE_IdValidation.jar` | 4 | unknown |
| `ESBASE_JointHolder.jar` | 4 | unknown |
| `ESBASE_MortgageNotaryFee.jar` | 5 | unknown |
| `ESBASE_NonPayableFile.jar` | 28 | unknown |
| `ESBASE_NormaExtract.jar` | 7 | unknown |
| `ESCHEQ_PaymentChequeValidation.jar` | 8 | unknown |
| `ESCLNG_BillPayments.jar` | 32 | unknown |
| `ESCLNG_ChequeDraftPayments.jar` | 48 | unknown |
| `ESCLNG_Commissions.jar` | 17 | unknown |
| `ESCLNG_EntityInformation.jar` | 22 | unknown |
| `ESCLNG_MandateAccountForward.jar` | 12 | unknown |
| `ESCLNG_MiscellaneousPayments.jar` | 85 | unknown |
| `ESCLNG_NonResidentPayments.jar` | 19 | unknown |
| `ESCROW_Analysis.jar` | 26 | unknown |
| `ESCROW_Foundation.jar` | 80 | unknown |
| `ESCROW_Interface.jar` | 17 | unknown |
| `ESCROW_PaymentProcessing.jar` | 64 | unknown |
| `ESFUND_AcceptRejectTraspasos.jar` | 18 | unknown |
| `ESFUND_DailyBrokerOrderReport.jar` | 11 | unknown |
| `ESFUND_InternalAsset.jar` | 2 | unknown |
| `ESFXOP_SpainForeignExchangeOperations.jar` | 2 | unknown |
| `ESIBER_AccountVerification.jar` | 31 | unknown |
| `ESIBER_AccountVerificationApi.jar` | 14 | unknown |
| `ESIBER_InstSettlement.jar` | 17 | unknown |
| `ESIBER_OrderAccounts.jar` | 13 | unknown |
| `ESIMSR_BenifitPayments.jar` | 74 | unknown |
| `ESLEND_AprCalculation.jar` | 6 | unknown |
| `ESLEND_Morosity.jar` | 1 | unknown |
| `ESLEND_MortgageAct.jar` | 20 | unknown |
| `ESMINR_NonEmancipatedMinors.jar` | 5 | unknown |
| `ESMINR_YoungAccount.jar` | 3 | unknown |
| `ESMNDT_AccountForwarding.jar` | 3 | unknown |
| `ESMNDT_SpanishFiscalNumber.jar` | 2 | unknown |
| `ESPVRC_Provisioning.jar` | 12 | unknown |
| `ESRDIN_RoundingInterest.jar` | 3 | unknown |
| `ESSPIN_EmbargoInterface.jar` | 54 | unknown |
| `ESSPIN_PayrollPayments.jar` | 11 | unknown |
| `ESSPIN_SocialInsurance.jar` | 45 | unknown |
| `ESSPIN_TgssBenefitsPayout.jar` | 24 | unknown |
| `ESSPIN_TgssDomiciledPayments.jar` | 7 | unknown |
| `ESTELL_NonCustomerCash.jar` | 22 | unknown |
| `ESTELL_TellerReport.jar` | 9 | unknown |
| `ESTXPY_SocialSecurityTax.jar` | 84 | unknown |
| `ESWHTX_WithHoldingTax.jar` | 6 | unknown |
| `ET_Contract.jar` | 100 | unknown |
| `ETBROP_CashiersPaymentOrderDD.jar` | 25 | unknown |
| `ETBROP_ChequeDateValidation.jar` | 2 | unknown |
| `ETBROP_LocalMoneyTransferService.jar` | 29 | unknown |
| `ETFXOP_ForexPermit.jar` | 41 | unknown |
| `ETFXOP_RetentionAccounts.jar` | 20 | unknown |
| `EU_AccountEuroConversion.jar` | 60 | unknown |
| `EU_ApplicationEuroConversion.jar` | 63 | unknown |
| `EU_Config.jar` | 26 | unknown |
| `EU_LocalCcyConversion.jar` | 74 | unknown |
| `EUIFGT_InvestmentFundGuarantee.jar` | 17 | unknown |
| `EV_Framework.jar` | 144 | unknown |
| `EW_HostCompare.jar` | 16 | unknown |
| `EW_InitialLoad.jar` | 285 | unknown |
| `EW_Integration.jar` | 9 | unknown |
| `EW_ModelBank.jar` | 11 | unknown |
| `EW_OrderCapture.jar` | 4 | unknown |
| `EW_TdsT24Interface.jar` | 10 | unknown |
| `FA_BalanceAggregation.jar` | 22 | unknown |
| `FA_Config.jar` | 23 | unknown |
| `FA_CustomerIdentification.jar` | 81 | unknown |
| `FA_ModelBank.jar` | 16 | unknown |
| `FD_Accounting.jar` | 8 | unknown |
| `FD_Accrual.jar` | 10 | unknown |
| `FD_Config.jar` | 69 | unknown |
| `FD_Contract.jar` | 52 | unknown |
| `FD_Delivery.jar` | 5 | unknown |
| `FD_Fees.jar` | 11 | unknown |
| `FD_Foundation.jar` | 16 | unknown |
| `FD_Interest.jar` | 19 | unknown |
| `FD_ModelBank.jar` | 3 | unknown |
| `FD_Pooling.jar` | 18 | unknown |
| `FD_Renewals.jar` | 8 | unknown |
| `FD_Reports.jar` | 21 | unknown |
| `FD_Schedules.jar` | 53 | unknown |
| `FE_FatcaReporting.jar` | 83 | unknown |
| `FE_ModelBank.jar` | 6 | unknown |
| `FIACCT_ASPFoundation.jar` | 33 | unknown |
| `FIACCT_ItellaProcessing.jar` | 8 | unknown |
| `FIBASE_Foundation.jar` | 4 | unknown |
| `FICOLL_AutomaticRenewalProcess.jar` | 13 | unknown |
| `FICOLL_Collateral.jar` | 11 | unknown |
| `FICOLL_CollateralHook.jar` | 3 | public-api, unknown |
| `FICOLL_CollateralLease.jar` | 6 | unknown |
| `FICOLL_Foundation.jar` | 20 | unknown |
| `FICOLL_GuarantiaGuarantee.jar` | 31 | unknown |
| `FICOLL_LTVProcessing.jar` | 8 | unknown |
| `FICOLL_RiskViewSimulation.jar` | 11 | unknown |
| `FICOLL_StatisticsProcessing.jar` | 18 | unknown |
| `FICUST_AccountLimit.jar` | 10 | unknown |
| `FICUST_CustomerOnboarding.jar` | 8 | unknown |
| `FICUST_CustomerProcessing.jar` | 15 | unknown |
| `FICUST_IbanSsnNo.jar` | 9 | unknown |
| `FIIPMT_IncomingPayments.jar` | 16 | unknown |
| `FILEND_CreditLossProcessing.jar` | 8 | unknown |
| `FILEND_ForbearanceProcessing.jar` | 14 | unknown |
| `FILEND_LegalFeeCap.jar` | 16 | unknown |
| `FILEND_MinimumOffsetPeriod.jar` | 3 | unknown |
| `FILEND_PenaltyInterestCalculation.jar` | 2 | unknown |
| `FINEXT_ATMRECON.jar` | 46 | unknown |
| `FINEXT_CBR.jar` | 42 | unknown |
| `FIPAVL_Foundation.jar` | 24 | unknown |
| `FIPAVL_GenerateDealSlip.jar` | 2 | unknown |
| `FISTLN_LoansOrigination.jar` | 23 | unknown |
| `FISTLN_StudentLoan.jar` | 20 | unknown |
| `FIVOCE_InvoicingCreditNote.jar` | 80 | unknown |
| `FIXAMT_Config.jar` | 49 | unknown |
| `FIXAMT_ModelBank.jar` | 4 | unknown |
| `FL_Framework.jar` | 13 | unknown |
| `FL_ModelBank.jar` | 24 | unknown |
| `FNDINV_Foundation.jar` | 22 | unknown |
| `FX_Accrual.jar` | 18 | unknown |
| `FX_Archiving.jar` | 6 | unknown |
| `FX_BulkOrder.jar` | 29 | unknown |
| `FX_ClosingGroup.jar` | 6 | unknown |
| `FX_Config.jar` | 23 | unknown |
| `FX_Confirmations.jar` | 14 | unknown |
| `FX_Contract.jar` | 90 | unknown |
| `FX_Delivery.jar` | 7 | unknown |
| `FX_Foundation.jar` | 18 | unknown |
| `FX_LimitOrder.jar` | 13 | unknown |
| `FX_ModelBank.jar` | 31 | unknown |
| `FX_Options.jar` | 10 | unknown |
| `FX_PositionAndReval.jar` | 29 | unknown |
| `FX_Reports.jar` | 32 | unknown |
| `FX_Swaps.jar` | 11 | unknown |
| `FX_Trading.jar` | 43 | unknown |
| `GA_Foundation.jar` | 15 | unknown |
| `GLROUP_GLRollup.jar` | 17 | unknown |
| `GTMTCH_DataExtraction.jar` | 6 | unknown |
| `I9_Config.jar` | 16 | unknown |
| `I9_ModelBank.jar` | 3 | unknown |
| `I9_Valuation.jar` | 42 | unknown |
| `IA_Accounting.jar` | 95 | unknown |
| `IA_AccountingHook.jar` | 5 | public-api, unknown |
| `IA_Config.jar` | 116 | unknown |
| `IA_ModelBank.jar` | 7 | unknown |
| `IA_NpvService.jar` | 6 | unknown |
| `IA_Valuation.jar` | 31 | unknown |
| `IA_ValuationApi.jar` | 4 | public-api, unknown |
| `IB_Foundation.jar` | 13 | unknown |
| `IC_Config.jar` | 76 | unknown |
| `IC_GroupAccrual.jar` | 41 | unknown |
| `IC_InterestAndCapitalisation.jar` | 274 | unknown |
| `IC_ModelBank.jar` | 24 | unknown |
| `IC_OtherInterest.jar` | 110 | unknown |
| `IC_Reports.jar` | 4 | unknown |
| `ID_ModelBank.jar` | 43 | unknown |
| `ID_PdsConfig.jar` | 65 | unknown |
| `ID_PdsProcess.jar` | 400 | unknown |
| `IDFXLI_Foundation.jar` | 11 | unknown |
| `IF_FlowCatalog.jar` | 39 | unknown |
| `IF_InboundSecurityService.jar` | 6 | unknown |
| `IF_InflowCatalog.jar` | 13 | unknown |
| `IF_InflowService.jar` | 69 | unknown |
| `IF_IntegrationFlowService.jar` | 74 | unknown |
| `IF_IntegrationFrameworkHook.jar` | 4 | public-api, unknown |
| `IF_IntegrationFrameworkService.jar` | 60 | unknown |
| `IF_IntegrationLandscapeService.jar` | 104 | unknown |
| `IF_IntegrationService.jar` | 45 | unknown |
| `IF_RuntimeFramework.jar` | 89 | unknown |
| `IH_API.jar` | 5 | unknown |
| `IH_Config.jar` | 5 | unknown |
| `IH_ModelBank.jar` | 2 | unknown |
| `IM_Foundation.jar` | 13 | unknown |
| `IM_ModelBank.jar` | 6 | unknown |
| `IS_Config.jar` | 56 | unknown |
| `IS_ModelBank.jar` | 112 | unknown |
| `IS_Payment.jar` | 143 | unknown |
| `IS_Purchase.jar` | 138 | unknown |
| `IX_API.jar` | 19 | unknown |
| `IX_Config.jar` | 13 | unknown |
| `IX_XmlStatementHook.jar` | 3 | public-api, unknown |
| `IX_XmlStatementService.jar` | 6 | unknown |
| `IX_XmlStmtPrinting.jar` | 43 | unknown |
| `JX_ContagionProcess.jar` | 6 | unknown |
| `LBACTR_AccountNumbering.jar` | 8 | unknown |
| `LBACTR_Foundation.jar` | 26 | unknown |
| `LBCORP_Foundation.jar` | 6 | unknown |
| `LBNCDR_Foundation.jar` | 82 | unknown |
| `LBRPTS_Foundation.jar` | 15 | unknown |
| `LBRPTS_HonoraryCalculation.jar` | 11 | unknown |
| `LC_Accounting.jar` | 46 | unknown |
| `LC_Channels.jar` | 15 | unknown |
| `LC_Config.jar` | 41 | unknown |
| `LC_Contract.jar` | 267 | unknown |
| `LC_Delivery.jar` | 40 | unknown |
| `LC_Fees.jar` | 47 | unknown |
| `LC_Foundation.jar` | 66 | unknown |
| `LC_LetterOfCreditHook.jar` | 6 | public-api, unknown |
| `LC_Limits.jar` | 14 | unknown |
| `LC_Maturity.jar` | 12 | unknown |
| `LC_ModelBank.jar` | 117 | unknown |
| `LC_Revolving.jar` | 6 | unknown |
| `LC_Schedules.jar` | 35 | unknown |
| `LE_Framework.jar` | 29 | unknown |
| `LENDMS_ModelBank.jar` | 1 | unknown |
| `LENINS_Insurance.jar` | 12 | unknown |
| `LENINS_InsuranceHook.jar` | 3 | public-api, unknown |
| `LENREN_LoanRenewalHook.jar` | 3 | public-api, unknown |
| `LENREN_Renewal.jar` | 41 | unknown |
| `LI_CashFlow.jar` | 12 | unknown |
| `LI_Collateral.jar` | 80 | unknown |
| `LI_Config.jar` | 169 | unknown |
| `LI_Contract.jar` | 43 | unknown |
| `LI_Events.jar` | 12 | unknown |
| `LI_ExternalTxn.jar` | 13 | unknown |
| `LI_GroupLimit.jar` | 66 | unknown |
| `LI_LimitApi.jar` | 5 | public-api, unknown |
| `LI_LimitTransaction.jar` | 151 | unknown |
| `LI_ModelBank.jar` | 73 | unknown |
| `LI_Reports.jar` | 72 | unknown |
| `LI_RestrictionLimit.jar` | 12 | unknown |
| `LKBASE_Foundation.jar` | 13 | unknown |
| `LKFXTR_ForexTransactionReporting.jar` | 11 | unknown |
| `LKIFRS_Foundation.jar` | 33 | unknown |
| `LKLEND_Foundation.jar` | 12 | unknown |
| `LKPVCO_ProvisioningandCollateral.jar` | 36 | unknown |
| `LKTDFN_Foundation.jar` | 4 | unknown |
| `LKWHTX_Foundation.jar` | 16 | unknown |
| `LMSCOL_Foundation.jar` | 22 | unknown |
| `LNRDRW_Foundation.jar` | 3 | unknown |
| `LNSECU_Framework.jar` | 1 | unknown |
| `LNSECU_ModelBank.jar` | 1 | unknown |
| `LNTRAD_Fees.jar` | 10 | unknown |
| `LNTRAD_Framework.jar` | 52 | unknown |
| `LNTRAD_ModelBank.jar` | 4 | unknown |
| `LQ_LiquidityManagement.jar` | 19 | unknown |
| `LQ_ModelBank.jar` | 3 | unknown |
| `MC_CompanyCreation.jar` | 45 | unknown |
| `MCYAAR_Framework.jar` | 19 | unknown |
| `MCYAAR_ModelBank.jar` | 5 | unknown |
| `MD_Accounting.jar` | 6 | unknown |
| `MD_Channels.jar` | 5 | unknown |
| `MD_COB.jar` | 12 | unknown |
| `MD_Config.jar` | 28 | unknown |
| `MD_Contract.jar` | 129 | unknown |
| `MD_Delivery.jar` | 10 | unknown |
| `MD_Fees.jar` | 49 | unknown |
| `MD_Foundation.jar` | 45 | unknown |
| `MD_Limits.jar` | 8 | unknown |
| `MD_MdDealHook.jar` | 3 | public-api, unknown |
| `MD_ModelBank.jar` | 41 | unknown |
| `MD_Schedules.jar` | 9 | unknown |
| `MDA_EndToEnd.jar` | 7 | unknown |
| `MDLACC_Accounts.jar` | 4 | unknown |
| `MDLLIM_Limits.jar` | 3 | unknown |
| `MDLMKT_MarketData.jar` | 13 | unknown |
| `MDLPTY_Party.jar` | 14 | unknown |
| `MDLREF_Iban.jar` | 9 | unknown |
| `MDLREF_ReferenceData.jar` | 20 | unknown |
| `MDLREF_ReferenceDirectory.jar` | 10 | unknown |
| `MF_Config.jar` | 23 | unknown |
| `MF_Contract.jar` | 23 | unknown |
| `MF_Fees.jar` | 13 | unknown |
| `MF_NAVCalculation.jar` | 18 | unknown |
| `MF_Orders.jar` | 19 | unknown |
| `MF_PreOrders.jar` | 10 | unknown |
| `MG_Accounting.jar` | 6 | unknown |
| `MG_Archiving.jar` | 5 | unknown |
| `MG_Config.jar` | 30 | unknown |
| `MG_Contract.jar` | 29 | unknown |
| `MG_Delivery.jar` | 7 | unknown |
| `MG_Foundation.jar` | 22 | unknown |
| `MG_Interest.jar` | 14 | unknown |
| `MG_Interface.jar` | 2 | unknown |
| `MG_ModelBank.jar` | 5 | unknown |
| `MG_Payment.jar` | 11 | unknown |
| `MG_RateChange.jar` | 17 | unknown |
| `MG_Reports.jar` | 7 | unknown |
| `MG_Schedules.jar` | 33 | unknown |
| `MI_AverageBalances.jar` | 10 | unknown |
| `MI_BalanceMovementBuild.jar` | 19 | unknown |
| `MI_Entries.jar` | 69 | unknown |
| `MI_ModelBank.jar` | 4 | unknown |
| `MI_Reports.jar` | 63 | unknown |
| `MIFDII_IRP.jar` | 64 | unknown |
| `MK_Config.jar` | 1 | unknown |
| `ML_Chinese.jar` | 1 | unknown |
| `ML_English.jar` | 1 | unknown |
| `ML_French.jar` | 1 | unknown |
| `ML_German.jar` | 1 | unknown |
| `ML_Spanish.jar` | 1 | unknown |
| `MM_Archiving.jar` | 6 | unknown |
| `MM_Confirmations.jar` | 20 | unknown |
| `MM_Contract.jar` | 101 | unknown |
| `MM_Delivery.jar` | 14 | unknown |
| `MM_Fiduciary.jar` | 30 | unknown |
| `MM_Foundation.jar` | 16 | unknown |
| `MM_Interest.jar` | 29 | unknown |
| `MM_PaymentAndReceipt.jar` | 18 | unknown |
| `MM_Reports.jar` | 8 | unknown |
| `MM_Schedules.jar` | 27 | unknown |
| `MO_Framework.jar` | 17 | unknown |
| `MO_ModelBank.jar` | 24 | unknown |
| `MSFRAM_Framework.jar` | 3 | unknown |
| `MT_Framework.jar` | 47 | unknown |
| `MT_MultiTenantService.jar` | 6 | unknown |
| `MV_Config.jar` | 24 | unknown |
| `MV_ModelBank.jar` | 2 | unknown |
| `MV_Valuation.jar` | 9 | unknown |
| `NA_Framework.jar` | 78 | unknown |
| `NACUST_Covenants.jar` | 14 | unknown |
| `NACUST_CustomerHolds.jar` | 52 | unknown |
| `NACUST_CustomerMessages.jar` | 16 | unknown |
| `NACUST_Foundation.jar` | 44 | unknown |
| `NAPVPT_Interface.jar` | 30 | unknown |
| `ND_Config.jar` | 12 | unknown |
| `ND_Contract.jar` | 46 | unknown |
| `ND_Delivery.jar` | 2 | unknown |
| `ND_Foundation.jar` | 2 | unknown |
| `ND_Reports.jar` | 3 | unknown |
| `ND_Trading.jar` | 24 | unknown |
| `NR_Contract.jar` | 22 | unknown |
| `NR_ModelBank.jar` | 9 | unknown |
| `NSFDES_Alerts.jar` | 14 | unknown |
| `NSFDES_DeskMgmt.jar` | 16 | unknown |
| `NSFDES_Foundation.jar` | 6 | unknown |
| `NSFDES_OtherExceptions.jar` | 17 | unknown |
| `NSFDES_Queue.jar` | 49 | unknown |
| `OA_Decision.jar` | 64 | unknown |
| `OA_Extraction.jar` | 16 | unknown |
| `OA_Framework.jar` | 231 | unknown |
| `OA_PolicyRules.jar` | 18 | unknown |
| `OA_Stages.jar` | 31 | unknown |
| `OA_Status.jar` | 150 | unknown |
| `OC_IntegrationHook.jar` | 3 | public-api, unknown |
| `OC_Parameters.jar` | 33 | unknown |
| `OC_Reporting.jar` | 131 | unknown |
| `OP_ModelBank.jar` | 40 | unknown |
| `OTREMI_Foundation.jar` | 31 | unknown |
| `OV_Config.jar` | 29 | unknown |
| `OX_Config.jar` | 10 | unknown |
| `OX_ModelBank.jar` | 2 | unknown |
| `OX_ObligorHook.jar` | 5 | public-api, unknown |
| `OX_ObligorObject.jar` | 56 | unknown |
| `PA_Channels.jar` | 2 | unknown |
| `PA_Consent.jar` | 15 | unknown |
| `PA_Contract.jar` | 12 | unknown |
| `PA_ErrorCodes.jar` | 1 | unknown |
| `PA_ModelBank.jar` | 1 | unknown |
| `PA_Reports.jar` | 1 | unknown |
| `PA_Versions.jar` | 1 | unknown |
| `PAYRAC_Accounts.jar` | 18 | unknown |
| `PC_Contract.jar` | 48 | unknown |
| `PC_IFConfig.jar` | 2 | unknown |
| `PD_AccountLimit.jar` | 11 | unknown |
| `PD_Config.jar` | 70 | unknown |
| `PD_Contract.jar` | 35 | unknown |
| `PD_Delivery.jar` | 11 | unknown |
| `PD_Foundation.jar` | 14 | unknown |
| `PD_Interest.jar` | 12 | unknown |
| `PD_Interface.jar` | 16 | unknown |
| `PD_ModelBank.jar` | 5 | unknown |
| `PD_OPProcess.jar` | 9 | unknown |
| `PD_Repayment.jar` | 37 | unknown |
| `PD_Schedules.jar` | 18 | unknown |
| `PD_Suspension.jar` | 26 | unknown |
| `PEACCT_AccountCCI.jar` | 2 | unknown |
| `PEACCT_CalculationOfRates.jar` | 6 | unknown |
| `PEBASE_CustomerCreation.jar` | 18 | unknown |
| `PEMINT_CamtAcctStmt.jar` | 2 | unknown |
| `PEMINT_DDAService.jar` | 31 | unknown |
| `PEMINT_StandaloneInterfaceService.jar` | 8 | unknown |
| `PETAXS_TaxCalculation.jar` | 8 | unknown |
| `PF_API.jar` | 3 | unknown |
| `PF_Config.jar` | 59 | unknown |
| `PH_LocalClearingGUI.jar` | 8 | unknown |
| `PI_Channels.jar` | 3 | unknown |
| `PI_Config.jar` | 49 | unknown |
| `PI_Contract.jar` | 203 | unknown |
| `PI_Delivery.jar` | 12 | unknown |
| `PI_ModelBank.jar` | 22 | unknown |
| `PI_PaymentOrderHook.jar` | 6 | public-api, unknown |
| `PI_PaymentOrderLifecycleHook.jar` | 7 | public-api, unknown |
| `PI_PaymentService.jar` | 10 | unknown |
| `PM_Config.jar` | 63 | unknown |
| `PM_Engine.jar` | 82 | unknown |
| `PM_ModelBank.jar` | 3 | unknown |
| `PM_PositionHook.jar` | 6 | public-api, unknown |
| `PM_ReportingService.jar` | 16 | unknown |
| `PM_Reports.jar` | 68 | unknown |
| `PO_AccountPoolHook.jar` | 3 | public-api, unknown |
| `PO_Cashpooling.jar` | 182 | unknown |
| `PO_ModelBank.jar` | 8 | unknown |
| `PPAACH_ClearingFramework.jar` | 22 | unknown |
| `PPADBR_DebinRegistration.jar` | 15 | unknown |
| `PPADBR_DebinRegnInterfaceService.jar` | 8 | unknown |
| `PPADEB_DebitOrder.jar` | 38 | unknown |
| `PPADEB_DebitOrderHook.jar` | 4 | public-api, unknown |
| `PPADEB_DebitOrderInterfaceService.jar` | 8 | unknown |
| `PPAIMT_ClearingFramework.jar` | 6 | unknown |
| `PPARMS_Foundation.jar` | 13 | unknown |
| `PPAUBD_Foundation.jar` | 2 | unknown |
| `PPAUBP_ClearingFramework.jar` | 11 | unknown |
| `PPAUNC_Foundation.jar` | 20 | unknown |
| `PPBACS_Foundation.jar` | 8 | unknown |
| `PPBECS_Foundation.jar` | 14 | unknown |
| `PPC2BM_Foundation.jar` | 2 | unknown |
| `PPCAIC_Foundation.jar` | 16 | unknown |
| `PPCAIC_InteracAccount.jar` | 4 | unknown |
| `PPCHAP_Foundation.jar` | 7 | unknown |
| `PPCLIT_Foundation.jar` | 7 | unknown |
| `PPESIC_Foundation.jar` | 5 | unknown |
| `PPEWSP_Foundation.jar` | 11 | unknown |
| `PPFEDW_Foundation.jar` | 6 | unknown |
| `PPHIG2_Foundation.jar` | 11 | unknown |
| `PPHINS_Foundation.jar` | 5 | unknown |
| `PPHKCQ_Foundation.jar` | 9 | unknown |
| `PPHKCX_Foundation.jar` | 4 | unknown |
| `PPICEF_Foundation.jar` | 5 | unknown |
| `PPIEBA_Foundation.jar` | 5 | unknown |
| `PPIHCT_Foundation.jar` | 2 | unknown |
| `PPINCT_Foundation.jar` | 4 | unknown |
| `PPINIP_Foundation.jar` | 9 | unknown |
| `PPINNP_Foundation.jar` | 16 | unknown |
| `PPINRX_Foundation.jar` | 17 | unknown |
| `PPINST_Foundation.jar` | 2 | unknown |
| `PPISIP_Foundation.jar` | 6 | unknown |
| `PPISOX_Foundation.jar` | 2 | unknown |
| `PPITIP_Foundation.jar` | 10 | unknown |
| `PPLBCQ_Foundation.jar` | 16 | unknown |
| `PPLBNC_Foundation.jar` | 3 | unknown |
| `PPLCIT_Foundation.jar` | 9 | unknown |
| `PPLKRT_ClearingFramework.jar` | 2 | unknown |
| `PPLNCL_ClearingFramework.jar` | 12 | unknown |
| `PPMASV_Foundation.jar` | 11 | unknown |
| `PPNPCT_Foundation.jar` | 8 | unknown |
| `PPRPCL_Foundation.jar` | 13 | unknown |
| `PPRPCQ_Foundation.jar` | 11 | unknown |
| `PPSAAS_Foundation.jar` | 2 | unknown |
| `PPSARI_Foundation.jar` | 4 | unknown |
| `PPSICH_Foundation.jar` | 15 | unknown |
| `PPSPCT_Foundation.jar` | 2 | unknown |
| `PPSSIU_Foundation.jar` | 4 | unknown |
| `PPSWCQ_Foundation.jar` | 2 | unknown |
| `PPSWCR_Foundation.jar` | 8 | unknown |
| `PPSWMX_CancellationRequestService.jar` | 10 | unknown |
| `PPSWMX_Foundation.jar` | 10 | unknown |
| `PPSYGM_ClearingFramework.jar` | 5 | unknown |
| `PPSYTC_ClearingFramework.jar` | 16 | unknown |
| `PPTGMX_Foundation.jar` | 16 | unknown |
| `PPTNCL_ChequeClearing.jar` | 39 | unknown |
| `PPTNCL_Foundation.jar` | 18 | unknown |
| `PPTNCL_MandateFileProcessing.jar` | 11 | unknown |
| `PPUFPS_Foundation.jar` | 4 | unknown |
| `PPUKCX_Foundation.jar` | 6 | unknown |
| `PPUSFI_FednowService.jar` | 6 | unknown |
| `PPUSFI_Foundation.jar` | 11 | unknown |
| `PPVIBR_Foundation.jar` | 4 | unknown |
| `PR_Framework.jar` | 14 | unknown |
| `PR_ModelBank.jar` | 3 | unknown |
| `PRDLMT_ProductLimit.jar` | 19 | unknown |
| `PROMOS_Framework.jar` | 7 | unknown |
| `PSINCV_CountryRules.jar` | 7 | unknown |
| `PT_Contract.jar` | 18 | unknown |
| `PT_Unit.jar` | 14 | unknown |
| `PV_Config.jar` | 98 | unknown |
| `PV_ContractAssessmentHook.jar` | 4 | public-api, unknown |
| `PV_DodRules.jar` | 40 | unknown |
| `PV_ModelBank.jar` | 10 | unknown |
| `PV_ProvisionManagementHook.jar` | 7 | public-api, unknown |
| `PW_API.jar` | 7 | unknown |
| `PW_Engine.jar` | 46 | unknown |
| `PW_Foundation.jar` | 157 | unknown |
| `PW_HumanTaskService.jar` | 30 | unknown |
| `PW_Mapping.jar` | 11 | unknown |
| `PW_ModelBank.jar` | 44 | unknown |
| `PW_ProcessEngineService.jar` | 16 | unknown |
| `PW_ProcessHook.jar` | 3 | public-api, unknown |
| `PX_Config.jar` | 15 | unknown |
| `PX_Framework.jar` | 12 | unknown |
| `PX_ModelBank.jar` | 15 | unknown |
| `PY_API.jar` | 8 | unknown |
| `PY_Config.jar` | 26 | unknown |
| `PY_ModelBank.jar` | 9 | unknown |
| `PY_Service.jar` | 9 | unknown |
| `PZ_Config.jar` | 7 | unknown |
| `PZ_Consent.jar` | 21 | unknown |
| `PZ_ModelBank.jar` | 34 | unknown |
| `QI_Config.jar` | 26 | unknown |
| `QI_CustomerIdentification.jar` | 6 | unknown |
| `QI_ModelBank.jar` | 5 | unknown |
| `QI_Reporting.jar` | 36 | unknown |
| `RC_Capture.jar` | 10 | unknown |
| `RC_Config.jar` | 38 | unknown |
| `RC_ContractHook.jar` | 12 | public-api, unknown |
| `RC_Interface.jar` | 4 | unknown |
| `RC_TransactionCycler.jar` | 74 | unknown |
| `RD_API.jar` | 11 | unknown |
| `RD_Config.jar` | 88 | unknown |
| `RD_Contract.jar` | 3 | unknown |
| `RD_ModelBank.jar` | 3 | unknown |
| `RD_Services.jar` | 20 | unknown |
| `RE_AccountingReportApi.jar` | 4 | public-api, unknown |
| `RE_ConBalanceUpdates.jar` | 72 | unknown |
| `RE_Config.jar` | 70 | unknown |
| `RE_Consolidation.jar` | 153 | unknown |
| `RE_ConsolidationRegeneration.jar` | 24 | unknown |
| `RE_ContractBalanceApi.jar` | 3 | public-api, unknown |
| `RE_EcbBalanceService.jar` | 6 | unknown |
| `RE_FinancialReportingService.jar` | 14 | unknown |
| `RE_IFConfig.jar` | 47 | unknown |
| `RE_ModelBank.jar` | 20 | unknown |
| `RE_ReportExtraction.jar` | 43 | unknown |
| `RE_ReportGeneration.jar` | 160 | unknown |
| `RE_YearEnd.jar` | 38 | unknown |
| `RETDEP_ModelBank.jar` | 2 | unknown |
| `RETGEN_ModelBank.jar` | 8 | unknown |
| `RETGEN_Statement.jar` | 5 | unknown |
| `RETLEN_LendingStatement.jar` | 2 | unknown |
| `RETLEN_ModelBank.jar` | 2 | unknown |
| `RF_Foundation.jar` | 138 | unknown |
| `RF_RTPInterfaceService.jar` | 10 | unknown |
| `RF_RTPOrderHook.jar` | 5 | public-api, unknown |
| `RFPYEU_Foundation.jar` | 8 | unknown |
| `RFPYSA_Foundation.jar` | 4 | unknown |
| `RFPYUK_Foundation.jar` | 8 | unknown |
| `RLGAAP_CollateralBorrowings.jar` | 18 | unknown |
| `RLGAAP_CollateralReports.jar` | 8 | unknown |
| `RLGAAP_Foundation.jar` | 3 | unknown |
| `RLGAAP_GLAverageBalance.jar` | 1 | unknown |
| `RLGAAP_RelatedPartyTransaction.jar` | 1 | unknown |
| `RLGAAP_Reports.jar` | 4 | unknown |
| `RMMNTC_Foundation.jar` | 41 | unknown |
| `RP_COB.jar` | 42 | unknown |
| `RP_Config.jar` | 23 | unknown |
| `RP_Contract.jar` | 78 | unknown |
| `RP_Foundation.jar` | 6 | unknown |
| `RP_ModelBank.jar` | 4 | unknown |
| `RR_Foundation.jar` | 18 | unknown |
| `RR_ModelBank.jar` | 7 | unknown |
| `RR_ReplicationService.jar` | 6 | unknown |
| `RS_Sweeping.jar` | 24 | unknown |
| `RT_BalanceAggregation.jar` | 66 | unknown |
| `RT_Config.jar` | 28 | unknown |
| `RT_IndiciaChecks.jar` | 19 | unknown |
| `RT_ModelBank.jar` | 2 | unknown |
| `RT_OpenBanking.jar` | 10 | unknown |
| `RT_RegAcctng.jar` | 12 | unknown |
| `RT_Regulation.jar` | 13 | unknown |
| `RTACMS_ModelBank.jar` | 4 | unknown |
| `RTADMS_ModelBank.jar` | 1 | unknown |
| `RTGSSW_Foundation.jar` | 2 | unknown |
| `RV_Framework.jar` | 2 | unknown |
| `RW_Framework.jar` | 4 | unknown |
| `SF_Foundation.jar` | 30 | unknown |
| `SFCONF_Config.jar` | 5 | unknown |
| `SFCONF_Contract.jar` | 8 | unknown |
| `SFCONF_Service.jar` | 4 | unknown |
| `SI_Config.jar` | 1 | unknown |
| `SL_Accounting.jar` | 17 | unknown |
| `SL_BuySell.jar` | 24 | unknown |
| `SL_Config.jar` | 27 | unknown |
| `SL_Contract.jar` | 168 | unknown |
| `SL_Delivery.jar` | 37 | unknown |
| `SL_Diary.jar` | 7 | unknown |
| `SL_Facility.jar` | 85 | unknown |
| `SL_Fees.jar` | 32 | unknown |
| `SL_Foundation.jar` | 28 | unknown |
| `SL_Interest.jar` | 60 | unknown |
| `SL_Loans.jar` | 27 | unknown |
| `SL_ModelBank.jar` | 41 | unknown |
| `SL_ODSettlement.jar` | 11 | unknown |
| `SL_Overdue.jar` | 31 | unknown |
| `SL_Presyndication.jar` | 20 | unknown |
| `SL_Rates.jar` | 25 | unknown |
| `SL_Repayment.jar` | 19 | unknown |
| `SL_Reports.jar` | 4 | unknown |
| `SL_Rollover.jar` | 29 | unknown |
| `SL_Schedules.jar` | 64 | unknown |
| `SP_Foundation.jar` | 123 | unknown |
| `SP_ModelBank.jar` | 2 | unknown |
| `SWFTAL_Foundation.jar` | 16 | unknown |
| `SWFTAL_FoundationApi.jar` | 3 | public-api, unknown |
| `SY_Config.jar` | 63 | unknown |
| `SY_CorporateAction.jar` | 19 | unknown |
| `SY_Event.jar` | 57 | unknown |
| `SY_Foundation.jar` | 83 | unknown |
| `SY_ModelBank.jar` | 6 | unknown |
| `SY_Portfolio.jar` | 2 | unknown |
| `SY_Reports.jar` | 8 | unknown |
| `SY_Trading.jar` | 40 | unknown |
| `SY_Unit.jar` | 40 | unknown |
| `SZ_Customer.jar` | 10 | unknown |
| `SZ_ModelBank.jar` | 2 | unknown |
| `T1_ModelBank.jar` | 4 | unknown |
| `t24-AC_DDAService-Data.jar` | 89 | unknown |
| `t24-AC_DDAService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-DF_DfMappingService-Data.jar` | 23 | unknown |
| `t24-DF_DfMappingService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-DS_DesignStudioInstallerService-Data.jar` | 10 | unknown |
| `t24-DS_DesignStudioInstallerService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_AuthenticationService-Data.jar` | 16 | unknown |
| `t24-EB_AuthenticationService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_AuthorizationService-Data.jar` | 11 | unknown |
| `t24-EB_AuthorizationService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_AutomationService-Data.jar` | 9 | unknown |
| `t24-EB_AutomationService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_CatalogService-Data.jar` | 97 | unknown |
| `t24-EB_CatalogService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_EntitlementService-Data.jar` | 3 | unknown |
| `t24-EB_EntitlementService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_OFSConnectorService-Data.jar` | 4 | unknown |
| `t24-EB_OFSConnectorService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_ResourceProviderService-Data.jar` | 100 | unknown |
| `t24-EB_ResourceProviderService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-EB_Sms-Data.jar` | 20 | unknown |
| `t24-EB_Sms-t24service.jar` | 4 | public-api, unknown |
| `t24-IF_InboundSecurityService-Data.jar` | 5 | unknown |
| `t24-IF_InboundSecurityService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-IF_InflowService-Data.jar` | 42 | unknown |
| `t24-IF_InflowService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-IF_IntegrationFlowService-Data.jar` | 40 | unknown |
| `t24-IF_IntegrationFlowService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-IF_IntegrationFrameworkService-Data.jar` | 81 | record-model, unknown |
| `t24-IF_IntegrationFrameworkService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-IF_IntegrationLandscapeService-Data.jar` | 64 | unknown |
| `t24-IF_IntegrationLandscapeService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-PP_TraFixService-Data.jar` | 35 | unknown |
| `t24-PP_TraFixService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-PW_HumanTaskService-Data.jar` | 25 | unknown |
| `t24-PW_HumanTaskService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-PW_ProcessEngineService-Data.jar` | 26 | unknown |
| `t24-PW_ProcessEngineService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-RR_ReplicationService-Data.jar` | 3 | unknown |
| `t24-RR_ReplicationService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `t24-ST_CustomerService-Data.jar` | 130 | record-model, unknown |
| `t24-ST_CustomerService-t24service.jar` | 4 | public-api, service-interface, unknown |
| `T2_ModelBank.jar` | 51 | unknown |
| `T2_Preferences.jar` | 11 | unknown |
| `T3_ModelBank.jar` | 2 | unknown |
| `T4_ModelBank.jar` | 9 | unknown |
| `T5_ModelBank.jar` | 9 | unknown |
| `Tables.jar` | 7740 | public-api, unknown |
| `TAXGST_Foundation.jar` | 169 | unknown |
| `TAXGST_TaxRegulatoryApi.jar` | 4 | public-api, unknown |
| `TF_Cache.jar` | 1 | unknown |
| `TF_Complex.jar` | 1 | unknown |
| `TF_Core.jar` | 2 | unknown |
| `TF_ErrorHandling.jar` | 3 | unknown |
| `TF_L3Helper.jar` | 1 | unknown |
| `TF_List.jar` | 7 | unknown |
| `TK_Foundation.jar` | 39 | unknown |
| `TM_PaymentOrder.jar` | 9 | unknown |
| `TNACIN_ChequeEligibility.jar` | 4 | unknown |
| `TNBASE_Foundation.jar` | 13 | unknown |
| `TNCUIN_CustomerCRM.jar` | 16 | unknown |
| `TNCUIN_Garnishment.jar` | 63 | unknown |
| `TNFCOP_Agency.jar` | 23 | unknown |
| `TNFCOP_AVA.jar` | 92 | unknown |
| `TNFCOP_ExportDocumentaryCredit.jar` | 42 | unknown |
| `TNFCOP_F1F2AuthorizationSheet.jar` | 28 | unknown |
| `TNFCOP_IncomingTransfer.jar` | 7 | unknown |
| `TNFCOP_InformationSheet.jar` | 38 | unknown |
| `TNFCOP_OutgoingTransfer.jar` | 28 | unknown |
| `TNFCOP_SchoolingProfessionalTraining.jar` | 18 | unknown |
| `TNFCOP_TradeTitle.jar` | 67 | unknown |
| `TSBNPL_ModelBank.jar` | 7 | unknown |
| `TV_Foundation.jar` | 106 | unknown |
| `TV_XmlRequest.jar` | 5 | unknown |
| `TX_Contract.jar` | 31 | unknown |
| `TX_TaxEngineHook.jar` | 3 | public-api, unknown |
| `TXRECT_TaxRectificationTool.jar` | 38 | unknown |
| `TY_Exceptions.jar` | 6 | unknown |
| `TY_Limits.jar` | 69 | unknown |
| `TY_Parameters.jar` | 12 | unknown |
| `TY_Position.jar` | 18 | unknown |
| `TY_RateParameters.jar` | 19 | unknown |
| `TY_Reports.jar` | 65 | unknown |
| `TZ_API.jar` | 8 | unknown |
| `TZ_Config.jar` | 26 | unknown |
| `TZ_Contract.jar` | 19 | unknown |
| `TZ_ModelBank.jar` | 2 | unknown |
| `UAECCS_Foundation.jar` | 15 | unknown |
| `VL_AMLService.jar` | 10 | unknown |
| `VL_Config.jar` | 19 | unknown |
| `VP_Config.jar` | 19 | unknown |
| `VS_Config.jar` | 2 | unknown |
| `WR_Foundation.jar` | 129 | unknown |
| `WR_ModelBank.jar` | 2 | unknown |
| `WS_ConnectionSetup.jar` | 2 | unknown |
| `WS_Metadata.jar` | 8 | unknown |
| `WTXSAI_WithholdingTax.jar` | 12 | unknown |
| `XF_Contract.jar` | 15 | unknown |
| `XF_Unit.jar` | 7 | unknown |
| `XP_Framework.jar` | 8 | unknown |
| `XT_PriceFeed.jar` | 38 | unknown |
