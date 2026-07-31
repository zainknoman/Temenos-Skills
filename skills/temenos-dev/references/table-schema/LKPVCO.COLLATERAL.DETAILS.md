# LKPVCO.COLLATERAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.LKPVCO.COLLATERAL.DETAILS` in `LKPVCO_ProvisioningandCollateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKPVCO.COLLATERAL.COLLATERAL.TYPE` | `LkpvcoCollateralDetails_CollateralType` | TField |  | Collateral type that can be selected from the COLLATERAL table. |
| 2 | `LKPVCO.COLLATERAL.PLAN.NUMBER.AND.DATE` | `LkpvcoCollateralDetails_PlanNumberAndDate` | TField |  | Identifies the plan reference for the immovable property. |
| 3 | `LKPVCO.COLLATERAL.BUILTUP.AREA` | `LkpvcoCollateralDetails_BuiltupArea` | TField |  | Builtup area for the building measured in square feet or square metre. |
| 4 | `LKPVCO.COLLATERAL.CHASSIS.NUMBER` | `LkpvcoCollateralDetails_ChassisNumber` | TField |  | Chassis number of the vehicle offered as collateral. |
| 5 | `LKPVCO.COLLATERAL.ENGINE.NUMBER` | `LkpvcoCollateralDetails_EngineNumber` | TField |  | Engine number for the vehicle offered as collateral. |
| 6 | `LKPVCO.COLLATERAL.VEHICLE.REGISTRATION.NUMBER` | `LkpvcoCollateralDetails_VehicleRegistrationNumber` | TField |  | Registration number for the vehicle offered as collateral. |
| 7 | `LKPVCO.COLLATERAL.VEHICLE.MAKE.OR.MODEL` | `LkpvcoCollateralDetails_VehicleMakeOrModel` | TField |  | Manufacturer, brand and the make for the vehicle offered as collateral. |
| 8 | `LKPVCO.COLLATERAL.GUARANTEED.AMOUNT` | `LkpvcoCollateralDetails_GuaranteedAmount` | TField |  | Amount of the Bank Guarantee. |
| 9 | `LKPVCO.COLLATERAL.INS.POLICY.SURRENDER.VALUE` | `LkpvcoCollateralDetails_InsPolicySurrenderValue` | TField |  | Realisable value of an insurance policy at the time of surrender. |
| 10 | `LKPVCO.COLLATERAL.ORIGINAL.MARKET.VALUE` | `LkpvcoCollateralDetails_OriginalMarketValue` | TField |  | Refers to the valuation of collateral as per the current market conditions. |
| 11 | `LKPVCO.COLLATERAL.ORIGINAL.FORCED.SALE.VALUE` | `LkpvcoCollateralDetails_OriginalForcedSaleValue` | TField |  | Realisable value of collateral in case of distressed sale. |
| 12 | `LKPVCO.COLLATERAL.ORIGINAL.VALUATION.AMOUNT` | `LkpvcoCollateralDetails_OriginalValuationAmount` | TField |  | Refers to the value of the collateral prior to depreciation. Applicable for vehicles. |
| 13 | `LKPVCO.COLLATERAL.PLEDGED.AMOUNT` | `LkpvcoCollateralDetails_PledgedAmount` | TField |  | Amount of the collateral pledged with the bank. |
| 14 | `LKPVCO.COLLATERAL.REVISED.FORCED.SALE.VALUE` | `LkpvcoCollateralDetails_RevisedForcedSaleValue` | TField |  | Revised sale value in case of distress sale. |
| 15 | `LKPVCO.COLLATERAL.REVISED.MARKET.VALUE` | `LkpvcoCollateralDetails_RevisedMarketValue` | TField |  | Value of collateral revised as per current market conditions. |
| 16 | `LKPVCO.COLLATERAL.REVISED.VALUATION` | `LkpvcoCollateralDetails_RevisedValuation` | TField |  | Refers to the revised value of collateral. |
| 17 | `LKPVCO.COLLATERAL.USEABLE.VALUE` | `LkpvcoCollateralDetails_UseableValue` | TField |  | Value of collateral available for usage. |
| 18 | `LKPVCO.COLLATERAL.VALUE.OF.SECURITY` | `LkpvcoCollateralDetails_ValueOfSecurity` | TField |  | Value of collaterals like government securities. |
| 19 | `LKPVCO.COLLATERAL.VALUE.OF.STOCK` | `LkpvcoCollateralDetails_ValueOfStock` | TField |  | Value of collaterals like goods and stock. |
| 20 | `LKPVCO.COLLATERAL.DATE.OF.EXECUTION.OF.SECURITY` | `LkpvcoCollateralDetails_DateOfExecutionOfSecurity` | TField |  | Date on which the security was created or executed. |
| 21 | `LKPVCO.COLLATERAL.DATE.OF.MANUFACTURE` | `LkpvcoCollateralDetails_DateOfManufacture` | TField |  | Manufacturing date for collaterals like vehicles, moveable equipments and machinery. |
| 22 | `LKPVCO.COLLATERAL.DATE.OF.ORIGINAL.SHARE.PRICE` | `LkpvcoCollateralDetails_DateOfOriginalSharePrice` | TField |  | Date of the original share price. |
| 23 | `LKPVCO.COLLATERAL.DATE.OF.PURCHASE` | `LkpvcoCollateralDetails_DateOfPurchase` | TField |  | Date of purchase for collaterals like movable equipments and machinery. |
| 24 | `LKPVCO.COLLATERAL.DATE.OF.REVISED.SHARE.PRICE` | `LkpvcoCollateralDetails_DateOfRevisedSharePrice` | TField |  | Revised share price date. |
| 25 | `LKPVCO.COLLATERAL.LATEST.STOCK.VERIFICATION.DATE` | `LkpvcoCollateralDetails_LatestStockVerificationDate` | TField |  | Latest date on which stock verification is done. |
| 26 | `LKPVCO.COLLATERAL.ORIGINAL.DATE.OF.STOCK.VALUE` | `LkpvcoCollateralDetails_OriginalDateOfStockValue` | TField |  | Original date of stock value. |
| 27 | `LKPVCO.COLLATERAL.ORIGINAL.POLICY.DATE` | `LkpvcoCollateralDetails_OriginalPolicyDate` | TField |  | original policy date. |
| 28 | `LKPVCO.COLLATERAL.ORIGINAL.VALUATION.DATE` | `LkpvcoCollateralDetails_OriginalValuationDate` | TField |  | Original date of valuation for immovable properties, vehicles, movable equipment and machinery. |
| 29 | `LKPVCO.COLLATERAL.PLEDGED.DATE` | `LkpvcoCollateralDetails_PledgedDate` | TField |  | Date on which the collateral was pledged. |
| 30 | `LKPVCO.COLLATERAL.REVISED.VALUE.OF.STOCK` | `LkpvcoCollateralDetails_RevisedValueOfStock` | TField |  | Stock value as per current market conditions. |
| 31 | `LKPVCO.COLLATERAL.REVISED.DATE.OF.STOCK.VALUE` | `LkpvcoCollateralDetails_RevisedDateOfStockValue` | TField |  | Date on which the stock value was revised. |
| 32 | `LKPVCO.COLLATERAL.REVISED.VALUATION.DATE` | `LkpvcoCollateralDetails_RevisedValuationDate` | TField |  | Date on which the valuation for immovable properties, vehicles, movable equipment and machinery have beenrevised. |
| 33 | `LKPVCO.COLLATERAL.NAME.FINANCIAL.INSTITUTION` | `LkpvcoCollateralDetails_NameFinancialInstitution` | TField |  |  |
| 34 | `LKPVCO.COLLATERAL.SHARE.BROKER` | `LkpvcoCollateralDetails_ShareBroker` | TField |  | Share broker name. |
| 35 | `LKPVCO.COLLATERAL.ORIGINAL.SHARE.PRICE` | `LkpvcoCollateralDetails_OriginalSharePrice` | TField |  | Share price as on date of purchase. |
| 36 | `LKPVCO.COLLATERAL.REVISED.SHARE.PRICE` | `LkpvcoCollateralDetails_RevisedSharePrice` | TField |  | Latest price of share. |
| 37 | `LKPVCO.COLLATERAL.SECURED.TRANS.REGISTRY.REF` | `LkpvcoCollateralDetails_SecuredTransRegistryRef` | TField |  | Transaction reference. |
| 38 | `LKPVCO.COLLATERAL.ORG.NUMBER.OF.SHARES.PLEDGED` | `LkpvcoCollateralDetails_OrgNumberOfSharesPledged` | TField |  | Quantity of shares pledged initially. |
| 39 | `LKPVCO.COLLATERAL.REV.NUMBER.OF.SHARES.PLEDGED` | `LkpvcoCollateralDetails_RevNumberOfSharesPledged` | TField |  | Latest quantity of shares pledged. |
| 40 | `LKPVCO.COLLATERAL.LICENSED.SURVEYOR.NAME` | `LkpvcoCollateralDetails_LicensedSurveyorName` | TField |  | Third party performing the survey for property valuation. |
| 41 | `LKPVCO.COLLATERAL.STAFF.STOCK.VERIFICATION` | `LkpvcoCollateralDetails_StaffStockVerification` |  |  |  |
| 42 | `LKPVCO.COLLATERAL.VALUERS.NAME` | `LkpvcoCollateralDetails_ValuersName` | TField |  | Third party performing the property valuation. |
| 43 | `LKPVCO.COLLATERAL.GUARANTOR.CLIENT.ID` | `LkpvcoCollateralDetails_GuarantorClientId` |  |  |  |
| 44 | `LKPVCO.COLLATERAL.GUARANTOR.NAME` | `LkpvcoCollateralDetails_GuarantorName` |  |  |  |
| 45 | `LKPVCO.COLLATERAL.LAND.EXTENT` | `LkpvcoCollateralDetails_LandExtent` | TField |  | Measurement of the land provided as collateral. |
| 46 | `LKPVCO.COLLATERAL.MACHINERY.TYPE` | `LkpvcoCollateralDetails_MachineryType` | TField |  | Machinery type being provided as collateral. |
| 47 | `LKPVCO.COLLATERAL.SOURCE.OF.VALUE.OF.STOCK` | `LkpvcoCollateralDetails_SourceOfValueOfStock` | TField |  | Source from which the stock valuation is derived. |
| 48 | `LKPVCO.COLLATERAL.T24.CLIENT.ID` | `LkpvcoCollateralDetails_T24ClientId` | TField |  | T24 ID of the customer providing the deposit. |
| 49 | `LKPVCO.COLLATERAL.EXTERNAL.CLIENT.ID` | `LkpvcoCollateralDetails_ExternalClientId` | TField |  | EXTERNAL ID of the customer providing the deposit. |
| 50 | `LKPVCO.COLLATERAL.DATE.OF.REGISTRATION` | `LkpvcoCollateralDetails_DateOfRegistration` | TField |  | Registration date for the vehicles. |
| 51 | `LKPVCO.COLLATERAL.LAND.REGISTRY` | `LkpvcoCollateralDetails_LandRegistry` | TField |  | Refers to the land registry. |
| 52 | `LKPVCO.COLLATERAL.MACHINERY.MODEL` | `LkpvcoCollateralDetails_MachineryModel` | TField |  | Model and make of the machinery. |
| 53 | `LKPVCO.COLLATERAL.PLOT.NUMBER` | `LkpvcoCollateralDetails_PlotNumber` | TField |  | Plot number for the land, building and plant - machinery. |
| 54 | `LKPVCO.COLLATERAL.PURCHASE.PRICE` | `LkpvcoCollateralDetails_PurchasePrice` | TField |  | Price at which the vehicles are purchased. |
| 55 | `LKPVCO.COLLATERAL.MORTGAGE.BOND.NUMBER` | `LkpvcoCollateralDetails_MortgageBondNumber` |  |  |  |
| 56 | `LKPVCO.COLLATERAL.STATUS.OF.MORTGAGE.BOND` | `LkpvcoCollateralDetails_StatusOfMortgageBond` |  |  |  |
| 57 | `LKPVCO.COLLATERAL.MORTGAGE.BOND.VALUE` | `LkpvcoCollateralDetails_MortgageBondValue` |  |  |  |
| 58 | `LKPVCO.COLLATERAL.MORTGAGE.BOND.EXECUTION.DATE` | `LkpvcoCollateralDetails_MortgageBondExecutionDate` |  |  |  |
| 59 | `LKPVCO.COLLATERAL.MORTGAGE.BOND.ATTESTED.BY` | `LkpvcoCollateralDetails_MortgageBondAttestedBy` |  |  |  |
| 60 | `LKPVCO.COLLATERAL.MB.ASSIGNED.VALUE` | `LkpvcoCollateralDetails_MbAssignedValue` |  |  |  |
| 61 | `LKPVCO.COLLATERAL.MB.TOTAL.ASSIGNED.VALUE` | `LkpvcoCollateralDetails_MbTotalAssignedValue` |  |  |  |
| 62 | `LKPVCO.COLLATERAL.MB.AVAILABLE.USEABLE.VALUE` | `LkpvcoCollateralDetails_MbAvailableUseableValue` |  |  |  |
| 63 | `LKPVCO.COLLATERAL.REMARKS` | `LkpvcoCollateralDetails_Remarks` |  |  |  |
| 64 | `LKPVCO.COLLATERAL.INSURANCE.POLICY.NUMBER` | `LkpvcoCollateralDetails_InsurancePolicyNumber` |  |  |  |
| 65 | `LKPVCO.COLLATERAL.INSURANCE.POLICY.TYPE` | `LkpvcoCollateralDetails_InsurancePolicyType` |  |  |  |
| 66 | `LKPVCO.COLLATERAL.INSURANCE.COMPANY` | `LkpvcoCollateralDetails_InsuranceCompany` |  |  |  |
| 67 | `LKPVCO.COLLATERAL.AMOUNT.INSURED` | `LkpvcoCollateralDetails_AmountInsured` |  |  |  |
| 68 | `LKPVCO.COLLATERAL.POLICY.START.DATE` | `LkpvcoCollateralDetails_PolicyStartDate` |  |  |  |
| 69 | `LKPVCO.COLLATERAL.POLICY.EXPIRY.DATE` | `LkpvcoCollateralDetails_PolicyExpiryDate` |  |  |  |
| 70 | `LKPVCO.COLLATERAL.INSURANCE.POLICY.VALUE` | `LkpvcoCollateralDetails_InsurancePolicyValue` | TField |  | Value of the insurance policy. |
| 71 | `LKPVCO.COLLATERAL.TOTAL.ASSIGNED.VALUE` | `LkpvcoCollateralDetails_TotalAssignedValue` | TField |  | Sum total of value assiged across facilities. |
| 72 | `LKPVCO.COLLATERAL.AVAILABLE.USEABLE.VALUE` | `LkpvcoCollateralDetails_AvailableUseableValue` | TField |  | Value of useable availabe for assignment. |
| 73 | `LKPVCO.COLLATERAL.REVISED.VALUE.OF.SECURITY` | `LkpvcoCollateralDetails_RevisedValueOfSecurity` | TField |  | Holds the revised value of security |
| 74 | `LKPVCO.COLLATERAL.INTERIM.FINAL.SECURITY` | `LkpvcoCollateralDetails_InterimFinalSecurity` | TField |  | Allows to select from two values Interim or Final |
| 75 | `LKPVCO.COLLATERAL.COLLATERAL.CURRENCY` | `LkpvcoCollateralDetails_CollaterialCurrency` |  |  |  |
| 76 | `LKPVCO.COLLATERAL.RESERVED.4` | `LkpvcoCollateralDetails_Reserved4` | TField |  | Reserved for future use. |
| 77 | `LKPVCO.COLLATERAL.RESERVED.5` | `LkpvcoCollateralDetails_Reserved5` | TField |  | Reserved for future use. |
| 78 | `LKPVCO.COLLATERAL.RESERVED.6` | `LkpvcoCollateralDetails_Reserved6` | TField |  | Reserved for future use. |
| 79 | `LKPVCO.COLLATERAL.RESERVED.7` | `LkpvcoCollateralDetails_Reserved7` | TField |  | Reserved for future use. |
| 80 | `LKPVCO.COLLATERAL.RESERVED.8` | `LkpvcoCollateralDetails_Reserved8` | TField |  | Reserved for future use. |
| 81 | `LKPVCO.COLLATERAL.LOCAL.REF` | `LkpvcoCollateralDetails_LocalRef` |  |  |  |
| 82 | `LKPVCO.COLLATERAL.OVERRIDE` | `LkpvcoCollateralDetails_Override` |  |  |  |
| 83 | `LKPVCO.COLLATERAL.RECORD.STATUS` | `LkpvcoCollateralDetails_RecordStatus` | String |  |  |
| 84 | `LKPVCO.COLLATERAL.CURR.NO` | `LkpvcoCollateralDetails_CurrNo` | String |  |  |
| 85 | `LKPVCO.COLLATERAL.INPUTTER` | `LkpvcoCollateralDetails_Inputter` |  |  |  |
| 86 | `LKPVCO.COLLATERAL.DATE.TIME` | `LkpvcoCollateralDetails_DateTime` |  |  |  |
| 87 | `LKPVCO.COLLATERAL.AUTHORISER` | `LkpvcoCollateralDetails_Authoriser` | String |  |  |
| 88 | `LKPVCO.COLLATERAL.CO.CODE` | `LkpvcoCollateralDetails_CoCode` | String |  |  |
| 89 | `LKPVCO.COLLATERAL.DEPT.CODE` | `LkpvcoCollateralDetails_DeptCode` | String |  |  |
| 90 | `LKPVCO.COLLATERAL.AUDITOR.CODE` | `LkpvcoCollateralDetails_AuditorCode` | String |  |  |
| 91 | `LKPVCO.COLLATERAL.AUDIT.DATE.TIME` | `LkpvcoCollateralDetails_AuditDateTime` | String |  |  |
| 92 | `LKPVCO.COLLATERAL.LIMIT` | `LkpvcoCollateralDetails_Limit` |  |  |  |
| 93 | `LKPVCO.COLLATERAL.LOAN.CONTRACT` | `LkpvcoCollateralDetails_LoanContract` |  |  |  |
| 94 | `LKPVCO.COLLATERAL.MD.DEAL.REFERENCE` | `LkpvcoCollateralDetails_MdDealReference` |  |  |  |
