# ID.ACCOUNT.CONDITION — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.CONDITION` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAC.DESCRIPTION` | `IdAccountCondition_Description` |  |  |  |
| 2 | `ID.IAC.EXCL.EVALUATION.CYCLE` | `IdAccountCondition_ExclEvaluationCycle` | TField |  | "Exclusion criteria" evaluation cycle used to evaluate the conditions configured. By default it allows "Monthly" as evaluation period. |
| 3 | `ID.IAC.COND.EVALUATION.PERIOD` | `IdAccountCondition_CondEvaluationPeriod` | TField |  | This field is used to setup the Minimum balance evaluation cycle. It can be set either as "Daily" or "Monthly". If it is set as "Daily" then minimum balance amount (MIN.BAL.AMOUNT) configured against each currency (CURRENCY) is evaluated on daily basis against the daily end of the balance in the Account. The account balance amount is considered as eligible for the day only if it satisfies the daily eligibility criteria. If it is set as "Monthly" then minimum balance amount (MIN.BAL.AMOUNT) configured against each currency (CURRENCY) is evaluated on monthly basis against the monthly minimum balance in the Account. The account balance amount is considered as eligible for the day only if it satisfies the monthly eligibility criteria. |
| 4 | `ID.IAC.PDS.CATEGORY.ID` | `IdAccountCondition_PdsCategoryId` | TField | Yes | This field is used to setup the link with the ID.PDS.CATEGORY parameter. Validation Rules: 1. Must be a valid record from ID.PDS.CATEGORY. 2. It is mandatory to setup the configuration in ID.PDS.CATEGORY with "U-CATEGORY" format. 3. Mandatory field for user input. |
| 5 | `ID.IAC.CURRENCY` | `IdAccountCondition_Currency` |  |  |  |
| 6 | `ID.IAC.MIN.BALANCE.AMOUNT` | `IdAccountCondition_MinBalanceAmount` |  |  |  |
| 7 | `ID.IAC.MIN.BAL.EVAL.START.DATE` | `IdAccountCondition_MinBalEvalStartDate` | TField |  | This field is used to choose whether the minimum balance evaluation should start from the Account opened date or Account funded value date. The Account can be funded on any other date than the account opened date.This option is applicable only during the Account opened month. "Account funded value date" can be selected if bank is willing to consider the account balance from the funded value date to calculate the minimum balance amount. |
| 8 | `ID.IAC.INITIATION` | `IdAccountCondition_Initiation` | TField |  | This field allows to capture the Transaction initiation owner for Transaction exclusion evaluation. By default, it is allowed to include the "Customer" initiated transactions for evaluation. The activities initiated by "Customer" from AA.ACTIVITY.HISTORY is selected for evaluation. |
| 9 | `ID.IAC.ACTIVITY.CLASS` | `IdAccountCondition_ActivityClass` | TField |  | This field is used to capture the debit activity to post accounting entries into the Account arrangement. By default it displays "ACCOUNTS-DEBIT-ARRANGEMENT" activity. The debit activities from AA.ACTIVITY.HISTORY is selected for evaluation. |
| 10 | `ID.IAC.ACTIVITY.DESCRIPTION` | `IdAccountCondition_ActivityDescription` |  |  |  |
| 11 | `ID.IAC.EXCLUDE.INDICATOR` | `IdAccountCondition_ExcludeIndicator` |  |  |  |
| 12 | `ID.IAC.TRAN.THRESHOLD.COUNT` | `IdAccountCondition_TranThresholdCount` | TField | Yes | This field is used to capture the threshold count for transaction count evaluation. Validation Rules: 1. Cannot hold negative values. 2. Cannot contain decimals. 3. It is mandatory to capture the number if ACTIVITY.CLASS is setup. |
| 13 | `ID.IAC.RESERVED.10` | `IdAccountCondition_Reserved10` |  |  |  |
| 14 | `ID.IAC.RESERVED.9` | `IdAccountCondition_Reserved9` | TField |  |  |
| 15 | `ID.IAC.RESERVED.8` | `IdAccountCondition_Reserved8` | TField |  |  |
| 16 | `ID.IAC.RESERVED.7` | `IdAccountCondition_Reserved7` | TField |  |  |
| 17 | `ID.IAC.RESERVED.6` | `IdAccountCondition_Reserved6` | TField |  |  |
| 18 | `ID.IAC.RESERVED.5` | `IdAccountCondition_Reserved5` | TField |  |  |
| 19 | `ID.IAC.RESERVED.4` | `IdAccountCondition_Reserved4` | TField |  |  |
| 20 | `ID.IAC.RESERVED.3` | `IdAccountCondition_Reserved3` | TField |  |  |
| 21 | `ID.IAC.RESERVED.2` | `IdAccountCondition_Reserved2` | TField |  |  |
| 22 | `ID.IAC.RESERVED.1` | `IdAccountCondition_Reserved1` | TField |  |  |
| 23 | `ID.IAC.LOCAL.REF` | `IdAccountCondition_LocalRef` |  |  |  |
| 24 | `ID.IAC.OVERRIDE` | `IdAccountCondition_Override` |  |  |  |
| 25 | `ID.IAC.RECORD.STATUS` | `IdAccountCondition_RecordStatus` | String |  |  |
| 26 | `ID.IAC.CURR.NO` | `IdAccountCondition_CurrNo` | String |  |  |
| 27 | `ID.IAC.INPUTTER` | `IdAccountCondition_Inputter` |  |  |  |
| 28 | `ID.IAC.DATE.TIME` | `IdAccountCondition_DateTime` |  |  |  |
| 29 | `ID.IAC.AUTHORISER` | `IdAccountCondition_Authoriser` | String |  |  |
| 30 | `ID.IAC.CO.CODE` | `IdAccountCondition_CoCode` | String |  |  |
| 31 | `ID.IAC.DEPT.CODE` | `IdAccountCondition_DeptCode` | String |  |  |
| 32 | `ID.IAC.AUDITOR.CODE` | `IdAccountCondition_AuditorCode` | String |  |  |
| 33 | `ID.IAC.AUDIT.DATE.TIME` | `IdAccountCondition_AuditDateTime` | String |  |  |
