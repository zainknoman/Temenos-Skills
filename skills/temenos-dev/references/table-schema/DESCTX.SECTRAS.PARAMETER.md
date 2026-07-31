# DESCTX.SECTRAS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.PARAMETER` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.PARAM.INTEREST.SUSPENSE.ACCOUNT` | `DesctxSectrasParameter_InterestSuspenseAccount` | TField |  | This field will contain the Category of the Internal account to which the interest amount is parked in case of net settlement |
| 2 | `SECTRAS.PARAM.TAX.INDICATOR` | `DesctxSectrasParameter_TaxIndicator` |  |  |  |
| 3 | `SECTRAS.PARAM.ACCOUNT.NO` | `DesctxSectrasParameter_AccountNo` |  |  |  |
| 4 | `SECTRAS.PARAM.BUSINESS.TRIGGERS` | `DesctxSectrasParameter_BusinessTriggers` |  |  |  |
| 5 | `SECTRAS.PARAM.APPLICATION` | `DesctxSectrasParameter_Application` |  |  |  |
| 6 | `SECTRAS.PARAM.FIELD.NAME` | `DesctxSectrasParameter_FieldName` |  |  |  |
| 7 | `SECTRAS.PARAM.MAPPING.RECORD` | `DesctxSectrasParameter_MappingRecord` |  |  |  |
| 8 | `SECTRAS.PARAM.RESERVED.8` | `DesctxSectrasParameter_Reserved8` |  |  |  |
| 9 | `SECTRAS.PARAM.SPOUSE.RELATION` | `DesctxSectrasParameter_SpouseRelation` | TField |  | This field is used to define the relation code to be considered for spouse relation. This field is vetted to the table RELATION |
| 10 | `SECTRAS.PARAM.DEFAULT.ACC.INT.PROPERTY` | `DesctxSectrasParameter_DefaultAccIntProperty` | TField |  | This field is used to define the default interest property to be used for Account product line |
| 11 | `SECTRAS.PARAM.DEFAULT.DEP.INT.PROPERTY` | `DesctxSectrasParameter_DefaultDepIntProperty` | TField |  | This field will be used to define the default interest property to be used for Deposit product line |
| 12 | `SECTRAS.PARAM.PRODUCT.NAME` | `DesctxSectrasParameter_ProductName` |  |  |  |
| 13 | `SECTRAS.PARAM.INTEREST.PROPERTY` | `DesctxSectrasParameter_InterestProperty` |  |  |  |
| 14 | `SECTRAS.PARAM.ROLE` | `DesctxSectrasParameter_Role` |  |  |  |
| 15 | `SECTRAS.PARAM.RETAIL.RELATION` | `DesctxSectrasParameter_RetailRelation` |  |  |  |
| 16 | `SECTRAS.PARAM.WEALTH.RELATION` | `DesctxSectrasParameter_WealthRelation` |  |  |  |
| 17 | `SECTRAS.PARAM.SECTRAS.USER` | `DesctxSectrasParameter_SectrasUser` | TField |  | This field capture the Sectras User ID |
| 18 | `SECTRAS.PARAM.SECTRAS.ENTITY` | `DesctxSectrasParameter_SectrasEntity` | TField |  | This field capture the Sectras Entity Value |
| 19 | `SECTRAS.PARAM.SHIPPING.ADDRESS` | `DesctxSectrasParameter_ShippingAddress` | TField |  |  |
| 20 | `SECTRAS.PARAM.OVERRIDE.PROCESSING` | `DesctxSectrasParameter_OverrideProcessing` |  |  |  |
| 21 | `SECTRAS.PARAM.AC.ENTRY.PARAM` | `DesctxSectrasParameter_AcEntryParam` |  |  |  |
| 22 | `SECTRAS.PARAM.EXCLUDE.TRANS` | `DesctxSectrasParameter_ExcludeTrans` |  |  |  |
| 23 | `SECTRAS.PARAM.FEES.INTERFACE` | `DesctxSectrasParameter_FeesInterface` |  |  |  |
| 24 | `SECTRAS.PARAM.FEES.REASON` | `DesctxSectrasParameter_FeesReason` |  |  |  |
| 25 | `SECTRAS.PARAM.GIFT.TRANS.TYPE` | `DesctxSectrasParameter_GiftTransType` |  |  |  |
| 26 | `SECTRAS.PARAM.SOLIDARITY.TAX` | `DesctxSectrasParameter_SolidarityTax` | TField |  | Tax type for Solidarity Tax |
| 27 | `SECTRAS.PARAM.WITHHOLDING.TAX` | `DesctxSectrasParameter_WithholdingTax` | TField |  | Tax type for Withholding Tax |
| 28 | `SECTRAS.PARAM.CHURCH.TAX` | `DesctxSectrasParameter_ChurchTax` | TField |  | Tax type for Church Tax |
| 29 | `SECTRAS.PARAM.ECB.CCY.MKT` | `DesctxSectrasParameter_EcbCcyMkt` | TField |  | Currency market value for ECB currency market |
| 30 | `SECTRAS.PARAM.STND.CCY.MKT` | `DesctxSectrasParameter_StndCcyMkt` | TField |  | Currency market value for Standard currency market |
| 31 | `SECTRAS.PARAM.TAX.IMPACT` | `DesctxSectrasParameter_TaxImpact` | TField |  | Flag to indicate if fee and commission amounts are to be taxed or not |
| 32 | `SECTRAS.PARAM.RETRO.CE.TRANS.TYPE` | `DesctxSectrasParameter_RetroCeTransType` | TField |  | Transaction type values for Retro type transfer |
| 33 | `SECTRAS.PARAM.GOODWILL.CE.TRANS.TYPE` | `DesctxSectrasParameter_GoodwillCeTransType` | TField |  | Transaction type values for Goodwill type transfer |
| 34 | `SECTRAS.PARAM.BENE.CHANGE.REASON` | `DesctxSectrasParameter_BeneChangeReason` |  |  |  |
| 35 | `SECTRAS.PARAM.BENE.CHANGE.IND` | `DesctxSectrasParameter_BeneChangeInd` |  |  |  |
| 36 | `SECTRAS.PARAM.CA.INTRF.CLIENT` | `DesctxSectrasParameter_CaIntrfClient` | TField |  | Client number for CA interface |
| 37 | `SECTRAS.PARAM.LOCAL.REF` | `DesctxSectrasParameter_LocalRef` |  |  |  |
| 38 | `SECTRAS.PARAM.EXCLUDE.PRODUCTS` | `DesctxSectrasParameter_ExcludeProducts` |  |  |  |
| 39 | `SECTRAS.PARAM.TAX.SETTLEMENT.PRODUCT` | `DesctxSectrasParameter_TaxSettlementProduct` |  |  |  |
| 40 | `SECTRAS.PARAM.CLIENT.CLOSURE` | `DesctxSectrasParameter_ClientClosure` | TField |  |  |
| 41 | `SECTRAS.PARAM.EXCLUDE.SUB.ASSET.TYPE` | `DesctxSectrasParameter_ExcludeSubAssetType` |  |  |  |
| 42 | `SECTRAS.PARAM.DX.ALT.ID.PRIORITY` | `DesctxSectrasParameter_DxAltIdPriority` |  |  |  |
| 43 | `SECTRAS.PARAM.ALL.IN.FEE.GROUP.ID` | `DesctxSectrasParameter_AllInFeeGroupId` |  |  |  |
| 44 | `SECTRAS.PARAM.TRANS.PORTION.PERC` | `DesctxSectrasParameter_TransPortionPerc` |  |  |  |
| 45 | `SECTRAS.PARAM.OVERRIDE` | `DesctxSectrasParameter_Override` |  |  |  |
| 46 | `SECTRAS.PARAM.RECORD.STATUS` | `DesctxSectrasParameter_RecordStatus` | String |  |  |
| 47 | `SECTRAS.PARAM.CURR.NO` | `DesctxSectrasParameter_CurrNo` | String |  |  |
| 48 | `SECTRAS.PARAM.INPUTTER` | `DesctxSectrasParameter_Inputter` |  |  |  |
| 49 | `SECTRAS.PARAM.DATE.TIME` | `DesctxSectrasParameter_DateTime` |  |  |  |
| 50 | `SECTRAS.PARAM.AUTHORISER` | `DesctxSectrasParameter_Authoriser` | String |  |  |
| 51 | `SECTRAS.PARAM.CO.CODE` | `DesctxSectrasParameter_CoCode` | String |  |  |
| 52 | `SECTRAS.PARAM.DEPT.CODE` | `DesctxSectrasParameter_DeptCode` | String |  |  |
| 53 | `SECTRAS.PARAM.AUDITOR.CODE` | `DesctxSectrasParameter_AuditorCode` | String |  |  |
| 54 | `SECTRAS.PARAM.AUDIT.DATE.TIME` | `DesctxSectrasParameter_AuditDateTime` | String |  |  |
| 55 | `SECTRAS.PARAM.CR.CUSTOMER.RELATION` | `DesctxSectrasParameter_CrCustomerRelation` |  |  |  |
| 56 | `SECTRAS.PARAM.PARTNER.ID.API` | `DesctxSectrasParameter_PartnerIdApi` | TField |  | This field holds the hook routine to generate Partner Id |
| 57 | `SECTRAS.PARAM.PARTNER.GROUP.ID.API` | `DesctxSectrasParameter_PartnerGroupIdApi` | TField |  | This field holds the hook routine to generate Partner Group Id |
| 58 | `SECTRAS.PARAM.FT.TRANS.TYPE` | `DesctxSectrasParameter_FtTransType` |  |  |  |
| 59 | `SECTRAS.PARAM.TAXABLE` | `DesctxSectrasParameter_Taxable` |  |  |  |
| 60 | `SECTRAS.PARAM.REC.DET.REQD` | `DesctxSectrasParameter_RecDetReqd` |  |  |  |
| 61 | `SECTRAS.PARAM.CL.REASON.CASH.MAN` | `DesctxSectrasParameter_ClReasonCashMan` | TField |  | Closing reason for manual cash settlement |
| 62 | `SECTRAS.PARAM.CL.REASON.CASH.AUTO` | `DesctxSectrasParameter_ClReasonCashAuto` | TField |  | Closing reason for auto cash settlement |
| 63 | `SECTRAS.PARAM.CL.REASON.EXC.MAN` | `DesctxSectrasParameter_ClReasonExcMan` | TField |  | Closing reason for exercise manual |
| 64 | `SECTRAS.PARAM.CL.REASON.EXC.AUTO` | `DesctxSectrasParameter_ClReasonExcAuto` | TField |  | Closing reason for exercise auto |
| 65 | `SECTRAS.PARAM.CL.REASON.ASN.MAN` | `DesctxSectrasParameter_ClReasonAsnMan` | TField |  | Closing reason for manual assignment |
| 66 | `SECTRAS.PARAM.CL.REASON.ASN.AUTO` | `DesctxSectrasParameter_ClReasonAsnAuto` | TField |  | Closing reason for auto assignment |
| 67 | `SECTRAS.PARAM.CL.REASON.EXP.MAN` | `DesctxSectrasParameter_ClReasonExpMan` | TField |  | Closing reason for manual expiry |
| 68 | `SECTRAS.PARAM.CL.REASON.EXP.AUTO` | `DesctxSectrasParameter_ClReasonExpAuto` | TField |  | Closing reason for auto expiry |
| 69 | `SECTRAS.PARAM.CL.REASON.EXT.TRNF` | `DesctxSectrasParameter_ClReasonExtTrnf` | TField |  | Closing reason for external transfers |
| 70 | `SECTRAS.PARAM.LS.IND.BUY` | `DesctxSectrasParameter_LsIndBuy` | TField |  | Denotes long short indicator for buy |
| 71 | `SECTRAS.PARAM.LS.IND.SELL` | `DesctxSectrasParameter_LsIndSell` | TField |  | Denotes long short indicator for sell |
| 72 | `SECTRAS.PARAM.PAYMENT.TYPE.BUY` | `DesctxSectrasParameter_PaymentTypeBuy` | TField |  | Denotes payment type indicator for buy |
| 73 | `SECTRAS.PARAM.PAYMENT.TYPE.SELL` | `DesctxSectrasParameter_PaymentTypeSell` | TField |  | Denotes payment type indicator for sell |
| 74 | `SECTRAS.PARAM.OFS.SOURCE.ID` | `DesctxSectrasParameter_OfsSourceId` | TField |  | Field to store the OFS Source Id. Should be a valid record in OFS.SOURCE |
| 75 | `SECTRAS.PARAM.APPLICATION.NAME` | `DesctxSectrasParameter_ApplicationName` |  |  |  |
| 76 | `SECTRAS.PARAM.APPLICATION.DFE.MAPPING` | `DesctxSectrasParameter_ApplicationDfeMapping` |  |  |  |
| 77 | `SECTRAS.PARAM.EXCLUDE.SAT.CA` | `DesctxSectrasParameter_ExcludeSatCa` |  |  |  |
| 78 | `SECTRAS.PARAM.RIGHTS.DIS.OPT.DIV.DT` | `DesctxSectrasParameter_RightsDisOptDivDt` |  |  |  |
| 79 | `SECTRAS.PARAM.CASH.OR.STOCK.EVENTS` | `DesctxSectrasParameter_CashOrStockEvents` |  |  |  |
| 80 | `SECTRAS.PARAM.DVP.FLAG` | `DesctxSectrasParameter_DvpFlag` | TField |  | This field indicates if DvP Transfers are applicable Yes or No field |
