# CMBASE.HAL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CMBASE.HAL.PARAMETER` in `CMBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.REQ.LOAN.AMT.CAP` | `CmbaseHalParameter_ReqLoanAmtCap` | TField |  | The requested loan amount for Housing loan should not exceed mentioned percent of the Purchase Price |
| 2 | `CMBASE.STATE.GTEE.PERCENT.CAP` | `CmbaseHalParameter_StateGteePercentCap` | TField |  | The State guarantee percent input by the user should not exceed mentioned percent for Housing loan |
| 3 | `CMBASE.HAL.LOAN.AMT.RATIO` | `CmbaseHalParameter_HalLoanAmtRatio` | TField |  | The HAL loan amount is calculated as collateral value/mentioned ratio for housing loan and the denominator is parameterizable |
| 4 | `CMBASE.HAL.LOAN.AMT.CAP` | `CmbaseHalParameter_HalLoanAmtCap` | TField |  | The HAL loan amount calculated should not exceed mentioned percent of the purchase price |
| 5 | `CMBASE.HAL.GTEE.AMT` | `CmbaseHalParameter_HalGteeAmt` | TField |  | This is the cap of the HAL Guarantee amount |
| 6 | `CMBASE.HAL.GTEE.PORTION.PERCENT` | `CmbaseHalParameter_HalGteePortionPercent` | TField |  | The State guarantee portion percent input by the user should not exceed mentioned percent for Housing loan. |
| 7 | `CMBASE.LOCAL.REF` | `CmbaseHalParameter_LocalRef` |  |  |  |
| 8 | `CMBASE.RESERVED.1` | `CmbaseHalParameter_Reserved1` | TField |  | Reserved for future use |
| 9 | `CMBASE.RESERVED.2` | `CmbaseHalParameter_Reserved2` | TField |  | Reserved for future use |
| 10 | `CMBASE.RESERVED.3` | `CmbaseHalParameter_Reserved3` | TField |  | Reserved for future use |
| 11 | `CMBASE.RESERVED.4` | `CmbaseHalParameter_Reserved4` | TField |  | Reserved for future use |
| 12 | `CMBASE.RESERVED.5` | `CmbaseHalParameter_Reserved5` | TField |  | Reserved for future use |
| 13 | `CMBASE.RESERVED.6` | `CmbaseHalParameter_Reserved6` | TField |  | Reserved for future use |
| 14 | `CMBASE.RESERVED.7` | `CmbaseHalParameter_Reserved7` | TField |  | Reserved for future use |
| 15 | `CMBASE.RESERVED.8` | `CmbaseHalParameter_Reserved8` | TField |  | Reserved for future use |
| 16 | `CMBASE.OVERRIDE` | `CmbaseHalParameter_Override` |  |  |  |
| 17 | `CMBASE.RECORD.STATUS` | `CmbaseHalParameter_RecordStatus` | String |  |  |
| 18 | `CMBASE.CURR.NO` | `CmbaseHalParameter_CurrNo` | String |  |  |
| 19 | `CMBASE.INPUTTER` | `CmbaseHalParameter_Inputter` |  |  |  |
| 20 | `CMBASE.DATE.TIME` | `CmbaseHalParameter_DateTime` |  |  |  |
| 21 | `CMBASE.AUTHORISER` | `CmbaseHalParameter_Authoriser` | String |  |  |
| 22 | `CMBASE.CO.CODE` | `CmbaseHalParameter_CoCode` | String |  |  |
| 23 | `CMBASE.DEPT.CODE` | `CmbaseHalParameter_DeptCode` | String |  |  |
| 24 | `CMBASE.AUDITOR.CODE` | `CmbaseHalParameter_AuditorCode` | String |  |  |
| 25 | `CMBASE.AUDIT.DATE.TIME` | `CmbaseHalParameter_AuditDateTime` | String |  |  |
