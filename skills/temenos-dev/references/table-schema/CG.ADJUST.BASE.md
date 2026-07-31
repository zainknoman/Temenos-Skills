# CG.ADJUST.BASE — Table Schema

> Source: `INSERTS/I_F.CG.ADJUST.BASE` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.ADJB.PORTFOLIO.NO` | `CgAdjustBase_PortfolioNo` | TField |  | The portfolio under which the transaction was enacted. |
| 2 | `CG.ADJB.SECURITY.MASTER` | `CgAdjustBase_SecurityMaster` | TField |  | A valid security master id. |
| 3 | `CG.ADJB.EXT.CUSTODIAN.ID` | `CgAdjustBase_ExtCustodianId` | TField |  | This field will contain the external custodian id for the records that are maintained separately for externalcustody positions. |
| 4 | `CG.ADJB.NARRATIVE` | `CgAdjustBase_Narrative` |  |  |  |
| 5 | `CG.ADJB.TRANSACTION.DATE` | `CgAdjustBase_TransactionDate` | TField |  | The transaction dates for which the adjustment or creation is done for a tax lot |
| 6 | `CG.ADJB.TAX.EFFECTIVE.DATE` | `CgAdjustBase_TaxEffectiveDate` | TField |  | Tax effective date is the date until which the lot has to be fetched from the CG.TXN.BASE |
| 7 | `CG.ADJB.CG.TXN.BASE.ID` | `CgAdjustBase_CgTxnBaseId` | TField |  | This field will contain the id of the CG.TXN.BASE record. The id is in three parts separated by a dot character ".". The first part contains the underlying CUSTOMER id, the second part contains the group to which the portfolio belongs, as defined in PORTFOLIO.GROUPING, therefore indicating the id of the portfolio to which the security belongs. If portfolio groups are not defined then the system will automatically set them up with each portfolio belonging to a unique group with the same id as theportfolio. The third part identifies the security itself. For example: 12435.12435-1.000123-000 Where 12435 is the CUSTOMER id, 12435-1 indicates the portfolio group and 000123-000 indicates the security heldby the customer. |
| 8 | `CG.ADJB.RETRIEVE.LOTS` | `CgAdjustBase_RetrieveLots` | TField |  | This field contains the value (OPEN/OPEN.ON.EFF.DT). If OPEN , the open lots in the CG.TXN.BASE will be retrieved to the CG.ADJUST.BASE table for adjustment If OPEN.ON.EFF.DT, the lots that were open on the TAX.EFFECTIVE DATE are retrieved and displayed |
| 9 | `CG.ADJB.TXN.TYPE` | `CgAdjustBase_TxnType` | TField |  | Indicates, for example, whether the underlying transaction is to decrease or increase Cost the cost or it aReconstruction or Rollover. Example: Decrease Cost ; Increase Cost ; Reconstruct ; RollOver |
| 10 | `CG.ADJB.TOTAL.AMT.TO.ADJUST` | `CgAdjustBase_TotalAmtToAdjust` | TField |  | This is the total of the field ADJ.CG.TRD.COST. For Decrease Cost, this should be negative and For increase Cost,this should be positive |
| 11 | `CG.ADJB.PER.UNIT.COST.ADJ` | `CgAdjustBase_PerUnitCostAdj` | TField |  | This will be the tax cost per unit that needs to be adjusted. For Decrease nominal, this should be negative andFor increase nominal, this should be positive |
| 12 | `CG.ADJB.PER.UNIT.REDUCED.COST` | `CgAdjustBase_PerUnitReducedCost` | TField |  | This will be the reduced cost to be adjusted per unit. For Decrease nominal, this should be negative and Forincrease nominal, this should be positive |
| 13 | `CG.ADJB.TOTAL.UNITS.TO.ADJUST` | `CgAdjustBase_TotalUnitsToAdjust` | TField |  | This is the total units to adjust which will be prorated if apply all is selected when txn type is Recostruct. For Decrease nominal, this should be negative and For increase nominal, this should be positive |
| 14 | `CG.ADJB.APPLY.TO.ALL` | `CgAdjustBase_ApplyToAll` | TField |  | Yes or No field. Default to NO. If this is set to YES and TOTAL.AMT.TO ADUST is given, then prorate theTOTAL.AMT.TO.ADJUST to thefields ADJ.RED.COST, ADJ.CG.TRD.COST. If it is YES and PER.UNIT.COST.ADJ is given, thenupdate the ADJ.CG.TRD.COST andADJ.RED.COST bymultiplying the CG.NOMINAL by the Per unit value. If it is YES andTOTAL.UNITS.TO.ADJUST is given, then apportion this amongthe lots,to the field ADJ.NOMINAL.Cannot be input for"Rollover" transaction |
| 15 | `CG.ADJB.TAX.LOT.ID` | `CgAdjustBase_TaxLotId` |  |  |  |
| 16 | `CG.ADJB.SEC.TRANS.ID` | `CgAdjustBase_SecTransId` |  |  |  |
| 17 | `CG.ADJB.TRANS.TYPE` | `CgAdjustBase_TransType` |  |  |  |
| 18 | `CG.ADJB.CG.NOMINAL` | `CgAdjustBase_CgNominal` |  |  |  |
| 19 | `CG.ADJB.ADJ.NOMINAL` | `CgAdjustBase_AdjNominal` |  |  |  |
| 20 | `CG.ADJB.CG.TRD.COST` | `CgAdjustBase_CgTrdCost` |  |  |  |
| 21 | `CG.ADJB.ADJ.CG.TRD.COST` | `CgAdjustBase_AdjCgTrdCost` |  |  |  |
| 22 | `CG.ADJB.CG.REDUCED.COST` | `CgAdjustBase_CgReducedCost` |  |  |  |
| 23 | `CG.ADJB.ADJ.RED.COST` | `CgAdjustBase_AdjRedCost` |  |  |  |
| 24 | `CG.ADJB.LINK.TXN.ID` | `CgAdjustBase_LinkTxnId` |  |  |  |
| 25 | `CG.ADJB.TOTAL.ORIG.NOMINAL` | `CgAdjustBase_TotalOrigNominal` | TField |  | This will be the total of CG.NOMINAL field of all the open lots. Noinput field |
| 26 | `CG.ADJB.TOTAL.ADJ.NOMINAL` | `CgAdjustBase_TotalAdjNominal` | TField |  | This will be the total of the ADJ.NOMINAL fields. This will be the amount by which the SECURITY.POSITION nominalwill be updated. Noinput field |
| 27 | `CG.ADJB.TOTAL.ADJ.COST` | `CgAdjustBase_TotalAdjCost` | TField |  | This will be the total of the ADJ.CG.TRD.COST fields. This will be the amount by which the SECURITY.POSITION costwill be updated. Noinput field |
| 28 | `CG.ADJB.NEW.SECURITY.ACQUIRED` | `CgAdjustBase_NewSecurityAcquired` | TField |  | Any valid Security Master. Nominals and cost will be rolled to the new security |
| 29 | `CG.ADJB.NEW.UNITS.ACQUIRED` | `CgAdjustBase_NewUnitsAcquired` | TField |  | This field hold the quantity. This will give the ratio in which the nominal has to be rolled over to the newsecurity. Input to this field is allowed only if TXN.TYPE is set as ROLLOVER |
| 30 | `CG.ADJB.ROLLOVER.TYPE` | `CgAdjustBase_RolloverType` | TField |  | Allowed values are FULL or blank . if FULL is selected then the entire nominals and the cost in each open lotswill be rolled to new one If rollover type FULL is not selected then it is considered as partial. The values entered in ADJ.NOMINAL andADJ.CG.TRD.COST will be rolled and theremaining will be still kept in the old security |
| 31 | `CG.ADJB.CREATE.NEW.LOT` | `CgAdjustBase_CreateNewLot` | TField |  | If this field is ticked, then where units are increased, the new units will be created as a separate new lot withacquisition date being the acquisition date of the old parcel.And the effective date of the new parcel will be thetax effective date of the CG.ADJUST.BASE |
| 32 | `CG.ADJB.RESERVED3` | `CgAdjustBase_Reserved3` | TField |  |  |
| 33 | `CG.ADJB.RESERVED2` | `CgAdjustBase_Reserved2` | TField |  |  |
| 34 | `CG.ADJB.RESERVED1` | `CgAdjustBase_Reserved1` | TField |  |  |
| 35 | `CG.ADJB.LOCAL.REF` | `CgAdjustBase_LocalRef` |  |  |  |
| 36 | `CG.ADJB.OVERRIDE` | `CgAdjustBase_Override` |  |  |  |
| 37 | `CG.ADJB.RECORD.STATUS` | `CgAdjustBase_RecordStatus` | String |  |  |
| 38 | `CG.ADJB.CURR.NO` | `CgAdjustBase_CurrNo` | String |  |  |
| 39 | `CG.ADJB.INPUTTER` | `CgAdjustBase_Inputter` |  |  |  |
| 40 | `CG.ADJB.DATE.TIME` | `CgAdjustBase_DateTime` |  |  |  |
| 41 | `CG.ADJB.AUTHORISER` | `CgAdjustBase_Authoriser` | String |  |  |
| 42 | `CG.ADJB.CO.CODE` | `CgAdjustBase_CoCode` | String |  |  |
| 43 | `CG.ADJB.DEPT.CODE` | `CgAdjustBase_DeptCode` | String |  |  |
| 44 | `CG.ADJB.AUDITOR.CODE` | `CgAdjustBase_AuditorCode` | String |  |  |
| 45 | `CG.ADJB.AUDIT.DATE.TIME` | `CgAdjustBase_AuditDateTime` | String |  |  |
| 46 | `CG.ADJB.NEW.SECURITY.QTY` | `CgAdjustBase_NewSecurityQty` |  |  |  |
| 47 | `CG.ADJB.APPORTIONED.COST` | `CgAdjustBase_ApportionedCost` |  |  |  |
| 48 | `CG.ADJB.TAX.LOT.STATUS` | `CgAdjustBase_TaxLotStatus` |  |  |  |
| 49 | `CG.ADJB.CG.NOMINAL.ON.EFF.DATE` | `CgAdjustBase_CgNominalOnEffDate` |  |  |  |
| 50 | `CG.ADJB.CG.TRD.COST.ON.EFF.DATE` | `CgAdjustBase_CgTrdCostOnEffDate` |  |  |  |
| 51 | `CG.ADJB.PARENT.TAX.LOT.ID` | `CgAdjustBase_ParentTaxLotId` |  |  |  |
