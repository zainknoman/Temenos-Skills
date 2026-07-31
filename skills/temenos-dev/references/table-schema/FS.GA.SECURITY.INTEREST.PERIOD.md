# FS.GA.SECURITY.INTEREST.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.INTEREST.PERIOD` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.INTEREST.PERIOD.PARENT.REF.ID` | `FsGaSecurityInterestPeriod_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.INTEREST.PERIOD.ORA.ROWID` | `FsGaSecurityInterestPeriod_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.INTEREST.PERIOD.INTERNAL.SECURITY.ID` | `FsGaSecurityInterestPeriod_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.SECURITY.INTEREST.PERIOD.DATE.OF.EFFECTIVE` | `FsGaSecurityInterestPeriod_DateOfEffective` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 5 | `FS.GA.SECURITY.INTEREST.PERIOD.FACTOR` | `FsGaSecurityInterestPeriod_Factor` | TField |  | Factor for Mortgage backed instruments, also used in CMV securities and Fair value pricing. This also finds use as a mark up or down value in case of other features Multifonds DB Column is FACTOR. |
| 6 | `FS.GA.SECURITY.INTEREST.PERIOD.FACTOR.ASSUMPTION` | `FsGaSecurityInterestPeriod_FactorAssumption` | TField |  | Estimated Income Trust Factor Multifonds DB Column is FACTOR_ASSUMPTIONS. |
| 7 | `FS.GA.SECURITY.INTEREST.PERIOD.YIELD.TO.MATURITY` | `FsGaSecurityInterestPeriod_YieldToMaturity` | TField |  | Yield To maturity of the security Multifonds DB Column is YIELD_TO_MATURITY. |
| 8 | `FS.GA.SECURITY.INTEREST.PERIOD.INTEREST.RATE` | `FsGaSecurityInterestPeriod_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 9 | `FS.GA.SECURITY.INTEREST.PERIOD.BALANCE.PRINCIPLE` | `FsGaSecurityInterestPeriod_BalancePrinciple` | TField |  | Relects the Principle Redemption balance Multifonds DB Column is COURS_REMB_BAL. |
| 10 | `FS.GA.SECURITY.INTEREST.PERIOD.OPER.AMOUNT` | `FsGaSecurityInterestPeriod_OperAmount` | TField |  | Oper Amount Multifonds DB Column is MNT_OPER. |
| 11 | `FS.GA.SECURITY.INTEREST.PERIOD.PAYDOWN.AMOUNT` | `FsGaSecurityInterestPeriod_PaydownAmount` | TField |  | Paydown Amount Multifonds DB Column is MNT_PAYDWN. |
| 12 | `FS.GA.SECURITY.INTEREST.PERIOD.PRINCIPAL.AMOUNT` | `FsGaSecurityInterestPeriod_PrincipalAmount` | TField |  | Principal Amount Multifonds DB Column is MNT_PRINCIPAL. |
| 13 | `FS.GA.SECURITY.INTEREST.PERIOD.TOTAL.PAYMENT.AMOUNT` | `FsGaSecurityInterestPeriod_TotalPaymentAmount` | TField |  | Total Payment Amount Multifonds DB Column is MNT_PYMNT_TOT. |
| 14 | `FS.GA.SECURITY.INTEREST.PERIOD.ENDING.BALANCE.AMOUNT` | `FsGaSecurityInterestPeriod_EndingBalanceAmount` | TField |  | Ending Balance Amount Multifonds DB Column is MNT_END_BAL. |
| 15 | `FS.GA.SECURITY.INTEREST.PERIOD.BP.CURRENCY` | `FsGaSecurityInterestPeriod_BpCurrency` | TField |  | BP Currency Multifonds DB Column is CMON_BP. |
| 16 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED10` | `FsGaSecurityInterestPeriod_Reserved10` | TField |  |  |
| 17 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED9` | `FsGaSecurityInterestPeriod_Reserved9` | TField |  |  |
| 18 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED8` | `FsGaSecurityInterestPeriod_Reserved8` | TField |  |  |
| 19 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED7` | `FsGaSecurityInterestPeriod_Reserved7` | TField |  |  |
| 20 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED6` | `FsGaSecurityInterestPeriod_Reserved6` | TField |  |  |
| 21 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED5` | `FsGaSecurityInterestPeriod_Reserved5` | TField |  |  |
| 22 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED4` | `FsGaSecurityInterestPeriod_Reserved4` | TField |  |  |
| 23 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED3` | `FsGaSecurityInterestPeriod_Reserved3` | TField |  |  |
| 24 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED2` | `FsGaSecurityInterestPeriod_Reserved2` | TField |  |  |
| 25 | `FS.GA.SECURITY.INTEREST.PERIOD.RESERVED1` | `FsGaSecurityInterestPeriod_Reserved1` | TField |  |  |
| 26 | `FS.GA.SECURITY.INTEREST.PERIOD.LOCAL.REF` | `FsGaSecurityInterestPeriod_LocalRef` |  |  |  |
| 27 | `FS.GA.SECURITY.INTEREST.PERIOD.OVERRIDE` | `FsGaSecurityInterestPeriod_Override` |  |  |  |
| 28 | `FS.GA.SECURITY.INTEREST.PERIOD.RECORD.STATUS` | `FsGaSecurityInterestPeriod_RecordStatus` | String |  |  |
| 29 | `FS.GA.SECURITY.INTEREST.PERIOD.CURR.NO` | `FsGaSecurityInterestPeriod_CurrNo` | String |  |  |
| 30 | `FS.GA.SECURITY.INTEREST.PERIOD.INPUTTER` | `FsGaSecurityInterestPeriod_Inputter` |  |  |  |
| 31 | `FS.GA.SECURITY.INTEREST.PERIOD.DATE.TIME` | `FsGaSecurityInterestPeriod_DateTime` |  |  |  |
| 32 | `FS.GA.SECURITY.INTEREST.PERIOD.AUTHORISER` | `FsGaSecurityInterestPeriod_Authoriser` | String |  |  |
| 33 | `FS.GA.SECURITY.INTEREST.PERIOD.CO.CODE` | `FsGaSecurityInterestPeriod_CoCode` | String |  |  |
| 34 | `FS.GA.SECURITY.INTEREST.PERIOD.DEPT.CODE` | `FsGaSecurityInterestPeriod_DeptCode` | String |  |  |
| 35 | `FS.GA.SECURITY.INTEREST.PERIOD.AUDITOR.CODE` | `FsGaSecurityInterestPeriod_AuditorCode` | String |  |  |
| 36 | `FS.GA.SECURITY.INTEREST.PERIOD.AUDIT.DATE.TIME` | `FsGaSecurityInterestPeriod_AuditDateTime` | String |  |  |
