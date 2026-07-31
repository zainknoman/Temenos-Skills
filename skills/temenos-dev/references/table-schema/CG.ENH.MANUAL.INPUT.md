# CG.ENH.MANUAL.INPUT — Table Schema

> Source: `INSERTS/I_F.CG.ENH.MANUAL.INPUT` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.EMI.PORTFOLIO.NO` | `CgEnhManualInput_PortfolioNo` | TField | Yes | Portfolio (SEC.ACC.MASTER) in which the tax parcel is replaced/modified. Validation Rules: Mandatory Field |
| 2 | `CG.EMI.GROUP.NAME` | `CgEnhManualInput_GroupName` | TField |  | Portfolio group of Portfolio No is updated. Validation Rules : NOINPUT Field. |
| 3 | `CG.EMI.SECURITY.NO` | `CgEnhManualInput_SecurityNo` | TField | Yes | Security (SECURITY.MASTER) for which the tax parcel is being replaced/modified. Validation Rules: Mandatory Field |
| 4 | `CG.EMI.SECURITY.CCY` | `CgEnhManualInput_SecurityCcy` | TField |  | SEC.CURRENCY from CG.TXN.BASE is updated. Validation Rules : NOINPUT Field. |
| 5 | `CG.EMI.MASTER.LOT.REF` | `CgEnhManualInput_MasterLotRef` | TField | Yes | Lot Reference of a Parcel can be given here. Accepts either SEC.TRANS.ID or TAX.LOT.ID of transaction for Portfolio and Security defined. This is the parcel that is getting replaced/modified. Validation Rules : Mandatory field Accepts Reference from a Valid Buy parcel |
| 6 | `CG.EMI.MASTER.TRANS.ID` | `CgEnhManualInput_MasterTransId` | TField |  | Transaction ID of Master Transaction. Field is updated with SEC.TRANS.ID from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 7 | `CG.EMI.MASTER.TAX.LOT.ID` | `CgEnhManualInput_MasterTaxLotId` | TField |  | Tax Lot ID of Master Transaction. Field is updated with TAX.LOT.ID from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 8 | `CG.EMI.MASTER.TRADE.DATE.TIME` | `CgEnhManualInput_MasterTradeDateTime` |  |  |  |
| 9 | `CG.EMI.MASTER.TXN.TYPE` | `CgEnhManualInput_MasterTxnType` | TField |  | Transaction Type of Master Transaction. Field is updated with TXN.TYPE from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 10 | `CG.EMI.MASTER.TRD.NOMINAL` | `CgEnhManualInput_MasterTrdNominal` | TField |  | Acquisition Nominal of Master Transaction. Field is updated with TRD.NOMINAL from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 11 | `CG.EMI.MASTER.TRD.VALUE` | `CgEnhManualInput_MasterTrdValue` | TField |  | Acquisition Cost exclusive of accrued interest and expenses of Master Transaction. Field is updated withTRD.VALUE from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 12 | `CG.EMI.MASTER.ACCRUED.INT` | `CgEnhManualInput_MasterAccruedInt` | TField |  | Expenses of Master Transaction. Field is updated with EXPENSES from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 13 | `CG.EMI.MASTER.EXPENSES` | `CgEnhManualInput_MasterExpenses` | TField |  | Accrued Interest of Master Transaction. Field is updated with ACCRUED.INT from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 14 | `CG.EMI.MASTER.POOL.FACTOR` | `CgEnhManualInput_MasterPoolFactor` | TField |  | Pool Factor of Master Transaction. Field is updated with POOL.FACTOR from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 15 | `CG.EMI.TRANS.ID` | `CgEnhManualInput_TransId` |  |  |  |
| 16 | `CG.EMI.TRADE.DATE.TIME` | `CgEnhManualInput_TradeDateTime` |  |  |  |
| 17 | `CG.EMI.TXN.TYPE` | `CgEnhManualInput_TxnType` |  |  |  |
| 18 | `CG.EMI.TRD.NOMINAL` | `CgEnhManualInput_TrdNominal` |  |  |  |
| 19 | `CG.EMI.TRD.VALUE` | `CgEnhManualInput_TrdValue` |  |  |  |
| 20 | `CG.EMI.ACCRUED.INT` | `CgEnhManualInput_AccruedInt` |  |  |  |
| 21 | `CG.EMI.EXPENSES` | `CgEnhManualInput_Expenses` |  |  |  |
| 22 | `CG.EMI.POOL.FACTOR` | `CgEnhManualInput_PoolFactor` |  |  |  |
| 23 | `CG.EMI.STAPLE.PARCEL.REBUILD` | `CgEnhManualInput_StapleParcelRebuild` | TField |  | Field to identify if attributes of this transactions are allowed to be modfied during Staples rebuilder. This is updated as STAPLE.PARCEL.REBUILD to new transaction created in CG.TXN.BASE. Fields from TRANS.ID to POOL.FACTOR form an associated multi-value group. |
| 24 | `CG.EMI.RESERVED.9` | `CgEnhManualInput_Reserved9` | TField |  |  |
| 25 | `CG.EMI.RESERVED.8` | `CgEnhManualInput_Reserved8` | TField |  |  |
| 26 | `CG.EMI.RESERVED.7` | `CgEnhManualInput_Reserved7` | TField |  |  |
| 27 | `CG.EMI.RESERVED.6` | `CgEnhManualInput_Reserved6` | TField |  |  |
| 28 | `CG.EMI.RESERVED.5` | `CgEnhManualInput_Reserved5` | TField |  |  |
| 29 | `CG.EMI.RESERVED.4` | `CgEnhManualInput_Reserved4` | TField |  |  |
| 30 | `CG.EMI.RESERVED.3` | `CgEnhManualInput_Reserved3` | TField |  |  |
| 31 | `CG.EMI.RESERVED.2` | `CgEnhManualInput_Reserved2` | TField |  |  |
| 32 | `CG.EMI.RESERVED.1` | `CgEnhManualInput_Reserved1` | TField |  |  |
| 33 | `CG.EMI.LOCAL.REF` | `CgEnhManualInput_LocalRef` |  |  |  |
| 34 | `CG.EMI.OVERRIDE` | `CgEnhManualInput_Override` |  |  |  |
| 35 | `CG.EMI.RECORD.STATUS` | `CgEnhManualInput_RecordStatus` | String |  |  |
| 36 | `CG.EMI.CURR.NO` | `CgEnhManualInput_CurrNo` | String |  |  |
| 37 | `CG.EMI.INPUTTER` | `CgEnhManualInput_Inputter` |  |  |  |
| 38 | `CG.EMI.DATE.TIME` | `CgEnhManualInput_DateTime` |  |  |  |
| 39 | `CG.EMI.AUTHORISER` | `CgEnhManualInput_Authoriser` | String |  |  |
| 40 | `CG.EMI.CO.CODE` | `CgEnhManualInput_CoCode` | String |  |  |
| 41 | `CG.EMI.DEPT.CODE` | `CgEnhManualInput_DeptCode` | String |  |  |
| 42 | `CG.EMI.AUDITOR.CODE` | `CgEnhManualInput_AuditorCode` | String |  |  |
| 43 | `CG.EMI.AUDIT.DATE.TIME` | `CgEnhManualInput_AuditDateTime` | String |  |  |
| 44 | `CG.EMI.EXT.CUSTODIAN` | `CgEnhManualInput_ExtCustodian` | TField |  | External Custody to which the transaction corresponds. |
| 45 | `CG.EMI.CG.CURRENCY` | `CgEnhManualInput_CgCurrency` | TField |  | CG.CURRENCY from CG.TXN.BASE is updated. Validation Rules : NOINPUT Field. |
| 46 | `CG.EMI.MASTER.REDUCED.COST` | `CgEnhManualInput_MasterReducedCost` | TField |  | Reduced Cost of Master Transaction. Field is updated with REDUCED.COST from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 47 | `CG.EMI.MASTER.INDEXED.COST` | `CgEnhManualInput_MasterIndexedCost` | TField |  | Indexed Cost of Master Transaction. Field is updated with INDEXED.COST from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 48 | `CG.EMI.REDUCED.COST` | `CgEnhManualInput_ReducedCost` |  |  |  |
| 49 | `CG.EMI.INDEXED.COST` | `CgEnhManualInput_IndexedCost` |  |  |  |
| 50 | `CG.EMI.MASTER.STAPLE.REBUILD` | `CgEnhManualInput_MasterStapleRebuild` | TField |  | Field is updated with STAPLE.REBUILD from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 51 | `CG.EMI.TYPE.OF.INPUT` | `CgEnhManualInput_TypeOfInput` | TField |  | Field to identify type of action to be done. Allowed Values : MODIFICATION If set to MODIFICATION - Attributed of a parcel are allowed to be modified . If set to Blank - A Parcel can be split to multiple parcels. |
| 52 | `CG.EMI.MASTER.EFFECTIVE.DATE` | `CgEnhManualInput_MasterEffectiveDate` | TField |  | Effective Date of Master Transaction. Field is updated with SEC.TRANS.ID from CG.TXN.BASE of MASTER.LOT.REF Validation Rules : NOINPUT field. |
| 53 | `CG.EMI.EFFECTIVE.DATE.TIME` | `CgEnhManualInput_EffectiveDateTime` |  |  |  |
