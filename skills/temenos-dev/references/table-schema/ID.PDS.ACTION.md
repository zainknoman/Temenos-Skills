# ID.PDS.ACTION — Table Schema

> Source: `INSERTS/I_F.ID.PDS.ACTION` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPA.ACTION` | `IdPdsAction_Action` | TField | Yes | This defines the PDS action to be performed. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Field Mandatory 3. For Options other than Simulate and Projection all below fields are No Input. |
| 2 | `ID.IPA.POOL.REF` | `IdPdsAction_PoolRef` | TField | Yes | This field holds the reference of the pool parameter. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Field Mandatory. 3. Must be a valid record from the file ID.POOL.PARAMETER. |
| 3 | `ID.IPA.START.DATE` | `IdPdsAction_StartDate` | TField | Yes | The start date from which the PDS calculation to be performed. Validation Rules: 1. Must be a standard T24 date field. 2. Field Mandatory 3. Should be GT last DISTRIB.DATE of ID.PDS.DISTRIB.DETAILS |
| 4 | `ID.IPA.END.DATE` | `IdPdsAction_EndDate` | TField | Yes | The end date from which the PDS calculation to be performed. Validation Rules: 1. Must be a standard T24 date field. 2. Field Mandatory. 3. Should be LT TODAY. |
| 5 | `ID.IPA.SH.CALC.TYPE` | `IdPdsAction_ShCalcType` | TField |  | The method in which the Share Holder's funds to be handled. Validation Rules: 1. Valid values are Manual, AssetLiab and Account. |
| 6 | `ID.IPA.SH.AMOUNT` | `IdPdsAction_ShAmount` | TField |  | The Share Holder investment amount to be used for calculation. |
| 7 | `ID.IPA.SH.INV.PERCENT` | `IdPdsAction_ShInvPercent` | TField |  | The Share Holder investment percentage to be used for calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 8 | `ID.IPA.SH.ADD.EXCL.ACCT.BAL` | `IdPdsAction_ShAddExclAcctBal` | TField |  | The option to choose if the excluded account average balances should be added to Share Holder's Equity funds as non-invested portion. Validation Rules: 1. Valid values are 'Y' and NULL while checking and unchecking the checkbox respectively. |
| 9 | `ID.IPA.SH.ADD.WT.DEPOSIT.BAL` | `IdPdsAction_ShAddWtDepositBal` | TField |  | The option to choose if the deposit unutilised weightage balances should be added to Share Holder's Equity funds as non-invested portion. Validation Rules: 1. Valid values are 'Y' and NULL while checking and unchecking the checkbox respectively. |
| 10 | `ID.IPA.SH.ADD.EARLY.MAT.BAL` | `IdPdsAction_ShAddEarlyMatBal` | TField |  | The option to choose if the early matured deposit last period should be added to Share Holder's Equity funds as non-invested portion. Validation Rules: 1. Valid values are 'Y' and NULL while checking and unchecking the checkbox respectively. |
| 11 | `ID.IPA.SH.ADD.WAK.DEP.BAL` | `IdPdsAction_ShAddWakDepBal` | TField |  | The option to choose if the wakala deposit should be added to Share Holder's Equity funds as non-invested portion. |
| 12 | `ID.IPA.OTHER.INCOME.AMOUNT` | `IdPdsAction_OtherIncomeAmount` | TField |  | The other income amount to be used for the PDS calculation.Value of this field should be mentioned in the Pool Currency. |
| 13 | `ID.IPA.OTHER.EXPENSE.AMOUNT` | `IdPdsAction_OtherExpenseAmount` | TField |  | The other expense amount to be used for the PDS calculation.Value of this field should be mentioned in the Pool Currency. |
| 14 | `ID.IPA.IRR.PERCENT` | `IdPdsAction_IrrPercent` | TField |  | The investment risk reserve percentage to be used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 15 | `ID.IPA.IRR.AMOUNT` | `IdPdsAction_IrrAmount` | TField |  | The investment risk reserve amount to be used for the PDS calculation. Validation Rules: 1. Must be a valid record from the table IS.PARAMETER. |
| 16 | `ID.IPA.PER.PERCENT` | `IdPdsAction_PerPercent` | TField |  | The profit equalisation reserve percentage to be used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 17 | `ID.IPA.PER.AMOUNT` | `IdPdsAction_PerAmount` | TField |  | The profit equalisation reserve amount to be used for the PDS calculation. Validation Rules: 1. Must be a valid percentage field. 2. Value should be in the range 0 to 100 with maximum of 2 decimal places. |
| 18 | `ID.IPA.REVERSAL.REF` | `IdPdsAction_ReversalRef` | TField |  | This field should display the list of records from ID.PDS.ACTION table. Validation Rules: 1. This field is used to capture reversed PDS distribution record reference number. 2. It is not required to capture any value to this field for creating simulation without reversal. |
| 19 | `ID.IPA.LAST.DIST.RUN.DATE` | `IdPdsAction_LastDistRunDate` | TField |  | This field displays the run date of the previous profit distribution ID.PDS.ACTION in the field REVERSAL.REF |
| 20 | `ID.IPA.RESERVED.3` | `IdPdsAction_Reserved3` |  |  |  |
| 21 | `ID.IPA.RESERVED.2` | `IdPdsAction_Reserved2` |  |  |  |
| 22 | `ID.IPA.RESERVED.1` | `IdPdsAction_Reserved1` |  |  |  |
| 23 | `ID.IPA.LOCAL.REF` | `IdPdsAction_LocalRef` |  |  |  |
| 24 | `ID.IPA.STMT.NOS` | `IdPdsAction_StmtNos` |  |  |  |
| 25 | `ID.IPA.OVERRIDE` | `IdPdsAction_Override` |  |  |  |
| 26 | `ID.IPA.RECORD.STATUS` | `IdPdsAction_RecordStatus` | String |  |  |
| 27 | `ID.IPA.CURR.NO` | `IdPdsAction_CurrNo` | String |  |  |
| 28 | `ID.IPA.INPUTTER` | `IdPdsAction_Inputter` |  |  |  |
| 29 | `ID.IPA.DATE.TIME` | `IdPdsAction_DateTime` |  |  |  |
| 30 | `ID.IPA.AUTHORISER` | `IdPdsAction_Authoriser` | String |  |  |
| 31 | `ID.IPA.CO.CODE` | `IdPdsAction_CoCode` | String |  |  |
| 32 | `ID.IPA.DEPT.CODE` | `IdPdsAction_DeptCode` | String |  |  |
| 33 | `ID.IPA.AUDITOR.CODE` | `IdPdsAction_AuditorCode` | String |  |  |
| 34 | `ID.IPA.AUDIT.DATE.TIME` | `IdPdsAction_AuditDateTime` | String |  |  |
