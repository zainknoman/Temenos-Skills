# ACCOUNT.OVERDRAWN — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.OVERDRAWN` in `AC_BalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.OD.LIMIT.NARRATIVE` | `AccountOverdrawn_LimitNarrative` |  |  |  |
| 2 | `AC.OD.ACCOUNT.OFFICER` | `AccountOverdrawn_AccountOfficer` |  |  |  |
| 3 | `AC.OD.CUSTOMER` | `AccountOverdrawn_Customer` |  |  |  |
| 4 | `AC.OD.CURRENCY` | `AccountOverdrawn_Currency` |  |  |  |
| 5 | `AC.OD.CLRD.BAL.LIMIT` | `AccountOverdrawn_ClrdBalLimit` |  |  |  |
| 6 | `AC.OD.ACT.BAL.TOT.OUT` | `AccountOverdrawn_ActBalTotOut` |  |  |  |
| 7 | `AC.OD.DATE.FIRST.OD` | `AccountOverdrawn_DateFirstOd` |  |  |  |
| 8 | `AC.OD.DATE.LAST.MOVE` | `AccountOverdrawn_DateLastMove` |  |  |  |
| 9 | `AC.OD.OD.EXCESS.NARR` | `AccountOverdrawn_OdExcessNarr` |  |  |  |
| 10 | `AC.OD.MOVED.NARR` | `AccountOverdrawn_MovedNarr` |  |  |  |
| 11 | `AC.OD.CURR.OD.STATUS` | `AccountOverdrawn_CurrOdStatus` | TField |  | This field indicates the current overdraft status of the Account, This feature is currently available only for Arrangement Accounts. When the OD.PERIOD is set in Limit condition of an Arrangement Accounts, then based on this period Account will be moved to each status 'OD.STATUS' associated with the OD.PERIOD For each change in the overdraft status Arrangement Activity will be triggered, Charges and notifications can be attached to this activity. Validation Rules: No input. System generated field. |
| 12 | `AC.OD.PREV.OD.STATUS` | `AccountOverdrawn_PrevOdStatus` |  |  |  |
| 13 | `AC.OD.STATUS.CHANGE.ON` | `AccountOverdrawn_StatusChangeOn` |  |  |  |
| 14 | `AC.OD.CURR.OD.START.DATE` | `AccountOverdrawn_CurrOdStartDate` | TField |  | This field stores the date from account's balance fall below the Threshold amount setup in the Limit condition of the Arrangement Account. Validation Rules: No input. System generated field. |
| 15 | `AC.OD.CURR.OD.DAYS` | `AccountOverdrawn_CurrOdDays` | TField |  | This field stores number of days account is continuously in Overdraft below the Threshold amount setup in the Limit condition of the Arrangement Account. Validation Rules: No input. System generated field. |
| 16 | `AC.OD.OVERDRAWN.AMT` | `AccountOverdrawn_OverdrawnAmt` | TField |  | Current overdraft amount is stored in this field. Validation Rules: No input. System generated field. |
| 17 | `AC.OD.THRESHOLD.AMT` | `AccountOverdrawn_ThresholdAmt` | TField |  | Threshold amount in account or Limit currency is stored in this field. Validation Rules: No input. System generated field. |
| 18 | `AC.OD.OD.FEE.DATE` | `AccountOverdrawn_OdFeeDate` | TField |  | This field stores the date on which Customer Overdraft fee is collected. Validation Rules: No input. System generated field. |
| 19 | `AC.OD.RESERVED.5` | `AccountOverdrawn_Reserved5` | TField |  |  |
| 20 | `AC.OD.RESERVED.4` | `AccountOverdrawn_Reserved4` | TField |  |  |
| 21 | `AC.OD.RESERVED.3` | `AccountOverdrawn_Reserved3` | TField |  |  |
| 22 | `AC.OD.RESERVED.2` | `AccountOverdrawn_Reserved2` | TField |  |  |
| 23 | `AC.OD.RESERVED.1` | `AccountOverdrawn_Reserved1` | TField |  |  |
