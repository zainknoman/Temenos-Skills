# CG.STAPLE.ENH.MANUAL.INPUT — Table Schema

> Source: `INSERTS/I_F.CG.STAPLE.ENH.MANUAL.INPUT` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.SMI.PORTFOLIO.NO` | `CgStapleEnhManualInput_PortfolioNo` | TField | Yes | Portfolio (SEC.ACC.MASTER) in which the tax parcel is replaced/modified. Validation Rules: Mandatory Field |
| 2 | `CG.SMI.GROUP.NAME` | `CgStapleEnhManualInput_GroupName` | TField |  | Portfolio group of Portfolio No is updated. Validation Rules : NOINPUT Field. |
| 3 | `CG.SMI.SECURITY.NO` | `CgStapleEnhManualInput_SecurityNo` | TField | Yes | Stapled security (SECURITY.MASTER) for which the tax parcel is being replaced/modified. Validation Rules: Mandatory Field |
| 4 | `CG.SMI.EXT.CUSTODIAN` | `CgStapleEnhManualInput_ExtCustodian` | TField |  |  |
| 5 | `CG.SMI.SECURITY.CCY` | `CgStapleEnhManualInput_SecurityCcy` | TField |  | SEC.CURRENCY from CG.TXN.BASE is updated. Validation Rules : NOINPUT Field. |
| 6 | `CG.SMI.CG.CURRENCY` | `CgStapleEnhManualInput_CgCurrency` | TField |  | CG.CURRENCY from CG.TXN.BASE is updated. Validation Rules : NOINPUT Field. |
| 7 | `CG.SMI.TYPE.OF.INPUT` | `CgStapleEnhManualInput_TypeOfInput` | TField |  | Field to identify type of action to be done. Allowed Values : MODIFICATION If set to MODIFICATION - Attributed of a parcel are allowed to be modified . If set to Blank - A Parcel can be split to multiple parcels. |
| 8 | `CG.SMI.MASTER.LOT.REF` | `CgStapleEnhManualInput_MasterLotRef` | TField | Yes | Lot Reference of a Parcel can be given here. Accepts PARENT.TAX.LOT.ID of transaction for Portfolio and Securitydefined. This is the parcel that is getting replaced/modified. Validation Rules : Mandatory field Accepts Reference from a Valid Buy parcel |
| 9 | `CG.SMI.MASTER.TRANS.ID` | `CgStapleEnhManualInput_MasterTransId` |  |  |  |
| 10 | `CG.SMI.MASTER.TAX.LOT.ID` | `CgStapleEnhManualInput_MasterTaxLotId` |  |  |  |
| 11 | `CG.SMI.MASTER.TRADE.DATE.TIME` | `CgStapleEnhManualInput_MasterTradeDateTime` |  |  |  |
| 12 | `CG.SMI.MASTER.EFFECTIVE.DATE` | `CgStapleEnhManualInput_MasterEffectiveDate` |  |  |  |
| 13 | `CG.SMI.MASTER.TXN.TYPE` | `CgStapleEnhManualInput_MasterTxnType` |  |  |  |
| 14 | `CG.SMI.MASTER.TRD.NOMINAL` | `CgStapleEnhManualInput_MasterTrdNominal` |  |  |  |
| 15 | `CG.SMI.MASTER.TRD.VALUE` | `CgStapleEnhManualInput_MasterTrdValue` |  |  |  |
| 16 | `CG.SMI.MASTER.ACCRUED.INT` | `CgStapleEnhManualInput_MasterAccruedInt` |  |  |  |
| 17 | `CG.SMI.MASTER.EXPENSES` | `CgStapleEnhManualInput_MasterExpenses` |  |  |  |
| 18 | `CG.SMI.MASTER.REDUCED.COST` | `CgStapleEnhManualInput_MasterReducedCost` |  |  |  |
| 19 | `CG.SMI.MASTER.INDEXED.COST` | `CgStapleEnhManualInput_MasterIndexedCost` |  |  |  |
| 20 | `CG.SMI.MASTER.STAPLE.REBUILD` | `CgStapleEnhManualInput_MasterStapleRebuild` |  |  |  |
| 21 | `CG.SMI.MASTER.POOL.FACTOR` | `CgStapleEnhManualInput_MasterPoolFactor` |  |  |  |
| 22 | `CG.SMI.MASTER.PARENT.TAX.LOT.ID` | `CgStapleEnhManualInput_MasterParentTaxLotId` |  |  |  |
| 23 | `CG.SMI.TRANS.ID` | `CgStapleEnhManualInput_TransId` |  |  |  |
| 24 | `CG.SMI.TRADE.DATE.TIME` | `CgStapleEnhManualInput_TradeDateTime` |  |  |  |
| 25 | `CG.SMI.EFFECTIVE.DATE.TIME` | `CgStapleEnhManualInput_EffectiveDateTime` |  |  |  |
| 26 | `CG.SMI.TXN.TYPE` | `CgStapleEnhManualInput_TxnType` |  |  |  |
| 27 | `CG.SMI.TRD.NOMINAL` | `CgStapleEnhManualInput_TrdNominal` |  |  |  |
| 28 | `CG.SMI.TRD.VALUE` | `CgStapleEnhManualInput_TrdValue` |  |  |  |
| 29 | `CG.SMI.ACCRUED.INT` | `CgStapleEnhManualInput_AccruedInt` |  |  |  |
| 30 | `CG.SMI.EXPENSES` | `CgStapleEnhManualInput_Expenses` |  |  |  |
| 31 | `CG.SMI.REDUCED.COST` | `CgStapleEnhManualInput_ReducedCost` |  |  |  |
| 32 | `CG.SMI.INDEXED.COST` | `CgStapleEnhManualInput_IndexedCost` |  |  |  |
| 33 | `CG.SMI.POOL.FACTOR` | `CgStapleEnhManualInput_PoolFactor` |  |  |  |
| 34 | `CG.SMI.PARENT.TAX.LOT.ID` | `CgStapleEnhManualInput_ParentTaxLotId` |  |  |  |
| 35 | `CG.SMI.STAPLE.PARCEL.REBUILD` | `CgStapleEnhManualInput_StapleParcelRebuild` | TField |  | Field to identify if attributes of this transactions are allowed to be modified during Staples rebuilder. This isupdated as STAPLE.PARCEL.REBUILD to new transaction created in CG.TXN.BASE. Fields from TRANS.ID to POOL.FACTOR form an associated multi-value group. |
| 36 | `CG.SMI.LOCAL.REF` | `CgStapleEnhManualInput_LocalRef` |  |  |  |
| 37 | `CG.SMI.OVERRIDE` | `CgStapleEnhManualInput_Override` |  |  |  |
| 38 | `CG.SMI.RECORD.STATUS` | `CgStapleEnhManualInput_RecordStatus` | String |  |  |
| 39 | `CG.SMI.CURR.NO` | `CgStapleEnhManualInput_CurrNo` | String |  |  |
| 40 | `CG.SMI.INPUTTER` | `CgStapleEnhManualInput_Inputter` |  |  |  |
| 41 | `CG.SMI.DATE.TIME` | `CgStapleEnhManualInput_DateTime` |  |  |  |
| 42 | `CG.SMI.AUTHORISER` | `CgStapleEnhManualInput_Authoriser` | String |  |  |
| 43 | `CG.SMI.CO.CODE` | `CgStapleEnhManualInput_CoCode` | String |  |  |
| 44 | `CG.SMI.DEPT.CODE` | `CgStapleEnhManualInput_DeptCode` | String |  |  |
| 45 | `CG.SMI.AUDITOR.CODE` | `CgStapleEnhManualInput_AuditorCode` | String |  |  |
| 46 | `CG.SMI.AUDIT.DATE.TIME` | `CgStapleEnhManualInput_AuditDateTime` | String |  |  |
| 47 | `CG.SMI.MASTER.SECURITY.NO` | `CgStapleEnhManualInput_MasterSecurityNo` |  |  |  |
