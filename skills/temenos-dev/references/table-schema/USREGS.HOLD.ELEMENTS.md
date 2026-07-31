# USREGS.HOLD.ELEMENTS — Table Schema

> Source: `INSERTS/I_F.USREGS.HOLD.ELEMENTS` in `NACUST_CustomerHolds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HLD.ELEM.LARGE.DEPOSIT` | `UsregsHoldElements_LargeDeposit` | TField |  | This field is used to indicate whether there is any large deposit done. |
| 2 | `HLD.ELEM.NEW.ACCOUNT` | `UsregsHoldElements_NewAccount` | TField |  | This field is used to indicate whether the Account used for transaction is New account or not. |
| 3 | `HLD.ELEM.REPEAT.OD` | `UsregsHoldElements_RepeatOd` | TField |  | This field is used to indicate whether the Account used for transaction is Repeated overdraft or not. |
| 4 | `HLD.ELEM.STANDARD.HOLD` | `UsregsHoldElements_StandardHold` | TField |  | This field will be set as YES when the default condition of the parameter table USREGS.REGULATION.PARAM is applied. |
| 5 | `HLD.ELEM.EXCEPTION` | `UsregsHoldElements_Exception` | TField |  |  |
| 6 | `HLD.ELEM.IMMEDIATE` | `UsregsHoldElements_Immediate` |  |  |  |
| 7 | `HLD.ELEM.IMMEDIATE.DATE` | `UsregsHoldElements_ImmediateDate` |  |  |  |
| 8 | `HLD.ELEM.AMOUNT1` | `UsregsHoldElements_Amount1` |  |  |  |
| 9 | `HLD.ELEM.DATE1` | `UsregsHoldElements_Date1` |  |  |  |
| 10 | `HLD.ELEM.AMOUNT2` | `UsregsHoldElements_Amount2` |  |  |  |
| 11 | `HLD.ELEM.DATE2` | `UsregsHoldElements_Date2` |  |  |  |
| 12 | `HLD.ELEM.RESERVED.13` | `UsregsHoldElements_Reserved13` |  |  |  |
| 13 | `HLD.ELEM.RESERVED.12` | `UsregsHoldElements_Reserved12` |  |  |  |
| 14 | `HLD.ELEM.RESERVED.11` | `UsregsHoldElements_Reserved11` |  |  |  |
| 15 | `HLD.ELEM.ACC.NEXT` | `UsregsHoldElements_AccNext` | TField |  | This field is used to intimate the user that how much amount is next available to the customer. T24 Amount Field |
| 16 | `HLD.ELEM.AGR.CHECK.TOTAL` | `UsregsHoldElements_AgrCheckTotal` | TField |  |  |
| 17 | `HLD.ELEM.EXCESS.CHECK.RETURN` | `UsregsHoldElements_ExcessCheckReturn` | TField |  | This field is used to indicate whether the Account has exceeded return deposit count |
| 18 | `HLD.ELEM.RESERVED.8` | `UsregsHoldElements_Reserved8` | TField |  |  |
| 19 | `HLD.ELEM.RESERVED.7` | `UsregsHoldElements_Reserved7` | TField |  |  |
| 20 | `HLD.ELEM.RESERVED.6` | `UsregsHoldElements_Reserved6` | TField |  |  |
| 21 | `HLD.ELEM.RESERVED.5` | `UsregsHoldElements_Reserved5` | TField |  |  |
| 22 | `HLD.ELEM.RESERVED.4` | `UsregsHoldElements_Reserved4` | TField |  |  |
| 23 | `HLD.ELEM.RESERVED.3` | `UsregsHoldElements_Reserved3` | TField |  |  |
| 24 | `HLD.ELEM.RESERVED.2` | `UsregsHoldElements_Reserved2` | TField |  |  |
| 25 | `HLD.ELEM.RESERVED.1` | `UsregsHoldElements_Reserved1` | TField |  |  |
