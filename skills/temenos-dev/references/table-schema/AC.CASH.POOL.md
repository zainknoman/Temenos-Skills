# AC.CASH.POOL — Table Schema

> Source: `INSERTS/I_F.AC.CASH.POOL` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CP.GROUP.ID` | `AcCashPool_GroupId` | TField | Yes | This mandatory field defines which group this Account is to be included in, this will be used for checking the Account currency and the options set in the AC.CP.GROUP.PARAM. If the related field SUB.GROUP has been entered then this field will automatically default since the relationship already exists. Validation Rules: Must be a valid id on the AC.CP.GROUP.PARAM file |
| 2 | `AC.CP.SUB.GROUP` | `AcCashPool_SubGroup` | TField |  | The sub group that this pool belongs to. A group may be split into many subgroups to enable a subgroup to be processed separately via the on line application INTRA.DAY.SWEEP. Validation Rules: Must be a valid ID on the AC.CP.GROUP.PARAM file Must have been defined as a sub group on the AC.CP.GROUP.PARAM file. |
| 3 | `AC.CP.MAIN.DEPOSIT` | `AcCashPool_MainDeposit` | TField |  | NOINPUT field. This field is not used at present. |
| 4 | `AC.CP.MAIN.MASTER` | `AcCashPool_MainMaster` | TField |  | The Account that is defined as the Main Master on AC.CP.GROUP.PARAM. The field is defaulted by the system on entering the GROUP.ID and is not user accessible. Validation Rules: No user input |
| 5 | `AC.CP.CURRENT.BALANCE` | `AcCashPool_CurrentBalance` | TField |  | A non input system generated field that shows the balance for this cash pool account. The balance shown depends on the BALANCE.TO.USE field set in the pools corresponding group parameter record. If this pool record is seen via the input function then the balance shown will be its current balance. If it is viewed via the See function then it will be the balance of the account , the last time the pool record was updated , either online or during the end of day run. It is merely a visual aid only. |
| 6 | `AC.CP.SEQUENCE` | `AcCashPool_Sequence` | TField | Yes | The sequence in which this cash pool record will be processed within the group. There is the option to sequence automatically via the SEQUENCING field on the AC.CP.GROUP.PARAM record. If this is set then this field becomes no input. Typical input would be low sequence number for the top of the group and higher numbers for those lower in the pyramid. The processing is in descending order, so the rules in the lowest part of the pyramid usually get effected first (as they usually have higher sequence numbers). Validation Rules: Mandatory when SEQUENCING = MANUAL |
| 7 | `AC.CP.LINK.ACCT` | `AcCashPool_LinkAcct` |  |  |  |
| 8 | `AC.CP.RULE` | `AcCashPool_Rule` |  |  |  |
| 9 | `AC.CP.ID.BAL.TYPE` | `AcCashPool_IdBalType` |  |  |  |
| 10 | `AC.CP.LINK.BAL.TYPE` | `AcCashPool_LinkBalType` |  |  |  |
| 11 | `AC.CP.CASHFLOW.AMT` | `AcCashPool_CashflowAmt` |  |  |  |
| 12 | `AC.CP.AGREGATE.BAL` | `AcCashPool_AgregateBal` |  |  |  |
| 13 | `AC.CP.DR.NARR.TXT` | `AcCashPool_DrNarrTxt` |  |  |  |
| 14 | `AC.CP.CR.NARR.TXT` | `AcCashPool_CrNarrTxt` |  |  |  |
| 15 | `AC.CP.FREQUENCY` | `AcCashPool_Frequency` |  |  |  |
| 16 | `AC.CP.MINIMUM.AMT` | `AcCashPool_MinimumAmt` |  |  |  |
| 17 | `AC.CP.MAXIMUM.AMT` | `AcCashPool_MaximumAmt` |  |  |  |
| 18 | `AC.CP.OVERRIDE.AMT` | `AcCashPool_OverrideAmt` |  |  |  |
| 19 | `AC.CP.OVERRIDE.PERCNT` | `AcCashPool_OverridePercnt` |  |  |  |
| 20 | `AC.CP.AMT.ROUTINE` | `AcCashPool_AmtRoutine` |  |  |  |
| 21 | `AC.CP.UP.TO.AMOUNT` | `AcCashPool_UpToAmount` |  |  |  |
| 22 | `AC.CP.UP.TO.PERCENT` | `AcCashPool_UpToPercent` |  |  |  |
| 23 | `AC.CP.RULE.PRIORITY` | `AcCashPool_RulePriority` |  |  |  |
| 24 | `AC.CP.SCHEDULE` | `AcCashPool_Schedule` |  |  |  |
| 25 | `AC.CP.EXCH.RATE.SPR` | `AcCashPool_ExchRateSpr` |  |  |  |
| 26 | `AC.CP.MIN.TFR.DR` | `AcCashPool_MinTfrDr` |  |  |  |
| 27 | `AC.CP.MIN.TFR.CR` | `AcCashPool_MinTfrCr` |  |  |  |
| 28 | `AC.CP.ADJ.START.DATE` | `AcCashPool_AdjStartDate` |  |  |  |
| 29 | `AC.CP.NARRATIVE` | `AcCashPool_Narrative` |  |  |  |
| 30 | `AC.CP.LINKS.PRODUCED` | `AcCashPool_LinksProduced` |  |  |  |
| 31 | `AC.CP.LEVEL.NO` | `AcCashPool_LevelNo` | TField |  | System updates the level or hierarchy of Cash pool in the group when a record is added. For future use. Validation Rules: No input -Internal field Updated by System. |
| 32 | `AC.CP.INTEREST.RATE` | `AcCashPool_InterestRate` | TField |  | NOINPUT field. This field is not used at present. |
| 33 | `AC.CP.INTEREST.KEY` | `AcCashPool_InterestKey` | TField |  | NOINPUT field. This field is not used at present. |
| 34 | `AC.CP.INTEREST.SPREAD` | `AcCashPool_InterestSpread` | TField |  | NOINPUT field. This field is not used at present. |
| 35 | `AC.CP.INT.LIQ.ACCT` | `AcCashPool_IntLiqAcct` | TField |  | NOINPUT field. This field is not used at present. |
| 36 | `AC.CP.CATEGORY` | `AcCashPool_Category` | TField |  | NOINPUT field. This field is not used at present. |
| 37 | `AC.CP.LAST.MAINT.DATE` | `AcCashPool_LastMaintDate` | TField |  | Holds the date on which the AC.CASH.POOL record got created or changed. If a live AC.CASH.POOL record is changed, then new cash pool link will be created with the latest details. In such case, for those links, any transaction done with a back value date before the maintained date will not get processed and no adjustment entries will be raised. Validation Rules: No input- Internal field |
| 38 | `AC.CP.MULTI.RULE` | `AcCashPool_MultiRule` | TField |  | Value as given in Multi rule in the respective cash pool group parameter is defaulted here. Cash pool with multi-rule is created to handle the cases where there is a restriction on the number of entries to Accounts. When multi-rule is set to "Yes" - then the cash pool should be created with two links-consists of Surplus and maintenance sweep rules and the frequency component for the maintenance should be greater than surplus sweep. For example surplus is mentioned as "BSNSS-Daily" then the Maintenance sweep should be either "Weekly" or "Monthly". Also the rules priority should be given at the cash pool level to prioritize the execution of cash pool links. Refer to multi-rule field at group level and AI-Accounts, Interest and Charges user guide related to Cash pool section for more details. Validation Rules: No input-updated by System. |
| 39 | `AC.CP.RTN.WITH.SW.AMT` | `AcCashPool_RtnWithSwAmt` | TField |  | If set to YES then the system expects the local routine to have 4 parameters in the following order: 1. Balance of TO account 2. Balance of FROM account 3. Sweep amount calculated by system4. Cash pool link record.Except paremeter 3, all the other parameters are input parameters and are not supposed to be modified by the local routine. Sweep amount is an input/output parameter and the modified value from the local routine will be used by the system as the final sweep amount. Validation Rules: Must be either YES or blank |
| 40 | `AC.CP.CHARGE.CODE` | `AcCashPool_ChargeCode` | TField | Conditional | Defines the charge that is to be collected for setting up the sweep instruction. Accepts valid record ID of FT.CHARGE.TYPE/FT.COMMISSION.TYPE. Note - Care must be taken to define a fixed charge amount either in FT.CHARGE.TYPE or FT.COMMISSION.TYPE. Otherwise, charge amount is a mandatory input. After collecting the charge amount, field is set to null. Optional field. |
| 41 | `AC.CP.CHARGE.AMOUNT` | `AcCashPool_ChargeAmount` | TField |  | Defines the fixed charge amount associated with the CHARGE.CODE field. |
| 42 | `AC.CP.CHARGE.ACCOUNT` | `AcCashPool_ChargeAccount` | TField |  | Defines the account from which the charge is to be collected. |
| 43 | `AC.CP.TAX.AMOUNT` | `AcCashPool_TaxAmount` | TField |  | The tax amount corresponding to the charges defined in "CHARGE.CODE" field. |
| 44 | `AC.CP.SWEEP.CHG.CODE` | `AcCashPool_SweepChgCode` | TField | No | Defines the charge code associated with the charge that is to be collected for each successful sweep. Value is defaulted from AC.CP.GROUP.PARAM which can be amended by the user. Optional field. |
| 45 | `AC.CP.SWEEP.CHG.AMOUNT` | `AcCashPool_SweepChgAmount` | TField |  | Defines the fixed charge amount to be collected for each sweep. System calculated, if not input by the user. |
| 46 | `AC.CP.WAIVE.CHARGES` | `AcCashPool_WaiveCharges` | TField |  | Defines whether charge is to be collected or not, for each successful sweep |
| 47 | `AC.CP.SUSP.START.DATE` | `AcCashPool_SuspStartDate` | TField |  | Holds the start date for suspending the sweep. No sweep will be done between this date and the date defined in SUSP.END.DATE. |
| 48 | `AC.CP.SUSP.END.DATE` | `AcCashPool_SuspEndDate` | TField |  | Holds the end date for suspending the sweep. No sweep will be done between the date defined in SUSP.START.DATE and this date, |
| 49 | `AC.CP.SWEEP.CANCEL.DATE` | `AcCashPool_SweepCancelDate` | TField |  | Holds the end date for the sweep record. The record will become inactive after this date, which means that no sweep will be executed after this date. |
| 50 | `AC.CP.ALLOCATE.SWEEP.AMT` | `AcCashPool_AllocateSweepAmt` | TField |  | When there are multiple link accounts, this option allows to treat the Sweeps as a Single sweep or Multiple Sweeps. If this option is Checked (Y), the sweep will be treated as a Single Sweep. Only one record will be generated in AC.CASH.POOL.LINK If this option is left blank, then it means NO and sweep for each of the link accounts will be treated as a separate sweep. Records will be generated in AC.CASH.POOL.LINK based on the number of link accounts. Example : If there are 3 Link accounts and Allocate Sweep is Y, a single record will be generated in AC.CASH.POOL.LINK. The debit/credit from/to the Main Account will be showed as a single entry.In the same case, if Allocate Sweep is N, 3 records will be generated in AC.CASH.POOL.LINK. The debit/credit from/to the Main Account will be shown as 3 different entries. Validation Rules: Amendment not allowed after authorization |
| 51 | `AC.CP.LOCAL.REF` | `AcCashPool_LocalRef` |  |  |  |
| 52 | `AC.CP.CB.SWEEP.ACCOUNT` | `AcCashPool_CbSweepAccount` | TField | Yes | Account field. Counter Booking Account for the ID Account. This Account is used by the system to raise an equal and opposite entry posted against ID Account Validation Rules: Mandatory when BACK.TO.BACK.FX field is set as YES in the Rule (AC.SWEEP.TYPE) record. Should belong to same pool as ID and Link account. Should have same currency as ID Account. Should have the balance type as MEMO |
| 53 | `AC.CP.CB.LINK.ACCOUNT` | `AcCashPool_CbLinkAccount` | TField | Yes | Account field. Counter Booking Account for the Link Account. This Account is used by the system to raise an equal and opposite entry posted against Link Account Validation Rules: Mandatory when BACK.TO.BACK.FX field is set as YES in the Rule (AC.SWEEP.TYPE) record. Should belong to same pool as ID and Link account. Should have same currency as Link Account. Should have the balance type as MEMO |
| 54 | `AC.CP.SUSPEND.INDEFINITE` | `AcCashPool_SuspendIndefinite` | TField |  | Field to indicate if sweep has to be suspended indefinitely. When Suspend start date is defined and if this flagis set to "Yes" in the absence of Suspend end date, then sweep will be suspended indefinitely till a date isspecified for ending the suspension. Validation Rules: Can be defined only when SUSP.START.DATE is defined. Cannot be defined in the presence of value in SUSP.END.DATE. |
| 55 | `AC.CP.DATE.ADJUSTMENT` | `AcCashPool_DateAdjustment` | TField |  | Specifies how the date has to be calculated if the frequency is a holiday |
| 56 | `AC.CP.BUS.DAY.DEFN` | `AcCashPool_BusDayDefn` |  |  |  |
| 57 | `AC.CP.STMT.NOS` | `AcCashPool_StmtNos` |  |  |  |
| 58 | `AC.CP.OVERRIDE` | `AcCashPool_Override` |  |  |  |
| 59 | `AC.CP.RECORD.STATUS` | `AcCashPool_RecordStatus` | String |  |  |
| 60 | `AC.CP.CURR.NO` | `AcCashPool_CurrNo` | String |  |  |
| 61 | `AC.CP.INPUTTER` | `AcCashPool_Inputter` |  |  |  |
| 62 | `AC.CP.DATE.TIME` | `AcCashPool_DateTime` |  |  |  |
| 63 | `AC.CP.AUTHORISER` | `AcCashPool_Authoriser` | String |  |  |
| 64 | `AC.CP.CO.CODE` | `AcCashPool_CoCode` | String |  |  |
| 65 | `AC.CP.DEPT.CODE` | `AcCashPool_DeptCode` | String |  |  |
| 66 | `AC.CP.AUDITOR.CODE` | `AcCashPool_AuditorCode` | String |  |  |
| 67 | `AC.CP.AUDIT.DATE.TIME` | `AcCashPool_AuditDateTime` | String |  |  |
| 68 | `AC.CP.MIN.AMT.TRANSFER` | `AcCashPool_MinAmtTransfer` |  |  |  |
| 69 | `AC.CP.SWEEP.UNIT.AMT` | `AcCashPool_SweepUnitAmt` |  |  |  |
| 70 | `AC.CP.PAYMENT.PRODUCT` | `AcCashPool_PaymentProduct` |  |  |  |
| 71 | `AC.CP.MAX.CONCENTRATION.AMT` | `AcCashPool_MaxConcentrationAmt` |  |  |  |
| 72 | `AC.CP.RETURN.RULE.PRIORITY` | `AcCashPool_ReturnRulePriority` |  |  |  |
| 73 | `AC.CP.TRIGGER.MIN.BAL` | `AcCashPool_TriggerMinBal` |  |  |  |
| 74 | `AC.CP.TRIGGER.MAX.BAL` | `AcCashPool_TriggerMaxBal` |  |  |  |
| 75 | `AC.CP.TRANSFER.AMOUNT` | `AcCashPool_TransferAmount` |  |  |  |
| 76 | `AC.CP.SUSP.SIGN` | `AcCashPool_SuspSign` | TField |  | If the value is Dr, SUSP.START.DATE in AC.CASH.POOL application will be updated and SUSP.SIGN will be updated as DR. Sweep will not be processed by debiting the Sweeping Account. If the value is Cr, SUSP.START.DATE in AC.CASH.POOL application will be updated and SUSP.SIGN will be updated as CR. Sweep will not be processed if any credit to Sweeping Account. |
| 77 | `AC.CP.POOL.CREATION.DATE` | `AcCashPool_PoolCreationDate` | TField |  | Indicates the date on which the cash pool record was created. |
| 78 | `AC.CP.BENEFICIARY.ID` | `AcCashPool_BeneficiaryId` |  |  |  |
