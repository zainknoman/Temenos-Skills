# AC.CASH.POOL.LINK — Table Schema

> Source: `INSERTS/I_F.AC.CASH.POOL.LINK` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.LINK.DESCRIPTION` | `AcCashPoolLink_Description` | TField |  | Details which AC.CASH.POOL record created this record. Validation Rules: System maintained - no user input |
| 2 | `CP.LINK.GROUP.ID` | `AcCashPoolLink_GroupId` | TField |  | Contains the GROUP.ID from AC.CASH.POOL, see HELPTEXT on that field for details. Validation Rules: System maintained - no user input |
| 3 | `CP.LINK.SUB.GROUP.ID` | `AcCashPoolLink_SubGroupId` | TField |  | Contains the SUB.GROUP.ID from AC.CASH.POOL, see HELPTEXT on that field for details. Validation Rules: System maintained - no user input |
| 4 | `CP.LINK.SEQUENCE` | `AcCashPoolLink_Sequence` | TField |  | Contains the SEQUENCE from AC.CASH.POOL, see HELPTEXT on that field for details. Validation Rules: System maintained - no user input |
| 5 | `CP.LINK.LINK.CURRENCY` | `AcCashPoolLink_LinkCurrency` | TField |  | Contains the CURRENCY of the Account. Validation Rules: System maintained - no user input |
| 6 | `CP.LINK.SWEEP.TYPE` | `AcCashPoolLink_SweepType` |  |  |  |
| 7 | `CP.LINK.CASHFLOW.AMT` | `AcCashPoolLink_CashflowAmt` |  |  |  |
| 8 | `CP.LINK.AGREGATE.BAL` | `AcCashPoolLink_AgregateBal` |  |  |  |
| 9 | `CP.LINK.FREQUENCY` | `AcCashPoolLink_Frequency` |  |  |  |
| 10 | `CP.LINK.NEXT.RUN.DATE` | `AcCashPoolLink_NextRunDate` |  |  |  |
| 11 | `CP.LINK.DR.NARR.TXT` | `AcCashPoolLink_DrNarrTxt` |  |  |  |
| 12 | `CP.LINK.CR.NARR.TXT` | `AcCashPoolLink_CrNarrTxt` |  |  |  |
| 13 | `CP.LINK.ACCOUNT.TO` | `AcCashPoolLink_AccountTo` |  |  |  |
| 14 | `CP.LINK.ACCOUNT.FROM` | `AcCashPoolLink_AccountFrom` |  |  |  |
| 15 | `CP.LINK.MAXIMUM.AMT` | `AcCashPoolLink_MaximumAmt` |  |  |  |
| 16 | `CP.LINK.MINIMUM.AMT` | `AcCashPoolLink_MinimumAmt` |  |  |  |
| 17 | `CP.LINK.OVERRIDE.AMT` | `AcCashPoolLink_OverrideAmt` |  |  |  |
| 18 | `CP.LINK.OVERRIDE.PERCNT` | `AcCashPoolLink_OverridePercnt` |  |  |  |
| 19 | `CP.LINK.AMT.ROUTINE` | `AcCashPoolLink_AmtRoutine` |  |  |  |
| 20 | `CP.LINK.UP.TO.AMOUNT` | `AcCashPoolLink_UpToAmount` |  |  |  |
| 21 | `CP.LINK.UP.TO.PERCENT` | `AcCashPoolLink_UpToPercent` |  |  |  |
| 22 | `CP.LINK.RULE.PRIORITY` | `AcCashPoolLink_RulePriority` |  |  |  |
| 23 | `CP.LINK.SCHEDULE` | `AcCashPoolLink_Schedule` |  |  |  |
| 24 | `CP.LINK.BACK.VALUE.IND` | `AcCashPoolLink_BackValueInd` |  |  |  |
| 25 | `CP.LINK.MIN.TFR.DR` | `AcCashPoolLink_MinTfrDr` |  |  |  |
| 26 | `CP.LINK.MIN.TFR.CR` | `AcCashPoolLink_MinTfrCr` |  |  |  |
| 27 | `CP.LINK.FROM.AC.BAL.TYPE` | `AcCashPoolLink_FromAcBalType` |  |  |  |
| 28 | `CP.LINK.TO.AC.BAL.TYPE` | `AcCashPoolLink_ToAcBalType` |  |  |  |
| 29 | `CP.LINK.INTEREST.RATE` | `AcCashPoolLink_InterestRate` | TField |  | This field is not used at present |
| 30 | `CP.LINK.INTEREST.KEY` | `AcCashPoolLink_InterestKey` | TField |  | This field is not used at present |
| 31 | `CP.LINK.INTEREST.SPREAD` | `AcCashPoolLink_InterestSpread` | TField |  | This field is not used at present |
| 32 | `CP.LINK.INT.LIQ.ACCT` | `AcCashPoolLink_IntLiqAcct` | TField |  | This field is not used at present |
| 33 | `CP.LINK.CATEGORY` | `AcCashPoolLink_Category` | TField |  | This field is not used at present |
| 34 | `CP.LINK.MM.CONTRACT` | `AcCashPoolLink_MmContract` |  |  |  |
| 35 | `CP.LINK.MULTI.RULE` | `AcCashPoolLink_MultiRule` | TField |  | Value as given in Multi rule in the respective cash pool group parameter is defaulted here. Cash pool with multi-rule is created to handle the cases where there is a restriction on the number of entries to Accounts. When multi-rule is "Yes" - then the cash pool should be created with two links-consists of Surplus and maintenance sweep rules and the frequency component for the maintenance should be greater than surplus sweep. For example surplus is mentioned as "BSNSS-Daily" then the Maintenance sweep should be either "Weekly" or "Monthly". Also the rules priority should be given at the cash pool level to prioritize the execution of cash pool links. Refer to multi-rule field at group level and AI-Accounts, Interest and Charges user guide related to Cash pool section for more details. |
| 36 | `CP.LINK.LAST.RUN.DATE` | `AcCashPoolLink_LastRunDate` | TField |  | Indicates the last date the sweep was run or executed. |
| 37 | `CP.LINK.SEQUENCE.PRIORITY` | `AcCashPoolLink_SequencePriority` | TField |  | When a single cash pool record has multiple linked accounts, the system displays the sequence priority according to the rule priority, such as 1.1 or 1.2. Example: A cash pool record is created for account 12345 with a sequence of 1 and includes multiple linked accounts: Link account 1 (23451) with Rule priority 2 Link account 2 (32456) with Rule priority 1 Upon authorization, two records are created in AC.CASH.POOL.LINK: one for link account 1 (23451) with a sequence priority of 1.2, and another for link account 2 (32456) with a sequence priority of 1.1. |
| 38 | `CP.LINK.EUCC.SOD.PROCESS` | `AcCashPoolLink_EuccSodProcess` | TField |  | If the field contains the text "YES", this indicates that the cash pool link record is in the Euro currency conversion process. Validation Rules: System maintained - no user input |
| 39 | `CP.LINK.SEQUENCE.RET.PRIORITY` | `AcCashPoolLink_SequenceRetPriority` | TField |  | Contains the combined input of fields - SEQUENCE and RETURN.RULE.PRIORITY from AC.CASH.POOL, see HELPTEXT on therelated fields for details. Validation Rules: System maintained - no user input |
| 40 | `CP.LINK.RESERVED01` | `AcCashPoolLink_Reserved01` |  |  |  |
| 41 | `CP.LINK.MIN.AMT.TRANSFER` | `AcCashPoolLink_MinAmtTransfer` |  |  |  |
| 42 | `CP.LINK.SWEEP.UNIT.AMT` | `AcCashPoolLink_SweepUnitAmt` |  |  |  |
| 43 | `CP.LINK.PAYMENT.PRODUCT` | `AcCashPoolLink_PaymentProduct` |  |  |  |
| 44 | `CP.LINK.MAX.CONCENTRATION.AMT` | `AcCashPoolLink_MaxConcentrationAmt` |  |  |  |
| 45 | `CP.LINK.RETURN.RULE.PRIORITY` | `AcCashPoolLink_ReturnRulePriority` |  |  |  |
| 46 | `CP.LINK.BASE.DATE` | `AcCashPoolLink_BaseDate` |  |  |  |
| 47 | `CP.LINK.BENEFICIARY.ID` | `AcCashPoolLink_BeneficiaryId` |  |  |  |
