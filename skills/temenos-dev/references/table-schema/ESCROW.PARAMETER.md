# ESCROW.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESCROW.PARAMETER` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.PAR.DESCRIPTION` | `EscrowParameter_Description` |  |  |  |
| 2 | `ESCROW.PAR.SURPLUS.TOLERANCE` | `EscrowParameter_SurplusTolerance` | TField |  | An analysis is performed on every Escrow account. At the end of the analysis, the account might have a positive or negative balance. If the balance is positive (surplus), this field determines what is the maximum surplus balance that is allowed (tolerance) |
| 3 | `ESCROW.PAR.BELOW.SURPLUS.ACTION` | `EscrowParameter_BelowSurplusAction` | TField |  | Defines the action to be performed when the analysis ends up with suprlus and the surplus is less than the amount specified in SURPLUS.TOLERANCE. Allowed values Reduce Escrow Payment: Use the surplus amount to reduce escrow installment amount for the forth coming year. Refund to Customer: The excess above 0 is refunded back to the customer. |
| 4 | `ESCROW.PAR.ABOVE.SURPLUS.ACTION` | `EscrowParameter_AboveSurplusAction` | TField |  | Defines the action to be performed when the analysis ends up with suprlus and the surplus is more than the amount specified in SURPLUS.TOLERANCE. Allowed values: Reduce Escrow Payment: Use the surplus amount to reduce escrow installment amount for the forth coming year. Refund to Customer: The excess above 0 is refunded back to the customer. |
| 5 | `ESCROW.PAR.SHORTAGE.TOLERANCE` | `EscrowParameter_ShortTolerance` |  |  |  |
| 6 | `ESCROW.PAR.BELOW.SHORTAGE.ACTION` | `EscrowParameter_BelowShortageAction` | TField |  | Defines the action to be performed when the analysis ends up with shortage and the shortage is less than the amount specified in SHORTAGE.TOLERANCE. Allowed values: Ignore Shortage - Ignores the short amount and the customer continues to owe the amount to the bank. This can be replenished by an ad-hoc funding towards the escrow balance on the loan. Increase Escrow Payment - The shortage amount is spread over the next period by adding it to the monthly (periodic) payments collected from the customer. Request Payment in 30 Days: This option would create a seperate charge bill (ESCROWSHORT) and the customer would have to repay the bill seperately. If Unpaid in 30 Days, Add to Escrow: This is a small variation to the previous option. When chosen, it will create a bill for the short amount. The bill can be repaid within 30 days, if not, the outstanding bill amount will be adjujsted to 0 and the adjustment amount will be spread over the next period by adding it to the monthly (periodic) payments collected from the customer. |
| 7 | `ESCROW.PAR.ABOVE.SHORTAGE.ACTION` | `EscrowParameter_AboveShortageAction` | TField |  | Defines the action to be performed when the analysis ends up with shortage and the shortage is greater than the amount specified in SHORTAGE.TOLERANCE. It allows the same 4 options as of BELOW.SHORTAGE.ACTION |
| 8 | `ESCROW.PAR.RESERVED.30` | `EscrowParameter_Reserved30` | TField |  | Reserved for future use |
| 9 | `ESCROW.PAR.RESERVED.29` | `EscrowParameter_Reserved29` | TField |  | Reserved for future use |
| 10 | `ESCROW.PAR.RESERVED.28` | `EscrowParameter_Reserved28` | TField |  | Reserved for future use |
| 11 | `ESCROW.PAR.RESERVED.27` | `EscrowParameter_Reserved27` | TField |  | Reserved for future use |
| 12 | `ESCROW.PAR.RESERVED.26` | `EscrowParameter_Reserved26` | TField |  | Reserved for future use |
| 13 | `ESCROW.PAR.RESERVED.25` | `EscrowParameter_Reserved25` | TField |  | Reserved for future use |
| 14 | `ESCROW.PAR.TEST.ANALYSIS.PERIOD` | `EscrowParameter_TestAnalysisPeriod` | TField | No | Period defined here will be considered to arrive at the test analysis date at individual escrow account level. Numerical input and the value provided is considered as months. Example Test analysis period: 1, Analysis Date: 31 Dec 2016, Test analsysis date would be calculated as 30 Nov 2016. If the date derived happens to be a holiday, it will be cycled to the next working date. Optional input. |
| 15 | `ESCROW.PAR.PAYMENT.EFFECTIVE.PERIOD` | `EscrowParameter_PaymentEffectivePeriod` | TField | Yes | Defines the period after which the new escrow installment amount would take effect after the annual analysis. Numerical input and the value provided is considered as months. Example: Payment effective period - 2, Analysis Date - 31-Dec-2016, The new escrow installment amount would be effective from 28-Feb-2017 occurring on the next schedule payment date in March of 2017. If the date derived happens to be a holiday, it will be cycled to the next working date. Mandatory input. |
| 16 | `ESCROW.PAR.CUSHION.PERIOD` | `EscrowParameter_CushionPeriod` | TField | No | Determines the number of Installments to be considered as a cushion for the initial analysis. Optional input. |
| 17 | `ESCROW.PAR.ALLOW.OVERDRAW` | `EscrowParameter_AllowOverdraw` | TField | Yes | Flag to determine escrow balance should be overdrawn for disbursing amounts to payees. Mandatory input. |
| 18 | `ESCROW.PAR.OVERDRAW.LIMIT` | `EscrowParameter_OverdrawLimit` | TField | No | Maximum amount to be overdrawn from escrow balance. Optional input.Input allowed only when Overdraw is set to YES. |
| 19 | `ESCROW.PAR.AUTO.RETRY` | `EscrowParameter_AutoRetry` | TField | Yes | Flag to enable auto-retry of failed disbursements functionality on crediting escrow balance. Mandatory input. |
| 20 | `ESCROW.PAR.ANNUAL.PERIOD.END` | `EscrowParameter_AnnualPeriodEnd` | TField |  | Denotes the end date of the fiscal year. If PERIOD.END in ESCROW.ANALYSIS.TYPE is set to ANNUAL.PERIOD, then the analysis would be scheduled on the end of each fiscal year. |
| 21 | `ESCROW.PAR.POSTING.RESTRICT` | `EscrowParameter_PostingRestrict` |  |  |  |
| 22 | `ESCROW.PAR.OP.MODE` | `EscrowParameter_OpMode` | TField |  | This field is used for FDIC/CDIC hold on funds during bankruptcy Possible values are NORMAL and BANKRUPTCY |
| 23 | `ESCROW.PAR.EXCEPTION.API` | `EscrowParameter_ExceptionApi` | TField |  | Valid EB.API record need to be defined. User defined API can be attached to this field to check whether specific AA.ACTIVITY is required or not for historical data computation |
| 24 | `ESCROW.PAR.EXCEPTION.PROD.GROUP` | `EscrowParameter_ExceptionProdGroup` |  |  |  |
| 25 | `ESCROW.PAR.EXCEPTION.ACTIVITY` | `EscrowParameter_ExceptionActivity` |  |  |  |
| 26 | `ESCROW.PAR.RESERVED.20` | `EscrowParameter_Reserved20` | TField |  | Reserved for future use |
| 27 | `ESCROW.PAR.RESERVED.19` | `EscrowParameter_Reserved19` | TField |  | Reserved for future use |
| 28 | `ESCROW.PAR.RESERVED.18` | `EscrowParameter_Reserved18` | TField |  | Reserved for future use |
| 29 | `ESCROW.PAR.RESERVED.17` | `EscrowParameter_Reserved17` | TField |  | Reserved for future use |
| 30 | `ESCROW.PAR.RESERVED.16` | `EscrowParameter_Reserved16` | TField |  | Reserved for future use |
| 31 | `ESCROW.PAR.RESERVED.15` | `EscrowParameter_Reserved15` | TField |  | Reserved for future use |
| 32 | `ESCROW.PAR.RESERVED.14` | `EscrowParameter_Reserved14` | TField |  | Reserved for future use |
| 33 | `ESCROW.PAR.RESERVED.13` | `EscrowParameter_Reserved13` | TField |  | Reserved for future use |
| 34 | `ESCROW.PAR.RESERVED.12` | `EscrowParameter_Reserved12` | TField |  | Reserved for future use |
| 35 | `ESCROW.PAR.RESERVED.11` | `EscrowParameter_Reserved11` | TField |  | Reserved for future use |
| 36 | `ESCROW.PAR.RESERVED.10` | `EscrowParameter_Reserved10` | TField |  | Reserved for future use |
| 37 | `ESCROW.PAR.RESERVED.9` | `EscrowParameter_Reserved9` | TField |  | Reserved for future use |
| 38 | `ESCROW.PAR.RESERVED.8` | `EscrowParameter_Reserved8` | TField |  | Reserved for future use |
| 39 | `ESCROW.PAR.RESERVED.7` | `EscrowParameter_Reserved7` | TField |  | Reserved for future use |
| 40 | `ESCROW.PAR.RESERVED.6` | `EscrowParameter_Reserved6` | TField |  | Reserved for future use |
| 41 | `ESCROW.PAR.RESERVED.5` | `EscrowParameter_Reserved5` | TField |  | Reserved for future use |
| 42 | `ESCROW.PAR.RESERVED.4` | `EscrowParameter_Reserved4` | TField |  | Reserved for future use |
| 43 | `ESCROW.PAR.RESERVED.3` | `EscrowParameter_Reserved3` | TField |  | Reserved for future use |
| 44 | `ESCROW.PAR.RESERVED.2` | `EscrowParameter_Reserved2` | TField |  | Reserved for future use |
| 45 | `ESCROW.PAR.RESERVED.1` | `EscrowParameter_Reserved1` | TField |  | Reserved for future use |
| 46 | `ESCROW.PAR.LOCAL.REF` | `EscrowParameter_LocalRef` |  |  |  |
| 47 | `ESCROW.PAR.OVERRIDE` | `EscrowParameter_Override` |  |  |  |
| 48 | `ESCROW.PAR.RECORD.STATUS` | `EscrowParameter_RecordStatus` | String |  |  |
| 49 | `ESCROW.PAR.CURR.NO` | `EscrowParameter_CurrNo` | String |  |  |
| 50 | `ESCROW.PAR.INPUTTER` | `EscrowParameter_Inputter` |  |  |  |
| 51 | `ESCROW.PAR.DATE.TIME` | `EscrowParameter_DateTime` |  |  |  |
| 52 | `ESCROW.PAR.AUTHORISER` | `EscrowParameter_Authoriser` | String |  |  |
| 53 | `ESCROW.PAR.CO.CODE` | `EscrowParameter_CoCode` | String |  |  |
| 54 | `ESCROW.PAR.DEPT.CODE` | `EscrowParameter_DeptCode` | String |  |  |
| 55 | `ESCROW.PAR.AUDITOR.CODE` | `EscrowParameter_AuditorCode` | String |  |  |
| 56 | `ESCROW.PAR.AUDIT.DATE.TIME` | `EscrowParameter_AuditDateTime` | String |  |  |
