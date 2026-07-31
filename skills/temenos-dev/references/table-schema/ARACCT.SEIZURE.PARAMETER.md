# ARACCT.SEIZURE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ARACCT.SEIZURE.PARAMETER` in `ARACCT_AccountAlias.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.SEIZURE.PRODUCT.SEQUENCE` | `AracctSeizureParameter_SeizureProductSequence` |  |  |  |
| 2 | `ARACCT.MINIMUM.WAGES.AMOUNT` | `AracctSeizureParameter_MinimumWagesAmount` | TField |  | Amount Holds the minimum vital salary of the customer. |
| 3 | `ARACCT.ACCOUNT.BAL.LT.TWICE.MWA` | `AracctSeizureParameter_AccountBalLtTwiceMwa` | TField |  |  |
| 4 | `ARACCT.ACCOUNT.BAL.GT.TWICE.MWA` | `AracctSeizureParameter_AccountBalGtTwiceMwa` | TField |  |  |
| 5 | `ARACCT.PAYROLL.ACCOUNT.PRODUCT` | `AracctSeizureParameter_PayrollAccountProduct` | TField |  | Valid record in AA.PRODUCT.CATALOG . Identified Payroll accounts product is configured here. |
| 6 | `ARACCT.PRODUCT.LOCKED` | `AracctSeizureParameter_ProductLocked` |  |  |  |
| 7 | `ARACCT.INTERNAL.SUSPENSE.ACCOUNT` | `AracctSeizureParameter_InternalSuspenseAccount` | TField |  | Valid Internal Account number to which Seized amount is transferred. |
| 8 | `ARACCT.EXCLUDE.ROLE` | `AracctSeizureParameter_ExcludeRole` |  |  |  |
| 9 | `ARACCT.BANK.CODE` | `AracctSeizureParameter_BankCode` | TField |  | Bank Code need to be configured here |
| 10 | `ARACCT.LOCAL.REF` | `AracctSeizureParameter_LocalRef` |  |  |  |
| 11 | `ARACCT.INMOBILIZED.BALANCE.PRODUCT` | `AracctSeizureParameter_InmobilizedBalanceProduct` |  |  |  |
| 12 | `ARACCT.RESERVED.2` | `AracctSeizureParameter_Reserved2` | TField |  | Reserved for future use |
| 13 | `ARACCT.RESERVED.3` | `AracctSeizureParameter_Reserved3` | TField |  | Reserved for future use |
| 14 | `ARACCT.RESERVED.4` | `AracctSeizureParameter_Reserved4` | TField |  | Reserved for future use |
| 15 | `ARACCT.RESERVED.5` | `AracctSeizureParameter_Reserved5` | TField |  | Reserved for future use |
| 16 | `ARACCT.RESERVED.6` | `AracctSeizureParameter_Reserved6` | TField |  | Reserved for future use |
| 17 | `ARACCT.RESERVED.7` | `AracctSeizureParameter_Reserved7` | TField |  | Reserved for future use |
| 18 | `ARACCT.RESERVED.8` | `AracctSeizureParameter_Reserved8` | TField |  | Reserved for future use |
| 19 | `ARACCT.RESERVED.9` | `AracctSeizureParameter_Reserved9` | TField |  | Reserved for future use |
| 20 | `ARACCT.RESERVED.10` | `AracctSeizureParameter_Reserved10` | TField |  | Reserved for future use |
| 21 | `ARACCT.RESERVED.11` | `AracctSeizureParameter_Reserved11` | TField |  | Reserved for future use |
| 22 | `ARACCT.RESERVED.12` | `AracctSeizureParameter_Reserved12` | TField |  | Reserved for future use |
| 23 | `ARACCT.RESERVED.13` | `AracctSeizureParameter_Reserved13` | TField |  | Reserved for future use |
| 24 | `ARACCT.RESERVED.14` | `AracctSeizureParameter_Reserved14` | TField |  | Reserved for future use |
| 25 | `ARACCT.RESERVED.15` | `AracctSeizureParameter_Reserved15` | TField |  | Reserved for future use |
| 26 | `ARACCT.OVERRIDE` | `AracctSeizureParameter_Override` |  |  |  |
| 27 | `ARACCT.RECORD.STATUS` | `AracctSeizureParameter_RecordStatus` | String |  |  |
| 28 | `ARACCT.CURR.NO` | `AracctSeizureParameter_CurrNo` | String |  |  |
| 29 | `ARACCT.INPUTTER` | `AracctSeizureParameter_Inputter` |  |  |  |
| 30 | `ARACCT.DATE.TIME` | `AracctSeizureParameter_DateTime` |  |  |  |
| 31 | `ARACCT.AUTHORISER` | `AracctSeizureParameter_Authoriser` | String |  |  |
| 32 | `ARACCT.CO.CODE` | `AracctSeizureParameter_CoCode` | String |  |  |
| 33 | `ARACCT.DEPT.CODE` | `AracctSeizureParameter_DeptCode` | String |  |  |
| 34 | `ARACCT.AUDITOR.CODE` | `AracctSeizureParameter_AuditorCode` | String |  |  |
| 35 | `ARACCT.AUDIT.DATE.TIME` | `AracctSeizureParameter_AuditDateTime` | String |  |  |
