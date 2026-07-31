# ESCROW.PAYEE — Table Schema

> Source: `INSERTS/I_F.ESCROW.PAYEE` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.PAY.PAYEE.NAME` | `EscrowPayee_PayeeName` | TField |  | Payee description, if blank will be defaulted from Customer. |
| 2 | `ESCROW.PAY.PAYEE.TYPE` | `EscrowPayee_PayeeType` | TField | Yes | Describes the type of payee loaded. Dropdown field with PAYEE.TYPE virtual table list of values from EB.LOOKUP. Possible values but not limited to: County Tax, Hazard Insurance, PMI, Property Insurance, Real Estate Tax Mandatory input. |
| 3 | `ESCROW.PAY.SETTLEMENT.TYPE` | `EscrowPayee_SettlementType` | TField |  | Type of settlement opted by the payee. This defines the channel that will be used to settle the payee after escrow disbursement activity takes place. |
| 4 | `ESCROW.PAY.COMPANY.CODE` | `EscrowPayee_CompanyCode` |  |  |  |
| 5 | `ESCROW.PAY.DISBURSE.ACC` | `EscrowPayee_DisburseAcc` |  |  |  |
| 6 | `ESCROW.PAY.RESERVED.34` | `EscrowPayee_Reserved34` |  |  |  |
| 7 | `ESCROW.PAY.RESERVED.33` | `EscrowPayee_Reserved33` |  |  |  |
| 8 | `ESCROW.PAY.RESERVED.32` | `EscrowPayee_Reserved32` |  |  |  |
| 9 | `ESCROW.PAY.RESERVED.31` | `EscrowPayee_Reserved31` |  |  |  |
| 10 | `ESCROW.PAY.STATUS` | `EscrowPayee_Status` | TField |  | This field contains the payee status: Active � This status is updated on payee creation. Default status. Inactive � Status marked by user when payee is decommissed. Merged � Represents the payee is merged with another payee. |
| 11 | `ESCROW.PAY.CREATION.DATE` | `EscrowPayee_CreationDate` | TField | No | Date on which the payee was on boarded. User input field. Optional Input. Defaulted to Today. |
| 12 | `ESCROW.PAY.START.DATE` | `EscrowPayee_StartDate` | TField | Yes | Start of first disbursement date from which payment frequency will be cycled to arrive at the next disbursement date. Mandatory input when DISBURSE.FREQ is entered. |
| 13 | `ESCROW.PAY.DISBURSE.FREQ` | `EscrowPayee_DisburseFreq` | TField |  | denotes the frequency on which the payee has to be settled periodically. This field is mutually exclusive with IRREGULAR.PRD field. Both field values cannot co-exist. If the payee is used in ESCROW.ACCOUNT and user does not specify a frequeency, this disbursement amount are calculated and disbursed using this field. |
| 14 | `ESCROW.PAY.IRREGULAR.PRD` | `EscrowPayee_IrregularPrd` |  |  |  |
| 15 | `ESCROW.PAY.END.DATE` | `EscrowPayee_EndDate` | TField |  |  |
| 16 | `ESCROW.PAY.LATE.FEE` | `EscrowPayee_LateFee` | TField | No | Standard late fee charged to the customer by the payee on defaulting the payment. Optional input. |
| 17 | `ESCROW.PAY.PENALTY.RATE` | `EscrowPayee_PenaltyRate` | TField | No | Rate used to calculate the penalty interest charged to the customer by the payee on defaulting the payment. Optional input. |
| 18 | `ESCROW.PAY.DAY.BASIS` | `EscrowPayee_DayBasis` | TField | Yes | Interest Day Basis for calculating penalty interest amount based on PENALTY.RATE. Mandatory input if PENALTY.RATE is entered. |
| 19 | `ESCROW.PAY.PENALTY.TYPE` | `EscrowPayee_PenaltyType` | TField |  | To determine the calculation type required for penalty interest for escrow payee bills which are failed during disbursment or captured bills of passed payments. DAILY: Calculation on daily basis which is determined from disbursement date to today(T24 Date) MONTHLY.INCLUDE: This type of calculation is similar to DAILY basis. MONTHLY.EXCLUDE: Monthly exclude will exclude the current month and consider the dates for calculation are from disbursement date till last day of previous month. PERIOD: MMDD is the period format defined in this field to consider the period range and interest rate for penalty interest calculation. ROUTINE: User defined routine to calculate and return the penalty interest. |
| 20 | `ESCROW.PAY.PERIOD.EFF` | `EscrowPayee_PeriodEff` |  |  |  |
| 21 | `ESCROW.PAY.PERIOD.RATE` | `EscrowPayee_PeriodRate` |  |  |  |
| 22 | `ESCROW.PAY.CALC.ROUTINE` | `EscrowPayee_CalcRoutine` | TField | Yes | A valid EB.API entry required to defined the routine in this field. Mandatory when PENALTY.TYPE is set as ROUTINE. Returns the user defined calculated penalty interest |
| 23 | `ESCROW.PAY.NOTES` | `EscrowPayee_Notes` |  |  |  |
| 24 | `ESCROW.PAY.RESERVED.26` | `EscrowPayee_Reserved26` | TField |  |  |
| 25 | `ESCROW.PAY.RESERVED.25` | `EscrowPayee_Reserved25` | TField |  |  |
| 26 | `ESCROW.PAY.RESERVED.24` | `EscrowPayee_Reserved24` | TField |  |  |
| 27 | `ESCROW.PAY.MERGE.PAYEE` | `EscrowPayee_MergePayee` |  |  |  |
| 28 | `ESCROW.PAY.MERGE.DATE` | `EscrowPayee_MergeDate` |  |  |  |
| 29 | `ESCROW.PAY.RESERVED.23` | `EscrowPayee_Reserved23` |  |  |  |
| 30 | `ESCROW.PAY.RESERVED.22` | `EscrowPayee_Reserved22` |  |  |  |
| 31 | `ESCROW.PAY.RESERVED.21` | `EscrowPayee_Reserved21` |  |  |  |
| 32 | `ESCROW.PAY.MERGED.INTO` | `EscrowPayee_MergedInto` | TField |  |  |
| 33 | `ESCROW.PAY.MERGED.INTO.DATE` | `EscrowPayee_MergedIntoDate` | TField |  | Contains the date on which the the current payee was merged (with the payee in MERGED.INTO) |
| 34 | `ESCROW.PAY.BENEFICIARY` | `EscrowPayee_Beneficiary` | TField |  | Valid Beneficiary ID that has to be referred while settling the funds to the payee |
| 35 | `ESCROW.PAY.RESERVED.20` | `EscrowPayee_Reserved20` | TField |  |  |
| 36 | `ESCROW.PAY.RESERVED.19` | `EscrowPayee_Reserved19` | TField |  |  |
| 37 | `ESCROW.PAY.RESERVED.18` | `EscrowPayee_Reserved18` | TField |  |  |
| 38 | `ESCROW.PAY.RESERVED.17` | `EscrowPayee_Reserved17` | TField |  |  |
| 39 | `ESCROW.PAY.RESERVED.16` | `EscrowPayee_Reserved16` | TField |  |  |
| 40 | `ESCROW.PAY.RESERVED.15` | `EscrowPayee_Reserved15` | TField |  |  |
| 41 | `ESCROW.PAY.RESERVED.14` | `EscrowPayee_Reserved14` | TField |  |  |
| 42 | `ESCROW.PAY.RESERVED.13` | `EscrowPayee_Reserved13` | TField |  |  |
| 43 | `ESCROW.PAY.RESERVED.12` | `EscrowPayee_Reserved12` | TField |  |  |
| 44 | `ESCROW.PAY.RESERVED.11` | `EscrowPayee_Reserved11` | TField |  |  |
| 45 | `ESCROW.PAY.RESERVED.10` | `EscrowPayee_Reserved10` | TField |  |  |
| 46 | `ESCROW.PAY.RESERVED.9` | `EscrowPayee_Reserved9` | TField |  |  |
| 47 | `ESCROW.PAY.RESERVED.8` | `EscrowPayee_Reserved8` | TField |  |  |
| 48 | `ESCROW.PAY.RESERVED.7` | `EscrowPayee_Reserved7` | TField |  |  |
| 49 | `ESCROW.PAY.RESERVED.6` | `EscrowPayee_Reserved6` | TField |  |  |
| 50 | `ESCROW.PAY.RESERVED.5` | `EscrowPayee_Reserved5` | TField |  |  |
| 51 | `ESCROW.PAY.RESERVED.4` | `EscrowPayee_Reserved4` | TField |  |  |
| 52 | `ESCROW.PAY.RESERVED.3` | `EscrowPayee_Reserved3` | TField |  |  |
| 53 | `ESCROW.PAY.RESERVED.2` | `EscrowPayee_Reserved2` | TField |  |  |
| 54 | `ESCROW.PAY.RESERVED.1` | `EscrowPayee_Reserved1` | TField |  |  |
| 55 | `ESCROW.PAY.LOCAL.REF` | `EscrowPayee_LocalRef` |  |  |  |
| 56 | `ESCROW.PAY.OVERRIDE` | `EscrowPayee_Override` |  |  |  |
| 57 | `ESCROW.PAY.RECORD.STATUS` | `EscrowPayee_RecordStatus` | String |  |  |
| 58 | `ESCROW.PAY.CURR.NO` | `EscrowPayee_CurrNo` | String |  |  |
| 59 | `ESCROW.PAY.INPUTTER` | `EscrowPayee_Inputter` |  |  |  |
| 60 | `ESCROW.PAY.DATE.TIME` | `EscrowPayee_DateTime` |  |  |  |
| 61 | `ESCROW.PAY.AUTHORISER` | `EscrowPayee_Authoriser` | String |  |  |
| 62 | `ESCROW.PAY.CO.CODE` | `EscrowPayee_CoCode` | String |  |  |
| 63 | `ESCROW.PAY.DEPT.CODE` | `EscrowPayee_DeptCode` | String |  |  |
| 64 | `ESCROW.PAY.AUDITOR.CODE` | `EscrowPayee_AuditorCode` | String |  |  |
| 65 | `ESCROW.PAY.AUDIT.DATE.TIME` | `EscrowPayee_AuditDateTime` | String |  |  |
