# SY.PRODUCT — Table Schema

> Source: `INSERTS/I_F.SY.PRODUCT` in `SY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.PR.PRODUCT.DEFINITION` | `SyProduct_ProductDefinition` | TField |  | Product Definition key (for SY.PRODUCT.DEFINITION), defaulted from the record key. System Generated field only - non-inputtable. |
| 2 | `SY.PR.TRANSACTION` | `SyProduct_Transaction` | TField |  | Transaction key (for SY.TRANSACTION), defaulted from the record key. System Generated field only - non-inputtable. |
| 3 | `SY.PR.PUBLISHED` | `SyProduct_Published` | TField |  | This field is set to YES if the Product is published in the AA catalog or to NO if it has been removed from theAA catalog. System generated field - defaulted from SY.PRODUCT.DEFINITION. |
| 4 | `SY.PR.COMPLETE` | `SyProduct_Complete` | TField |  | When YES this indicates that the Product is complete and can be dealt on. Deals cannot be created for a Product which is not complete. |
| 5 | `SY.PR.SHORT.NAME` | `SyProduct_ShortName` |  |  |  |
| 6 | `SY.PR.DESCRIPTION` | `SyProduct_Description` |  |  |  |
| 7 | `SY.PR.TRACKING` | `SyProduct_Tracking` | TField |  | When Tracking is enabled the instantiated Product will track any changes made to the Product Definition duringthe product lifecycle. Otherwise the instantiated Product will copy the state of the Product definition whencreated. Therefore, if TRACKING is set, the tracked fields will be cleared Can be set to either YES or NO. |
| 8 | `SY.PR.VALUATION.ROUTINE` | `SyProduct_ValuationRoutine` | TField |  | If populated this will be the valuation routine that will be used to valuate this structured product. Valuation routine must have an associated PGM.FILE record. |
| 9 | `SY.PR.SWEEP.ACCT` | `SyProduct_SweepAcct` | TField |  | When YES this indicates that the Account Sweeping Process should automatically sweep transactions from thecustomers segregated account to the customers source account. When the appropriate SY.PARAMETER record has its SWEEP.ACCT.MASTER field set to 'Off' then this field will beignored and no sweeping will occur. Can be YES or NO (or blank if TRACKING is set to YES) |
| 10 | `SY.PR.DEPOSIT` | `SyProduct_Deposit` | TField |  | Defines whether a deposit will be taken from the client at inception of this deal. |
| 11 | `SY.PR.PRODUCT.CCY` | `SyProduct_ProductCcy` | TField |  | A currency which defines the product. Such as "USD". |
| 12 | `SY.PR.SY.EXCLUDE.VALUATION` | `SyProduct_SyExcludeValuation` | TField |  | This field sets the default value for inclusion/exclusion of SY underlying deals in the valuation and customerposition reporting. If set to "YES" this will report only the SY deal otherwise all transactions created by the SY product alongwith the SY deal will be displayed. |
| 13 | `SY.PR.SWEEP.TXNS` | `SyProduct_SweepTxns` |  |  |  |
| 14 | `SY.PR.EVENT` | `SyProduct_Event` |  |  |  |
| 15 | `SY.PR.DEPENDENCY` | `SyProduct_Dependency` |  |  |  |
| 16 | `SY.PR.ACTIVE` | `SyProduct_Active` |  |  |  |
| 17 | `SY.PR.EB.ACTIVITY` | `SyProduct_EbActivity` |  |  |  |
| 18 | `SY.PR.EB.EVENT.TYPE` | `SyProduct_EbEventType` |  |  |  |
| 19 | `SY.PR.COB.PHASE` | `SyProduct_CobPhase` |  |  |  |
| 20 | `SY.PR.OPERATION` | `SyProduct_Operation` |  |  |  |
| 21 | `SY.PR.UNIT.DEF` | `SyProduct_UnitDef` |  |  |  |
| 22 | `SY.PR.INSTANCE` | `SyProduct_Instance` |  |  |  |
| 23 | `SY.PR.RESERVED.16` | `SyProduct_Reserved16` |  |  |  |
| 24 | `SY.PR.RESERVED.15` | `SyProduct_Reserved15` |  |  |  |
| 25 | `SY.PR.RESERVED.14` | `SyProduct_Reserved14` |  |  |  |
| 26 | `SY.PR.SUB.ASSET.TYPE` | `SyProduct_SubAssetType` | TField |  | This is the Sub-Asset Type for this product. This will be defaulted from SY.PARAMETER Must be a valid SUB.ASSET.TYPE. |
| 27 | `SY.PR.RESERVED.12` | `SyProduct_Reserved12` | TField |  |  |
| 28 | `SY.PR.TERMINATED.DATE` | `SyProduct_TerminatedDate` | TField |  | This field will hold the date on which the contract was terminated. |
| 29 | `SY.PR.TERMINATED` | `SyProduct_Terminated` | TField |  | Indicates whether the product has reached the end of it's lifecycle yet - set to 'Yes' when this has happened. System Generated field - non-inputtable. |
| 30 | `SY.PR.INTERNAL.USE` | `SyProduct_InternalUse` | TField |  | This is a system generated non-inputtable field. This field is used internally by T24 to monitor the status of the tracking fields on the application. |
| 31 | `SY.PR.PROD.INTERFACE` | `SyProduct_ProdInterface` | TField |  | The key to the product interface record which exposes an underlying application to the framework and will resultin the processing of this product. |
| 32 | `SY.PR.FIRST.DATE` | `SyProduct_FirstDate` | TField |  | The first date from which a deal for this product will be accepted into the system. |
| 33 | `SY.PR.LAST.DATE` | `SyProduct_LastDate` | TField |  | The last date on which a deal for this product may be accepted into the system. |
| 34 | `SY.PR.PRODUCT.CATEGORY` | `SyProduct_ProductCategory` | TField |  | This field holds a generic category id which defines the category of the product. This information is defaultedfrom the SY.PARAMETER record. |
| 35 | `SY.PR.VALUE.UNIT` | `SyProduct_ValueUnit` |  |  |  |
| 36 | `SY.PR.SUPPRESS.UNDERLYING` | `SyProduct_SuppressUnderlying` | TField |  |  |
| 37 | `SY.PR.FIXING.ROUTINE` | `SyProduct_FixingRoutine` | TField |  |  |
| 38 | `SY.PR.MIN.PERIOD.KOUT` | `SyProduct_MinPeriodKout` | TField |  |  |
| 39 | `SY.PR.CUST.NETTING.REQD` | `SyProduct_CustNettingReqd` | TField |  | This field decides whether premium and fee amount should be netted and raised as a single entry for customerside. This field is applicable only for agency booking model. |
| 40 | `SY.PR.NET.CR.TXN.CODE` | `SyProduct_NetCrTxnCode` | TField |  | Credit Transaction code for raising the net entry raised out of premium and fee amount. (Premium and Feeamount). |
| 41 | `SY.PR.NET.DR.TXN.CODE` | `SyProduct_NetDrTxnCode` | TField |  | Debit Transaction code for raising the net entry raised out of premium and fee amount. (Premium and Fee amount). |
| 42 | `SY.PR.MTM.ROUTINE` | `SyProduct_MtmRoutine` | TField |  |  |
| 43 | `SY.PR.MTM.REQUIRED` | `SyProduct_MtmRequired` | TField |  |  |
| 44 | `SY.PR.MTM.DIFFERENCE` | `SyProduct_MtmDifference` | TField |  |  |
| 45 | `SY.PR.MTM.PL.CATEG` | `SyProduct_MtmPlCateg` | TField |  |  |
| 46 | `SY.PR.MTM.CATEG` | `SyProduct_MtmCateg` | TField |  |  |
| 47 | `SY.PR.MTM.CR.TXN.CODE` | `SyProduct_MtmCrTxnCode` | TField |  |  |
| 48 | `SY.PR.MTM.DR.TXN.CODE` | `SyProduct_MtmDrTxnCode` | TField |  |  |
| 49 | `SY.PR.DEPOSIT.CATEG` | `SyProduct_DepositCateg` | TField |  |  |
| 50 | `SY.PR.DEPOSIT.DAY.BASIS` | `SyProduct_DepositDayBasis` | TField |  |  |
| 51 | `SY.PR.LOAN.CATEG` | `SyProduct_LoanCateg` | TField |  |  |
| 52 | `SY.PR.LOAN.DAY.BASIS` | `SyProduct_LoanDayBasis` | TField |  |  |
| 53 | `SY.PR.FEE.PL.CATEG` | `SyProduct_FeePlCateg` | TField |  |  |
| 54 | `SY.PR.FEE.CR.TXN.CODE` | `SyProduct_FeeCrTxnCode` | TField |  |  |
| 55 | `SY.PR.FEE.DR.TXN.CODE` | `SyProduct_FeeDrTxnCode` | TField |  |  |
| 56 | `SY.PR.PREM.REAL.MAT` | `SyProduct_PremRealMat` | TField |  |  |
| 57 | `SY.PR.PREM.PL` | `SyProduct_PremPl` | TField |  |  |
| 58 | `SY.PR.PREM.CR.TXN.CODE` | `SyProduct_PremCrTxnCode` | TField |  |  |
| 59 | `SY.PR.PREM.DR.TXN.CODE` | `SyProduct_PremDrTxnCode` | TField |  |  |
| 60 | `SY.PR.UNREAL.PREM.PL` | `SyProduct_UnrealPremPl` | TField |  |  |
| 61 | `SY.PR.ULPREM.CR.TXN.CODE` | `SyProduct_UlpremCrTxnCode` | TField |  |  |
| 62 | `SY.PR.ULPREM.DR.TXN.CODE` | `SyProduct_UlpremDrTxnCode` | TField |  |  |
| 63 | `SY.PR.UNWIND.CHG.PL` | `SyProduct_UnwindChgPl` | TField |  |  |
| 64 | `SY.PR.UNWIND.CR.TXN.CODE` | `SyProduct_UnwindCrTxnCode` | TField |  |  |
| 65 | `SY.PR.UNWIND.DR.TXN.CODE` | `SyProduct_UnwindDrTxnCode` | TField |  |  |
| 66 | `SY.PR.CA.IMPACT` | `SyProduct_CaImpact` | TField |  |  |
| 67 | `SY.PR.APPLICABLE.ELEMENT` | `SyProduct_ApplicableElement` |  |  |  |
| 68 | `SY.PR.ELEMENT.TYPE` | `SyProduct_ElementType` |  |  |  |
| 69 | `SY.PR.RESERVED19` | `SyProduct_Reserved19` | TField |  |  |
| 70 | `SY.PR.RESERVED18` | `SyProduct_Reserved18` | TField |  |  |
| 71 | `SY.PR.NOTIONAL.ENTRIES` | `SyProduct_NotionalEntries` | TField |  |  |
| 72 | `SY.PR.NOTIONAL.DIFF` | `SyProduct_NotionalDiff` | TField |  |  |
| 73 | `SY.PR.INCL.SUSP.DAYS` | `SyProduct_InclSuspDays` | TField |  |  |
| 74 | `SY.PR.ACCRUAL.BASIS` | `SyProduct_AccrualBasis` | TField |  |  |
| 75 | `SY.PR.CASH.SETT.PL.CATEG` | `SyProduct_CashSettPlCateg` | TField |  |  |
| 76 | `SY.PR.CASH.CR.TXN.CODE` | `SyProduct_CashCrTxnCode` | TField |  |  |
| 77 | `SY.PR.CASH.DR.TXN.CODE` | `SyProduct_CashDrTxnCode` | TField |  |  |
| 78 | `SY.PR.NOVATION.PL.CATEG` | `SyProduct_NovationPlCateg` | TField |  |  |
| 79 | `SY.PR.NOV.CR.TXN.CODE` | `SyProduct_NovCrTxnCode` | TField |  |  |
| 80 | `SY.PR.NOV.DR.TXN.CODE` | `SyProduct_NovDrTxnCode` | TField |  |  |
| 81 | `SY.PR.INCL.VANILLA.OPTION` | `SyProduct_InclVanillaOption` | TField |  |  |
| 82 | `SY.PR.USE.MASTER.SAT` | `SyProduct_UseMasterSat` | TField |  | This field decides whether sub asset type should be used from SY.MASTER application. |
| 83 | `SY.PR.AGENCY.BOOKING.MODEL` | `SyProduct_AgencyBookingModel` | TField |  | This field decides whether transaction is agency booking model or not. ie. Customer Vs Counterparty transaction.No dealer book is involved. |
| 84 | `SY.PR.GEARED.ACCRUAL` | `SyProduct_GearedAccrual` | TField |  | This field decides the basis on which gearing will be applied on the accrued units. |
| 85 | `SY.PR.SC.CR.TXN` | `SyProduct_ScCrTxn` | TField |  | This field indicates the credit transaction name that is mapped to field CUST.TRANS.CODE(incase ofaccumulator)/BR.TRANS.CODE(incase of decumulator) in SEC.TRADE record created from SY.ACCU.DECU contract duringfixing. |
| 86 | `SY.PR.SC.DR.TXN` | `SyProduct_ScDrTxn` | TField |  | This field indicates the debit transaction name that is mapped to field BR.TRANS.CODE(incase ofaccumulator)/CUST.TRANS.CODE(incase of decumulator) in SEC.TRADE record created from SY.ACCU.DECU contract duringfixing. |
| 87 | `SY.PR.LIMIT.UPD.REQD` | `SyProduct_LimitUpdReqd` | TField |  | This field decides whether limit should be updated for customer. |
| 88 | `SY.PR.SINGLE.SCHEDULE` | `SyProduct_SingleSchedule` | TField |  | This field indicates whether the notional amount and leveraged/geared notional amount follow the same fixingschedule in SY.FX.FORWARDS contract. |
| 89 | `SY.PR.SPOT.ENTRIES` | `SyProduct_SpotEntries` | TField |  | Accepts YES, NO and BOTH Default value - YES YES - When contract is exercised, maturity entries will not be raised from SYForex - customer or wash accountwill be credited to/debited from based on thebooking model NO - When contract is matured :SY entries - customer or wash account will be credited to/debited from based onthebooking modelForex entries - washaccount will be credited to/debited from based on the booking model BOTH - When contract is matured :SY entries - customer or wash account will be credited to/debited from based onthebooking modelForex entries -customer account will be credited to/debited from based on thebooking model |
| 90 | `SY.PR.LOCAL.REF` | `SyProduct_LocalRef` |  |  |  |
| 91 | `SY.PR.OVERRIDE` | `SyProduct_Override` |  |  |  |
| 92 | `SY.PR.RECORD.STATUS` | `SyProduct_RecordStatus` | String |  |  |
| 93 | `SY.PR.CURR.NO` | `SyProduct_CurrNo` | String |  |  |
| 94 | `SY.PR.INPUTTER` | `SyProduct_Inputter` |  |  |  |
| 95 | `SY.PR.DATE.TIME` | `SyProduct_DateTime` |  |  |  |
| 96 | `SY.PR.AUTHORISER` | `SyProduct_Authoriser` | String |  |  |
| 97 | `SY.PR.CO.CODE` | `SyProduct_CoCode` | String |  |  |
| 98 | `SY.PR.DEPT.CODE` | `SyProduct_DeptCode` | String |  |  |
| 99 | `SY.PR.AUDITOR.CODE` | `SyProduct_AuditorCode` | String |  |  |
| 100 | `SY.PR.AUDIT.DATE.TIME` | `SyProduct_AuditDateTime` | String |  |  |
