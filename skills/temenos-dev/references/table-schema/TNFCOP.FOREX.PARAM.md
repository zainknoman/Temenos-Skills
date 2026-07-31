# TNFCOP.FOREX.PARAM — Table Schema

> Source: `INSERTS/I_F.TNFCOP.FOREX.PARAM` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.FOREX.PARAM.TAX.CUT.OFF.DATE` | `TnfcopForexParam_TaxCutOffDate` | TField |  | This field is predominantly for the Business Type Foreign Market. If Tax Report for the Previous Year is not collected before the cut-off date then the file gets suspended. 1) The Tax Declaration Date cannot be beyond previous to previous year if the record creation date/amendment date is before 15th July (TAX.CUT.OFF.DT) of the Current Year. E.g. If the record creation/amendment date is 1st July 2020, then the date Tax Declaration Date cannot be less than 1st Jan 2018. 2) The date cannot be beyond previous year if the record creation date/amendment date is on or after 15th July (TAX.CUT.OFF.DT) of the Current Year. E.g. If the record creation/amendment date is 16th July 2020, then the date Tax Declaration Date cannot be less than 1st Jan 2019. 3) The Year of Tax Declaration Year cannot be equal to the Current System Year. |
| 2 | `TNFCOP.FOREX.PARAM.FOREIGN.MARKET.PERCENT` | `TnfcopForexParam_ForeignMarketPercent` | TField |  | This field determines the percentage of Contract Amount to be considered for calculation of Eligible Amount. The field will be applicable for Business Type "Foreign Market". |
| 3 | `TNFCOP.FOREX.PARAM.OTHER.ACTIVITIES.PERCENT` | `TnfcopForexParam_OtherActivitiesPercent` | TField |  |  |
| 4 | `TNFCOP.FOREX.PARAM.LIMIT.EXPORTER` | `TnfcopForexParam_LimitExporter` | TField |  | This field determines the ceiling amount for Business Type Exporter. The calculated Eligible Amount cannot be greater than the ceiling defined in this field. The amount defined here should be in Local Currency. |
| 5 | `TNFCOP.FOREX.PARAM.LIMIT.OTHER.ACTIVITIES` | `TnfcopForexParam_LimitOtherActivities` | TField |  | This field determines the ceiling amount for Business Type Other Activities and for Non-bank customers. The calculated Eligible Amount cannot be greater than the ceiling defined in this field. The amount defined here should be in Local Currency. |
| 6 | `TNFCOP.FOREX.PARAM.LIMIT.OTHER.ACTIVITIES.BANK` | `TnfcopForexParam_LimitOtherActivitiesBank` | TField |  | This field determines the ceiling amount for Business Type Other Activities and for Bank customers. The calculated Eligible Amount cannot be greater than the ceiling defined in this field. The amount defined here should be in Local Currency. |
| 7 | `TNFCOP.FOREX.PARAM.LIMIT.PROMOTER` | `TnfcopForexParam_LimitPromoter` | TField |  | This field determines the ceiling amount for Business Type Other Activities and the NEW.PROJECT flag is checked. The Eligible Amount will be the amount defined in this field. The amount defined here should be in Local Currency. |
| 8 | `TNFCOP.FOREX.PARAM.FOREIGN.MARKET.EXP` | `TnfcopForexParam_ForeignMarketExp` | TField |  | If the SYSTEM DATE is greater than CONTRACT.DATE + Days defined in this field then system will throw an error that "Not allowed as Input since contract period has expired" |
| 9 | `TNFCOP.FOREX.PARAM.PREV.YEAR.PERCENT` | `TnfcopForexParam_PrevYearPercent` | TField |  | If the Tax Declaration Date is for previous to previous year for Business Type Other Activities then the Eligible Amount will be further multiplied by the percent defined in this field. The purpose of this field is to reduce the eligibility amount if the Tax Declaration Amount is for previous to previous year. |
| 10 | `TNFCOP.FOREX.PARAM.CURRENCY.MARKET` | `TnfcopForexParam_CurrencyMarket` | TField |  | Buy / Sell Rate for the currency market configured here will be considered for conversion from Foreign Currency to Local Currency. |
| 11 | `TNFCOP.FOREX.PARAM.SECTOR` | `TnfcopForexParam_Sector` | TField |  | Sector applicable for Bank customers has to be configured here. |
| 12 | `TNFCOP.FOREX.PARAM.FX.CEILING.LIMIT` | `TnfcopForexParam_FxCeilingLimit` | TField | Yes | Foreign exchange transaction limit above which declaration is mandatory The amount is expressed in local currency. |
| 13 | `TNFCOP.FOREX.PARAM.DECLARATION.VALIDITY` | `TnfcopForexParam_DeclarationValidity` | TField |  | Default validity months for declaration. This field represents the value in months. This value will be used during declaration creation to auto populate the expiry date. |
| 14 | `TNFCOP.FOREX.PARAM.SDC.ALLOWED.PRODUCT` | `TnfcopForexParam_SdcAllowedProduct` |  |  |  |
| 15 | `TNFCOP.FOREX.PARAM.SDC.CUTOFF.DAYS` | `TnfcopForexParam_SdcCutoffDays` | TField |  | Business days beyond which the sub delegation deposit purchase is not allowed. |
| 16 | `TNFCOP.FOREX.PARAM.TT.FCY.DEPOSIT.CODE` | `TnfcopForexParam_TtFcyDepositCode` | TField |  | Teller transaction code for Foreign Currency deposits. |
| 17 | `TNFCOP.FOREX.PARAM.TT.FCY.CASH.CODE` | `TnfcopForexParam_TtFcyCashCode` | TField |  | Teller transaction code for Foreign Currency Cash. |
| 18 | `TNFCOP.FOREX.PARAM.TT.SUBDELEGATION.CODE` | `TnfcopForexParam_TtSubdelegationCode` | TField |  | Teller transaction code for Sub-delegation. |
| 19 | `TNFCOP.FOREX.PARAM.HEADER.REG.CODE` | `TnfcopForexParam_HeaderRegCode` | TField |  | Header Reg code for the reporting. |
| 20 | `TNFCOP.FOREX.PARAM.INTERMEDIARY.CODE` | `TnfcopForexParam_IntermediaryCode` | TField |  | Intermediary Code for the reporting. |
| 21 | `TNFCOP.FOREX.PARAM.DETAIL.REG.CODE` | `TnfcopForexParam_DetailRegCode` | TField |  | Detail Reg Code for the reporting. |
| 22 | `TNFCOP.FOREX.PARAM.APPROVAL.STATUS` | `TnfcopForexParam_ApprovalStatus` | TField |  | The status which is considered as Approved for the information sheet. |
| 23 | `TNFCOP.FOREX.PARAM.CLEARANCE.CODE` | `TnfcopForexParam_ClearanceCode` | TField |  | This field is to store the Nature of the cleared Titles. |
| 24 | `TNFCOP.FOREX.PARAM.NON.CLEARANCE.CODE` | `TnfcopForexParam_NonClearanceCode` | TField |  | This field is to store the nature code of the Non Cleared Titles. |
| 25 | `TNFCOP.FOREX.PARAM.NEW.STATUS.CODE` | `TnfcopForexParam_NewStatusCode` | TField |  | This field is to store the nature code of the New status of the title reporting. |
| 26 | `TNFCOP.FOREX.PARAM.BANK.CODE.REPORT` | `TnfcopForexParam_BankCodeReport` | TField |  | This field is for Reporting purpose. This is the unique code of the Bank as provided by the Central Bank. E.g: 01 |
| 27 | `TNFCOP.FOREX.PARAM.DECI.CODE.CLEARED` | `TnfcopForexParam_DeciCodeCleared` | TField |  | This field denotes the decision code, which has to be updated in the report when the title is cleared. |
| 28 | `TNFCOP.FOREX.PARAM.DECI.CODE.NON.CLEARED` | `TnfcopForexParam_DeciCodeNonCleared` | TField |  |  |
| 29 | `TNFCOP.FOREX.PARAM.IMP.MARGIN.AMT` | `TnfcopForexParam_ImpMarginAmt` | TField |  | This field denotes the Import Margin amount for title codes 31,33,39. |
| 30 | `TNFCOP.FOREX.PARAM.IMP.MARGIN.PERCENT` | `TnfcopForexParam_ImpMarginPercent` | TField |  | This field denotes the Margin percentage of Imputation amount to be compared with difference between imputation amount and settlement amount for Title codes 31,33 and 39. |
| 31 | `TNFCOP.FOREX.PARAM.EXP.MARGIN.AMT` | `TnfcopForexParam_ExpMarginAmt` | TField |  | This field denotes the Export Margin amount for title codes 21,22. |
| 32 | `TNFCOP.FOREX.PARAM.EXP.MARGIN.PERCENT` | `TnfcopForexParam_ExpMarginPercent` | TField |  | This field denotes the Margin percentage of Imputation amount to be compared with difference between imputation amount and settlement amount for Title codes 21,22. |
| 33 | `TNFCOP.FOREX.PARAM.RELATION` | `TnfcopForexParam_Relation` | TField |  | All the Relation Customer tagged under the Relation Code configured in this field will be treated as Beneficiary. |
| 34 | `TNFCOP.FOREX.PARAM.EXPIRY.MONTH` | `TnfcopForexParam_ExpiryMonth` | TField |  | This field denotes the month on when the title is getting expired for reporting. |
| 35 | `TNFCOP.FOREX.PARAM.TRADE.TITLE.OPR` | `TnfcopForexParam_TradeTitleOpr` |  |  |  |
| 36 | `TNFCOP.FOREX.PARAM.CHARGE.TYPE` | `TnfcopForexParam_ChargeType` |  |  |  |
| 37 | `TNFCOP.FOREX.PARAM.F1.VALIDITY.DAYS` | `TnfcopForexParam_F1ValidityDays` | TField |  | Days specified here will be the number of days after which the contract will be expired. Calculated from the date spcified in CBT.AUTH.DATE |
| 38 | `TNFCOP.FOREX.PARAM.LOCAL.REF` | `TnfcopForexParam_LocalRef` |  |  |  |
| 39 | `TNFCOP.FOREX.PARAM.CHARGE.TXN.TYPE` | `TnfcopForexParam_ChargeTxnType` | TField |  | Stores the FT Transaction type which has to be used for making charge and tax payment |
| 40 | `TNFCOP.FOREX.PARAM.DECI.DTL.NON.CLEARED` | `TnfcopForexParam_DeciDtlNonCleared` | TField |  | Denotes the decision Detail which has to be updated in the report when the title is not-cleared. |
| 41 | `TNFCOP.FOREX.PARAM.DECI.DTL.CLEARED` | `TnfcopForexParam_DeciDtlCleared` | TField |  | Denotes the decision Detail which has to be updated in the report when the title is cleared. |
| 42 | `TNFCOP.FOREX.PARAM.MAX.MON.EXP` | `TnfcopForexParam_MaxMonExp` | TField |  | This field stores the maximum monthly expenses allowed |
| 43 | `TNFCOP.FOREX.PARAM.MAX.OTHER.EXPENSES` | `TnfcopForexParam_MaxOtherExpenses` | TField |  | This field stores the maximum other expenses allowed |
| 44 | `TNFCOP.FOREX.PARAM.SUSPENSION.PERIOD` | `TnfcopForexParam_SuspensionPeriod` | TField |  | This field stores the number of days or months, if the file is not final registered within this period it has to be suspended |
| 45 | `TNFCOP.FOREX.PARAM.EXPORT.PERCENT` | `TnfcopForexParam_ExportPercent` | TField |  | For manual supply of LIMIT Export Revenue is auto-calculated based on the value configured here. It is applicable only for Business Type EXPORTER. |
| 46 | `TNFCOP.FOREX.PARAM.RECORD.TYPE.ENTITY` | `TnfcopForexParam_RecordTypeEntity` | TField |  | This field is used to identify whether the record is for Entity or Movements. E.g: if E is configured here the Entity record will be prefixed with E. |
| 47 | `TNFCOP.FOREX.PARAM.RECORD.TYPE.MOVEMENTS` | `TnfcopForexParam_RecordTypeMovements` | TField |  | This field is used to identify whether the record is for Entity or Movements. E.g: if M is configured here the Movement records will be prefixed with M. |
| 48 | `TNFCOP.FOREX.PARAM.LEGAL.DOC.NAME` | `TnfcopForexParam_LegalDocName` |  |  |  |
| 49 | `TNFCOP.FOREX.PARAM.OVERRIDE` | `TnfcopForexParam_Override` |  |  |  |
| 50 | `TNFCOP.FOREX.PARAM.RECORD.STATUS` | `TnfcopForexParam_RecordStatus` | String |  |  |
| 51 | `TNFCOP.FOREX.PARAM.CURR.NO` | `TnfcopForexParam_CurrNo` | String |  |  |
| 52 | `TNFCOP.FOREX.PARAM.INPUTTER` | `TnfcopForexParam_Inputter` |  |  |  |
| 53 | `TNFCOP.FOREX.PARAM.DATE.TIME` | `TnfcopForexParam_DateTime` |  |  |  |
| 54 | `TNFCOP.FOREX.PARAM.AUTHORISER` | `TnfcopForexParam_Authoriser` | String |  |  |
| 55 | `TNFCOP.FOREX.PARAM.CO.CODE` | `TnfcopForexParam_CoCode` | String |  |  |
| 56 | `TNFCOP.FOREX.PARAM.DEPT.CODE` | `TnfcopForexParam_DeptCode` | String |  |  |
| 57 | `TNFCOP.FOREX.PARAM.AUDITOR.CODE` | `TnfcopForexParam_AuditorCode` | String |  |  |
| 58 | `TNFCOP.FOREX.PARAM.AUDIT.DATE.TIME` | `TnfcopForexParam_AuditDateTime` | String |  |  |
| 59 | `TNFCOP.FOREX.PARAM.BENE.DOC.NAME` | `TnfcopForexParam_BeneDocName` |  |  |  |
| 60 | `TNFCOP.FOREX.PARAM.PARAM.BENEFICIARY.CODE` | `TnfcopForexParam_BeneficiaryCode` |  |  |  |
| 61 | `TNFCOP.FOREX.PARAM.AUTH.AMT.CBT.CDE` | `TnfcopForexParam_AuthAmtCbtCde` | TField |  | If value is present in the field AUTH.AMT.CBT in the application TNFCOP.AVA.APPLICATION then at the time of reporting MOC should be reported. E.g: MOC to be configured here. |
| 62 | `TNFCOP.FOREX.PARAM.FEATURE.FLAG` | `TnfcopForexParam_FeatureFlag` | TField |  | Used for Temenos internal purpose |
| 63 | `TNFCOP.FOREX.PARAM.CONVERTIBLE.DINAR.PRODUCT` | `TnfcopForexParam_ConvertibleDinarProduct` |  |  |  |
| 64 | `TNFCOP.FOREX.PARAM.TOLERANCE.FOR.TITLE` | `TnfcopForexParam_ToleranceForTitle` |  |  |  |
| 65 | `TNFCOP.FOREX.PARAM.TOLERANCE.PERCENTAGE` | `TnfcopForexParam_TolerancePercentage` |  |  |  |
| 66 | `TNFCOP.FOREX.PARAM.SECTOR.IND.FROM` | `TnfcopForexParam_SectorIndFrom` |  |  |  |
| 67 | `TNFCOP.FOREX.PARAM.SECTOR.IND.TO` | `TnfcopForexParam_SectorIndTo` |  |  |  |
| 68 | `TNFCOP.FOREX.PARAM.EXCLUDE.PRODUCT.PPR` | `TnfcopForexParam_ExcludeProductPpr` |  |  |  |
