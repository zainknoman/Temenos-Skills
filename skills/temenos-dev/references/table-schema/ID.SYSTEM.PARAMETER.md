# ID.SYSTEM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ID.SYSTEM.PARAMETER` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.SYS.DESCRIPTION` | `IdSystemParameter_Description` |  |  |  |
| 2 | `ID.SYS.ACCOUNT.SEQ` | `IdSystemParameter_AccountSeq` | TField | Yes | The Account Sequence that could be used for the Profit Distribution System(PDS) accounting entries. Validation Rules: 1. Must not be a record in the table IS.PARAMETER. 2. Field Mandatory for input. |
| 3 | `ID.SYS.DISTRIB.FREQ` | `IdSystemParameter_DistribFreq` | TField |  | The frequency at which the profit has to be distributed for the given deposit products. Validation Rules: 1. Must be a valid frequency field. |
| 4 | `ID.SYS.LAST.FREQ.DATE` | `IdSystemParameter_LastFreqDate` | TField |  | It is the previous date of profit distribution for the frequency based arrangements belong to the accounts category. |
| 5 | `ID.SYS.RESERVED.11` | `IdSystemParameter_Reserved11` |  |  |  |
| 6 | `ID.SYS.PER.TXN.TYPE` | `IdSystemParameter_PerTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Profit Equalization Reserve (PER) Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 7 | `ID.SYS.IRR.TXN.TYPE` | `IdSystemParameter_IrrTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Investment Risk Reserve (IRR) Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 8 | `ID.SYS.HIBA.TXN.TYPE` | `IdSystemParameter_HibaTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for HIBA Payments. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 9 | `ID.SYS.WAK.ADJ.TXN.TYPE` | `IdSystemParameter_WakAdjTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Wakala Adjustment Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 10 | `ID.SYS.PFT.ADJ.TXN.TYPE` | `IdSystemParameter_PftAdjTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Profit Adjustment Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 11 | `ID.SYS.EM.ADJ.TXN.TYPE` | `IdSystemParameter_EmAdjTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for early maturity adjustment entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 12 | `ID.SYS.MUDARIB.TXN.TYPE` | `IdSystemParameter_MudaribTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Mudarib share Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 13 | `ID.SYS.DAYS.POST.MATURITY` | `IdSystemParameter_DaysPostMaturity` | TField |  | Field used to archive PDS processing files. Will hold the value of no. of days to look after maturity of the arrangements, the tracker files ( such as ID.DEPOSIT.TRACKER, ID.ACCOUNT.TRACKER, etc.) will be moved from live to history. Validation Rules: 1. Must be a numeric value from 1 to 366. |
| 14 | `ID.SYS.SPREAD.ADJ.TXN.TYPE` | `IdSystemParameter_SpreadAdjTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for Spread Adjustment Entries. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 15 | `ID.SYS.DEP.PAYOUT.TXN.TYPE` | `IdSystemParameter_DepPayoutTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for profit payment for deposits (PAYOUT). Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 16 | `ID.SYS.DEP.PAYIN.TXN.TYPE` | `IdSystemParameter_DepPayinTxnType` | TField |  | FT.TXN.TYPE.CONDITION or TRANSACTION record to be used for profit payment for deposits (PAYIN). Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 17 | `ID.SYS.AC.PAYOUT.TXN.TYPE` | `IdSystemParameter_AcPayoutTxnType` | TField |  | FT.TXN.TYPE.CONDITION record or TRANSACTION to be used for profit payment for accounts. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 18 | `ID.SYS.ACTION` | `IdSystemParameter_Action` |  |  |  |
| 19 | `ID.SYS.USER.ACTIVITY` | `IdSystemParameter_UserActivity` |  |  |  |
| 20 | `ID.SYS.SPL.HIBA.PO.TXN.TYPE` | `IdSystemParameter_SplHibaPoTxnType` | TField |  | The transaction type to be referenced while raising accounting entries for Profit adjustment. User Configurable field used in the Funds transfer transaction to pay the Special HIBA profit amount to the Customer account on the frequency date. Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 21 | `ID.SYS.SPL.HIBA.TXN.TYPE` | `IdSystemParameter_SplHibaTxnType` | TField |  | The transaction type to be referenced while raising accounting entries for consolidated Profit adjustment . Validation Rules: 1. Valid record from the table FT.TXN.TYPE.CONDITION or TRANSACTION. |
| 22 | `ID.SYS.ACCT.CLOSE.POST.RESTRICT` | `IdSystemParameter_AcctClosePostRestrict` | TField |  | This field captures the posting restriction code. This code will be used to restrict all type of financial transactions after an arrangement is marked for closure during PDS. Validation Rules: 1. Valid record from the table POSTING.RESTRICT. 2. Valid Range is 01 - 89 . |
| 23 | `ID.SYS.MIGRATION.MODE` | `IdSystemParameter_MigrationMode` | TField |  | This field is to be set as 'Yes' if the system is expected to work in migrated environment and to override validations like prevention of opening of arrangements to a older date than its pool available date. |
| 24 | `ID.SYS.DIRECT.PAY.PROFIT` | `IdSystemParameter_DirectPayProfit` | TField | Yes | This field setup is applicable only for Mudaraba savings accounts. It can be set as 'Yes', if Bank does not want to capture [or] perform daily profit accruals by using the Notional profit rate. As and when PDS simulation is performed the profit amount/ profit rate is calculated for the period. During PDS distribution it is required to pay the profit amount calculated during PDS simulation to each Mudaraba savings account immediately. The profit amount is paid as Pay charge to the customer account. In case if it is required to set this field as 'Yes' after running few PDS distributions by using Profit property, then the profit accruals performed by the existing profit properties should be nullified manually for all the Accounts. Non-mandatory. Once it is set as Yes, it is not allowed to modify this field again to Null. |
| 25 | `ID.SYS.RESERVED.5` | `IdSystemParameter_Reserved5` |  |  |  |
| 26 | `ID.SYS.RESERVED.4` | `IdSystemParameter_Reserved4` |  |  |  |
| 27 | `ID.SYS.RESERVED.3` | `IdSystemParameter_Reserved3` |  |  |  |
| 28 | `ID.SYS.RESERVED.2` | `IdSystemParameter_Reserved2` |  |  |  |
| 29 | `ID.SYS.RESERVED.1` | `IdSystemParameter_Reserved1` |  |  |  |
| 30 | `ID.SYS.LOCAL.REF` | `IdSystemParameter_LocalRef` |  |  |  |
| 31 | `ID.SYS.OVERRIDE` | `IdSystemParameter_Override` |  |  |  |
| 32 | `ID.SYS.RECORD.STATUS` | `IdSystemParameter_RecordStatus` | String |  |  |
| 33 | `ID.SYS.CURR.NO` | `IdSystemParameter_CurrNo` | String |  |  |
| 34 | `ID.SYS.INPUTTER` | `IdSystemParameter_Inputter` |  |  |  |
| 35 | `ID.SYS.DATE.TIME` | `IdSystemParameter_DateTime` |  |  |  |
| 36 | `ID.SYS.AUTHORISER` | `IdSystemParameter_Authoriser` | String |  |  |
| 37 | `ID.SYS.CO.CODE` | `IdSystemParameter_CoCode` | String |  |  |
| 38 | `ID.SYS.DEPT.CODE` | `IdSystemParameter_DeptCode` | String |  |  |
| 39 | `ID.SYS.AUDITOR.CODE` | `IdSystemParameter_AuditorCode` | String |  |  |
| 40 | `ID.SYS.AUDIT.DATE.TIME` | `IdSystemParameter_AuditDateTime` | String |  |  |
