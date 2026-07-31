# CG.TXN.DETS — Table Schema

> Source: `INSERTS/I_F.CG.TXN.DETS` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.DET.GROUP.NAME` | `CgTxnDets_GroupName` | TField |  | Group Name from ID is stored. |
| 2 | `CG.DET.SECURITY.NO` | `CgTxnDets_SecurityNo` | TField |  | Instrument reference from ID is stored |
| 3 | `CG.DET.EXT.CUSTODIAN` | `CgTxnDets_ExtCustodian` | TField |  | External Custodian from ID is stored. |
| 4 | `CG.DET.CURRENCY` | `CgTxnDets_Currency` | TField |  | Currency in which cost bases are represented is stored. |
| 5 | `CG.DET.TAX.LOT.ID` | `CgTxnDets_TaxLotId` |  |  |  |
| 6 | `CG.DET.PORTFOLIO` | `CgTxnDets_Portfolio` |  |  |  |
| 7 | `CG.DET.TXN.ID` | `CgTxnDets_TxnId` |  |  |  |
| 8 | `CG.DET.TRD.DATE.TIME` | `CgTxnDets_TrdDateTime` |  |  |  |
| 9 | `CG.DET.EFF.DATE.TIME` | `CgTxnDets_EffDateTime` |  |  |  |
| 10 | `CG.DET.TXN.TYPE` | `CgTxnDets_TxnType` |  |  |  |
| 11 | `CG.DET.NOMINAL` | `CgTxnDets_Nominal` |  |  |  |
| 12 | `CG.DET.COST` | `CgTxnDets_Cost` |  |  |  |
| 13 | `CG.DET.EXPENSES` | `CgTxnDets_Expenses` |  |  |  |
| 14 | `CG.DET.ACCRUED.INT` | `CgTxnDets_AccruedInt` |  |  |  |
| 15 | `CG.DET.REDUCED.COST` | `CgTxnDets_ReducedCost` |  |  |  |
| 16 | `CG.DET.INDEXED.COST` | `CgTxnDets_IndexedCost` |  |  |  |
| 17 | `CG.DET.CG.NOMINAL` | `CgTxnDets_CgNominal` |  |  |  |
| 18 | `CG.DET.CG.COST` | `CgTxnDets_CgCost` |  |  |  |
| 19 | `CG.DET.CG.EXPENSES` | `CgTxnDets_CgExpenses` |  |  |  |
| 20 | `CG.DET.CG.ACCRUED.INT` | `CgTxnDets_CgAccruedInt` |  |  |  |
| 21 | `CG.DET.CG.REDUCED.COST` | `CgTxnDets_CgReducedCost` |  |  |  |
| 22 | `CG.DET.CG.INDEXED.COST` | `CgTxnDets_CgIndexedCost` |  |  |  |
| 23 | `CG.DET.S.TXN` | `CgTxnDets_STxn` |  |  |  |
| 24 | `CG.DET.D.PORTFOLIO` | `CgTxnDets_DPortfolio` |  |  |  |
| 25 | `CG.DET.D.SECURITY.NO` | `CgTxnDets_DSecurityNo` |  |  |  |
| 26 | `CG.DET.D.EXT.CUSTODIAN` | `CgTxnDets_DExtCustodian` |  |  |  |
| 27 | `CG.DET.S.TAX.LOT.ID` | `CgTxnDets_STaxLotId` |  |  |  |
| 28 | `CG.DET.S.SEC.TRANS.ID` | `CgTxnDets_SSecTransId` |  |  |  |
| 29 | `CG.DET.D.TRD.DATE.TIME` | `CgTxnDets_DTrdDateTime` |  |  |  |
| 30 | `CG.DET.D.EFF.DATE.TIME` | `CgTxnDets_DEffDateTime` |  |  |  |
| 31 | `CG.DET.D.TXN.TYPE` | `CgTxnDets_DTxnType` |  |  |  |
| 32 | `CG.DET.D.NOMINAL` | `CgTxnDets_DNominal` |  |  |  |
| 33 | `CG.DET.D.TRD.COST` | `CgTxnDets_DTrdCost` |  |  |  |
| 34 | `CG.DET.D.EXPENSES` | `CgTxnDets_DExpenses` |  |  |  |
| 35 | `CG.DET.D.ACCRUED.INT` | `CgTxnDets_DAccruedInt` |  |  |  |
| 36 | `CG.DET.D.REDUCED.COST` | `CgTxnDets_DReducedCost` |  |  |  |
| 37 | `CG.DET.D.INDEXED.COST` | `CgTxnDets_DIndexedCost` |  |  |  |
| 38 | `CG.DET.ORIGINAL.COST` | `CgTxnDets_OriginalCost` |  |  |  |
| 39 | `CG.DET.CG.ORIGINAL.COST` | `CgTxnDets_CgOriginalCost` |  |  |  |
| 40 | `CG.DET.DATE.TIME.CGUPDT` | `CgTxnDets_DateTimeCgupdt` |  |  |  |
| 41 | `CG.DET.PARENT.TAX.LOT.ID` | `CgTxnDets_ParentTaxLotId` |  |  |  |
| 42 | `CG.DET.STAPLING.EFF.DATE.TIME` | `CgTxnDets_StaplingEffDateTime` |  |  |  |
| 43 | `CG.DET.UNSTAPLING.EFF.DATE.TIME` | `CgTxnDets_UnstaplingEffDateTime` |  |  |  |
