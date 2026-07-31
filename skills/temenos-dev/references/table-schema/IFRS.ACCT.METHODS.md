# IFRS.ACCT.METHODS — Table Schema

> Source: `INSERTS/I_F.IFRS.ACCT.METHODS` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFRS.AC.METH.DESCRIT` | `IfrsAcctMethods_Descrit` |  |  |  |
| 2 | `IFRS.AC.METH.ACCT.HEAD.TYPE` | `IfrsAcctMethods_AcctHeadType` |  |  |  |
| 3 | `IFRS.AC.METH.NPV.METHOD` | `IfrsAcctMethods_NpvMethod` |  |  |  |
| 4 | `IFRS.AC.METH.NPV.RATE` | `IfrsAcctMethods_NpvRate` |  |  |  |
| 5 | `IFRS.AC.METH.POSTING.REQD` | `IfrsAcctMethods_PostingReqd` |  |  |  |
| 6 | `IFRS.AC.METH.ADJUST.ENTRY` | `IfrsAcctMethods_AdjustEntry` |  |  |  |
| 7 | `IFRS.AC.METH.BAL.TO.EXLD` | `IfrsAcctMethods_BalToExld` |  |  |  |
| 8 | `IFRS.AC.METH.CALC.RTN` | `IfrsAcctMethods_CalcRtn` |  |  |  |
| 9 | `IFRS.AC.METH.HYBRID.ACCT.TYPE` | `IfrsAcctMethods_HybridAcctType` | TField |  | This field will denote that current acct method being defined follows the Hybrid method of IFRS accounting when attached to any contracts. In Hybrid method of IFRS accounting, on the firsday of a loan disbursement the contract will be measured based on Fairvalue using the Market Key. On subsequent days the loan is measured using amortised cost method Options field with allowed values as "YES" or "NO". When a value of "YES" is provided then Multivalue set of ACCT.HEAD.TYPE should have "FAIRVALUE" defined first followed by "AMORTISED". Othercase validation error would be raised. When a value of "NO" or null is specified then any existing definition allowed but "FAIRVALUE" followed by "AMORTISED" will be stopped. Input not allowed when ACCR.AMORT.SL accounting head is defined. |
| 10 | `IFRS.AC.METH.IMPAIR.INT.BAL.TYPE` | `IfrsAcctMethods_ImpairIntBalType` | TField |  | Interest revenue is recognised on net basis when a contract is impaired and moves to stage 3. This interest recognition will be done as an interest adjustment on net carrying amount from the period the contracts becomes impaired and accounting for the same will be done under IMPAIR.INTEREST head. Whenever impaired contract is suspended, accrued interest will be suspended and not recognised under P &amp; L, in such cases there is no need to adjust the accrued interest i.e IMAPIR.INTEREST need not be posted. If this field is configured with specific interest asset types, then interest revenue adjustment is calculated only in the absence of suspended balances under the mentioned asset types. This field is left blank, then the interest revenue adjustment is calculated and posted irrespective of any suspended amount being present or not, but for this the suspended amount under IF Position Type must first be realised. This field is common for both overdraft accounts and contracts. If SUSPENDED.INTEREST head is defined in IFRS.ACCT.METHODS, then it is not advisable to specify this field value. For overdraft accounts, When the Impair Int Bal Type field in IFRS.ACCT.METHODS is left blank, the Acct Head Type multivalue field should be set as SUSPENDED.INTEREST, to realise the suspended amount under IF Position Type and interest adjustments will continue to be posted. If the Impair Int Bal Type field is defined in IFRS.ACCT.METHODS, then the SUSPENDED.INTEREST field value is not required in the Acct Head Type multivalue field and interest adjustment posting will be stopped on suspension. For IFRS9 contracts, If BAL.TO.EXCLD is not specified, then suspended balances are recognised to IF by default as T24 balance, hence leave IMPAIR.INT.BAL.TYPE as null. Interest adjustment is posted irrespective of suspension If BAL.TO.EXCLD is specified with suspended interest assets, then suspended interest is not recognised in IF so specify IMPAIR.INT.BAL.TYPE. Interest adjusment posting will be stopped on suspension. Validation Rules: A Valid record from the table AC.BALANCE.TYPE with REPORTING.TYPE as VIRTUAL. This is to define the asset types under which accrual entries are raised for differenet T24 applications . Allowed to input only if IMPAIR.INTEREST head is defined and there is no FAIRVALUE definition. |
| 11 | `IFRS.AC.METH.BELOW.MARKET.ACCT` | `IfrsAcctMethods_BelowMarketAcct` | TField | Yes | This field indicates whether contract's rate is below market rate and the loss has to be booked to PL at inception itself. Validation Rules: Possible values are Yes, No, Null. Yes - It is mandatory to define FAIRVALUE.LOSS and FAIRVALUE.LOSS.ADJUST Accounting heads. System will book the loss to PL at inception. No - Below Market Rate Accounting not done. Both HYBRID.ACCT.TYPE and BELOW.MARKET.ACCT field values cannot be set to YES. Input not allowed when ACCR.AMORT.SL accounting head is defined. Yes to No value change not allowed for this field.If a contract has to be moved from below market rate accounting to commercial, then corresponding application should handoff details on the same. No/Null to Yes value change allowed only for the purpose to takeover contracts into IFRS. |
| 12 | `IFRS.AC.METH.RESERVED.07` | `IfrsAcctMethods_Reserved07` | TField |  |  |
| 13 | `IFRS.AC.METH.RESERVED.06` | `IfrsAcctMethods_Reserved06` | TField |  |  |
| 14 | `IFRS.AC.METH.RESERVED.05` | `IfrsAcctMethods_Reserved05` | TField |  |  |
| 15 | `IFRS.AC.METH.RESERVED.04` | `IfrsAcctMethods_Reserved04` | TField |  |  |
| 16 | `IFRS.AC.METH.RESERVED.03` | `IfrsAcctMethods_Reserved03` | TField |  |  |
| 17 | `IFRS.AC.METH.LOCAL.REF` | `IfrsAcctMethods_LocalRef` |  |  |  |
| 18 | `IFRS.AC.METH.OVERRIDE` | `IfrsAcctMethods_Override` |  |  |  |
| 19 | `IFRS.AC.METH.RECORD.STATUS` | `IfrsAcctMethods_RecordStatus` | String |  |  |
| 20 | `IFRS.AC.METH.CURR.NO` | `IfrsAcctMethods_CurrNo` | String |  |  |
| 21 | `IFRS.AC.METH.INPUTTER` | `IfrsAcctMethods_Inputter` |  |  |  |
| 22 | `IFRS.AC.METH.DATE.TIME` | `IfrsAcctMethods_DateTime` |  |  |  |
| 23 | `IFRS.AC.METH.AUTHORISER` | `IfrsAcctMethods_Authoriser` | String |  |  |
| 24 | `IFRS.AC.METH.CO.CODE` | `IfrsAcctMethods_CoCode` | String |  |  |
| 25 | `IFRS.AC.METH.DEPT.CODE` | `IfrsAcctMethods_DeptCode` | String |  |  |
| 26 | `IFRS.AC.METH.AUDITOR.CODE` | `IfrsAcctMethods_AuditorCode` | String |  |  |
| 27 | `IFRS.AC.METH.AUDIT.DATE.TIME` | `IfrsAcctMethods_AuditDateTime` | String |  |  |
