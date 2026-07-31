# CG.STAPLES.MANUAL.ALLOC — Table Schema

> Source: `INSERTS/I_F.CG.STAPLES.MANUAL.ALLOC` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.SMA.PORTFOLIO.ID` | `CgStaplesManualAlloc_PortfolioId` | TField | Yes | This field holds the valid portfolio id Mandatory Input. |
| 2 | `CG.SMA.SECURITY.MASTER` | `CgStaplesManualAlloc_SecurityMaster` | TField | Yes | This field holds the valid security code Must be defined as parent stapled security Mandatory Input. |
| 3 | `CG.SMA.RETRIEVE.LOT` | `CgStaplesManualAlloc_RetrieveLot` | TField |  | When set to Yes and validated, the system will retrieve the lots from CG.TXN.BASE and will unallocate all thedisposaltransactions that has taken place after portfolio lock date and present both the open lots (afterunallocation) andthe sell transactions (All disposals after the portfolio lock dates). All multi value sets will bedisplayed in thesame sequence as it is present in CG.TXN.BASE Allowed Values: YES/Blank |
| 4 | `CG.SMA.CALC.CG` | `CgStaplesManualAlloc_CalcCg` | TField |  | Once the user manually allocates the parcels and set this field to yes and validate, system will calculate the CGbased on the new allocation. Allowed Values: YES/Blank |
| 5 | `CG.SMA.PARENT.TAX.LOT.ID` | `CgStaplesManualAlloc_ParentTaxLotId` |  |  |  |
| 6 | `CG.SMA.NOMINAL` | `CgStaplesManualAlloc_Nominal` |  |  |  |
| 7 | `CG.SMA.TXN.TYPE` | `CgStaplesManualAlloc_TxnType` |  |  |  |
| 8 | `CG.SMA.PARENT.LOT.ALLOCATE` | `CgStaplesManualAlloc_ParentLotAllocate` |  |  |  |
| 9 | `CG.SMA.NOMINAL.ALLOCATE` | `CgStaplesManualAlloc_NominalAllocate` |  |  |  |
| 10 | `CG.SMA.SYS.PARENT.LOT.ALLOCATE` | `CgStaplesManualAlloc_SysParentLotAllocate` |  |  |  |
| 11 | `CG.SMA.SYS.NOMINAL.ALLOCATE` | `CgStaplesManualAlloc_SysNominalAllocate` |  |  |  |
| 12 | `CG.SMA.CG.PL` | `CgStaplesManualAlloc_CgPl` |  |  |  |
| 13 | `CG.SMA.TOT.CG.PL` | `CgStaplesManualAlloc_TotCgPl` | TField |  | This field holds the sum of all CG.PL No input field, system updated field |
| 14 | `CG.SMA.LOCAL.REF` | `CgStaplesManualAlloc_LocalRef` |  |  |  |
| 15 | `CG.SMA.OVERRIDE` | `CgStaplesManualAlloc_Override` |  |  |  |
| 16 | `CG.SMA.RECORD.STATUS` | `CgStaplesManualAlloc_RecordStatus` | String |  |  |
| 17 | `CG.SMA.CURR.NO` | `CgStaplesManualAlloc_CurrNo` | String |  |  |
| 18 | `CG.SMA.INPUTTER` | `CgStaplesManualAlloc_Inputter` |  |  |  |
| 19 | `CG.SMA.DATE.TIME` | `CgStaplesManualAlloc_DateTime` |  |  |  |
| 20 | `CG.SMA.AUTHORISER` | `CgStaplesManualAlloc_Authoriser` | String |  |  |
| 21 | `CG.SMA.CO.CODE` | `CgStaplesManualAlloc_CoCode` | String |  |  |
| 22 | `CG.SMA.DEPT.CODE` | `CgStaplesManualAlloc_DeptCode` | String |  |  |
| 23 | `CG.SMA.AUDITOR.CODE` | `CgStaplesManualAlloc_AuditorCode` | String |  |  |
| 24 | `CG.SMA.AUDIT.DATE.TIME` | `CgStaplesManualAlloc_AuditDateTime` | String |  |  |
