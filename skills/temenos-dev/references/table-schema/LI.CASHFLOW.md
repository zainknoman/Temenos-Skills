# LI.CASHFLOW — Table Schema

> Source: `INSERTS/I_F.LI.CASHFLOW` in `LI_CashFlow.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.CF.LIMIT.SCHEDULE.REF` | `LiCashflow_LimitScheduleRef` | TField |  | Record ID of LI.CASHFLOW which holds the limit schedule for this utilisation limit. Will be updated only for Consolidated Cash flow record, will not have contract wise detail. Example: ID - LIXXXXXX1.AA0911111 Where LIXXXXXX1 is the utilisation limit id and AA0911111 is the facility arrangement id |
| 2 | `LI.CF.CONTRACT.OR.LIMIT.CCY` | `LiCashflow_ContractOrLimitCcy` | TField |  | Currency of contract as passed from the application. Currently it should be always same as utilisation limit currency. |
| 3 | `LI.CF.CONTRACT.REVOLVING` | `LiCashflow_ContractRevolving` | TField |  | Indicates revolving nature of the drawing contract NR - Balance for the effective dates will be considered as passed from the application. R - Balance of the first effective date will be considered for all effective dates until the last effective where the application is expected to pass value as 0 or if there are any increase in the interim dates that increased balance will be considered for rest of the effective date until the last effective date. |
| 4 | `LI.CF.LIMIT.REVOLVING` | `LiCashflow_LimitRevolving` | TField |  | Indicates revolving nature of the limit schedule NR - For decrease in each effective date, limit values will be reduced. R - Limit Values will never be decreased. |
| 5 | `LI.CF.CONTRACT.MAT.DATE` | `LiCashflow_ContractMatDate` | TField |  | Indicates the maturity date of facility and drawing. Maturity Date will be used to determine the final effective date for the contract if application does not make the balance to zero. |
| 6 | `LI.CF.EFFECTIVE.DATE` | `LiCashflow_EffectiveDate` |  |  |  |
| 7 | `LI.CF.SCH.ORG.LIMIT.AMOUNT` | `LiCashflow_SchOrgLimitAmount` |  |  |  |
| 8 | `LI.CF.REDUCED.LIMIT.AMOUNT` | `LiCashflow_ReducedLimitAmount` |  |  |  |
| 9 | `LI.CF.SCH.CONTRACT.OUTSTANDING` | `LiCashflow_SchContractOutstanding` |  |  |  |
| 10 | `LI.CF.SCH.LIMIT.OUTSTANDING` | `LiCashflow_SchLimitOutstanding` |  |  |  |
| 11 | `LI.CF.SCH.REPAY.AMOUNT` | `LiCashflow_SchRepayAmount` |  |  |  |
| 12 | `LI.CF.CONSOLIDATED.CASHFLOW` | `LiCashflow_ConsolidatedCashflow` |  |  |  |
| 13 | `LI.CF.SCH.RESERVED.10` | `LiCashflow_SchReserved10` |  |  |  |
| 14 | `LI.CF.SCH.RESERVED.9` | `LiCashflow_SchReserved9` |  |  |  |
| 15 | `LI.CF.SCH.RESERVED.8` | `LiCashflow_SchReserved8` |  |  |  |
| 16 | `LI.CF.SCH.RESERVED.7` | `LiCashflow_SchReserved7` |  |  |  |
| 17 | `LI.CF.SCH.RESERVED.6` | `LiCashflow_SchReserved6` |  |  |  |
| 18 | `LI.CF.SCH.RESERVED.5` | `LiCashflow_SchReserved5` |  |  |  |
| 19 | `LI.CF.SCH.RESERVED.4` | `LiCashflow_SchReserved4` |  |  |  |
| 20 | `LI.CF.SCH.RESERVED.3` | `LiCashflow_SchReserved3` |  |  |  |
| 21 | `LI.CF.SCH.RESERVED.2` | `LiCashflow_SchReserved2` |  |  |  |
| 22 | `LI.CF.SCH.RESERVED.1` | `LiCashflow_SchReserved1` |  |  |  |
