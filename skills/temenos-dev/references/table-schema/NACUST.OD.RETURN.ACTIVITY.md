# NACUST.OD.RETURN.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.NACUST.OD.RETURN.ACTIVITY` in `NACUST_CustomerHolds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OD.RET.ACT.ACCOUNT` | `NacustOdReturnActivity_Account` | TField |  | Id of overdrawn account; same as account in Id. |
| 2 | `OD.RET.ACT.YEAR` | `NacustOdReturnActivity_Year` | TField |  | Year when account was overdrawn; same as year in Id. |
| 3 | `OD.RET.ACT.THRESHOLD.OD` | `NacustOdReturnActivity_ThresholdOd` | TField |  | Excessive Amount Overdraft counter must follow parameter setup in USREGS.REGULATION.PARAM> REG.CC*REPEAT.OD within multi-value set in which the Threshold Type = Count This field must be incrementally updated during COB when account is found to be overdrawn. This field must be reset to 'null' if the account is not overdrawn for given retention period. E.g if retention period 3M; if the account was not overdrawn for 90 days then this field will reset to null. |
| 4 | `OD.RET.ACT.THRESHOLD.CONSEC.OD` | `NacustOdReturnActivity_ThresholdConsecOd` | TField |  | This field will hold the number of day the account got overdrawn consecutively. It will be incrementally updated during COB when account is overdrawn on a consecutive day. It must be reset to 'null' during COB if the account balance is found to be zero or has a positive balance |
| 5 | `OD.RET.ACT.THRESHOLD.EXCESS.OD` | `NacustOdReturnActivity_ThresholdExcessOd` | TField |  |  |
| 6 | `OD.RET.ACT.THRESHOLD.RETURNS` | `NacustOdReturnActivity_ThresholdReturns` | TField |  | Deposit Items counter must follow parameter USREGS.REGULATION.PARAM>REG.CC*RETURN.DEPOSITED.ITEMS This counter will be incremented when the creidt or debit transaction happen on an account during the past period defined 'Threshold Period' that matches the transaction code defined in field 'Return Transaction Code' in parameter USREGS.REGULATION.PARAM Reset this field to 'null' when no returned deposited items are identified during the 'Threshold Period'. |
| 7 | `OD.RET.ACT.EXCESS.RETURNS` | `NacustOdReturnActivity_ExcessReturns` | TField |  | This field will be used to indicate that the account has excessively returned deposit. It will be flaged as Yes when the returned deposited items count breach threshold value. Allowed values are YES/NO. |
| 8 | `OD.RET.ACT.MONTH` | `NacustOdReturnActivity_Month` |  |  |  |
| 9 | `OD.RET.ACT.OD.DATE` | `NacustOdReturnActivity_OdDate` |  |  |  |
| 10 | `OD.RET.ACT.EXCESS.OD.DATE` | `NacustOdReturnActivity_ExcessOdDate` |  |  |  |
| 11 | `OD.RET.ACT.TOTAL.OD` | `NacustOdReturnActivity_TotalOd` |  |  |  |
| 12 | `OD.RET.ACT.RETURN.DATE` | `NacustOdReturnActivity_ReturnDate` |  |  |  |
| 13 | `OD.RET.ACT.TOT.RET.DATE` | `NacustOdReturnActivity_TotRetDate` |  |  |  |
| 14 | `OD.RET.ACT.TOTAL.RETURN` | `NacustOdReturnActivity_TotalReturn` |  |  |  |
| 15 | `OD.RET.ACT.RESERVED.15` | `NacustOdReturnActivity_Reserved15` | TField |  |  |
| 16 | `OD.RET.ACT.RESERVED.14` | `NacustOdReturnActivity_Reserved14` | TField |  |  |
| 17 | `OD.RET.ACT.RESERVED.13` | `NacustOdReturnActivity_Reserved13` | TField |  |  |
| 18 | `OD.RET.ACT.RESERVED.12` | `NacustOdReturnActivity_Reserved12` | TField |  |  |
| 19 | `OD.RET.ACT.RESERVED.11` | `NacustOdReturnActivity_Reserved11` | TField |  |  |
| 20 | `OD.RET.ACT.RESERVED.10` | `NacustOdReturnActivity_Reserved10` | TField |  |  |
| 21 | `OD.RET.ACT.RESERVED.9` | `NacustOdReturnActivity_Reserved9` | TField |  |  |
| 22 | `OD.RET.ACT.RESERVED.8` | `NacustOdReturnActivity_Reserved8` | TField |  |  |
| 23 | `OD.RET.ACT.RESERVED.7` | `NacustOdReturnActivity_Reserved7` | TField |  |  |
| 24 | `OD.RET.ACT.RESERVED.6` | `NacustOdReturnActivity_Reserved6` | TField |  |  |
| 25 | `OD.RET.ACT.RESERVED.5` | `NacustOdReturnActivity_Reserved5` | TField |  |  |
| 26 | `OD.RET.ACT.RESERVED.4` | `NacustOdReturnActivity_Reserved4` | TField |  |  |
| 27 | `OD.RET.ACT.RESERVED.3` | `NacustOdReturnActivity_Reserved3` | TField |  |  |
| 28 | `OD.RET.ACT.RESERVED.2` | `NacustOdReturnActivity_Reserved2` | TField |  |  |
| 29 | `OD.RET.ACT.RESERVED.1` | `NacustOdReturnActivity_Reserved1` | TField |  |  |
