# AC.ACCOUNT.LINK — Table Schema

> Source: `INSERTS/I_F.AC.ACCOUNT.LINK` in `RS_Sweeping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.LINK.DESCRIPTION` | `AcAccountLink_Description` | A (alphanumeric) |  | DESCRIPTION Description of Link Up to 35 type A (alphanumeric) characters. |
| 2 | `AC.LINK.SWEEP.TYPE` | `AcAccountLink_SweepType` | A (alphanumeric) |  | SWEEP.TYPE Sweep types can be defined with different transaction codes for the Maintenance, Surplus or Two-way Sweep. SWEEP.TYPE is assigned for linked accounts, linked through the AC.ACCOUNT.LINK table. It must be the key to a record on the AC.SWEEP.TYPE file Up to 35 type A (alphanumeric) characters. AC.SWEEP.TYPE with SWEEP.STYLE as "CASHFLOW" is allowed only in AC.CASH.POOL. It is same as a Two Way sweep rule except there is a controlling limit on how much can be taken from higher level account. |
| 3 | `AC.LINK.FREQUENCY` | `AcAccountLink_Frequency` | TField |  | FREQUENCY Frequency for running the sweeps. Accepts T24 standard date frequencies. "DAILY" is not valid for Account Sweeping. |
| 4 | `AC.LINK.NEXT.RUN.DATE` | `AcAccountLink_NextRunDate` | TField |  | NEXT.RUN.DATE Specifies the next run date of the sweep. NOINPUT field. Defaulted from the FREQUENCY field. |
| 5 | `AC.LINK.ACCOUNT.TO` | `AcAccountLink_AccountTo` |  |  |  |
| 6 | `AC.LINK.TO.ACCT.BALTYPE` | `AcAccountLink_ToAcctBaltype` |  |  |  |
| 7 | `AC.LINK.ACCT.TO.CCY` | `AcAccountLink_AcctToCcy` |  |  |  |
| 8 | `AC.LINK.MINIMUM.AMT` | `AcAccountLink_MinimumAmt` |  |  |  |
| 9 | `AC.LINK.MAXIMUM.AMT` | `AcAccountLink_MaximumAmt` |  |  |  |
| 10 | `AC.LINK.ACCOUNT.FROM` | `AcAccountLink_AccountFrom` |  |  |  |
| 11 | `AC.LINK.FROM.ACCT.BALTYPE` | `AcAccountLink_FromAcctBaltype` |  |  |  |
| 12 | `AC.LINK.ACCT.FROM.CCY` | `AcAccountLink_AcctFromCcy` |  |  |  |
| 13 | `AC.LINK.FROM.MIN.AMT` | `AcAccountLink_FromMinAmt` |  |  |  |
| 14 | `AC.LINK.LOCAL.REF` | `AcAccountLink_LocalRef` |  |  |  |
| 15 | `AC.LINK.CHARGE.CODE` | `AcAccountLink_ChargeCode` | TField | No | Defines the charge that is to be collected for setting up a sweep instruction. Accepts valid record ID of FT.CHARGE.TYPE / FT.COMMISSION.TYPE. After collecting the charge amount, field is set to null. Optional field. |
| 16 | `AC.LINK.CHARGE.AMOUNT` | `AcAccountLink_ChargeAmount` | TField |  | Defines the fixed charge amount associated with the CHARGE.CODE field. |
| 17 | `AC.LINK.CHARGE.ACCOUNT` | `AcAccountLink_ChargeAccount` | TField |  | Defines the Account from which the charge is to be debited. |
| 18 | `AC.LINK.TAX.AMOUNT` | `AcAccountLink_TaxAmount` | TField |  |  |
| 19 | `AC.LINK.SWEEP.CHG.CODE` | `AcAccountLink_SweepChgCode` | TField | No | Defines the charge code associated with the charge that is to be collected for each successful sweep. Value is defaulted from AC.CP.GROUP.PARAM which can be amended by the user. Optional field. |
| 20 | `AC.LINK.SWEEP.CHG.AMOUNT` | `AcAccountLink_SweepChgAmount` | TField |  | Defines the fixed charge amount to be collected for each sweep. Value is system calculated, if not input by the user. |
| 21 | `AC.LINK.WAIVE.CHARGES` | `AcAccountLink_WaiveCharges` | TField |  | Defines whether charge is to be collected or not, for each successful sweep |
| 22 | `AC.LINK.SUSP.START.DATE` | `AcAccountLink_SuspStartDate` | TField |  | Holds the start date for suspending the sweep. Sweeps will not be processed between this date and the date defined in SUSP.END.DATE. |
| 23 | `AC.LINK.SUSP.END.DATE` | `AcAccountLink_SuspEndDate` | TField |  | Holds the end date for suspending the sweep. Sweeps will not be processed between the date defined in SUSP.START.DATE and this date, |
| 24 | `AC.LINK.SWEEP.CANCEL.DATE` | `AcAccountLink_SweepCancelDate` | TField |  | Holds the end date for the sweep record. Record will be inactive after this date and sweep will not be executed after this date. |
| 25 | `AC.LINK.CONVERSION.RATE` | `AcAccountLink_ConversionRate` | TField |  | Identifies which conversion rate to be applied during the cross currency sweeping. Acceptable values are: MID - Mid rate from the currency table will be used for conversion BUY-SELL - Buy/sell rate from the currency table will be used for conversion Default value is MID. |
| 26 | `AC.LINK.SHARED.BALANCE` | `AcAccountLink_SharedBalance` | TField | No | YES or No Field. Blank means No. Significance of the field is limited to AA accounts with Credit check as Component. If Yes is specified , the available balance of the defined sweep accounts will be utilized in case of insufficient balance to approve a transaction in the maintenance account, provided the donor account has the required amount excluding its minimum to be maintained. Also sweep should be set as an optional component for the activity involved. The balance to be used from sweep account will be calculated as BaseBalance + Existing projected amount - Minimum amount to be maintained for the account + TransactionAmt . Based on the SWEEP.COVERAGE set up and the eligibility of the donors , the balance for the overdraft override is arrived. The amount donated / received will be updated as projected amount in respective account's ECB and working Balance along with the amount projected will be considered for balance calculation in online . The projected amount specified in ECB will then be swept in EOD to / from the respective Sweep account , while at EOD funds only from the balance type configured will be considered. If No is specified , then sweep account balance will not be considered for overdraft check while online transactions recieved. Value cannot be changed from Yes to No, if there is a balance projection from any of the donor accounts configured in the sweep. Any other requests for account's credit check balance based on credit check set up will consider projections and the balance of the donor accounts too. |
| 27 | `AC.LINK.SWEEP.COVERAGE` | `AcAccountLink_SweepCoverage` | TField |  | SWEEP.COVERAGE can be set to FULL or PARTIAL. Full - The amount will be utilized only when any one of the donor account can cover the required amount in full. Partial - Existing functionality, one or more accounts can collectively share balance to cover overdraft amount. |
| 28 | `AC.LINK.RESERVED.3` | `AcAccountLink_Reserved3` | TField |  |  |
| 29 | `AC.LINK.RESERVED.4` | `AcAccountLink_Reserved4` | TField |  |  |
| 30 | `AC.LINK.RESERVED.5` | `AcAccountLink_Reserved5` | TField |  |  |
| 31 | `AC.LINK.RESERVED.6` | `AcAccountLink_Reserved6` | TField |  |  |
| 32 | `AC.LINK.RESERVED.7` | `AcAccountLink_Reserved7` | TField |  |  |
| 33 | `AC.LINK.RESERVED.8` | `AcAccountLink_Reserved8` | TField |  |  |
| 34 | `AC.LINK.RESERVED.9` | `AcAccountLink_Reserved9` | TField |  |  |
| 35 | `AC.LINK.STMT.NOS` | `AcAccountLink_StmtNos` |  |  |  |
| 36 | `AC.LINK.OVERRIDE` | `AcAccountLink_Override` |  |  |  |
| 37 | `AC.LINK.RECORD.STATUS` | `AcAccountLink_RecordStatus` | String |  |  |
| 38 | `AC.LINK.CURR.NO` | `AcAccountLink_CurrNo` | String |  |  |
| 39 | `AC.LINK.INPUTTER` | `AcAccountLink_Inputter` |  |  |  |
| 40 | `AC.LINK.DATE.TIME` | `AcAccountLink_DateTime` |  |  |  |
| 41 | `AC.LINK.AUTHORISER` | `AcAccountLink_Authoriser` | String |  |  |
| 42 | `AC.LINK.CO.CODE` | `AcAccountLink_CoCode` | String |  |  |
| 43 | `AC.LINK.DEPT.CODE` | `AcAccountLink_DeptCode` | String |  |  |
| 44 | `AC.LINK.AUDITOR.CODE` | `AcAccountLink_AuditorCode` | String |  |  |
| 45 | `AC.LINK.AUDIT.DATE.TIME` | `AcAccountLink_AuditDateTime` | String |  |  |
