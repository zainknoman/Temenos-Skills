# CG.MANUAL.ALLOC — Table Schema

> Source: `INSERTS/I_F.CG.MANUAL.ALLOC` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.MA.PORTFOLIO.NO` | `CgManualAlloc_PortfolioNo` | TField | Yes | This field holds the valid portfolio id Mandatory Input. |
| 2 | `CG.MA.GROUP.NAME` | `CgManualAlloc_GroupName` | TField |  | Field will hold the Portfolio group name This will be the second half of the ID i.e the name of the Portfolio group No input, system generated field |
| 3 | `CG.MA.SECURITY.NO` | `CgManualAlloc_SecurityNo` | TField | Yes | This field holds the valid security code Mandatory Input. |
| 4 | `CG.MA.EXT.CUSTODIAN` | `CgManualAlloc_ExtCustodian` | TField |  | This field holds the External custodian id. |
| 5 | `CG.MA.CG.TXN.BASE` | `CgManualAlloc_CgTxnBase` | TField |  | This field will hold the CG.TXN.BASE id based on the inputted values in the fields Portfolio, Security code,external custodian No input, system generated field |
| 6 | `CG.MA.SECURITY.CCY` | `CgManualAlloc_SecurityCcy` | TField |  | This field holds the security currency No input, system generated field |
| 7 | `CG.MA.CG.CURRENCY` | `CgManualAlloc_CgCurrency` | TField |  | This field will hold the currency in which capital gains is calculated. This will hold the local currency if CG.CALC.LCY field is set to YES in CG.PARAMETER record else with securitycurrency. |
| 8 | `CG.MA.RETRIEVE.LOT` | `CgManualAlloc_RetrieveLot` | TField |  | When set to Yes and validated, the system will retrieve the lots from CG.TXN.BASE , unallocate all the disposaltransactions that has taken place after portfolio lock date and present both the open lots (after unallocation) andthe sell transactions (All disposals after the portfolio lock dates). All multi value sets will be displayed in thesame sequence as it is present in CG.TXN.BASE Allowed Values: YES/Blank |
| 9 | `CG.MA.CALC.CG` | `CgManualAlloc_CalcCg` | TField |  | Once the user manually allocates the parcels and set this field to yes and validate, system will calculate the CGbased on the new allocation. Allowed Values: YES/Blank |
| 10 | `CG.MA.TRADE.DATE.TIME` | `CgManualAlloc_TradeDateTime` |  |  |  |
| 11 | `CG.MA.EFFECTIVE.DATE` | `CgManualAlloc_EffectiveDate` |  |  |  |
| 12 | `CG.MA.SEC.TRANS.ID` | `CgManualAlloc_SecTransId` |  |  |  |
| 13 | `CG.MA.TAX.LOT.ID` | `CgManualAlloc_TaxLotId` |  |  |  |
| 14 | `CG.MA.TXN.TYPE` | `CgManualAlloc_TxnType` |  |  |  |
| 15 | `CG.MA.TRD.NOMINAL` | `CgManualAlloc_TrdNominal` |  |  |  |
| 16 | `CG.MA.CG.NOMINAL` | `CgManualAlloc_CgNominal` |  |  |  |
| 17 | `CG.MA.CG.TRD.COST` | `CgManualAlloc_CgTrdCost` |  |  |  |
| 18 | `CG.MA.CG.REDUCED.COST` | `CgManualAlloc_CgReducedCost` |  |  |  |
| 19 | `CG.MA.CG.INDEXED.COST` | `CgManualAlloc_CgIndexedCost` |  |  |  |
| 20 | `CG.MA.CG.ORIGINAL.COST` | `CgManualAlloc_CgOriginalCost` |  |  |  |
| 21 | `CG.MA.COST.PER.UNIT` | `CgManualAlloc_CostPerUnit` |  |  |  |
| 22 | `CG.MA.CG.PL` | `CgManualAlloc_CgPl` |  |  |  |
| 23 | `CG.MA.ORIG.CG.PL` | `CgManualAlloc_OrigCgPl` |  |  |  |
| 24 | `CG.MA.PUR.TXN.ID` | `CgManualAlloc_PurTxnId` |  |  |  |
| 25 | `CG.MA.PUR.TAX.LOT.ID` | `CgManualAlloc_PurTaxLotId` |  |  |  |
| 26 | `CG.MA.PUR.TXN.NOM` | `CgManualAlloc_PurTxnNom` |  |  |  |
| 27 | `CG.MA.PUR.CG.PL` | `CgManualAlloc_PurCgPl` |  |  |  |
| 28 | `CG.MA.ORIG.PUR.TXN.ID` | `CgManualAlloc_OrigPurTxnId` |  |  |  |
| 29 | `CG.MA.ORIG.PUR.TAX.LOT.ID` | `CgManualAlloc_OrigPurTaxLotId` |  |  |  |
| 30 | `CG.MA.ORIG.PUR.TXN.NOM` | `CgManualAlloc_OrigPurTxnNom` |  |  |  |
| 31 | `CG.MA.ORIG.PUR.CG.PL` | `CgManualAlloc_OrigPurCgPl` |  |  |  |
| 32 | `CG.MA.MANUAL.ALLOCATION` | `CgManualAlloc_ManualAllocation` |  |  |  |
| 33 | `CG.MA.CG.METHOD` | `CgManualAlloc_CgMethod` |  |  |  |
| 34 | `CG.MA.TOT.CG.PL` | `CgManualAlloc_TotCgPl` | TField |  | This field holds the sum of all CG.PL No input field, system updated field |
| 35 | `CG.MA.TOT.ORIG.CG.PL` | `CgManualAlloc_TotOrigCgPl` | TField |  | This field will hold the sum of all original CG.PL No input field, system updated field |
| 36 | `CG.MA.TOT.CG.DIFFERENCE` | `CgManualAlloc_TotCgDifference` | TField |  | This field will hold the difference between the TOT.CG.PL and TOT.ORIG.CG.PL No input field, system updated field |
| 37 | `CG.MA.LOCAL.REF` | `CgManualAlloc_LocalRef` |  |  |  |
| 38 | `CG.MA.OVERRIDE` | `CgManualAlloc_Override` |  |  |  |
| 39 | `CG.MA.RECORD.STATUS` | `CgManualAlloc_RecordStatus` | String |  |  |
| 40 | `CG.MA.CURR.NO` | `CgManualAlloc_CurrNo` | String |  |  |
| 41 | `CG.MA.INPUTTER` | `CgManualAlloc_Inputter` |  |  |  |
| 42 | `CG.MA.DATE.TIME` | `CgManualAlloc_DateTime` |  |  |  |
| 43 | `CG.MA.AUTHORISER` | `CgManualAlloc_Authoriser` | String |  |  |
| 44 | `CG.MA.CO.CODE` | `CgManualAlloc_CoCode` | String |  |  |
| 45 | `CG.MA.DEPT.CODE` | `CgManualAlloc_DeptCode` | String |  |  |
| 46 | `CG.MA.AUDITOR.CODE` | `CgManualAlloc_AuditorCode` | String |  |  |
| 47 | `CG.MA.AUDIT.DATE.TIME` | `CgManualAlloc_AuditDateTime` | String |  |  |
| 48 | `CG.MA.SYS.PUR.TXN.ID` | `CgManualAlloc_SysPurTxnId` |  |  |  |
| 49 | `CG.MA.SYS.PUR.TAX.LOT.ID` | `CgManualAlloc_SysPurTaxLotId` |  |  |  |
| 50 | `CG.MA.SYS.PUR.TXN.NOM` | `CgManualAlloc_SysPurTxnNom` |  |  |  |
